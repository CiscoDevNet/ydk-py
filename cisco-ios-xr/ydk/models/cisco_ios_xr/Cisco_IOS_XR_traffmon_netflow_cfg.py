""" Cisco_IOS_XR_traffmon_netflow_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR traffmon\-netflow package configuration.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NfCacheAgingMode(Enum):
    """
    NfCacheAgingMode

    Nf cache aging mode

    .. data:: normal = 0

    	Normal, caches age

    .. data:: permanent = 1

    	Permanent, caches never age

    .. data:: immediate = 2

    	Immediate, caches age immediately

    """

    normal = Enum.YLeaf(0, "normal")

    permanent = Enum.YLeaf(1, "permanent")

    immediate = Enum.YLeaf(2, "immediate")


class NfSamplingMode(Enum):
    """
    NfSamplingMode

    Nf sampling mode

    .. data:: random = 2

    	Random sampling

    """

    random = Enum.YLeaf(2, "random")



class NetFlow(Entity):
    """
    NetFlow Configuration
    
    .. attribute:: flow_exporter_maps
    
    	Configure a flow exporter map
    	**type**\:   :py:class:`FlowExporterMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps>`
    
    .. attribute:: flow_monitor_map_performance_table
    
    	Configure a performance traffic flow monitor map
    	**type**\:   :py:class:`FlowMonitorMapPerformanceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable>`
    
    .. attribute:: flow_monitor_map_table
    
    	Flow monitor map configuration
    	**type**\:   :py:class:`FlowMonitorMapTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable>`
    
    .. attribute:: flow_sampler_maps
    
    	Flow sampler map configuration
    	**type**\:   :py:class:`FlowSamplerMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps>`
    
    

    """

    _prefix = 'traffmon-netflow-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NetFlow, self).__init__()
        self._top_entity = None

        self.yang_name = "net-flow"
        self.yang_parent_name = "Cisco-IOS-XR-traffmon-netflow-cfg"

        self.flow_exporter_maps = NetFlow.FlowExporterMaps()
        self.flow_exporter_maps.parent = self
        self._children_name_map["flow_exporter_maps"] = "flow-exporter-maps"
        self._children_yang_names.add("flow-exporter-maps")

        self.flow_monitor_map_performance_table = NetFlow.FlowMonitorMapPerformanceTable()
        self.flow_monitor_map_performance_table.parent = self
        self._children_name_map["flow_monitor_map_performance_table"] = "flow-monitor-map-performance-table"
        self._children_yang_names.add("flow-monitor-map-performance-table")

        self.flow_monitor_map_table = NetFlow.FlowMonitorMapTable()
        self.flow_monitor_map_table.parent = self
        self._children_name_map["flow_monitor_map_table"] = "flow-monitor-map-table"
        self._children_yang_names.add("flow-monitor-map-table")

        self.flow_sampler_maps = NetFlow.FlowSamplerMaps()
        self.flow_sampler_maps.parent = self
        self._children_name_map["flow_sampler_maps"] = "flow-sampler-maps"
        self._children_yang_names.add("flow-sampler-maps")


    class FlowExporterMaps(Entity):
        """
        Configure a flow exporter map
        
        .. attribute:: flow_exporter_map
        
        	Exporter map name
        	**type**\: list of    :py:class:`FlowExporterMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.FlowExporterMaps, self).__init__()

            self.yang_name = "flow-exporter-maps"
            self.yang_parent_name = "net-flow"

            self.flow_exporter_map = YList(self)

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
                        super(NetFlow.FlowExporterMaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetFlow.FlowExporterMaps, self).__setattr__(name, value)


        class FlowExporterMap(Entity):
            """
            Exporter map name
            
            .. attribute:: exporter_map_name  <key>
            
            	Exporter map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: destination
            
            	Configure export destination (collector)
            	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Destination>`
            
            .. attribute:: dscp
            
            	Specify DSCP value for export packets
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: packet_length
            
            	Configure Maximum Value for Export Packet size
            	**type**\:  int
            
            	**range:** 512..1468
            
            .. attribute:: source_interface
            
            	Configure source interface for collector
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: udp
            
            	Use UDP as transport protocol
            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Udp>`
            
            .. attribute:: versions
            
            	Specify export version parameters
            	**type**\:   :py:class:`Versions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.FlowExporterMaps.FlowExporterMap, self).__init__()

                self.yang_name = "flow-exporter-map"
                self.yang_parent_name = "flow-exporter-maps"

                self.exporter_map_name = YLeaf(YType.str, "exporter-map-name")

                self.dscp = YLeaf(YType.uint32, "dscp")

                self.packet_length = YLeaf(YType.uint32, "packet-length")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.destination = NetFlow.FlowExporterMaps.FlowExporterMap.Destination()
                self.destination.parent = self
                self._children_name_map["destination"] = "destination"
                self._children_yang_names.add("destination")

                self.udp = NetFlow.FlowExporterMaps.FlowExporterMap.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
                self._children_yang_names.add("udp")

                self.versions = NetFlow.FlowExporterMaps.FlowExporterMap.Versions()
                self.versions.parent = self
                self._children_name_map["versions"] = "versions"
                self._children_yang_names.add("versions")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("exporter_map_name",
                                "dscp",
                                "packet_length",
                                "source_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetFlow.FlowExporterMaps.FlowExporterMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetFlow.FlowExporterMaps.FlowExporterMap, self).__setattr__(name, value)


            class Udp(Entity):
                """
                Use UDP as transport protocol
                
                .. attribute:: destination_port
                
                	Configure Destination UDP port
                	**type**\:  int
                
                	**range:** 1024..65535
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, self).__init__()

                    self.yang_name = "udp"
                    self.yang_parent_name = "flow-exporter-map"

                    self.destination_port = YLeaf(YType.uint32, "destination-port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, self).__setattr__(name, value)

                def has_data(self):
                    return self.destination_port.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "udp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-port"):
                        self.destination_port = value
                        self.destination_port.value_namespace = name_space
                        self.destination_port.value_namespace_prefix = name_space_prefix


            class Versions(Entity):
                """
                Specify export version parameters
                
                .. attribute:: version
                
                	Configure export version options
                	**type**\: list of    :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions, self).__init__()

                    self.yang_name = "versions"
                    self.yang_parent_name = "flow-exporter-map"

                    self.version = YList(self)

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
                                super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions, self).__setattr__(name, value)


                class Version(Entity):
                    """
                    Configure export version options
                    
                    .. attribute:: version_number  <key>
                    
                    	Export version number
                    	**type**\:  int
                    
                    	**range:** 9..10
                    
                    .. attribute:: common_template_timeout
                    
                    	Specify custom timeout for the template
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    .. attribute:: data_template_timeout
                    
                    	Data template configuration options
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    .. attribute:: options
                    
                    	Specify options for exporting templates
                    	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options>`
                    
                    .. attribute:: options_template_timeout
                    
                    	Option template configuration options
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version, self).__init__()

                        self.yang_name = "version"
                        self.yang_parent_name = "versions"

                        self.version_number = YLeaf(YType.uint32, "version-number")

                        self.common_template_timeout = YLeaf(YType.uint32, "common-template-timeout")

                        self.data_template_timeout = YLeaf(YType.uint32, "data-template-timeout")

                        self.options_template_timeout = YLeaf(YType.uint32, "options-template-timeout")

                        self.options = NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options()
                        self.options.parent = self
                        self._children_name_map["options"] = "options"
                        self._children_yang_names.add("options")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("version_number",
                                        "common_template_timeout",
                                        "data_template_timeout",
                                        "options_template_timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version, self).__setattr__(name, value)


                    class Options(Entity):
                        """
                        Specify options for exporting templates
                        
                        .. attribute:: interface_table_export_timeout
                        
                        	Specify timeout for exporting interface table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        .. attribute:: sampler_table_export_timeout
                        
                        	Specify timeout for exporting sampler table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        .. attribute:: vrf_table_export_timeout
                        
                        	Specify timeout for exporting vrf table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'traffmon-netflow-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options, self).__init__()

                            self.yang_name = "options"
                            self.yang_parent_name = "version"

                            self.interface_table_export_timeout = YLeaf(YType.uint32, "interface-table-export-timeout")

                            self.sampler_table_export_timeout = YLeaf(YType.uint32, "sampler-table-export-timeout")

                            self.vrf_table_export_timeout = YLeaf(YType.uint32, "vrf-table-export-timeout")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_table_export_timeout",
                                            "sampler_table_export_timeout",
                                            "vrf_table_export_timeout") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_table_export_timeout.is_set or
                                self.sampler_table_export_timeout.is_set or
                                self.vrf_table_export_timeout.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_table_export_timeout.yfilter != YFilter.not_set or
                                self.sampler_table_export_timeout.yfilter != YFilter.not_set or
                                self.vrf_table_export_timeout.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_table_export_timeout.is_set or self.interface_table_export_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_table_export_timeout.get_name_leafdata())
                            if (self.sampler_table_export_timeout.is_set or self.sampler_table_export_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sampler_table_export_timeout.get_name_leafdata())
                            if (self.vrf_table_export_timeout.is_set or self.vrf_table_export_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_table_export_timeout.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-table-export-timeout" or name == "sampler-table-export-timeout" or name == "vrf-table-export-timeout"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-table-export-timeout"):
                                self.interface_table_export_timeout = value
                                self.interface_table_export_timeout.value_namespace = name_space
                                self.interface_table_export_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "sampler-table-export-timeout"):
                                self.sampler_table_export_timeout = value
                                self.sampler_table_export_timeout.value_namespace = name_space
                                self.sampler_table_export_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-table-export-timeout"):
                                self.vrf_table_export_timeout = value
                                self.vrf_table_export_timeout.value_namespace = name_space
                                self.vrf_table_export_timeout.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.version_number.is_set or
                            self.common_template_timeout.is_set or
                            self.data_template_timeout.is_set or
                            self.options_template_timeout.is_set or
                            (self.options is not None and self.options.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.version_number.yfilter != YFilter.not_set or
                            self.common_template_timeout.yfilter != YFilter.not_set or
                            self.data_template_timeout.yfilter != YFilter.not_set or
                            self.options_template_timeout.yfilter != YFilter.not_set or
                            (self.options is not None and self.options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "version" + "[version-number='" + self.version_number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.version_number.is_set or self.version_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version_number.get_name_leafdata())
                        if (self.common_template_timeout.is_set or self.common_template_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_template_timeout.get_name_leafdata())
                        if (self.data_template_timeout.is_set or self.data_template_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.data_template_timeout.get_name_leafdata())
                        if (self.options_template_timeout.is_set or self.options_template_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.options_template_timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "options"):
                            if (self.options is None):
                                self.options = NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                            return self.options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "options" or name == "version-number" or name == "common-template-timeout" or name == "data-template-timeout" or name == "options-template-timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "version-number"):
                            self.version_number = value
                            self.version_number.value_namespace = name_space
                            self.version_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "common-template-timeout"):
                            self.common_template_timeout = value
                            self.common_template_timeout.value_namespace = name_space
                            self.common_template_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "data-template-timeout"):
                            self.data_template_timeout = value
                            self.data_template_timeout.value_namespace = name_space
                            self.data_template_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "options-template-timeout"):
                            self.options_template_timeout = value
                            self.options_template_timeout.value_namespace = name_space
                            self.options_template_timeout.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.version:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.version:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "versions" + path_buffer

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

                    if (child_yang_name == "version"):
                        for c in self.version:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.version.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Destination(Entity):
                """
                Configure export destination (collector)
                
                .. attribute:: ip_address
                
                	Destination IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPV6 address of the tunnel destination
                	**type**\:  str
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "flow-exporter-map"

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

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
                        if name in ("ip_address",
                                    "ipv6_address",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip_address.is_set or
                        self.ipv6_address.is_set or
                        self.vrf_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip_address.yfilter != YFilter.not_set or
                        self.ipv6_address.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address.get_name_leafdata())
                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())
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
                    if(name == "ip-address" or name == "ipv6-address" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip-address"):
                        self.ip_address = value
                        self.ip_address.value_namespace = name_space
                        self.ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-address"):
                        self.ipv6_address = value
                        self.ipv6_address.value_namespace = name_space
                        self.ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.exporter_map_name.is_set or
                    self.dscp.is_set or
                    self.packet_length.is_set or
                    self.source_interface.is_set or
                    (self.destination is not None and self.destination.has_data()) or
                    (self.udp is not None and self.udp.has_data()) or
                    (self.versions is not None and self.versions.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.exporter_map_name.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.packet_length.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set or
                    (self.destination is not None and self.destination.has_operation()) or
                    (self.udp is not None and self.udp.has_operation()) or
                    (self.versions is not None and self.versions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flow-exporter-map" + "[exporter-map-name='" + self.exporter_map_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-exporter-maps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.exporter_map_name.is_set or self.exporter_map_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.exporter_map_name.get_name_leafdata())
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.packet_length.is_set or self.packet_length.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packet_length.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "destination"):
                    if (self.destination is None):
                        self.destination = NetFlow.FlowExporterMaps.FlowExporterMap.Destination()
                        self.destination.parent = self
                        self._children_name_map["destination"] = "destination"
                    return self.destination

                if (child_yang_name == "udp"):
                    if (self.udp is None):
                        self.udp = NetFlow.FlowExporterMaps.FlowExporterMap.Udp()
                        self.udp.parent = self
                        self._children_name_map["udp"] = "udp"
                    return self.udp

                if (child_yang_name == "versions"):
                    if (self.versions is None):
                        self.versions = NetFlow.FlowExporterMaps.FlowExporterMap.Versions()
                        self.versions.parent = self
                        self._children_name_map["versions"] = "versions"
                    return self.versions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "udp" or name == "versions" or name == "exporter-map-name" or name == "dscp" or name == "packet-length" or name == "source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "exporter-map-name"):
                    self.exporter_map_name = value
                    self.exporter_map_name.value_namespace = name_space
                    self.exporter_map_name.value_namespace_prefix = name_space_prefix
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "packet-length"):
                    self.packet_length = value
                    self.packet_length.value_namespace = name_space
                    self.packet_length.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.flow_exporter_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.flow_exporter_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flow-exporter-maps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flow-exporter-map"):
                for c in self.flow_exporter_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetFlow.FlowExporterMaps.FlowExporterMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.flow_exporter_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flow-exporter-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class FlowSamplerMaps(Entity):
        """
        Flow sampler map configuration
        
        .. attribute:: flow_sampler_map
        
        	Sampler map name
        	**type**\: list of    :py:class:`FlowSamplerMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.FlowSamplerMaps, self).__init__()

            self.yang_name = "flow-sampler-maps"
            self.yang_parent_name = "net-flow"

            self.flow_sampler_map = YList(self)

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
                        super(NetFlow.FlowSamplerMaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetFlow.FlowSamplerMaps, self).__setattr__(name, value)


        class FlowSamplerMap(Entity):
            """
            Sampler map name
            
            .. attribute:: sampler_map_name  <key>
            
            	Sampler map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: sampling_modes
            
            	Configure packet sampling mode
            	**type**\:   :py:class:`SamplingModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.FlowSamplerMaps.FlowSamplerMap, self).__init__()

                self.yang_name = "flow-sampler-map"
                self.yang_parent_name = "flow-sampler-maps"

                self.sampler_map_name = YLeaf(YType.str, "sampler-map-name")

                self.sampling_modes = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes()
                self.sampling_modes.parent = self
                self._children_name_map["sampling_modes"] = "sampling-modes"
                self._children_yang_names.add("sampling-modes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sampler_map_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetFlow.FlowSamplerMaps.FlowSamplerMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetFlow.FlowSamplerMaps.FlowSamplerMap, self).__setattr__(name, value)


            class SamplingModes(Entity):
                """
                Configure packet sampling mode
                
                .. attribute:: sampling_mode
                
                	Configure sampling mode
                	**type**\: list of    :py:class:`SamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, self).__init__()

                    self.yang_name = "sampling-modes"
                    self.yang_parent_name = "flow-sampler-map"

                    self.sampling_mode = YList(self)

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
                                super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, self).__setattr__(name, value)


                class SamplingMode(Entity):
                    """
                    Configure sampling mode
                    
                    .. attribute:: mode  <key>
                    
                    	Sampling mode
                    	**type**\:   :py:class:`NfSamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfSamplingMode>`
                    
                    .. attribute:: interval
                    
                    	Sampling interval in units of packets
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: sample_number
                    
                    	Number of packets to be sampled in the sampling interval
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, self).__init__()

                        self.yang_name = "sampling-mode"
                        self.yang_parent_name = "sampling-modes"

                        self.mode = YLeaf(YType.enumeration, "mode")

                        self.interval = YLeaf(YType.uint32, "interval")

                        self.sample_number = YLeaf(YType.uint32, "sample-number")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mode",
                                        "interval",
                                        "sample_number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.mode.is_set or
                            self.interval.is_set or
                            self.sample_number.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mode.yfilter != YFilter.not_set or
                            self.interval.yfilter != YFilter.not_set or
                            self.sample_number.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sampling-mode" + "[mode='" + self.mode.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mode.get_name_leafdata())
                        if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval.get_name_leafdata())
                        if (self.sample_number.is_set or self.sample_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sample_number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mode" or name == "interval" or name == "sample-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mode"):
                            self.mode = value
                            self.mode.value_namespace = name_space
                            self.mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "interval"):
                            self.interval = value
                            self.interval.value_namespace = name_space
                            self.interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "sample-number"):
                            self.sample_number = value
                            self.sample_number.value_namespace = name_space
                            self.sample_number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sampling_mode:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sampling_mode:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sampling-modes" + path_buffer

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

                    if (child_yang_name == "sampling-mode"):
                        for c in self.sampling_mode:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sampling_mode.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sampling-mode"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.sampler_map_name.is_set or
                    (self.sampling_modes is not None and self.sampling_modes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sampler_map_name.yfilter != YFilter.not_set or
                    (self.sampling_modes is not None and self.sampling_modes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flow-sampler-map" + "[sampler-map-name='" + self.sampler_map_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-sampler-maps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sampler_map_name.is_set or self.sampler_map_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sampler_map_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sampling-modes"):
                    if (self.sampling_modes is None):
                        self.sampling_modes = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes()
                        self.sampling_modes.parent = self
                        self._children_name_map["sampling_modes"] = "sampling-modes"
                    return self.sampling_modes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sampling-modes" or name == "sampler-map-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sampler-map-name"):
                    self.sampler_map_name = value
                    self.sampler_map_name.value_namespace = name_space
                    self.sampler_map_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.flow_sampler_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.flow_sampler_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flow-sampler-maps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flow-sampler-map"):
                for c in self.flow_sampler_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetFlow.FlowSamplerMaps.FlowSamplerMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.flow_sampler_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flow-sampler-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class FlowMonitorMapTable(Entity):
        """
        Flow monitor map configuration
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of    :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.FlowMonitorMapTable, self).__init__()

            self.yang_name = "flow-monitor-map-table"
            self.yang_parent_name = "net-flow"

            self.flow_monitor_map = YList(self)

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
                        super(NetFlow.FlowMonitorMapTable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetFlow.FlowMonitorMapTable, self).__setattr__(name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  <key>
            
            	Monitor map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:   :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\:  int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\:  int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:   :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:   :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-table"

                self.monitor_map_name = YLeaf(YType.str, "monitor-map-name")

                self.cache_active_aging_timeout = YLeaf(YType.uint32, "cache-active-aging-timeout")

                self.cache_aging_mode = YLeaf(YType.enumeration, "cache-aging-mode")

                self.cache_entries = YLeaf(YType.uint32, "cache-entries")

                self.cache_inactive_aging_timeout = YLeaf(YType.uint32, "cache-inactive-aging-timeout")

                self.cache_timeout_rate_limit = YLeaf(YType.uint32, "cache-timeout-rate-limit")

                self.cache_update_aging_timeout = YLeaf(YType.uint32, "cache-update-aging-timeout")

                self.exporters = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.option = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("monitor_map_name",
                                "cache_active_aging_timeout",
                                "cache_aging_mode",
                                "cache_entries",
                                "cache_inactive_aging_timeout",
                                "cache_timeout_rate_limit",
                                "cache_update_aging_timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetFlow.FlowMonitorMapTable.FlowMonitorMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetFlow.FlowMonitorMapTable.FlowMonitorMap, self).__setattr__(name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"

                    self.bgp_attr = YLeaf(YType.empty, "bgp-attr")

                    self.filtered = YLeaf(YType.empty, "filtered")

                    self.out_bundle_member = YLeaf(YType.empty, "out-bundle-member")

                    self.out_phys_int = YLeaf(YType.empty, "out-phys-int")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bgp_attr",
                                    "filtered",
                                    "out_bundle_member",
                                    "out_phys_int") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bgp_attr.is_set or
                        self.filtered.is_set or
                        self.out_bundle_member.is_set or
                        self.out_phys_int.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bgp_attr.yfilter != YFilter.not_set or
                        self.filtered.yfilter != YFilter.not_set or
                        self.out_bundle_member.yfilter != YFilter.not_set or
                        self.out_phys_int.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "option" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bgp_attr.is_set or self.bgp_attr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bgp_attr.get_name_leafdata())
                    if (self.filtered.is_set or self.filtered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.filtered.get_name_leafdata())
                    if (self.out_bundle_member.is_set or self.out_bundle_member.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_bundle_member.get_name_leafdata())
                    if (self.out_phys_int.is_set or self.out_phys_int.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_phys_int.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-attr" or name == "filtered" or name == "out-bundle-member" or name == "out-phys-int"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bgp-attr"):
                        self.bgp_attr = value
                        self.bgp_attr.value_namespace = name_space
                        self.bgp_attr.value_namespace_prefix = name_space_prefix
                    if(value_path == "filtered"):
                        self.filtered = value
                        self.filtered.value_namespace = name_space
                        self.filtered.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-bundle-member"):
                        self.out_bundle_member = value
                        self.out_bundle_member.value_namespace = name_space
                        self.out_bundle_member.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-phys-int"):
                        self.out_phys_int = value
                        self.out_phys_int.value_namespace = name_space
                        self.out_phys_int.value_namespace_prefix = name_space_prefix


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of    :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"

                    self.exporter = YList(self)

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
                                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, self).__setattr__(name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  <key>
                    
                    	Exporter name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, self).__init__()

                        self.yang_name = "exporter"
                        self.yang_parent_name = "exporters"

                        self.exporter_name = YLeaf(YType.str, "exporter-name")

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
                                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, self).__setattr__(name, value)

                    def has_data(self):
                        return self.exporter_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.exporter_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "exporter" + "[exporter-name='" + self.exporter_name.get() + "']" + path_buffer

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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "exporter-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "exporter-name"):
                            self.exporter_name = value
                            self.exporter_name.value_namespace = name_space
                            self.exporter_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.exporter:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.exporter:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "exporters" + path_buffer

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

                    if (child_yang_name == "exporter"):
                        for c in self.exporter:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.exporter.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "exporter"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\:  int
                
                	**range:** 1..6
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\:  str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, self).__init__()

                    self.yang_name = "record"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_presence_container = True

                    self.label = YLeaf(YType.uint32, "label")

                    self.record_name = YLeaf(YType.str, "record-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("label",
                                    "record_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.label.is_set or
                        self.record_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.label.yfilter != YFilter.not_set or
                        self.record_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "record" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.label.get_name_leafdata())
                    if (self.record_name.is_set or self.record_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.record_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "label" or name == "record-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "label"):
                        self.label = value
                        self.label.value_namespace = name_space
                        self.label.value_namespace_prefix = name_space_prefix
                    if(value_path == "record-name"):
                        self.record_name = value
                        self.record_name.value_namespace = name_space
                        self.record_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.monitor_map_name.is_set or
                    self.cache_active_aging_timeout.is_set or
                    self.cache_aging_mode.is_set or
                    self.cache_entries.is_set or
                    self.cache_inactive_aging_timeout.is_set or
                    self.cache_timeout_rate_limit.is_set or
                    self.cache_update_aging_timeout.is_set or
                    (self.exporters is not None and self.exporters.has_data()) or
                    (self.option is not None and self.option.has_data()) or
                    (self.record is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.monitor_map_name.yfilter != YFilter.not_set or
                    self.cache_active_aging_timeout.yfilter != YFilter.not_set or
                    self.cache_aging_mode.yfilter != YFilter.not_set or
                    self.cache_entries.yfilter != YFilter.not_set or
                    self.cache_inactive_aging_timeout.yfilter != YFilter.not_set or
                    self.cache_timeout_rate_limit.yfilter != YFilter.not_set or
                    self.cache_update_aging_timeout.yfilter != YFilter.not_set or
                    (self.exporters is not None and self.exporters.has_operation()) or
                    (self.option is not None and self.option.has_operation()) or
                    (self.record is not None and self.record.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flow-monitor-map" + "[monitor-map-name='" + self.monitor_map_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.monitor_map_name.is_set or self.monitor_map_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.monitor_map_name.get_name_leafdata())
                if (self.cache_active_aging_timeout.is_set or self.cache_active_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_active_aging_timeout.get_name_leafdata())
                if (self.cache_aging_mode.is_set or self.cache_aging_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_aging_mode.get_name_leafdata())
                if (self.cache_entries.is_set or self.cache_entries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_entries.get_name_leafdata())
                if (self.cache_inactive_aging_timeout.is_set or self.cache_inactive_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_inactive_aging_timeout.get_name_leafdata())
                if (self.cache_timeout_rate_limit.is_set or self.cache_timeout_rate_limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_timeout_rate_limit.get_name_leafdata())
                if (self.cache_update_aging_timeout.is_set or self.cache_update_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_update_aging_timeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "exporters"):
                    if (self.exporters is None):
                        self.exporters = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters()
                        self.exporters.parent = self
                        self._children_name_map["exporters"] = "exporters"
                    return self.exporters

                if (child_yang_name == "option"):
                    if (self.option is None):
                        self.option = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option()
                        self.option.parent = self
                        self._children_name_map["option"] = "option"
                    return self.option

                if (child_yang_name == "record"):
                    if (self.record is None):
                        self.record = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record()
                        self.record.parent = self
                        self._children_name_map["record"] = "record"
                    return self.record

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "exporters" or name == "option" or name == "record" or name == "monitor-map-name" or name == "cache-active-aging-timeout" or name == "cache-aging-mode" or name == "cache-entries" or name == "cache-inactive-aging-timeout" or name == "cache-timeout-rate-limit" or name == "cache-update-aging-timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "monitor-map-name"):
                    self.monitor_map_name = value
                    self.monitor_map_name.value_namespace = name_space
                    self.monitor_map_name.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-active-aging-timeout"):
                    self.cache_active_aging_timeout = value
                    self.cache_active_aging_timeout.value_namespace = name_space
                    self.cache_active_aging_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-aging-mode"):
                    self.cache_aging_mode = value
                    self.cache_aging_mode.value_namespace = name_space
                    self.cache_aging_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-entries"):
                    self.cache_entries = value
                    self.cache_entries.value_namespace = name_space
                    self.cache_entries.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-inactive-aging-timeout"):
                    self.cache_inactive_aging_timeout = value
                    self.cache_inactive_aging_timeout.value_namespace = name_space
                    self.cache_inactive_aging_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-timeout-rate-limit"):
                    self.cache_timeout_rate_limit = value
                    self.cache_timeout_rate_limit.value_namespace = name_space
                    self.cache_timeout_rate_limit.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-update-aging-timeout"):
                    self.cache_update_aging_timeout = value
                    self.cache_update_aging_timeout.value_namespace = name_space
                    self.cache_update_aging_timeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.flow_monitor_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.flow_monitor_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flow-monitor-map-table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flow-monitor-map"):
                for c in self.flow_monitor_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetFlow.FlowMonitorMapTable.FlowMonitorMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.flow_monitor_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flow-monitor-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class FlowMonitorMapPerformanceTable(Entity):
        """
        Configure a performance traffic flow monitor map
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of    :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.FlowMonitorMapPerformanceTable, self).__init__()

            self.yang_name = "flow-monitor-map-performance-table"
            self.yang_parent_name = "net-flow"

            self.flow_monitor_map = YList(self)

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
                        super(NetFlow.FlowMonitorMapPerformanceTable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetFlow.FlowMonitorMapPerformanceTable, self).__setattr__(name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  <key>
            
            	Monitor map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:   :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\:  int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\:  int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:   :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:   :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-performance-table"

                self.monitor_map_name = YLeaf(YType.str, "monitor-map-name")

                self.cache_active_aging_timeout = YLeaf(YType.uint32, "cache-active-aging-timeout")

                self.cache_aging_mode = YLeaf(YType.enumeration, "cache-aging-mode")

                self.cache_entries = YLeaf(YType.uint32, "cache-entries")

                self.cache_inactive_aging_timeout = YLeaf(YType.uint32, "cache-inactive-aging-timeout")

                self.cache_timeout_rate_limit = YLeaf(YType.uint32, "cache-timeout-rate-limit")

                self.cache_update_aging_timeout = YLeaf(YType.uint32, "cache-update-aging-timeout")

                self.exporters = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.option = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("monitor_map_name",
                                "cache_active_aging_timeout",
                                "cache_aging_mode",
                                "cache_entries",
                                "cache_inactive_aging_timeout",
                                "cache_timeout_rate_limit",
                                "cache_update_aging_timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, self).__setattr__(name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"

                    self.bgp_attr = YLeaf(YType.empty, "bgp-attr")

                    self.filtered = YLeaf(YType.empty, "filtered")

                    self.out_bundle_member = YLeaf(YType.empty, "out-bundle-member")

                    self.out_phys_int = YLeaf(YType.empty, "out-phys-int")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bgp_attr",
                                    "filtered",
                                    "out_bundle_member",
                                    "out_phys_int") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bgp_attr.is_set or
                        self.filtered.is_set or
                        self.out_bundle_member.is_set or
                        self.out_phys_int.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bgp_attr.yfilter != YFilter.not_set or
                        self.filtered.yfilter != YFilter.not_set or
                        self.out_bundle_member.yfilter != YFilter.not_set or
                        self.out_phys_int.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "option" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bgp_attr.is_set or self.bgp_attr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bgp_attr.get_name_leafdata())
                    if (self.filtered.is_set or self.filtered.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.filtered.get_name_leafdata())
                    if (self.out_bundle_member.is_set or self.out_bundle_member.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_bundle_member.get_name_leafdata())
                    if (self.out_phys_int.is_set or self.out_phys_int.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_phys_int.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-attr" or name == "filtered" or name == "out-bundle-member" or name == "out-phys-int"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bgp-attr"):
                        self.bgp_attr = value
                        self.bgp_attr.value_namespace = name_space
                        self.bgp_attr.value_namespace_prefix = name_space_prefix
                    if(value_path == "filtered"):
                        self.filtered = value
                        self.filtered.value_namespace = name_space
                        self.filtered.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-bundle-member"):
                        self.out_bundle_member = value
                        self.out_bundle_member.value_namespace = name_space
                        self.out_bundle_member.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-phys-int"):
                        self.out_phys_int = value
                        self.out_phys_int.value_namespace = name_space
                        self.out_phys_int.value_namespace_prefix = name_space_prefix


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of    :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"

                    self.exporter = YList(self)

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
                                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, self).__setattr__(name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  <key>
                    
                    	Exporter name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, self).__init__()

                        self.yang_name = "exporter"
                        self.yang_parent_name = "exporters"

                        self.exporter_name = YLeaf(YType.str, "exporter-name")

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
                                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, self).__setattr__(name, value)

                    def has_data(self):
                        return self.exporter_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.exporter_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "exporter" + "[exporter-name='" + self.exporter_name.get() + "']" + path_buffer

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

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "exporter-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "exporter-name"):
                            self.exporter_name = value
                            self.exporter_name.value_namespace = name_space
                            self.exporter_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.exporter:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.exporter:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "exporters" + path_buffer

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

                    if (child_yang_name == "exporter"):
                        for c in self.exporter:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.exporter.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "exporter"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\:  int
                
                	**range:** 1..6
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\:  str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, self).__init__()

                    self.yang_name = "record"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_presence_container = True

                    self.label = YLeaf(YType.uint32, "label")

                    self.record_name = YLeaf(YType.str, "record-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("label",
                                    "record_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.label.is_set or
                        self.record_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.label.yfilter != YFilter.not_set or
                        self.record_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "record" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.label.get_name_leafdata())
                    if (self.record_name.is_set or self.record_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.record_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "label" or name == "record-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "label"):
                        self.label = value
                        self.label.value_namespace = name_space
                        self.label.value_namespace_prefix = name_space_prefix
                    if(value_path == "record-name"):
                        self.record_name = value
                        self.record_name.value_namespace = name_space
                        self.record_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.monitor_map_name.is_set or
                    self.cache_active_aging_timeout.is_set or
                    self.cache_aging_mode.is_set or
                    self.cache_entries.is_set or
                    self.cache_inactive_aging_timeout.is_set or
                    self.cache_timeout_rate_limit.is_set or
                    self.cache_update_aging_timeout.is_set or
                    (self.exporters is not None and self.exporters.has_data()) or
                    (self.option is not None and self.option.has_data()) or
                    (self.record is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.monitor_map_name.yfilter != YFilter.not_set or
                    self.cache_active_aging_timeout.yfilter != YFilter.not_set or
                    self.cache_aging_mode.yfilter != YFilter.not_set or
                    self.cache_entries.yfilter != YFilter.not_set or
                    self.cache_inactive_aging_timeout.yfilter != YFilter.not_set or
                    self.cache_timeout_rate_limit.yfilter != YFilter.not_set or
                    self.cache_update_aging_timeout.yfilter != YFilter.not_set or
                    (self.exporters is not None and self.exporters.has_operation()) or
                    (self.option is not None and self.option.has_operation()) or
                    (self.record is not None and self.record.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flow-monitor-map" + "[monitor-map-name='" + self.monitor_map_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-performance-table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.monitor_map_name.is_set or self.monitor_map_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.monitor_map_name.get_name_leafdata())
                if (self.cache_active_aging_timeout.is_set or self.cache_active_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_active_aging_timeout.get_name_leafdata())
                if (self.cache_aging_mode.is_set or self.cache_aging_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_aging_mode.get_name_leafdata())
                if (self.cache_entries.is_set or self.cache_entries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_entries.get_name_leafdata())
                if (self.cache_inactive_aging_timeout.is_set or self.cache_inactive_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_inactive_aging_timeout.get_name_leafdata())
                if (self.cache_timeout_rate_limit.is_set or self.cache_timeout_rate_limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_timeout_rate_limit.get_name_leafdata())
                if (self.cache_update_aging_timeout.is_set or self.cache_update_aging_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_update_aging_timeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "exporters"):
                    if (self.exporters is None):
                        self.exporters = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters()
                        self.exporters.parent = self
                        self._children_name_map["exporters"] = "exporters"
                    return self.exporters

                if (child_yang_name == "option"):
                    if (self.option is None):
                        self.option = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option()
                        self.option.parent = self
                        self._children_name_map["option"] = "option"
                    return self.option

                if (child_yang_name == "record"):
                    if (self.record is None):
                        self.record = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record()
                        self.record.parent = self
                        self._children_name_map["record"] = "record"
                    return self.record

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "exporters" or name == "option" or name == "record" or name == "monitor-map-name" or name == "cache-active-aging-timeout" or name == "cache-aging-mode" or name == "cache-entries" or name == "cache-inactive-aging-timeout" or name == "cache-timeout-rate-limit" or name == "cache-update-aging-timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "monitor-map-name"):
                    self.monitor_map_name = value
                    self.monitor_map_name.value_namespace = name_space
                    self.monitor_map_name.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-active-aging-timeout"):
                    self.cache_active_aging_timeout = value
                    self.cache_active_aging_timeout.value_namespace = name_space
                    self.cache_active_aging_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-aging-mode"):
                    self.cache_aging_mode = value
                    self.cache_aging_mode.value_namespace = name_space
                    self.cache_aging_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-entries"):
                    self.cache_entries = value
                    self.cache_entries.value_namespace = name_space
                    self.cache_entries.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-inactive-aging-timeout"):
                    self.cache_inactive_aging_timeout = value
                    self.cache_inactive_aging_timeout.value_namespace = name_space
                    self.cache_inactive_aging_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-timeout-rate-limit"):
                    self.cache_timeout_rate_limit = value
                    self.cache_timeout_rate_limit.value_namespace = name_space
                    self.cache_timeout_rate_limit.value_namespace_prefix = name_space_prefix
                if(value_path == "cache-update-aging-timeout"):
                    self.cache_update_aging_timeout = value
                    self.cache_update_aging_timeout.value_namespace = name_space
                    self.cache_update_aging_timeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.flow_monitor_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.flow_monitor_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flow-monitor-map-performance-table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flow-monitor-map"):
                for c in self.flow_monitor_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.flow_monitor_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flow-monitor-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.flow_exporter_maps is not None and self.flow_exporter_maps.has_data()) or
            (self.flow_monitor_map_performance_table is not None and self.flow_monitor_map_performance_table.has_data()) or
            (self.flow_monitor_map_table is not None and self.flow_monitor_map_table.has_data()) or
            (self.flow_sampler_maps is not None and self.flow_sampler_maps.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.flow_exporter_maps is not None and self.flow_exporter_maps.has_operation()) or
            (self.flow_monitor_map_performance_table is not None and self.flow_monitor_map_performance_table.has_operation()) or
            (self.flow_monitor_map_table is not None and self.flow_monitor_map_table.has_operation()) or
            (self.flow_sampler_maps is not None and self.flow_sampler_maps.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow" + path_buffer

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

        if (child_yang_name == "flow-exporter-maps"):
            if (self.flow_exporter_maps is None):
                self.flow_exporter_maps = NetFlow.FlowExporterMaps()
                self.flow_exporter_maps.parent = self
                self._children_name_map["flow_exporter_maps"] = "flow-exporter-maps"
            return self.flow_exporter_maps

        if (child_yang_name == "flow-monitor-map-performance-table"):
            if (self.flow_monitor_map_performance_table is None):
                self.flow_monitor_map_performance_table = NetFlow.FlowMonitorMapPerformanceTable()
                self.flow_monitor_map_performance_table.parent = self
                self._children_name_map["flow_monitor_map_performance_table"] = "flow-monitor-map-performance-table"
            return self.flow_monitor_map_performance_table

        if (child_yang_name == "flow-monitor-map-table"):
            if (self.flow_monitor_map_table is None):
                self.flow_monitor_map_table = NetFlow.FlowMonitorMapTable()
                self.flow_monitor_map_table.parent = self
                self._children_name_map["flow_monitor_map_table"] = "flow-monitor-map-table"
            return self.flow_monitor_map_table

        if (child_yang_name == "flow-sampler-maps"):
            if (self.flow_sampler_maps is None):
                self.flow_sampler_maps = NetFlow.FlowSamplerMaps()
                self.flow_sampler_maps.parent = self
                self._children_name_map["flow_sampler_maps"] = "flow-sampler-maps"
            return self.flow_sampler_maps

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "flow-exporter-maps" or name == "flow-monitor-map-performance-table" or name == "flow-monitor-map-table" or name == "flow-sampler-maps"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NetFlow()
        return self._top_entity

