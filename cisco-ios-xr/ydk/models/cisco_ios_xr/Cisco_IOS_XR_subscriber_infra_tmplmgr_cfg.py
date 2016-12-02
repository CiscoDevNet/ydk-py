""" Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-infra\-tmplmgr package configuration.

This module contains definitions
for the following management objects\:
  dynamic\-template\: All dynamic template configurations

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class DynamicTemplate(object):
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
        self.ip_subscribers = DynamicTemplate.IpSubscribers()
        self.ip_subscribers.parent = self
        self.ppps = DynamicTemplate.Ppps()
        self.ppps.parent = self
        self.subscriber_services = DynamicTemplate.SubscriberServices()
        self.subscriber_services.parent = self


    class Ppps(object):
        """
        Templates of the PPP Type
        
        .. attribute:: ppp
        
        	A Template of the PPP Type
        	**type**\: list of    :py:class:`Ppp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.ppp = YList()
            self.ppp.parent = self
            self.ppp.name = 'ppp'


        class Ppp(object):
            """
            A Template of the PPP Type
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
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
            
            .. attribute:: qos
            
            	QoS dynamically applied configuration template
            	**type**\:   :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Qos>`
            
            .. attribute:: span_monitor_sessions
            
            	Monitor Session container for this template
            	**type**\:   :py:class:`SpanMonitorSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions>`
            
            .. attribute:: vrf
            
            	Assign the interface to a VRF 
            	**type**\:  str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.template_name = None
                self.dhcpv6 = DynamicTemplate.Ppps.Ppp.Dhcpv6()
                self.dhcpv6.parent = self
                self.igmp = DynamicTemplate.Ppps.Ppp.Igmp()
                self.igmp.parent = self
                self.ipv4_network = DynamicTemplate.Ppps.Ppp.Ipv4Network()
                self.ipv4_network.parent = self
                self.ipv4_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self.ipv6_neighbor = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self.ipv6_network = DynamicTemplate.Ppps.Ppp.Ipv6Network()
                self.ipv6_network.parent = self
                self.ipv6_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self.pbr = DynamicTemplate.Ppps.Ppp.Pbr()
                self.pbr.parent = self
                self.qos = DynamicTemplate.Ppps.Ppp.Qos()
                self.qos.parent = self
                self.span_monitor_sessions = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self.vrf = None


            class SpanMonitorSessions(object):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.span_monitor_session = YList()
                    self.span_monitor_session.parent = self
                    self.span_monitor_session.name = 'span_monitor_session'


                class SpanMonitorSession(object):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorIntervalEnum>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session_class = None
                        self.acl = None
                        self.attachment = None
                        self.mirror_first = None
                        self.mirror_interval = None


                    class Attachment(object):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirectionEnum>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**range:** 0..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.direction = None
                            self.port_level_enable = None
                            self.session_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:attachment'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.direction is not None:
                                return True

                            if self.port_level_enable is not None:
                                return True

                            if self.session_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.session_class is None:
                            raise YPYModelError('Key property session_class is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-session[Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:session-class = ' + str(self.session_class) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.session_class is not None:
                            return True

                        if self.acl is not None:
                            return True

                        if self.attachment is not None and self.attachment._has_data():
                            return True

                        if self.mirror_first is not None:
                            return True

                        if self.mirror_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.span_monitor_session is not None:
                        for child_ref in self.span_monitor_session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info']


            class Ipv4PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']


            class Igmp(object):
                """
                IGMPconfiguration
                
                .. attribute:: default_vrf
                
                	Default VRF
                	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf>`
                
                

                """

                _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.default_vrf = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf()
                    self.default_vrf.parent = self


                class DefaultVrf(object):
                    """
                    Default VRF
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access\-list group range
                    	**type**\:  str
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: max_groups
                    
                    	IGMP Max Groups
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: multicast
                    
                    	Configure Multicast mode variable
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**default value**\: 10
                    
                    .. attribute:: robustness
                    
                    	Configure IGMP Robustness variable
                    	**type**\:  int
                    
                    	**range:** 2..10
                    
                    	**default value**\: 2
                    
                    .. attribute:: version
                    
                    	IGMP Version
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.access_group = None
                        self.explicit_tracking = None
                        self.max_groups = None
                        self.multicast = None
                        self.query_interval = None
                        self.query_max_response_time = None
                        self.robustness = None
                        self.version = None


                    class ExplicitTracking(object):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        .. attribute:: enable
                        
                        	Enable or disable, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-dyn-tmpl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:explicit-tracking'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:default-vrf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.access_group is not None:
                            return True

                        if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                            return True

                        if self.max_groups is not None:
                            return True

                        if self.multicast is not None:
                            return True

                        if self.query_interval is not None:
                            return True

                        if self.query_max_response_time is not None:
                            return True

                        if self.robustness is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.default_vrf is not None and self.default_vrf._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info']


            class Ipv4Network(object):
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
                    self.parent = None
                    self.mtu = None
                    self.rpf = None
                    self.unnumbered = None
                    self.unreachables = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mtu is not None:
                        return True

                    if self.rpf is not None:
                        return True

                    if self.unnumbered is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv4Network']['meta_info']


            class Ipv6Network(object):
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
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: verify
                
                	IPv6 Verify Unicast Souce Reachable
                	**type**\:   :py:class:`Ipv6ReachableViaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg.Ipv6ReachableViaEnum>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.addresses = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self.mtu = None
                    self.unreachables = None
                    self.verify = None


                class Addresses(object):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.auto_configuration = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self


                    class AutoConfiguration(object):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:auto-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.auto_configuration is not None and self.auto_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.addresses is not None and self.addresses._has_data():
                        return True

                    if self.mtu is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    if self.verify is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info']


            class Ipv6Neighbor(object):
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
                
                	**range:** 1000..3600000
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_hop_limit
                
                	IPv6 ND RA HopLimit
                	**type**\:   :py:class:`Ipv6NdHopLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdHopLimitEnum>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  int
                
                	**range:** 3..1800
                
                	**units**\: second
                
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
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplateEnum>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.duplicate_address_detection = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self.framed_prefix = None
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.ns_interval = None
                    self.nud_enable = None
                    self.other_config = None
                    self.ra_hop_limit = None
                    self.ra_initial = None
                    self.ra_interval = None
                    self.ra_lifetime = None
                    self.ra_suppress = None
                    self.ra_suppress_mtu = None
                    self.ra_unicast = None
                    self.reachable_time = None
                    self.router_preference = None
                    self.start_ra_on_ipv6_enable = None
                    self.suppress_cache_learning = None


                class FramedPrefix(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:framed-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(object):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attempts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:duplicate-address-detection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attempts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.count = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ra-initial'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.count is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.duplicate_address_detection is not None and self.duplicate_address_detection._has_data():
                        return True

                    if self.framed_prefix is not None and self.framed_prefix._has_data():
                        return True

                    if self.framed_prefix_pool is not None:
                        return True

                    if self.managed_config is not None:
                        return True

                    if self.ns_interval is not None:
                        return True

                    if self.nud_enable is not None:
                        return True

                    if self.other_config is not None:
                        return True

                    if self.ra_hop_limit is not None:
                        return True

                    if self.ra_initial is not None and self.ra_initial._has_data():
                        return True

                    if self.ra_interval is not None:
                        return True

                    if self.ra_lifetime is not None:
                        return True

                    if self.ra_suppress is not None:
                        return True

                    if self.ra_suppress_mtu is not None:
                        return True

                    if self.ra_unicast is not None:
                        return True

                    if self.reachable_time is not None:
                        return True

                    if self.router_preference is not None:
                        return True

                    if self.start_ra_on_ipv6_enable is not None:
                        return True

                    if self.suppress_cache_learning is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']


            class Dhcpv6(object):
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
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address_pool = None
                    self.class_ = None
                    self.delegated_prefix = None
                    self.delegated_prefix_pool = None
                    self.dns_ipv6address = None
                    self.stateful_address = None


                class DelegatedPrefix(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:delegated-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_pool is not None:
                        return True

                    if self.class_ is not None:
                        return True

                    if self.delegated_prefix is not None and self.delegated_prefix._has_data():
                        return True

                    if self.delegated_prefix_pool is not None:
                        return True

                    if self.dns_ipv6address is not None:
                        return True

                    if self.stateful_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info']


            class Pbr(object):
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
                    self.parent = None
                    self.service_policy = DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self.service_policy_in = None


                class ServicePolicy(object):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.input = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:pbr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    if self.service_policy_in is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info']


            class Qos(object):
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
                    self.parent = None
                    self.account = DynamicTemplate.Ppps.Ppp.Qos.Account()
                    self.account.parent = self
                    self.output = DynamicTemplate.Ppps.Ppp.Qos.Output()
                    self.output.parent = self
                    self.service_policy = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy()
                    self.service_policy.parent = self


                class ServicePolicy(object):
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
                        self.parent = None
                        self.input = None
                        self.output = None


                    class Input(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input']['meta_info']


                    class Output(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None and self.input._has_data():
                            return True

                        if self.output is not None and self.output._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']


                class Account(object):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLinkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLinkEnum>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2EncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2EncapEnum>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        self.parent = None
                        self.aal = None
                        self.atm_cell_tax = None
                        self.encapsulation = None
                        self.user_defined = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:account'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.aal is not None:
                            return True

                        if self.atm_cell_tax is not None:
                            return True

                        if self.encapsulation is not None:
                            return True

                        if self.user_defined is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.Account']['meta_info']


                class Output(object):
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
                        self.parent = None
                        self.minimum_bandwidth = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.minimum_bandwidth is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos.Output']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:qos'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.account is not None and self.account._has_data():
                        return True

                    if self.output is not None and self.output._has_data():
                        return True

                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']

            @property
            def _common_path(self):
                if self.template_name is None:
                    raise YPYModelError('Key property template_name is None')

                return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ppps/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ppp[Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:template-name = ' + str(self.template_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.template_name is not None:
                    return True

                if self.dhcpv6 is not None and self.dhcpv6._has_data():
                    return True

                if self.igmp is not None and self.igmp._has_data():
                    return True

                if self.ipv4_network is not None and self.ipv4_network._has_data():
                    return True

                if self.ipv4_packet_filter is not None and self.ipv4_packet_filter._has_data():
                    return True

                if self.ipv6_neighbor is not None and self.ipv6_neighbor._has_data():
                    return True

                if self.ipv6_network is not None and self.ipv6_network._has_data():
                    return True

                if self.ipv6_packet_filter is not None and self.ipv6_packet_filter._has_data():
                    return True

                if self.pbr is not None and self.pbr._has_data():
                    return True

                if self.qos is not None and self.qos._has_data():
                    return True

                if self.span_monitor_sessions is not None and self.span_monitor_sessions._has_data():
                    return True

                if self.vrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ppps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ppp is not None:
                for child_ref in self.ppp:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.Ppps']['meta_info']


    class IpSubscribers(object):
        """
        The IP Subscriber Template Table
        
        .. attribute:: ip_subscriber
        
        	A IP Subscriber Type Template 
        	**type**\: list of    :py:class:`IpSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.ip_subscriber = YList()
            self.ip_subscriber.parent = self
            self.ip_subscriber.name = 'ip_subscriber'


        class IpSubscriber(object):
            """
            A IP Subscriber Type Template 
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: dhcpv6
            
            	Interface dhcpv6 configuration data
            	**type**\:   :py:class:`Dhcpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6>`
            
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
            
            	**range:** 0..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.template_name = None
                self.dhcpv6 = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6()
                self.dhcpv6.parent = self
                self.ipv4_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network()
                self.ipv4_network.parent = self
                self.ipv4_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self.ipv6_neighbor = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self.ipv6_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network()
                self.ipv6_network.parent = self
                self.ipv6_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self.pbr = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr()
                self.pbr.parent = self
                self.qos = DynamicTemplate.IpSubscribers.IpSubscriber.Qos()
                self.qos.parent = self
                self.span_monitor_sessions = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self.vrf = None


            class SpanMonitorSessions(object):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.span_monitor_session = YList()
                    self.span_monitor_session.parent = self
                    self.span_monitor_session.name = 'span_monitor_session'


                class SpanMonitorSession(object):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorIntervalEnum>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session_class = None
                        self.acl = None
                        self.attachment = None
                        self.mirror_first = None
                        self.mirror_interval = None


                    class Attachment(object):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirectionEnum>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**range:** 0..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.direction = None
                            self.port_level_enable = None
                            self.session_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:attachment'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.direction is not None:
                                return True

                            if self.port_level_enable is not None:
                                return True

                            if self.session_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.session_class is None:
                            raise YPYModelError('Key property session_class is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-session[Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:session-class = ' + str(self.session_class) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.session_class is not None:
                            return True

                        if self.acl is not None:
                            return True

                        if self.attachment is not None and self.attachment._has_data():
                            return True

                        if self.mirror_first is not None:
                            return True

                        if self.mirror_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.span_monitor_session is not None:
                        for child_ref in self.span_monitor_session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info']


            class Ipv4PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']


            class Ipv4Network(object):
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
                    self.parent = None
                    self.mtu = None
                    self.rpf = None
                    self.unnumbered = None
                    self.unreachables = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mtu is not None:
                        return True

                    if self.rpf is not None:
                        return True

                    if self.unnumbered is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network']['meta_info']


            class Ipv6Network(object):
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
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: verify
                
                	IPv6 Verify Unicast Souce Reachable
                	**type**\:   :py:class:`Ipv6ReachableViaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg.Ipv6ReachableViaEnum>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.addresses = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self.mtu = None
                    self.unreachables = None
                    self.verify = None


                class Addresses(object):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.auto_configuration = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self


                    class AutoConfiguration(object):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:auto-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.auto_configuration is not None and self.auto_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.addresses is not None and self.addresses._has_data():
                        return True

                    if self.mtu is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    if self.verify is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info']


            class Ipv6Neighbor(object):
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
                
                	**range:** 1000..3600000
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_hop_limit
                
                	IPv6 ND RA HopLimit
                	**type**\:   :py:class:`Ipv6NdHopLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdHopLimitEnum>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  int
                
                	**range:** 3..1800
                
                	**units**\: second
                
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
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplateEnum>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.duplicate_address_detection = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self.framed_prefix = None
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.ns_interval = None
                    self.nud_enable = None
                    self.other_config = None
                    self.ra_hop_limit = None
                    self.ra_initial = None
                    self.ra_interval = None
                    self.ra_lifetime = None
                    self.ra_suppress = None
                    self.ra_suppress_mtu = None
                    self.ra_unicast = None
                    self.reachable_time = None
                    self.router_preference = None
                    self.start_ra_on_ipv6_enable = None
                    self.suppress_cache_learning = None


                class FramedPrefix(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:framed-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(object):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attempts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:duplicate-address-detection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attempts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.count = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ra-initial'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.count is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.duplicate_address_detection is not None and self.duplicate_address_detection._has_data():
                        return True

                    if self.framed_prefix is not None and self.framed_prefix._has_data():
                        return True

                    if self.framed_prefix_pool is not None:
                        return True

                    if self.managed_config is not None:
                        return True

                    if self.ns_interval is not None:
                        return True

                    if self.nud_enable is not None:
                        return True

                    if self.other_config is not None:
                        return True

                    if self.ra_hop_limit is not None:
                        return True

                    if self.ra_initial is not None and self.ra_initial._has_data():
                        return True

                    if self.ra_interval is not None:
                        return True

                    if self.ra_lifetime is not None:
                        return True

                    if self.ra_suppress is not None:
                        return True

                    if self.ra_suppress_mtu is not None:
                        return True

                    if self.ra_unicast is not None:
                        return True

                    if self.reachable_time is not None:
                        return True

                    if self.router_preference is not None:
                        return True

                    if self.start_ra_on_ipv6_enable is not None:
                        return True

                    if self.suppress_cache_learning is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']


            class Dhcpv6(object):
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
                
                .. attribute:: stateful_address
                
                	Stateful IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address_pool = None
                    self.class_ = None
                    self.delegated_prefix = None
                    self.delegated_prefix_pool = None
                    self.dns_ipv6address = None
                    self.stateful_address = None


                class DelegatedPrefix(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-new-dhcpv6d-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:delegated-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_pool is not None:
                        return True

                    if self.class_ is not None:
                        return True

                    if self.delegated_prefix is not None and self.delegated_prefix._has_data():
                        return True

                    if self.delegated_prefix_pool is not None:
                        return True

                    if self.dns_ipv6address is not None:
                        return True

                    if self.stateful_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info']


            class Pbr(object):
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
                    self.parent = None
                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self.service_policy_in = None


                class ServicePolicy(object):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.input = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:pbr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    if self.service_policy_in is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info']


            class Qos(object):
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
                    self.parent = None
                    self.account = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account()
                    self.account.parent = self
                    self.output = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output()
                    self.output.parent = self
                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy()
                    self.service_policy.parent = self


                class ServicePolicy(object):
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
                        self.parent = None
                        self.input = None
                        self.output = None


                    class Input(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input']['meta_info']


                    class Output(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None and self.input._has_data():
                            return True

                        if self.output is not None and self.output._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']


                class Account(object):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLinkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLinkEnum>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2EncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2EncapEnum>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        self.parent = None
                        self.aal = None
                        self.atm_cell_tax = None
                        self.encapsulation = None
                        self.user_defined = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:account'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.aal is not None:
                            return True

                        if self.atm_cell_tax is not None:
                            return True

                        if self.encapsulation is not None:
                            return True

                        if self.user_defined is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account']['meta_info']


                class Output(object):
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
                        self.parent = None
                        self.minimum_bandwidth = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.minimum_bandwidth is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:qos'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.account is not None and self.account._has_data():
                        return True

                    if self.output is not None and self.output._has_data():
                        return True

                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']

            @property
            def _common_path(self):
                if self.template_name is None:
                    raise YPYModelError('Key property template_name is None')

                return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ip-subscribers/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ip-subscriber[Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:template-name = ' + str(self.template_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.template_name is not None:
                    return True

                if self.dhcpv6 is not None and self.dhcpv6._has_data():
                    return True

                if self.ipv4_network is not None and self.ipv4_network._has_data():
                    return True

                if self.ipv4_packet_filter is not None and self.ipv4_packet_filter._has_data():
                    return True

                if self.ipv6_neighbor is not None and self.ipv6_neighbor._has_data():
                    return True

                if self.ipv6_network is not None and self.ipv6_network._has_data():
                    return True

                if self.ipv6_packet_filter is not None and self.ipv6_packet_filter._has_data():
                    return True

                if self.pbr is not None and self.pbr._has_data():
                    return True

                if self.qos is not None and self.qos._has_data():
                    return True

                if self.span_monitor_sessions is not None and self.span_monitor_sessions._has_data():
                    return True

                if self.vrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:ip-subscribers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ip_subscriber is not None:
                for child_ref in self.ip_subscriber:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.IpSubscribers']['meta_info']


    class SubscriberServices(object):
        """
        The Service Type Template Table
        
        .. attribute:: subscriber_service
        
        	A Service Type Template 
        	**type**\: list of    :py:class:`SubscriberService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService>`
        
        

        """

        _prefix = 'subscriber-infra-tmplmgr-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.subscriber_service = YList()
            self.subscriber_service.parent = self
            self.subscriber_service.name = 'subscriber_service'


        class SubscriberService(object):
            """
            A Service Type Template 
            
            .. attribute:: template_name  <key>
            
            	The name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
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
            
            	**range:** 0..32
            
            

            """

            _prefix = 'subscriber-infra-tmplmgr-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.template_name = None
                self.ipv4_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network()
                self.ipv4_network.parent = self
                self.ipv4_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter()
                self.ipv4_packet_filter.parent = self
                self.ipv6_neighbor = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor()
                self.ipv6_neighbor.parent = self
                self.ipv6_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network()
                self.ipv6_network.parent = self
                self.ipv6_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter()
                self.ipv6_packet_filter.parent = self
                self.pbr = DynamicTemplate.SubscriberServices.SubscriberService.Pbr()
                self.pbr.parent = self
                self.qos = DynamicTemplate.SubscriberServices.SubscriberService.Qos()
                self.qos.parent = self
                self.span_monitor_sessions = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions()
                self.span_monitor_sessions.parent = self
                self.vrf = None


            class SpanMonitorSessions(object):
                """
                Monitor Session container for this template
                
                .. attribute:: span_monitor_session
                
                	Configuration for a particular class of Monitor Session
                	**type**\: list of    :py:class:`SpanMonitorSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession>`
                
                

                """

                _prefix = 'ethernet-span-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.span_monitor_session = YList()
                    self.span_monitor_session.parent = self
                    self.span_monitor_session.name = 'span_monitor_session'


                class SpanMonitorSession(object):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClassEnum>`
                    
                    .. attribute:: acl
                    
                    	Enable ACL matching for traffic mirroring
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorIntervalEnum>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session_class = None
                        self.acl = None
                        self.attachment = None
                        self.mirror_first = None
                        self.mirror_interval = None


                    class Attachment(object):
                        """
                        Attach the interface to a Monitor Session
                        
                        .. attribute:: direction
                        
                        	Specify the direction of traffic to replicate (optional)
                        	**type**\:   :py:class:`SpanTrafficDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanTrafficDirectionEnum>`
                        
                        .. attribute:: port_level_enable
                        
                        	Enable port level traffic mirroring
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: session_name
                        
                        	Session Name
                        	**type**\:  str
                        
                        	**range:** 0..79
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-span-subscriber-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.direction = None
                            self.port_level_enable = None
                            self.session_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:attachment'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.direction is not None:
                                return True

                            if self.port_level_enable is not None:
                                return True

                            if self.session_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.session_class is None:
                            raise YPYModelError('Key property session_class is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-session[Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:session-class = ' + str(self.session_class) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.session_class is not None:
                            return True

                        if self.acl is not None:
                            return True

                        if self.attachment is not None and self.attachment._has_data():
                            return True

                        if self.mirror_first is not None:
                            return True

                        if self.mirror_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.span_monitor_session is not None:
                        for child_ref in self.span_monitor_session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info']


            class Ipv4PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound']['meta_info']


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.hardware_count = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.hardware_count is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']


            class Ipv6PacketFilter(object):
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
                    self.parent = None
                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self.outbound = None


                class Inbound(object):
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
                    
                    	**range:** 0..65
                    
                    

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:inbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound']['meta_info']


                class Outbound(object):
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
                    
                    	**range:** 0..65
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-pfilter-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.common_acl_name = None
                        self.interface_statistics = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:outbound'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.common_acl_name is not None:
                            return True

                        if self.interface_statistics is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inbound is not None and self.inbound._has_data():
                        return True

                    if self.outbound is not None and self.outbound._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']


            class Ipv4Network(object):
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
                    self.parent = None
                    self.mtu = None
                    self.rpf = None
                    self.unnumbered = None
                    self.unreachables = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mtu is not None:
                        return True

                    if self.rpf is not None:
                        return True

                    if self.unnumbered is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network']['meta_info']


            class Ipv6Network(object):
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
                
                .. attribute:: unreachables
                
                	Override Sending of ICMP Unreachable Messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: verify
                
                	IPv6 Verify Unicast Souce Reachable
                	**type**\:   :py:class:`Ipv6ReachableViaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg.Ipv6ReachableViaEnum>`
                
                

                """

                _prefix = 'ipv6-ma-subscriber-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.addresses = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self.mtu = None
                    self.unreachables = None
                    self.verify = None


                class Addresses(object):
                    """
                    Set the IPv6 address of an interface
                    
                    .. attribute:: auto_configuration
                    
                    	Auto IPv6 Interface Configuration
                    	**type**\:   :py:class:`AutoConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-subscriber-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.auto_configuration = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self


                    class AutoConfiguration(object):
                        """
                        Auto IPv6 Interface Configuration
                        
                        .. attribute:: enable
                        
                        	The flag to enable auto ipv6 interface configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-subscriber-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:auto-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.auto_configuration is not None and self.auto_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.addresses is not None and self.addresses._has_data():
                        return True

                    if self.mtu is not None:
                        return True

                    if self.unreachables is not None:
                        return True

                    if self.verify is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info']


            class Ipv6Neighbor(object):
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
                
                	**range:** 1000..3600000
                
                	**units**\: millisecond
                
                .. attribute:: nud_enable
                
                	NUD enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: other_config
                
                	Host to use stateful protocol for non\-address configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ra_hop_limit
                
                	IPv6 ND RA HopLimit
                	**type**\:   :py:class:`Ipv6NdHopLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdHopLimitEnum>`
                
                .. attribute:: ra_initial
                
                	IPv6 ND RA Initial
                	**type**\:   :py:class:`RaInitial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg.DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial>`
                
                	**presence node**\: True
                
                .. attribute:: ra_interval
                
                	Set IPv6 Router Advertisement (RA) interval in seconds
                	**type**\:  int
                
                	**range:** 3..1800
                
                	**units**\: second
                
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
                
                .. attribute:: reachable_time
                
                	Set advertised reachability time in milliseconds
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: millisecond
                
                .. attribute:: router_preference
                
                	RA Router Preference
                	**type**\:   :py:class:`Ipv6NdRouterPrefTemplateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg.Ipv6NdRouterPrefTemplateEnum>`
                
                .. attribute:: start_ra_on_ipv6_enable
                
                	Start RA on ipv6\-enable config
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_cache_learning
                
                	Suppress cache learning flag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-nd-subscriber-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.duplicate_address_detection = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection()
                    self.duplicate_address_detection.parent = self
                    self.framed_prefix = None
                    self.framed_prefix_pool = None
                    self.managed_config = None
                    self.ns_interval = None
                    self.nud_enable = None
                    self.other_config = None
                    self.ra_hop_limit = None
                    self.ra_initial = None
                    self.ra_interval = None
                    self.ra_lifetime = None
                    self.ra_suppress = None
                    self.ra_suppress_mtu = None
                    self.ra_unicast = None
                    self.reachable_time = None
                    self.router_preference = None
                    self.start_ra_on_ipv6_enable = None
                    self.suppress_cache_learning = None


                class FramedPrefix(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.prefix = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:framed-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix']['meta_info']


                class DuplicateAddressDetection(object):
                    """
                    Duplicate Address Detection (DAD)
                    
                    .. attribute:: attempts
                    
                    	Set IPv6 duplicate address detection transmits
                    	**type**\:  int
                    
                    	**range:** 0..600
                    
                    

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attempts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:duplicate-address-detection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attempts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection']['meta_info']


                class RaInitial(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv6-nd-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.count = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ra-initial'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.count is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.duplicate_address_detection is not None and self.duplicate_address_detection._has_data():
                        return True

                    if self.framed_prefix is not None and self.framed_prefix._has_data():
                        return True

                    if self.framed_prefix_pool is not None:
                        return True

                    if self.managed_config is not None:
                        return True

                    if self.ns_interval is not None:
                        return True

                    if self.nud_enable is not None:
                        return True

                    if self.other_config is not None:
                        return True

                    if self.ra_hop_limit is not None:
                        return True

                    if self.ra_initial is not None and self.ra_initial._has_data():
                        return True

                    if self.ra_interval is not None:
                        return True

                    if self.ra_lifetime is not None:
                        return True

                    if self.ra_suppress is not None:
                        return True

                    if self.ra_suppress_mtu is not None:
                        return True

                    if self.ra_unicast is not None:
                        return True

                    if self.reachable_time is not None:
                        return True

                    if self.router_preference is not None:
                        return True

                    if self.start_ra_on_ipv6_enable is not None:
                        return True

                    if self.suppress_cache_learning is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']


            class Pbr(object):
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
                    self.parent = None
                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self.service_policy_in = None


                class ServicePolicy(object):
                    """
                    PBR service policy configuration
                    
                    .. attribute:: input
                    
                    	Ingress service policy
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'pbr-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.input = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pbr-subscriber-cfg:pbr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    if self.service_policy_in is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info']


            class Qos(object):
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
                    self.parent = None
                    self.account = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account()
                    self.account.parent = self
                    self.output = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output()
                    self.output.parent = self
                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy()
                    self.service_policy.parent = self


                class ServicePolicy(object):
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
                        self.parent = None
                        self.input = None
                        self.output = None


                    class Input(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input']['meta_info']


                    class Output(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'qos-ma-bng-cfg'
                        _revision = '2016-04-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.account_stats = None
                            self.merge = None
                            self.merge_id = None
                            self.policy_name = None
                            self.spi_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.account_stats is not None:
                                return True

                            if self.merge is not None:
                                return True

                            if self.merge_id is not None:
                                return True

                            if self.policy_name is not None:
                                return True

                            if self.spi_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                            return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None and self.input._has_data():
                            return True

                        if self.output is not None and self.output._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']


                class Account(object):
                    """
                    QoS L2 overhead accounting
                    
                    .. attribute:: aal
                    
                    	ATM adaptation layer AAL
                    	**type**\:   :py:class:`Qosl2DataLinkEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2DataLinkEnum>`
                    
                    .. attribute:: atm_cell_tax
                    
                    	ATM cell tax to L2 overhead
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: encapsulation
                    
                    	Specify encapsulation type
                    	**type**\:   :py:class:`Qosl2EncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg.Qosl2EncapEnum>`
                    
                    .. attribute:: user_defined
                    
                    	Numeric L2 overhead offset
                    	**type**\:  int
                    
                    	**range:** \-63..63
                    
                    

                    """

                    _prefix = 'qos-ma-bng-cfg'
                    _revision = '2016-04-01'

                    def __init__(self):
                        self.parent = None
                        self.aal = None
                        self.atm_cell_tax = None
                        self.encapsulation = None
                        self.user_defined = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:account'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.aal is not None:
                            return True

                        if self.atm_cell_tax is not None:
                            return True

                        if self.encapsulation is not None:
                            return True

                        if self.user_defined is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account']['meta_info']


                class Output(object):
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
                        self.parent = None
                        self.minimum_bandwidth = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:output'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.minimum_bandwidth is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                        return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-qos-ma-bng-cfg:qos'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.account is not None and self.account._has_data():
                        return True

                    if self.output is not None and self.output._has_data():
                        return True

                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                    return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']

            @property
            def _common_path(self):
                if self.template_name is None:
                    raise YPYModelError('Key property template_name is None')

                return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:subscriber-services/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:subscriber-service[Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:template-name = ' + str(self.template_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.template_name is not None:
                    return True

                if self.ipv4_network is not None and self.ipv4_network._has_data():
                    return True

                if self.ipv4_packet_filter is not None and self.ipv4_packet_filter._has_data():
                    return True

                if self.ipv6_neighbor is not None and self.ipv6_neighbor._has_data():
                    return True

                if self.ipv6_network is not None and self.ipv6_network._has_data():
                    return True

                if self.ipv6_packet_filter is not None and self.ipv6_packet_filter._has_data():
                    return True

                if self.pbr is not None and self.pbr._has_data():
                    return True

                if self.qos is not None and self.qos._has_data():
                    return True

                if self.span_monitor_sessions is not None and self.span_monitor_sessions._has_data():
                    return True

                if self.vrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
                return meta._meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:subscriber-services'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.subscriber_service is not None:
                for child_ref in self.subscriber_service:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
            return meta._meta_table['DynamicTemplate.SubscriberServices']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ip_subscribers is not None and self.ip_subscribers._has_data():
            return True

        if self.ppps is not None and self.ppps._has_data():
            return True

        if self.subscriber_services is not None and self.subscriber_services._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg as meta
        return meta._meta_table['DynamicTemplate']['meta_info']


