""" Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-infra\-tmplmgr package configuration.

This module contains definitions
for the following management objects\:
  dynamic\-template\: All dynamic template configurations

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.ppp = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DynamicTemplate.Ppps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DynamicTemplate.Ppps, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("template_name",
                                "vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DynamicTemplate.Ppps.Ppp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DynamicTemplate.Ppps.Ppp, self).__setattr__(name, value)


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

                    self.span_monitor_session = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions, self).__setattr__(name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.acl = YLeaf(YType.empty, "acl")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_class",
                                        "acl",
                                        "mirror_first",
                                        "mirror_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "port_level_enable",
                                            "session_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.port_level_enable.is_set or
                                self.session_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.port_level_enable.yfilter != YFilter.not_set or
                                self.session_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "attachment" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.port_level_enable.is_set or self.port_level_enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_level_enable.get_name_leafdata())
                            if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "port-level-enable" or name == "session-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-level-enable"):
                                self.port_level_enable = value
                                self.port_level_enable.value_namespace = name_space
                                self.port_level_enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-name"):
                                self.session_name = value
                                self.session_name.value_namespace = name_space
                                self.session_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.session_class.is_set or
                            self.acl.is_set or
                            self.mirror_first.is_set or
                            self.mirror_interval.is_set or
                            (self.attachment is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_class.yfilter != YFilter.not_set or
                            self.acl.yfilter != YFilter.not_set or
                            self.mirror_first.yfilter != YFilter.not_set or
                            self.mirror_interval.yfilter != YFilter.not_set or
                            (self.attachment is not None and self.attachment.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "span-monitor-session" + "[session-class='" + self.session_class.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_class.is_set or self.session_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_class.get_name_leafdata())
                        if (self.acl.is_set or self.acl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl.get_name_leafdata())
                        if (self.mirror_first.is_set or self.mirror_first.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_first.get_name_leafdata())
                        if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "attachment"):
                            if (self.attachment is None):
                                self.attachment = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment()
                                self.attachment.parent = self
                                self._children_name_map["attachment"] = "attachment"
                            return self.attachment

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attachment" or name == "session-class" or name == "acl" or name == "mirror-first" or name == "mirror-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-class"):
                            self.session_class = value
                            self.session_class.value_namespace = name_space
                            self.session_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl"):
                            self.acl = value
                            self.acl.value_namespace = name_space
                            self.acl.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-first"):
                            self.mirror_first = value
                            self.mirror_first.value_namespace = name_space
                            self.mirror_first.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-interval"):
                            self.mirror_interval = value
                            self.mirror_interval.value_namespace = name_space
                            self.mirror_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.span_monitor_session:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.span_monitor_session:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "span-monitor-session"):
                        for c in self.span_monitor_session:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.span_monitor_session.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "span-monitor-session"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.default_vrf = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._children_yang_names.add("default-vrf")


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

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.max_groups = YLeaf(YType.uint32, "max-groups")

                        self.multicast_mode = YLeaf(YType.enumeration, "multicast-mode")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_group",
                                        "max_groups",
                                        "multicast_mode",
                                        "query_interval",
                                        "query_max_response_time",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.enable.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "explicit-tracking" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.access_group.is_set or
                            self.max_groups.is_set or
                            self.multicast_mode.is_set or
                            self.query_interval.is_set or
                            self.query_max_response_time.is_set or
                            self.version.is_set or
                            (self.explicit_tracking is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_group.yfilter != YFilter.not_set or
                            self.max_groups.yfilter != YFilter.not_set or
                            self.multicast_mode.yfilter != YFilter.not_set or
                            self.query_interval.yfilter != YFilter.not_set or
                            self.query_max_response_time.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            (self.explicit_tracking is not None and self.explicit_tracking.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "default-vrf" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_group.get_name_leafdata())
                        if (self.max_groups.is_set or self.max_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_groups.get_name_leafdata())
                        if (self.multicast_mode.is_set or self.multicast_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_mode.get_name_leafdata())
                        if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_interval.get_name_leafdata())
                        if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "explicit-tracking"):
                            if (self.explicit_tracking is None):
                                self.explicit_tracking = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking()
                                self.explicit_tracking.parent = self
                                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                            return self.explicit_tracking

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "explicit-tracking" or name == "access-group" or name == "max-groups" or name == "multicast-mode" or name == "query-interval" or name == "query-max-response-time" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-group"):
                            self.access_group = value
                            self.access_group.value_namespace = name_space
                            self.access_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-groups"):
                            self.max_groups = value
                            self.max_groups.value_namespace = name_space
                            self.max_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-mode"):
                            self.multicast_mode = value
                            self.multicast_mode.value_namespace = name_space
                            self.multicast_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-interval"):
                            self.query_interval = value
                            self.query_interval.value_namespace = name_space
                            self.query_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-max-response-time"):
                            self.query_max_response_time = value
                            self.query_max_response_time.value_namespace = name_space
                            self.query_max_response_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.default_vrf is not None and self.default_vrf.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.default_vrf is not None and self.default_vrf.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "default-vrf"):
                        if (self.default_vrf is None):
                            self.default_vrf = DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf()
                            self.default_vrf.parent = self
                            self._children_name_map["default_vrf"] = "default-vrf"
                        return self.default_vrf

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "default-vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unnumbered",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Ipv4Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Ipv4Network, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unnumbered.is_set or
                        self.unreachables.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unnumbered.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unnumbered.is_set or self.unnumbered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unnumbered.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mtu" or name == "rpf" or name == "unnumbered" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unnumbered"):
                        self.unnumbered = value
                        self.unnumbered.value_namespace = name_space
                        self.unnumbered.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Network, self).__setattr__(name, value)


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

                        self.auto_configuration = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")


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

                            self.enable = YLeaf(YType.empty, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)

                        def has_data(self):
                            return self.enable.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.auto_configuration is not None and self.auto_configuration.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.auto_configuration is not None and self.auto_configuration.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "addresses" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "auto-configuration"):
                            if (self.auto_configuration is None):
                                self.auto_configuration = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration()
                                self.auto_configuration.parent = self
                                self._children_name_map["auto_configuration"] = "auto-configuration"
                            return self.auto_configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auto-configuration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unreachables.is_set or
                        (self.addresses is not None and self.addresses.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set or
                        (self.addresses is not None and self.addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "addresses"):
                        if (self.addresses is None):
                            self.addresses = DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses()
                            self.addresses.parent = self
                            self._children_name_map["addresses"] = "addresses"
                        return self.addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "addresses" or name == "mtu" or name == "rpf" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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
                
                	**range:** 1000..3600000
                
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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("framed_prefix_pool",
                                    "managed_config",
                                    "ns_interval",
                                    "nud_enable",
                                    "other_config",
                                    "ra_lifetime",
                                    "ra_suppress",
                                    "ra_suppress_mtu",
                                    "ra_unicast",
                                    "ra_unspecify_hoplimit",
                                    "reachable_time",
                                    "router_preference",
                                    "start_ra_on_ipv6_enable",
                                    "suppress_cache_learning") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("maximum",
                                        "minimum") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.maximum.is_set or
                            self.minimum.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.maximum.yfilter != YFilter.not_set or
                            self.minimum.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-interval" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum.get_name_leafdata())
                        if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "maximum" or name == "minimum"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "maximum"):
                            self.maximum = value
                            self.maximum.value_namespace = name_space
                            self.maximum.value_namespace_prefix = name_space_prefix
                        if(value_path == "minimum"):
                            self.minimum = value
                            self.minimum.value_namespace = name_space
                            self.minimum.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "framed-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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

                        self.attempts = YLeaf(YType.uint32, "attempts")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("attempts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)

                    def has_data(self):
                        return self.attempts.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.attempts.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "duplicate-address-detection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.attempts.is_set or self.attempts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.attempts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attempts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "attempts"):
                            self.attempts = value
                            self.attempts.value_namespace = name_space
                            self.attempts.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.count.is_set or
                            self.interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-initial" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.count.get_name_leafdata())
                        if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count = value
                            self.count.value_namespace = name_space
                            self.count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interval"):
                            self.interval = value
                            self.interval.value_namespace = name_space
                            self.interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.framed_prefix_pool.is_set or
                        self.managed_config.is_set or
                        self.ns_interval.is_set or
                        self.nud_enable.is_set or
                        self.other_config.is_set or
                        self.ra_lifetime.is_set or
                        self.ra_suppress.is_set or
                        self.ra_suppress_mtu.is_set or
                        self.ra_unicast.is_set or
                        self.ra_unspecify_hoplimit.is_set or
                        self.reachable_time.is_set or
                        self.router_preference.is_set or
                        self.start_ra_on_ipv6_enable.is_set or
                        self.suppress_cache_learning.is_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_data()) or
                        (self.framed_prefix is not None) or
                        (self.ra_initial is not None) or
                        (self.ra_interval is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.framed_prefix_pool.yfilter != YFilter.not_set or
                        self.managed_config.yfilter != YFilter.not_set or
                        self.ns_interval.yfilter != YFilter.not_set or
                        self.nud_enable.yfilter != YFilter.not_set or
                        self.other_config.yfilter != YFilter.not_set or
                        self.ra_lifetime.yfilter != YFilter.not_set or
                        self.ra_suppress.yfilter != YFilter.not_set or
                        self.ra_suppress_mtu.yfilter != YFilter.not_set or
                        self.ra_unicast.yfilter != YFilter.not_set or
                        self.ra_unspecify_hoplimit.yfilter != YFilter.not_set or
                        self.reachable_time.yfilter != YFilter.not_set or
                        self.router_preference.yfilter != YFilter.not_set or
                        self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set or
                        self.suppress_cache_learning.yfilter != YFilter.not_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_operation()) or
                        (self.framed_prefix is not None and self.framed_prefix.has_operation()) or
                        (self.ra_initial is not None and self.ra_initial.has_operation()) or
                        (self.ra_interval is not None and self.ra_interval.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.framed_prefix_pool.is_set or self.framed_prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.framed_prefix_pool.get_name_leafdata())
                    if (self.managed_config.is_set or self.managed_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.managed_config.get_name_leafdata())
                    if (self.ns_interval.is_set or self.ns_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ns_interval.get_name_leafdata())
                    if (self.nud_enable.is_set or self.nud_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nud_enable.get_name_leafdata())
                    if (self.other_config.is_set or self.other_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.other_config.get_name_leafdata())
                    if (self.ra_lifetime.is_set or self.ra_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_lifetime.get_name_leafdata())
                    if (self.ra_suppress.is_set or self.ra_suppress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress.get_name_leafdata())
                    if (self.ra_suppress_mtu.is_set or self.ra_suppress_mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress_mtu.get_name_leafdata())
                    if (self.ra_unicast.is_set or self.ra_unicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unicast.get_name_leafdata())
                    if (self.ra_unspecify_hoplimit.is_set or self.ra_unspecify_hoplimit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unspecify_hoplimit.get_name_leafdata())
                    if (self.reachable_time.is_set or self.reachable_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reachable_time.get_name_leafdata())
                    if (self.router_preference.is_set or self.router_preference.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_preference.get_name_leafdata())
                    if (self.start_ra_on_ipv6_enable.is_set or self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_ra_on_ipv6_enable.get_name_leafdata())
                    if (self.suppress_cache_learning.is_set or self.suppress_cache_learning.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppress_cache_learning.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "duplicate-address-detection"):
                        if (self.duplicate_address_detection is None):
                            self.duplicate_address_detection = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection()
                            self.duplicate_address_detection.parent = self
                            self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                        return self.duplicate_address_detection

                    if (child_yang_name == "framed-prefix"):
                        if (self.framed_prefix is None):
                            self.framed_prefix = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix()
                            self.framed_prefix.parent = self
                            self._children_name_map["framed_prefix"] = "framed-prefix"
                        return self.framed_prefix

                    if (child_yang_name == "ra-initial"):
                        if (self.ra_initial is None):
                            self.ra_initial = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial()
                            self.ra_initial.parent = self
                            self._children_name_map["ra_initial"] = "ra-initial"
                        return self.ra_initial

                    if (child_yang_name == "ra-interval"):
                        if (self.ra_interval is None):
                            self.ra_interval = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval()
                            self.ra_interval.parent = self
                            self._children_name_map["ra_interval"] = "ra-interval"
                        return self.ra_interval

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "duplicate-address-detection" or name == "framed-prefix" or name == "ra-initial" or name == "ra-interval" or name == "framed-prefix-pool" or name == "managed-config" or name == "ns-interval" or name == "nud-enable" or name == "other-config" or name == "ra-lifetime" or name == "ra-suppress" or name == "ra-suppress-mtu" or name == "ra-unicast" or name == "ra-unspecify-hoplimit" or name == "reachable-time" or name == "router-preference" or name == "start-ra-on-ipv6-enable" or name == "suppress-cache-learning"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "framed-prefix-pool"):
                        self.framed_prefix_pool = value
                        self.framed_prefix_pool.value_namespace = name_space
                        self.framed_prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "managed-config"):
                        self.managed_config = value
                        self.managed_config.value_namespace = name_space
                        self.managed_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ns-interval"):
                        self.ns_interval = value
                        self.ns_interval.value_namespace = name_space
                        self.ns_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "nud-enable"):
                        self.nud_enable = value
                        self.nud_enable.value_namespace = name_space
                        self.nud_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "other-config"):
                        self.other_config = value
                        self.other_config.value_namespace = name_space
                        self.other_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-lifetime"):
                        self.ra_lifetime = value
                        self.ra_lifetime.value_namespace = name_space
                        self.ra_lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress"):
                        self.ra_suppress = value
                        self.ra_suppress.value_namespace = name_space
                        self.ra_suppress.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress-mtu"):
                        self.ra_suppress_mtu = value
                        self.ra_suppress_mtu.value_namespace = name_space
                        self.ra_suppress_mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unicast"):
                        self.ra_unicast = value
                        self.ra_unicast.value_namespace = name_space
                        self.ra_unicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unspecify-hoplimit"):
                        self.ra_unspecify_hoplimit = value
                        self.ra_unspecify_hoplimit.value_namespace = name_space
                        self.ra_unspecify_hoplimit.value_namespace_prefix = name_space_prefix
                    if(value_path == "reachable-time"):
                        self.reachable_time = value
                        self.reachable_time.value_namespace = name_space
                        self.reachable_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-preference"):
                        self.router_preference = value
                        self.router_preference.value_namespace = name_space
                        self.router_preference.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-ra-on-ipv6-enable"):
                        self.start_ra_on_ipv6_enable = value
                        self.start_ra_on_ipv6_enable.value_namespace = name_space
                        self.start_ra_on_ipv6_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppress-cache-learning"):
                        self.suppress_cache_learning = value
                        self.suppress_cache_learning.value_namespace = name_space
                        self.suppress_cache_learning.value_namespace_prefix = name_space_prefix


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

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.class_ = YLeaf(YType.str, "class")

                    self.delegated_prefix_pool = YLeaf(YType.str, "delegated-prefix-pool")

                    self.dns_ipv6address = YLeaf(YType.str, "dns-ipv6address")

                    self.mode_class = YLeaf(YType.str, "mode-class")

                    self.stateful_address = YLeaf(YType.str, "stateful-address")

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._children_yang_names.add("delegated-prefix")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address_pool",
                                    "class_",
                                    "delegated_prefix_pool",
                                    "dns_ipv6address",
                                    "mode_class",
                                    "stateful_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Dhcpv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Dhcpv6, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "delegated-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.address_pool.is_set or
                        self.class_.is_set or
                        self.delegated_prefix_pool.is_set or
                        self.dns_ipv6address.is_set or
                        self.mode_class.is_set or
                        self.stateful_address.is_set or
                        (self.delegated_prefix is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address_pool.yfilter != YFilter.not_set or
                        self.class_.yfilter != YFilter.not_set or
                        self.delegated_prefix_pool.yfilter != YFilter.not_set or
                        self.dns_ipv6address.yfilter != YFilter.not_set or
                        self.mode_class.yfilter != YFilter.not_set or
                        self.stateful_address.yfilter != YFilter.not_set or
                        (self.delegated_prefix is not None and self.delegated_prefix.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address_pool.is_set or self.address_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_pool.get_name_leafdata())
                    if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.class_.get_name_leafdata())
                    if (self.delegated_prefix_pool.is_set or self.delegated_prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delegated_prefix_pool.get_name_leafdata())
                    if (self.dns_ipv6address.is_set or self.dns_ipv6address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dns_ipv6address.get_name_leafdata())
                    if (self.mode_class.is_set or self.mode_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode_class.get_name_leafdata())
                    if (self.stateful_address.is_set or self.stateful_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.stateful_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "delegated-prefix"):
                        if (self.delegated_prefix is None):
                            self.delegated_prefix = DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix()
                            self.delegated_prefix.parent = self
                            self._children_name_map["delegated_prefix"] = "delegated-prefix"
                        return self.delegated_prefix

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "delegated-prefix" or name == "address-pool" or name == "class" or name == "delegated-prefix-pool" or name == "dns-ipv6address" or name == "mode-class" or name == "stateful-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address-pool"):
                        self.address_pool = value
                        self.address_pool.value_namespace = name_space
                        self.address_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "class"):
                        self.class_ = value
                        self.class_.value_namespace = name_space
                        self.class_.value_namespace_prefix = name_space_prefix
                    if(value_path == "delegated-prefix-pool"):
                        self.delegated_prefix_pool = value
                        self.delegated_prefix_pool.value_namespace = name_space
                        self.delegated_prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "dns-ipv6address"):
                        self.dns_ipv6address = value
                        self.dns_ipv6address.value_namespace = name_space
                        self.dns_ipv6address.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode-class"):
                        self.mode_class = value
                        self.mode_class.value_namespace = name_space
                        self.mode_class.value_namespace_prefix = name_space_prefix
                    if(value_path == "stateful-address"):
                        self.stateful_address = value
                        self.stateful_address.value_namespace = name_space
                        self.stateful_address.value_namespace_prefix = name_space_prefix


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

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("service_policy_in") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Pbr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Pbr, self).__setattr__(name, value)


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

                        self.input = YLeaf(YType.str, "input")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("input") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy, self).__setattr__(name, value)

                    def has_data(self):
                        return self.input.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.input.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.input.is_set or self.input.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "input"):
                            self.input = value
                            self.input.value_namespace = name_space
                            self.input.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.service_policy_in.is_set or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.service_policy_in.yfilter != YFilter.not_set or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.service_policy_in.is_set or self.service_policy_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service_policy_in.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service-policy" or name == "service-policy-in"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "service-policy-in"):
                        self.service_policy_in = value
                        self.service_policy_in.value_namespace = name_space
                        self.service_policy_in.value_namespace_prefix = name_space_prefix


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

                        self.max_consecutive_conf_naks = YLeaf(YType.uint32, "max-consecutive-conf-naks")

                        self.max_unacknowledged_conf_requests = YLeaf(YType.uint32, "max-unacknowledged-conf-requests")

                        self.protocol_reject_timeout = YLeaf(YType.uint32, "protocol-reject-timeout")

                        self.retry_timeout = YLeaf(YType.uint32, "retry-timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("max_consecutive_conf_naks",
                                        "max_unacknowledged_conf_requests",
                                        "protocol_reject_timeout",
                                        "retry_timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.max_consecutive_conf_naks.is_set or
                            self.max_unacknowledged_conf_requests.is_set or
                            self.protocol_reject_timeout.is_set or
                            self.retry_timeout.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.max_consecutive_conf_naks.yfilter != YFilter.not_set or
                            self.max_unacknowledged_conf_requests.yfilter != YFilter.not_set or
                            self.protocol_reject_timeout.yfilter != YFilter.not_set or
                            self.retry_timeout.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fsm" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.max_consecutive_conf_naks.is_set or self.max_consecutive_conf_naks.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_consecutive_conf_naks.get_name_leafdata())
                        if (self.max_unacknowledged_conf_requests.is_set or self.max_unacknowledged_conf_requests.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_unacknowledged_conf_requests.get_name_leafdata())
                        if (self.protocol_reject_timeout.is_set or self.protocol_reject_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_reject_timeout.get_name_leafdata())
                        if (self.retry_timeout.is_set or self.retry_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.retry_timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "max-consecutive-conf-naks" or name == "max-unacknowledged-conf-requests" or name == "protocol-reject-timeout" or name == "retry-timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "max-consecutive-conf-naks"):
                            self.max_consecutive_conf_naks = value
                            self.max_consecutive_conf_naks.value_namespace = name_space
                            self.max_consecutive_conf_naks.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-unacknowledged-conf-requests"):
                            self.max_unacknowledged_conf_requests = value
                            self.max_unacknowledged_conf_requests.value_namespace = name_space
                            self.max_unacknowledged_conf_requests.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-reject-timeout"):
                            self.protocol_reject_timeout = value
                            self.protocol_reject_timeout.value_namespace = name_space
                            self.protocol_reject_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "retry-timeout"):
                            self.retry_timeout = value
                            self.retry_timeout.value_namespace = name_space
                            self.retry_timeout.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mru_ignore",
                                        "renegotiation",
                                        "send_term_request_on_shut_down",
                                        "service_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp, self).__setattr__(name, value)


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

                            self.minutes = YLeaf(YType.uint32, "minutes")

                            self.seconds = YLeaf(YType.uint32, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("minutes",
                                            "seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.minutes.is_set or
                                self.seconds.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.minutes.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "absolute-timeout" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minutes.get_name_leafdata())
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "minutes" or name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "minutes"):
                                self.minutes = value
                                self.minutes.value_namespace = name_space
                                self.minutes.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix


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

                            self.milliseconds = YLeaf(YType.uint32, "milliseconds")

                            self.seconds = YLeaf(YType.uint32, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("milliseconds",
                                            "seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.milliseconds.is_set or
                                self.seconds.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.milliseconds.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "delay" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.milliseconds.is_set or self.milliseconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.milliseconds.get_name_leafdata())
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "milliseconds" or name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "milliseconds"):
                                self.milliseconds = value
                                self.milliseconds.value_namespace = name_space
                                self.milliseconds.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix


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

                            self.chap_host_name = YLeaf(YType.str, "chap-host-name")

                            self.max_authentication_failures = YLeaf(YType.uint32, "max-authentication-failures")

                            self.mschap_host_name = YLeaf(YType.str, "mschap-host-name")

                            self.pap = YLeaf(YType.int32, "pap")

                            self.timeout = YLeaf(YType.uint32, "timeout")

                            self.methods = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods()
                            self.methods.parent = self
                            self._children_name_map["methods"] = "methods"
                            self._children_yang_names.add("methods")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("chap_host_name",
                                            "max_authentication_failures",
                                            "mschap_host_name",
                                            "pap",
                                            "timeout") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication, self).__setattr__(name, value)


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

                                self.method = YLeafList(YType.enumeration, "method")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("method") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.method.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.method.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.method.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "methods" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.method.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "method"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "method"):
                                    self.method.append(value)

                        def has_data(self):
                            return (
                                self.chap_host_name.is_set or
                                self.max_authentication_failures.is_set or
                                self.mschap_host_name.is_set or
                                self.pap.is_set or
                                self.timeout.is_set or
                                (self.methods is not None and self.methods.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.chap_host_name.yfilter != YFilter.not_set or
                                self.max_authentication_failures.yfilter != YFilter.not_set or
                                self.mschap_host_name.yfilter != YFilter.not_set or
                                self.pap.yfilter != YFilter.not_set or
                                self.timeout.yfilter != YFilter.not_set or
                                (self.methods is not None and self.methods.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "authentication" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.chap_host_name.is_set or self.chap_host_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.chap_host_name.get_name_leafdata())
                            if (self.max_authentication_failures.is_set or self.max_authentication_failures.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_authentication_failures.get_name_leafdata())
                            if (self.mschap_host_name.is_set or self.mschap_host_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mschap_host_name.get_name_leafdata())
                            if (self.pap.is_set or self.pap.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pap.get_name_leafdata())
                            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timeout.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "methods"):
                                if (self.methods is None):
                                    self.methods = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods()
                                    self.methods.parent = self
                                    self._children_name_map["methods"] = "methods"
                                return self.methods

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "methods" or name == "chap-host-name" or name == "max-authentication-failures" or name == "mschap-host-name" or name == "pap" or name == "timeout"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "chap-host-name"):
                                self.chap_host_name = value
                                self.chap_host_name.value_namespace = name_space
                                self.chap_host_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-authentication-failures"):
                                self.max_authentication_failures = value
                                self.max_authentication_failures.value_namespace = name_space
                                self.max_authentication_failures.value_namespace_prefix = name_space_prefix
                            if(value_path == "mschap-host-name"):
                                self.mschap_host_name = value
                                self.mschap_host_name.value_namespace = name_space
                                self.mschap_host_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "pap"):
                                self.pap = value
                                self.pap.value_namespace = name_space
                                self.pap.value_namespace_prefix = name_space_prefix
                            if(value_path == "timeout"):
                                self.timeout = value
                                self.timeout.value_namespace = name_space
                                self.timeout.value_namespace_prefix = name_space_prefix


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

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.keepalive_disable = YLeaf(YType.boolean, "keepalive-disable")

                            self.retry_count = YLeaf(YType.uint32, "retry-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interval",
                                            "keepalive_disable",
                                            "retry_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interval.is_set or
                                self.keepalive_disable.is_set or
                                self.retry_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interval.yfilter != YFilter.not_set or
                                self.keepalive_disable.yfilter != YFilter.not_set or
                                self.retry_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "keepalive" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interval.get_name_leafdata())
                            if (self.keepalive_disable.is_set or self.keepalive_disable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.keepalive_disable.get_name_leafdata())
                            if (self.retry_count.is_set or self.retry_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.retry_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interval" or name == "keepalive-disable" or name == "retry-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interval"):
                                self.interval = value
                                self.interval.value_namespace = name_space
                                self.interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "keepalive-disable"):
                                self.keepalive_disable = value
                                self.keepalive_disable.value_namespace = name_space
                                self.keepalive_disable.value_namespace_prefix = name_space_prefix
                            if(value_path == "retry-count"):
                                self.retry_count = value
                                self.retry_count.value_namespace = name_space
                                self.retry_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mru_ignore.is_set or
                            self.renegotiation.is_set or
                            self.send_term_request_on_shut_down.is_set or
                            self.service_type.is_set or
                            (self.absolute_timeout is not None and self.absolute_timeout.has_data()) or
                            (self.authentication is not None and self.authentication.has_data()) or
                            (self.delay is not None and self.delay.has_data()) or
                            (self.keepalive is not None and self.keepalive.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mru_ignore.yfilter != YFilter.not_set or
                            self.renegotiation.yfilter != YFilter.not_set or
                            self.send_term_request_on_shut_down.yfilter != YFilter.not_set or
                            self.service_type.yfilter != YFilter.not_set or
                            (self.absolute_timeout is not None and self.absolute_timeout.has_operation()) or
                            (self.authentication is not None and self.authentication.has_operation()) or
                            (self.delay is not None and self.delay.has_operation()) or
                            (self.keepalive is not None and self.keepalive.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lcp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mru_ignore.is_set or self.mru_ignore.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mru_ignore.get_name_leafdata())
                        if (self.renegotiation.is_set or self.renegotiation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.renegotiation.get_name_leafdata())
                        if (self.send_term_request_on_shut_down.is_set or self.send_term_request_on_shut_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_term_request_on_shut_down.get_name_leafdata())
                        if (self.service_type.is_set or self.service_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "absolute-timeout"):
                            if (self.absolute_timeout is None):
                                self.absolute_timeout = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout()
                                self.absolute_timeout.parent = self
                                self._children_name_map["absolute_timeout"] = "absolute-timeout"
                            return self.absolute_timeout

                        if (child_yang_name == "authentication"):
                            if (self.authentication is None):
                                self.authentication = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication()
                                self.authentication.parent = self
                                self._children_name_map["authentication"] = "authentication"
                            return self.authentication

                        if (child_yang_name == "delay"):
                            if (self.delay is None):
                                self.delay = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay()
                                self.delay.parent = self
                                self._children_name_map["delay"] = "delay"
                            return self.delay

                        if (child_yang_name == "keepalive"):
                            if (self.keepalive is None):
                                self.keepalive = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive()
                                self.keepalive.parent = self
                                self._children_name_map["keepalive"] = "keepalive"
                            return self.keepalive

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "absolute-timeout" or name == "authentication" or name == "delay" or name == "keepalive" or name == "mru-ignore" or name == "renegotiation" or name == "send-term-request-on-shut-down" or name == "service-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mru-ignore"):
                            self.mru_ignore = value
                            self.mru_ignore.value_namespace = name_space
                            self.mru_ignore.value_namespace_prefix = name_space_prefix
                        if(value_path == "renegotiation"):
                            self.renegotiation = value
                            self.renegotiation.value_namespace = name_space
                            self.renegotiation.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-term-request-on-shut-down"):
                            self.send_term_request_on_shut_down = value
                            self.send_term_request_on_shut_down.value_namespace = name_space
                            self.send_term_request_on_shut_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-type"):
                            self.service_type = value
                            self.service_type.value_namespace = name_space
                            self.service_type.value_namespace_prefix = name_space_prefix


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

                        self.passive = YLeaf(YType.empty, "passive")

                        self.peer_interface_id = YLeaf(YType.str, "peer-interface-id")

                        self.protocol_reject = YLeaf(YType.empty, "protocol-reject")

                        self.renegotiation = YLeaf(YType.empty, "renegotiation")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("passive",
                                        "peer_interface_id",
                                        "protocol_reject",
                                        "renegotiation") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.passive.is_set or
                            self.peer_interface_id.is_set or
                            self.protocol_reject.is_set or
                            self.renegotiation.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.passive.yfilter != YFilter.not_set or
                            self.peer_interface_id.yfilter != YFilter.not_set or
                            self.protocol_reject.yfilter != YFilter.not_set or
                            self.renegotiation.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6cp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.passive.is_set or self.passive.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.passive.get_name_leafdata())
                        if (self.peer_interface_id.is_set or self.peer_interface_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_interface_id.get_name_leafdata())
                        if (self.protocol_reject.is_set or self.protocol_reject.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_reject.get_name_leafdata())
                        if (self.renegotiation.is_set or self.renegotiation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.renegotiation.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "passive" or name == "peer-interface-id" or name == "protocol-reject" or name == "renegotiation"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "passive"):
                            self.passive = value
                            self.passive.value_namespace = name_space
                            self.passive.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-interface-id"):
                            self.peer_interface_id = value
                            self.peer_interface_id.value_namespace = name_space
                            self.peer_interface_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-reject"):
                            self.protocol_reject = value
                            self.protocol_reject.value_namespace = name_space
                            self.protocol_reject.value_namespace_prefix = name_space_prefix
                        if(value_path == "renegotiation"):
                            self.renegotiation = value
                            self.renegotiation.value_namespace = name_space
                            self.renegotiation.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("passive",
                                        "peer_netmask",
                                        "protocol_reject",
                                        "renegotiation") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp, self).__setattr__(name, value)


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

                            self.wins_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses()
                            self.wins_addresses.parent = self
                            self._children_name_map["wins_addresses"] = "wins-addresses"
                            self._children_yang_names.add("wins-addresses")


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

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("primary",
                                                "secondary") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.primary.is_set or
                                    self.secondary.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.primary.yfilter != YFilter.not_set or
                                    self.secondary.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "wins-addresses" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.primary.is_set or self.primary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.primary.get_name_leafdata())
                                if (self.secondary.is_set or self.secondary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.secondary.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "primary" or name == "secondary"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "primary"):
                                    self.primary = value
                                    self.primary.value_namespace = name_space
                                    self.primary.value_namespace_prefix = name_space_prefix
                                if(value_path == "secondary"):
                                    self.secondary = value
                                    self.secondary.value_namespace = name_space
                                    self.secondary.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.wins_addresses is not None and self.wins_addresses.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.wins_addresses is not None and self.wins_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "wins" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "wins-addresses"):
                                if (self.wins_addresses is None):
                                    self.wins_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses()
                                    self.wins_addresses.parent = self
                                    self._children_name_map["wins_addresses"] = "wins-addresses"
                                return self.wins_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "wins-addresses"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.dns_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses()
                            self.dns_addresses.parent = self
                            self._children_name_map["dns_addresses"] = "dns-addresses"
                            self._children_yang_names.add("dns-addresses")


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

                                self.primary = YLeaf(YType.str, "primary")

                                self.secondary = YLeaf(YType.str, "secondary")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("primary",
                                                "secondary") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.primary.is_set or
                                    self.secondary.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.primary.yfilter != YFilter.not_set or
                                    self.secondary.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dns-addresses" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.primary.is_set or self.primary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.primary.get_name_leafdata())
                                if (self.secondary.is_set or self.secondary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.secondary.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "primary" or name == "secondary"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "primary"):
                                    self.primary = value
                                    self.primary.value_namespace = name_space
                                    self.primary.value_namespace_prefix = name_space_prefix
                                if(value_path == "secondary"):
                                    self.secondary = value
                                    self.secondary.value_namespace = name_space
                                    self.secondary.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.dns_addresses is not None and self.dns_addresses.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dns_addresses is not None and self.dns_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dns" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dns-addresses"):
                                if (self.dns_addresses is None):
                                    self.dns_addresses = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses()
                                    self.dns_addresses.parent = self
                                    self._children_name_map["dns_addresses"] = "dns-addresses"
                                return self.dns_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dns-addresses"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.default = YLeaf(YType.str, "default")

                            self.pool = YLeaf(YType.str, "pool")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("default",
                                            "pool") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.default.is_set or
                                self.pool.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.default.yfilter != YFilter.not_set or
                                self.pool.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.default.get_name_leafdata())
                            if (self.pool.is_set or self.pool.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "default" or name == "pool"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "default"):
                                self.default = value
                                self.default.value_namespace = name_space
                                self.default.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool"):
                                self.pool = value
                                self.pool.value_namespace = name_space
                                self.pool.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.passive.is_set or
                            self.peer_netmask.is_set or
                            self.protocol_reject.is_set or
                            self.renegotiation.is_set or
                            (self.dns is not None and self.dns.has_data()) or
                            (self.peer_address is not None and self.peer_address.has_data()) or
                            (self.wins is not None and self.wins.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.passive.yfilter != YFilter.not_set or
                            self.peer_netmask.yfilter != YFilter.not_set or
                            self.protocol_reject.yfilter != YFilter.not_set or
                            self.renegotiation.yfilter != YFilter.not_set or
                            (self.dns is not None and self.dns.has_operation()) or
                            (self.peer_address is not None and self.peer_address.has_operation()) or
                            (self.wins is not None and self.wins.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipcp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.passive.is_set or self.passive.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.passive.get_name_leafdata())
                        if (self.peer_netmask.is_set or self.peer_netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_netmask.get_name_leafdata())
                        if (self.protocol_reject.is_set or self.protocol_reject.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_reject.get_name_leafdata())
                        if (self.renegotiation.is_set or self.renegotiation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.renegotiation.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dns"):
                            if (self.dns is None):
                                self.dns = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns()
                                self.dns.parent = self
                                self._children_name_map["dns"] = "dns"
                            return self.dns

                        if (child_yang_name == "peer-address"):
                            if (self.peer_address is None):
                                self.peer_address = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress()
                                self.peer_address.parent = self
                                self._children_name_map["peer_address"] = "peer-address"
                            return self.peer_address

                        if (child_yang_name == "wins"):
                            if (self.wins is None):
                                self.wins = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins()
                                self.wins.parent = self
                                self._children_name_map["wins"] = "wins"
                            return self.wins

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dns" or name == "peer-address" or name == "wins" or name == "passive" or name == "peer-netmask" or name == "protocol-reject" or name == "renegotiation"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "passive"):
                            self.passive = value
                            self.passive.value_namespace = name_space
                            self.passive.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-netmask"):
                            self.peer_netmask = value
                            self.peer_netmask.value_namespace = name_space
                            self.peer_netmask.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-reject"):
                            self.protocol_reject = value
                            self.protocol_reject.value_namespace = name_space
                            self.protocol_reject.value_namespace_prefix = name_space_prefix
                        if(value_path == "renegotiation"):
                            self.renegotiation = value
                            self.renegotiation.value_namespace = name_space
                            self.renegotiation.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.fsm is not None and self.fsm.has_data()) or
                        (self.ipcp is not None and self.ipcp.has_data()) or
                        (self.ipv6cp is not None and self.ipv6cp.has_data()) or
                        (self.lcp is not None and self.lcp.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.fsm is not None and self.fsm.has_operation()) or
                        (self.ipcp is not None and self.ipcp.has_operation()) or
                        (self.ipv6cp is not None and self.ipv6cp.has_operation()) or
                        (self.lcp is not None and self.lcp.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ppp-ma-gbl-cfg:ppp-template" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fsm"):
                        if (self.fsm is None):
                            self.fsm = DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm()
                            self.fsm.parent = self
                            self._children_name_map["fsm"] = "fsm"
                        return self.fsm

                    if (child_yang_name == "ipcp"):
                        if (self.ipcp is None):
                            self.ipcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp()
                            self.ipcp.parent = self
                            self._children_name_map["ipcp"] = "ipcp"
                        return self.ipcp

                    if (child_yang_name == "ipv6cp"):
                        if (self.ipv6cp is None):
                            self.ipv6cp = DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6Cp()
                            self.ipv6cp.parent = self
                            self._children_name_map["ipv6cp"] = "ipv6cp"
                        return self.ipv6cp

                    if (child_yang_name == "lcp"):
                        if (self.lcp is None):
                            self.lcp = DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp()
                            self.lcp.parent = self
                            self._children_name_map["lcp"] = "lcp"
                        return self.lcp

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fsm" or name == "ipcp" or name == "ipv6cp" or name == "lcp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "input" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "output" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.input is not None) or
                            (self.output is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.input is not None and self.input.has_operation()) or
                            (self.output is not None and self.output.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "input"):
                            if (self.input is None):
                                self.input = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                            return self.input

                        if (child_yang_name == "output"):
                            if (self.output is None):
                                self.output = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                            return self.output

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input" or name == "output"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aal",
                                        "atm_cell_tax",
                                        "encapsulation",
                                        "user_defined") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Qos.Account, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Qos.Account, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.aal.is_set or
                            self.atm_cell_tax.is_set or
                            self.encapsulation.is_set or
                            self.user_defined.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aal.yfilter != YFilter.not_set or
                            self.atm_cell_tax.yfilter != YFilter.not_set or
                            self.encapsulation.yfilter != YFilter.not_set or
                            self.user_defined.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "account" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aal.is_set or self.aal.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aal.get_name_leafdata())
                        if (self.atm_cell_tax.is_set or self.atm_cell_tax.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.atm_cell_tax.get_name_leafdata())
                        if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation.get_name_leafdata())
                        if (self.user_defined.is_set or self.user_defined.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_defined.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aal" or name == "atm-cell-tax" or name == "encapsulation" or name == "user-defined"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aal"):
                            self.aal = value
                            self.aal.value_namespace = name_space
                            self.aal.value_namespace_prefix = name_space_prefix
                        if(value_path == "atm-cell-tax"):
                            self.atm_cell_tax = value
                            self.atm_cell_tax.value_namespace = name_space
                            self.atm_cell_tax.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation"):
                            self.encapsulation = value
                            self.encapsulation.value_namespace = name_space
                            self.encapsulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-defined"):
                            self.user_defined = value
                            self.user_defined.value_namespace = name_space
                            self.user_defined.value_namespace_prefix = name_space_prefix


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

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("minimum_bandwidth") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Qos.Output, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Qos.Output, self).__setattr__(name, value)

                    def has_data(self):
                        return self.minimum_bandwidth.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.minimum_bandwidth.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "output" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.minimum_bandwidth.is_set or self.minimum_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum_bandwidth.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "minimum-bandwidth"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "minimum-bandwidth"):
                            self.minimum_bandwidth = value
                            self.minimum_bandwidth.value_namespace = name_space
                            self.minimum_bandwidth.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.account is not None and self.account.has_data()) or
                        (self.output is not None and self.output.has_data()) or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.account is not None and self.account.has_operation()) or
                        (self.output is not None and self.output.has_operation()) or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-qos-ma-bng-cfg:qos" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "account"):
                        if (self.account is None):
                            self.account = DynamicTemplate.Ppps.Ppp.Qos.Account()
                            self.account.parent = self
                            self._children_name_map["account"] = "account"
                        return self.account

                    if (child_yang_name == "output"):
                        if (self.output is None):
                            self.output = DynamicTemplate.Ppps.Ppp.Qos.Output()
                            self.output.parent = self
                            self._children_name_map["output"] = "output"
                        return self.output

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "account" or name == "output" or name == "service-policy"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prepaid_feature") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.Accounting, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.Accounting, self).__setattr__(name, value)


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.int32, "threshold")

                        self.timeout_value = YLeaf(YType.int32, "timeout-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction",
                                        "threshold",
                                        "timeout_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.direction.is_set or
                            self.threshold.is_set or
                            self.timeout_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set or
                            self.timeout_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "idle-timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())
                        if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction" or name == "threshold" or name == "timeout-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-value"):
                            self.timeout_value = value
                            self.timeout_value.value_namespace = name_space
                            self.timeout_value.value_namespace_prefix = name_space_prefix


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

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dual_stack_delay",
                                        "hold_acct_start",
                                        "method_list_name",
                                        "periodic_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Accounting.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Accounting.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dual_stack_delay.is_set or
                            self.hold_acct_start.is_set or
                            self.method_list_name.is_set or
                            self.periodic_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dual_stack_delay.yfilter != YFilter.not_set or
                            self.hold_acct_start.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set or
                            self.periodic_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dual_stack_delay.is_set or self.dual_stack_delay.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dual_stack_delay.get_name_leafdata())
                        if (self.hold_acct_start.is_set or self.hold_acct_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_acct_start.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())
                        if (self.periodic_interval.is_set or self.periodic_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.periodic_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dual-stack-delay" or name == "hold-acct-start" or name == "method-list-name" or name == "periodic-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dual-stack-delay"):
                            self.dual_stack_delay = value
                            self.dual_stack_delay.value_namespace = name_space
                            self.dual_stack_delay.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-acct-start"):
                            self.hold_acct_start = value
                            self.hold_acct_start.value_namespace = name_space
                            self.hold_acct_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "periodic-interval"):
                            self.periodic_interval = value
                            self.periodic_interval.value_namespace = name_space
                            self.periodic_interval.value_namespace_prefix = name_space_prefix


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

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accounting_interim_interval",
                                        "method_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accounting_interim_interval.is_set or
                            self.method_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accounting_interim_interval.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-accounting" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accounting_interim_interval.is_set or self.accounting_interim_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_interim_interval.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-interim-interval" or name == "method-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accounting-interim-interval"):
                            self.accounting_interim_interval = value
                            self.accounting_interim_interval.value_namespace = name_space
                            self.accounting_interim_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.prepaid_feature.is_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_data()) or
                        (self.service_accounting is not None and self.service_accounting.has_data()) or
                        (self.session is not None and self.session.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prepaid_feature.yfilter != YFilter.not_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_operation()) or
                        (self.service_accounting is not None and self.service_accounting.has_operation()) or
                        (self.session is not None and self.session.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prepaid_feature.is_set or self.prepaid_feature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prepaid_feature.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "idle-timeout"):
                        if (self.idle_timeout is None):
                            self.idle_timeout = DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout()
                            self.idle_timeout.parent = self
                            self._children_name_map["idle_timeout"] = "idle-timeout"
                        return self.idle_timeout

                    if (child_yang_name == "service-accounting"):
                        if (self.service_accounting is None):
                            self.service_accounting = DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting()
                            self.service_accounting.parent = self
                            self._children_name_map["service_accounting"] = "service-accounting"
                        return self.service_accounting

                    if (child_yang_name == "session"):
                        if (self.session is None):
                            self.session = DynamicTemplate.Ppps.Ppp.Accounting.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                        return self.session

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "idle-timeout" or name == "service-accounting" or name == "session" or name == "prepaid-feature"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prepaid-feature"):
                        self.prepaid_feature = value
                        self.prepaid_feature.value_namespace = name_space
                        self.prepaid_feature.value_namespace_prefix = name_space_prefix


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

                    self.port_limit = YLeaf(YType.uint16, "port-limit")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("port_limit") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.Ppps.Ppp.PppoeTemplate, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.Ppps.Ppp.PppoeTemplate, self).__setattr__(name, value)

                def has_data(self):
                    return self.port_limit.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.port_limit.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-template" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.port_limit.is_set or self.port_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_limit.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port-limit"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "port-limit"):
                        self.port_limit = value
                        self.port_limit.value_namespace = name_space
                        self.port_limit.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.template_name.is_set or
                    self.vrf.is_set or
                    (self.accounting is not None and self.accounting.has_data()) or
                    (self.dhcpv6 is not None and self.dhcpv6.has_data()) or
                    (self.igmp is not None and self.igmp.has_data()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_data()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_data()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_data()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_data()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_data()) or
                    (self.pbr is not None and self.pbr.has_data()) or
                    (self.ppp_template is not None and self.ppp_template.has_data()) or
                    (self.pppoe_template is not None and self.pppoe_template.has_data()) or
                    (self.qos is not None and self.qos.has_data()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.template_name.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.accounting is not None and self.accounting.has_operation()) or
                    (self.dhcpv6 is not None and self.dhcpv6.has_operation()) or
                    (self.igmp is not None and self.igmp.has_operation()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_operation()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_operation()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_operation()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_operation()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_operation()) or
                    (self.pbr is not None and self.pbr.has_operation()) or
                    (self.ppp_template is not None and self.ppp_template.has_operation()) or
                    (self.pppoe_template is not None and self.pppoe_template.has_operation()) or
                    (self.qos is not None and self.qos.has_operation()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ppp" + "[template-name='" + self.template_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ppps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.template_name.is_set or self.template_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.template_name.get_name_leafdata())
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "accounting"):
                    if (self.accounting is None):
                        self.accounting = DynamicTemplate.Ppps.Ppp.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                    return self.accounting

                if (child_yang_name == "dhcpv6"):
                    if (self.dhcpv6 is None):
                        self.dhcpv6 = DynamicTemplate.Ppps.Ppp.Dhcpv6()
                        self.dhcpv6.parent = self
                        self._children_name_map["dhcpv6"] = "dhcpv6"
                    return self.dhcpv6

                if (child_yang_name == "igmp"):
                    if (self.igmp is None):
                        self.igmp = DynamicTemplate.Ppps.Ppp.Igmp()
                        self.igmp.parent = self
                        self._children_name_map["igmp"] = "igmp"
                    return self.igmp

                if (child_yang_name == "ipv4-network"):
                    if (self.ipv4_network is None):
                        self.ipv4_network = DynamicTemplate.Ppps.Ppp.Ipv4Network()
                        self.ipv4_network.parent = self
                        self._children_name_map["ipv4_network"] = "ipv4-network"
                    return self.ipv4_network

                if (child_yang_name == "ipv4-packet-filter"):
                    if (self.ipv4_packet_filter is None):
                        self.ipv4_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter()
                        self.ipv4_packet_filter.parent = self
                        self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                    return self.ipv4_packet_filter

                if (child_yang_name == "ipv6-neighbor"):
                    if (self.ipv6_neighbor is None):
                        self.ipv6_neighbor = DynamicTemplate.Ppps.Ppp.Ipv6Neighbor()
                        self.ipv6_neighbor.parent = self
                        self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                    return self.ipv6_neighbor

                if (child_yang_name == "ipv6-network"):
                    if (self.ipv6_network is None):
                        self.ipv6_network = DynamicTemplate.Ppps.Ppp.Ipv6Network()
                        self.ipv6_network.parent = self
                        self._children_name_map["ipv6_network"] = "ipv6-network"
                    return self.ipv6_network

                if (child_yang_name == "ipv6-packet-filter"):
                    if (self.ipv6_packet_filter is None):
                        self.ipv6_packet_filter = DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter()
                        self.ipv6_packet_filter.parent = self
                        self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                    return self.ipv6_packet_filter

                if (child_yang_name == "pbr"):
                    if (self.pbr is None):
                        self.pbr = DynamicTemplate.Ppps.Ppp.Pbr()
                        self.pbr.parent = self
                        self._children_name_map["pbr"] = "pbr"
                    return self.pbr

                if (child_yang_name == "ppp-template"):
                    if (self.ppp_template is None):
                        self.ppp_template = DynamicTemplate.Ppps.Ppp.PppTemplate()
                        self.ppp_template.parent = self
                        self._children_name_map["ppp_template"] = "ppp-template"
                    return self.ppp_template

                if (child_yang_name == "pppoe-template"):
                    if (self.pppoe_template is None):
                        self.pppoe_template = DynamicTemplate.Ppps.Ppp.PppoeTemplate()
                        self.pppoe_template.parent = self
                        self._children_name_map["pppoe_template"] = "pppoe-template"
                    return self.pppoe_template

                if (child_yang_name == "qos"):
                    if (self.qos is None):
                        self.qos = DynamicTemplate.Ppps.Ppp.Qos()
                        self.qos.parent = self
                        self._children_name_map["qos"] = "qos"
                    return self.qos

                if (child_yang_name == "span-monitor-sessions"):
                    if (self.span_monitor_sessions is None):
                        self.span_monitor_sessions = DynamicTemplate.Ppps.Ppp.SpanMonitorSessions()
                        self.span_monitor_sessions.parent = self
                        self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                    return self.span_monitor_sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting" or name == "dhcpv6" or name == "igmp" or name == "ipv4-network" or name == "ipv4-packet-filter" or name == "ipv6-neighbor" or name == "ipv6-network" or name == "ipv6-packet-filter" or name == "pbr" or name == "ppp-template" or name == "pppoe-template" or name == "qos" or name == "span-monitor-sessions" or name == "template-name" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "template-name"):
                    self.template_name = value
                    self.template_name.value_namespace = name_space
                    self.template_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ppp:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ppp:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ppps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ppp"):
                for c in self.ppp:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DynamicTemplate.Ppps.Ppp()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ppp.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ppp"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.ip_subscriber = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DynamicTemplate.IpSubscribers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DynamicTemplate.IpSubscribers, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("template_name",
                                "vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DynamicTemplate.IpSubscribers.IpSubscriber, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DynamicTemplate.IpSubscribers.IpSubscriber, self).__setattr__(name, value)


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

                    self.span_monitor_session = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions, self).__setattr__(name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.acl = YLeaf(YType.empty, "acl")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_class",
                                        "acl",
                                        "mirror_first",
                                        "mirror_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "port_level_enable",
                                            "session_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.port_level_enable.is_set or
                                self.session_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.port_level_enable.yfilter != YFilter.not_set or
                                self.session_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "attachment" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.port_level_enable.is_set or self.port_level_enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_level_enable.get_name_leafdata())
                            if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "port-level-enable" or name == "session-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-level-enable"):
                                self.port_level_enable = value
                                self.port_level_enable.value_namespace = name_space
                                self.port_level_enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-name"):
                                self.session_name = value
                                self.session_name.value_namespace = name_space
                                self.session_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.session_class.is_set or
                            self.acl.is_set or
                            self.mirror_first.is_set or
                            self.mirror_interval.is_set or
                            (self.attachment is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_class.yfilter != YFilter.not_set or
                            self.acl.yfilter != YFilter.not_set or
                            self.mirror_first.yfilter != YFilter.not_set or
                            self.mirror_interval.yfilter != YFilter.not_set or
                            (self.attachment is not None and self.attachment.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "span-monitor-session" + "[session-class='" + self.session_class.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_class.is_set or self.session_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_class.get_name_leafdata())
                        if (self.acl.is_set or self.acl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl.get_name_leafdata())
                        if (self.mirror_first.is_set or self.mirror_first.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_first.get_name_leafdata())
                        if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "attachment"):
                            if (self.attachment is None):
                                self.attachment = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment()
                                self.attachment.parent = self
                                self._children_name_map["attachment"] = "attachment"
                            return self.attachment

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attachment" or name == "session-class" or name == "acl" or name == "mirror-first" or name == "mirror-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-class"):
                            self.session_class = value
                            self.session_class.value_namespace = name_space
                            self.session_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl"):
                            self.acl = value
                            self.acl.value_namespace = name_space
                            self.acl.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-first"):
                            self.mirror_first = value
                            self.mirror_first.value_namespace = name_space
                            self.mirror_first.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-interval"):
                            self.mirror_interval = value
                            self.mirror_interval.value_namespace = name_space
                            self.mirror_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.span_monitor_session:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.span_monitor_session:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "span-monitor-session"):
                        for c in self.span_monitor_session:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.span_monitor_session.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "span-monitor-session"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.class_ = YLeaf(YType.str, "class")

                    self.default_gateway = YLeaf(YType.str, "default-gateway")

                    self.dhcpv4_option = YLeaf(YType.str, "dhcpv4-option")

                    self.session_limit = YLeaf(YType.int32, "session-limit")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("class_",
                                    "default_gateway",
                                    "dhcpv4_option",
                                    "session_limit") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.class_.is_set or
                        self.default_gateway.is_set or
                        self.dhcpv4_option.is_set or
                        self.session_limit.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.class_.yfilter != YFilter.not_set or
                        self.default_gateway.yfilter != YFilter.not_set or
                        self.dhcpv4_option.yfilter != YFilter.not_set or
                        self.session_limit.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg:dhcpd" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.class_.get_name_leafdata())
                    if (self.default_gateway.is_set or self.default_gateway.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_gateway.get_name_leafdata())
                    if (self.dhcpv4_option.is_set or self.dhcpv4_option.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcpv4_option.get_name_leafdata())
                    if (self.session_limit.is_set or self.session_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_limit.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "class" or name == "default-gateway" or name == "dhcpv4-option" or name == "session-limit"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "class"):
                        self.class_ = value
                        self.class_.value_namespace = name_space
                        self.class_.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-gateway"):
                        self.default_gateway = value
                        self.default_gateway.value_namespace = name_space
                        self.default_gateway.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcpv4-option"):
                        self.dhcpv4_option = value
                        self.dhcpv4_option.value_namespace = name_space
                        self.dhcpv4_option.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-limit"):
                        self.session_limit = value
                        self.session_limit.value_namespace = name_space
                        self.session_limit.value_namespace_prefix = name_space_prefix


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

                    self.default_vrf = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                    self._children_yang_names.add("default-vrf")


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

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.max_groups = YLeaf(YType.uint32, "max-groups")

                        self.multicast_mode = YLeaf(YType.enumeration, "multicast-mode")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_group",
                                        "max_groups",
                                        "multicast_mode",
                                        "query_interval",
                                        "query_max_response_time",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.enable.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "explicit-tracking" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.access_group.is_set or
                            self.max_groups.is_set or
                            self.multicast_mode.is_set or
                            self.query_interval.is_set or
                            self.query_max_response_time.is_set or
                            self.version.is_set or
                            (self.explicit_tracking is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_group.yfilter != YFilter.not_set or
                            self.max_groups.yfilter != YFilter.not_set or
                            self.multicast_mode.yfilter != YFilter.not_set or
                            self.query_interval.yfilter != YFilter.not_set or
                            self.query_max_response_time.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            (self.explicit_tracking is not None and self.explicit_tracking.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "default-vrf" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_group.get_name_leafdata())
                        if (self.max_groups.is_set or self.max_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_groups.get_name_leafdata())
                        if (self.multicast_mode.is_set or self.multicast_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_mode.get_name_leafdata())
                        if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_interval.get_name_leafdata())
                        if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "explicit-tracking"):
                            if (self.explicit_tracking is None):
                                self.explicit_tracking = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking()
                                self.explicit_tracking.parent = self
                                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                            return self.explicit_tracking

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "explicit-tracking" or name == "access-group" or name == "max-groups" or name == "multicast-mode" or name == "query-interval" or name == "query-max-response-time" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-group"):
                            self.access_group = value
                            self.access_group.value_namespace = name_space
                            self.access_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-groups"):
                            self.max_groups = value
                            self.max_groups.value_namespace = name_space
                            self.max_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-mode"):
                            self.multicast_mode = value
                            self.multicast_mode.value_namespace = name_space
                            self.multicast_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-interval"):
                            self.query_interval = value
                            self.query_interval.value_namespace = name_space
                            self.query_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-max-response-time"):
                            self.query_max_response_time = value
                            self.query_max_response_time.value_namespace = name_space
                            self.query_max_response_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.default_vrf is not None and self.default_vrf.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.default_vrf is not None and self.default_vrf.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg:igmp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "default-vrf"):
                        if (self.default_vrf is None):
                            self.default_vrf = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf()
                            self.default_vrf.parent = self
                            self._children_name_map["default_vrf"] = "default-vrf"
                        return self.default_vrf

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "default-vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unnumbered",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unnumbered.is_set or
                        self.unreachables.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unnumbered.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unnumbered.is_set or self.unnumbered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unnumbered.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mtu" or name == "rpf" or name == "unnumbered" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unnumbered"):
                        self.unnumbered = value
                        self.unnumbered.value_namespace = name_space
                        self.unnumbered.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network, self).__setattr__(name, value)


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

                        self.auto_configuration = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")


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

                            self.enable = YLeaf(YType.empty, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)

                        def has_data(self):
                            return self.enable.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.auto_configuration is not None and self.auto_configuration.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.auto_configuration is not None and self.auto_configuration.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "addresses" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "auto-configuration"):
                            if (self.auto_configuration is None):
                                self.auto_configuration = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration()
                                self.auto_configuration.parent = self
                                self._children_name_map["auto_configuration"] = "auto-configuration"
                            return self.auto_configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auto-configuration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unreachables.is_set or
                        (self.addresses is not None and self.addresses.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set or
                        (self.addresses is not None and self.addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "addresses"):
                        if (self.addresses is None):
                            self.addresses = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses()
                            self.addresses.parent = self
                            self._children_name_map["addresses"] = "addresses"
                        return self.addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "addresses" or name == "mtu" or name == "rpf" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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
                
                	**range:** 1000..3600000
                
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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("framed_prefix_pool",
                                    "managed_config",
                                    "ns_interval",
                                    "nud_enable",
                                    "other_config",
                                    "ra_lifetime",
                                    "ra_suppress",
                                    "ra_suppress_mtu",
                                    "ra_unicast",
                                    "ra_unspecify_hoplimit",
                                    "reachable_time",
                                    "router_preference",
                                    "start_ra_on_ipv6_enable",
                                    "suppress_cache_learning") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("maximum",
                                        "minimum") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.maximum.is_set or
                            self.minimum.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.maximum.yfilter != YFilter.not_set or
                            self.minimum.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-interval" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum.get_name_leafdata())
                        if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "maximum" or name == "minimum"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "maximum"):
                            self.maximum = value
                            self.maximum.value_namespace = name_space
                            self.maximum.value_namespace_prefix = name_space_prefix
                        if(value_path == "minimum"):
                            self.minimum = value
                            self.minimum.value_namespace = name_space
                            self.minimum.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "framed-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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

                        self.attempts = YLeaf(YType.uint32, "attempts")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("attempts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)

                    def has_data(self):
                        return self.attempts.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.attempts.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "duplicate-address-detection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.attempts.is_set or self.attempts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.attempts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attempts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "attempts"):
                            self.attempts = value
                            self.attempts.value_namespace = name_space
                            self.attempts.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.count.is_set or
                            self.interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-initial" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.count.get_name_leafdata())
                        if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count = value
                            self.count.value_namespace = name_space
                            self.count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interval"):
                            self.interval = value
                            self.interval.value_namespace = name_space
                            self.interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.framed_prefix_pool.is_set or
                        self.managed_config.is_set or
                        self.ns_interval.is_set or
                        self.nud_enable.is_set or
                        self.other_config.is_set or
                        self.ra_lifetime.is_set or
                        self.ra_suppress.is_set or
                        self.ra_suppress_mtu.is_set or
                        self.ra_unicast.is_set or
                        self.ra_unspecify_hoplimit.is_set or
                        self.reachable_time.is_set or
                        self.router_preference.is_set or
                        self.start_ra_on_ipv6_enable.is_set or
                        self.suppress_cache_learning.is_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_data()) or
                        (self.framed_prefix is not None) or
                        (self.ra_initial is not None) or
                        (self.ra_interval is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.framed_prefix_pool.yfilter != YFilter.not_set or
                        self.managed_config.yfilter != YFilter.not_set or
                        self.ns_interval.yfilter != YFilter.not_set or
                        self.nud_enable.yfilter != YFilter.not_set or
                        self.other_config.yfilter != YFilter.not_set or
                        self.ra_lifetime.yfilter != YFilter.not_set or
                        self.ra_suppress.yfilter != YFilter.not_set or
                        self.ra_suppress_mtu.yfilter != YFilter.not_set or
                        self.ra_unicast.yfilter != YFilter.not_set or
                        self.ra_unspecify_hoplimit.yfilter != YFilter.not_set or
                        self.reachable_time.yfilter != YFilter.not_set or
                        self.router_preference.yfilter != YFilter.not_set or
                        self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set or
                        self.suppress_cache_learning.yfilter != YFilter.not_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_operation()) or
                        (self.framed_prefix is not None and self.framed_prefix.has_operation()) or
                        (self.ra_initial is not None and self.ra_initial.has_operation()) or
                        (self.ra_interval is not None and self.ra_interval.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.framed_prefix_pool.is_set or self.framed_prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.framed_prefix_pool.get_name_leafdata())
                    if (self.managed_config.is_set or self.managed_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.managed_config.get_name_leafdata())
                    if (self.ns_interval.is_set or self.ns_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ns_interval.get_name_leafdata())
                    if (self.nud_enable.is_set or self.nud_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nud_enable.get_name_leafdata())
                    if (self.other_config.is_set or self.other_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.other_config.get_name_leafdata())
                    if (self.ra_lifetime.is_set or self.ra_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_lifetime.get_name_leafdata())
                    if (self.ra_suppress.is_set or self.ra_suppress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress.get_name_leafdata())
                    if (self.ra_suppress_mtu.is_set or self.ra_suppress_mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress_mtu.get_name_leafdata())
                    if (self.ra_unicast.is_set or self.ra_unicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unicast.get_name_leafdata())
                    if (self.ra_unspecify_hoplimit.is_set or self.ra_unspecify_hoplimit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unspecify_hoplimit.get_name_leafdata())
                    if (self.reachable_time.is_set or self.reachable_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reachable_time.get_name_leafdata())
                    if (self.router_preference.is_set or self.router_preference.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_preference.get_name_leafdata())
                    if (self.start_ra_on_ipv6_enable.is_set or self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_ra_on_ipv6_enable.get_name_leafdata())
                    if (self.suppress_cache_learning.is_set or self.suppress_cache_learning.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppress_cache_learning.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "duplicate-address-detection"):
                        if (self.duplicate_address_detection is None):
                            self.duplicate_address_detection = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection()
                            self.duplicate_address_detection.parent = self
                            self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                        return self.duplicate_address_detection

                    if (child_yang_name == "framed-prefix"):
                        if (self.framed_prefix is None):
                            self.framed_prefix = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix()
                            self.framed_prefix.parent = self
                            self._children_name_map["framed_prefix"] = "framed-prefix"
                        return self.framed_prefix

                    if (child_yang_name == "ra-initial"):
                        if (self.ra_initial is None):
                            self.ra_initial = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial()
                            self.ra_initial.parent = self
                            self._children_name_map["ra_initial"] = "ra-initial"
                        return self.ra_initial

                    if (child_yang_name == "ra-interval"):
                        if (self.ra_interval is None):
                            self.ra_interval = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval()
                            self.ra_interval.parent = self
                            self._children_name_map["ra_interval"] = "ra-interval"
                        return self.ra_interval

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "duplicate-address-detection" or name == "framed-prefix" or name == "ra-initial" or name == "ra-interval" or name == "framed-prefix-pool" or name == "managed-config" or name == "ns-interval" or name == "nud-enable" or name == "other-config" or name == "ra-lifetime" or name == "ra-suppress" or name == "ra-suppress-mtu" or name == "ra-unicast" or name == "ra-unspecify-hoplimit" or name == "reachable-time" or name == "router-preference" or name == "start-ra-on-ipv6-enable" or name == "suppress-cache-learning"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "framed-prefix-pool"):
                        self.framed_prefix_pool = value
                        self.framed_prefix_pool.value_namespace = name_space
                        self.framed_prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "managed-config"):
                        self.managed_config = value
                        self.managed_config.value_namespace = name_space
                        self.managed_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ns-interval"):
                        self.ns_interval = value
                        self.ns_interval.value_namespace = name_space
                        self.ns_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "nud-enable"):
                        self.nud_enable = value
                        self.nud_enable.value_namespace = name_space
                        self.nud_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "other-config"):
                        self.other_config = value
                        self.other_config.value_namespace = name_space
                        self.other_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-lifetime"):
                        self.ra_lifetime = value
                        self.ra_lifetime.value_namespace = name_space
                        self.ra_lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress"):
                        self.ra_suppress = value
                        self.ra_suppress.value_namespace = name_space
                        self.ra_suppress.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress-mtu"):
                        self.ra_suppress_mtu = value
                        self.ra_suppress_mtu.value_namespace = name_space
                        self.ra_suppress_mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unicast"):
                        self.ra_unicast = value
                        self.ra_unicast.value_namespace = name_space
                        self.ra_unicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unspecify-hoplimit"):
                        self.ra_unspecify_hoplimit = value
                        self.ra_unspecify_hoplimit.value_namespace = name_space
                        self.ra_unspecify_hoplimit.value_namespace_prefix = name_space_prefix
                    if(value_path == "reachable-time"):
                        self.reachable_time = value
                        self.reachable_time.value_namespace = name_space
                        self.reachable_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-preference"):
                        self.router_preference = value
                        self.router_preference.value_namespace = name_space
                        self.router_preference.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-ra-on-ipv6-enable"):
                        self.start_ra_on_ipv6_enable = value
                        self.start_ra_on_ipv6_enable.value_namespace = name_space
                        self.start_ra_on_ipv6_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppress-cache-learning"):
                        self.suppress_cache_learning = value
                        self.suppress_cache_learning.value_namespace = name_space
                        self.suppress_cache_learning.value_namespace_prefix = name_space_prefix


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

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.class_ = YLeaf(YType.str, "class")

                    self.delegated_prefix_pool = YLeaf(YType.str, "delegated-prefix-pool")

                    self.dns_ipv6address = YLeaf(YType.str, "dns-ipv6address")

                    self.mode_class = YLeaf(YType.str, "mode-class")

                    self.stateful_address = YLeaf(YType.str, "stateful-address")

                    self.delegated_prefix = None
                    self._children_name_map["delegated_prefix"] = "delegated-prefix"
                    self._children_yang_names.add("delegated-prefix")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address_pool",
                                    "class_",
                                    "delegated_prefix_pool",
                                    "dns_ipv6address",
                                    "mode_class",
                                    "stateful_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "delegated-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.address_pool.is_set or
                        self.class_.is_set or
                        self.delegated_prefix_pool.is_set or
                        self.dns_ipv6address.is_set or
                        self.mode_class.is_set or
                        self.stateful_address.is_set or
                        (self.delegated_prefix is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address_pool.yfilter != YFilter.not_set or
                        self.class_.yfilter != YFilter.not_set or
                        self.delegated_prefix_pool.yfilter != YFilter.not_set or
                        self.dns_ipv6address.yfilter != YFilter.not_set or
                        self.mode_class.yfilter != YFilter.not_set or
                        self.stateful_address.yfilter != YFilter.not_set or
                        (self.delegated_prefix is not None and self.delegated_prefix.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg:dhcpv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address_pool.is_set or self.address_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_pool.get_name_leafdata())
                    if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.class_.get_name_leafdata())
                    if (self.delegated_prefix_pool.is_set or self.delegated_prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delegated_prefix_pool.get_name_leafdata())
                    if (self.dns_ipv6address.is_set or self.dns_ipv6address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dns_ipv6address.get_name_leafdata())
                    if (self.mode_class.is_set or self.mode_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode_class.get_name_leafdata())
                    if (self.stateful_address.is_set or self.stateful_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.stateful_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "delegated-prefix"):
                        if (self.delegated_prefix is None):
                            self.delegated_prefix = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix()
                            self.delegated_prefix.parent = self
                            self._children_name_map["delegated_prefix"] = "delegated-prefix"
                        return self.delegated_prefix

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "delegated-prefix" or name == "address-pool" or name == "class" or name == "delegated-prefix-pool" or name == "dns-ipv6address" or name == "mode-class" or name == "stateful-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address-pool"):
                        self.address_pool = value
                        self.address_pool.value_namespace = name_space
                        self.address_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "class"):
                        self.class_ = value
                        self.class_.value_namespace = name_space
                        self.class_.value_namespace_prefix = name_space_prefix
                    if(value_path == "delegated-prefix-pool"):
                        self.delegated_prefix_pool = value
                        self.delegated_prefix_pool.value_namespace = name_space
                        self.delegated_prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "dns-ipv6address"):
                        self.dns_ipv6address = value
                        self.dns_ipv6address.value_namespace = name_space
                        self.dns_ipv6address.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode-class"):
                        self.mode_class = value
                        self.mode_class.value_namespace = name_space
                        self.mode_class.value_namespace_prefix = name_space_prefix
                    if(value_path == "stateful-address"):
                        self.stateful_address = value
                        self.stateful_address.value_namespace = name_space
                        self.stateful_address.value_namespace_prefix = name_space_prefix


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

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("service_policy_in") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr, self).__setattr__(name, value)


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

                        self.input = YLeaf(YType.str, "input")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("input") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy, self).__setattr__(name, value)

                    def has_data(self):
                        return self.input.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.input.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.input.is_set or self.input.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "input"):
                            self.input = value
                            self.input.value_namespace = name_space
                            self.input.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.service_policy_in.is_set or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.service_policy_in.yfilter != YFilter.not_set or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.service_policy_in.is_set or self.service_policy_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service_policy_in.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service-policy" or name == "service-policy-in"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "service-policy-in"):
                        self.service_policy_in = value
                        self.service_policy_in.value_namespace = name_space
                        self.service_policy_in.value_namespace_prefix = name_space_prefix


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

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "input" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "output" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.input is not None) or
                            (self.output is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.input is not None and self.input.has_operation()) or
                            (self.output is not None and self.output.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "input"):
                            if (self.input is None):
                                self.input = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                            return self.input

                        if (child_yang_name == "output"):
                            if (self.output is None):
                                self.output = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                            return self.output

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input" or name == "output"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aal",
                                        "atm_cell_tax",
                                        "encapsulation",
                                        "user_defined") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.aal.is_set or
                            self.atm_cell_tax.is_set or
                            self.encapsulation.is_set or
                            self.user_defined.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aal.yfilter != YFilter.not_set or
                            self.atm_cell_tax.yfilter != YFilter.not_set or
                            self.encapsulation.yfilter != YFilter.not_set or
                            self.user_defined.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "account" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aal.is_set or self.aal.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aal.get_name_leafdata())
                        if (self.atm_cell_tax.is_set or self.atm_cell_tax.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.atm_cell_tax.get_name_leafdata())
                        if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation.get_name_leafdata())
                        if (self.user_defined.is_set or self.user_defined.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_defined.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aal" or name == "atm-cell-tax" or name == "encapsulation" or name == "user-defined"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aal"):
                            self.aal = value
                            self.aal.value_namespace = name_space
                            self.aal.value_namespace_prefix = name_space_prefix
                        if(value_path == "atm-cell-tax"):
                            self.atm_cell_tax = value
                            self.atm_cell_tax.value_namespace = name_space
                            self.atm_cell_tax.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation"):
                            self.encapsulation = value
                            self.encapsulation.value_namespace = name_space
                            self.encapsulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-defined"):
                            self.user_defined = value
                            self.user_defined.value_namespace = name_space
                            self.user_defined.value_namespace_prefix = name_space_prefix


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

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("minimum_bandwidth") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output, self).__setattr__(name, value)

                    def has_data(self):
                        return self.minimum_bandwidth.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.minimum_bandwidth.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "output" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.minimum_bandwidth.is_set or self.minimum_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum_bandwidth.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "minimum-bandwidth"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "minimum-bandwidth"):
                            self.minimum_bandwidth = value
                            self.minimum_bandwidth.value_namespace = name_space
                            self.minimum_bandwidth.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.account is not None and self.account.has_data()) or
                        (self.output is not None and self.output.has_data()) or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.account is not None and self.account.has_operation()) or
                        (self.output is not None and self.output.has_operation()) or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-qos-ma-bng-cfg:qos" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "account"):
                        if (self.account is None):
                            self.account = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account()
                            self.account.parent = self
                            self._children_name_map["account"] = "account"
                        return self.account

                    if (child_yang_name == "output"):
                        if (self.output is None):
                            self.output = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output()
                            self.output.parent = self
                            self._children_name_map["output"] = "output"
                        return self.output

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "account" or name == "output" or name == "service-policy"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prepaid_feature") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting, self).__setattr__(name, value)


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

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accounting_interim_interval",
                                        "method_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accounting_interim_interval.is_set or
                            self.method_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accounting_interim_interval.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-accounting" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accounting_interim_interval.is_set or self.accounting_interim_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_interim_interval.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-interim-interval" or name == "method-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accounting-interim-interval"):
                            self.accounting_interim_interval = value
                            self.accounting_interim_interval.value_namespace = name_space
                            self.accounting_interim_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix


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

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dual_stack_delay",
                                        "hold_acct_start",
                                        "method_list_name",
                                        "periodic_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dual_stack_delay.is_set or
                            self.hold_acct_start.is_set or
                            self.method_list_name.is_set or
                            self.periodic_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dual_stack_delay.yfilter != YFilter.not_set or
                            self.hold_acct_start.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set or
                            self.periodic_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dual_stack_delay.is_set or self.dual_stack_delay.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dual_stack_delay.get_name_leafdata())
                        if (self.hold_acct_start.is_set or self.hold_acct_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_acct_start.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())
                        if (self.periodic_interval.is_set or self.periodic_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.periodic_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dual-stack-delay" or name == "hold-acct-start" or name == "method-list-name" or name == "periodic-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dual-stack-delay"):
                            self.dual_stack_delay = value
                            self.dual_stack_delay.value_namespace = name_space
                            self.dual_stack_delay.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-acct-start"):
                            self.hold_acct_start = value
                            self.hold_acct_start.value_namespace = name_space
                            self.hold_acct_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "periodic-interval"):
                            self.periodic_interval = value
                            self.periodic_interval.value_namespace = name_space
                            self.periodic_interval.value_namespace_prefix = name_space_prefix


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.int32, "threshold")

                        self.timeout_value = YLeaf(YType.int32, "timeout-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction",
                                        "threshold",
                                        "timeout_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.direction.is_set or
                            self.threshold.is_set or
                            self.timeout_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set or
                            self.timeout_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "idle-timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())
                        if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction" or name == "threshold" or name == "timeout-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-value"):
                            self.timeout_value = value
                            self.timeout_value.value_namespace = name_space
                            self.timeout_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.prepaid_feature.is_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_data()) or
                        (self.service_accounting is not None and self.service_accounting.has_data()) or
                        (self.session is not None and self.session.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prepaid_feature.yfilter != YFilter.not_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_operation()) or
                        (self.service_accounting is not None and self.service_accounting.has_operation()) or
                        (self.session is not None and self.session.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prepaid_feature.is_set or self.prepaid_feature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prepaid_feature.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "idle-timeout"):
                        if (self.idle_timeout is None):
                            self.idle_timeout = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout()
                            self.idle_timeout.parent = self
                            self._children_name_map["idle_timeout"] = "idle-timeout"
                        return self.idle_timeout

                    if (child_yang_name == "service-accounting"):
                        if (self.service_accounting is None):
                            self.service_accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting()
                            self.service_accounting.parent = self
                            self._children_name_map["service_accounting"] = "service-accounting"
                        return self.service_accounting

                    if (child_yang_name == "session"):
                        if (self.session is None):
                            self.session = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                        return self.session

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "idle-timeout" or name == "service-accounting" or name == "session" or name == "prepaid-feature"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prepaid-feature"):
                        self.prepaid_feature = value
                        self.prepaid_feature.value_namespace = name_space
                        self.prepaid_feature.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.template_name.is_set or
                    self.vrf.is_set or
                    (self.accounting is not None and self.accounting.has_data()) or
                    (self.dhcpd is not None and self.dhcpd.has_data()) or
                    (self.dhcpv6 is not None and self.dhcpv6.has_data()) or
                    (self.igmp is not None and self.igmp.has_data()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_data()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_data()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_data()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_data()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_data()) or
                    (self.pbr is not None and self.pbr.has_data()) or
                    (self.qos is not None and self.qos.has_data()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.template_name.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.accounting is not None and self.accounting.has_operation()) or
                    (self.dhcpd is not None and self.dhcpd.has_operation()) or
                    (self.dhcpv6 is not None and self.dhcpv6.has_operation()) or
                    (self.igmp is not None and self.igmp.has_operation()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_operation()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_operation()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_operation()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_operation()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_operation()) or
                    (self.pbr is not None and self.pbr.has_operation()) or
                    (self.qos is not None and self.qos.has_operation()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ip-subscriber" + "[template-name='" + self.template_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/ip-subscribers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.template_name.is_set or self.template_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.template_name.get_name_leafdata())
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "accounting"):
                    if (self.accounting is None):
                        self.accounting = DynamicTemplate.IpSubscribers.IpSubscriber.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                    return self.accounting

                if (child_yang_name == "dhcpd"):
                    if (self.dhcpd is None):
                        self.dhcpd = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd()
                        self.dhcpd.parent = self
                        self._children_name_map["dhcpd"] = "dhcpd"
                    return self.dhcpd

                if (child_yang_name == "dhcpv6"):
                    if (self.dhcpv6 is None):
                        self.dhcpv6 = DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6()
                        self.dhcpv6.parent = self
                        self._children_name_map["dhcpv6"] = "dhcpv6"
                    return self.dhcpv6

                if (child_yang_name == "igmp"):
                    if (self.igmp is None):
                        self.igmp = DynamicTemplate.IpSubscribers.IpSubscriber.Igmp()
                        self.igmp.parent = self
                        self._children_name_map["igmp"] = "igmp"
                    return self.igmp

                if (child_yang_name == "ipv4-network"):
                    if (self.ipv4_network is None):
                        self.ipv4_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network()
                        self.ipv4_network.parent = self
                        self._children_name_map["ipv4_network"] = "ipv4-network"
                    return self.ipv4_network

                if (child_yang_name == "ipv4-packet-filter"):
                    if (self.ipv4_packet_filter is None):
                        self.ipv4_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter()
                        self.ipv4_packet_filter.parent = self
                        self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                    return self.ipv4_packet_filter

                if (child_yang_name == "ipv6-neighbor"):
                    if (self.ipv6_neighbor is None):
                        self.ipv6_neighbor = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor()
                        self.ipv6_neighbor.parent = self
                        self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                    return self.ipv6_neighbor

                if (child_yang_name == "ipv6-network"):
                    if (self.ipv6_network is None):
                        self.ipv6_network = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network()
                        self.ipv6_network.parent = self
                        self._children_name_map["ipv6_network"] = "ipv6-network"
                    return self.ipv6_network

                if (child_yang_name == "ipv6-packet-filter"):
                    if (self.ipv6_packet_filter is None):
                        self.ipv6_packet_filter = DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter()
                        self.ipv6_packet_filter.parent = self
                        self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                    return self.ipv6_packet_filter

                if (child_yang_name == "pbr"):
                    if (self.pbr is None):
                        self.pbr = DynamicTemplate.IpSubscribers.IpSubscriber.Pbr()
                        self.pbr.parent = self
                        self._children_name_map["pbr"] = "pbr"
                    return self.pbr

                if (child_yang_name == "qos"):
                    if (self.qos is None):
                        self.qos = DynamicTemplate.IpSubscribers.IpSubscriber.Qos()
                        self.qos.parent = self
                        self._children_name_map["qos"] = "qos"
                    return self.qos

                if (child_yang_name == "span-monitor-sessions"):
                    if (self.span_monitor_sessions is None):
                        self.span_monitor_sessions = DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions()
                        self.span_monitor_sessions.parent = self
                        self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                    return self.span_monitor_sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting" or name == "dhcpd" or name == "dhcpv6" or name == "igmp" or name == "ipv4-network" or name == "ipv4-packet-filter" or name == "ipv6-neighbor" or name == "ipv6-network" or name == "ipv6-packet-filter" or name == "pbr" or name == "qos" or name == "span-monitor-sessions" or name == "template-name" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "template-name"):
                    self.template_name = value
                    self.template_name.value_namespace = name_space
                    self.template_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ip_subscriber:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ip_subscriber:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ip-subscribers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ip-subscriber"):
                for c in self.ip_subscriber:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DynamicTemplate.IpSubscribers.IpSubscriber()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ip_subscriber.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ip-subscriber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.subscriber_service = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DynamicTemplate.SubscriberServices, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DynamicTemplate.SubscriberServices, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("template_name",
                                "vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DynamicTemplate.SubscriberServices.SubscriberService, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DynamicTemplate.SubscriberServices.SubscriberService, self).__setattr__(name, value)


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

                    self.span_monitor_session = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions, self).__setattr__(name, value)


                class SpanMonitorSession(Entity):
                    """
                    Configuration for a particular class of Monitor
                    Session
                    
                    .. attribute:: session_class  <key>
                    
                    	Session Class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
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
                    	**type**\:   :py:class:`SpanMirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg.SpanMirrorInterval>`
                    
                    

                    """

                    _prefix = 'ethernet-span-subscriber-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, self).__init__()

                        self.yang_name = "span-monitor-session"
                        self.yang_parent_name = "span-monitor-sessions"

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.acl = YLeaf(YType.empty, "acl")

                        self.mirror_first = YLeaf(YType.uint32, "mirror-first")

                        self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                        self.attachment = None
                        self._children_name_map["attachment"] = "attachment"
                        self._children_yang_names.add("attachment")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_class",
                                        "acl",
                                        "mirror_first",
                                        "mirror_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession, self).__setattr__(name, value)


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
                            self.is_presence_container = True

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.port_level_enable = YLeaf(YType.empty, "port-level-enable")

                            self.session_name = YLeaf(YType.str, "session-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "port_level_enable",
                                            "session_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.port_level_enable.is_set or
                                self.session_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.port_level_enable.yfilter != YFilter.not_set or
                                self.session_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "attachment" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.port_level_enable.is_set or self.port_level_enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_level_enable.get_name_leafdata())
                            if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "port-level-enable" or name == "session-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-level-enable"):
                                self.port_level_enable = value
                                self.port_level_enable.value_namespace = name_space
                                self.port_level_enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-name"):
                                self.session_name = value
                                self.session_name.value_namespace = name_space
                                self.session_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.session_class.is_set or
                            self.acl.is_set or
                            self.mirror_first.is_set or
                            self.mirror_interval.is_set or
                            (self.attachment is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_class.yfilter != YFilter.not_set or
                            self.acl.yfilter != YFilter.not_set or
                            self.mirror_first.yfilter != YFilter.not_set or
                            self.mirror_interval.yfilter != YFilter.not_set or
                            (self.attachment is not None and self.attachment.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "span-monitor-session" + "[session-class='" + self.session_class.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_class.is_set or self.session_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_class.get_name_leafdata())
                        if (self.acl.is_set or self.acl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.acl.get_name_leafdata())
                        if (self.mirror_first.is_set or self.mirror_first.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_first.get_name_leafdata())
                        if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mirror_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "attachment"):
                            if (self.attachment is None):
                                self.attachment = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment()
                                self.attachment.parent = self
                                self._children_name_map["attachment"] = "attachment"
                            return self.attachment

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attachment" or name == "session-class" or name == "acl" or name == "mirror-first" or name == "mirror-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-class"):
                            self.session_class = value
                            self.session_class.value_namespace = name_space
                            self.session_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "acl"):
                            self.acl = value
                            self.acl.value_namespace = name_space
                            self.acl.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-first"):
                            self.mirror_first = value
                            self.mirror_first.value_namespace = name_space
                            self.mirror_first.value_namespace_prefix = name_space_prefix
                        if(value_path == "mirror-interval"):
                            self.mirror_interval = value
                            self.mirror_interval.value_namespace = name_space
                            self.mirror_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.span_monitor_session:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.span_monitor_session:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg:span-monitor-sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "span-monitor-session"):
                        for c in self.span_monitor_session:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.span_monitor_session.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "span-monitor-session"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.hardware_count = YLeaf(YType.empty, "hardware-count")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "hardware_count",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.hardware_count.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.hardware_count.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.hardware_count.is_set or self.hardware_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_count.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "hardware-count" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-count"):
                            self.hardware_count = value
                            self.hardware_count.value_namespace = name_space
                            self.hardware_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv4-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound()
                    self.inbound.parent = self
                    self._children_name_map["inbound"] = "inbound"
                    self._children_yang_names.add("inbound")

                    self.outbound = None
                    self._children_name_map["outbound"] = "outbound"
                    self._children_yang_names.add("outbound")


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

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.common_acl_name = YLeaf(YType.str, "common-acl-name")

                        self.interface_statistics = YLeaf(YType.empty, "interface-statistics")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_acl_name",
                                        "interface_statistics",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_acl_name.is_set or
                            self.interface_statistics.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_acl_name.yfilter != YFilter.not_set or
                            self.interface_statistics.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outbound" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_acl_name.is_set or self.common_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_acl_name.get_name_leafdata())
                        if (self.interface_statistics.is_set or self.interface_statistics.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_statistics.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-acl-name" or name == "interface-statistics" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-acl-name"):
                            self.common_acl_name = value
                            self.common_acl_name.value_namespace = name_space
                            self.common_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-statistics"):
                            self.interface_statistics = value
                            self.interface_statistics.value_namespace = name_space
                            self.interface_statistics.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.inbound is not None and self.inbound.has_data()) or
                        (self.outbound is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.inbound is not None and self.inbound.has_operation()) or
                        (self.outbound is not None and self.outbound.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-subscriber-cfg:ipv6-packet-filter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "inbound"):
                        if (self.inbound is None):
                            self.inbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound()
                            self.inbound.parent = self
                            self._children_name_map["inbound"] = "inbound"
                        return self.inbound

                    if (child_yang_name == "outbound"):
                        if (self.outbound is None):
                            self.outbound = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound()
                            self.outbound.parent = self
                            self._children_name_map["outbound"] = "outbound"
                        return self.outbound

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inbound" or name == "outbound"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unnumbered = YLeaf(YType.str, "unnumbered")

                    self.unreachables = YLeaf(YType.boolean, "unreachables")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unnumbered",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unnumbered.is_set or
                        self.unreachables.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unnumbered.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv4-ma-subscriber-cfg:ipv4-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unnumbered.is_set or self.unnumbered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unnumbered.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mtu" or name == "rpf" or name == "unnumbered" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unnumbered"):
                        self.unnumbered = value
                        self.unnumbered.value_namespace = name_space
                        self.unnumbered.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.rpf = YLeaf(YType.boolean, "rpf")

                    self.unreachables = YLeaf(YType.empty, "unreachables")

                    self.addresses = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mtu",
                                    "rpf",
                                    "unreachables") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network, self).__setattr__(name, value)


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

                        self.auto_configuration = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration()
                        self.auto_configuration.parent = self
                        self._children_name_map["auto_configuration"] = "auto-configuration"
                        self._children_yang_names.add("auto-configuration")


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

                            self.enable = YLeaf(YType.empty, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration, self).__setattr__(name, value)

                        def has_data(self):
                            return self.enable.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.auto_configuration is not None and self.auto_configuration.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.auto_configuration is not None and self.auto_configuration.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "addresses" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "auto-configuration"):
                            if (self.auto_configuration is None):
                                self.auto_configuration = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration()
                                self.auto_configuration.parent = self
                                self._children_name_map["auto_configuration"] = "auto-configuration"
                            return self.auto_configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auto-configuration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.mtu.is_set or
                        self.rpf.is_set or
                        self.unreachables.is_set or
                        (self.addresses is not None and self.addresses.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.rpf.yfilter != YFilter.not_set or
                        self.unreachables.yfilter != YFilter.not_set or
                        (self.addresses is not None and self.addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-ma-subscriber-cfg:ipv6-network" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.rpf.is_set or self.rpf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpf.get_name_leafdata())
                    if (self.unreachables.is_set or self.unreachables.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unreachables.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "addresses"):
                        if (self.addresses is None):
                            self.addresses = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses()
                            self.addresses.parent = self
                            self._children_name_map["addresses"] = "addresses"
                        return self.addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "addresses" or name == "mtu" or name == "rpf" or name == "unreachables"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpf"):
                        self.rpf = value
                        self.rpf.value_namespace = name_space
                        self.rpf.value_namespace_prefix = name_space_prefix
                    if(value_path == "unreachables"):
                        self.unreachables = value
                        self.unreachables.value_namespace = name_space
                        self.unreachables.value_namespace_prefix = name_space_prefix


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
                
                	**range:** 1000..3600000
                
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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("framed_prefix_pool",
                                    "managed_config",
                                    "ns_interval",
                                    "nud_enable",
                                    "other_config",
                                    "ra_lifetime",
                                    "ra_suppress",
                                    "ra_suppress_mtu",
                                    "ra_unicast",
                                    "ra_unspecify_hoplimit",
                                    "reachable_time",
                                    "router_preference",
                                    "start_ra_on_ipv6_enable",
                                    "suppress_cache_learning") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("maximum",
                                        "minimum") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.maximum.is_set or
                            self.minimum.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.maximum.yfilter != YFilter.not_set or
                            self.minimum.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-interval" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum.get_name_leafdata())
                        if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "maximum" or name == "minimum"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "maximum"):
                            self.maximum = value
                            self.maximum.value_namespace = name_space
                            self.maximum.value_namespace_prefix = name_space_prefix
                        if(value_path == "minimum"):
                            self.minimum = value
                            self.minimum.value_namespace = name_space
                            self.minimum.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "framed-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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

                        self.attempts = YLeaf(YType.uint32, "attempts")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("attempts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection, self).__setattr__(name, value)

                    def has_data(self):
                        return self.attempts.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.attempts.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "duplicate-address-detection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.attempts.is_set or self.attempts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.attempts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attempts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "attempts"):
                            self.attempts = value
                            self.attempts.value_namespace = name_space
                            self.attempts.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.count = YLeaf(YType.uint32, "count")

                        self.interval = YLeaf(YType.uint32, "interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.count.is_set or
                            self.interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ra-initial" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.count.get_name_leafdata())
                        if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count = value
                            self.count.value_namespace = name_space
                            self.count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interval"):
                            self.interval = value
                            self.interval.value_namespace = name_space
                            self.interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.framed_prefix_pool.is_set or
                        self.managed_config.is_set or
                        self.ns_interval.is_set or
                        self.nud_enable.is_set or
                        self.other_config.is_set or
                        self.ra_lifetime.is_set or
                        self.ra_suppress.is_set or
                        self.ra_suppress_mtu.is_set or
                        self.ra_unicast.is_set or
                        self.ra_unspecify_hoplimit.is_set or
                        self.reachable_time.is_set or
                        self.router_preference.is_set or
                        self.start_ra_on_ipv6_enable.is_set or
                        self.suppress_cache_learning.is_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_data()) or
                        (self.framed_prefix is not None) or
                        (self.ra_initial is not None) or
                        (self.ra_interval is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.framed_prefix_pool.yfilter != YFilter.not_set or
                        self.managed_config.yfilter != YFilter.not_set or
                        self.ns_interval.yfilter != YFilter.not_set or
                        self.nud_enable.yfilter != YFilter.not_set or
                        self.other_config.yfilter != YFilter.not_set or
                        self.ra_lifetime.yfilter != YFilter.not_set or
                        self.ra_suppress.yfilter != YFilter.not_set or
                        self.ra_suppress_mtu.yfilter != YFilter.not_set or
                        self.ra_unicast.yfilter != YFilter.not_set or
                        self.ra_unspecify_hoplimit.yfilter != YFilter.not_set or
                        self.reachable_time.yfilter != YFilter.not_set or
                        self.router_preference.yfilter != YFilter.not_set or
                        self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set or
                        self.suppress_cache_learning.yfilter != YFilter.not_set or
                        (self.duplicate_address_detection is not None and self.duplicate_address_detection.has_operation()) or
                        (self.framed_prefix is not None and self.framed_prefix.has_operation()) or
                        (self.ra_initial is not None and self.ra_initial.has_operation()) or
                        (self.ra_interval is not None and self.ra_interval.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-ipv6-nd-subscriber-cfg:ipv6-neighbor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.framed_prefix_pool.is_set or self.framed_prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.framed_prefix_pool.get_name_leafdata())
                    if (self.managed_config.is_set or self.managed_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.managed_config.get_name_leafdata())
                    if (self.ns_interval.is_set or self.ns_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ns_interval.get_name_leafdata())
                    if (self.nud_enable.is_set or self.nud_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nud_enable.get_name_leafdata())
                    if (self.other_config.is_set or self.other_config.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.other_config.get_name_leafdata())
                    if (self.ra_lifetime.is_set or self.ra_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_lifetime.get_name_leafdata())
                    if (self.ra_suppress.is_set or self.ra_suppress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress.get_name_leafdata())
                    if (self.ra_suppress_mtu.is_set or self.ra_suppress_mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_suppress_mtu.get_name_leafdata())
                    if (self.ra_unicast.is_set or self.ra_unicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unicast.get_name_leafdata())
                    if (self.ra_unspecify_hoplimit.is_set or self.ra_unspecify_hoplimit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ra_unspecify_hoplimit.get_name_leafdata())
                    if (self.reachable_time.is_set or self.reachable_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reachable_time.get_name_leafdata())
                    if (self.router_preference.is_set or self.router_preference.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_preference.get_name_leafdata())
                    if (self.start_ra_on_ipv6_enable.is_set or self.start_ra_on_ipv6_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_ra_on_ipv6_enable.get_name_leafdata())
                    if (self.suppress_cache_learning.is_set or self.suppress_cache_learning.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppress_cache_learning.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "duplicate-address-detection"):
                        if (self.duplicate_address_detection is None):
                            self.duplicate_address_detection = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection()
                            self.duplicate_address_detection.parent = self
                            self._children_name_map["duplicate_address_detection"] = "duplicate-address-detection"
                        return self.duplicate_address_detection

                    if (child_yang_name == "framed-prefix"):
                        if (self.framed_prefix is None):
                            self.framed_prefix = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix()
                            self.framed_prefix.parent = self
                            self._children_name_map["framed_prefix"] = "framed-prefix"
                        return self.framed_prefix

                    if (child_yang_name == "ra-initial"):
                        if (self.ra_initial is None):
                            self.ra_initial = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial()
                            self.ra_initial.parent = self
                            self._children_name_map["ra_initial"] = "ra-initial"
                        return self.ra_initial

                    if (child_yang_name == "ra-interval"):
                        if (self.ra_interval is None):
                            self.ra_interval = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval()
                            self.ra_interval.parent = self
                            self._children_name_map["ra_interval"] = "ra-interval"
                        return self.ra_interval

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "duplicate-address-detection" or name == "framed-prefix" or name == "ra-initial" or name == "ra-interval" or name == "framed-prefix-pool" or name == "managed-config" or name == "ns-interval" or name == "nud-enable" or name == "other-config" or name == "ra-lifetime" or name == "ra-suppress" or name == "ra-suppress-mtu" or name == "ra-unicast" or name == "ra-unspecify-hoplimit" or name == "reachable-time" or name == "router-preference" or name == "start-ra-on-ipv6-enable" or name == "suppress-cache-learning"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "framed-prefix-pool"):
                        self.framed_prefix_pool = value
                        self.framed_prefix_pool.value_namespace = name_space
                        self.framed_prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "managed-config"):
                        self.managed_config = value
                        self.managed_config.value_namespace = name_space
                        self.managed_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ns-interval"):
                        self.ns_interval = value
                        self.ns_interval.value_namespace = name_space
                        self.ns_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "nud-enable"):
                        self.nud_enable = value
                        self.nud_enable.value_namespace = name_space
                        self.nud_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "other-config"):
                        self.other_config = value
                        self.other_config.value_namespace = name_space
                        self.other_config.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-lifetime"):
                        self.ra_lifetime = value
                        self.ra_lifetime.value_namespace = name_space
                        self.ra_lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress"):
                        self.ra_suppress = value
                        self.ra_suppress.value_namespace = name_space
                        self.ra_suppress.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-suppress-mtu"):
                        self.ra_suppress_mtu = value
                        self.ra_suppress_mtu.value_namespace = name_space
                        self.ra_suppress_mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unicast"):
                        self.ra_unicast = value
                        self.ra_unicast.value_namespace = name_space
                        self.ra_unicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "ra-unspecify-hoplimit"):
                        self.ra_unspecify_hoplimit = value
                        self.ra_unspecify_hoplimit.value_namespace = name_space
                        self.ra_unspecify_hoplimit.value_namespace_prefix = name_space_prefix
                    if(value_path == "reachable-time"):
                        self.reachable_time = value
                        self.reachable_time.value_namespace = name_space
                        self.reachable_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-preference"):
                        self.router_preference = value
                        self.router_preference.value_namespace = name_space
                        self.router_preference.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-ra-on-ipv6-enable"):
                        self.start_ra_on_ipv6_enable = value
                        self.start_ra_on_ipv6_enable.value_namespace = name_space
                        self.start_ra_on_ipv6_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppress-cache-learning"):
                        self.suppress_cache_learning = value
                        self.suppress_cache_learning.value_namespace = name_space
                        self.suppress_cache_learning.value_namespace_prefix = name_space_prefix


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

                    self.service_policy_in = YLeaf(YType.str, "service-policy-in")

                    self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("service_policy_in") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr, self).__setattr__(name, value)


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

                        self.input = YLeaf(YType.str, "input")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("input") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy, self).__setattr__(name, value)

                    def has_data(self):
                        return self.input.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.input.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.input.is_set or self.input.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "input"):
                            self.input = value
                            self.input.value_namespace = name_space
                            self.input.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.service_policy_in.is_set or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.service_policy_in.yfilter != YFilter.not_set or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-pbr-subscriber-cfg:pbr" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.service_policy_in.is_set or self.service_policy_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service_policy_in.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service-policy" or name == "service-policy-in"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "service-policy-in"):
                        self.service_policy_in = value
                        self.service_policy_in.value_namespace = name_space
                        self.service_policy_in.value_namespace_prefix = name_space_prefix


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

                        self.input = None
                        self._children_name_map["input"] = "input"
                        self._children_yang_names.add("input")

                        self.output = None
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "input" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix


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
                            self.is_presence_container = True

                            self.account_stats = YLeaf(YType.boolean, "account-stats")

                            self.merge = YLeaf(YType.boolean, "merge")

                            self.merge_id = YLeaf(YType.uint32, "merge-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.spi_name = YLeaf(YType.str, "spi-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("account_stats",
                                            "merge",
                                            "merge_id",
                                            "policy_name",
                                            "spi_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.account_stats.is_set or
                                self.merge.is_set or
                                self.merge_id.is_set or
                                self.policy_name.is_set or
                                self.spi_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.account_stats.yfilter != YFilter.not_set or
                                self.merge.yfilter != YFilter.not_set or
                                self.merge_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.spi_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "output" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.account_stats.is_set or self.account_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.account_stats.get_name_leafdata())
                            if (self.merge.is_set or self.merge.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge.get_name_leafdata())
                            if (self.merge_id.is_set or self.merge_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.merge_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.spi_name.is_set or self.spi_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "account-stats" or name == "merge" or name == "merge-id" or name == "policy-name" or name == "spi-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "account-stats"):
                                self.account_stats = value
                                self.account_stats.value_namespace = name_space
                                self.account_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge"):
                                self.merge = value
                                self.merge.value_namespace = name_space
                                self.merge.value_namespace_prefix = name_space_prefix
                            if(value_path == "merge-id"):
                                self.merge_id = value
                                self.merge_id.value_namespace = name_space
                                self.merge_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi-name"):
                                self.spi_name = value
                                self.spi_name.value_namespace = name_space
                                self.spi_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.input is not None) or
                            (self.output is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.input is not None and self.input.has_operation()) or
                            (self.output is not None and self.output.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "input"):
                            if (self.input is None):
                                self.input = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                            return self.input

                        if (child_yang_name == "output"):
                            if (self.output is None):
                                self.output = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                            return self.output

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "input" or name == "output"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.aal = YLeaf(YType.enumeration, "aal")

                        self.atm_cell_tax = YLeaf(YType.empty, "atm-cell-tax")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.user_defined = YLeaf(YType.int32, "user-defined")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aal",
                                        "atm_cell_tax",
                                        "encapsulation",
                                        "user_defined") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.aal.is_set or
                            self.atm_cell_tax.is_set or
                            self.encapsulation.is_set or
                            self.user_defined.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aal.yfilter != YFilter.not_set or
                            self.atm_cell_tax.yfilter != YFilter.not_set or
                            self.encapsulation.yfilter != YFilter.not_set or
                            self.user_defined.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "account" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aal.is_set or self.aal.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aal.get_name_leafdata())
                        if (self.atm_cell_tax.is_set or self.atm_cell_tax.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.atm_cell_tax.get_name_leafdata())
                        if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation.get_name_leafdata())
                        if (self.user_defined.is_set or self.user_defined.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user_defined.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aal" or name == "atm-cell-tax" or name == "encapsulation" or name == "user-defined"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aal"):
                            self.aal = value
                            self.aal.value_namespace = name_space
                            self.aal.value_namespace_prefix = name_space_prefix
                        if(value_path == "atm-cell-tax"):
                            self.atm_cell_tax = value
                            self.atm_cell_tax.value_namespace = name_space
                            self.atm_cell_tax.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation"):
                            self.encapsulation = value
                            self.encapsulation.value_namespace = name_space
                            self.encapsulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "user-defined"):
                            self.user_defined = value
                            self.user_defined.value_namespace = name_space
                            self.user_defined.value_namespace_prefix = name_space_prefix


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

                        self.minimum_bandwidth = YLeaf(YType.uint32, "minimum-bandwidth")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("minimum_bandwidth") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output, self).__setattr__(name, value)

                    def has_data(self):
                        return self.minimum_bandwidth.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.minimum_bandwidth.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "output" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.minimum_bandwidth.is_set or self.minimum_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum_bandwidth.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "minimum-bandwidth"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "minimum-bandwidth"):
                            self.minimum_bandwidth = value
                            self.minimum_bandwidth.value_namespace = name_space
                            self.minimum_bandwidth.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.account is not None and self.account.has_data()) or
                        (self.output is not None and self.output.has_data()) or
                        (self.service_policy is not None and self.service_policy.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.account is not None and self.account.has_operation()) or
                        (self.output is not None and self.output.has_operation()) or
                        (self.service_policy is not None and self.service_policy.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-qos-ma-bng-cfg:qos" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "account"):
                        if (self.account is None):
                            self.account = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account()
                            self.account.parent = self
                            self._children_name_map["account"] = "account"
                        return self.account

                    if (child_yang_name == "output"):
                        if (self.output is None):
                            self.output = DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output()
                            self.output.parent = self
                            self._children_name_map["output"] = "output"
                        return self.output

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "account" or name == "output" or name == "service-policy"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prepaid_feature") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting, self).__setattr__(name, value)


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

                        self.accounting_interim_interval = YLeaf(YType.int32, "accounting-interim-interval")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accounting_interim_interval",
                                        "method_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accounting_interim_interval.is_set or
                            self.method_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accounting_interim_interval.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-accounting" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accounting_interim_interval.is_set or self.accounting_interim_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_interim_interval.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-interim-interval" or name == "method-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accounting-interim-interval"):
                            self.accounting_interim_interval = value
                            self.accounting_interim_interval.value_namespace = name_space
                            self.accounting_interim_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix


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

                        self.dual_stack_delay = YLeaf(YType.int32, "dual-stack-delay")

                        self.hold_acct_start = YLeaf(YType.int32, "hold-acct-start")

                        self.method_list_name = YLeaf(YType.str, "method-list-name")

                        self.periodic_interval = YLeaf(YType.int32, "periodic-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dual_stack_delay",
                                        "hold_acct_start",
                                        "method_list_name",
                                        "periodic_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dual_stack_delay.is_set or
                            self.hold_acct_start.is_set or
                            self.method_list_name.is_set or
                            self.periodic_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dual_stack_delay.yfilter != YFilter.not_set or
                            self.hold_acct_start.yfilter != YFilter.not_set or
                            self.method_list_name.yfilter != YFilter.not_set or
                            self.periodic_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dual_stack_delay.is_set or self.dual_stack_delay.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dual_stack_delay.get_name_leafdata())
                        if (self.hold_acct_start.is_set or self.hold_acct_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_acct_start.get_name_leafdata())
                        if (self.method_list_name.is_set or self.method_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method_list_name.get_name_leafdata())
                        if (self.periodic_interval.is_set or self.periodic_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.periodic_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dual-stack-delay" or name == "hold-acct-start" or name == "method-list-name" or name == "periodic-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dual-stack-delay"):
                            self.dual_stack_delay = value
                            self.dual_stack_delay.value_namespace = name_space
                            self.dual_stack_delay.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-acct-start"):
                            self.hold_acct_start = value
                            self.hold_acct_start.value_namespace = name_space
                            self.hold_acct_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "method-list-name"):
                            self.method_list_name = value
                            self.method_list_name.value_namespace = name_space
                            self.method_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "periodic-interval"):
                            self.periodic_interval = value
                            self.periodic_interval.value_namespace = name_space
                            self.periodic_interval.value_namespace_prefix = name_space_prefix


                class IdleTimeout(Entity):
                    """
                    Subscriber accounting idle timeout
                    
                    .. attribute:: direction
                    
                    	Idle timeout traffic direction
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Threshold in minute(s) per packet
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: timeout_value
                    
                    	Idle timeout value in seconds
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'subscriber-accounting-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, self).__init__()

                        self.yang_name = "idle-timeout"
                        self.yang_parent_name = "accounting"

                        self.direction = YLeaf(YType.str, "direction")

                        self.threshold = YLeaf(YType.int32, "threshold")

                        self.timeout_value = YLeaf(YType.int32, "timeout-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction",
                                        "threshold",
                                        "timeout_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.direction.is_set or
                            self.threshold.is_set or
                            self.timeout_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set or
                            self.timeout_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "idle-timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())
                        if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction" or name == "threshold" or name == "timeout-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-value"):
                            self.timeout_value = value
                            self.timeout_value.value_namespace = name_space
                            self.timeout_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.prepaid_feature.is_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_data()) or
                        (self.service_accounting is not None and self.service_accounting.has_data()) or
                        (self.session is not None and self.session.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prepaid_feature.yfilter != YFilter.not_set or
                        (self.idle_timeout is not None and self.idle_timeout.has_operation()) or
                        (self.service_accounting is not None and self.service_accounting.has_operation()) or
                        (self.session is not None and self.session.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:accounting" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prepaid_feature.is_set or self.prepaid_feature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prepaid_feature.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "idle-timeout"):
                        if (self.idle_timeout is None):
                            self.idle_timeout = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout()
                            self.idle_timeout.parent = self
                            self._children_name_map["idle_timeout"] = "idle-timeout"
                        return self.idle_timeout

                    if (child_yang_name == "service-accounting"):
                        if (self.service_accounting is None):
                            self.service_accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting()
                            self.service_accounting.parent = self
                            self._children_name_map["service_accounting"] = "service-accounting"
                        return self.service_accounting

                    if (child_yang_name == "session"):
                        if (self.session is None):
                            self.session = DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                        return self.session

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "idle-timeout" or name == "service-accounting" or name == "session" or name == "prepaid-feature"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prepaid-feature"):
                        self.prepaid_feature = value
                        self.prepaid_feature.value_namespace = name_space
                        self.prepaid_feature.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.template_name.is_set or
                    self.vrf.is_set or
                    (self.accounting is not None and self.accounting.has_data()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_data()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_data()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_data()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_data()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_data()) or
                    (self.pbr is not None and self.pbr.has_data()) or
                    (self.qos is not None and self.qos.has_data()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.template_name.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.accounting is not None and self.accounting.has_operation()) or
                    (self.ipv4_network is not None and self.ipv4_network.has_operation()) or
                    (self.ipv4_packet_filter is not None and self.ipv4_packet_filter.has_operation()) or
                    (self.ipv6_neighbor is not None and self.ipv6_neighbor.has_operation()) or
                    (self.ipv6_network is not None and self.ipv6_network.has_operation()) or
                    (self.ipv6_packet_filter is not None and self.ipv6_packet_filter.has_operation()) or
                    (self.pbr is not None and self.pbr.has_operation()) or
                    (self.qos is not None and self.qos.has_operation()) or
                    (self.span_monitor_sessions is not None and self.span_monitor_sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "subscriber-service" + "[template-name='" + self.template_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/subscriber-services/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.template_name.is_set or self.template_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.template_name.get_name_leafdata())
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "accounting"):
                    if (self.accounting is None):
                        self.accounting = DynamicTemplate.SubscriberServices.SubscriberService.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                    return self.accounting

                if (child_yang_name == "ipv4-network"):
                    if (self.ipv4_network is None):
                        self.ipv4_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network()
                        self.ipv4_network.parent = self
                        self._children_name_map["ipv4_network"] = "ipv4-network"
                    return self.ipv4_network

                if (child_yang_name == "ipv4-packet-filter"):
                    if (self.ipv4_packet_filter is None):
                        self.ipv4_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter()
                        self.ipv4_packet_filter.parent = self
                        self._children_name_map["ipv4_packet_filter"] = "ipv4-packet-filter"
                    return self.ipv4_packet_filter

                if (child_yang_name == "ipv6-neighbor"):
                    if (self.ipv6_neighbor is None):
                        self.ipv6_neighbor = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor()
                        self.ipv6_neighbor.parent = self
                        self._children_name_map["ipv6_neighbor"] = "ipv6-neighbor"
                    return self.ipv6_neighbor

                if (child_yang_name == "ipv6-network"):
                    if (self.ipv6_network is None):
                        self.ipv6_network = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network()
                        self.ipv6_network.parent = self
                        self._children_name_map["ipv6_network"] = "ipv6-network"
                    return self.ipv6_network

                if (child_yang_name == "ipv6-packet-filter"):
                    if (self.ipv6_packet_filter is None):
                        self.ipv6_packet_filter = DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter()
                        self.ipv6_packet_filter.parent = self
                        self._children_name_map["ipv6_packet_filter"] = "ipv6-packet-filter"
                    return self.ipv6_packet_filter

                if (child_yang_name == "pbr"):
                    if (self.pbr is None):
                        self.pbr = DynamicTemplate.SubscriberServices.SubscriberService.Pbr()
                        self.pbr.parent = self
                        self._children_name_map["pbr"] = "pbr"
                    return self.pbr

                if (child_yang_name == "qos"):
                    if (self.qos is None):
                        self.qos = DynamicTemplate.SubscriberServices.SubscriberService.Qos()
                        self.qos.parent = self
                        self._children_name_map["qos"] = "qos"
                    return self.qos

                if (child_yang_name == "span-monitor-sessions"):
                    if (self.span_monitor_sessions is None):
                        self.span_monitor_sessions = DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions()
                        self.span_monitor_sessions.parent = self
                        self._children_name_map["span_monitor_sessions"] = "span-monitor-sessions"
                    return self.span_monitor_sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting" or name == "ipv4-network" or name == "ipv4-packet-filter" or name == "ipv6-neighbor" or name == "ipv6-network" or name == "ipv6-packet-filter" or name == "pbr" or name == "qos" or name == "span-monitor-sessions" or name == "template-name" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "template-name"):
                    self.template_name = value
                    self.template_name.value_namespace = name_space
                    self.template_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.subscriber_service:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.subscriber_service:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subscriber-services" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "subscriber-service"):
                for c in self.subscriber_service:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DynamicTemplate.SubscriberServices.SubscriberService()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.subscriber_service.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "subscriber-service"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ip_subscribers is not None and self.ip_subscribers.has_data()) or
            (self.ppps is not None and self.ppps.has_data()) or
            (self.subscriber_services is not None and self.subscriber_services.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ip_subscribers is not None and self.ip_subscribers.has_operation()) or
            (self.ppps is not None and self.ppps.has_operation()) or
            (self.subscriber_services is not None and self.subscriber_services.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg:dynamic-template" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ip-subscribers"):
            if (self.ip_subscribers is None):
                self.ip_subscribers = DynamicTemplate.IpSubscribers()
                self.ip_subscribers.parent = self
                self._children_name_map["ip_subscribers"] = "ip-subscribers"
            return self.ip_subscribers

        if (child_yang_name == "ppps"):
            if (self.ppps is None):
                self.ppps = DynamicTemplate.Ppps()
                self.ppps.parent = self
                self._children_name_map["ppps"] = "ppps"
            return self.ppps

        if (child_yang_name == "subscriber-services"):
            if (self.subscriber_services is None):
                self.subscriber_services = DynamicTemplate.SubscriberServices()
                self.subscriber_services.parent = self
                self._children_name_map["subscriber_services"] = "subscriber-services"
            return self.subscriber_services

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ip-subscribers" or name == "ppps" or name == "subscriber-services"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DynamicTemplate()
        return self._top_entity

