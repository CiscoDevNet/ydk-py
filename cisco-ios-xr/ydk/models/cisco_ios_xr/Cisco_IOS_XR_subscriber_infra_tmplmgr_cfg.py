""" Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-infra\-tmplmgr package configuration.

This module contains definitions
for the following management objects\:
  dynamic\-template\: All dynamic template configurations

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DynamicTemplate(Entity):
    """
    All dynamic template configurations
    
    .. attribute:: ip_subscribers
    
    	The IP Subscriber Template Table
    	**type**\:   :py:class:`IpSubscribers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers>`
    
    .. attribute:: ppps
    
    	Templates of the PPP Type
    	**type**\:   :py:class:`Ppps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps>`
    
    .. attribute:: subscriber_services
    
    	The Service Type Template Table
    	**type**\:   :py:class:`SubscriberServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices>`
    
    

    """

    _prefix = 'subscriber-infra-tmplmgr-cfg'
    _revision = '2015-01-07'

    def __init__(self):
        super(DynamicTemplate, self).__init__()
        self._top_entity = None

        self.yang_name = "dynamic-template"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ip-subscribers" : ("ip_subscribers", DynamicTemplate.IpSubscribers), "ppps" : ("ppps", DynamicTemplate.Ppps), "subscriber-services" : ("subscriber_services", DynamicTemplate.SubscriberServices)}
        self._child_list_classes = {}

        self.ip_subscribers = DynamicTemplate.IpSubscribers()
        self.ip_subscribers.parent = self
        self._children_name_map["ip_subscribers"] = "ip-subscribers"
        self._children_yang_names.add("ip-subscribers")

        self.ppps = DynamicTemplate.Ppps()
        self.ppps.parent = self
        self._children_name_map["ppps"] = "ppps"
        self._children_yang_names.add("ppps")

        self.subscriber_services = DynamicTemplate.SubscriberServices()
        self.subscriber_services.parent = self
        self._children_name_map["subscriber_services"] = "subscriber-services"
        self._children_yang_names.add("subscriber-services")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template"


    class IpSubscribers(Entity):
        """
        The IP Subscriber Template Table
        
        .. attribute:: ip_subscriber
        
        	A IP Subscriber Type Template 
        	**type**\: list of    :py:class:`IpSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            super(DynamicTemplate.IpSubscribers, self).__init__()

            self.yang_name = "ip-subscribers"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ip-subscriber" : ("ip_subscriber", DynamicTemplate.IpSubscribers.IpSubscriber)}

            self.ip_subscriber = YList(self)
            self._segment_path = lambda: "ip-subscribers"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.IpSubscribers, [], name, value)


        class IpSubscriber(Entity):
            """
            A IP Subscriber Type Template 
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting>`
            
            .. attribute:: dhcpd
            
            	Interface dhcpv4 configuration data
            	**type**\:   :py:class:`Dhcpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd>`
            
            .. attribute:: dhcpv6
            
            	Interface dhcpv6 configuration data
            	**type**\:   :py:class:`Dhcpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6>`
            
            .. attribute:: igmp
            
            	IGMPconfiguration
            	**type**\:   :py:class:`Igmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp>`
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:   :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:   :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:   :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:   :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Pbr>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:   :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:   :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                super(DynamicTemplate.IpSubscribers.IpSubscriber, self).__init__()

                self.yang_name = "ip-subscriber"
                self.yang_parent_name = "ip-subscribers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"accounting" : ("accounting", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting), "dhcpd" : ("dhcpd", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd), "dhcpv6" : ("dhcpv6", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6), "igmp" : ("igmp", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp), "ipv4-network" : ("ipv4_network", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network), "ipv4-packet-filter" : ("ipv4_packet_filter", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter), "ipv6-neighbor" : ("ipv6_neighbor", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor), "ipv6-network" : ("ipv6_network", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network), "ipv6-packet-filter" : ("ipv6_packet_filter", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter), "pbr" : ("pbr", DynamicTemplate.IpSubscribers.IpSubscriber.Pbr), "qos" : ("qos", DynamicTemplate.IpSubscribers.IpSubscriber.Qos), "span-monitor-sessions" : ("span_monitor_sessions", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions)}
                self._child_list_classes = {}

                self.template_name = YLeaf(YType.str, "template-name")

                self.vrf = YLeaf(YType.str, "Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf")

                self.accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
                self._children_yang_names.add("accounting")

                self.dhcpd = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd()
                self.dhcpd.parent = self
                self._children_name_map["dhcpd"] = "dhcpd"
                self._children_yang_names.add("dhcpd")

                self.dhcpv6 = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6()
                self.dhcpv6.parent = self
                self._children_name_map["dhcpv6"] = "dhcpv6"
                self._children_yang_names.add("dhcpv6")

                self.igmp = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp()
                self.igmp.parent = self
                self._children_name_map["igmp"] = "igmp"
                self._children_yang_names.add("igmp")

                self.ipv4_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "ipv4-network"
                self._children_yang_names.add("ipv4-network")

                self.ipv4_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                self._children_yang_names.add("ipv4-packet-filter")

                self.ipv6_neighbor = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                self._children_yang_names.add("ipv6-neighbor")

                self.ipv6_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "ipv6-network"
                self._children_yang_names.add("ipv6-network")

                self.ipv6_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                self._children_yang_names.add("ipv6-packet-filter")

                self.pbr = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "pbr"
                self._children_yang_names.add("pbr")

                self.qos = DynamicTemplate.IpSubscribers.IpSubscriber.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "qos"
                self._children_yang_names.add("qos")

                self.span_monitor_sessions = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                self._children_yang_names.add("span-monitor-sessions")
                self._segment_path = lambda: "ip-subscriber" + "[template-name='" + self.template_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ip-subscribers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber, ['template_name', 'vrf'], name, value)


            class Accounting(Entity):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:   :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout>`
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\:  str
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session>`
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"idle-timeout" : ("idle_timeout", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout), "service-accounting" : ("service_accounting", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting), "session" : ("session", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session)}
                    self._child_list_classes = {}

                    self.prepaid_feature = YLeaf(YType.str, "prepaid-feature")

                    self.idle_timeout = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"
                    self._children_yang_names.add("idle-timeout")

                    self.service_accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                    self._children_yang_names.add("service-accounting")

                    self.session = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, ['prepaid_feature'], name, value)


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** 60..4320000
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                        self.timeout_value = YLeaf(YType.uint32, "timeout-value")
                        self._segment_path = lambda: "idle-timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, ['direction', 'threshold', 'timeout_value'], name, value)


                class ServiceAccounting(Entity):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: minute
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")
                        self._segment_path = lambda: "service-accounting"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, ['accounting_interim_interval', 'method_list_name'], name, value)


                class Session(Entity):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\:  str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")
                        self._segment_path = lambda: "session"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, ['dual_stack_delay', 'hold_acct_start', 'method_list_name', 'periodic_interval'], name, value)


            class Dhcpd(Entity):
                """
                Interface dhcpv4 configuration data
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\:  str
                
                .. attribute:: default_gateway
                
                	The Default Gateway IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: dhcpv4_option
                
                	Cisco VSA to configure any dhcp4 option per subscriber
                	**type**\:  str
                
                .. attribute:: session_limit
                
                	The pool to be used for Prefix Delegation
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'ipv4-dhcpd-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, self).__init__()

                    self.yang_name = "dhcpd"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.class_ = YLeaf(YType.str, "class")

                    self.default_gateway = YLeaf(YType.str, "default-gateway")

                    self.dhcpv4_option = YLeaf(YType.str, "dhcpv4-option")

                    self.session_limit = YLeaf(YType.int32, "session-limit")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg:dhcpd"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, ['class_', 'default_gateway', 'dhcpv4_option', 'session_limit'], name, value)


            class Dhcpv6(Entity):
                """
                Interface dhcpv6 configuration data
                
                .. attribute:: address_pool
                
                	The pool to be used for Address assignment
                	**type**\:  str
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\:  str
                
                .. attribute:: delegated_prefix
                
                	The prefix to be used for Prefix Delegation
                	**type**\:   :py:class:`DelegatedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: delegated_prefix_pool
                
                	The pool to be used for Prefix Delegation
                	**type**\:  str
                
                .. attribute:: dns_ipv6address
                
                	Dns IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mode_class
                
                	Select proxy/server profile based on mode class name
                	**type**\:  str
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, self).__init__()

                    self.yang_name = "dhcpv6"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"delegated-prefix" : ("delegated_prefix", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix)}
                    self._child_list_classes = {}

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.class_ = YLeaf(YType.str, "class")

                    self.delegated_prefix_pool = YLeaf(YType.str, "delegated-prefix-pool")

                    self.dns_ipv6address = YLeaf(YType.str, "dns-ipv6address")

                    self.mode_class = YLeaf(YType.str, "mode-class")

                    self.stateful_address = YLeaf(YType.str, "stateful-address")

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._children_yang_names.add("delegated-prefix")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, ['address_pool', 'class_', 'delegated_prefix_pool', 'dns_ipv6address', 'mode_class', 'stateful_address'], name, value)


                class DelegatedPrefix(Entity):
                    """
                    The prefix to be used for Prefix Delegation
                    
                    .. attribute:: prefix
                    
                    	IPv6 Prefix
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	PD Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, self).__init__()

                        self.yang_name = "delegated-prefix"
                        self.yang_parent_name = "dhcpv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "delegated-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, ['prefix', 'prefix_length'], name, value)


            class Igmp(Entity):
                """
                IGMPconfiguration
                
                .. attribute:: default_vrf
                
                	Default VRF
                	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf>`
                
                

                """

                _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp, self).__init__()

                    self.yang_name = "igmp"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"default-vrf" : ("default_vrf", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf)}
                    self._child_list_classes = {}

                    self.default_vrf = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._children_yang_names.add("default-vrf")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"


                class DefaultVrf(Entity):
                    """
                    Default VRF
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access\-list group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_groups
                    
                    	IGMP Max Groups
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: multicast_mode
                    
                    	Configure Multicast mode variable
                    	**type**\:   :py:class:`DynTmplMulticastMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg.DynTmplMulticastMode>`
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: version
                    
                    	IGMP Version
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, self).__init__()

                        self.yang_name = "default-vrf"
                        self.yang_parent_name = "igmp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking)}
                        self._child_list_classes = {}

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.max_groups = YLeaf(YType.uint32, "max-groups")

                        self.multicast_mode = YLeaf(YType.enumeration, "multicast-mode")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")
                        self._segment_path = lambda: "default-vrf"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, ['access_group', 'max_groups', 'multicast_mode', 'query_interval', 'query_max_response_time', 'version'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enable or disable, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "default-vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")
                            self._segment_path = lambda: "explicit-tracking"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, ['access_list_name', 'enable'], name, value)


            class Ipv4Network(Entity):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\:  int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\:  str
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, ['mtu', 'rpf', 'unnumbered', 'unreachables'], name, value)


            class Ipv4PacketFilter(Entity):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"


                class Inbound(Entity):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


            class Ipv6Neighbor(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:   :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:   :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\:  str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\:  int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:   :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\:  int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"duplicate-address-detection" : ("duplicate_address_detection", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection), "framed-prefix" : ("framed_prefix", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix), "ra-initial" : ("ra_initial", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial), "ra-interval" : ("ra_interval", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval)}
                    self._child_list_classes = {}

                    self.framed_prefix_pool = YLeaf(YType.str, "framed-prefix-pool")

                    self.managed_config = YLeaf(YType.empty, "managed-config")

                    self.ns_interval = YLeaf(YType.uint32, "ns-interval")

                    self.nud_enable = YLeaf(YType.empty, "nud-enable")

                    self.other_config = YLeaf(YType.empty, "other-config")

                    self.ra_lifetime = YLeaf(YType.uint32, "ra-lifetime")

                    self.ra_suppress = YLeaf(YType.empty, "ra-suppress")

                    self.ra_suppress_mtu = YLeaf(YType.empty, "ra-suppress-mtu")

                    self.ra_unicast = YLeaf(YType.empty, "ra-unicast")

                    self.ra_unspecify_hoplimit = YLeaf(YType.empty, "ra-unspecify-hoplimit")

                    self.reachable_time = YLeaf(YType.uint32, "reachable-time")

                    self.router_preference = YLeaf(YType.enumeration, "router-preference")

                    self.start_ra_on_ipv6_enable = YLeaf(YType.empty, "start-ra-on-ipv6-enable")

                    self.suppress_cache_learning = YLeaf(YType.empty, "suppress-cache-learning")

                    self.duplicate_address_detection = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                    self._children_yang_names.add("duplicate-address-detection")

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"
                    self._children_yang_names.add("framed-prefix")

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._children_yang_names.add("ra-initial")

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"
                    self._children_yang_names.add("ra-interval")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'ns_interval', 'nud_enable', 'other_config', 'ra_lifetime', 'ra_suppress', 'ra_suppress_mtu', 'ra_unicast', 'ra_unspecify_hoplimit', 'reachable_time', 'router_preference', 'start_ra_on_ipv6_enable', 'suppress_cache_learning'], name, value)


                class DuplicateAddressDetection(Entity):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.attempts = YLeaf(YType.uint32, "attempts")
                        self._segment_path = lambda: "duplicate-address-detection"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)


                class FramedPrefix(Entity):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "framed-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, ['prefix', 'prefix_length'], name, value)


                class RaInitial(Entity):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")
                        self._segment_path = lambda: "ra-initial"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)


                class RaInterval(Entity):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\:  int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")
                        self._segment_path = lambda: "ra-interval"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)


            class Ipv6Network(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\:  int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"addresses" : ("addresses", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses)}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(Entity):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auto-configuration" : ("auto_configuration", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration)}
                        self._child_list_classes = {}

                        self.auto_configuration = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")
                        self._segment_path = lambda: "addresses"


                    class AutoConfiguration(Entity):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "auto-configuration"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)


            class Ipv6PacketFilter(Entity):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"


                class Inbound(Entity):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


            class Pbr(Entity):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policy
                
                	PBR service policy configuration
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\:  str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"service-policy" : ("service_policy", DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy)}
                    self._child_list_classes = {}

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, ['service_policy_in'], name, value)


                class ServicePolicy(Entity):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.input = YLeaf(YType.str, "input")
                        self._segment_path = lambda: "service-policy"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy, ['input'], name, value)


            class Qos(Entity):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:   :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output>`
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"account" : ("account", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account), "output" : ("output", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output), "service-policy" : ("service_policy", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy)}
                    self._child_list_classes = {}

                    self.account = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"
                    self._children_yang_names.add("account")

                    self.output = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._children_yang_names.add("output")

                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"


                class Account(Entity):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")
                        self._segment_path = lambda: "account"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, ['aal', 'atm_cell_tax', 'encapsulation', 'user_defined'], name, value)


                class Output(Entity):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")
                        self._segment_path = lambda: "output"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, ['minimum_bandwidth'], name, value)


                class ServicePolicy(Entity):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"input" : ("input", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input), "output" : ("output", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output)}
                        self._child_list_classes = {}

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")
                        self._segment_path = lambda: "service-policy"


                    class Input(Entity):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "input"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


                    class Output(Entity):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


            class SpanMonitorSessions(Entity):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"span-monitor-session" : ("span_monitor_session", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession)}

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:   :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"acl" : ("acl", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl), "attachment" : ("attachment", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment)}
                        self._child_list_classes = {}

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._children_yang_names.add("acl")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + self.session_class.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Acl(Entity):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\:  str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.acl_enable = YLeaf(YType.empty, "acl-enable")

                            self.acl_name = YLeaf(YType.str, "acl-name")
                            self._segment_path = lambda: "acl"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)


                    class Attachment(Entity):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")
                            self._segment_path = lambda: "attachment"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, ['direction', 'port_level_enable', 'session_name'], name, value)


    class Ppps(Entity):
        """
        Templates of the PPP Type
        
        .. attribute:: ppp
        
        	A Template of the PPP Type
        	**type**\: list of    :py:class:`Ppp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            super(DynamicTemplate.Ppps, self).__init__()

            self.yang_name = "ppps"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ppp" : ("ppp", DynamicTemplate.Ppps.Ppp)}

            self.ppp = YList(self)
            self._segment_path = lambda: "ppps"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.Ppps, [], name, value)


        class Ppp(Entity):
            """
            A Template of the PPP Type
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting>`
            
            .. attribute:: dhcpv6
            
            	Interface dhcpv6 configuration data
            	**type**\:   :py:class:`Dhcpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Dhcpv6>`
            
            .. attribute:: igmp
            
            	IGMPconfiguration
            	**type**\:   :py:class:`Igmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp>`
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:   :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4Network>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:   :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:   :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:   :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Pbr>`
            
            .. attribute:: ppp_template
            
            	PPP template configuration data
            	**type**\:   :py:class:`PppTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate>`
            
            .. attribute:: pppoe_template
            
            	PPPoE template configuration data
            	**type**\:   :py:class:`PppoeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppoeTemplate>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:   :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:   :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                super(DynamicTemplate.Ppps.Ppp, self).__init__()

                self.yang_name = "ppp"
                self.yang_parent_name = "ppps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"accounting" : ("accounting", DynamicTemplate.Ppps.Ppp.Accounting), "dhcpv6" : ("dhcpv6", DynamicTemplate.Ppps.Ppp.Dhcpv6), "igmp" : ("igmp", DynamicTemplate.Ppps.Ppp.Igmp), "ipv4-network" : ("ipv4_network", DynamicTemplate.Ppps.Ppp.Ipv4Network), "ipv4-packet-filter" : ("ipv4_packet_filter", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter), "ipv6-neighbor" : ("ipv6_neighbor", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor), "ipv6-network" : ("ipv6_network", DynamicTemplate.Ppps.Ppp.Ipv6Network), "ipv6-packet-filter" : ("ipv6_packet_filter", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter), "pbr" : ("pbr", DynamicTemplate.Ppps.Ppp.Pbr), "ppp-template" : ("ppp_template", DynamicTemplate.Ppps.Ppp.PppTemplate), "pppoe-template" : ("pppoe_template", DynamicTemplate.Ppps.Ppp.PppoeTemplate), "qos" : ("qos", DynamicTemplate.Ppps.Ppp.Qos), "span-monitor-sessions" : ("span_monitor_sessions", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions)}
                self._child_list_classes = {}

                self.template_name = YLeaf(YType.str, "template-name")

                self.vrf = YLeaf(YType.str, "Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf")

                self.accounting = DynamicTemplate.Ppps.Ppp.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
                self._children_yang_names.add("accounting")

                self.dhcpv6 = DynamicTemplate.Ppps.Ppp.Dhcpv6()
                self.dhcpv6.parent = self
                self._children_name_map["dhcpv6"] = "dhcpv6"
                self._children_yang_names.add("dhcpv6")

                self.igmp = DynamicTemplate.Ppps.Ppp.Igmp()
                self.igmp.parent = self
                self._children_name_map["igmp"] = "igmp"
                self._children_yang_names.add("igmp")

                self.ipv4_network = DynamicTemplate.Ppps.Ppp.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "ipv4-network"
                self._children_yang_names.add("ipv4-network")

                self.ipv4_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                self._children_yang_names.add("ipv4-packet-filter")

                self.ipv6_neighbor = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                self._children_yang_names.add("ipv6-neighbor")

                self.ipv6_network = DynamicTemplate.Ppps.Ppp.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "ipv6-network"
                self._children_yang_names.add("ipv6-network")

                self.ipv6_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                self._children_yang_names.add("ipv6-packet-filter")

                self.pbr = DynamicTemplate.Ppps.Ppp.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "pbr"
                self._children_yang_names.add("pbr")

                self.ppp_template = DynamicTemplate.Ppps.Ppp.PppTemplate()
                self.ppp_template.parent = self
                self._children_name_map["ppp_template"] = "ppp-template"
                self._children_yang_names.add("ppp-template")

                self.pppoe_template = DynamicTemplate.Ppps.Ppp.PppoeTemplate()
                self.pppoe_template.parent = self
                self._children_name_map["pppoe_template"] = "pppoe-template"
                self._children_yang_names.add("pppoe-template")

                self.qos = DynamicTemplate.Ppps.Ppp.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "qos"
                self._children_yang_names.add("qos")

                self.span_monitor_sessions = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                self._children_yang_names.add("span-monitor-sessions")
                self._segment_path = lambda: "ppp" + "[template-name='" + self.template_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ppps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.Ppps.Ppp, ['template_name', 'vrf'], name, value)


            class Accounting(Entity):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:   :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout>`
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\:  str
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.Session>`
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"idle-timeout" : ("idle_timeout", DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout), "service-accounting" : ("service_accounting", DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting), "session" : ("session", DynamicTemplate.Ppps.Ppp.Accounting.Session)}
                    self._child_list_classes = {}

                    self.prepaid_feature = YLeaf(YType.str, "prepaid-feature")

                    self.idle_timeout = DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"
                    self._children_yang_names.add("idle-timeout")

                    self.service_accounting = DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                    self._children_yang_names.add("service-accounting")

                    self.session = DynamicTemplate.Ppps.Ppp.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting, ['prepaid_feature'], name, value)


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** 60..4320000
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                        self.timeout_value = YLeaf(YType.uint32, "timeout-value")
                        self._segment_path = lambda: "idle-timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, ['direction', 'threshold', 'timeout_value'], name, value)


                class ServiceAccounting(Entity):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")
                        self._segment_path = lambda: "service-accounting"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, ['accounting_interim_interval', 'method_list_name'], name, value)


                class Session(Entity):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\:  str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")
                        self._segment_path = lambda: "session"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.Session, ['dual_stack_delay', 'hold_acct_start', 'method_list_name', 'periodic_interval'], name, value)


            class Dhcpv6(Entity):
                """
                Interface dhcpv6 configuration data
                
                .. attribute:: address_pool
                
                	The pool to be used for Address assignment
                	**type**\:  str
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\:  str
                
                .. attribute:: delegated_prefix
                
                	The prefix to be used for Prefix Delegation
                	**type**\:   :py:class:`DelegatedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: delegated_prefix_pool
                
                	The pool to be used for Prefix Delegation
                	**type**\:  str
                
                .. attribute:: dns_ipv6address
                
                	Dns IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mode_class
                
                	Select proxy/server profile based on mode class name
                	**type**\:  str
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Dhcpv6, self).__init__()

                    self.yang_name = "dhcpv6"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"delegated-prefix" : ("delegated_prefix", DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix)}
                    self._child_list_classes = {}

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.class_ = YLeaf(YType.str, "class")

                    self.delegated_prefix_pool = YLeaf(YType.str, "delegated-prefix-pool")

                    self.dns_ipv6address = YLeaf(YType.str, "dns-ipv6address")

                    self.mode_class = YLeaf(YType.str, "mode-class")

                    self.stateful_address = YLeaf(YType.str, "stateful-address")

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._children_yang_names.add("delegated-prefix")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Dhcpv6, ['address_pool', 'class_', 'delegated_prefix_pool', 'dns_ipv6address', 'mode_class', 'stateful_address'], name, value)


                class DelegatedPrefix(Entity):
                    """
                    The prefix to be used for Prefix Delegation
                    
                    .. attribute:: prefix
                    
                    	IPv6 Prefix
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	PD Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, self).__init__()

                        self.yang_name = "delegated-prefix"
                        self.yang_parent_name = "dhcpv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "delegated-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, ['prefix', 'prefix_length'], name, value)


            class Igmp(Entity):
                """
                IGMPconfiguration
                
                .. attribute:: default_vrf
                
                	Default VRF
                	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf>`
                
                

                """

                _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Igmp, self).__init__()

                    self.yang_name = "igmp"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"default-vrf" : ("default_vrf", DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf)}
                    self._child_list_classes = {}

                    self.default_vrf = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._children_yang_names.add("default-vrf")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"


                class DefaultVrf(Entity):
                    """
                    Default VRF
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access\-list group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_groups
                    
                    	IGMP Max Groups
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: multicast_mode
                    
                    	Configure Multicast mode variable
                    	**type**\:   :py:class:`DynTmplMulticastMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg.DynTmplMulticastMode>`
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: version
                    
                    	IGMP Version
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, self).__init__()

                        self.yang_name = "default-vrf"
                        self.yang_parent_name = "igmp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking)}
                        self._child_list_classes = {}

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.max_groups = YLeaf(YType.uint32, "max-groups")

                        self.multicast_mode = YLeaf(YType.enumeration, "multicast-mode")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")
                        self._segment_path = lambda: "default-vrf"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, ['access_group', 'max_groups', 'multicast_mode', 'query_interval', 'query_max_response_time', 'version'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enable or disable, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "default-vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")
                            self._segment_path = lambda: "explicit-tracking"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, ['access_list_name', 'enable'], name, value)


            class Ipv4Network(Entity):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\:  int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\:  str
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4Network, ['mtu', 'rpf', 'unnumbered', 'unreachables'], name, value)


            class Ipv4PacketFilter(Entity):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"


                class Inbound(Entity):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


            class Ipv6Neighbor(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:   :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:   :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\:  str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\:  int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:   :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\:  int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"duplicate-address-detection" : ("duplicate_address_detection", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection), "framed-prefix" : ("framed_prefix", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix), "ra-initial" : ("ra_initial", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial), "ra-interval" : ("ra_interval", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval)}
                    self._child_list_classes = {}

                    self.framed_prefix_pool = YLeaf(YType.str, "framed-prefix-pool")

                    self.managed_config = YLeaf(YType.empty, "managed-config")

                    self.ns_interval = YLeaf(YType.uint32, "ns-interval")

                    self.nud_enable = YLeaf(YType.empty, "nud-enable")

                    self.other_config = YLeaf(YType.empty, "other-config")

                    self.ra_lifetime = YLeaf(YType.uint32, "ra-lifetime")

                    self.ra_suppress = YLeaf(YType.empty, "ra-suppress")

                    self.ra_suppress_mtu = YLeaf(YType.empty, "ra-suppress-mtu")

                    self.ra_unicast = YLeaf(YType.empty, "ra-unicast")

                    self.ra_unspecify_hoplimit = YLeaf(YType.empty, "ra-unspecify-hoplimit")

                    self.reachable_time = YLeaf(YType.uint32, "reachable-time")

                    self.router_preference = YLeaf(YType.enumeration, "router-preference")

                    self.start_ra_on_ipv6_enable = YLeaf(YType.empty, "start-ra-on-ipv6-enable")

                    self.suppress_cache_learning = YLeaf(YType.empty, "suppress-cache-learning")

                    self.duplicate_address_detection = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                    self._children_yang_names.add("duplicate-address-detection")

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"
                    self._children_yang_names.add("framed-prefix")

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._children_yang_names.add("ra-initial")

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"
                    self._children_yang_names.add("ra-interval")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'ns_interval', 'nud_enable', 'other_config', 'ra_lifetime', 'ra_suppress', 'ra_suppress_mtu', 'ra_unicast', 'ra_unspecify_hoplimit', 'reachable_time', 'router_preference', 'start_ra_on_ipv6_enable', 'suppress_cache_learning'], name, value)


                class DuplicateAddressDetection(Entity):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.attempts = YLeaf(YType.uint32, "attempts")
                        self._segment_path = lambda: "duplicate-address-detection"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)


                class FramedPrefix(Entity):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "framed-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, ['prefix', 'prefix_length'], name, value)


                class RaInitial(Entity):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")
                        self._segment_path = lambda: "ra-initial"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)


                class RaInterval(Entity):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\:  int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")
                        self._segment_path = lambda: "ra-interval"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)


            class Ipv6Network(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\:  int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"addresses" : ("addresses", DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses)}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(Entity):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auto-configuration" : ("auto_configuration", DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration)}
                        self._child_list_classes = {}

                        self.auto_configuration = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")
                        self._segment_path = lambda: "addresses"


                    class AutoConfiguration(Entity):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "auto-configuration"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)


            class Ipv6PacketFilter(Entity):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"


                class Inbound(Entity):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


            class Pbr(Entity):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policy
                
                	PBR service policy configuration
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\:  str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"service-policy" : ("service_policy", DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy)}
                    self._child_list_classes = {}

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Pbr, ['service_policy_in'], name, value)


                class ServicePolicy(Entity):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.input = YLeaf(YType.str, "input")
                        self._segment_path = lambda: "service-policy"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy, ['input'], name, value)


            class PppTemplate(Entity):
                """
                PPP template configuration data
                
                .. attribute:: fsm
                
                	PPP FSM global template configuration data
                	**type**\:   :py:class:`Fsm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm>`
                
                .. attribute:: ipcp
                
                	PPP IPCP global template configuration data
                	**type**\:   :py:class:`Ipcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp>`
                
                .. attribute:: ipv6cp
                
                	PPP IPv6CP global template configuration data
                	**type**\:   :py:class:`Ipv6Cp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp>`
                
                .. attribute:: lcp
                
                	PPP LCP global template configuration data
                	**type**\:   :py:class:`Lcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp>`
                
                

                """

                _prefix = 'ppp-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.PppTemplate, self).__init__()

                    self.yang_name = "ppp-template"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"fsm" : ("fsm", DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm), "ipcp" : ("ipcp", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp), "ipv6cp" : ("ipv6cp", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp), "lcp" : ("lcp", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp)}
                    self._child_list_classes = {}

                    self.fsm = DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm()
                    self.fsm.parent = self
                    self._children_name_map["fsm"] = "fsm"
                    self._children_yang_names.add("fsm")

                    self.ipcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp()
                    self.ipcp.parent = self
                    self._children_name_map["ipcp"] = "ipcp"
                    self._children_yang_names.add("ipcp")

                    self.ipv6cp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp()
                    self.ipv6cp.parent = self
                    self._children_name_map["ipv6cp"] = "ipv6cp"
                    self._children_yang_names.add("ipv6cp")

                    self.lcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp()
                    self.lcp.parent = self
                    self._children_name_map["lcp"] = "lcp"
                    self._children_yang_names.add("lcp")
                    self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-gbl-cfg:ppp-template"


                class Fsm(Entity):
                    """
                    PPP FSM global template configuration data
                    
                    .. attribute:: max_consecutive_conf_naks
                    
                    	This specifies the maximum number of consecutive Conf\-Naks
                    	**type**\:  int
                    
                    	**range:** 2..10
                    
                    	**default value**\: 5
                    
                    .. attribute:: max_unacknowledged_conf_requests
                    
                    	This specifies the maximum number of unacknowledged Conf\-Requests
                    	**type**\:  int
                    
                    	**range:** 4..20
                    
                    	**default value**\: 10
                    
                    .. attribute:: protocol_reject_timeout
                    
                    	This specifies the maximum time to wait before sending Protocol Reject
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**default value**\: 60
                    
                    .. attribute:: retry_timeout
                    
                    	This specifies the maximum time to wait for a response during PPP negotiation
                    	**type**\:  int
                    
                    	**range:** 1..10
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, self).__init__()

                        self.yang_name = "fsm"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.max_consecutive_conf_naks = YLeaf(YType.uint32, "max-consecutive-conf-naks")

                        self.max_unacknowledged_conf_requests = YLeaf(YType.uint32, "max-unacknowledged-conf-requests")

                        self.protocol_reject_timeout = YLeaf(YType.uint32, "protocol-reject-timeout")

                        self.retry_timeout = YLeaf(YType.uint32, "retry-timeout")
                        self._segment_path = lambda: "fsm"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, ['max_consecutive_conf_naks', 'max_unacknowledged_conf_requests', 'protocol_reject_timeout', 'retry_timeout'], name, value)


                class Ipcp(Entity):
                    """
                    PPP IPCP global template configuration data
                    
                    .. attribute:: dns
                    
                    	IPCP DNS parameters
                    	**type**\:   :py:class:`Dns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns>`
                    
                    .. attribute:: passive
                    
                    	Specify whether to run IPCP in Passive mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_address
                    
                    	IPCP address parameters
                    	**type**\:   :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress>`
                    
                    .. attribute:: peer_netmask
                    
                    	Specify the IPv4 netmask to negotiate for the peer
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: protocol_reject
                    
                    	Specify whether to protocol reject IPCP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate IPCP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: wins
                    
                    	IPCP WINS parameters
                    	**type**\:   :py:class:`Wins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins>`
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, self).__init__()

                        self.yang_name = "ipcp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"dns" : ("dns", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns), "peer-address" : ("peer_address", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress), "wins" : ("wins", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins)}
                        self._child_list_classes = {}

                        self.passive = YLeaf(YType.empty, "passive")

                        self.peer_netmask = YLeaf(YType.str, "peer-netmask")

                        self.protocol_reject = YLeaf(YType.empty, "protocol-reject")

                        self.renegotiation = YLeaf(YType.empty, "renegotiation")

                        self.dns = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns()
                        self.dns.parent = self
                        self._children_name_map["dns"] = "dns"
                        self._children_yang_names.add("dns")

                        self.peer_address = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress()
                        self.peer_address.parent = self
                        self._children_name_map["peer_address"] = "peer-address"
                        self._children_yang_names.add("peer-address")

                        self.wins = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins()
                        self.wins.parent = self
                        self._children_name_map["wins"] = "wins"
                        self._children_yang_names.add("wins")
                        self._segment_path = lambda: "ipcp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, ['passive', 'peer_netmask', 'protocol_reject', 'renegotiation'], name, value)


                    class Dns(Entity):
                        """
                        IPCP DNS parameters
                        
                        .. attribute:: dns_addresses
                        
                        	Specify DNS address(es) to provide
                        	**type**\:   :py:class:`DnsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses>`
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns, self).__init__()

                            self.yang_name = "dns"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"dns-addresses" : ("dns_addresses", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses)}
                            self._child_list_classes = {}

                            self.dns_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses()
                            self.dns_addresses.parent = self
                            self._children_name_map["dns_addresses"] = "dns-addresses"
                            self._children_yang_names.add("dns-addresses")
                            self._segment_path = lambda: "dns"


                        class DnsAddresses(Entity):
                            """
                            Specify DNS address(es) to provide
                            
                            .. attribute:: primary
                            
                            	Primary DNS IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary
                            
                            	Secondary DNS IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, self).__init__()

                                self.yang_name = "dns-addresses"
                                self.yang_parent_name = "dns"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")
                                self._segment_path = lambda: "dns-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, ['primary', 'secondary'], name, value)


                    class PeerAddress(Entity):
                        """
                        IPCP address parameters
                        
                        .. attribute:: default
                        
                        	Specify an IP address to assign to peers through IPCP
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: pool
                        
                        	Accepts an IP address from the peer if in the pool, else allocates one from the pool
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.default = YLeaf(YType.str, "default")

                            self.pool = YLeaf(YType.str, "pool")
                            self._segment_path = lambda: "peer-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, ['default', 'pool'], name, value)


                    class Wins(Entity):
                        """
                        IPCP WINS parameters
                        
                        .. attribute:: wins_addresses
                        
                        	Specify WINS address(es) to provide
                        	**type**\:   :py:class:`WinsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses>`
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins, self).__init__()

                            self.yang_name = "wins"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"wins-addresses" : ("wins_addresses", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses)}
                            self._child_list_classes = {}

                            self.wins_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses()
                            self.wins_addresses.parent = self
                            self._children_name_map["wins_addresses"] = "wins-addresses"
                            self._children_yang_names.add("wins-addresses")
                            self._segment_path = lambda: "wins"


                        class WinsAddresses(Entity):
                            """
                            Specify WINS address(es) to provide
                            
                            .. attribute:: primary
                            
                            	Primary WINS IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary
                            
                            	Secondary WINS IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, self).__init__()

                                self.yang_name = "wins-addresses"
                                self.yang_parent_name = "wins"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")
                                self._segment_path = lambda: "wins-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, ['primary', 'secondary'], name, value)


                class Ipv6Cp(Entity):
                    """
                    PPP IPv6CP global template configuration data
                    
                    .. attribute:: passive
                    
                    	Specify whether to run IPv6CP in Passive mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_interface_id
                    
                    	Specify the Interface\-Id to impose on the peer
                    	**type**\:  str
                    
                    .. attribute:: protocol_reject
                    
                    	Specify whether to protocol reject IPv6CP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate IPv6CP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp, self).__init__()

                        self.yang_name = "ipv6cp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.passive = YLeaf(YType.empty, "passive")

                        self.peer_interface_id = YLeaf(YType.str, "peer-interface-id")

                        self.protocol_reject = YLeaf(YType.empty, "protocol-reject")

                        self.renegotiation = YLeaf(YType.empty, "renegotiation")
                        self._segment_path = lambda: "ipv6cp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp, ['passive', 'peer_interface_id', 'protocol_reject', 'renegotiation'], name, value)


                class Lcp(Entity):
                    """
                    PPP LCP global template configuration data
                    
                    .. attribute:: absolute_timeout
                    
                    	This specifies the session absolute timeout value
                    	**type**\:   :py:class:`AbsoluteTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout>`
                    
                    .. attribute:: authentication
                    
                    	PPP authentication parameters
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication>`
                    
                    .. attribute:: delay
                    
                    	This specifies the time to delay before starting active LCPnegotiations
                    	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay>`
                    
                    .. attribute:: keepalive
                    
                    	This specifies the rate at which EchoReq packets are sent
                    	**type**\:   :py:class:`Keepalive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive>`
                    
                    .. attribute:: mru_ignore
                    
                    	Ignore MRU negotiated with peer while setting interface BW
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate LCP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: send_term_request_on_shut_down
                    
                    	Enable Sending LCP Terminate request on shutdown
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: service_type
                    
                    	This is the Service\-Type
                    	**type**\:  int
                    
                    	**range:** 0..15
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, self).__init__()

                        self.yang_name = "lcp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"absolute-timeout" : ("absolute_timeout", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout), "authentication" : ("authentication", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication), "delay" : ("delay", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay), "keepalive" : ("keepalive", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive)}
                        self._child_list_classes = {}

                        self.mru_ignore = YLeaf(YType.empty, "mru-ignore")

                        self.renegotiation = YLeaf(YType.empty, "renegotiation")

                        self.send_term_request_on_shut_down = YLeaf(YType.empty, "send-term-request-on-shut-down")

                        self.service_type = YLeaf(YType.uint32, "service-type")

                        self.absolute_timeout = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout()
                        self.absolute_timeout.parent = self
                        self._children_name_map["absolute_timeout"] = "absolute-timeout"
                        self._children_yang_names.add("absolute-timeout")

                        self.authentication = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                        self.delay = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay()
                        self.delay.parent = self
                        self._children_name_map["delay"] = "delay"
                        self._children_yang_names.add("delay")

                        self.keepalive = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive()
                        self.keepalive.parent = self
                        self._children_name_map["keepalive"] = "keepalive"
                        self._children_yang_names.add("keepalive")
                        self._segment_path = lambda: "lcp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, ['mru_ignore', 'renegotiation', 'send_term_request_on_shut_down', 'service_type'], name, value)


                    class AbsoluteTimeout(Entity):
                        """
                        This specifies the session absolute timeout
                        value
                        
                        .. attribute:: minutes
                        
                        	Minutes
                        	**type**\:  int
                        
                        	**range:** 0..35000000
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, self).__init__()

                            self.yang_name = "absolute-timeout"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.minutes = YLeaf(YType.uint32, "minutes")

                            self.seconds = YLeaf(YType.uint32, "seconds")
                            self._segment_path = lambda: "absolute-timeout"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, ['minutes', 'seconds'], name, value)


                    class Authentication(Entity):
                        """
                        PPP authentication parameters
                        
                        .. attribute:: chap_host_name
                        
                        	This specifies the CHAP hostname
                        	**type**\:  str
                        
                        .. attribute:: max_authentication_failures
                        
                        	This specifies whether to allow multiple authentication failures and, if so, how many
                        	**type**\:  int
                        
                        	**range:** 0..10
                        
                        .. attribute:: methods
                        
                        	This specifies the PPP link authentication method
                        	**type**\:   :py:class:`Methods <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods>`
                        
                        .. attribute:: mschap_host_name
                        
                        	This specifies the MS\-CHAP hostname
                        	**type**\:  str
                        
                        .. attribute:: pap
                        
                        	<1> for accepting null\-passwordduring authentication
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: timeout
                        
                        	Maximum time to wait for an authentication response
                        	**type**\:  int
                        
                        	**range:** 3..30
                        
                        	**default value**\: 10
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"methods" : ("methods", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods)}
                            self._child_list_classes = {}

                            self.chap_host_name = YLeaf(YType.str, "chap-host-name")

                            self.max_authentication_failures = YLeaf(YType.uint32, "max-authentication-failures")

                            self.mschap_host_name = YLeaf(YType.str, "mschap-host-name")

                            self.pap = YLeaf(YType.int32, "pap")

                            self.timeout = YLeaf(YType.uint32, "timeout")

                            self.methods = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods()
                            self.methods.parent = self
                            self._children_name_map["methods"] = "methods"
                            self._children_yang_names.add("methods")
                            self._segment_path = lambda: "authentication"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, ['chap_host_name', 'max_authentication_failures', 'mschap_host_name', 'pap', 'timeout'], name, value)


                        class Methods(Entity):
                            """
                            This specifies the PPP link authentication
                            method
                            
                            .. attribute:: method
                            
                            	Select between one and three authentication methods in order of preference
                            	**type**\:  list of   :py:class:`PppAuthenticationMethodGbl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_gbl_cfg.PppAuthenticationMethodGbl>`
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, self).__init__()

                                self.yang_name = "methods"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.method = YLeafList(YType.enumeration, "method")
                                self._segment_path = lambda: "methods"

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, ['method'], name, value)


                    class Delay(Entity):
                        """
                        This specifies the time to delay before
                        starting active LCPnegotiations
                        
                        .. attribute:: milliseconds
                        
                        	Milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..999
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, self).__init__()

                            self.yang_name = "delay"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.milliseconds = YLeaf(YType.uint32, "milliseconds")

                            self.seconds = YLeaf(YType.uint32, "seconds")
                            self._segment_path = lambda: "delay"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, ['milliseconds', 'seconds'], name, value)


                    class Keepalive(Entity):
                        """
                        This specifies the rate at which EchoReq
                        packets are sent
                        
                        .. attribute:: interval
                        
                        	The keepalive interval. Leave unspecified when disabling keepalives
                        	**type**\:  int
                        
                        	**range:** 10..180
                        
                        .. attribute:: keepalive_disable
                        
                        	TRUE to disable keepalives, FALSE to specify a new keepalive interval
                        	**type**\:  bool
                        
                        .. attribute:: retry_count
                        
                        	The keepalive retry count. Leave unspecified when disabling keepalives
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, self).__init__()

                            self.yang_name = "keepalive"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.keepalive_disable = YLeaf(YType.boolean, "keepalive-disable")

                            self.retry_count = YLeaf(YType.uint32, "retry-count")
                            self._segment_path = lambda: "keepalive"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, ['interval', 'keepalive_disable', 'retry_count'], name, value)


            class PppoeTemplate(Entity):
                """
                PPPoE template configuration data
                
                .. attribute:: port_limit
                
                	Specify the Port limit (attr 62) to apply to the subscriber
                	**type**\:  int
                
                	**range:** 1..65535
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.PppoeTemplate, self).__init__()

                    self.yang_name = "pppoe-template"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.port_limit = YLeaf(YType.uint16, "port-limit")
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-template"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppoeTemplate, ['port_limit'], name, value)


            class Qos(Entity):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:   :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.Output>`
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"account" : ("account", DynamicTemplate.Ppps.Ppp.Qos.Account), "output" : ("output", DynamicTemplate.Ppps.Ppp.Qos.Output), "service-policy" : ("service_policy", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy)}
                    self._child_list_classes = {}

                    self.account = DynamicTemplate.Ppps.Ppp.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"
                    self._children_yang_names.add("account")

                    self.output = DynamicTemplate.Ppps.Ppp.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._children_yang_names.add("output")

                    self.service_policy = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"


                class Account(Entity):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")
                        self._segment_path = lambda: "account"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.Account, ['aal', 'atm_cell_tax', 'encapsulation', 'user_defined'], name, value)


                class Output(Entity):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")
                        self._segment_path = lambda: "output"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.Output, ['minimum_bandwidth'], name, value)


                class ServicePolicy(Entity):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"input" : ("input", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input), "output" : ("output", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output)}
                        self._child_list_classes = {}

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")
                        self._segment_path = lambda: "service-policy"


                    class Input(Entity):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "input"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


                    class Output(Entity):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


            class SpanMonitorSessions(Entity):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"span-monitor-session" : ("span_monitor_session", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession)}

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:   :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"acl" : ("acl", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl), "attachment" : ("attachment", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment)}
                        self._child_list_classes = {}

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._children_yang_names.add("acl")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + self.session_class.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Acl(Entity):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\:  str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.acl_enable = YLeaf(YType.empty, "acl-enable")

                            self.acl_name = YLeaf(YType.str, "acl-name")
                            self._segment_path = lambda: "acl"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)


                    class Attachment(Entity):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")
                            self._segment_path = lambda: "attachment"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, ['direction', 'port_level_enable', 'session_name'], name, value)


    class SubscriberServices(Entity):
        """
        The Service Type Template Table
        
        .. attribute:: subscriber_service
        
        	A Service Type Template 
        	**type**\: list of    :py:class:`SubscriberService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            super(DynamicTemplate.SubscriberServices, self).__init__()

            self.yang_name = "subscriber-services"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"subscriber-service" : ("subscriber_service", DynamicTemplate.SubscriberServices.SubscriberService)}

            self.subscriber_service = YList(self)
            self._segment_path = lambda: "subscriber-services"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.SubscriberServices, [], name, value)


        class SubscriberService(Entity):
            """
            A Service Type Template 
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting>`
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:   :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:   :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:   :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:   :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:   :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Pbr>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:   :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:   :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                super(DynamicTemplate.SubscriberServices.SubscriberService, self).__init__()

                self.yang_name = "subscriber-service"
                self.yang_parent_name = "subscriber-services"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"accounting" : ("accounting", DynamicTemplate.SubscriberServices.SubscriberService.Accounting), "ipv4-network" : ("ipv4_network", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network), "ipv4-packet-filter" : ("ipv4_packet_filter", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter), "ipv6-neighbor" : ("ipv6_neighbor", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor), "ipv6-network" : ("ipv6_network", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network), "ipv6-packet-filter" : ("ipv6_packet_filter", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter), "pbr" : ("pbr", DynamicTemplate.SubscriberServices.SubscriberService.Pbr), "qos" : ("qos", DynamicTemplate.SubscriberServices.SubscriberService.Qos), "span-monitor-sessions" : ("span_monitor_sessions", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions)}
                self._child_list_classes = {}

                self.template_name = YLeaf(YType.str, "template-name")

                self.vrf = YLeaf(YType.str, "Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf")

                self.accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
                self._children_yang_names.add("accounting")

                self.ipv4_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "ipv4-network"
                self._children_yang_names.add("ipv4-network")

                self.ipv4_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                self._children_yang_names.add("ipv4-packet-filter")

                self.ipv6_neighbor = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                self._children_yang_names.add("ipv6-neighbor")

                self.ipv6_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "ipv6-network"
                self._children_yang_names.add("ipv6-network")

                self.ipv6_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                self._children_yang_names.add("ipv6-packet-filter")

                self.pbr = DynamicTemplate.SubscriberServices.SubscriberService.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "pbr"
                self._children_yang_names.add("pbr")

                self.qos = DynamicTemplate.SubscriberServices.SubscriberService.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "qos"
                self._children_yang_names.add("qos")

                self.span_monitor_sessions = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                self._children_yang_names.add("span-monitor-sessions")
                self._segment_path = lambda: "subscriber-service" + "[template-name='" + self.template_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/subscriber-services/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService, ['template_name', 'vrf'], name, value)


            class Accounting(Entity):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:   :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout>`
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\:  str
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session>`
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"idle-timeout" : ("idle_timeout", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout), "service-accounting" : ("service_accounting", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting), "session" : ("session", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session)}
                    self._child_list_classes = {}

                    self.prepaid_feature = YLeaf(YType.str, "prepaid-feature")

                    self.idle_timeout = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"
                    self._children_yang_names.add("idle-timeout")

                    self.service_accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                    self._children_yang_names.add("service-accounting")

                    self.session = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, ['prepaid_feature'], name, value)


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** 60..4320000
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                        self.timeout_value = YLeaf(YType.uint32, "timeout-value")
                        self._segment_path = lambda: "idle-timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, ['direction', 'threshold', 'timeout_value'], name, value)


                class ServiceAccounting(Entity):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: minute
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")
                        self._segment_path = lambda: "service-accounting"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, ['accounting_interim_interval', 'method_list_name'], name, value)


                class Session(Entity):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\:  str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")
                        self._segment_path = lambda: "session"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, ['dual_stack_delay', 'hold_acct_start', 'method_list_name', 'periodic_interval'], name, value)


            class Ipv4Network(Entity):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\:  int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\:  str
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, ['mtu', 'rpf', 'unnumbered', 'unreachables'], name, value)


            class Ipv4PacketFilter(Entity):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"


                class Inbound(Entity):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, ['common_acl_name', 'hardware_count', 'interface_statistics', 'name'], name, value)


            class Ipv6Neighbor(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:   :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:   :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\:  str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\:  int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:   :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\:  int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"duplicate-address-detection" : ("duplicate_address_detection", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection), "framed-prefix" : ("framed_prefix", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix), "ra-initial" : ("ra_initial", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial), "ra-interval" : ("ra_interval", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval)}
                    self._child_list_classes = {}

                    self.framed_prefix_pool = YLeaf(YType.str, "framed-prefix-pool")

                    self.managed_config = YLeaf(YType.empty, "managed-config")

                    self.ns_interval = YLeaf(YType.uint32, "ns-interval")

                    self.nud_enable = YLeaf(YType.empty, "nud-enable")

                    self.other_config = YLeaf(YType.empty, "other-config")

                    self.ra_lifetime = YLeaf(YType.uint32, "ra-lifetime")

                    self.ra_suppress = YLeaf(YType.empty, "ra-suppress")

                    self.ra_suppress_mtu = YLeaf(YType.empty, "ra-suppress-mtu")

                    self.ra_unicast = YLeaf(YType.empty, "ra-unicast")

                    self.ra_unspecify_hoplimit = YLeaf(YType.empty, "ra-unspecify-hoplimit")

                    self.reachable_time = YLeaf(YType.uint32, "reachable-time")

                    self.router_preference = YLeaf(YType.enumeration, "router-preference")

                    self.start_ra_on_ipv6_enable = YLeaf(YType.empty, "start-ra-on-ipv6-enable")

                    self.suppress_cache_learning = YLeaf(YType.empty, "suppress-cache-learning")

                    self.duplicate_address_detection = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                    self._children_yang_names.add("duplicate-address-detection")

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"
                    self._children_yang_names.add("framed-prefix")

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._children_yang_names.add("ra-initial")

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"
                    self._children_yang_names.add("ra-interval")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'ns_interval', 'nud_enable', 'other_config', 'ra_lifetime', 'ra_suppress', 'ra_suppress_mtu', 'ra_unicast', 'ra_unspecify_hoplimit', 'reachable_time', 'router_preference', 'start_ra_on_ipv6_enable', 'suppress_cache_learning'], name, value)


                class DuplicateAddressDetection(Entity):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.attempts = YLeaf(YType.uint32, "attempts")
                        self._segment_path = lambda: "duplicate-address-detection"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)


                class FramedPrefix(Entity):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "framed-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, ['prefix', 'prefix_length'], name, value)


                class RaInitial(Entity):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")
                        self._segment_path = lambda: "ra-initial"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)


                class RaInterval(Entity):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\:  int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\:  int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")
                        self._segment_path = lambda: "ra-interval"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)


            class Ipv6Network(Entity):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\:  int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\:  bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"addresses" : ("addresses", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses)}
                    self._child_list_classes = {}

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(Entity):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auto-configuration" : ("auto_configuration", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration)}
                        self._child_list_classes = {}

                        self.auto_configuration = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")
                        self._segment_path = lambda: "addresses"


                    class AutoConfiguration(Entity):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "auto-configuration"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)


            class Ipv6PacketFilter(Entity):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:   :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:   :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inbound" : ("inbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound), "outbound" : ("outbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound)}
                    self._child_list_classes = {}

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"


                class Inbound(Entity):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "inbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


                class Outbound(Entity):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  str
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "outbound"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, ['common_acl_name', 'interface_statistics', 'name'], name, value)


            class Pbr(Entity):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policy
                
                	PBR service policy configuration
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\:  str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"service-policy" : ("service_policy", DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy)}
                    self._child_list_classes = {}

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, ['service_policy_in'], name, value)


                class ServicePolicy(Entity):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.input = YLeaf(YType.str, "input")
                        self._segment_path = lambda: "service-policy"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy, ['input'], name, value)


            class Qos(Entity):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:   :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output>`
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"account" : ("account", DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account), "output" : ("output", DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output), "service-policy" : ("service_policy", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy)}
                    self._child_list_classes = {}

                    self.account = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"
                    self._children_yang_names.add("account")

                    self.output = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._children_yang_names.add("output")

                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"


                class Account(Entity):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")
                        self._segment_path = lambda: "account"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, ['aal', 'atm_cell_tax', 'encapsulation', 'user_defined'], name, value)


                class Output(Entity):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")
                        self._segment_path = lambda: "output"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, ['minimum_bandwidth'], name, value)


                class ServicePolicy(Entity):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"input" : ("input", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input), "output" : ("output", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output)}
                        self._child_list_classes = {}

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")
                        self._segment_path = lambda: "service-policy"


                    class Input(Entity):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "input"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


                    class Output(Entity):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\:  bool
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\:  bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")
                            self._segment_path = lambda: "output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, ['account_stats', 'merge', 'merge_id', 'policy_name', 'spi_name'], name, value)


            class SpanMonitorSessions(Entity):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"span-monitor-session" : ("span_monitor_session", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession)}

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:   :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"acl" : ("acl", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl), "attachment" : ("attachment", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment)}
                        self._child_list_classes = {}

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._children_yang_names.add("acl")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + self.session_class.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Acl(Entity):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\:  str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.acl_enable = YLeaf(YType.empty, "acl-enable")

                            self.acl_name = YLeaf(YType.str, "acl-name")
                            self._segment_path = lambda: "acl"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)


                    class Attachment(Entity):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")
                            self._segment_path = lambda: "attachment"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, ['direction', 'port_level_enable', 'session_name'], name, value)

    def clone_ptr(self):
        self._top_entity = DynamicTemplate()
        return self._top_entity

