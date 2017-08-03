""" Cisco_IOS_XR_asr9k_netflow_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-netflow package operational data.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NetFlow(Entity):
    """
    NetFlow operational data
    
    .. attribute:: statistics
    
    	Node\-specific NetFlow statistics information
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics>`
    
    

    """

    _prefix = 'asr9k-netflow-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(NetFlow, self).__init__()
        self._top_entity = None

        self.yang_name = "net-flow"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-netflow-oper"

        self.statistics = NetFlow.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")


    class Statistics(Entity):
        """
        Node\-specific NetFlow statistics information
        
        .. attribute:: statistic
        
        	NetFlow statistics information for a particular node
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic>`
        
        

        """

        _prefix = 'asr9k-netflow-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "net-flow"

            self.statistic = YList(self)

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
                        super(NetFlow.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetFlow.Statistics, self).__setattr__(name, value)


        class Statistic(Entity):
            """
            NetFlow statistics information for a particular
            node
            
            .. attribute:: node  <key>
            
            	Node location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: producer
            
            	NetFlow producer statistics
            	**type**\:   :py:class:`Producer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer>`
            
            .. attribute:: server
            
            	NetFlow server statistics
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.Statistics.Statistic, self).__init__()

                self.yang_name = "statistic"
                self.yang_parent_name = "statistics"

                self.node = YLeaf(YType.str, "node")

                self.producer = NetFlow.Statistics.Statistic.Producer()
                self.producer.parent = self
                self._children_name_map["producer"] = "producer"
                self._children_yang_names.add("producer")

                self.server = NetFlow.Statistics.Statistic.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetFlow.Statistics.Statistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetFlow.Statistics.Statistic, self).__setattr__(name, value)


            class Producer(Entity):
                """
                NetFlow producer statistics
                
                .. attribute:: statistics
                
                	Statistics information
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer.Statistics>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.Statistics.Statistic.Producer, self).__init__()

                    self.yang_name = "producer"
                    self.yang_parent_name = "statistic"

                    self.statistics = NetFlow.Statistics.Statistic.Producer.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")


                class Statistics(Entity):
                    """
                    Statistics information
                    
                    .. attribute:: drops_no_space
                    
                    	Drops (no space)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drops_others
                    
                    	Drops (others)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_packet_counts
                    
                    	Number of Rxed Flow Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_egress_flows
                    
                    	IPv4 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_ingress_flows
                    
                    	IPv4 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_egress_flows
                    
                    	IPv6 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_ingress_flows
                    
                    	IPv6 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_cleared
                    
                    	Last time Statistics cleared in 'Mon Jan 1 12\:00 \:00 2xxx' format
                    	**type**\:  str
                    
                    .. attribute:: mpls_egress_flows
                    
                    	MPLS egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: mpls_ingress_flows
                    
                    	MPLS ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: spp_rx_counts
                    
                    	Number of Rxed SPP Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_egress_flows
                    
                    	Unknown egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_ingress_flows
                    
                    	Unknown ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: waiting_servers
                    
                    	Number of waiting servers
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.Statistics.Statistic.Producer.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "producer"

                        self.drops_no_space = YLeaf(YType.uint64, "drops-no-space")

                        self.drops_others = YLeaf(YType.uint64, "drops-others")

                        self.flow_packet_counts = YLeaf(YType.uint64, "flow-packet-counts")

                        self.ipv4_egress_flows = YLeaf(YType.uint64, "ipv4-egress-flows")

                        self.ipv4_ingress_flows = YLeaf(YType.uint64, "ipv4-ingress-flows")

                        self.ipv6_egress_flows = YLeaf(YType.uint64, "ipv6-egress-flows")

                        self.ipv6_ingress_flows = YLeaf(YType.uint64, "ipv6-ingress-flows")

                        self.last_cleared = YLeaf(YType.str, "last-cleared")

                        self.mpls_egress_flows = YLeaf(YType.uint64, "mpls-egress-flows")

                        self.mpls_ingress_flows = YLeaf(YType.uint64, "mpls-ingress-flows")

                        self.spp_rx_counts = YLeaf(YType.uint64, "spp-rx-counts")

                        self.unknown_egress_flows = YLeaf(YType.uint64, "unknown-egress-flows")

                        self.unknown_ingress_flows = YLeaf(YType.uint64, "unknown-ingress-flows")

                        self.waiting_servers = YLeaf(YType.uint64, "waiting-servers")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("drops_no_space",
                                        "drops_others",
                                        "flow_packet_counts",
                                        "ipv4_egress_flows",
                                        "ipv4_ingress_flows",
                                        "ipv6_egress_flows",
                                        "ipv6_ingress_flows",
                                        "last_cleared",
                                        "mpls_egress_flows",
                                        "mpls_ingress_flows",
                                        "spp_rx_counts",
                                        "unknown_egress_flows",
                                        "unknown_ingress_flows",
                                        "waiting_servers") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NetFlow.Statistics.Statistic.Producer.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.Statistics.Statistic.Producer.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.drops_no_space.is_set or
                            self.drops_others.is_set or
                            self.flow_packet_counts.is_set or
                            self.ipv4_egress_flows.is_set or
                            self.ipv4_ingress_flows.is_set or
                            self.ipv6_egress_flows.is_set or
                            self.ipv6_ingress_flows.is_set or
                            self.last_cleared.is_set or
                            self.mpls_egress_flows.is_set or
                            self.mpls_ingress_flows.is_set or
                            self.spp_rx_counts.is_set or
                            self.unknown_egress_flows.is_set or
                            self.unknown_ingress_flows.is_set or
                            self.waiting_servers.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.drops_no_space.yfilter != YFilter.not_set or
                            self.drops_others.yfilter != YFilter.not_set or
                            self.flow_packet_counts.yfilter != YFilter.not_set or
                            self.ipv4_egress_flows.yfilter != YFilter.not_set or
                            self.ipv4_ingress_flows.yfilter != YFilter.not_set or
                            self.ipv6_egress_flows.yfilter != YFilter.not_set or
                            self.ipv6_ingress_flows.yfilter != YFilter.not_set or
                            self.last_cleared.yfilter != YFilter.not_set or
                            self.mpls_egress_flows.yfilter != YFilter.not_set or
                            self.mpls_ingress_flows.yfilter != YFilter.not_set or
                            self.spp_rx_counts.yfilter != YFilter.not_set or
                            self.unknown_egress_flows.yfilter != YFilter.not_set or
                            self.unknown_ingress_flows.yfilter != YFilter.not_set or
                            self.waiting_servers.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.drops_no_space.is_set or self.drops_no_space.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drops_no_space.get_name_leafdata())
                        if (self.drops_others.is_set or self.drops_others.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drops_others.get_name_leafdata())
                        if (self.flow_packet_counts.is_set or self.flow_packet_counts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_packet_counts.get_name_leafdata())
                        if (self.ipv4_egress_flows.is_set or self.ipv4_egress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_egress_flows.get_name_leafdata())
                        if (self.ipv4_ingress_flows.is_set or self.ipv4_ingress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_ingress_flows.get_name_leafdata())
                        if (self.ipv6_egress_flows.is_set or self.ipv6_egress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_egress_flows.get_name_leafdata())
                        if (self.ipv6_ingress_flows.is_set or self.ipv6_ingress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_ingress_flows.get_name_leafdata())
                        if (self.last_cleared.is_set or self.last_cleared.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_cleared.get_name_leafdata())
                        if (self.mpls_egress_flows.is_set or self.mpls_egress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_egress_flows.get_name_leafdata())
                        if (self.mpls_ingress_flows.is_set or self.mpls_ingress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_ingress_flows.get_name_leafdata())
                        if (self.spp_rx_counts.is_set or self.spp_rx_counts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spp_rx_counts.get_name_leafdata())
                        if (self.unknown_egress_flows.is_set or self.unknown_egress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_egress_flows.get_name_leafdata())
                        if (self.unknown_ingress_flows.is_set or self.unknown_ingress_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_ingress_flows.get_name_leafdata())
                        if (self.waiting_servers.is_set or self.waiting_servers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.waiting_servers.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "drops-no-space" or name == "drops-others" or name == "flow-packet-counts" or name == "ipv4-egress-flows" or name == "ipv4-ingress-flows" or name == "ipv6-egress-flows" or name == "ipv6-ingress-flows" or name == "last-cleared" or name == "mpls-egress-flows" or name == "mpls-ingress-flows" or name == "spp-rx-counts" or name == "unknown-egress-flows" or name == "unknown-ingress-flows" or name == "waiting-servers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "drops-no-space"):
                            self.drops_no_space = value
                            self.drops_no_space.value_namespace = name_space
                            self.drops_no_space.value_namespace_prefix = name_space_prefix
                        if(value_path == "drops-others"):
                            self.drops_others = value
                            self.drops_others.value_namespace = name_space
                            self.drops_others.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-packet-counts"):
                            self.flow_packet_counts = value
                            self.flow_packet_counts.value_namespace = name_space
                            self.flow_packet_counts.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-egress-flows"):
                            self.ipv4_egress_flows = value
                            self.ipv4_egress_flows.value_namespace = name_space
                            self.ipv4_egress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-ingress-flows"):
                            self.ipv4_ingress_flows = value
                            self.ipv4_ingress_flows.value_namespace = name_space
                            self.ipv4_ingress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-egress-flows"):
                            self.ipv6_egress_flows = value
                            self.ipv6_egress_flows.value_namespace = name_space
                            self.ipv6_egress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-ingress-flows"):
                            self.ipv6_ingress_flows = value
                            self.ipv6_ingress_flows.value_namespace = name_space
                            self.ipv6_ingress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-cleared"):
                            self.last_cleared = value
                            self.last_cleared.value_namespace = name_space
                            self.last_cleared.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-egress-flows"):
                            self.mpls_egress_flows = value
                            self.mpls_egress_flows.value_namespace = name_space
                            self.mpls_egress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-ingress-flows"):
                            self.mpls_ingress_flows = value
                            self.mpls_ingress_flows.value_namespace = name_space
                            self.mpls_ingress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "spp-rx-counts"):
                            self.spp_rx_counts = value
                            self.spp_rx_counts.value_namespace = name_space
                            self.spp_rx_counts.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-egress-flows"):
                            self.unknown_egress_flows = value
                            self.unknown_egress_flows.value_namespace = name_space
                            self.unknown_egress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-ingress-flows"):
                            self.unknown_ingress_flows = value
                            self.unknown_ingress_flows.value_namespace = name_space
                            self.unknown_ingress_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "waiting-servers"):
                            self.waiting_servers = value
                            self.waiting_servers.value_namespace = name_space
                            self.waiting_servers.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.statistics is not None and self.statistics.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.statistics is not None and self.statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "producer" + path_buffer

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

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = NetFlow.Statistics.Statistic.Producer.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Server(Entity):
                """
                NetFlow server statistics
                
                .. attribute:: flow_exporters
                
                	Flow exporter information
                	**type**\:   :py:class:`FlowExporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.Statistics.Statistic.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "statistic"

                    self.flow_exporters = NetFlow.Statistics.Statistic.Server.FlowExporters()
                    self.flow_exporters.parent = self
                    self._children_name_map["flow_exporters"] = "flow-exporters"
                    self._children_yang_names.add("flow-exporters")


                class FlowExporters(Entity):
                    """
                    Flow exporter information
                    
                    .. attribute:: flow_exporter
                    
                    	Exporter information
                    	**type**\: list of    :py:class:`FlowExporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter>`
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.Statistics.Statistic.Server.FlowExporters, self).__init__()

                        self.yang_name = "flow-exporters"
                        self.yang_parent_name = "server"

                        self.flow_exporter = YList(self)

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
                                    super(NetFlow.Statistics.Statistic.Server.FlowExporters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.Statistics.Statistic.Server.FlowExporters, self).__setattr__(name, value)


                    class FlowExporter(Entity):
                        """
                        Exporter information
                        
                        .. attribute:: exporter_name  <key>
                        
                        	Exporter name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: exporter
                        
                        	Statistics information for the exporter
                        	**type**\:   :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter>`
                        
                        

                        """

                        _prefix = 'asr9k-netflow-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter, self).__init__()

                            self.yang_name = "flow-exporter"
                            self.yang_parent_name = "flow-exporters"

                            self.exporter_name = YLeaf(YType.str, "exporter-name")

                            self.exporter = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter()
                            self.exporter.parent = self
                            self._children_name_map["exporter"] = "exporter"
                            self._children_yang_names.add("exporter")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("exporter_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter, self).__setattr__(name, value)


                        class Exporter(Entity):
                            """
                            Statistics information for the exporter
                            
                            .. attribute:: statistic
                            
                            	Array of flow exporters
                            	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic>`
                            
                            

                            """

                            _prefix = 'asr9k-netflow-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter, self).__init__()

                                self.yang_name = "exporter"
                                self.yang_parent_name = "flow-exporter"

                                self.statistic = YList(self)

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
                                            super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter, self).__setattr__(name, value)


                            class Statistic(Entity):
                                """
                                Array of flow exporters
                                
                                .. attribute:: collector
                                
                                	Statistics of all collectors
                                	**type**\: list of    :py:class:`Collector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector>`
                                
                                .. attribute:: memory_usage
                                
                                	Memory usage
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: name
                                
                                	Exporter name
                                	**type**\:  str
                                
                                .. attribute:: used_by_flow_monitor
                                
                                	List of flow monitors that use the exporter
                                	**type**\:  list of str
                                
                                

                                """

                                _prefix = 'asr9k-netflow-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic, self).__init__()

                                    self.yang_name = "statistic"
                                    self.yang_parent_name = "exporter"

                                    self.memory_usage = YLeaf(YType.uint32, "memory-usage")

                                    self.name = YLeaf(YType.str, "name")

                                    self.used_by_flow_monitor = YLeafList(YType.str, "used-by-flow-monitor")

                                    self.collector = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("memory_usage",
                                                    "name",
                                                    "used_by_flow_monitor") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic, self).__setattr__(name, value)


                                class Collector(Entity):
                                    """
                                    Statistics of all collectors
                                    
                                    .. attribute:: bytes_dropped
                                    
                                    	Bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: bytes_sent
                                    
                                    	Bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: destination_address
                                    
                                    	Destination IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: destination_port
                                    
                                    	Destination port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: exporter_state
                                    
                                    	Exporter state
                                    	**type**\:  str
                                    
                                    .. attribute:: flow_bytes_dropped
                                    
                                    	Flow bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flow_bytes_sent
                                    
                                    	Flow bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flows_dropped
                                    
                                    	Flows dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flows_sent
                                    
                                    	Flows sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_bytes_sent
                                    
                                    	Total bytes exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_hour_flows_sent
                                    
                                    	Total flows exported over the of last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_packest_sent
                                    
                                    	Total packets exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_bytes_sent
                                    
                                    	Total bytes exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_minute_flows_sent
                                    
                                    	Total flows exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_packets
                                    
                                    	Total packets exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_bytes_sent
                                    
                                    	Total bytes exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_second_flows_sent
                                    
                                    	Total flows exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_packets_sent
                                    
                                    	Total packets exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_sent
                                    
                                    	Option data bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_data_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_sent
                                    
                                    	Option data sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_template_bytes_dropped
                                    
                                    	Option template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_template_bytes_sent
                                    
                                    	Option template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_templates_dropped
                                    
                                    	Option templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_templates_sent
                                    
                                    	Option templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_dropped
                                    
                                    	Packets dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_sent
                                    
                                    	Packets sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: souce_port
                                    
                                    	Source port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: source_address
                                    
                                    	Source IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: template_bytes_dropped
                                    
                                    	Template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: template_bytes_sent
                                    
                                    	Template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: templates_dropped
                                    
                                    	Templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: templates_sent
                                    
                                    	Templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transport_protocol
                                    
                                    	Transport protocol
                                    	**type**\:  str
                                    
                                    .. attribute:: vrf_name
                                    
                                    	VRF Name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-netflow-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector, self).__init__()

                                        self.yang_name = "collector"
                                        self.yang_parent_name = "statistic"

                                        self.bytes_dropped = YLeaf(YType.uint64, "bytes-dropped")

                                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                                        self.destination_address = YLeaf(YType.str, "destination-address")

                                        self.destination_port = YLeaf(YType.uint16, "destination-port")

                                        self.exporter_state = YLeaf(YType.str, "exporter-state")

                                        self.flow_bytes_dropped = YLeaf(YType.uint64, "flow-bytes-dropped")

                                        self.flow_bytes_sent = YLeaf(YType.uint64, "flow-bytes-sent")

                                        self.flows_dropped = YLeaf(YType.uint64, "flows-dropped")

                                        self.flows_sent = YLeaf(YType.uint64, "flows-sent")

                                        self.last_hour_bytes_sent = YLeaf(YType.uint64, "last-hour-bytes-sent")

                                        self.last_hour_flows_sent = YLeaf(YType.uint64, "last-hour-flows-sent")

                                        self.last_hour_packest_sent = YLeaf(YType.uint64, "last-hour-packest-sent")

                                        self.last_minute_bytes_sent = YLeaf(YType.uint64, "last-minute-bytes-sent")

                                        self.last_minute_flows_sent = YLeaf(YType.uint64, "last-minute-flows-sent")

                                        self.last_minute_packets = YLeaf(YType.uint64, "last-minute-packets")

                                        self.last_second_bytes_sent = YLeaf(YType.uint64, "last-second-bytes-sent")

                                        self.last_second_flows_sent = YLeaf(YType.uint64, "last-second-flows-sent")

                                        self.last_second_packets_sent = YLeaf(YType.uint64, "last-second-packets-sent")

                                        self.option_data_bytes_dropped = YLeaf(YType.uint64, "option-data-bytes-dropped")

                                        self.option_data_bytes_sent = YLeaf(YType.uint64, "option-data-bytes-sent")

                                        self.option_data_dropped = YLeaf(YType.uint64, "option-data-dropped")

                                        self.option_data_sent = YLeaf(YType.uint64, "option-data-sent")

                                        self.option_template_bytes_dropped = YLeaf(YType.uint64, "option-template-bytes-dropped")

                                        self.option_template_bytes_sent = YLeaf(YType.uint64, "option-template-bytes-sent")

                                        self.option_templates_dropped = YLeaf(YType.uint64, "option-templates-dropped")

                                        self.option_templates_sent = YLeaf(YType.uint64, "option-templates-sent")

                                        self.packets_dropped = YLeaf(YType.uint64, "packets-dropped")

                                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                                        self.souce_port = YLeaf(YType.uint16, "souce-port")

                                        self.source_address = YLeaf(YType.str, "source-address")

                                        self.template_bytes_dropped = YLeaf(YType.uint64, "template-bytes-dropped")

                                        self.template_bytes_sent = YLeaf(YType.uint64, "template-bytes-sent")

                                        self.templates_dropped = YLeaf(YType.uint64, "templates-dropped")

                                        self.templates_sent = YLeaf(YType.uint64, "templates-sent")

                                        self.transport_protocol = YLeaf(YType.str, "transport-protocol")

                                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("bytes_dropped",
                                                        "bytes_sent",
                                                        "destination_address",
                                                        "destination_port",
                                                        "exporter_state",
                                                        "flow_bytes_dropped",
                                                        "flow_bytes_sent",
                                                        "flows_dropped",
                                                        "flows_sent",
                                                        "last_hour_bytes_sent",
                                                        "last_hour_flows_sent",
                                                        "last_hour_packest_sent",
                                                        "last_minute_bytes_sent",
                                                        "last_minute_flows_sent",
                                                        "last_minute_packets",
                                                        "last_second_bytes_sent",
                                                        "last_second_flows_sent",
                                                        "last_second_packets_sent",
                                                        "option_data_bytes_dropped",
                                                        "option_data_bytes_sent",
                                                        "option_data_dropped",
                                                        "option_data_sent",
                                                        "option_template_bytes_dropped",
                                                        "option_template_bytes_sent",
                                                        "option_templates_dropped",
                                                        "option_templates_sent",
                                                        "packets_dropped",
                                                        "packets_sent",
                                                        "souce_port",
                                                        "source_address",
                                                        "template_bytes_dropped",
                                                        "template_bytes_sent",
                                                        "templates_dropped",
                                                        "templates_sent",
                                                        "transport_protocol",
                                                        "vrf_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.bytes_dropped.is_set or
                                            self.bytes_sent.is_set or
                                            self.destination_address.is_set or
                                            self.destination_port.is_set or
                                            self.exporter_state.is_set or
                                            self.flow_bytes_dropped.is_set or
                                            self.flow_bytes_sent.is_set or
                                            self.flows_dropped.is_set or
                                            self.flows_sent.is_set or
                                            self.last_hour_bytes_sent.is_set or
                                            self.last_hour_flows_sent.is_set or
                                            self.last_hour_packest_sent.is_set or
                                            self.last_minute_bytes_sent.is_set or
                                            self.last_minute_flows_sent.is_set or
                                            self.last_minute_packets.is_set or
                                            self.last_second_bytes_sent.is_set or
                                            self.last_second_flows_sent.is_set or
                                            self.last_second_packets_sent.is_set or
                                            self.option_data_bytes_dropped.is_set or
                                            self.option_data_bytes_sent.is_set or
                                            self.option_data_dropped.is_set or
                                            self.option_data_sent.is_set or
                                            self.option_template_bytes_dropped.is_set or
                                            self.option_template_bytes_sent.is_set or
                                            self.option_templates_dropped.is_set or
                                            self.option_templates_sent.is_set or
                                            self.packets_dropped.is_set or
                                            self.packets_sent.is_set or
                                            self.souce_port.is_set or
                                            self.source_address.is_set or
                                            self.template_bytes_dropped.is_set or
                                            self.template_bytes_sent.is_set or
                                            self.templates_dropped.is_set or
                                            self.templates_sent.is_set or
                                            self.transport_protocol.is_set or
                                            self.vrf_name.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.bytes_dropped.yfilter != YFilter.not_set or
                                            self.bytes_sent.yfilter != YFilter.not_set or
                                            self.destination_address.yfilter != YFilter.not_set or
                                            self.destination_port.yfilter != YFilter.not_set or
                                            self.exporter_state.yfilter != YFilter.not_set or
                                            self.flow_bytes_dropped.yfilter != YFilter.not_set or
                                            self.flow_bytes_sent.yfilter != YFilter.not_set or
                                            self.flows_dropped.yfilter != YFilter.not_set or
                                            self.flows_sent.yfilter != YFilter.not_set or
                                            self.last_hour_bytes_sent.yfilter != YFilter.not_set or
                                            self.last_hour_flows_sent.yfilter != YFilter.not_set or
                                            self.last_hour_packest_sent.yfilter != YFilter.not_set or
                                            self.last_minute_bytes_sent.yfilter != YFilter.not_set or
                                            self.last_minute_flows_sent.yfilter != YFilter.not_set or
                                            self.last_minute_packets.yfilter != YFilter.not_set or
                                            self.last_second_bytes_sent.yfilter != YFilter.not_set or
                                            self.last_second_flows_sent.yfilter != YFilter.not_set or
                                            self.last_second_packets_sent.yfilter != YFilter.not_set or
                                            self.option_data_bytes_dropped.yfilter != YFilter.not_set or
                                            self.option_data_bytes_sent.yfilter != YFilter.not_set or
                                            self.option_data_dropped.yfilter != YFilter.not_set or
                                            self.option_data_sent.yfilter != YFilter.not_set or
                                            self.option_template_bytes_dropped.yfilter != YFilter.not_set or
                                            self.option_template_bytes_sent.yfilter != YFilter.not_set or
                                            self.option_templates_dropped.yfilter != YFilter.not_set or
                                            self.option_templates_sent.yfilter != YFilter.not_set or
                                            self.packets_dropped.yfilter != YFilter.not_set or
                                            self.packets_sent.yfilter != YFilter.not_set or
                                            self.souce_port.yfilter != YFilter.not_set or
                                            self.source_address.yfilter != YFilter.not_set or
                                            self.template_bytes_dropped.yfilter != YFilter.not_set or
                                            self.template_bytes_sent.yfilter != YFilter.not_set or
                                            self.templates_dropped.yfilter != YFilter.not_set or
                                            self.templates_sent.yfilter != YFilter.not_set or
                                            self.transport_protocol.yfilter != YFilter.not_set or
                                            self.vrf_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "collector" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.bytes_dropped.is_set or self.bytes_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.bytes_dropped.get_name_leafdata())
                                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                                        if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.destination_port.get_name_leafdata())
                                        if (self.exporter_state.is_set or self.exporter_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.exporter_state.get_name_leafdata())
                                        if (self.flow_bytes_dropped.is_set or self.flow_bytes_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flow_bytes_dropped.get_name_leafdata())
                                        if (self.flow_bytes_sent.is_set or self.flow_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flow_bytes_sent.get_name_leafdata())
                                        if (self.flows_dropped.is_set or self.flows_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flows_dropped.get_name_leafdata())
                                        if (self.flows_sent.is_set or self.flows_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flows_sent.get_name_leafdata())
                                        if (self.last_hour_bytes_sent.is_set or self.last_hour_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_hour_bytes_sent.get_name_leafdata())
                                        if (self.last_hour_flows_sent.is_set or self.last_hour_flows_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_hour_flows_sent.get_name_leafdata())
                                        if (self.last_hour_packest_sent.is_set or self.last_hour_packest_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_hour_packest_sent.get_name_leafdata())
                                        if (self.last_minute_bytes_sent.is_set or self.last_minute_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_minute_bytes_sent.get_name_leafdata())
                                        if (self.last_minute_flows_sent.is_set or self.last_minute_flows_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_minute_flows_sent.get_name_leafdata())
                                        if (self.last_minute_packets.is_set or self.last_minute_packets.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_minute_packets.get_name_leafdata())
                                        if (self.last_second_bytes_sent.is_set or self.last_second_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_second_bytes_sent.get_name_leafdata())
                                        if (self.last_second_flows_sent.is_set or self.last_second_flows_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_second_flows_sent.get_name_leafdata())
                                        if (self.last_second_packets_sent.is_set or self.last_second_packets_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_second_packets_sent.get_name_leafdata())
                                        if (self.option_data_bytes_dropped.is_set or self.option_data_bytes_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_data_bytes_dropped.get_name_leafdata())
                                        if (self.option_data_bytes_sent.is_set or self.option_data_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_data_bytes_sent.get_name_leafdata())
                                        if (self.option_data_dropped.is_set or self.option_data_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_data_dropped.get_name_leafdata())
                                        if (self.option_data_sent.is_set or self.option_data_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_data_sent.get_name_leafdata())
                                        if (self.option_template_bytes_dropped.is_set or self.option_template_bytes_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_template_bytes_dropped.get_name_leafdata())
                                        if (self.option_template_bytes_sent.is_set or self.option_template_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_template_bytes_sent.get_name_leafdata())
                                        if (self.option_templates_dropped.is_set or self.option_templates_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_templates_dropped.get_name_leafdata())
                                        if (self.option_templates_sent.is_set or self.option_templates_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_templates_sent.get_name_leafdata())
                                        if (self.packets_dropped.is_set or self.packets_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.packets_dropped.get_name_leafdata())
                                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                                        if (self.souce_port.is_set or self.souce_port.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.souce_port.get_name_leafdata())
                                        if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.source_address.get_name_leafdata())
                                        if (self.template_bytes_dropped.is_set or self.template_bytes_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.template_bytes_dropped.get_name_leafdata())
                                        if (self.template_bytes_sent.is_set or self.template_bytes_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.template_bytes_sent.get_name_leafdata())
                                        if (self.templates_dropped.is_set or self.templates_dropped.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.templates_dropped.get_name_leafdata())
                                        if (self.templates_sent.is_set or self.templates_sent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.templates_sent.get_name_leafdata())
                                        if (self.transport_protocol.is_set or self.transport_protocol.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transport_protocol.get_name_leafdata())
                                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bytes-dropped" or name == "bytes-sent" or name == "destination-address" or name == "destination-port" or name == "exporter-state" or name == "flow-bytes-dropped" or name == "flow-bytes-sent" or name == "flows-dropped" or name == "flows-sent" or name == "last-hour-bytes-sent" or name == "last-hour-flows-sent" or name == "last-hour-packest-sent" or name == "last-minute-bytes-sent" or name == "last-minute-flows-sent" or name == "last-minute-packets" or name == "last-second-bytes-sent" or name == "last-second-flows-sent" or name == "last-second-packets-sent" or name == "option-data-bytes-dropped" or name == "option-data-bytes-sent" or name == "option-data-dropped" or name == "option-data-sent" or name == "option-template-bytes-dropped" or name == "option-template-bytes-sent" or name == "option-templates-dropped" or name == "option-templates-sent" or name == "packets-dropped" or name == "packets-sent" or name == "souce-port" or name == "source-address" or name == "template-bytes-dropped" or name == "template-bytes-sent" or name == "templates-dropped" or name == "templates-sent" or name == "transport-protocol" or name == "vrf-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "bytes-dropped"):
                                            self.bytes_dropped = value
                                            self.bytes_dropped.value_namespace = name_space
                                            self.bytes_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "bytes-sent"):
                                            self.bytes_sent = value
                                            self.bytes_sent.value_namespace = name_space
                                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "destination-address"):
                                            self.destination_address = value
                                            self.destination_address.value_namespace = name_space
                                            self.destination_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "destination-port"):
                                            self.destination_port = value
                                            self.destination_port.value_namespace = name_space
                                            self.destination_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "exporter-state"):
                                            self.exporter_state = value
                                            self.exporter_state.value_namespace = name_space
                                            self.exporter_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "flow-bytes-dropped"):
                                            self.flow_bytes_dropped = value
                                            self.flow_bytes_dropped.value_namespace = name_space
                                            self.flow_bytes_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "flow-bytes-sent"):
                                            self.flow_bytes_sent = value
                                            self.flow_bytes_sent.value_namespace = name_space
                                            self.flow_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "flows-dropped"):
                                            self.flows_dropped = value
                                            self.flows_dropped.value_namespace = name_space
                                            self.flows_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "flows-sent"):
                                            self.flows_sent = value
                                            self.flows_sent.value_namespace = name_space
                                            self.flows_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-hour-bytes-sent"):
                                            self.last_hour_bytes_sent = value
                                            self.last_hour_bytes_sent.value_namespace = name_space
                                            self.last_hour_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-hour-flows-sent"):
                                            self.last_hour_flows_sent = value
                                            self.last_hour_flows_sent.value_namespace = name_space
                                            self.last_hour_flows_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-hour-packest-sent"):
                                            self.last_hour_packest_sent = value
                                            self.last_hour_packest_sent.value_namespace = name_space
                                            self.last_hour_packest_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-minute-bytes-sent"):
                                            self.last_minute_bytes_sent = value
                                            self.last_minute_bytes_sent.value_namespace = name_space
                                            self.last_minute_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-minute-flows-sent"):
                                            self.last_minute_flows_sent = value
                                            self.last_minute_flows_sent.value_namespace = name_space
                                            self.last_minute_flows_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-minute-packets"):
                                            self.last_minute_packets = value
                                            self.last_minute_packets.value_namespace = name_space
                                            self.last_minute_packets.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-second-bytes-sent"):
                                            self.last_second_bytes_sent = value
                                            self.last_second_bytes_sent.value_namespace = name_space
                                            self.last_second_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-second-flows-sent"):
                                            self.last_second_flows_sent = value
                                            self.last_second_flows_sent.value_namespace = name_space
                                            self.last_second_flows_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-second-packets-sent"):
                                            self.last_second_packets_sent = value
                                            self.last_second_packets_sent.value_namespace = name_space
                                            self.last_second_packets_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-data-bytes-dropped"):
                                            self.option_data_bytes_dropped = value
                                            self.option_data_bytes_dropped.value_namespace = name_space
                                            self.option_data_bytes_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-data-bytes-sent"):
                                            self.option_data_bytes_sent = value
                                            self.option_data_bytes_sent.value_namespace = name_space
                                            self.option_data_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-data-dropped"):
                                            self.option_data_dropped = value
                                            self.option_data_dropped.value_namespace = name_space
                                            self.option_data_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-data-sent"):
                                            self.option_data_sent = value
                                            self.option_data_sent.value_namespace = name_space
                                            self.option_data_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-template-bytes-dropped"):
                                            self.option_template_bytes_dropped = value
                                            self.option_template_bytes_dropped.value_namespace = name_space
                                            self.option_template_bytes_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-template-bytes-sent"):
                                            self.option_template_bytes_sent = value
                                            self.option_template_bytes_sent.value_namespace = name_space
                                            self.option_template_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-templates-dropped"):
                                            self.option_templates_dropped = value
                                            self.option_templates_dropped.value_namespace = name_space
                                            self.option_templates_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-templates-sent"):
                                            self.option_templates_sent = value
                                            self.option_templates_sent.value_namespace = name_space
                                            self.option_templates_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "packets-dropped"):
                                            self.packets_dropped = value
                                            self.packets_dropped.value_namespace = name_space
                                            self.packets_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "packets-sent"):
                                            self.packets_sent = value
                                            self.packets_sent.value_namespace = name_space
                                            self.packets_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "souce-port"):
                                            self.souce_port = value
                                            self.souce_port.value_namespace = name_space
                                            self.souce_port.value_namespace_prefix = name_space_prefix
                                        if(value_path == "source-address"):
                                            self.source_address = value
                                            self.source_address.value_namespace = name_space
                                            self.source_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "template-bytes-dropped"):
                                            self.template_bytes_dropped = value
                                            self.template_bytes_dropped.value_namespace = name_space
                                            self.template_bytes_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "template-bytes-sent"):
                                            self.template_bytes_sent = value
                                            self.template_bytes_sent.value_namespace = name_space
                                            self.template_bytes_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "templates-dropped"):
                                            self.templates_dropped = value
                                            self.templates_dropped.value_namespace = name_space
                                            self.templates_dropped.value_namespace_prefix = name_space_prefix
                                        if(value_path == "templates-sent"):
                                            self.templates_sent = value
                                            self.templates_sent.value_namespace = name_space
                                            self.templates_sent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "transport-protocol"):
                                            self.transport_protocol = value
                                            self.transport_protocol.value_namespace = name_space
                                            self.transport_protocol.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vrf-name"):
                                            self.vrf_name = value
                                            self.vrf_name.value_namespace = name_space
                                            self.vrf_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.collector:
                                        if (c.has_data()):
                                            return True
                                    for leaf in self.used_by_flow_monitor.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.memory_usage.is_set or
                                        self.name.is_set)

                                def has_operation(self):
                                    for c in self.collector:
                                        if (c.has_operation()):
                                            return True
                                    for leaf in self.used_by_flow_monitor.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.memory_usage.yfilter != YFilter.not_set or
                                        self.name.yfilter != YFilter.not_set or
                                        self.used_by_flow_monitor.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "statistic" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.name.get_name_leafdata())

                                    leaf_name_data.extend(self.used_by_flow_monitor.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "collector"):
                                        for c in self.collector:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.collector.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "collector" or name == "memory-usage" or name == "name" or name == "used-by-flow-monitor"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "memory-usage"):
                                        self.memory_usage = value
                                        self.memory_usage.value_namespace = name_space
                                        self.memory_usage.value_namespace_prefix = name_space_prefix
                                    if(value_path == "name"):
                                        self.name = value
                                        self.name.value_namespace = name_space
                                        self.name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "used-by-flow-monitor"):
                                        self.used_by_flow_monitor.append(value)

                            def has_data(self):
                                for c in self.statistic:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.statistic:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "exporter" + path_buffer

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

                                if (child_yang_name == "statistic"):
                                    for c in self.statistic:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.statistic.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "statistic"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.exporter_name.is_set or
                                (self.exporter is not None and self.exporter.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.exporter_name.yfilter != YFilter.not_set or
                                (self.exporter is not None and self.exporter.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow-exporter" + "[exporter-name='" + self.exporter_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.exporter_name.is_set or self.exporter_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.exporter_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "exporter"):
                                if (self.exporter is None):
                                    self.exporter = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter()
                                    self.exporter.parent = self
                                    self._children_name_map["exporter"] = "exporter"
                                return self.exporter

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "exporter" or name == "exporter-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "exporter-name"):
                                self.exporter_name = value
                                self.exporter_name.value_namespace = name_space
                                self.exporter_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.flow_exporter:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.flow_exporter:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flow-exporters" + path_buffer

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

                        if (child_yang_name == "flow-exporter"):
                            for c in self.flow_exporter:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.flow_exporter.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow-exporter"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.flow_exporters is not None and self.flow_exporters.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.flow_exporters is not None and self.flow_exporters.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

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

                    if (child_yang_name == "flow-exporters"):
                        if (self.flow_exporters is None):
                            self.flow_exporters = NetFlow.Statistics.Statistic.Server.FlowExporters()
                            self.flow_exporters.parent = self
                            self._children_name_map["flow_exporters"] = "flow-exporters"
                        return self.flow_exporters

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "flow-exporters"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node.is_set or
                    (self.producer is not None and self.producer.has_data()) or
                    (self.server is not None and self.server.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set or
                    (self.producer is not None and self.producer.has_operation()) or
                    (self.server is not None and self.server.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistic" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-netflow-oper:net-flow/statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "producer"):
                    if (self.producer is None):
                        self.producer = NetFlow.Statistics.Statistic.Producer()
                        self.producer.parent = self
                        self._children_name_map["producer"] = "producer"
                    return self.producer

                if (child_yang_name == "server"):
                    if (self.server is None):
                        self.server = NetFlow.Statistics.Statistic.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                    return self.server

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "producer" or name == "server" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.statistic:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.statistic:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-netflow-oper:net-flow/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "statistic"):
                for c in self.statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetFlow.Statistics.Statistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.statistic.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "statistic"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.statistics is not None and self.statistics.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.statistics is not None and self.statistics.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-netflow-oper:net-flow" + path_buffer

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

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = NetFlow.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "statistics"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NetFlow()
        return self._top_entity

