""" Cisco_IOS_XR_infra_statsd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package operational data.

This module contains definitions
for the following management objects\:
  infra\-statistics\: Statistics Infrastructure

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InfraStatistics(Entity):
    """
    Statistics Infrastructure
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces>`
    
    

    """

    _prefix = 'infra-statsd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(InfraStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-oper"

        self.interfaces = InfraStatistics.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")


    class Interfaces(Entity):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Statistics of an interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-statsd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(InfraStatistics.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "infra-statistics"

            self.interface = YList(self)

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
                        super(InfraStatistics.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InfraStatistics.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Statistics of an interface
            
            .. attribute:: interface_name  <key>
            
            	Name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: cache
            
            	Cached stats data of interfaces
            	**type**\:   :py:class:`Cache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache>`
            
            .. attribute:: data_rate
            
            	Datarate information
            	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.DataRate>`
            
            .. attribute:: generic_counters
            
            	Generic set of interface counters
            	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.GenericCounters>`
            
            .. attribute:: interfaces_mib_counters
            
            	Set of interface counters as displayed by the InterfacesMIB
            	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.InterfacesMibCounters>`
            
            .. attribute:: latest
            
            	Latest stats data of interfaces
            	**type**\:   :py:class:`Latest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest>`
            
            .. attribute:: protocols
            
            	List of protocols
            	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols>`
            
            .. attribute:: total
            
            	Total stats data of interfaces
            	**type**\:   :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total>`
            
            

            """

            _prefix = 'infra-statsd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(InfraStatistics.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.cache = InfraStatistics.Interfaces.Interface.Cache()
                self.cache.parent = self
                self._children_name_map["cache"] = "cache"
                self._children_yang_names.add("cache")

                self.data_rate = InfraStatistics.Interfaces.Interface.DataRate()
                self.data_rate.parent = self
                self._children_name_map["data_rate"] = "data-rate"
                self._children_yang_names.add("data-rate")

                self.generic_counters = InfraStatistics.Interfaces.Interface.GenericCounters()
                self.generic_counters.parent = self
                self._children_name_map["generic_counters"] = "generic-counters"
                self._children_yang_names.add("generic-counters")

                self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.InterfacesMibCounters()
                self.interfaces_mib_counters.parent = self
                self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                self._children_yang_names.add("interfaces-mib-counters")

                self.latest = InfraStatistics.Interfaces.Interface.Latest()
                self.latest.parent = self
                self._children_name_map["latest"] = "latest"
                self._children_yang_names.add("latest")

                self.protocols = InfraStatistics.Interfaces.Interface.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"
                self._children_yang_names.add("protocols")

                self.total = InfraStatistics.Interfaces.Interface.Total()
                self.total.parent = self
                self._children_name_map["total"] = "total"
                self._children_yang_names.add("total")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InfraStatistics.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InfraStatistics.Interfaces.Interface, self).__setattr__(name, value)


            class Cache(Entity):
                """
                Cached stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Cache, self).__init__()

                    self.yang_name = "cache"
                    self.yang_parent_name = "interface"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Cache.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Cache.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Cache.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "cache"

                        self.protocol = YList(self)

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
                                    super(InfraStatistics.Interfaces.Interface.Cache.Protocols, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Cache.Protocols, self).__setattr__(name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("protocol_name",
                                            "bytes_received",
                                            "bytes_sent",
                                            "input_data_rate",
                                            "input_packet_rate",
                                            "last_data_time",
                                            "output_data_rate",
                                            "output_packet_rate",
                                            "packets_received",
                                            "packets_sent",
                                            "protocol") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.protocol_name.is_set or
                                self.bytes_received.is_set or
                                self.bytes_sent.is_set or
                                self.input_data_rate.is_set or
                                self.input_packet_rate.is_set or
                                self.last_data_time.is_set or
                                self.output_data_rate.is_set or
                                self.output_packet_rate.is_set or
                                self.packets_received.is_set or
                                self.packets_sent.is_set or
                                self.protocol.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.protocol_name.yfilter != YFilter.not_set or
                                self.bytes_received.yfilter != YFilter.not_set or
                                self.bytes_sent.yfilter != YFilter.not_set or
                                self.input_data_rate.yfilter != YFilter.not_set or
                                self.input_packet_rate.yfilter != YFilter.not_set or
                                self.last_data_time.yfilter != YFilter.not_set or
                                self.output_data_rate.yfilter != YFilter.not_set or
                                self.output_packet_rate.yfilter != YFilter.not_set or
                                self.packets_received.yfilter != YFilter.not_set or
                                self.packets_sent.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_name.get_name_leafdata())
                            if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_received.get_name_leafdata())
                            if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                            if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                            if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                            if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_data_time.get_name_leafdata())
                            if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                            if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                            if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_received.get_name_leafdata())
                            if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_sent.get_name_leafdata())
                            if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "protocol-name" or name == "bytes-received" or name == "bytes-sent" or name == "input-data-rate" or name == "input-packet-rate" or name == "last-data-time" or name == "output-data-rate" or name == "output-packet-rate" or name == "packets-received" or name == "packets-sent" or name == "protocol"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "protocol-name"):
                                self.protocol_name = value
                                self.protocol_name.value_namespace = name_space
                                self.protocol_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-received"):
                                self.bytes_received = value
                                self.bytes_received.value_namespace = name_space
                                self.bytes_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-sent"):
                                self.bytes_sent = value
                                self.bytes_sent.value_namespace = name_space
                                self.bytes_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-data-rate"):
                                self.input_data_rate = value
                                self.input_data_rate.value_namespace = name_space
                                self.input_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-packet-rate"):
                                self.input_packet_rate = value
                                self.input_packet_rate.value_namespace = name_space
                                self.input_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-data-time"):
                                self.last_data_time = value
                                self.last_data_time.value_namespace = name_space
                                self.last_data_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-data-rate"):
                                self.output_data_rate = value
                                self.output_data_rate.value_namespace = name_space
                                self.output_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-packet-rate"):
                                self.output_packet_rate = value
                                self.output_packet_rate.value_namespace = name_space
                                self.output_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-received"):
                                self.packets_received = value
                                self.packets_received.value_namespace = name_space
                                self.packets_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-sent"):
                                self.packets_sent = value
                                self.packets_sent.value_namespace = name_space
                                self.packets_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol"):
                                self.protocol = value
                                self.protocol.value_namespace = name_space
                                self.protocol.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.protocol:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.protocol:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocols" + path_buffer

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

                        if (child_yang_name == "protocol"):
                            for c in self.protocol:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.protocol.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "cache"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interfaces-mib-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "cache"

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bandwidth",
                                        "input_data_rate",
                                        "input_load",
                                        "input_packet_rate",
                                        "load_interval",
                                        "output_data_rate",
                                        "output_load",
                                        "output_packet_rate",
                                        "peak_input_data_rate",
                                        "peak_input_packet_rate",
                                        "peak_output_data_rate",
                                        "peak_output_packet_rate",
                                        "reliability") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Cache.DataRate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Cache.DataRate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bandwidth.is_set or
                            self.input_data_rate.is_set or
                            self.input_load.is_set or
                            self.input_packet_rate.is_set or
                            self.load_interval.is_set or
                            self.output_data_rate.is_set or
                            self.output_load.is_set or
                            self.output_packet_rate.is_set or
                            self.peak_input_data_rate.is_set or
                            self.peak_input_packet_rate.is_set or
                            self.peak_output_data_rate.is_set or
                            self.peak_output_packet_rate.is_set or
                            self.reliability.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bandwidth.yfilter != YFilter.not_set or
                            self.input_data_rate.yfilter != YFilter.not_set or
                            self.input_load.yfilter != YFilter.not_set or
                            self.input_packet_rate.yfilter != YFilter.not_set or
                            self.load_interval.yfilter != YFilter.not_set or
                            self.output_data_rate.yfilter != YFilter.not_set or
                            self.output_load.yfilter != YFilter.not_set or
                            self.output_packet_rate.yfilter != YFilter.not_set or
                            self.peak_input_data_rate.yfilter != YFilter.not_set or
                            self.peak_input_packet_rate.yfilter != YFilter.not_set or
                            self.peak_output_data_rate.yfilter != YFilter.not_set or
                            self.peak_output_packet_rate.yfilter != YFilter.not_set or
                            self.reliability.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "data-rate" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bandwidth.get_name_leafdata())
                        if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                        if (self.input_load.is_set or self.input_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_load.get_name_leafdata())
                        if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                        if (self.load_interval.is_set or self.load_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.load_interval.get_name_leafdata())
                        if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                        if (self.output_load.is_set or self.output_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_load.get_name_leafdata())
                        if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                        if (self.peak_input_data_rate.is_set or self.peak_input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_data_rate.get_name_leafdata())
                        if (self.peak_input_packet_rate.is_set or self.peak_input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_packet_rate.get_name_leafdata())
                        if (self.peak_output_data_rate.is_set or self.peak_output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_data_rate.get_name_leafdata())
                        if (self.peak_output_packet_rate.is_set or self.peak_output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_packet_rate.get_name_leafdata())
                        if (self.reliability.is_set or self.reliability.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliability.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bandwidth" or name == "input-data-rate" or name == "input-load" or name == "input-packet-rate" or name == "load-interval" or name == "output-data-rate" or name == "output-load" or name == "output-packet-rate" or name == "peak-input-data-rate" or name == "peak-input-packet-rate" or name == "peak-output-data-rate" or name == "peak-output-packet-rate" or name == "reliability"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bandwidth"):
                            self.bandwidth = value
                            self.bandwidth.value_namespace = name_space
                            self.bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-data-rate"):
                            self.input_data_rate = value
                            self.input_data_rate.value_namespace = name_space
                            self.input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-load"):
                            self.input_load = value
                            self.input_load.value_namespace = name_space
                            self.input_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-packet-rate"):
                            self.input_packet_rate = value
                            self.input_packet_rate.value_namespace = name_space
                            self.input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "load-interval"):
                            self.load_interval = value
                            self.load_interval.value_namespace = name_space
                            self.load_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-data-rate"):
                            self.output_data_rate = value
                            self.output_data_rate.value_namespace = name_space
                            self.output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-load"):
                            self.output_load = value
                            self.output_load.value_namespace = name_space
                            self.output_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-packet-rate"):
                            self.output_packet_rate = value
                            self.output_packet_rate.value_namespace = name_space
                            self.output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-data-rate"):
                            self.peak_input_data_rate = value
                            self.peak_input_data_rate.value_namespace = name_space
                            self.peak_input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-packet-rate"):
                            self.peak_input_packet_rate = value
                            self.peak_input_packet_rate.value_namespace = name_space
                            self.peak_input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-data-rate"):
                            self.peak_output_data_rate = value
                            self.peak_output_data_rate.value_namespace = name_space
                            self.peak_output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-packet-rate"):
                            self.peak_output_packet_rate = value
                            self.peak_output_packet_rate.value_namespace = name_space
                            self.peak_output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliability"):
                            self.reliability = value
                            self.reliability.value_namespace = name_space
                            self.reliability.value_namespace_prefix = name_space_prefix


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "cache"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "generic-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.data_rate is not None and self.data_rate.has_data()) or
                        (self.generic_counters is not None and self.generic_counters.has_data()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_data()) or
                        (self.protocols is not None and self.protocols.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.data_rate is not None and self.data_rate.has_operation()) or
                        (self.generic_counters is not None and self.generic_counters.has_operation()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_operation()) or
                        (self.protocols is not None and self.protocols.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cache" + path_buffer

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

                    if (child_yang_name == "data-rate"):
                        if (self.data_rate is None):
                            self.data_rate = InfraStatistics.Interfaces.Interface.Cache.DataRate()
                            self.data_rate.parent = self
                            self._children_name_map["data_rate"] = "data-rate"
                        return self.data_rate

                    if (child_yang_name == "generic-counters"):
                        if (self.generic_counters is None):
                            self.generic_counters = InfraStatistics.Interfaces.Interface.Cache.GenericCounters()
                            self.generic_counters.parent = self
                            self._children_name_map["generic_counters"] = "generic-counters"
                        return self.generic_counters

                    if (child_yang_name == "interfaces-mib-counters"):
                        if (self.interfaces_mib_counters is None):
                            self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters()
                            self.interfaces_mib_counters.parent = self
                            self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                        return self.interfaces_mib_counters

                    if (child_yang_name == "protocols"):
                        if (self.protocols is None):
                            self.protocols = InfraStatistics.Interfaces.Interface.Cache.Protocols()
                            self.protocols.parent = self
                            self._children_name_map["protocols"] = "protocols"
                        return self.protocols

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "data-rate" or name == "generic-counters" or name == "interfaces-mib-counters" or name == "protocols"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Latest(Entity):
                """
                Latest stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Latest, self).__init__()

                    self.yang_name = "latest"
                    self.yang_parent_name = "interface"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Latest.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Latest.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Latest.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "latest"

                        self.protocol = YList(self)

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
                                    super(InfraStatistics.Interfaces.Interface.Latest.Protocols, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Latest.Protocols, self).__setattr__(name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("protocol_name",
                                            "bytes_received",
                                            "bytes_sent",
                                            "input_data_rate",
                                            "input_packet_rate",
                                            "last_data_time",
                                            "output_data_rate",
                                            "output_packet_rate",
                                            "packets_received",
                                            "packets_sent",
                                            "protocol") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.protocol_name.is_set or
                                self.bytes_received.is_set or
                                self.bytes_sent.is_set or
                                self.input_data_rate.is_set or
                                self.input_packet_rate.is_set or
                                self.last_data_time.is_set or
                                self.output_data_rate.is_set or
                                self.output_packet_rate.is_set or
                                self.packets_received.is_set or
                                self.packets_sent.is_set or
                                self.protocol.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.protocol_name.yfilter != YFilter.not_set or
                                self.bytes_received.yfilter != YFilter.not_set or
                                self.bytes_sent.yfilter != YFilter.not_set or
                                self.input_data_rate.yfilter != YFilter.not_set or
                                self.input_packet_rate.yfilter != YFilter.not_set or
                                self.last_data_time.yfilter != YFilter.not_set or
                                self.output_data_rate.yfilter != YFilter.not_set or
                                self.output_packet_rate.yfilter != YFilter.not_set or
                                self.packets_received.yfilter != YFilter.not_set or
                                self.packets_sent.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_name.get_name_leafdata())
                            if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_received.get_name_leafdata())
                            if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                            if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                            if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                            if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_data_time.get_name_leafdata())
                            if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                            if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                            if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_received.get_name_leafdata())
                            if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_sent.get_name_leafdata())
                            if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "protocol-name" or name == "bytes-received" or name == "bytes-sent" or name == "input-data-rate" or name == "input-packet-rate" or name == "last-data-time" or name == "output-data-rate" or name == "output-packet-rate" or name == "packets-received" or name == "packets-sent" or name == "protocol"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "protocol-name"):
                                self.protocol_name = value
                                self.protocol_name.value_namespace = name_space
                                self.protocol_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-received"):
                                self.bytes_received = value
                                self.bytes_received.value_namespace = name_space
                                self.bytes_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-sent"):
                                self.bytes_sent = value
                                self.bytes_sent.value_namespace = name_space
                                self.bytes_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-data-rate"):
                                self.input_data_rate = value
                                self.input_data_rate.value_namespace = name_space
                                self.input_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-packet-rate"):
                                self.input_packet_rate = value
                                self.input_packet_rate.value_namespace = name_space
                                self.input_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-data-time"):
                                self.last_data_time = value
                                self.last_data_time.value_namespace = name_space
                                self.last_data_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-data-rate"):
                                self.output_data_rate = value
                                self.output_data_rate.value_namespace = name_space
                                self.output_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-packet-rate"):
                                self.output_packet_rate = value
                                self.output_packet_rate.value_namespace = name_space
                                self.output_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-received"):
                                self.packets_received = value
                                self.packets_received.value_namespace = name_space
                                self.packets_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-sent"):
                                self.packets_sent = value
                                self.packets_sent.value_namespace = name_space
                                self.packets_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol"):
                                self.protocol = value
                                self.protocol.value_namespace = name_space
                                self.protocol.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.protocol:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.protocol:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocols" + path_buffer

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

                        if (child_yang_name == "protocol"):
                            for c in self.protocol:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.protocol.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "latest"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interfaces-mib-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "latest"

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bandwidth",
                                        "input_data_rate",
                                        "input_load",
                                        "input_packet_rate",
                                        "load_interval",
                                        "output_data_rate",
                                        "output_load",
                                        "output_packet_rate",
                                        "peak_input_data_rate",
                                        "peak_input_packet_rate",
                                        "peak_output_data_rate",
                                        "peak_output_packet_rate",
                                        "reliability") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Latest.DataRate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Latest.DataRate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bandwidth.is_set or
                            self.input_data_rate.is_set or
                            self.input_load.is_set or
                            self.input_packet_rate.is_set or
                            self.load_interval.is_set or
                            self.output_data_rate.is_set or
                            self.output_load.is_set or
                            self.output_packet_rate.is_set or
                            self.peak_input_data_rate.is_set or
                            self.peak_input_packet_rate.is_set or
                            self.peak_output_data_rate.is_set or
                            self.peak_output_packet_rate.is_set or
                            self.reliability.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bandwidth.yfilter != YFilter.not_set or
                            self.input_data_rate.yfilter != YFilter.not_set or
                            self.input_load.yfilter != YFilter.not_set or
                            self.input_packet_rate.yfilter != YFilter.not_set or
                            self.load_interval.yfilter != YFilter.not_set or
                            self.output_data_rate.yfilter != YFilter.not_set or
                            self.output_load.yfilter != YFilter.not_set or
                            self.output_packet_rate.yfilter != YFilter.not_set or
                            self.peak_input_data_rate.yfilter != YFilter.not_set or
                            self.peak_input_packet_rate.yfilter != YFilter.not_set or
                            self.peak_output_data_rate.yfilter != YFilter.not_set or
                            self.peak_output_packet_rate.yfilter != YFilter.not_set or
                            self.reliability.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "data-rate" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bandwidth.get_name_leafdata())
                        if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                        if (self.input_load.is_set or self.input_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_load.get_name_leafdata())
                        if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                        if (self.load_interval.is_set or self.load_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.load_interval.get_name_leafdata())
                        if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                        if (self.output_load.is_set or self.output_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_load.get_name_leafdata())
                        if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                        if (self.peak_input_data_rate.is_set or self.peak_input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_data_rate.get_name_leafdata())
                        if (self.peak_input_packet_rate.is_set or self.peak_input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_packet_rate.get_name_leafdata())
                        if (self.peak_output_data_rate.is_set or self.peak_output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_data_rate.get_name_leafdata())
                        if (self.peak_output_packet_rate.is_set or self.peak_output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_packet_rate.get_name_leafdata())
                        if (self.reliability.is_set or self.reliability.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliability.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bandwidth" or name == "input-data-rate" or name == "input-load" or name == "input-packet-rate" or name == "load-interval" or name == "output-data-rate" or name == "output-load" or name == "output-packet-rate" or name == "peak-input-data-rate" or name == "peak-input-packet-rate" or name == "peak-output-data-rate" or name == "peak-output-packet-rate" or name == "reliability"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bandwidth"):
                            self.bandwidth = value
                            self.bandwidth.value_namespace = name_space
                            self.bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-data-rate"):
                            self.input_data_rate = value
                            self.input_data_rate.value_namespace = name_space
                            self.input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-load"):
                            self.input_load = value
                            self.input_load.value_namespace = name_space
                            self.input_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-packet-rate"):
                            self.input_packet_rate = value
                            self.input_packet_rate.value_namespace = name_space
                            self.input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "load-interval"):
                            self.load_interval = value
                            self.load_interval.value_namespace = name_space
                            self.load_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-data-rate"):
                            self.output_data_rate = value
                            self.output_data_rate.value_namespace = name_space
                            self.output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-load"):
                            self.output_load = value
                            self.output_load.value_namespace = name_space
                            self.output_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-packet-rate"):
                            self.output_packet_rate = value
                            self.output_packet_rate.value_namespace = name_space
                            self.output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-data-rate"):
                            self.peak_input_data_rate = value
                            self.peak_input_data_rate.value_namespace = name_space
                            self.peak_input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-packet-rate"):
                            self.peak_input_packet_rate = value
                            self.peak_input_packet_rate.value_namespace = name_space
                            self.peak_input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-data-rate"):
                            self.peak_output_data_rate = value
                            self.peak_output_data_rate.value_namespace = name_space
                            self.peak_output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-packet-rate"):
                            self.peak_output_packet_rate = value
                            self.peak_output_packet_rate.value_namespace = name_space
                            self.peak_output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliability"):
                            self.reliability = value
                            self.reliability.value_namespace = name_space
                            self.reliability.value_namespace_prefix = name_space_prefix


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "latest"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "generic-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.data_rate is not None and self.data_rate.has_data()) or
                        (self.generic_counters is not None and self.generic_counters.has_data()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_data()) or
                        (self.protocols is not None and self.protocols.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.data_rate is not None and self.data_rate.has_operation()) or
                        (self.generic_counters is not None and self.generic_counters.has_operation()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_operation()) or
                        (self.protocols is not None and self.protocols.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "latest" + path_buffer

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

                    if (child_yang_name == "data-rate"):
                        if (self.data_rate is None):
                            self.data_rate = InfraStatistics.Interfaces.Interface.Latest.DataRate()
                            self.data_rate.parent = self
                            self._children_name_map["data_rate"] = "data-rate"
                        return self.data_rate

                    if (child_yang_name == "generic-counters"):
                        if (self.generic_counters is None):
                            self.generic_counters = InfraStatistics.Interfaces.Interface.Latest.GenericCounters()
                            self.generic_counters.parent = self
                            self._children_name_map["generic_counters"] = "generic-counters"
                        return self.generic_counters

                    if (child_yang_name == "interfaces-mib-counters"):
                        if (self.interfaces_mib_counters is None):
                            self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters()
                            self.interfaces_mib_counters.parent = self
                            self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                        return self.interfaces_mib_counters

                    if (child_yang_name == "protocols"):
                        if (self.protocols is None):
                            self.protocols = InfraStatistics.Interfaces.Interface.Latest.Protocols()
                            self.protocols.parent = self
                            self._children_name_map["protocols"] = "protocols"
                        return self.protocols

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "data-rate" or name == "generic-counters" or name == "interfaces-mib-counters" or name == "protocols"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Total(Entity):
                """
                Total stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Total, self).__init__()

                    self.yang_name = "total"
                    self.yang_parent_name = "interface"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Total.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Total.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Total.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "total"

                        self.protocol = YList(self)

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
                                    super(InfraStatistics.Interfaces.Interface.Total.Protocols, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Total.Protocols, self).__setattr__(name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("protocol_name",
                                            "bytes_received",
                                            "bytes_sent",
                                            "input_data_rate",
                                            "input_packet_rate",
                                            "last_data_time",
                                            "output_data_rate",
                                            "output_packet_rate",
                                            "packets_received",
                                            "packets_sent",
                                            "protocol") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.protocol_name.is_set or
                                self.bytes_received.is_set or
                                self.bytes_sent.is_set or
                                self.input_data_rate.is_set or
                                self.input_packet_rate.is_set or
                                self.last_data_time.is_set or
                                self.output_data_rate.is_set or
                                self.output_packet_rate.is_set or
                                self.packets_received.is_set or
                                self.packets_sent.is_set or
                                self.protocol.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.protocol_name.yfilter != YFilter.not_set or
                                self.bytes_received.yfilter != YFilter.not_set or
                                self.bytes_sent.yfilter != YFilter.not_set or
                                self.input_data_rate.yfilter != YFilter.not_set or
                                self.input_packet_rate.yfilter != YFilter.not_set or
                                self.last_data_time.yfilter != YFilter.not_set or
                                self.output_data_rate.yfilter != YFilter.not_set or
                                self.output_packet_rate.yfilter != YFilter.not_set or
                                self.packets_received.yfilter != YFilter.not_set or
                                self.packets_sent.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_name.get_name_leafdata())
                            if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_received.get_name_leafdata())
                            if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                            if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                            if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                            if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_data_time.get_name_leafdata())
                            if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                            if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                            if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_received.get_name_leafdata())
                            if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_sent.get_name_leafdata())
                            if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "protocol-name" or name == "bytes-received" or name == "bytes-sent" or name == "input-data-rate" or name == "input-packet-rate" or name == "last-data-time" or name == "output-data-rate" or name == "output-packet-rate" or name == "packets-received" or name == "packets-sent" or name == "protocol"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "protocol-name"):
                                self.protocol_name = value
                                self.protocol_name.value_namespace = name_space
                                self.protocol_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-received"):
                                self.bytes_received = value
                                self.bytes_received.value_namespace = name_space
                                self.bytes_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "bytes-sent"):
                                self.bytes_sent = value
                                self.bytes_sent.value_namespace = name_space
                                self.bytes_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-data-rate"):
                                self.input_data_rate = value
                                self.input_data_rate.value_namespace = name_space
                                self.input_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-packet-rate"):
                                self.input_packet_rate = value
                                self.input_packet_rate.value_namespace = name_space
                                self.input_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-data-time"):
                                self.last_data_time = value
                                self.last_data_time.value_namespace = name_space
                                self.last_data_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-data-rate"):
                                self.output_data_rate = value
                                self.output_data_rate.value_namespace = name_space
                                self.output_data_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-packet-rate"):
                                self.output_packet_rate = value
                                self.output_packet_rate.value_namespace = name_space
                                self.output_packet_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-received"):
                                self.packets_received = value
                                self.packets_received.value_namespace = name_space
                                self.packets_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-sent"):
                                self.packets_sent = value
                                self.packets_sent.value_namespace = name_space
                                self.packets_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol"):
                                self.protocol = value
                                self.protocol.value_namespace = name_space
                                self.protocol.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.protocol:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.protocol:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocols" + path_buffer

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

                        if (child_yang_name == "protocol"):
                            for c in self.protocol:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.protocol.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "total"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interfaces-mib-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "total"

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bandwidth",
                                        "input_data_rate",
                                        "input_load",
                                        "input_packet_rate",
                                        "load_interval",
                                        "output_data_rate",
                                        "output_load",
                                        "output_packet_rate",
                                        "peak_input_data_rate",
                                        "peak_input_packet_rate",
                                        "peak_output_data_rate",
                                        "peak_output_packet_rate",
                                        "reliability") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Total.DataRate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Total.DataRate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bandwidth.is_set or
                            self.input_data_rate.is_set or
                            self.input_load.is_set or
                            self.input_packet_rate.is_set or
                            self.load_interval.is_set or
                            self.output_data_rate.is_set or
                            self.output_load.is_set or
                            self.output_packet_rate.is_set or
                            self.peak_input_data_rate.is_set or
                            self.peak_input_packet_rate.is_set or
                            self.peak_output_data_rate.is_set or
                            self.peak_output_packet_rate.is_set or
                            self.reliability.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bandwidth.yfilter != YFilter.not_set or
                            self.input_data_rate.yfilter != YFilter.not_set or
                            self.input_load.yfilter != YFilter.not_set or
                            self.input_packet_rate.yfilter != YFilter.not_set or
                            self.load_interval.yfilter != YFilter.not_set or
                            self.output_data_rate.yfilter != YFilter.not_set or
                            self.output_load.yfilter != YFilter.not_set or
                            self.output_packet_rate.yfilter != YFilter.not_set or
                            self.peak_input_data_rate.yfilter != YFilter.not_set or
                            self.peak_input_packet_rate.yfilter != YFilter.not_set or
                            self.peak_output_data_rate.yfilter != YFilter.not_set or
                            self.peak_output_packet_rate.yfilter != YFilter.not_set or
                            self.reliability.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "data-rate" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bandwidth.get_name_leafdata())
                        if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                        if (self.input_load.is_set or self.input_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_load.get_name_leafdata())
                        if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                        if (self.load_interval.is_set or self.load_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.load_interval.get_name_leafdata())
                        if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                        if (self.output_load.is_set or self.output_load.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_load.get_name_leafdata())
                        if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                        if (self.peak_input_data_rate.is_set or self.peak_input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_data_rate.get_name_leafdata())
                        if (self.peak_input_packet_rate.is_set or self.peak_input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_input_packet_rate.get_name_leafdata())
                        if (self.peak_output_data_rate.is_set or self.peak_output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_data_rate.get_name_leafdata())
                        if (self.peak_output_packet_rate.is_set or self.peak_output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_output_packet_rate.get_name_leafdata())
                        if (self.reliability.is_set or self.reliability.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliability.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bandwidth" or name == "input-data-rate" or name == "input-load" or name == "input-packet-rate" or name == "load-interval" or name == "output-data-rate" or name == "output-load" or name == "output-packet-rate" or name == "peak-input-data-rate" or name == "peak-input-packet-rate" or name == "peak-output-data-rate" or name == "peak-output-packet-rate" or name == "reliability"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bandwidth"):
                            self.bandwidth = value
                            self.bandwidth.value_namespace = name_space
                            self.bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-data-rate"):
                            self.input_data_rate = value
                            self.input_data_rate.value_namespace = name_space
                            self.input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-load"):
                            self.input_load = value
                            self.input_load.value_namespace = name_space
                            self.input_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-packet-rate"):
                            self.input_packet_rate = value
                            self.input_packet_rate.value_namespace = name_space
                            self.input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "load-interval"):
                            self.load_interval = value
                            self.load_interval.value_namespace = name_space
                            self.load_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-data-rate"):
                            self.output_data_rate = value
                            self.output_data_rate.value_namespace = name_space
                            self.output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-load"):
                            self.output_load = value
                            self.output_load.value_namespace = name_space
                            self.output_load.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-packet-rate"):
                            self.output_packet_rate = value
                            self.output_packet_rate.value_namespace = name_space
                            self.output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-data-rate"):
                            self.peak_input_data_rate = value
                            self.peak_input_data_rate.value_namespace = name_space
                            self.peak_input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-input-packet-rate"):
                            self.peak_input_packet_rate = value
                            self.peak_input_packet_rate.value_namespace = name_space
                            self.peak_input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-data-rate"):
                            self.peak_output_data_rate = value
                            self.peak_output_data_rate.value_namespace = name_space
                            self.peak_output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-output-packet-rate"):
                            self.peak_output_packet_rate = value
                            self.peak_output_packet_rate.value_namespace = name_space
                            self.peak_output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliability"):
                            self.reliability = value
                            self.reliability.value_namespace = name_space
                            self.reliability.value_namespace_prefix = name_space_prefix


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "total"

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("applique",
                                        "availability_flag",
                                        "broadcast_packets_received",
                                        "broadcast_packets_sent",
                                        "bytes_received",
                                        "bytes_sent",
                                        "carrier_transitions",
                                        "crc_errors",
                                        "framing_errors_received",
                                        "giant_packets_received",
                                        "input_aborts",
                                        "input_drops",
                                        "input_errors",
                                        "input_ignored_packets",
                                        "input_overruns",
                                        "input_queue_drops",
                                        "last_data_time",
                                        "last_discontinuity_time",
                                        "multicast_packets_received",
                                        "multicast_packets_sent",
                                        "output_buffer_failures",
                                        "output_buffers_swapped_out",
                                        "output_drops",
                                        "output_errors",
                                        "output_queue_drops",
                                        "output_underruns",
                                        "packets_received",
                                        "packets_sent",
                                        "parity_packets_received",
                                        "resets",
                                        "runt_packets_received",
                                        "seconds_since_last_clear_counters",
                                        "seconds_since_packet_received",
                                        "seconds_since_packet_sent",
                                        "throttled_packets_received",
                                        "unknown_protocol_packets_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Total.GenericCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Total.GenericCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.applique.is_set or
                            self.availability_flag.is_set or
                            self.broadcast_packets_received.is_set or
                            self.broadcast_packets_sent.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.carrier_transitions.is_set or
                            self.crc_errors.is_set or
                            self.framing_errors_received.is_set or
                            self.giant_packets_received.is_set or
                            self.input_aborts.is_set or
                            self.input_drops.is_set or
                            self.input_errors.is_set or
                            self.input_ignored_packets.is_set or
                            self.input_overruns.is_set or
                            self.input_queue_drops.is_set or
                            self.last_data_time.is_set or
                            self.last_discontinuity_time.is_set or
                            self.multicast_packets_received.is_set or
                            self.multicast_packets_sent.is_set or
                            self.output_buffer_failures.is_set or
                            self.output_buffers_swapped_out.is_set or
                            self.output_drops.is_set or
                            self.output_errors.is_set or
                            self.output_queue_drops.is_set or
                            self.output_underruns.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.parity_packets_received.is_set or
                            self.resets.is_set or
                            self.runt_packets_received.is_set or
                            self.seconds_since_last_clear_counters.is_set or
                            self.seconds_since_packet_received.is_set or
                            self.seconds_since_packet_sent.is_set or
                            self.throttled_packets_received.is_set or
                            self.unknown_protocol_packets_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.applique.yfilter != YFilter.not_set or
                            self.availability_flag.yfilter != YFilter.not_set or
                            self.broadcast_packets_received.yfilter != YFilter.not_set or
                            self.broadcast_packets_sent.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.carrier_transitions.yfilter != YFilter.not_set or
                            self.crc_errors.yfilter != YFilter.not_set or
                            self.framing_errors_received.yfilter != YFilter.not_set or
                            self.giant_packets_received.yfilter != YFilter.not_set or
                            self.input_aborts.yfilter != YFilter.not_set or
                            self.input_drops.yfilter != YFilter.not_set or
                            self.input_errors.yfilter != YFilter.not_set or
                            self.input_ignored_packets.yfilter != YFilter.not_set or
                            self.input_overruns.yfilter != YFilter.not_set or
                            self.input_queue_drops.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.last_discontinuity_time.yfilter != YFilter.not_set or
                            self.multicast_packets_received.yfilter != YFilter.not_set or
                            self.multicast_packets_sent.yfilter != YFilter.not_set or
                            self.output_buffer_failures.yfilter != YFilter.not_set or
                            self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                            self.output_drops.yfilter != YFilter.not_set or
                            self.output_errors.yfilter != YFilter.not_set or
                            self.output_queue_drops.yfilter != YFilter.not_set or
                            self.output_underruns.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.parity_packets_received.yfilter != YFilter.not_set or
                            self.resets.yfilter != YFilter.not_set or
                            self.runt_packets_received.yfilter != YFilter.not_set or
                            self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                            self.seconds_since_packet_received.yfilter != YFilter.not_set or
                            self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                            self.throttled_packets_received.yfilter != YFilter.not_set or
                            self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "generic-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.applique.get_name_leafdata())
                        if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.availability_flag.get_name_leafdata())
                        if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                        if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                        if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.crc_errors.get_name_leafdata())
                        if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                        if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                        if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_aborts.get_name_leafdata())
                        if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_drops.get_name_leafdata())
                        if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_errors.get_name_leafdata())
                        if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                        if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_overruns.get_name_leafdata())
                        if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                        if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                        if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                        if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                        if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                        if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_drops.get_name_leafdata())
                        if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_errors.get_name_leafdata())
                        if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                        if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_underruns.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                        if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resets.get_name_leafdata())
                        if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                        if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                        if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                        if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                        if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                        if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "applique"):
                            self.applique = value
                            self.applique.value_namespace = name_space
                            self.applique.value_namespace_prefix = name_space_prefix
                        if(value_path == "availability-flag"):
                            self.availability_flag = value
                            self.availability_flag.value_namespace = name_space
                            self.availability_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-received"):
                            self.broadcast_packets_received = value
                            self.broadcast_packets_received.value_namespace = name_space
                            self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "broadcast-packets-sent"):
                            self.broadcast_packets_sent = value
                            self.broadcast_packets_sent.value_namespace = name_space
                            self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "carrier-transitions"):
                            self.carrier_transitions = value
                            self.carrier_transitions.value_namespace = name_space
                            self.carrier_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "crc-errors"):
                            self.crc_errors = value
                            self.crc_errors.value_namespace = name_space
                            self.crc_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "framing-errors-received"):
                            self.framing_errors_received = value
                            self.framing_errors_received.value_namespace = name_space
                            self.framing_errors_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "giant-packets-received"):
                            self.giant_packets_received = value
                            self.giant_packets_received.value_namespace = name_space
                            self.giant_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-aborts"):
                            self.input_aborts = value
                            self.input_aborts.value_namespace = name_space
                            self.input_aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-drops"):
                            self.input_drops = value
                            self.input_drops.value_namespace = name_space
                            self.input_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-errors"):
                            self.input_errors = value
                            self.input_errors.value_namespace = name_space
                            self.input_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-ignored-packets"):
                            self.input_ignored_packets = value
                            self.input_ignored_packets.value_namespace = name_space
                            self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-overruns"):
                            self.input_overruns = value
                            self.input_overruns.value_namespace = name_space
                            self.input_overruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue-drops"):
                            self.input_queue_drops = value
                            self.input_queue_drops.value_namespace = name_space
                            self.input_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-discontinuity-time"):
                            self.last_discontinuity_time = value
                            self.last_discontinuity_time.value_namespace = name_space
                            self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-received"):
                            self.multicast_packets_received = value
                            self.multicast_packets_received.value_namespace = name_space
                            self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-packets-sent"):
                            self.multicast_packets_sent = value
                            self.multicast_packets_sent.value_namespace = name_space
                            self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffer-failures"):
                            self.output_buffer_failures = value
                            self.output_buffer_failures.value_namespace = name_space
                            self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-buffers-swapped-out"):
                            self.output_buffers_swapped_out = value
                            self.output_buffers_swapped_out.value_namespace = name_space
                            self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-drops"):
                            self.output_drops = value
                            self.output_drops.value_namespace = name_space
                            self.output_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-errors"):
                            self.output_errors = value
                            self.output_errors.value_namespace = name_space
                            self.output_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue-drops"):
                            self.output_queue_drops = value
                            self.output_queue_drops.value_namespace = name_space
                            self.output_queue_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-underruns"):
                            self.output_underruns = value
                            self.output_underruns.value_namespace = name_space
                            self.output_underruns.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "parity-packets-received"):
                            self.parity_packets_received = value
                            self.parity_packets_received.value_namespace = name_space
                            self.parity_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resets"):
                            self.resets = value
                            self.resets.value_namespace = name_space
                            self.resets.value_namespace_prefix = name_space_prefix
                        if(value_path == "runt-packets-received"):
                            self.runt_packets_received = value
                            self.runt_packets_received.value_namespace = name_space
                            self.runt_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-last-clear-counters"):
                            self.seconds_since_last_clear_counters = value
                            self.seconds_since_last_clear_counters.value_namespace = name_space
                            self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-received"):
                            self.seconds_since_packet_received = value
                            self.seconds_since_packet_received.value_namespace = name_space
                            self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-since-packet-sent"):
                            self.seconds_since_packet_sent = value
                            self.seconds_since_packet_sent.value_namespace = name_space
                            self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttled-packets-received"):
                            self.throttled_packets_received = value
                            self.throttled_packets_received.value_namespace = name_space
                            self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-protocol-packets-received"):
                            self.unknown_protocol_packets_received = value
                            self.unknown_protocol_packets_received.value_namespace = name_space
                            self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.data_rate is not None and self.data_rate.has_data()) or
                        (self.generic_counters is not None and self.generic_counters.has_data()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_data()) or
                        (self.protocols is not None and self.protocols.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.data_rate is not None and self.data_rate.has_operation()) or
                        (self.generic_counters is not None and self.generic_counters.has_operation()) or
                        (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_operation()) or
                        (self.protocols is not None and self.protocols.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "total" + path_buffer

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

                    if (child_yang_name == "data-rate"):
                        if (self.data_rate is None):
                            self.data_rate = InfraStatistics.Interfaces.Interface.Total.DataRate()
                            self.data_rate.parent = self
                            self._children_name_map["data_rate"] = "data-rate"
                        return self.data_rate

                    if (child_yang_name == "generic-counters"):
                        if (self.generic_counters is None):
                            self.generic_counters = InfraStatistics.Interfaces.Interface.Total.GenericCounters()
                            self.generic_counters.parent = self
                            self._children_name_map["generic_counters"] = "generic-counters"
                        return self.generic_counters

                    if (child_yang_name == "interfaces-mib-counters"):
                        if (self.interfaces_mib_counters is None):
                            self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters()
                            self.interfaces_mib_counters.parent = self
                            self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                        return self.interfaces_mib_counters

                    if (child_yang_name == "protocols"):
                        if (self.protocols is None):
                            self.protocols = InfraStatistics.Interfaces.Interface.Total.Protocols()
                            self.protocols.parent = self
                            self._children_name_map["protocols"] = "protocols"
                        return self.protocols

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "data-rate" or name == "generic-counters" or name == "interfaces-mib-counters" or name == "protocols"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Protocols(Entity):
                """
                List of protocols
                
                .. attribute:: protocol
                
                	Interface counters per protocol
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols.Protocol>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Protocols, self).__init__()

                    self.yang_name = "protocols"
                    self.yang_parent_name = "interface"

                    self.protocol = YList(self)

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
                                super(InfraStatistics.Interfaces.Interface.Protocols, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InfraStatistics.Interfaces.Interface.Protocols, self).__setattr__(name, value)


                class Protocol(Entity):
                    """
                    Interface counters per protocol
                    
                    .. attribute:: protocol_name  <key>
                    
                    	Name of the protocol
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: protocol
                    
                    	Protocol number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Protocols.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "protocols"

                        self.protocol_name = YLeaf(YType.str, "protocol-name")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.protocol = YLeaf(YType.uint32, "protocol")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("protocol_name",
                                        "bytes_received",
                                        "bytes_sent",
                                        "input_data_rate",
                                        "input_packet_rate",
                                        "last_data_time",
                                        "output_data_rate",
                                        "output_packet_rate",
                                        "packets_received",
                                        "packets_sent",
                                        "protocol") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InfraStatistics.Interfaces.Interface.Protocols.Protocol, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InfraStatistics.Interfaces.Interface.Protocols.Protocol, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.protocol_name.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.input_data_rate.is_set or
                            self.input_packet_rate.is_set or
                            self.last_data_time.is_set or
                            self.output_data_rate.is_set or
                            self.output_packet_rate.is_set or
                            self.packets_received.is_set or
                            self.packets_sent.is_set or
                            self.protocol.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.protocol_name.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.input_data_rate.yfilter != YFilter.not_set or
                            self.input_packet_rate.yfilter != YFilter.not_set or
                            self.last_data_time.yfilter != YFilter.not_set or
                            self.output_data_rate.yfilter != YFilter.not_set or
                            self.output_packet_rate.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.protocol.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocol" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_name.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                        if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                        if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_data_time.get_name_leafdata())
                        if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                        if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol-name" or name == "bytes-received" or name == "bytes-sent" or name == "input-data-rate" or name == "input-packet-rate" or name == "last-data-time" or name == "output-data-rate" or name == "output-packet-rate" or name == "packets-received" or name == "packets-sent" or name == "protocol"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "protocol-name"):
                            self.protocol_name = value
                            self.protocol_name.value_namespace = name_space
                            self.protocol_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-data-rate"):
                            self.input_data_rate = value
                            self.input_data_rate.value_namespace = name_space
                            self.input_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-packet-rate"):
                            self.input_packet_rate = value
                            self.input_packet_rate.value_namespace = name_space
                            self.input_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-data-time"):
                            self.last_data_time = value
                            self.last_data_time.value_namespace = name_space
                            self.last_data_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-data-rate"):
                            self.output_data_rate = value
                            self.output_data_rate.value_namespace = name_space
                            self.output_data_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-packet-rate"):
                            self.output_packet_rate = value
                            self.output_packet_rate.value_namespace = name_space
                            self.output_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol"):
                            self.protocol = value
                            self.protocol.value_namespace = name_space
                            self.protocol.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.protocol:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.protocol:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protocols" + path_buffer

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

                    if (child_yang_name == "protocol"):
                        for c in self.protocol:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = InfraStatistics.Interfaces.Interface.Protocols.Protocol()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.protocol.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InterfacesMibCounters(Entity):
                """
                Set of interface counters as displayed by the
                InterfacesMIB
                
                .. attribute:: applique
                
                	Applique
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, self).__init__()

                    self.yang_name = "interfaces-mib-counters"
                    self.yang_parent_name = "interface"

                    self.applique = YLeaf(YType.uint32, "applique")

                    self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                    self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                    self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                    self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                    self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                    self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                    self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                    self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                    self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                    self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                    self.input_drops = YLeaf(YType.uint32, "input-drops")

                    self.input_errors = YLeaf(YType.uint32, "input-errors")

                    self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                    self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                    self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                    self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                    self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                    self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                    self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                    self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                    self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                    self.output_drops = YLeaf(YType.uint32, "output-drops")

                    self.output_errors = YLeaf(YType.uint32, "output-errors")

                    self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                    self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                    self.packets_received = YLeaf(YType.uint64, "packets-received")

                    self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                    self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                    self.resets = YLeaf(YType.uint32, "resets")

                    self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                    self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                    self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                    self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                    self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                    self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("applique",
                                    "availability_flag",
                                    "broadcast_packets_received",
                                    "broadcast_packets_sent",
                                    "bytes_received",
                                    "bytes_sent",
                                    "carrier_transitions",
                                    "crc_errors",
                                    "framing_errors_received",
                                    "giant_packets_received",
                                    "input_aborts",
                                    "input_drops",
                                    "input_errors",
                                    "input_ignored_packets",
                                    "input_overruns",
                                    "input_queue_drops",
                                    "last_data_time",
                                    "last_discontinuity_time",
                                    "multicast_packets_received",
                                    "multicast_packets_sent",
                                    "output_buffer_failures",
                                    "output_buffers_swapped_out",
                                    "output_drops",
                                    "output_errors",
                                    "output_queue_drops",
                                    "output_underruns",
                                    "packets_received",
                                    "packets_sent",
                                    "parity_packets_received",
                                    "resets",
                                    "runt_packets_received",
                                    "seconds_since_last_clear_counters",
                                    "seconds_since_packet_received",
                                    "seconds_since_packet_sent",
                                    "throttled_packets_received",
                                    "unknown_protocol_packets_received") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.applique.is_set or
                        self.availability_flag.is_set or
                        self.broadcast_packets_received.is_set or
                        self.broadcast_packets_sent.is_set or
                        self.bytes_received.is_set or
                        self.bytes_sent.is_set or
                        self.carrier_transitions.is_set or
                        self.crc_errors.is_set or
                        self.framing_errors_received.is_set or
                        self.giant_packets_received.is_set or
                        self.input_aborts.is_set or
                        self.input_drops.is_set or
                        self.input_errors.is_set or
                        self.input_ignored_packets.is_set or
                        self.input_overruns.is_set or
                        self.input_queue_drops.is_set or
                        self.last_data_time.is_set or
                        self.last_discontinuity_time.is_set or
                        self.multicast_packets_received.is_set or
                        self.multicast_packets_sent.is_set or
                        self.output_buffer_failures.is_set or
                        self.output_buffers_swapped_out.is_set or
                        self.output_drops.is_set or
                        self.output_errors.is_set or
                        self.output_queue_drops.is_set or
                        self.output_underruns.is_set or
                        self.packets_received.is_set or
                        self.packets_sent.is_set or
                        self.parity_packets_received.is_set or
                        self.resets.is_set or
                        self.runt_packets_received.is_set or
                        self.seconds_since_last_clear_counters.is_set or
                        self.seconds_since_packet_received.is_set or
                        self.seconds_since_packet_sent.is_set or
                        self.throttled_packets_received.is_set or
                        self.unknown_protocol_packets_received.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.applique.yfilter != YFilter.not_set or
                        self.availability_flag.yfilter != YFilter.not_set or
                        self.broadcast_packets_received.yfilter != YFilter.not_set or
                        self.broadcast_packets_sent.yfilter != YFilter.not_set or
                        self.bytes_received.yfilter != YFilter.not_set or
                        self.bytes_sent.yfilter != YFilter.not_set or
                        self.carrier_transitions.yfilter != YFilter.not_set or
                        self.crc_errors.yfilter != YFilter.not_set or
                        self.framing_errors_received.yfilter != YFilter.not_set or
                        self.giant_packets_received.yfilter != YFilter.not_set or
                        self.input_aborts.yfilter != YFilter.not_set or
                        self.input_drops.yfilter != YFilter.not_set or
                        self.input_errors.yfilter != YFilter.not_set or
                        self.input_ignored_packets.yfilter != YFilter.not_set or
                        self.input_overruns.yfilter != YFilter.not_set or
                        self.input_queue_drops.yfilter != YFilter.not_set or
                        self.last_data_time.yfilter != YFilter.not_set or
                        self.last_discontinuity_time.yfilter != YFilter.not_set or
                        self.multicast_packets_received.yfilter != YFilter.not_set or
                        self.multicast_packets_sent.yfilter != YFilter.not_set or
                        self.output_buffer_failures.yfilter != YFilter.not_set or
                        self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                        self.output_drops.yfilter != YFilter.not_set or
                        self.output_errors.yfilter != YFilter.not_set or
                        self.output_queue_drops.yfilter != YFilter.not_set or
                        self.output_underruns.yfilter != YFilter.not_set or
                        self.packets_received.yfilter != YFilter.not_set or
                        self.packets_sent.yfilter != YFilter.not_set or
                        self.parity_packets_received.yfilter != YFilter.not_set or
                        self.resets.yfilter != YFilter.not_set or
                        self.runt_packets_received.yfilter != YFilter.not_set or
                        self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                        self.seconds_since_packet_received.yfilter != YFilter.not_set or
                        self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                        self.throttled_packets_received.yfilter != YFilter.not_set or
                        self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces-mib-counters" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.applique.get_name_leafdata())
                    if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.availability_flag.get_name_leafdata())
                    if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                    if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                    if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_received.get_name_leafdata())
                    if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                    if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                    if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.crc_errors.get_name_leafdata())
                    if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                    if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                    if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_aborts.get_name_leafdata())
                    if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_drops.get_name_leafdata())
                    if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_errors.get_name_leafdata())
                    if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                    if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_overruns.get_name_leafdata())
                    if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                    if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_data_time.get_name_leafdata())
                    if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                    if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                    if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                    if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                    if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                    if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_drops.get_name_leafdata())
                    if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_errors.get_name_leafdata())
                    if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                    if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_underruns.get_name_leafdata())
                    if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_received.get_name_leafdata())
                    if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_sent.get_name_leafdata())
                    if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                    if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resets.get_name_leafdata())
                    if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                    if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                    if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                    if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                    if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                    if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "applique"):
                        self.applique = value
                        self.applique.value_namespace = name_space
                        self.applique.value_namespace_prefix = name_space_prefix
                    if(value_path == "availability-flag"):
                        self.availability_flag = value
                        self.availability_flag.value_namespace = name_space
                        self.availability_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast-packets-received"):
                        self.broadcast_packets_received = value
                        self.broadcast_packets_received.value_namespace = name_space
                        self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast-packets-sent"):
                        self.broadcast_packets_sent = value
                        self.broadcast_packets_sent.value_namespace = name_space
                        self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-received"):
                        self.bytes_received = value
                        self.bytes_received.value_namespace = name_space
                        self.bytes_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-sent"):
                        self.bytes_sent = value
                        self.bytes_sent.value_namespace = name_space
                        self.bytes_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "carrier-transitions"):
                        self.carrier_transitions = value
                        self.carrier_transitions.value_namespace = name_space
                        self.carrier_transitions.value_namespace_prefix = name_space_prefix
                    if(value_path == "crc-errors"):
                        self.crc_errors = value
                        self.crc_errors.value_namespace = name_space
                        self.crc_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "framing-errors-received"):
                        self.framing_errors_received = value
                        self.framing_errors_received.value_namespace = name_space
                        self.framing_errors_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "giant-packets-received"):
                        self.giant_packets_received = value
                        self.giant_packets_received.value_namespace = name_space
                        self.giant_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-aborts"):
                        self.input_aborts = value
                        self.input_aborts.value_namespace = name_space
                        self.input_aborts.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-drops"):
                        self.input_drops = value
                        self.input_drops.value_namespace = name_space
                        self.input_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-errors"):
                        self.input_errors = value
                        self.input_errors.value_namespace = name_space
                        self.input_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-ignored-packets"):
                        self.input_ignored_packets = value
                        self.input_ignored_packets.value_namespace = name_space
                        self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-overruns"):
                        self.input_overruns = value
                        self.input_overruns.value_namespace = name_space
                        self.input_overruns.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-queue-drops"):
                        self.input_queue_drops = value
                        self.input_queue_drops.value_namespace = name_space
                        self.input_queue_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-data-time"):
                        self.last_data_time = value
                        self.last_data_time.value_namespace = name_space
                        self.last_data_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-discontinuity-time"):
                        self.last_discontinuity_time = value
                        self.last_discontinuity_time.value_namespace = name_space
                        self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-packets-received"):
                        self.multicast_packets_received = value
                        self.multicast_packets_received.value_namespace = name_space
                        self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-packets-sent"):
                        self.multicast_packets_sent = value
                        self.multicast_packets_sent.value_namespace = name_space
                        self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-buffer-failures"):
                        self.output_buffer_failures = value
                        self.output_buffer_failures.value_namespace = name_space
                        self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-buffers-swapped-out"):
                        self.output_buffers_swapped_out = value
                        self.output_buffers_swapped_out.value_namespace = name_space
                        self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-drops"):
                        self.output_drops = value
                        self.output_drops.value_namespace = name_space
                        self.output_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-errors"):
                        self.output_errors = value
                        self.output_errors.value_namespace = name_space
                        self.output_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-queue-drops"):
                        self.output_queue_drops = value
                        self.output_queue_drops.value_namespace = name_space
                        self.output_queue_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-underruns"):
                        self.output_underruns = value
                        self.output_underruns.value_namespace = name_space
                        self.output_underruns.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-received"):
                        self.packets_received = value
                        self.packets_received.value_namespace = name_space
                        self.packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-sent"):
                        self.packets_sent = value
                        self.packets_sent.value_namespace = name_space
                        self.packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "parity-packets-received"):
                        self.parity_packets_received = value
                        self.parity_packets_received.value_namespace = name_space
                        self.parity_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "resets"):
                        self.resets = value
                        self.resets.value_namespace = name_space
                        self.resets.value_namespace_prefix = name_space_prefix
                    if(value_path == "runt-packets-received"):
                        self.runt_packets_received = value
                        self.runt_packets_received.value_namespace = name_space
                        self.runt_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-last-clear-counters"):
                        self.seconds_since_last_clear_counters = value
                        self.seconds_since_last_clear_counters.value_namespace = name_space
                        self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-packet-received"):
                        self.seconds_since_packet_received = value
                        self.seconds_since_packet_received.value_namespace = name_space
                        self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-packet-sent"):
                        self.seconds_since_packet_sent = value
                        self.seconds_since_packet_sent.value_namespace = name_space
                        self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-packets-received"):
                        self.throttled_packets_received = value
                        self.throttled_packets_received.value_namespace = name_space
                        self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-protocol-packets-received"):
                        self.unknown_protocol_packets_received = value
                        self.unknown_protocol_packets_received.value_namespace = name_space
                        self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix


            class DataRate(Entity):
                """
                Datarate information
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: kbit/s
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.DataRate, self).__init__()

                    self.yang_name = "data-rate"
                    self.yang_parent_name = "interface"

                    self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                    self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                    self.input_load = YLeaf(YType.uint8, "input-load")

                    self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                    self.load_interval = YLeaf(YType.uint32, "load-interval")

                    self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                    self.output_load = YLeaf(YType.uint8, "output-load")

                    self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                    self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                    self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                    self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                    self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                    self.reliability = YLeaf(YType.uint8, "reliability")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bandwidth",
                                    "input_data_rate",
                                    "input_load",
                                    "input_packet_rate",
                                    "load_interval",
                                    "output_data_rate",
                                    "output_load",
                                    "output_packet_rate",
                                    "peak_input_data_rate",
                                    "peak_input_packet_rate",
                                    "peak_output_data_rate",
                                    "peak_output_packet_rate",
                                    "reliability") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InfraStatistics.Interfaces.Interface.DataRate, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InfraStatistics.Interfaces.Interface.DataRate, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bandwidth.is_set or
                        self.input_data_rate.is_set or
                        self.input_load.is_set or
                        self.input_packet_rate.is_set or
                        self.load_interval.is_set or
                        self.output_data_rate.is_set or
                        self.output_load.is_set or
                        self.output_packet_rate.is_set or
                        self.peak_input_data_rate.is_set or
                        self.peak_input_packet_rate.is_set or
                        self.peak_output_data_rate.is_set or
                        self.peak_output_packet_rate.is_set or
                        self.reliability.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bandwidth.yfilter != YFilter.not_set or
                        self.input_data_rate.yfilter != YFilter.not_set or
                        self.input_load.yfilter != YFilter.not_set or
                        self.input_packet_rate.yfilter != YFilter.not_set or
                        self.load_interval.yfilter != YFilter.not_set or
                        self.output_data_rate.yfilter != YFilter.not_set or
                        self.output_load.yfilter != YFilter.not_set or
                        self.output_packet_rate.yfilter != YFilter.not_set or
                        self.peak_input_data_rate.yfilter != YFilter.not_set or
                        self.peak_input_packet_rate.yfilter != YFilter.not_set or
                        self.peak_output_data_rate.yfilter != YFilter.not_set or
                        self.peak_output_packet_rate.yfilter != YFilter.not_set or
                        self.reliability.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "data-rate" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bandwidth.get_name_leafdata())
                    if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                    if (self.input_load.is_set or self.input_load.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_load.get_name_leafdata())
                    if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                    if (self.load_interval.is_set or self.load_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.load_interval.get_name_leafdata())
                    if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                    if (self.output_load.is_set or self.output_load.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_load.get_name_leafdata())
                    if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                    if (self.peak_input_data_rate.is_set or self.peak_input_data_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_input_data_rate.get_name_leafdata())
                    if (self.peak_input_packet_rate.is_set or self.peak_input_packet_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_input_packet_rate.get_name_leafdata())
                    if (self.peak_output_data_rate.is_set or self.peak_output_data_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_output_data_rate.get_name_leafdata())
                    if (self.peak_output_packet_rate.is_set or self.peak_output_packet_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_output_packet_rate.get_name_leafdata())
                    if (self.reliability.is_set or self.reliability.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reliability.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bandwidth" or name == "input-data-rate" or name == "input-load" or name == "input-packet-rate" or name == "load-interval" or name == "output-data-rate" or name == "output-load" or name == "output-packet-rate" or name == "peak-input-data-rate" or name == "peak-input-packet-rate" or name == "peak-output-data-rate" or name == "peak-output-packet-rate" or name == "reliability"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bandwidth"):
                        self.bandwidth = value
                        self.bandwidth.value_namespace = name_space
                        self.bandwidth.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-data-rate"):
                        self.input_data_rate = value
                        self.input_data_rate.value_namespace = name_space
                        self.input_data_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-load"):
                        self.input_load = value
                        self.input_load.value_namespace = name_space
                        self.input_load.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-packet-rate"):
                        self.input_packet_rate = value
                        self.input_packet_rate.value_namespace = name_space
                        self.input_packet_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "load-interval"):
                        self.load_interval = value
                        self.load_interval.value_namespace = name_space
                        self.load_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-data-rate"):
                        self.output_data_rate = value
                        self.output_data_rate.value_namespace = name_space
                        self.output_data_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-load"):
                        self.output_load = value
                        self.output_load.value_namespace = name_space
                        self.output_load.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-packet-rate"):
                        self.output_packet_rate = value
                        self.output_packet_rate.value_namespace = name_space
                        self.output_packet_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-input-data-rate"):
                        self.peak_input_data_rate = value
                        self.peak_input_data_rate.value_namespace = name_space
                        self.peak_input_data_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-input-packet-rate"):
                        self.peak_input_packet_rate = value
                        self.peak_input_packet_rate.value_namespace = name_space
                        self.peak_input_packet_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-output-data-rate"):
                        self.peak_output_data_rate = value
                        self.peak_output_data_rate.value_namespace = name_space
                        self.peak_output_data_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-output-packet-rate"):
                        self.peak_output_packet_rate = value
                        self.peak_output_packet_rate.value_namespace = name_space
                        self.peak_output_packet_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "reliability"):
                        self.reliability = value
                        self.reliability.value_namespace = name_space
                        self.reliability.value_namespace_prefix = name_space_prefix


            class GenericCounters(Entity):
                """
                Generic set of interface counters
                
                .. attribute:: applique
                
                	Applique
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.GenericCounters, self).__init__()

                    self.yang_name = "generic-counters"
                    self.yang_parent_name = "interface"

                    self.applique = YLeaf(YType.uint32, "applique")

                    self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                    self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                    self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                    self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                    self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                    self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                    self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                    self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                    self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                    self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                    self.input_drops = YLeaf(YType.uint32, "input-drops")

                    self.input_errors = YLeaf(YType.uint32, "input-errors")

                    self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                    self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                    self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                    self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                    self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                    self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                    self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                    self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                    self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                    self.output_drops = YLeaf(YType.uint32, "output-drops")

                    self.output_errors = YLeaf(YType.uint32, "output-errors")

                    self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                    self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                    self.packets_received = YLeaf(YType.uint64, "packets-received")

                    self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                    self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                    self.resets = YLeaf(YType.uint32, "resets")

                    self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                    self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                    self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                    self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                    self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                    self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("applique",
                                    "availability_flag",
                                    "broadcast_packets_received",
                                    "broadcast_packets_sent",
                                    "bytes_received",
                                    "bytes_sent",
                                    "carrier_transitions",
                                    "crc_errors",
                                    "framing_errors_received",
                                    "giant_packets_received",
                                    "input_aborts",
                                    "input_drops",
                                    "input_errors",
                                    "input_ignored_packets",
                                    "input_overruns",
                                    "input_queue_drops",
                                    "last_data_time",
                                    "last_discontinuity_time",
                                    "multicast_packets_received",
                                    "multicast_packets_sent",
                                    "output_buffer_failures",
                                    "output_buffers_swapped_out",
                                    "output_drops",
                                    "output_errors",
                                    "output_queue_drops",
                                    "output_underruns",
                                    "packets_received",
                                    "packets_sent",
                                    "parity_packets_received",
                                    "resets",
                                    "runt_packets_received",
                                    "seconds_since_last_clear_counters",
                                    "seconds_since_packet_received",
                                    "seconds_since_packet_sent",
                                    "throttled_packets_received",
                                    "unknown_protocol_packets_received") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InfraStatistics.Interfaces.Interface.GenericCounters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InfraStatistics.Interfaces.Interface.GenericCounters, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.applique.is_set or
                        self.availability_flag.is_set or
                        self.broadcast_packets_received.is_set or
                        self.broadcast_packets_sent.is_set or
                        self.bytes_received.is_set or
                        self.bytes_sent.is_set or
                        self.carrier_transitions.is_set or
                        self.crc_errors.is_set or
                        self.framing_errors_received.is_set or
                        self.giant_packets_received.is_set or
                        self.input_aborts.is_set or
                        self.input_drops.is_set or
                        self.input_errors.is_set or
                        self.input_ignored_packets.is_set or
                        self.input_overruns.is_set or
                        self.input_queue_drops.is_set or
                        self.last_data_time.is_set or
                        self.last_discontinuity_time.is_set or
                        self.multicast_packets_received.is_set or
                        self.multicast_packets_sent.is_set or
                        self.output_buffer_failures.is_set or
                        self.output_buffers_swapped_out.is_set or
                        self.output_drops.is_set or
                        self.output_errors.is_set or
                        self.output_queue_drops.is_set or
                        self.output_underruns.is_set or
                        self.packets_received.is_set or
                        self.packets_sent.is_set or
                        self.parity_packets_received.is_set or
                        self.resets.is_set or
                        self.runt_packets_received.is_set or
                        self.seconds_since_last_clear_counters.is_set or
                        self.seconds_since_packet_received.is_set or
                        self.seconds_since_packet_sent.is_set or
                        self.throttled_packets_received.is_set or
                        self.unknown_protocol_packets_received.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.applique.yfilter != YFilter.not_set or
                        self.availability_flag.yfilter != YFilter.not_set or
                        self.broadcast_packets_received.yfilter != YFilter.not_set or
                        self.broadcast_packets_sent.yfilter != YFilter.not_set or
                        self.bytes_received.yfilter != YFilter.not_set or
                        self.bytes_sent.yfilter != YFilter.not_set or
                        self.carrier_transitions.yfilter != YFilter.not_set or
                        self.crc_errors.yfilter != YFilter.not_set or
                        self.framing_errors_received.yfilter != YFilter.not_set or
                        self.giant_packets_received.yfilter != YFilter.not_set or
                        self.input_aborts.yfilter != YFilter.not_set or
                        self.input_drops.yfilter != YFilter.not_set or
                        self.input_errors.yfilter != YFilter.not_set or
                        self.input_ignored_packets.yfilter != YFilter.not_set or
                        self.input_overruns.yfilter != YFilter.not_set or
                        self.input_queue_drops.yfilter != YFilter.not_set or
                        self.last_data_time.yfilter != YFilter.not_set or
                        self.last_discontinuity_time.yfilter != YFilter.not_set or
                        self.multicast_packets_received.yfilter != YFilter.not_set or
                        self.multicast_packets_sent.yfilter != YFilter.not_set or
                        self.output_buffer_failures.yfilter != YFilter.not_set or
                        self.output_buffers_swapped_out.yfilter != YFilter.not_set or
                        self.output_drops.yfilter != YFilter.not_set or
                        self.output_errors.yfilter != YFilter.not_set or
                        self.output_queue_drops.yfilter != YFilter.not_set or
                        self.output_underruns.yfilter != YFilter.not_set or
                        self.packets_received.yfilter != YFilter.not_set or
                        self.packets_sent.yfilter != YFilter.not_set or
                        self.parity_packets_received.yfilter != YFilter.not_set or
                        self.resets.yfilter != YFilter.not_set or
                        self.runt_packets_received.yfilter != YFilter.not_set or
                        self.seconds_since_last_clear_counters.yfilter != YFilter.not_set or
                        self.seconds_since_packet_received.yfilter != YFilter.not_set or
                        self.seconds_since_packet_sent.yfilter != YFilter.not_set or
                        self.throttled_packets_received.yfilter != YFilter.not_set or
                        self.unknown_protocol_packets_received.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "generic-counters" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.applique.is_set or self.applique.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.applique.get_name_leafdata())
                    if (self.availability_flag.is_set or self.availability_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.availability_flag.get_name_leafdata())
                    if (self.broadcast_packets_received.is_set or self.broadcast_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast_packets_received.get_name_leafdata())
                    if (self.broadcast_packets_sent.is_set or self.broadcast_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.broadcast_packets_sent.get_name_leafdata())
                    if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_received.get_name_leafdata())
                    if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                    if (self.carrier_transitions.is_set or self.carrier_transitions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.carrier_transitions.get_name_leafdata())
                    if (self.crc_errors.is_set or self.crc_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.crc_errors.get_name_leafdata())
                    if (self.framing_errors_received.is_set or self.framing_errors_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.framing_errors_received.get_name_leafdata())
                    if (self.giant_packets_received.is_set or self.giant_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.giant_packets_received.get_name_leafdata())
                    if (self.input_aborts.is_set or self.input_aborts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_aborts.get_name_leafdata())
                    if (self.input_drops.is_set or self.input_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_drops.get_name_leafdata())
                    if (self.input_errors.is_set or self.input_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_errors.get_name_leafdata())
                    if (self.input_ignored_packets.is_set or self.input_ignored_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_ignored_packets.get_name_leafdata())
                    if (self.input_overruns.is_set or self.input_overruns.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_overruns.get_name_leafdata())
                    if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                    if (self.last_data_time.is_set or self.last_data_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_data_time.get_name_leafdata())
                    if (self.last_discontinuity_time.is_set or self.last_discontinuity_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_discontinuity_time.get_name_leafdata())
                    if (self.multicast_packets_received.is_set or self.multicast_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_packets_received.get_name_leafdata())
                    if (self.multicast_packets_sent.is_set or self.multicast_packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_packets_sent.get_name_leafdata())
                    if (self.output_buffer_failures.is_set or self.output_buffer_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_buffer_failures.get_name_leafdata())
                    if (self.output_buffers_swapped_out.is_set or self.output_buffers_swapped_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_buffers_swapped_out.get_name_leafdata())
                    if (self.output_drops.is_set or self.output_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_drops.get_name_leafdata())
                    if (self.output_errors.is_set or self.output_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_errors.get_name_leafdata())
                    if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                    if (self.output_underruns.is_set or self.output_underruns.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_underruns.get_name_leafdata())
                    if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_received.get_name_leafdata())
                    if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_sent.get_name_leafdata())
                    if (self.parity_packets_received.is_set or self.parity_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parity_packets_received.get_name_leafdata())
                    if (self.resets.is_set or self.resets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resets.get_name_leafdata())
                    if (self.runt_packets_received.is_set or self.runt_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.runt_packets_received.get_name_leafdata())
                    if (self.seconds_since_last_clear_counters.is_set or self.seconds_since_last_clear_counters.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_last_clear_counters.get_name_leafdata())
                    if (self.seconds_since_packet_received.is_set or self.seconds_since_packet_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_packet_received.get_name_leafdata())
                    if (self.seconds_since_packet_sent.is_set or self.seconds_since_packet_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_since_packet_sent.get_name_leafdata())
                    if (self.throttled_packets_received.is_set or self.throttled_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_packets_received.get_name_leafdata())
                    if (self.unknown_protocol_packets_received.is_set or self.unknown_protocol_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_protocol_packets_received.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "applique" or name == "availability-flag" or name == "broadcast-packets-received" or name == "broadcast-packets-sent" or name == "bytes-received" or name == "bytes-sent" or name == "carrier-transitions" or name == "crc-errors" or name == "framing-errors-received" or name == "giant-packets-received" or name == "input-aborts" or name == "input-drops" or name == "input-errors" or name == "input-ignored-packets" or name == "input-overruns" or name == "input-queue-drops" or name == "last-data-time" or name == "last-discontinuity-time" or name == "multicast-packets-received" or name == "multicast-packets-sent" or name == "output-buffer-failures" or name == "output-buffers-swapped-out" or name == "output-drops" or name == "output-errors" or name == "output-queue-drops" or name == "output-underruns" or name == "packets-received" or name == "packets-sent" or name == "parity-packets-received" or name == "resets" or name == "runt-packets-received" or name == "seconds-since-last-clear-counters" or name == "seconds-since-packet-received" or name == "seconds-since-packet-sent" or name == "throttled-packets-received" or name == "unknown-protocol-packets-received"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "applique"):
                        self.applique = value
                        self.applique.value_namespace = name_space
                        self.applique.value_namespace_prefix = name_space_prefix
                    if(value_path == "availability-flag"):
                        self.availability_flag = value
                        self.availability_flag.value_namespace = name_space
                        self.availability_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast-packets-received"):
                        self.broadcast_packets_received = value
                        self.broadcast_packets_received.value_namespace = name_space
                        self.broadcast_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "broadcast-packets-sent"):
                        self.broadcast_packets_sent = value
                        self.broadcast_packets_sent.value_namespace = name_space
                        self.broadcast_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-received"):
                        self.bytes_received = value
                        self.bytes_received.value_namespace = name_space
                        self.bytes_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-sent"):
                        self.bytes_sent = value
                        self.bytes_sent.value_namespace = name_space
                        self.bytes_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "carrier-transitions"):
                        self.carrier_transitions = value
                        self.carrier_transitions.value_namespace = name_space
                        self.carrier_transitions.value_namespace_prefix = name_space_prefix
                    if(value_path == "crc-errors"):
                        self.crc_errors = value
                        self.crc_errors.value_namespace = name_space
                        self.crc_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "framing-errors-received"):
                        self.framing_errors_received = value
                        self.framing_errors_received.value_namespace = name_space
                        self.framing_errors_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "giant-packets-received"):
                        self.giant_packets_received = value
                        self.giant_packets_received.value_namespace = name_space
                        self.giant_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-aborts"):
                        self.input_aborts = value
                        self.input_aborts.value_namespace = name_space
                        self.input_aborts.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-drops"):
                        self.input_drops = value
                        self.input_drops.value_namespace = name_space
                        self.input_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-errors"):
                        self.input_errors = value
                        self.input_errors.value_namespace = name_space
                        self.input_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-ignored-packets"):
                        self.input_ignored_packets = value
                        self.input_ignored_packets.value_namespace = name_space
                        self.input_ignored_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-overruns"):
                        self.input_overruns = value
                        self.input_overruns.value_namespace = name_space
                        self.input_overruns.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-queue-drops"):
                        self.input_queue_drops = value
                        self.input_queue_drops.value_namespace = name_space
                        self.input_queue_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-data-time"):
                        self.last_data_time = value
                        self.last_data_time.value_namespace = name_space
                        self.last_data_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-discontinuity-time"):
                        self.last_discontinuity_time = value
                        self.last_discontinuity_time.value_namespace = name_space
                        self.last_discontinuity_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-packets-received"):
                        self.multicast_packets_received = value
                        self.multicast_packets_received.value_namespace = name_space
                        self.multicast_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-packets-sent"):
                        self.multicast_packets_sent = value
                        self.multicast_packets_sent.value_namespace = name_space
                        self.multicast_packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-buffer-failures"):
                        self.output_buffer_failures = value
                        self.output_buffer_failures.value_namespace = name_space
                        self.output_buffer_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-buffers-swapped-out"):
                        self.output_buffers_swapped_out = value
                        self.output_buffers_swapped_out.value_namespace = name_space
                        self.output_buffers_swapped_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-drops"):
                        self.output_drops = value
                        self.output_drops.value_namespace = name_space
                        self.output_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-errors"):
                        self.output_errors = value
                        self.output_errors.value_namespace = name_space
                        self.output_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-queue-drops"):
                        self.output_queue_drops = value
                        self.output_queue_drops.value_namespace = name_space
                        self.output_queue_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-underruns"):
                        self.output_underruns = value
                        self.output_underruns.value_namespace = name_space
                        self.output_underruns.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-received"):
                        self.packets_received = value
                        self.packets_received.value_namespace = name_space
                        self.packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-sent"):
                        self.packets_sent = value
                        self.packets_sent.value_namespace = name_space
                        self.packets_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "parity-packets-received"):
                        self.parity_packets_received = value
                        self.parity_packets_received.value_namespace = name_space
                        self.parity_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "resets"):
                        self.resets = value
                        self.resets.value_namespace = name_space
                        self.resets.value_namespace_prefix = name_space_prefix
                    if(value_path == "runt-packets-received"):
                        self.runt_packets_received = value
                        self.runt_packets_received.value_namespace = name_space
                        self.runt_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-last-clear-counters"):
                        self.seconds_since_last_clear_counters = value
                        self.seconds_since_last_clear_counters.value_namespace = name_space
                        self.seconds_since_last_clear_counters.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-packet-received"):
                        self.seconds_since_packet_received = value
                        self.seconds_since_packet_received.value_namespace = name_space
                        self.seconds_since_packet_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "seconds-since-packet-sent"):
                        self.seconds_since_packet_sent = value
                        self.seconds_since_packet_sent.value_namespace = name_space
                        self.seconds_since_packet_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-packets-received"):
                        self.throttled_packets_received = value
                        self.throttled_packets_received.value_namespace = name_space
                        self.throttled_packets_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-protocol-packets-received"):
                        self.unknown_protocol_packets_received = value
                        self.unknown_protocol_packets_received.value_namespace = name_space
                        self.unknown_protocol_packets_received.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.cache is not None and self.cache.has_data()) or
                    (self.data_rate is not None and self.data_rate.has_data()) or
                    (self.generic_counters is not None and self.generic_counters.has_data()) or
                    (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_data()) or
                    (self.latest is not None and self.latest.has_data()) or
                    (self.protocols is not None and self.protocols.has_data()) or
                    (self.total is not None and self.total.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.cache is not None and self.cache.has_operation()) or
                    (self.data_rate is not None and self.data_rate.has_operation()) or
                    (self.generic_counters is not None and self.generic_counters.has_operation()) or
                    (self.interfaces_mib_counters is not None and self.interfaces_mib_counters.has_operation()) or
                    (self.latest is not None and self.latest.has_operation()) or
                    (self.protocols is not None and self.protocols.has_operation()) or
                    (self.total is not None and self.total.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cache"):
                    if (self.cache is None):
                        self.cache = InfraStatistics.Interfaces.Interface.Cache()
                        self.cache.parent = self
                        self._children_name_map["cache"] = "cache"
                    return self.cache

                if (child_yang_name == "data-rate"):
                    if (self.data_rate is None):
                        self.data_rate = InfraStatistics.Interfaces.Interface.DataRate()
                        self.data_rate.parent = self
                        self._children_name_map["data_rate"] = "data-rate"
                    return self.data_rate

                if (child_yang_name == "generic-counters"):
                    if (self.generic_counters is None):
                        self.generic_counters = InfraStatistics.Interfaces.Interface.GenericCounters()
                        self.generic_counters.parent = self
                        self._children_name_map["generic_counters"] = "generic-counters"
                    return self.generic_counters

                if (child_yang_name == "interfaces-mib-counters"):
                    if (self.interfaces_mib_counters is None):
                        self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.InterfacesMibCounters()
                        self.interfaces_mib_counters.parent = self
                        self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    return self.interfaces_mib_counters

                if (child_yang_name == "latest"):
                    if (self.latest is None):
                        self.latest = InfraStatistics.Interfaces.Interface.Latest()
                        self.latest.parent = self
                        self._children_name_map["latest"] = "latest"
                    return self.latest

                if (child_yang_name == "protocols"):
                    if (self.protocols is None):
                        self.protocols = InfraStatistics.Interfaces.Interface.Protocols()
                        self.protocols.parent = self
                        self._children_name_map["protocols"] = "protocols"
                    return self.protocols

                if (child_yang_name == "total"):
                    if (self.total is None):
                        self.total = InfraStatistics.Interfaces.Interface.Total()
                        self.total.parent = self
                        self._children_name_map["total"] = "total"
                    return self.total

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cache" or name == "data-rate" or name == "generic-counters" or name == "interfaces-mib-counters" or name == "latest" or name == "protocols" or name == "total" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = InfraStatistics.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.interfaces is not None and self.interfaces.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-statsd-oper:infra-statistics" + path_buffer

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

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = InfraStatistics.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraStatistics()
        return self._top_entity

