""" Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-infra\-tmplmgr package configuration.

This module contains definitions
for the following management objects\:
  dynamic\-template\: All dynamic template configurations

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DynamicTemplate(_Entity_):
    """
    All dynamic template configurations
    
    .. attribute:: ppps
    
    	Templates of the PPP Type
    	**type**\:  :py:class:`Ppps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps>`
    
    .. attribute:: ip_subscribers
    
    	The IP Subscriber Template Table
    	**type**\:  :py:class:`IpSubscribers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers>`
    
    .. attribute:: subscriber_services
    
    	The Service Type Template Table
    	**type**\:  :py:class:`SubscriberServices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices>`
    
    

    """

    _prefix = 'subscriber-infra-tmplmgr-cfg'
    _revision = '2015-01-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(DynamicTemplate, self).__init__()
        self._top_entity = None

        self.yang_name = "dynamic-template"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ppps", ("ppps", DynamicTemplate.Ppps)), ("ip-subscribers", ("ip_subscribers", DynamicTemplate.IpSubscribers)), ("subscriber-services", ("subscriber_services", DynamicTemplate.SubscriberServices))])
        self._leafs = OrderedDict()

        self.ppps = DynamicTemplate.Ppps()
        self.ppps.parent = self
        self._children_name_map["ppps"] = "ppps"

        self.ip_subscribers = DynamicTemplate.IpSubscribers()
        self.ip_subscribers.parent = self
        self._children_name_map["ip_subscribers"] = "ip-subscribers"

        self.subscriber_services = DynamicTemplate.SubscriberServices()
        self.subscriber_services.parent = self
        self._children_name_map["subscriber_services"] = "subscriber-services"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DynamicTemplate, [], name, value)


    class Ppps(_Entity_):
        """
        Templates of the PPP Type
        
        .. attribute:: ppp
        
        	A Template of the PPP Type
        	**type**\: list of  		 :py:class:`Ppp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DynamicTemplate.Ppps, self).__init__()

            self.yang_name = "ppps"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ppp", ("ppp", DynamicTemplate.Ppps.Ppp))])
            self._leafs = OrderedDict()

            self.ppp = YList(self)
            self._segment_path = lambda: "ppps"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.Ppps, [], name, value)


        class Ppp(_Entity_):
            """
            A Template of the PPP Type
            
            .. attribute:: template_name  (key)
            
            	The name of the template
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:  :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4Network>`
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:  :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos>`
            
            .. attribute:: igmp
            
            	IGMPconfiguration
            	**type**\:  :py:class:`Igmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network>`
            
            .. attribute:: pppoe_template
            
            	PPPoE template configuration data
            	**type**\:  :py:class:`PppoeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppoeTemplate>`
            
            	**presence node**\: True
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:  :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor>`
            
            .. attribute:: ppp_template
            
            	PPP template configuration data
            	**type**\:  :py:class:`PppTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:  :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Pbr>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:  :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:  :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter>`
            
            .. attribute:: dhcpv6
            
            	Interface dhcpv6 configuration data
            	**type**\:  :py:class:`Dhcpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Dhcpv6>`
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DynamicTemplate.Ppps.Ppp, self).__init__()

                self.yang_name = "ppp"
                self.yang_parent_name = "ppps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['template_name']
                self._child_classes = OrderedDict([("Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network", ("ipv4_network", DynamicTemplate.Ppps.Ppp.Ipv4Network)), ("Cisco-IOS-XR-subscriber-accounting-cfg:accounting", ("accounting", DynamicTemplate.Ppps.Ppp.Accounting)), ("Cisco-IOS-XR-qos-ma-bng-cfg:qos", ("qos", DynamicTemplate.Ppps.Ppp.Qos)), ("Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp", ("igmp", DynamicTemplate.Ppps.Ppp.Igmp)), ("Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network", ("ipv6_network", DynamicTemplate.Ppps.Ppp.Ipv6Network)), ("Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-template", ("pppoe_template", DynamicTemplate.Ppps.Ppp.PppoeTemplate)), ("Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions", ("span_monitor_sessions", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions)), ("Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor", ("ipv6_neighbor", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor)), ("Cisco-IOS-XR-ppp-ma-gbl-cfg:ppp-template", ("ppp_template", DynamicTemplate.Ppps.Ppp.PppTemplate)), ("Cisco-IOS-XR-pbr-subscriber-cfg:pbr", ("pbr", DynamicTemplate.Ppps.Ppp.Pbr)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter", ("ipv4_packet_filter", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter", ("ipv6_packet_filter", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter)), ("Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6", ("dhcpv6", DynamicTemplate.Ppps.Ppp.Dhcpv6))])
                self._leafs = OrderedDict([
                    ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ('vrf', (YLeaf(YType.str, 'Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf'), ['str'])),
                ])
                self.template_name = None
                self.vrf = None

                self.ipv4_network = DynamicTemplate.Ppps.Ppp.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                self.accounting = DynamicTemplate.Ppps.Ppp.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                self.qos = DynamicTemplate.Ppps.Ppp.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "Cisco-IOS-XR-qos-ma-bng-cfg:qos"

                self.igmp = DynamicTemplate.Ppps.Ppp.Igmp()
                self.igmp.parent = self
                self._children_name_map["igmp"] = "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"

                self.ipv6_network = DynamicTemplate.Ppps.Ppp.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                self.pppoe_template = None
                self._children_name_map["pppoe_template"] = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-template"

                self.span_monitor_sessions = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                self.ipv6_neighbor = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                self.ppp_template = DynamicTemplate.Ppps.Ppp.PppTemplate()
                self.ppp_template.parent = self
                self._children_name_map["ppp_template"] = "Cisco-IOS-XR-ppp-ma-gbl-cfg:ppp-template"

                self.pbr = DynamicTemplate.Ppps.Ppp.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                self.ipv4_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"

                self.ipv6_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"

                self.dhcpv6 = DynamicTemplate.Ppps.Ppp.Dhcpv6()
                self.dhcpv6.parent = self
                self._children_name_map["dhcpv6"] = "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"
                self._segment_path = lambda: "ppp" + "[template-name='" + str(self.template_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ppps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.Ppps.Ppp, ['template_name', 'vrf'], name, value)


            class Ipv4Network(_Entity_):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\: str
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\: int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('unnumbered', (YLeaf(YType.str, 'unnumbered'), ['str'])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('unreachables', (YLeaf(YType.boolean, 'unreachables'), ['bool'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                    ])
                    self.unnumbered = None
                    self.mtu = None
                    self.unreachables = None
                    self.rpf = None
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4Network, ['unnumbered', 'mtu', 'unreachables', 'rpf'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4Network']['meta_info']


            class Accounting(_Entity_):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:  :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.Session>`
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:  :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting>`
                
                .. attribute:: monitor_feature
                
                	Subscriber monitor feature
                	**type**\: str
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\: str
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("idle-timeout", ("idle_timeout", DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout)), ("session", ("session", DynamicTemplate.Ppps.Ppp.Accounting.Session)), ("service-accounting", ("service_accounting", DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting))])
                    self._leafs = OrderedDict([
                        ('monitor_feature', (YLeaf(YType.str, 'monitor-feature'), ['str'])),
                        ('prepaid_feature', (YLeaf(YType.str, 'prepaid-feature'), ['str'])),
                    ])
                    self.monitor_feature = None
                    self.prepaid_feature = None

                    self.idle_timeout = DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"

                    self.session = DynamicTemplate.Ppps.Ppp.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"

                    self.service_accounting = DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting, ['monitor_feature', 'prepaid_feature'], name, value)


                class IdleTimeout(_Entity_):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\: int
                    
                    	**range:** 60..4320000
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                            ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                        ])
                        self.timeout_value = None
                        self.threshold = None
                        self.direction = None
                        self._segment_path = lambda: "idle-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, ['timeout_value', 'threshold', 'direction'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout']['meta_info']


                class Session(_Entity_):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\: str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  :py:class:`HoldAcctStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Accounting.Session.HoldAcctStart>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
                            ('dual_stack_delay', (YLeaf(YType.uint32, 'dual-stack-delay'), ['int'])),
                            ('hold_acct_start', (YLeaf(YType.enumeration, 'hold-acct-start'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate', 'Ppps.Ppp.Accounting.Session.HoldAcctStart')])),
                        ])
                        self.method_list_name = None
                        self.periodic_interval = None
                        self.dual_stack_delay = None
                        self.hold_acct_start = None
                        self._segment_path = lambda: "session"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.Session, ['method_list_name', 'periodic_interval', 'dual_stack_delay', 'hold_acct_start'], name, value)

                    class HoldAcctStart(Enum):
                        """
                        HoldAcctStart (Enum Class)

                        Hold Accounting start based on IA\_PD

                        .. data:: ipv6_prefix_delegation = 3

                        	Based on ipv6 delegated prefix

                        """

                        ipv6_prefix_delegation = Enum.YLeaf(3, "ipv6-prefix-delegation")


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Accounting.Session.HoldAcctStart']


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Accounting.Session']['meta_info']


                class ServiceAccounting(_Entity_):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\: str
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('accounting_interim_interval', (YLeaf(YType.uint32, 'accounting-interim-interval'), ['int'])),
                        ])
                        self.method_list_name = None
                        self.accounting_interim_interval = None
                        self._segment_path = lambda: "service-accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, ['method_list_name', 'accounting_interim_interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Accounting']['meta_info']


            class Qos(_Entity_):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:  :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy>`
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:  :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.Output>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy)), ("account", ("account", DynamicTemplate.Ppps.Ppp.Qos.Account)), ("output", ("output", DynamicTemplate.Ppps.Ppp.Qos.Output))])
                    self._leafs = OrderedDict()

                    self.service_policy = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"

                    self.account = DynamicTemplate.Ppps.Ppp.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"

                    self.output = DynamicTemplate.Ppps.Ppp.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos, [], name, value)


                class ServicePolicy(_Entity_):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("input", ("input", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input)), ("output", ("output", DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output))])
                        self._leafs = OrderedDict()

                        self.input = None
                        self._children_name_map["input"] = "input"

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._segment_path = lambda: "service-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy, [], name, value)


                    class Input(_Entity_):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input']['meta_info']


                    class Output(_Entity_):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']


                class Account(_Entity_):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:  :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:  :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\: int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aal', (YLeaf(YType.enumeration, 'aal'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap', '')])),
                            ('atm_cell_tax', (YLeaf(YType.empty, 'atm-cell-tax'), ['Empty'])),
                            ('user_defined', (YLeaf(YType.int32, 'user-defined'), ['int'])),
                        ])
                        self.aal = None
                        self.encapsulation = None
                        self.atm_cell_tax = None
                        self.user_defined = None
                        self._segment_path = lambda: "account"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.Account, ['aal', 'encapsulation', 'atm_cell_tax', 'user_defined'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.Account']['meta_info']


                class Output(_Entity_):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('minimum_bandwidth', (YLeaf(YType.uint32, 'minimum-bandwidth'), ['int'])),
                        ])
                        self.minimum_bandwidth = None
                        self._segment_path = lambda: "output"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Qos.Output, ['minimum_bandwidth'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.Output']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']


            class Igmp(_Entity_):
                """
                IGMPconfiguration
                
                .. attribute:: default_vrf
                
                	Default VRF
                	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf>`
                
                

                """

                _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Igmp, self).__init__()

                    self.yang_name = "igmp"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-vrf", ("default_vrf", DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf))])
                    self._leafs = OrderedDict()

                    self.default_vrf = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Igmp, [], name, value)


                class DefaultVrf(_Entity_):
                    """
                    Default VRF
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_groups
                    
                    	IGMP Max Groups
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access\-list group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: version
                    
                    	IGMP Version
                    	**type**\: int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\: int
                    
                    	**range:** 1..25
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: multicast_mode
                    
                    	Configure Multicast mode variable
                    	**type**\:  :py:class:`DynTmplMulticastMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg.DynTmplMulticastMode>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, self).__init__()

                        self.yang_name = "default-vrf"
                        self.yang_parent_name = "igmp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("explicit-tracking", ("explicit_tracking", DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking))])
                        self._leafs = OrderedDict([
                            ('max_groups', (YLeaf(YType.uint32, 'max-groups'), ['int'])),
                            ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                            ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                            ('multicast_mode', (YLeaf(YType.enumeration, 'multicast-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg', 'DynTmplMulticastMode', '')])),
                        ])
                        self.max_groups = None
                        self.access_group = None
                        self.version = None
                        self.query_interval = None
                        self.query_max_response_time = None
                        self.multicast_mode = None

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._segment_path = lambda: "default-vrf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, ['max_groups', 'access_group', 'version', 'query_interval', 'query_max_response_time', 'multicast_mode'], name, value)


                    class ExplicitTracking(_Entity_):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: enable
                        
                        	Enable or disable, when value is TRUE or FALSE respectively
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "default-vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.enable = None
                            self.access_list_name = None
                            self._segment_path = lambda: "explicit-tracking"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, ['enable', 'access_list_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info']


            class Ipv6Network(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\: int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addresses", ("addresses", DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses))])
                    self._leafs = OrderedDict([
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                        ('unreachables', (YLeaf(YType.empty, 'unreachables'), ['Empty'])),
                    ])
                    self.mtu = None
                    self.rpf = None
                    self.unreachables = None

                    self.addresses = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(_Entity_):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:  :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auto-configuration", ("auto_configuration", DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration))])
                        self._leafs = OrderedDict()

                        self.auto_configuration = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._segment_path = lambda: "addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses, [], name, value)


                    class AutoConfiguration(_Entity_):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "auto-configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info']


            class PppoeTemplate(_Entity_):
                """
                PPPoE template configuration data
                
                .. attribute:: port_limit
                
                	Specify the Port limit (attr 62) to apply to the subscriber
                	**type**\: int
                
                	**range:** 1..65535
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.PppoeTemplate, self).__init__()

                    self.yang_name = "pppoe-template"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('port_limit', (YLeaf(YType.uint16, 'port-limit'), ['int'])),
                    ])
                    self.port_limit = None
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-template"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppoeTemplate, ['port_limit'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppoeTemplate']['meta_info']


            class SpanMonitorSessions(_Entity_):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of  		 :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("span-monitor-session", ("span_monitor_session", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession))])
                    self._leafs = OrderedDict()

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(_Entity_):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  (key)
                    
                    	Session Class
                    	**type**\:  :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:  :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:  :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session_class']
                        self._child_classes = OrderedDict([("attachment", ("attachment", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment)), ("acl", ("acl", DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl))])
                        self._leafs = OrderedDict([
                            ('session_class', (YLeaf(YType.enumeration, 'session-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass', '')])),
                            ('mirror_first', (YLeaf(YType.uint32, 'mirror-first'), ['int'])),
                            ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval', '')])),
                        ])
                        self.session_class = None
                        self.mirror_first = None
                        self.mirror_interval = None

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + str(self.session_class) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Attachment(_Entity_):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\: str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:  :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection', '')])),
                                ('port_level_enable', (YLeaf(YType.empty, 'port-level-enable'), ['Empty'])),
                            ])
                            self.session_name = None
                            self.direction = None
                            self.port_level_enable = None
                            self._segment_path = lambda: "attachment"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, ['session_name', 'direction', 'port_level_enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']


                    class Acl(_Entity_):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('acl_enable', (YLeaf(YType.empty, 'acl-enable'), ['Empty'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.acl_enable = None
                            self.acl_name = None
                            self._segment_path = lambda: "acl"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info']


            class Ipv6Neighbor(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:  :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:  :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:  :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\: str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\: int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:  :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\: int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\: int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ra-interval", ("ra_interval", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval)), ("framed-prefix", ("framed_prefix", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix)), ("duplicate-address-detection", ("duplicate_address_detection", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection)), ("ra-initial", ("ra_initial", DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial))])
                    self._leafs = OrderedDict([
                        ('framed_prefix_pool', (YLeaf(YType.str, 'framed-prefix-pool'), ['str'])),
                        ('managed_config', (YLeaf(YType.empty, 'managed-config'), ['Empty'])),
                        ('other_config', (YLeaf(YType.empty, 'other-config'), ['Empty'])),
                        ('start_ra_on_ipv6_enable', (YLeaf(YType.empty, 'start-ra-on-ipv6-enable'), ['Empty'])),
                        ('nud_enable', (YLeaf(YType.empty, 'nud-enable'), ['Empty'])),
                        ('ra_lifetime', (YLeaf(YType.uint32, 'ra-lifetime'), ['int'])),
                        ('router_preference', (YLeaf(YType.enumeration, 'router-preference'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate', '')])),
                        ('ra_suppress', (YLeaf(YType.empty, 'ra-suppress'), ['Empty'])),
                        ('ra_unicast', (YLeaf(YType.empty, 'ra-unicast'), ['Empty'])),
                        ('ra_unspecify_hoplimit', (YLeaf(YType.empty, 'ra-unspecify-hoplimit'), ['Empty'])),
                        ('ra_suppress_mtu', (YLeaf(YType.empty, 'ra-suppress-mtu'), ['Empty'])),
                        ('suppress_cache_learning', (YLeaf(YType.empty, 'suppress-cache-learning'), ['Empty'])),
                        ('reachable_time', (YLeaf(YType.uint32, 'reachable-time'), ['int'])),
                        ('ns_interval', (YLeaf(YType.uint32, 'ns-interval'), ['int'])),
                    ])
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.other_config = None
                    self.start_ra_on_ipv6_enable = None
                    self.nud_enable = None
                    self.ra_lifetime = None
                    self.router_preference = None
                    self.ra_suppress = None
                    self.ra_unicast = None
                    self.ra_unspecify_hoplimit = None
                    self.ra_suppress_mtu = None
                    self.suppress_cache_learning = None
                    self.reachable_time = None
                    self.ns_interval = None

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"

                    self.duplicate_address_detection = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'other_config', 'start_ra_on_ipv6_enable', 'nud_enable', 'ra_lifetime', 'router_preference', 'ra_suppress', 'ra_unicast', 'ra_unspecify_hoplimit', 'ra_suppress_mtu', 'suppress_cache_learning', 'reachable_time', 'ns_interval'], name, value)


                class RaInterval(_Entity_):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\: int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                        ])
                        self.maximum = None
                        self.minimum = None
                        self._segment_path = lambda: "ra-interval"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval']['meta_info']


                class FramedPrefix(_Entity_):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ])
                        self.prefix_length = None
                        self.prefix = None
                        self._segment_path = lambda: "framed-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, ['prefix_length', 'prefix'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(_Entity_):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\: int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('attempts', (YLeaf(YType.uint32, 'attempts'), ['int'])),
                        ])
                        self.attempts = None
                        self._segment_path = lambda: "duplicate-address-detection"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(_Entity_):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ])
                        self.count = None
                        self.interval = None
                        self._segment_path = lambda: "ra-initial"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']


            class PppTemplate(_Entity_):
                """
                PPP template configuration data
                
                .. attribute:: fsm
                
                	PPP FSM global template configuration data
                	**type**\:  :py:class:`Fsm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm>`
                
                .. attribute:: lcp
                
                	PPP LCP global template configuration data
                	**type**\:  :py:class:`Lcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp>`
                
                .. attribute:: ipv6cp
                
                	PPP IPv6CP global template configuration data
                	**type**\:  :py:class:`Ipv6cp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp>`
                
                .. attribute:: ipcp
                
                	PPP IPCP global template configuration data
                	**type**\:  :py:class:`Ipcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp>`
                
                

                """

                _prefix = 'ppp-ma-gbl-cfg'
                _revision = '2017-11-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.PppTemplate, self).__init__()

                    self.yang_name = "ppp-template"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("fsm", ("fsm", DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm)), ("lcp", ("lcp", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp)), ("ipv6cp", ("ipv6cp", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp)), ("ipcp", ("ipcp", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp))])
                    self._leafs = OrderedDict()

                    self.fsm = DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm()
                    self.fsm.parent = self
                    self._children_name_map["fsm"] = "fsm"

                    self.lcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp()
                    self.lcp.parent = self
                    self._children_name_map["lcp"] = "lcp"

                    self.ipv6cp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp()
                    self.ipv6cp.parent = self
                    self._children_name_map["ipv6cp"] = "ipv6cp"

                    self.ipcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp()
                    self.ipcp.parent = self
                    self._children_name_map["ipcp"] = "ipcp"
                    self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-gbl-cfg:ppp-template"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate, [], name, value)


                class Fsm(_Entity_):
                    """
                    PPP FSM global template configuration data
                    
                    .. attribute:: max_consecutive_conf_naks
                    
                    	This specifies the maximum number of consecutive Conf\-Naks
                    	**type**\: int
                    
                    	**range:** 2..10
                    
                    	**default value**\: 5
                    
                    .. attribute:: max_unacknowledged_conf_requests
                    
                    	This specifies the maximum number of unacknowledged Conf\-Requests
                    	**type**\: int
                    
                    	**range:** 4..20
                    
                    	**default value**\: 10
                    
                    .. attribute:: retry_timeout
                    
                    	This specifies the maximum time to wait for a response during PPP negotiation
                    	**type**\: int
                    
                    	**range:** 1..10
                    
                    	**default value**\: 3
                    
                    .. attribute:: protocol_reject_timeout
                    
                    	This specifies the maximum time to wait before sending Protocol Reject
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**default value**\: 60
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, self).__init__()

                        self.yang_name = "fsm"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('max_consecutive_conf_naks', (YLeaf(YType.uint32, 'max-consecutive-conf-naks'), ['int'])),
                            ('max_unacknowledged_conf_requests', (YLeaf(YType.uint32, 'max-unacknowledged-conf-requests'), ['int'])),
                            ('retry_timeout', (YLeaf(YType.uint32, 'retry-timeout'), ['int'])),
                            ('protocol_reject_timeout', (YLeaf(YType.uint32, 'protocol-reject-timeout'), ['int'])),
                        ])
                        self.max_consecutive_conf_naks = None
                        self.max_unacknowledged_conf_requests = None
                        self.retry_timeout = None
                        self.protocol_reject_timeout = None
                        self._segment_path = lambda: "fsm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, ['max_consecutive_conf_naks', 'max_unacknowledged_conf_requests', 'retry_timeout', 'protocol_reject_timeout'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm']['meta_info']


                class Lcp(_Entity_):
                    """
                    PPP LCP global template configuration data
                    
                    .. attribute:: absolute_timeout
                    
                    	This specifies the session absolute timeout value
                    	**type**\:  :py:class:`AbsoluteTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout>`
                    
                    .. attribute:: delay
                    
                    	This specifies the time to delay before starting active LCPnegotiations
                    	**type**\:  :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay>`
                    
                    .. attribute:: authentication
                    
                    	PPP authentication parameters
                    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication>`
                    
                    .. attribute:: keepalive
                    
                    	This specifies the rate at which EchoReq packets are sent
                    	**type**\:  :py:class:`Keepalive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate LCP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: service_type
                    
                    	This is the Service\-Type
                    	**type**\: int
                    
                    	**range:** 0..15
                    
                    	**default value**\: 0
                    
                    .. attribute:: send_term_request_on_shut_down
                    
                    	Enable Sending LCP Terminate request on shutdown
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: mru_ignore
                    
                    	Ignore MRU negotiated with peer while setting interface BW
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, self).__init__()

                        self.yang_name = "lcp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("absolute-timeout", ("absolute_timeout", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout)), ("delay", ("delay", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay)), ("authentication", ("authentication", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication)), ("keepalive", ("keepalive", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive))])
                        self._leafs = OrderedDict([
                            ('renegotiation', (YLeaf(YType.empty, 'renegotiation'), ['Empty'])),
                            ('service_type', (YLeaf(YType.uint32, 'service-type'), ['int'])),
                            ('send_term_request_on_shut_down', (YLeaf(YType.empty, 'send-term-request-on-shut-down'), ['Empty'])),
                            ('mru_ignore', (YLeaf(YType.empty, 'mru-ignore'), ['Empty'])),
                        ])
                        self.renegotiation = None
                        self.service_type = None
                        self.send_term_request_on_shut_down = None
                        self.mru_ignore = None

                        self.absolute_timeout = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout()
                        self.absolute_timeout.parent = self
                        self._children_name_map["absolute_timeout"] = "absolute-timeout"

                        self.delay = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay()
                        self.delay.parent = self
                        self._children_name_map["delay"] = "delay"

                        self.authentication = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"

                        self.keepalive = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive()
                        self.keepalive.parent = self
                        self._children_name_map["keepalive"] = "keepalive"
                        self._segment_path = lambda: "lcp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, ['renegotiation', 'service_type', 'send_term_request_on_shut_down', 'mru_ignore'], name, value)


                    class AbsoluteTimeout(_Entity_):
                        """
                        This specifies the session absolute timeout
                        value
                        
                        .. attribute:: minutes
                        
                        	Minutes
                        	**type**\: int
                        
                        	**range:** 0..35000000
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, self).__init__()

                            self.yang_name = "absolute-timeout"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ])
                            self.minutes = None
                            self.seconds = None
                            self._segment_path = lambda: "absolute-timeout"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, ['minutes', 'seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout']['meta_info']


                    class Delay(_Entity_):
                        """
                        This specifies the time to delay before
                        starting active LCPnegotiations
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: milliseconds
                        
                        	Milliseconds
                        	**type**\: int
                        
                        	**range:** 0..999
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, self).__init__()

                            self.yang_name = "delay"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('milliseconds', (YLeaf(YType.uint32, 'milliseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.milliseconds = None
                            self._segment_path = lambda: "delay"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, ['seconds', 'milliseconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay']['meta_info']


                    class Authentication(_Entity_):
                        """
                        PPP authentication parameters
                        
                        .. attribute:: methods
                        
                        	This specifies the PPP link authentication method
                        	**type**\:  :py:class:`Methods <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods>`
                        
                        .. attribute:: chap_host_name
                        
                        	This specifies the CHAP hostname
                        	**type**\: str
                        
                        .. attribute:: pap
                        
                        	<1> for accepting null\-passwordduring authentication
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mschap_host_name
                        
                        	This specifies the MS\-CHAP hostname
                        	**type**\: str
                        
                        .. attribute:: max_authentication_failures
                        
                        	This specifies whether to allow multiple authentication failures and, if so, how many
                        	**type**\: int
                        
                        	**range:** 0..10
                        
                        .. attribute:: timeout
                        
                        	Maximum time to wait for an authentication response
                        	**type**\: int
                        
                        	**range:** 3..30
                        
                        	**default value**\: 10
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("methods", ("methods", DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods))])
                            self._leafs = OrderedDict([
                                ('chap_host_name', (YLeaf(YType.str, 'chap-host-name'), ['str'])),
                                ('pap', (YLeaf(YType.uint32, 'pap'), ['int'])),
                                ('mschap_host_name', (YLeaf(YType.str, 'mschap-host-name'), ['str'])),
                                ('max_authentication_failures', (YLeaf(YType.uint32, 'max-authentication-failures'), ['int'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ])
                            self.chap_host_name = None
                            self.pap = None
                            self.mschap_host_name = None
                            self.max_authentication_failures = None
                            self.timeout = None

                            self.methods = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods()
                            self.methods.parent = self
                            self._children_name_map["methods"] = "methods"
                            self._segment_path = lambda: "authentication"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, ['chap_host_name', 'pap', 'mschap_host_name', 'max_authentication_failures', 'timeout'], name, value)


                        class Methods(_Entity_):
                            """
                            This specifies the PPP link authentication
                            method
                            
                            .. attribute:: method
                            
                            	Select between one and three authentication methods in order of preference
                            	**type**\: list of   :py:class:`PppAuthenticationMethodGbl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_gbl_cfg.PppAuthenticationMethodGbl>`
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, self).__init__()

                                self.yang_name = "methods"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_gbl_cfg', 'PppAuthenticationMethodGbl', '')])),
                                ])
                                self.method = []
                                self._segment_path = lambda: "methods"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, ['method'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                                return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication']['meta_info']


                    class Keepalive(_Entity_):
                        """
                        This specifies the rate at which EchoReq
                        packets are sent
                        
                        .. attribute:: keepalive_disable
                        
                        	TRUE to disable keepalives, FALSE to specify a new keepalive interval
                        	**type**\: bool
                        
                        .. attribute:: interval
                        
                        	The keepalive interval. Leave unspecified when disabling keepalives
                        	**type**\: int
                        
                        	**range:** 10..180
                        
                        .. attribute:: retry_count
                        
                        	The keepalive retry count. Leave unspecified when disabling keepalives
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, self).__init__()

                            self.yang_name = "keepalive"
                            self.yang_parent_name = "lcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('keepalive_disable', (YLeaf(YType.boolean, 'keepalive-disable'), ['bool'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                            ])
                            self.keepalive_disable = None
                            self.interval = None
                            self.retry_count = None
                            self._segment_path = lambda: "keepalive"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, ['keepalive_disable', 'interval', 'retry_count'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info']


                class Ipv6cp(_Entity_):
                    """
                    PPP IPv6CP global template configuration data
                    
                    .. attribute:: passive
                    
                    	Specify whether to run IPv6CP in Passive mode
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate IPv6CP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_interface_id
                    
                    	Specify the Interface\-Id to impose on the peer
                    	**type**\: str
                    
                    .. attribute:: protocol_reject
                    
                    	Specify whether to protocol reject IPv6CP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp, self).__init__()

                        self.yang_name = "ipv6cp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('passive', (YLeaf(YType.empty, 'passive'), ['Empty'])),
                            ('renegotiation', (YLeaf(YType.empty, 'renegotiation'), ['Empty'])),
                            ('peer_interface_id', (YLeaf(YType.str, 'peer-interface-id'), ['str'])),
                            ('protocol_reject', (YLeaf(YType.empty, 'protocol-reject'), ['Empty'])),
                        ])
                        self.passive = None
                        self.renegotiation = None
                        self.peer_interface_id = None
                        self.protocol_reject = None
                        self._segment_path = lambda: "ipv6cp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp, ['passive', 'renegotiation', 'peer_interface_id', 'protocol_reject'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp']['meta_info']


                class Ipcp(_Entity_):
                    """
                    PPP IPCP global template configuration data
                    
                    .. attribute:: wins
                    
                    	IPCP WINS parameters
                    	**type**\:  :py:class:`Wins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins>`
                    
                    .. attribute:: dns
                    
                    	IPCP DNS parameters
                    	**type**\:  :py:class:`Dns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns>`
                    
                    .. attribute:: peer_address
                    
                    	IPCP address parameters
                    	**type**\:  :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress>`
                    
                    .. attribute:: renegotiation
                    
                    	Specify whether to ignore attempts to renegotiate IPCP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: passive
                    
                    	Specify whether to run IPCP in Passive mode
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: protocol_reject
                    
                    	Specify whether to protocol reject IPCP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_netmask
                    
                    	Specify the IPv4 netmask to negotiate for the peer
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ppp-ma-gbl-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, self).__init__()

                        self.yang_name = "ipcp"
                        self.yang_parent_name = "ppp-template"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("wins", ("wins", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins)), ("dns", ("dns", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns)), ("peer-address", ("peer_address", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress))])
                        self._leafs = OrderedDict([
                            ('renegotiation', (YLeaf(YType.empty, 'renegotiation'), ['Empty'])),
                            ('passive', (YLeaf(YType.empty, 'passive'), ['Empty'])),
                            ('protocol_reject', (YLeaf(YType.empty, 'protocol-reject'), ['Empty'])),
                            ('peer_netmask', (YLeaf(YType.str, 'peer-netmask'), ['str'])),
                        ])
                        self.renegotiation = None
                        self.passive = None
                        self.protocol_reject = None
                        self.peer_netmask = None

                        self.wins = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins()
                        self.wins.parent = self
                        self._children_name_map["wins"] = "wins"

                        self.dns = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns()
                        self.dns.parent = self
                        self._children_name_map["dns"] = "dns"

                        self.peer_address = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress()
                        self.peer_address.parent = self
                        self._children_name_map["peer_address"] = "peer-address"
                        self._segment_path = lambda: "ipcp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, ['renegotiation', 'passive', 'protocol_reject', 'peer_netmask'], name, value)


                    class Wins(_Entity_):
                        """
                        IPCP WINS parameters
                        
                        .. attribute:: wins_addresses
                        
                        	Specify WINS address(es) to provide
                        	**type**\:  :py:class:`WinsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses>`
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins, self).__init__()

                            self.yang_name = "wins"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("wins-addresses", ("wins_addresses", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses))])
                            self._leafs = OrderedDict()

                            self.wins_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses()
                            self.wins_addresses.parent = self
                            self._children_name_map["wins_addresses"] = "wins-addresses"
                            self._segment_path = lambda: "wins"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins, [], name, value)


                        class WinsAddresses(_Entity_):
                            """
                            Specify WINS address(es) to provide
                            
                            .. attribute:: primary
                            
                            	Primary WINS IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary
                            
                            	Secondary WINS IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, self).__init__()

                                self.yang_name = "wins-addresses"
                                self.yang_parent_name = "wins"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                    ('secondary', (YLeaf(YType.str, 'secondary'), ['str'])),
                                ])
                                self.primary = None
                                self.secondary = None
                                self._segment_path = lambda: "wins-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, ['primary', 'secondary'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                                return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins']['meta_info']


                    class Dns(_Entity_):
                        """
                        IPCP DNS parameters
                        
                        .. attribute:: dns_addresses
                        
                        	Specify DNS address(es) to provide
                        	**type**\:  :py:class:`DnsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses>`
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns, self).__init__()

                            self.yang_name = "dns"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("dns-addresses", ("dns_addresses", DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses))])
                            self._leafs = OrderedDict()

                            self.dns_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses()
                            self.dns_addresses.parent = self
                            self._children_name_map["dns_addresses"] = "dns-addresses"
                            self._segment_path = lambda: "dns"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns, [], name, value)


                        class DnsAddresses(_Entity_):
                            """
                            Specify DNS address(es) to provide
                            
                            .. attribute:: primary
                            
                            	Primary DNS IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary
                            
                            	Secondary DNS IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ppp-ma-gbl-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, self).__init__()

                                self.yang_name = "dns-addresses"
                                self.yang_parent_name = "dns"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                    ('secondary', (YLeaf(YType.str, 'secondary'), ['str'])),
                                ])
                                self.primary = None
                                self.secondary = None
                                self._segment_path = lambda: "dns-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, ['primary', 'secondary'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                                return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns']['meta_info']


                    class PeerAddress(_Entity_):
                        """
                        IPCP address parameters
                        
                        .. attribute:: default
                        
                        	Specify an IP address to assign to peers through IPCP
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: pool
                        
                        	Accepts an IP address from the peer if in the pool, else allocates one from the pool
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ppp-ma-gbl-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "ipcp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('default', (YLeaf(YType.str, 'default'), ['str'])),
                                ('pool', (YLeaf(YType.str, 'pool'), ['str'])),
                            ])
                            self.default = None
                            self.pool = None
                            self._segment_path = lambda: "peer-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, ['default', 'pool'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info']


            class Pbr(_Entity_):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policies
                
                	Ingress service policy
                	**type**\:  :py:class:`ServicePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\: str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policies", ("service_policies", DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies))])
                    self._leafs = OrderedDict([
                        ('service_policy_in', (YLeaf(YType.str, 'service-policy-in'), ['str'])),
                    ])
                    self.service_policy_in = None

                    self.service_policies = DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies()
                    self.service_policies.parent = self
                    self._children_name_map["service_policies"] = "service-policies"
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Pbr, ['service_policy_in'], name, value)


                class ServicePolicies(_Entity_):
                    """
                    Ingress service policy
                    
                    .. attribute:: service_policy
                    
                    	Service policy details
                    	**type**\: list of  		 :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy>`
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies, self).__init__()

                        self.yang_name = "service-policies"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy))])
                        self._leafs = OrderedDict()

                        self.service_policy = YList(self)
                        self._segment_path = lambda: "service-policies"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies, [], name, value)


                    class ServicePolicy(_Entity_):
                        """
                        Service policy details
                        
                        .. attribute:: service_policy  (key)
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'pbr-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy, self).__init__()

                            self.yang_name = "service-policy"
                            self.yang_parent_name = "service-policies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['service_policy']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('service_policy', (YLeaf(YType.str, 'service-policy'), ['str'])),
                            ])
                            self.service_policy = None
                            self._segment_path = lambda: "service-policy" + "[service-policy='" + str(self.service_policy) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy, ['service_policy'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info']


            class Ipv4PacketFilter(_Entity_):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound>`
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("outbound", ("outbound", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound)), ("inbound", ("inbound", DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound))])
                    self._leafs = OrderedDict()

                    self.outbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter, [], name, value)


                class Outbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(_Entity_):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inbound", ("inbound", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound)), ("outbound", ("outbound", DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound))])
                    self._leafs = OrderedDict()

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"

                    self.outbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter, [], name, value)


                class Inbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']


            class Dhcpv6(_Entity_):
                """
                Interface dhcpv6 configuration data
                
                .. attribute:: delegated_prefix
                
                	The prefix to be used for Prefix Delegation
                	**type**\:  :py:class:`DelegatedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: dns_ipv6address
                
                	Dns IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mode_class
                
                	Select proxy/server profile based on mode class name
                	**type**\: str
                
                .. attribute:: dhcpv6_iplease
                
                	Cisco VSA to configure any dhcpv6 ip lease per subscriber
                	**type**\: str
                
                .. attribute:: dhcpv6_option
                
                	Cisco VSA to configure any dhcpv6 option per subscriber
                	**type**\: str
                
                .. attribute:: address_pool
                
                	The pool to be used for Address assignment
                	**type**\: str
                
                .. attribute:: delegated_prefix_pool
                
                	The pool to be used for Prefix Delegation
                	**type**\: str
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\: str
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.Ppps.Ppp.Dhcpv6, self).__init__()

                    self.yang_name = "dhcpv6"
                    self.yang_parent_name = "ppp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("delegated-prefix", ("delegated_prefix", DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix))])
                    self._leafs = OrderedDict([
                        ('dns_ipv6address', (YLeaf(YType.str, 'dns-ipv6address'), ['str'])),
                        ('mode_class', (YLeaf(YType.str, 'mode-class'), ['str'])),
                        ('dhcpv6_iplease', (YLeaf(YType.str, 'dhcpv6-iplease'), ['str'])),
                        ('dhcpv6_option', (YLeaf(YType.str, 'dhcpv6-option'), ['str'])),
                        ('address_pool', (YLeaf(YType.str, 'address-pool'), ['str'])),
                        ('delegated_prefix_pool', (YLeaf(YType.str, 'delegated-prefix-pool'), ['str'])),
                        ('class_', (YLeaf(YType.str, 'class'), ['str'])),
                        ('stateful_address', (YLeaf(YType.str, 'stateful-address'), ['str'])),
                    ])
                    self.dns_ipv6address = None
                    self.mode_class = None
                    self.dhcpv6_iplease = None
                    self.dhcpv6_option = None
                    self.address_pool = None
                    self.delegated_prefix_pool = None
                    self.class_ = None
                    self.stateful_address = None

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.Ppps.Ppp.Dhcpv6, ['dns_ipv6address', 'mode_class', 'dhcpv6_iplease', 'dhcpv6_option', 'address_pool', 'delegated_prefix_pool', 'class_', 'stateful_address'], name, value)


                class DelegatedPrefix(_Entity_):
                    """
                    The prefix to be used for Prefix Delegation
                    
                    .. attribute:: prefix
                    
                    	IPv6 Prefix
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	PD Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, self).__init__()

                        self.yang_name = "delegated-prefix"
                        self.yang_parent_name = "dhcpv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self._segment_path = lambda: "delegated-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, ['prefix', 'prefix_length'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.Ppps']['meta_info']


    class IpSubscribers(_Entity_):
        """
        The IP Subscriber Template Table
        
        .. attribute:: ip_subscriber
        
        	A IP Subscriber Type Template 
        	**type**\: list of  		 :py:class:`IpSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DynamicTemplate.IpSubscribers, self).__init__()

            self.yang_name = "ip-subscribers"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ip-subscriber", ("ip_subscriber", DynamicTemplate.IpSubscribers.IpSubscriber))])
            self._leafs = OrderedDict()

            self.ip_subscriber = YList(self)
            self._segment_path = lambda: "ip-subscribers"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.IpSubscribers, [], name, value)


        class IpSubscriber(_Entity_):
            """
            A IP Subscriber Type Template 
            
            .. attribute:: template_name  (key)
            
            	The name of the template
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:  :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network>`
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:  :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos>`
            
            .. attribute:: igmp
            
            	IGMPconfiguration
            	**type**\:  :py:class:`Igmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:  :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:  :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Pbr>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:  :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:  :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter>`
            
            .. attribute:: dhcpd
            
            	Interface dhcpv4 configuration data
            	**type**\:  :py:class:`Dhcpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd>`
            
            .. attribute:: dhcpv6
            
            	Interface dhcpv6 configuration data
            	**type**\:  :py:class:`Dhcpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6>`
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DynamicTemplate.IpSubscribers.IpSubscriber, self).__init__()

                self.yang_name = "ip-subscriber"
                self.yang_parent_name = "ip-subscribers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['template_name']
                self._child_classes = OrderedDict([("Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network", ("ipv4_network", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network)), ("Cisco-IOS-XR-subscriber-accounting-cfg:accounting", ("accounting", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting)), ("Cisco-IOS-XR-qos-ma-bng-cfg:qos", ("qos", DynamicTemplate.IpSubscribers.IpSubscriber.Qos)), ("Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp", ("igmp", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp)), ("Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network", ("ipv6_network", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network)), ("Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions", ("span_monitor_sessions", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions)), ("Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor", ("ipv6_neighbor", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor)), ("Cisco-IOS-XR-pbr-subscriber-cfg:pbr", ("pbr", DynamicTemplate.IpSubscribers.IpSubscriber.Pbr)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter", ("ipv4_packet_filter", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter", ("ipv6_packet_filter", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter)), ("Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg:dhcpd", ("dhcpd", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd)), ("Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6", ("dhcpv6", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6))])
                self._leafs = OrderedDict([
                    ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ('vrf', (YLeaf(YType.str, 'Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf'), ['str'])),
                ])
                self.template_name = None
                self.vrf = None

                self.ipv4_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                self.accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                self.qos = DynamicTemplate.IpSubscribers.IpSubscriber.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "Cisco-IOS-XR-qos-ma-bng-cfg:qos"

                self.igmp = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp()
                self.igmp.parent = self
                self._children_name_map["igmp"] = "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"

                self.ipv6_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                self.span_monitor_sessions = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                self.ipv6_neighbor = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                self.pbr = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                self.ipv4_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"

                self.ipv6_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"

                self.dhcpd = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd()
                self.dhcpd.parent = self
                self._children_name_map["dhcpd"] = "Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg:dhcpd"

                self.dhcpv6 = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6()
                self.dhcpv6.parent = self
                self._children_name_map["dhcpv6"] = "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"
                self._segment_path = lambda: "ip-subscriber" + "[template-name='" + str(self.template_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ip-subscribers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber, ['template_name', 'vrf'], name, value)


            class Ipv4Network(_Entity_):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\: str
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\: int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('unnumbered', (YLeaf(YType.str, 'unnumbered'), ['str'])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('unreachables', (YLeaf(YType.boolean, 'unreachables'), ['bool'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                    ])
                    self.unnumbered = None
                    self.mtu = None
                    self.unreachables = None
                    self.rpf = None
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, ['unnumbered', 'mtu', 'unreachables', 'rpf'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network']['meta_info']


            class Accounting(_Entity_):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:  :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session>`
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:  :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout>`
                
                .. attribute:: monitor_feature
                
                	Subscriber monitor feature
                	**type**\: str
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\: str
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-accounting", ("service_accounting", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting)), ("session", ("session", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session)), ("idle-timeout", ("idle_timeout", DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout))])
                    self._leafs = OrderedDict([
                        ('monitor_feature', (YLeaf(YType.str, 'monitor-feature'), ['str'])),
                        ('prepaid_feature', (YLeaf(YType.str, 'prepaid-feature'), ['str'])),
                    ])
                    self.monitor_feature = None
                    self.prepaid_feature = None

                    self.service_accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"

                    self.session = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"

                    self.idle_timeout = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, ['monitor_feature', 'prepaid_feature'], name, value)


                class ServiceAccounting(_Entity_):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\: str
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('accounting_interim_interval', (YLeaf(YType.uint32, 'accounting-interim-interval'), ['int'])),
                        ])
                        self.method_list_name = None
                        self.accounting_interim_interval = None
                        self._segment_path = lambda: "service-accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, ['method_list_name', 'accounting_interim_interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting']['meta_info']


                class Session(_Entity_):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\: str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  :py:class:`HoldAcctStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
                            ('dual_stack_delay', (YLeaf(YType.uint32, 'dual-stack-delay'), ['int'])),
                            ('hold_acct_start', (YLeaf(YType.enumeration, 'hold-acct-start'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate', 'IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart')])),
                        ])
                        self.method_list_name = None
                        self.periodic_interval = None
                        self.dual_stack_delay = None
                        self.hold_acct_start = None
                        self._segment_path = lambda: "session"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, ['method_list_name', 'periodic_interval', 'dual_stack_delay', 'hold_acct_start'], name, value)

                    class HoldAcctStart(Enum):
                        """
                        HoldAcctStart (Enum Class)

                        Hold Accounting start based on IA\_PD

                        .. data:: ipv6_prefix_delegation = 3

                        	Based on ipv6 delegated prefix

                        """

                        ipv6_prefix_delegation = Enum.YLeaf(3, "ipv6-prefix-delegation")


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart']


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session']['meta_info']


                class IdleTimeout(_Entity_):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\: int
                    
                    	**range:** 60..4320000
                    
                    	**units**\: second
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                            ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                        ])
                        self.timeout_value = None
                        self.threshold = None
                        self.direction = None
                        self._segment_path = lambda: "idle-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, ['timeout_value', 'threshold', 'direction'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting']['meta_info']


            class Qos(_Entity_):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:  :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy>`
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:  :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy)), ("account", ("account", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account)), ("output", ("output", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output))])
                    self._leafs = OrderedDict()

                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"

                    self.account = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"

                    self.output = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos, [], name, value)


                class ServicePolicy(_Entity_):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("input", ("input", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input)), ("output", ("output", DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output))])
                        self._leafs = OrderedDict()

                        self.input = None
                        self._children_name_map["input"] = "input"

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._segment_path = lambda: "service-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy, [], name, value)


                    class Input(_Entity_):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input']['meta_info']


                    class Output(_Entity_):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']


                class Account(_Entity_):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:  :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:  :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\: int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aal', (YLeaf(YType.enumeration, 'aal'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap', '')])),
                            ('atm_cell_tax', (YLeaf(YType.empty, 'atm-cell-tax'), ['Empty'])),
                            ('user_defined', (YLeaf(YType.int32, 'user-defined'), ['int'])),
                        ])
                        self.aal = None
                        self.encapsulation = None
                        self.atm_cell_tax = None
                        self.user_defined = None
                        self._segment_path = lambda: "account"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, ['aal', 'encapsulation', 'atm_cell_tax', 'user_defined'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account']['meta_info']


                class Output(_Entity_):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('minimum_bandwidth', (YLeaf(YType.uint32, 'minimum-bandwidth'), ['int'])),
                        ])
                        self.minimum_bandwidth = None
                        self._segment_path = lambda: "output"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, ['minimum_bandwidth'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']


            class Igmp(_Entity_):
                """
                IGMPconfiguration
                
                .. attribute:: default_vrf
                
                	Default VRF
                	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf>`
                
                

                """

                _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp, self).__init__()

                    self.yang_name = "igmp"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-vrf", ("default_vrf", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf))])
                    self._leafs = OrderedDict()

                    self.default_vrf = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp, [], name, value)


                class DefaultVrf(_Entity_):
                    """
                    Default VRF
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_groups
                    
                    	IGMP Max Groups
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access\-list group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: version
                    
                    	IGMP Version
                    	**type**\: int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\: int
                    
                    	**range:** 1..25
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: multicast_mode
                    
                    	Configure Multicast mode variable
                    	**type**\:  :py:class:`DynTmplMulticastMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg.DynTmplMulticastMode>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, self).__init__()

                        self.yang_name = "default-vrf"
                        self.yang_parent_name = "igmp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("explicit-tracking", ("explicit_tracking", DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking))])
                        self._leafs = OrderedDict([
                            ('max_groups', (YLeaf(YType.uint32, 'max-groups'), ['int'])),
                            ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                            ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                            ('multicast_mode', (YLeaf(YType.enumeration, 'multicast-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg', 'DynTmplMulticastMode', '')])),
                        ])
                        self.max_groups = None
                        self.access_group = None
                        self.version = None
                        self.query_interval = None
                        self.query_max_response_time = None
                        self.multicast_mode = None

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._segment_path = lambda: "default-vrf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, ['max_groups', 'access_group', 'version', 'query_interval', 'query_max_response_time', 'multicast_mode'], name, value)


                    class ExplicitTracking(_Entity_):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: enable
                        
                        	Enable or disable, when value is TRUE or FALSE respectively
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "default-vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.enable = None
                            self.access_list_name = None
                            self._segment_path = lambda: "explicit-tracking"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, ['enable', 'access_list_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp']['meta_info']


            class Ipv6Network(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\: int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addresses", ("addresses", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses))])
                    self._leafs = OrderedDict([
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                        ('unreachables', (YLeaf(YType.empty, 'unreachables'), ['Empty'])),
                    ])
                    self.mtu = None
                    self.rpf = None
                    self.unreachables = None

                    self.addresses = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(_Entity_):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:  :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auto-configuration", ("auto_configuration", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration))])
                        self._leafs = OrderedDict()

                        self.auto_configuration = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._segment_path = lambda: "addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses, [], name, value)


                    class AutoConfiguration(_Entity_):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "auto-configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info']


            class SpanMonitorSessions(_Entity_):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of  		 :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("span-monitor-session", ("span_monitor_session", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession))])
                    self._leafs = OrderedDict()

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(_Entity_):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  (key)
                    
                    	Session Class
                    	**type**\:  :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:  :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:  :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session_class']
                        self._child_classes = OrderedDict([("attachment", ("attachment", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment)), ("acl", ("acl", DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl))])
                        self._leafs = OrderedDict([
                            ('session_class', (YLeaf(YType.enumeration, 'session-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass', '')])),
                            ('mirror_first', (YLeaf(YType.uint32, 'mirror-first'), ['int'])),
                            ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval', '')])),
                        ])
                        self.session_class = None
                        self.mirror_first = None
                        self.mirror_interval = None

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + str(self.session_class) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Attachment(_Entity_):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\: str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:  :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection', '')])),
                                ('port_level_enable', (YLeaf(YType.empty, 'port-level-enable'), ['Empty'])),
                            ])
                            self.session_name = None
                            self.direction = None
                            self.port_level_enable = None
                            self._segment_path = lambda: "attachment"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, ['session_name', 'direction', 'port_level_enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']


                    class Acl(_Entity_):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('acl_enable', (YLeaf(YType.empty, 'acl-enable'), ['Empty'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.acl_enable = None
                            self.acl_name = None
                            self._segment_path = lambda: "acl"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info']


            class Ipv6Neighbor(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:  :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:  :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:  :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\: str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\: int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:  :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\: int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\: int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ra-interval", ("ra_interval", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval)), ("framed-prefix", ("framed_prefix", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix)), ("duplicate-address-detection", ("duplicate_address_detection", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection)), ("ra-initial", ("ra_initial", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial))])
                    self._leafs = OrderedDict([
                        ('framed_prefix_pool', (YLeaf(YType.str, 'framed-prefix-pool'), ['str'])),
                        ('managed_config', (YLeaf(YType.empty, 'managed-config'), ['Empty'])),
                        ('other_config', (YLeaf(YType.empty, 'other-config'), ['Empty'])),
                        ('start_ra_on_ipv6_enable', (YLeaf(YType.empty, 'start-ra-on-ipv6-enable'), ['Empty'])),
                        ('nud_enable', (YLeaf(YType.empty, 'nud-enable'), ['Empty'])),
                        ('ra_lifetime', (YLeaf(YType.uint32, 'ra-lifetime'), ['int'])),
                        ('router_preference', (YLeaf(YType.enumeration, 'router-preference'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate', '')])),
                        ('ra_suppress', (YLeaf(YType.empty, 'ra-suppress'), ['Empty'])),
                        ('ra_unicast', (YLeaf(YType.empty, 'ra-unicast'), ['Empty'])),
                        ('ra_unspecify_hoplimit', (YLeaf(YType.empty, 'ra-unspecify-hoplimit'), ['Empty'])),
                        ('ra_suppress_mtu', (YLeaf(YType.empty, 'ra-suppress-mtu'), ['Empty'])),
                        ('suppress_cache_learning', (YLeaf(YType.empty, 'suppress-cache-learning'), ['Empty'])),
                        ('reachable_time', (YLeaf(YType.uint32, 'reachable-time'), ['int'])),
                        ('ns_interval', (YLeaf(YType.uint32, 'ns-interval'), ['int'])),
                    ])
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.other_config = None
                    self.start_ra_on_ipv6_enable = None
                    self.nud_enable = None
                    self.ra_lifetime = None
                    self.router_preference = None
                    self.ra_suppress = None
                    self.ra_unicast = None
                    self.ra_unspecify_hoplimit = None
                    self.ra_suppress_mtu = None
                    self.suppress_cache_learning = None
                    self.reachable_time = None
                    self.ns_interval = None

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"

                    self.duplicate_address_detection = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'other_config', 'start_ra_on_ipv6_enable', 'nud_enable', 'ra_lifetime', 'router_preference', 'ra_suppress', 'ra_unicast', 'ra_unspecify_hoplimit', 'ra_suppress_mtu', 'suppress_cache_learning', 'reachable_time', 'ns_interval'], name, value)


                class RaInterval(_Entity_):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\: int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                        ])
                        self.maximum = None
                        self.minimum = None
                        self._segment_path = lambda: "ra-interval"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval']['meta_info']


                class FramedPrefix(_Entity_):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ])
                        self.prefix_length = None
                        self.prefix = None
                        self._segment_path = lambda: "framed-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, ['prefix_length', 'prefix'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(_Entity_):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\: int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('attempts', (YLeaf(YType.uint32, 'attempts'), ['int'])),
                        ])
                        self.attempts = None
                        self._segment_path = lambda: "duplicate-address-detection"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(_Entity_):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ])
                        self.count = None
                        self.interval = None
                        self._segment_path = lambda: "ra-initial"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']


            class Pbr(_Entity_):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policies
                
                	Ingress service policy
                	**type**\:  :py:class:`ServicePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\: str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policies", ("service_policies", DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies))])
                    self._leafs = OrderedDict([
                        ('service_policy_in', (YLeaf(YType.str, 'service-policy-in'), ['str'])),
                    ])
                    self.service_policy_in = None

                    self.service_policies = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies()
                    self.service_policies.parent = self
                    self._children_name_map["service_policies"] = "service-policies"
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, ['service_policy_in'], name, value)


                class ServicePolicies(_Entity_):
                    """
                    Ingress service policy
                    
                    .. attribute:: service_policy
                    
                    	Service policy details
                    	**type**\: list of  		 :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy>`
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies, self).__init__()

                        self.yang_name = "service-policies"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy))])
                        self._leafs = OrderedDict()

                        self.service_policy = YList(self)
                        self._segment_path = lambda: "service-policies"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies, [], name, value)


                    class ServicePolicy(_Entity_):
                        """
                        Service policy details
                        
                        .. attribute:: service_policy  (key)
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'pbr-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy, self).__init__()

                            self.yang_name = "service-policy"
                            self.yang_parent_name = "service-policies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['service_policy']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('service_policy', (YLeaf(YType.str, 'service-policy'), ['str'])),
                            ])
                            self.service_policy = None
                            self._segment_path = lambda: "service-policy" + "[service-policy='" + str(self.service_policy) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy, ['service_policy'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info']


            class Ipv4PacketFilter(_Entity_):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound>`
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("outbound", ("outbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound)), ("inbound", ("inbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound))])
                    self._leafs = OrderedDict()

                    self.outbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter, [], name, value)


                class Outbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(_Entity_):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inbound", ("inbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound)), ("outbound", ("outbound", DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound))])
                    self._leafs = OrderedDict()

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"

                    self.outbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter, [], name, value)


                class Inbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']


            class Dhcpd(_Entity_):
                """
                Interface dhcpv4 configuration data
                
                .. attribute:: dhcpv4_iplease
                
                	Cisco VSA to configure any dhcp4 ip lease per subscriber
                	**type**\: str
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\: str
                
                .. attribute:: mode_class
                
                	Select proxy/server profile based on mode class name
                	**type**\: str
                
                .. attribute:: default_gateway
                
                	The Default Gateway IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: session_limit
                
                	The pool to be used for Prefix Delegation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcpv4_option
                
                	Cisco VSA to configure any dhcp4 option per subscriber
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-dhcpd-subscriber-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, self).__init__()

                    self.yang_name = "dhcpd"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('dhcpv4_iplease', (YLeaf(YType.str, 'dhcpv4-iplease'), ['str'])),
                        ('class_', (YLeaf(YType.str, 'class'), ['str'])),
                        ('mode_class', (YLeaf(YType.str, 'mode-class'), ['str'])),
                        ('default_gateway', (YLeaf(YType.str, 'default-gateway'), ['str'])),
                        ('session_limit', (YLeaf(YType.uint32, 'session-limit'), ['int'])),
                        ('dhcpv4_option', (YLeaf(YType.str, 'dhcpv4-option'), ['str'])),
                    ])
                    self.dhcpv4_iplease = None
                    self.class_ = None
                    self.mode_class = None
                    self.default_gateway = None
                    self.session_limit = None
                    self.dhcpv4_option = None
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg:dhcpd"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, ['dhcpv4_iplease', 'class_', 'mode_class', 'default_gateway', 'session_limit', 'dhcpv4_option'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd']['meta_info']


            class Dhcpv6(_Entity_):
                """
                Interface dhcpv6 configuration data
                
                .. attribute:: delegated_prefix
                
                	The prefix to be used for Prefix Delegation
                	**type**\:  :py:class:`DelegatedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: dns_ipv6address
                
                	Dns IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mode_class
                
                	Select proxy/server profile based on mode class name
                	**type**\: str
                
                .. attribute:: dhcpv6_iplease
                
                	Cisco VSA to configure any dhcpv6 ip lease per subscriber
                	**type**\: str
                
                .. attribute:: dhcpv6_option
                
                	Cisco VSA to configure any dhcpv6 option per subscriber
                	**type**\: str
                
                .. attribute:: address_pool
                
                	The pool to be used for Address assignment
                	**type**\: str
                
                .. attribute:: delegated_prefix_pool
                
                	The pool to be used for Prefix Delegation
                	**type**\: str
                
                .. attribute:: class_
                
                	The class to be used for proxy/server profile
                	**type**\: str
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, self).__init__()

                    self.yang_name = "dhcpv6"
                    self.yang_parent_name = "ip-subscriber"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("delegated-prefix", ("delegated_prefix", DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix))])
                    self._leafs = OrderedDict([
                        ('dns_ipv6address', (YLeaf(YType.str, 'dns-ipv6address'), ['str'])),
                        ('mode_class', (YLeaf(YType.str, 'mode-class'), ['str'])),
                        ('dhcpv6_iplease', (YLeaf(YType.str, 'dhcpv6-iplease'), ['str'])),
                        ('dhcpv6_option', (YLeaf(YType.str, 'dhcpv6-option'), ['str'])),
                        ('address_pool', (YLeaf(YType.str, 'address-pool'), ['str'])),
                        ('delegated_prefix_pool', (YLeaf(YType.str, 'delegated-prefix-pool'), ['str'])),
                        ('class_', (YLeaf(YType.str, 'class'), ['str'])),
                        ('stateful_address', (YLeaf(YType.str, 'stateful-address'), ['str'])),
                    ])
                    self.dns_ipv6address = None
                    self.mode_class = None
                    self.dhcpv6_iplease = None
                    self.dhcpv6_option = None
                    self.address_pool = None
                    self.delegated_prefix_pool = None
                    self.class_ = None
                    self.stateful_address = None

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, ['dns_ipv6address', 'mode_class', 'dhcpv6_iplease', 'dhcpv6_option', 'address_pool', 'delegated_prefix_pool', 'class_', 'stateful_address'], name, value)


                class DelegatedPrefix(_Entity_):
                    """
                    The prefix to be used for Prefix Delegation
                    
                    .. attribute:: prefix
                    
                    	IPv6 Prefix
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	PD Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, self).__init__()

                        self.yang_name = "delegated-prefix"
                        self.yang_parent_name = "dhcpv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self._segment_path = lambda: "delegated-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, ['prefix', 'prefix_length'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.IpSubscribers']['meta_info']


    class SubscriberServices(_Entity_):
        """
        The Service Type Template Table
        
        .. attribute:: subscriber_service
        
        	A Service Type Template 
        	**type**\: list of  		 :py:class:`SubscriberService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(DynamicTemplate.SubscriberServices, self).__init__()

            self.yang_name = "subscriber-services"
            self.yang_parent_name = "dynamic-template"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("subscriber-service", ("subscriber_service", DynamicTemplate.SubscriberServices.SubscriberService))])
            self._leafs = OrderedDict()

            self.subscriber_service = YList(self)
            self._segment_path = lambda: "subscriber-services"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DynamicTemplate.SubscriberServices, [], name, value)


        class SubscriberService(_Entity_):
            """
            A Service Type Template 
            
            .. attribute:: template_name  (key)
            
            	The name of the template
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_network
            
            	Interface IPv4 Network configuration data
            	**type**\:  :py:class:`Ipv4Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network>`
            
            .. attribute:: subscriber_attribute
            
            	Subscriber attribute configuration data
            	**type**\:  :py:class:`SubscriberAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute>`
            
            .. attribute:: accounting
            
            	Subscriber accounting dynamic\-template commands
            	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting>`
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:  :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos>`
            
            .. attribute:: ipv6_network
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:  :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ipv6_neighbor
            
            	Interface IPv6 Network configuration data
            	**type**\:  :py:class:`Ipv6Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor>`
            
            .. attribute:: pbr
            
            	Dynamic Template PBR configuration
            	**type**\:  :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Pbr>`
            
            .. attribute:: ipv4_packet_filter
            
            	IPv4 Packet Filtering configuration for the template
            	**type**\:  :py:class:`Ipv4PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter>`
            
            .. attribute:: ipv6_packet_filter
            
            	IPv6 Packet Filtering configuration for the interface
            	**type**\:  :py:class:`Ipv6PacketFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter>`
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(DynamicTemplate.SubscriberServices.SubscriberService, self).__init__()

                self.yang_name = "subscriber-service"
                self.yang_parent_name = "subscriber-services"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['template_name']
                self._child_classes = OrderedDict([("Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network", ("ipv4_network", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network)), ("Cisco-IOS-XR-opendns-deviceid-cfg:subscriber-attribute", ("subscriber_attribute", DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute)), ("Cisco-IOS-XR-subscriber-accounting-cfg:accounting", ("accounting", DynamicTemplate.SubscriberServices.SubscriberService.Accounting)), ("Cisco-IOS-XR-qos-ma-bng-cfg:qos", ("qos", DynamicTemplate.SubscriberServices.SubscriberService.Qos)), ("Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network", ("ipv6_network", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network)), ("Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions", ("span_monitor_sessions", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions)), ("Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor", ("ipv6_neighbor", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor)), ("Cisco-IOS-XR-pbr-subscriber-cfg:pbr", ("pbr", DynamicTemplate.SubscriberServices.SubscriberService.Pbr)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter", ("ipv4_packet_filter", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter)), ("Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter", ("ipv6_packet_filter", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter))])
                self._leafs = OrderedDict([
                    ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ('vrf', (YLeaf(YType.str, 'Cisco-IOS-XR-infra-rsi-subscriber-cfg:vrf'), ['str'])),
                ])
                self.template_name = None
                self.vrf = None

                self.ipv4_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network()
                self.ipv4_network.parent = self
                self._children_name_map["ipv4_network"] = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"

                self.subscriber_attribute = DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute()
                self.subscriber_attribute.parent = self
                self._children_name_map["subscriber_attribute"] = "Cisco-IOS-XR-opendns-deviceid-cfg:subscriber-attribute"

                self.accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"

                self.qos = DynamicTemplate.SubscriberServices.SubscriberService.Qos()
                self.qos.parent = self
                self._children_name_map["qos"] = "Cisco-IOS-XR-qos-ma-bng-cfg:qos"

                self.ipv6_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network()
                self.ipv6_network.parent = self
                self._children_name_map["ipv6_network"] = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"

                self.span_monitor_sessions = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self._children_name_map["span_monitor_sessions"] = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"

                self.ipv6_neighbor = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self._children_name_map["ipv6_neighbor"] = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"

                self.pbr = DynamicTemplate.SubscriberServices.SubscriberService.Pbr()
                self.pbr.parent = self
                self._children_name_map["pbr"] = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"

                self.ipv4_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self._children_name_map["ipv4_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"

                self.ipv6_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self._children_name_map["ipv6_packet_filter"] = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"
                self._segment_path = lambda: "subscriber-service" + "[template-name='" + str(self.template_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/subscriber-services/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService, ['template_name', 'vrf'], name, value)


            class Ipv4Network(_Entity_):
                """
                Interface IPv4 Network configuration data
                
                .. attribute:: unnumbered
                
                	Enable IP processing without an explicit address
                	**type**\: str
                
                .. attribute:: mtu
                
                	The IP Maximum Transmission Unit
                	**type**\: int
                
                	**range:** 68..65535
                
                	**units**\: byte
                
                .. attribute:: unreachables
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'ipv4-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, self).__init__()

                    self.yang_name = "ipv4-network"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('unnumbered', (YLeaf(YType.str, 'unnumbered'), ['str'])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('unreachables', (YLeaf(YType.boolean, 'unreachables'), ['bool'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                    ])
                    self.unnumbered = None
                    self.mtu = None
                    self.unreachables = None
                    self.rpf = None
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, ['unnumbered', 'mtu', 'unreachables', 'rpf'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network']['meta_info']


            class SubscriberAttribute(_Entity_):
                """
                Subscriber attribute configuration data
                
                .. attribute:: open_dns
                
                	OpenDNS configuration data
                	**type**\:  :py:class:`OpenDns <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns>`
                
                

                """

                _prefix = 'opendns-deviceid-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute, self).__init__()

                    self.yang_name = "subscriber-attribute"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("open-dns", ("open_dns", DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns))])
                    self._leafs = OrderedDict()

                    self.open_dns = DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns()
                    self.open_dns.parent = self
                    self._children_name_map["open_dns"] = "open-dns"
                    self._segment_path = lambda: "Cisco-IOS-XR-opendns-deviceid-cfg:subscriber-attribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute, [], name, value)


                class OpenDns(_Entity_):
                    """
                    OpenDNS configuration data
                    
                    .. attribute:: device_id
                    
                    	Specify deviceID to be used for applying OpenDNS policies
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'opendns-deviceid-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns, self).__init__()

                        self.yang_name = "open-dns"
                        self.yang_parent_name = "subscriber-attribute"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                        ])
                        self.device_id = None
                        self._segment_path = lambda: "open-dns"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns, ['device_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute']['meta_info']


            class Accounting(_Entity_):
                """
                Subscriber accounting dynamic\-template commands
                
                .. attribute:: service_accounting
                
                	Subscriber accounting service accounting
                	**type**\:  :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting>`
                
                .. attribute:: session
                
                	Subscriber accounting session accounting
                	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session>`
                
                .. attribute:: idle_timeout
                
                	Subscriber accounting idle timeout
                	**type**\:  :py:class:`IdleTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout>`
                
                .. attribute:: monitor_feature
                
                	Subscriber monitor feature
                	**type**\: str
                
                .. attribute:: prepaid_feature
                
                	Subscriber accounting prepaid feature
                	**type**\: str
                
                

                """

                _prefix = 'subscriber-accounting-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-accounting", ("service_accounting", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting)), ("session", ("session", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session)), ("idle-timeout", ("idle_timeout", DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout))])
                    self._leafs = OrderedDict([
                        ('monitor_feature', (YLeaf(YType.str, 'monitor-feature'), ['str'])),
                        ('prepaid_feature', (YLeaf(YType.str, 'prepaid-feature'), ['str'])),
                    ])
                    self.monitor_feature = None
                    self.prepaid_feature = None

                    self.service_accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"

                    self.session = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"

                    self.idle_timeout = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout()
                    self.idle_timeout.parent = self
                    self._children_name_map["idle_timeout"] = "idle-timeout"
                    self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-cfg:accounting"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, ['monitor_feature', 'prepaid_feature'], name, value)


                class ServiceAccounting(_Entity_):
                    """
                    Subscriber accounting service accounting
                    
                    .. attribute:: method_list_name
                    
                    	Service accounting method list name
                    	**type**\: str
                    
                    .. attribute:: accounting_interim_interval
                    
                    	Accounting interim interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, self).__init__()

                        self.yang_name = "service-accounting"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('accounting_interim_interval', (YLeaf(YType.uint32, 'accounting-interim-interval'), ['int'])),
                        ])
                        self.method_list_name = None
                        self.accounting_interim_interval = None
                        self._segment_path = lambda: "service-accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, ['method_list_name', 'accounting_interim_interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting']['meta_info']


                class Session(_Entity_):
                    """
                    Subscriber accounting session accounting
                    
                    .. attribute:: method_list_name
                    
                    	Session accounting method list name
                    	**type**\: str
                    
                    .. attribute:: periodic_interval
                    
                    	Interim accounting interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: dual_stack_delay
                    
                    	Dual stack wait delay in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: hold_acct_start
                    
                    	Hold Accounting start based on IA\_PD
                    	**type**\:  :py:class:`HoldAcctStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method_list_name', (YLeaf(YType.str, 'method-list-name'), ['str'])),
                            ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
                            ('dual_stack_delay', (YLeaf(YType.uint32, 'dual-stack-delay'), ['int'])),
                            ('hold_acct_start', (YLeaf(YType.enumeration, 'hold-acct-start'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate', 'SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart')])),
                        ])
                        self.method_list_name = None
                        self.periodic_interval = None
                        self.dual_stack_delay = None
                        self.hold_acct_start = None
                        self._segment_path = lambda: "session"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, ['method_list_name', 'periodic_interval', 'dual_stack_delay', 'hold_acct_start'], name, value)

                    class HoldAcctStart(Enum):
                        """
                        HoldAcctStart (Enum Class)

                        Hold Accounting start based on IA\_PD

                        .. data:: ipv6_prefix_delegation = 3

                        	Based on ipv6 delegated prefix

                        """

                        ipv6_prefix_delegation = Enum.YLeaf(3, "ipv6-prefix-delegation")


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart']


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session']['meta_info']


                class IdleTimeout(_Entity_):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\: int
                    
                    	**range:** 60..4320000
                    
                    	**units**\: second
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                            ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                        ])
                        self.timeout_value = None
                        self.threshold = None
                        self.direction = None
                        self._segment_path = lambda: "idle-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, ['timeout_value', 'threshold', 'direction'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting']['meta_info']


            class Qos(_Entity_):
                """
                QoS dynamically applied configuration template
                
                .. attribute:: service_policy
                
                	Service policy to be applied in ingress/egress direction
                	**type**\:  :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy>`
                
                .. attribute:: account
                
                	QoS L2 overhead accounting
                	**type**\:  :py:class:`Account <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account>`
                
                .. attribute:: output
                
                	QoS to be applied in egress direction
                	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output>`
                
                

                """

                _prefix = 'qos-ma-bng-cfg'
                _revision = '2016-04-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos, self).__init__()

                    self.yang_name = "qos"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy)), ("account", ("account", DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account)), ("output", ("output", DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output))])
                    self._leafs = OrderedDict()

                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"

                    self.account = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account()
                    self.account.parent = self
                    self._children_name_map["account"] = "account"

                    self.output = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output()
                    self.output.parent = self
                    self._children_name_map["output"] = "output"
                    self._segment_path = lambda: "Cisco-IOS-XR-qos-ma-bng-cfg:qos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos, [], name, value)


                class ServicePolicy(_Entity_):
                    """
                    Service policy to be applied in ingress/egress
                    direction
                    
                    .. attribute:: input
                    
                    	Subscriber ingress policy
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output
                    
                    	Subscriber egress policy
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("input", ("input", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input)), ("output", ("output", DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output))])
                        self._leafs = OrderedDict()

                        self.input = None
                        self._children_name_map["input"] = "input"

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._segment_path = lambda: "service-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy, [], name, value)


                    class Input(_Entity_):
                        """
                        Subscriber ingress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input']['meta_info']


                    class Output(_Entity_):
                        """
                        Subscriber egress policy
                        
                        .. attribute:: policy_name
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: spi_name
                        
                        	Name of the SPI
                        	**type**\: str
                        
                        .. attribute:: merge
                        
                        	TRUE for merge enabled for service\-policy applied on dynamic template
                        	**type**\: bool
                        
                        .. attribute:: merge_id
                        
                        	Merge ID value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: account_stats
                        
                        	TRUE for account stats enabled for service\-policy applied on dynamic template. Note\: account stats not supported for subscriber type 'ppp' and 'ipsubscriber'
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('spi_name', (YLeaf(YType.str, 'spi-name'), ['str'])),
                                ('merge', (YLeaf(YType.boolean, 'merge'), ['bool'])),
                                ('merge_id', (YLeaf(YType.uint32, 'merge-id'), ['int'])),
                                ('account_stats', (YLeaf(YType.boolean, 'account-stats'), ['bool'])),
                            ])
                            self.policy_name = None
                            self.spi_name = None
                            self.merge = None
                            self.merge_id = None
                            self.account_stats = None
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, ['policy_name', 'spi_name', 'merge', 'merge_id', 'account_stats'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']


                class Account(_Entity_):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:  :py:class:`Qosl2DataLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLink>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:  :py:class:`Qosl2Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2Encap>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\: int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, self).__init__()

                        self.yang_name = "account"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aal', (YLeaf(YType.enumeration, 'aal'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap', '')])),
                            ('atm_cell_tax', (YLeaf(YType.empty, 'atm-cell-tax'), ['Empty'])),
                            ('user_defined', (YLeaf(YType.int32, 'user-defined'), ['int'])),
                        ])
                        self.aal = None
                        self.encapsulation = None
                        self.atm_cell_tax = None
                        self.user_defined = None
                        self._segment_path = lambda: "account"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, ['aal', 'encapsulation', 'atm_cell_tax', 'user_defined'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account']['meta_info']


                class Output(_Entity_):
                    """
                    QoS to be applied in egress direction
                    
                    .. attribute:: minimum_bandwidth
                    
                    	Minimum bandwidth value for the subscriber (in kbps)
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, self).__init__()

                        self.yang_name = "output"
                        self.yang_parent_name = "qos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('minimum_bandwidth', (YLeaf(YType.uint32, 'minimum-bandwidth'), ['int'])),
                        ])
                        self.minimum_bandwidth = None
                        self._segment_path = lambda: "output"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, ['minimum_bandwidth'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']


            class Ipv6Network(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: addresses
                
                	Set the IPv6 address of an interface
                	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses>`
                
                .. attribute:: mtu
                
                	MTU Setting of Interface
                	**type**\: int
                
                	**range:** 1280..65535
                
                	**units**\: byte
                
                .. attribute:: rpf
                
                	TRUE if enabled, FALSE if disabled
                	**type**\: bool
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2017-01-11'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, self).__init__()

                    self.yang_name = "ipv6-network"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addresses", ("addresses", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses))])
                    self._leafs = OrderedDict([
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('rpf', (YLeaf(YType.boolean, 'rpf'), ['bool'])),
                        ('unreachables', (YLeaf(YType.empty, 'unreachables'), ['Empty'])),
                    ])
                    self.mtu = None
                    self.rpf = None
                    self.unreachables = None

                    self.addresses = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, ['mtu', 'rpf', 'unreachables'], name, value)


                class Addresses(_Entity_):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:  :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2017-01-11'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6-network"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auto-configuration", ("auto_configuration", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration))])
                        self._leafs = OrderedDict()

                        self.auto_configuration = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._segment_path = lambda: "addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses, [], name, value)


                    class AutoConfiguration(_Entity_):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2017-01-11'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, self).__init__()

                            self.yang_name = "auto-configuration"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "auto-configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, ['enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info']


            class SpanMonitorSessions(_Entity_):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of  		 :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, self).__init__()

                    self.yang_name = "span-monitor-sessions"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("span-monitor-session", ("span_monitor_session", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession))])
                    self._leafs = OrderedDict()

                    self.span_monitor_session = YList(self)
                    self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, [], name, value)


                class SpanMonitorSession(_Entity_):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  (key)
                    
                    	Session Class
                    	**type**\:  :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: mirror_first
                    
                    	Mirror a specified number of bytes from start of packet
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**units**\: byte
                    
                    .. attribute:: attachment
                    
                    	Attach the interface to a Monitor Session
                    	**type**\:  :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mirror_interval
                    
                    	Specify the mirror interval
                    	**type**\:  :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session_class']
                        self._child_classes = OrderedDict([("attachment", ("attachment", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment)), ("acl", ("acl", DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl))])
                        self._leafs = OrderedDict([
                            ('session_class', (YLeaf(YType.enumeration, 'session-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass', '')])),
                            ('mirror_first', (YLeaf(YType.uint32, 'mirror-first'), ['int'])),
                            ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval', '')])),
                        ])
                        self.session_class = None
                        self.mirror_first = None
                        self.mirror_interval = None

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"

                        self.acl = None
                        self._children_name_map["acl"] = "acl"
                        self._segment_path = lambda: "span-monitor-session" + "[session-class='" + str(self.session_class) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, ['session_class', 'mirror_first', 'mirror_interval'], name, value)


                    class Attachment(_Entity_):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\: str
                        
                        	**length:** 1..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:  :py:class:`SpanTrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirection>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection', '')])),
                                ('port_level_enable', (YLeaf(YType.empty, 'port-level-enable'), ['Empty'])),
                            ])
                            self.session_name = None
                            self.direction = None
                            self.port_level_enable = None
                            self._segment_path = lambda: "attachment"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, ['session_name', 'direction', 'port_level_enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']


                    class Acl(_Entity_):
                        """
                        Enable ACL matching for traffic mirroring
                        
                        .. attribute:: acl_enable
                        
                        	Enable ACL
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        	**length:** 1..80
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl, self).__init__()

                            self.yang_name = "acl"
                            self.yang_parent_name = "span-monitor-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('acl_enable', (YLeaf(YType.empty, 'acl-enable'), ['Empty'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.acl_enable = None
                            self.acl_name = None
                            self._segment_path = lambda: "acl"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl, ['acl_enable', 'acl_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info']


            class Ipv6Neighbor(_Entity_):
                """
                Interface IPv6 Network configuration data
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  :py:class:`RaInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix
                
                	Set the IPv6 framed ipv6 prefix for a subscriber interface 
                	**type**\:  :py:class:`FramedPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: duplicate_address_detection
                
                	Duplicate Address Detection (DAD)
                	**type**\:  :py:class:`DuplicateAddressDetection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:  :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: framed_prefix_pool
                
                	Set the IPv6 framed ipv6 prefix pool for a subscriber interface 
                	**type**\: str
                
                .. attribute:: managed_config
                
                	Host to use stateful protocol for address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_lifetime
                
                	Set IPv6 Router Advertisement (RA) lifetime in seconds
                	**type**\: int
                
                	**range:** 0..9000
                
                	**units**\: second
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:  :py:class:`Ipv6NdRouterPrefTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplate>`
                
                .. attribute:: ra_suppress
                
                	Enable suppress IPv6 router advertisement
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unicast
                
                	Enable RA unicast Flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_unspecify_hoplimit
                
                	Unspecify IPv6 Router Advertisement (RA) hop\-limit
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_suppress_mtu
                
                	RA suppress MTU flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\: int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: ns_interval
                
                	Set advertised NS retransmission interval in milliseconds
                	**type**\: int
                
                	**range:** 1000..4294967295
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, self).__init__()

                    self.yang_name = "ipv6-neighbor"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ra-interval", ("ra_interval", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval)), ("framed-prefix", ("framed_prefix", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix)), ("duplicate-address-detection", ("duplicate_address_detection", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection)), ("ra-initial", ("ra_initial", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial))])
                    self._leafs = OrderedDict([
                        ('framed_prefix_pool', (YLeaf(YType.str, 'framed-prefix-pool'), ['str'])),
                        ('managed_config', (YLeaf(YType.empty, 'managed-config'), ['Empty'])),
                        ('other_config', (YLeaf(YType.empty, 'other-config'), ['Empty'])),
                        ('start_ra_on_ipv6_enable', (YLeaf(YType.empty, 'start-ra-on-ipv6-enable'), ['Empty'])),
                        ('nud_enable', (YLeaf(YType.empty, 'nud-enable'), ['Empty'])),
                        ('ra_lifetime', (YLeaf(YType.uint32, 'ra-lifetime'), ['int'])),
                        ('router_preference', (YLeaf(YType.enumeration, 'router-preference'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate', '')])),
                        ('ra_suppress', (YLeaf(YType.empty, 'ra-suppress'), ['Empty'])),
                        ('ra_unicast', (YLeaf(YType.empty, 'ra-unicast'), ['Empty'])),
                        ('ra_unspecify_hoplimit', (YLeaf(YType.empty, 'ra-unspecify-hoplimit'), ['Empty'])),
                        ('ra_suppress_mtu', (YLeaf(YType.empty, 'ra-suppress-mtu'), ['Empty'])),
                        ('suppress_cache_learning', (YLeaf(YType.empty, 'suppress-cache-learning'), ['Empty'])),
                        ('reachable_time', (YLeaf(YType.uint32, 'reachable-time'), ['int'])),
                        ('ns_interval', (YLeaf(YType.uint32, 'ns-interval'), ['int'])),
                    ])
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.other_config = None
                    self.start_ra_on_ipv6_enable = None
                    self.nud_enable = None
                    self.ra_lifetime = None
                    self.router_preference = None
                    self.ra_suppress = None
                    self.ra_unicast = None
                    self.ra_unspecify_hoplimit = None
                    self.ra_suppress_mtu = None
                    self.suppress_cache_learning = None
                    self.reachable_time = None
                    self.ns_interval = None

                    self.ra_interval = None
                    self._children_name_map["ra_interval"] = "ra-interval"

                    self.framed_prefix = None
                    self._children_name_map["framed_prefix"] = "framed-prefix"

                    self.duplicate_address_detection = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"

                    self.ra_initial = None
                    self._children_name_map["ra_initial"] = "ra-initial"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, ['framed_prefix_pool', 'managed_config', 'other_config', 'start_ra_on_ipv6_enable', 'nud_enable', 'ra_lifetime', 'router_preference', 'ra_suppress', 'ra_unicast', 'ra_unspecify_hoplimit', 'ra_suppress_mtu', 'suppress_cache_learning', 'reachable_time', 'ns_interval'], name, value)


                class RaInterval(_Entity_):
                    """
                    Set IPv6 Router Advertisement (RA) interval in
                    seconds
                    
                    .. attribute:: maximum
                    
                    	Maximum RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: minimum
                    
                    	Minimum RA interval in seconds. Must be less than 0.75 \* maximum interval
                    	**type**\: int
                    
                    	**range:** 3..1800
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, self).__init__()

                        self.yang_name = "ra-interval"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                        ])
                        self.maximum = None
                        self.minimum = None
                        self._segment_path = lambda: "ra-interval"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, ['maximum', 'minimum'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval']['meta_info']


                class FramedPrefix(_Entity_):
                    """
                    Set the IPv6 framed ipv6 prefix for a
                    subscriber interface 
                    
                    .. attribute:: prefix_length
                    
                    	IPv6 framed prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix
                    
                    	IPV6 framed prefix address
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, self).__init__()

                        self.yang_name = "framed-prefix"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ])
                        self.prefix_length = None
                        self.prefix = None
                        self._segment_path = lambda: "framed-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, ['prefix_length', 'prefix'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(_Entity_):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\: int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, self).__init__()

                        self.yang_name = "duplicate-address-detection"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('attempts', (YLeaf(YType.uint32, 'attempts'), ['int'])),
                        ])
                        self.attempts = None
                        self._segment_path = lambda: "duplicate-address-detection"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, ['attempts'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(_Entity_):
                    """
                    IPv6 ND RA Initial
                    
                    .. attribute:: count
                    
                    	Initial RA count
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Initial RA interval in seconds
                    	**type**\: int
                    
                    	**range:** 4..1800
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, self).__init__()

                        self.yang_name = "ra-initial"
                        self.yang_parent_name = "ipv6-neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ])
                        self.count = None
                        self.interval = None
                        self._segment_path = lambda: "ra-initial"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, ['count', 'interval'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']


            class Pbr(_Entity_):
                """
                Dynamic Template PBR configuration
                
                .. attribute:: service_policies
                
                	Ingress service policy
                	**type**\:  :py:class:`ServicePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies>`
                
                .. attribute:: service_policy_in
                
                	Class for subscriber ingress policy
                	**type**\: str
                
                

                """

                _prefix = 'pbr-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, self).__init__()

                    self.yang_name = "pbr"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policies", ("service_policies", DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies))])
                    self._leafs = OrderedDict([
                        ('service_policy_in', (YLeaf(YType.str, 'service-policy-in'), ['str'])),
                    ])
                    self.service_policy_in = None

                    self.service_policies = DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies()
                    self.service_policies.parent = self
                    self._children_name_map["service_policies"] = "service-policies"
                    self._segment_path = lambda: "Cisco-IOS-XR-pbr-subscriber-cfg:pbr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, ['service_policy_in'], name, value)


                class ServicePolicies(_Entity_):
                    """
                    Ingress service policy
                    
                    .. attribute:: service_policy
                    
                    	Service policy details
                    	**type**\: list of  		 :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy>`
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies, self).__init__()

                        self.yang_name = "service-policies"
                        self.yang_parent_name = "pbr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-policy", ("service_policy", DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy))])
                        self._leafs = OrderedDict()

                        self.service_policy = YList(self)
                        self._segment_path = lambda: "service-policies"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies, [], name, value)


                    class ServicePolicy(_Entity_):
                        """
                        Service policy details
                        
                        .. attribute:: service_policy  (key)
                        
                        	Name of policy\-map
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'pbr-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy, self).__init__()

                            self.yang_name = "service-policy"
                            self.yang_parent_name = "service-policies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['service_policy']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('service_policy', (YLeaf(YType.str, 'service-policy'), ['str'])),
                            ])
                            self.service_policy = None
                            self._segment_path = lambda: "service-policy" + "[service-policy='" + str(self.service_policy) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy, ['service_policy'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info']


            class Ipv4PacketFilter(_Entity_):
                """
                IPv4 Packet Filtering configuration for the
                template
                
                .. attribute:: outbound
                
                	IPv4 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound>`
                
                .. attribute:: inbound
                
                	IPv4 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter, self).__init__()

                    self.yang_name = "ipv4-packet-filter"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("outbound", ("outbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound)), ("inbound", ("inbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound))])
                    self._leafs = OrderedDict()

                    self.outbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter, [], name, value)


                class Outbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(_Entity_):
                    """
                    IPv4 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv4 Packet Filter Name to be applied to Inbound packets NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hardware_count
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv4-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('hardware_count', (YLeaf(YType.empty, 'hardware-count'), ['Empty'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, ['common_acl_name', 'name', 'hardware_count', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(_Entity_):
                """
                IPv6 Packet Filtering configuration for the
                interface
                
                .. attribute:: inbound
                
                	IPv6 Packet filter to be applied to inbound packets
                	**type**\:  :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound>`
                
                .. attribute:: outbound
                
                	IPv6 Packet filter to be applied to outbound packets
                	**type**\:  :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound>`
                
                

                """

                _prefix = 'ip-pfilter-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter, self).__init__()

                    self.yang_name = "ipv6-packet-filter"
                    self.yang_parent_name = "subscriber-service"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inbound", ("inbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound)), ("outbound", ("outbound", DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound))])
                    self._leafs = OrderedDict()

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"

                    self.outbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound()
                    self.outbound.parent = self
                    self._children_name_map["outbound"] = "outbound"
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter, [], name, value)


                class Inbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to inbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Inbound  NOTE\: This parameter is mandatory if 'CommonACLName' is not specified
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, self).__init__()

                        self.yang_name = "inbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "inbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(_Entity_):
                    """
                    IPv6 Packet filter to be applied to outbound
                    packets
                    
                    .. attribute:: common_acl_name
                    
                    	Not supported (Leave unspecified)
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: name
                    
                    	IPv6 Packet Filter Name to be applied to Outbound packets
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_statistics
                    
                    	Not supported (Leave unspecified)
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, self).__init__()

                        self.yang_name = "outbound"
                        self.yang_parent_name = "ipv6-packet-filter"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_acl_name', (YLeaf(YType.str, 'common-acl-name'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('interface_statistics', (YLeaf(YType.empty, 'interface-statistics'), ['Empty'])),
                        ])
                        self.common_acl_name = None
                        self.name = None
                        self.interface_statistics = None
                        self._segment_path = lambda: "outbound"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, ['common_acl_name', 'name', 'interface_statistics'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.SubscriberServices']['meta_info']

    def clone_ptr(self):
        self._top_entity = DynamicTemplate()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
        return meta._meta_table['DynamicTemplate']['meta_info']


