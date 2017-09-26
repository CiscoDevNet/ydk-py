""" Cisco_IOS_XR_terminal_device_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package operational data.

This module contains definitions
for the following management objects\:
  optical\-interface\: System\-wide view of interface operational
    data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LogicalProtocol(Enum):
    """
    LogicalProtocol

    Logical protocol

    .. data:: proto_type_unknown = 0

    	Unknown protocol framing

    .. data:: proto_type_ethernet = 1

    	Ethernet protocol framing

    .. data:: proto_type_otn = 2

    	OTN protocol framing

    """

    proto_type_unknown = Enum.YLeaf(0, "proto-type-unknown")

    proto_type_ethernet = Enum.YLeaf(1, "proto-type-ethernet")

    proto_type_otn = Enum.YLeaf(2, "proto-type-otn")


class TribProtocol(Enum):
    """
    TribProtocol

    Trib protocol

    .. data:: trib_proto_type_unknown = 0

    	Unknown protocol

    .. data:: trib_proto_type1ge = 1

    	1G Ethernet protocol

    .. data:: trib_proto_type_oc48 = 2

    	OC48 protocol

    .. data:: trib_proto_type_stm16 = 3

    	STM 16 protocol

    .. data:: trib_proto_type10gelan = 4

    	10G Ethernet LAN protocol

    .. data:: trib_proto_type10gewan = 5

    	10G Ethernet WAN protocol

    .. data:: trib_proto_type_oc192 = 6

    	OC 192 (9.6GB) port protocol

    .. data:: trib_proto_type_stm64 = 7

    	STM 64 protocol

    .. data:: trib_proto_type_otu2 = 8

    	OTU 2 protocol

    .. data:: trib_proto_type_otu2e = 9

    	OTU 2e protocol

    .. data:: trib_proto_type_otu1e = 10

    	OTU 1e protocol

    .. data:: trib_proto_type_odu2 = 11

    	ODU 2 protocol

    .. data:: trib_proto_type_odu2e = 12

    	ODU 2e protocol

    .. data:: trib_proto_type40ge = 13

    	40G Ethernet port protocol

    .. data:: trib_proto_type_oc768 = 14

    	OC 768 protocol

    .. data:: trib_proto_type_stm256 = 15

    	STM 256 protocol

    .. data:: trib_proto_type_otu3 = 16

    	OTU 3 protocol

    .. data:: trib_proto_type_odu3 = 17

    	ODU 3 protocol

    .. data:: trib_proto_type100ge = 18

    	100G Ethernet protocol

    .. data:: trib_proto_type100g_mlg = 19

    	100G MLG protocol

    .. data:: trib_proto_type_otu4 = 20

    	OTU4 signal protocol (112G) for transporting

    	100GE signal

    .. data:: trib_proto_type_otu_cn = 21

    	OTU Cn protocol

    .. data:: trib_proto_type_odu4 = 22

    	ODU 4 protocol

    """

    trib_proto_type_unknown = Enum.YLeaf(0, "trib-proto-type-unknown")

    trib_proto_type1ge = Enum.YLeaf(1, "trib-proto-type1ge")

    trib_proto_type_oc48 = Enum.YLeaf(2, "trib-proto-type-oc48")

    trib_proto_type_stm16 = Enum.YLeaf(3, "trib-proto-type-stm16")

    trib_proto_type10gelan = Enum.YLeaf(4, "trib-proto-type10gelan")

    trib_proto_type10gewan = Enum.YLeaf(5, "trib-proto-type10gewan")

    trib_proto_type_oc192 = Enum.YLeaf(6, "trib-proto-type-oc192")

    trib_proto_type_stm64 = Enum.YLeaf(7, "trib-proto-type-stm64")

    trib_proto_type_otu2 = Enum.YLeaf(8, "trib-proto-type-otu2")

    trib_proto_type_otu2e = Enum.YLeaf(9, "trib-proto-type-otu2e")

    trib_proto_type_otu1e = Enum.YLeaf(10, "trib-proto-type-otu1e")

    trib_proto_type_odu2 = Enum.YLeaf(11, "trib-proto-type-odu2")

    trib_proto_type_odu2e = Enum.YLeaf(12, "trib-proto-type-odu2e")

    trib_proto_type40ge = Enum.YLeaf(13, "trib-proto-type40ge")

    trib_proto_type_oc768 = Enum.YLeaf(14, "trib-proto-type-oc768")

    trib_proto_type_stm256 = Enum.YLeaf(15, "trib-proto-type-stm256")

    trib_proto_type_otu3 = Enum.YLeaf(16, "trib-proto-type-otu3")

    trib_proto_type_odu3 = Enum.YLeaf(17, "trib-proto-type-odu3")

    trib_proto_type100ge = Enum.YLeaf(18, "trib-proto-type100ge")

    trib_proto_type100g_mlg = Enum.YLeaf(19, "trib-proto-type100g-mlg")

    trib_proto_type_otu4 = Enum.YLeaf(20, "trib-proto-type-otu4")

    trib_proto_type_otu_cn = Enum.YLeaf(21, "trib-proto-type-otu-cn")

    trib_proto_type_odu4 = Enum.YLeaf(22, "trib-proto-type-odu4")


class TribRateClass(Enum):
    """
    TribRateClass

    Trib rate class

    .. data:: trib_rate_unknown = 0

    	Unknown tributary signal rate

    .. data:: trib_rate1g = 1

    	1G tributary signal rate

    .. data:: trib_rate25g = 2

    	2.5G tributary signal rate

    .. data:: trib_rate10g = 3

    	10G tributary signal rate

    .. data:: trib_rate40g = 4

    	40G tributary signal rate

    .. data:: trib_rate100g = 5

    	100G tributary signal rate

    """

    trib_rate_unknown = Enum.YLeaf(0, "trib-rate-unknown")

    trib_rate1g = Enum.YLeaf(1, "trib-rate1g")

    trib_rate25g = Enum.YLeaf(2, "trib-rate25g")

    trib_rate10g = Enum.YLeaf(3, "trib-rate10g")

    trib_rate40g = Enum.YLeaf(4, "trib-rate40g")

    trib_rate100g = Enum.YLeaf(5, "trib-rate100g")



class OpticalInterface(Entity):
    """
    System\-wide view of interface operational data
    
    .. attribute:: config_status
    
    	Table containing status information
    	**type**\:   :py:class:`ConfigStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus>`
    
    .. attribute:: graph
    
    	Table containing Graph Structure and related info
    	**type**\:   :py:class:`Graph <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph>`
    
    .. attribute:: operational_modes
    
    	The Operational Mode Table
    	**type**\:   :py:class:`OperationalModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes>`
    
    .. attribute:: optical_channel_interfaces
    
    	The operational attributes for a particular optical channel
    	**type**\:   :py:class:`OpticalChannelInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces>`
    
    .. attribute:: optical_logical_interfaces
    
    	The operational attributes for a logical channel
    	**type**\:   :py:class:`OpticalLogicalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces>`
    
    

    """

    _prefix = 'terminal-device-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(OpticalInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "optical-interface"
        self.yang_parent_name = "Cisco-IOS-XR-terminal-device-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"config-status" : ("config_status", OpticalInterface.ConfigStatus), "graph" : ("graph", OpticalInterface.Graph), "operational-modes" : ("operational_modes", OpticalInterface.OperationalModes), "optical-channel-interfaces" : ("optical_channel_interfaces", OpticalInterface.OpticalChannelInterfaces), "optical-logical-interfaces" : ("optical_logical_interfaces", OpticalInterface.OpticalLogicalInterfaces)}
        self._child_list_classes = {}

        self.config_status = OpticalInterface.ConfigStatus()
        self.config_status.parent = self
        self._children_name_map["config_status"] = "config-status"
        self._children_yang_names.add("config-status")

        self.graph = OpticalInterface.Graph()
        self.graph.parent = self
        self._children_name_map["graph"] = "graph"
        self._children_yang_names.add("graph")

        self.operational_modes = OpticalInterface.OperationalModes()
        self.operational_modes.parent = self
        self._children_name_map["operational_modes"] = "operational-modes"
        self._children_yang_names.add("operational-modes")

        self.optical_channel_interfaces = OpticalInterface.OpticalChannelInterfaces()
        self.optical_channel_interfaces.parent = self
        self._children_name_map["optical_channel_interfaces"] = "optical-channel-interfaces"
        self._children_yang_names.add("optical-channel-interfaces")

        self.optical_logical_interfaces = OpticalInterface.OpticalLogicalInterfaces()
        self.optical_logical_interfaces.parent = self
        self._children_name_map["optical_logical_interfaces"] = "optical-logical-interfaces"
        self._children_yang_names.add("optical-logical-interfaces")
        self._segment_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface"


    class ConfigStatus(Entity):
        """
        Table containing status information
        
        .. attribute:: partial_config
        
        	The bag containing partial config status
        	**type**\:   :py:class:`PartialConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.PartialConfig>`
        
        .. attribute:: slice_tables
        
        	The container containing slice status information
        	**type**\:   :py:class:`SliceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.ConfigStatus, self).__init__()

            self.yang_name = "config-status"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"partial-config" : ("partial_config", OpticalInterface.ConfigStatus.PartialConfig), "slice-tables" : ("slice_tables", OpticalInterface.ConfigStatus.SliceTables)}
            self._child_list_classes = {}

            self.partial_config = OpticalInterface.ConfigStatus.PartialConfig()
            self.partial_config.parent = self
            self._children_name_map["partial_config"] = "partial-config"
            self._children_yang_names.add("partial-config")

            self.slice_tables = OpticalInterface.ConfigStatus.SliceTables()
            self.slice_tables.parent = self
            self._children_name_map["slice_tables"] = "slice-tables"
            self._children_yang_names.add("slice-tables")
            self._segment_path = lambda: "config-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()


        class PartialConfig(Entity):
            """
            The bag containing partial config status
            
            .. attribute:: partial_config
            
            	PartialConfig
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.ConfigStatus.PartialConfig, self).__init__()

                self.yang_name = "partial-config"
                self.yang_parent_name = "config-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.partial_config = YLeaf(YType.uint8, "partial-config")
                self._segment_path = lambda: "partial-config"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.ConfigStatus.PartialConfig, ['partial_config'], name, value)


        class SliceTables(Entity):
            """
            The container containing slice status
            information
            
            .. attribute:: slice_table
            
            	The table contains list of slices present
            	**type**\: list of    :py:class:`SliceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.ConfigStatus.SliceTables, self).__init__()

                self.yang_name = "slice-tables"
                self.yang_parent_name = "config-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"slice-table" : ("slice_table", OpticalInterface.ConfigStatus.SliceTables.SliceTable)}

                self.slice_table = YList(self)
                self._segment_path = lambda: "slice-tables"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables, [], name, value)


            class SliceTable(Entity):
                """
                The table contains list of slices present
                
                .. attribute:: index  <key>
                
                	The index of slice
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: slice_status_attr
                
                	The bag containing slice config status
                	**type**\:   :py:class:`SliceStatusAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.ConfigStatus.SliceTables.SliceTable, self).__init__()

                    self.yang_name = "slice-table"
                    self.yang_parent_name = "slice-tables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"slice-status-attr" : ("slice_status_attr", OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr)}
                    self._child_list_classes = {}

                    self.index = YLeaf(YType.int32, "index")

                    self.slice_status_attr = OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr()
                    self.slice_status_attr.parent = self
                    self._children_name_map["slice_status_attr"] = "slice-status-attr"
                    self._children_yang_names.add("slice-status-attr")
                    self._segment_path = lambda: "slice-table" + "[index='" + self.index.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/slice-tables/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables.SliceTable, ['index'], name, value)


                class SliceStatusAttr(Entity):
                    """
                    The bag containing slice config status
                    
                    .. attribute:: err_str
                    
                    	ErrStr
                    	**type**\:  str
                    
                    	**length:** 0..1024
                    
                    .. attribute:: err_timestamp
                    
                    	ErrTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_config
                    
                    	PastConfig
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_timestamp
                    
                    	PastTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_config
                    
                    	PresentConfig
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_timestamp
                    
                    	PresentTimestamp
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prov_status
                    
                    	ProvStatus
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: slice
                    
                    	Slice
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, self).__init__()

                        self.yang_name = "slice-status-attr"
                        self.yang_parent_name = "slice-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.err_str = YLeaf(YType.str, "err-str")

                        self.err_timestamp = YLeaf(YType.str, "err-timestamp")

                        self.past_config = YLeaf(YType.str, "past-config")

                        self.past_timestamp = YLeaf(YType.str, "past-timestamp")

                        self.present_config = YLeaf(YType.str, "present-config")

                        self.present_timestamp = YLeaf(YType.str, "present-timestamp")

                        self.prov_status = YLeaf(YType.str, "prov-status")

                        self.slice = YLeaf(YType.uint8, "slice")
                        self._segment_path = lambda: "slice-status-attr"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, ['err_str', 'err_timestamp', 'past_config', 'past_timestamp', 'present_config', 'present_timestamp', 'prov_status', 'slice'], name, value)


    class Graph(Entity):
        """
        Table containing Graph Structure and related
        info
        
        .. attribute:: adj_list_path
        
        	The path containg file which has adjacency list stored
        	**type**\:   :py:class:`AdjListPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.AdjListPath>`
        
        .. attribute:: graph_structure_path
        
        	The path containg file which has graph structure stored
        	**type**\:   :py:class:`GraphStructurePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.GraphStructurePath>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.Graph, self).__init__()

            self.yang_name = "graph"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"adj-list-path" : ("adj_list_path", OpticalInterface.Graph.AdjListPath), "graph-structure-path" : ("graph_structure_path", OpticalInterface.Graph.GraphStructurePath)}
            self._child_list_classes = {}

            self.adj_list_path = OpticalInterface.Graph.AdjListPath()
            self.adj_list_path.parent = self
            self._children_name_map["adj_list_path"] = "adj-list-path"
            self._children_yang_names.add("adj-list-path")

            self.graph_structure_path = OpticalInterface.Graph.GraphStructurePath()
            self.graph_structure_path.parent = self
            self._children_name_map["graph_structure_path"] = "graph-structure-path"
            self._children_yang_names.add("graph-structure-path")
            self._segment_path = lambda: "graph"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()


        class AdjListPath(Entity):
            """
            The path containg file which has adjacency list
            stored
            
            .. attribute:: path
            
            	Path
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.Graph.AdjListPath, self).__init__()

                self.yang_name = "adj-list-path"
                self.yang_parent_name = "graph"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.path = YLeaf(YType.str, "path")
                self._segment_path = lambda: "adj-list-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.Graph.AdjListPath, ['path'], name, value)


        class GraphStructurePath(Entity):
            """
            The path containg file which has graph
            structure stored
            
            .. attribute:: path
            
            	Path
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.Graph.GraphStructurePath, self).__init__()

                self.yang_name = "graph-structure-path"
                self.yang_parent_name = "graph"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.path = YLeaf(YType.str, "path")
                self._segment_path = lambda: "graph-structure-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.Graph.GraphStructurePath, ['path'], name, value)


    class OperationalModes(Entity):
        """
        The Operational Mode Table
        
        .. attribute:: operational_mode
        
        	Mode supported on Device
        	**type**\: list of    :py:class:`OperationalMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OperationalModes, self).__init__()

            self.yang_name = "operational-modes"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"operational-mode" : ("operational_mode", OpticalInterface.OperationalModes.OperationalMode)}

            self.operational_mode = YList(self)
            self._segment_path = lambda: "operational-modes"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OperationalModes, [], name, value)


        class OperationalMode(Entity):
            """
            Mode supported on Device
            
            .. attribute:: mode_id  <key>
            
            	Mode\-id for supported mode on Device
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: operational_mode_attributes
            
            	The operational attributes for mxp driver fec\-mode
            	**type**\:   :py:class:`OperationalModeAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OperationalModes.OperationalMode, self).__init__()

                self.yang_name = "operational-mode"
                self.yang_parent_name = "operational-modes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"operational-mode-attributes" : ("operational_mode_attributes", OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes)}
                self._child_list_classes = {}

                self.mode_id = YLeaf(YType.int32, "mode-id")

                self.operational_mode_attributes = OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes()
                self.operational_mode_attributes.parent = self
                self._children_name_map["operational_mode_attributes"] = "operational-mode-attributes"
                self._children_yang_names.add("operational-mode-attributes")
                self._segment_path = lambda: "operational-mode" + "[mode-id='" + self.mode_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/operational-modes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OperationalModes.OperationalMode, ['mode_id'], name, value)


            class OperationalModeAttributes(Entity):
                """
                The operational attributes for mxp driver
                fec\-mode
                
                .. attribute:: description
                
                	Description
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: vendor_id
                
                	VendorId
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes, self).__init__()

                    self.yang_name = "operational-mode-attributes"
                    self.yang_parent_name = "operational-mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.description = YLeaf(YType.str, "description")

                    self.vendor_id = YLeaf(YType.str, "vendor-id")
                    self._segment_path = lambda: "operational-mode-attributes"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes, ['description', 'vendor_id'], name, value)


    class OpticalChannelInterfaces(Entity):
        """
        The operational attributes for a particular
        optical channel
        
        .. attribute:: optical_channel_interface
        
        	The operational attributes for an optical channel
        	**type**\: list of    :py:class:`OpticalChannelInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OpticalChannelInterfaces, self).__init__()

            self.yang_name = "optical-channel-interfaces"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"optical-channel-interface" : ("optical_channel_interface", OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface)}

            self.optical_channel_interface = YList(self)
            self._segment_path = lambda: "optical-channel-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OpticalChannelInterfaces, [], name, value)


        class OpticalChannelInterface(Entity):
            """
            The operational attributes for an optical
            channel
            
            .. attribute:: location  <key>
            
            	The name of the optical\-channel
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: optical_channel_interface_attr
            
            	The operational attributes for an optical channel
            	**type**\:   :py:class:`OpticalChannelInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, self).__init__()

                self.yang_name = "optical-channel-interface"
                self.yang_parent_name = "optical-channel-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"optical-channel-interface-attr" : ("optical_channel_interface_attr", OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr)}
                self._child_list_classes = {}

                self.location = YLeaf(YType.str, "location")

                self.optical_channel_interface_attr = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr()
                self.optical_channel_interface_attr.parent = self
                self._children_name_map["optical_channel_interface_attr"] = "optical-channel-interface-attr"
                self._children_yang_names.add("optical-channel-interface-attr")
                self._segment_path = lambda: "optical-channel-interface" + "[location='" + self.location.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-channel-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, ['location'], name, value)


            class OpticalChannelInterfaceAttr(Entity):
                """
                The operational attributes for an optical
                channel
                
                .. attribute:: frequency
                
                	Frequency
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: index
                
                	Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_port
                
                	LinePort
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: name
                
                	Name
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: oper_mode
                
                	OperMode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: power
                
                	Power
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, self).__init__()

                    self.yang_name = "optical-channel-interface-attr"
                    self.yang_parent_name = "optical-channel-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.frequency = YLeaf(YType.uint64, "frequency")

                    self.index = YLeaf(YType.uint32, "index")

                    self.line_port = YLeaf(YType.str, "line-port")

                    self.name = YLeaf(YType.str, "name")

                    self.oper_mode = YLeaf(YType.uint32, "oper-mode")

                    self.power = YLeaf(YType.uint64, "power")
                    self._segment_path = lambda: "optical-channel-interface-attr"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, ['frequency', 'index', 'line_port', 'name', 'oper_mode', 'power'], name, value)


    class OpticalLogicalInterfaces(Entity):
        """
        The operational attributes for a logical channel
        
        .. attribute:: optical_logical_interface
        
        	The operational attributes for a logical channel
        	**type**\: list of    :py:class:`OpticalLogicalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OpticalLogicalInterfaces, self).__init__()

            self.yang_name = "optical-logical-interfaces"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"optical-logical-interface" : ("optical_logical_interface", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface)}

            self.optical_logical_interface = YList(self)
            self._segment_path = lambda: "optical-logical-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces, [], name, value)


        class OpticalLogicalInterface(Entity):
            """
            The operational attributes for a logical
            channel
            
            .. attribute:: index  <key>
            
            	The index of the logical\-channel
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: optical_logical_interface_attr
            
            	The operational attributes for a particular logical channel
            	**type**\:   :py:class:`OpticalLogicalInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr>`
            
            .. attribute:: optical_logical_interface_logical_channel_assignments
            
            	The operational attributes for a particular interface
            	**type**\:   :py:class:`OpticalLogicalInterfaceLogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, self).__init__()

                self.yang_name = "optical-logical-interface"
                self.yang_parent_name = "optical-logical-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"optical-logical-interface-attr" : ("optical_logical_interface_attr", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr), "optical-logical-interface-logical-channel-assignments" : ("optical_logical_interface_logical_channel_assignments", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments)}
                self._child_list_classes = {}

                self.index = YLeaf(YType.int32, "index")

                self.optical_logical_interface_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr()
                self.optical_logical_interface_attr.parent = self
                self._children_name_map["optical_logical_interface_attr"] = "optical-logical-interface-attr"
                self._children_yang_names.add("optical-logical-interface-attr")

                self.optical_logical_interface_logical_channel_assignments = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments()
                self.optical_logical_interface_logical_channel_assignments.parent = self
                self._children_name_map["optical_logical_interface_logical_channel_assignments"] = "optical-logical-interface-logical-channel-assignments"
                self._children_yang_names.add("optical-logical-interface-logical-channel-assignments")
                self._segment_path = lambda: "optical-logical-interface" + "[index='" + self.index.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-logical-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, ['index'], name, value)


            class OpticalLogicalInterfaceAttr(Entity):
                """
                The operational attributes for a particular
                logical channel
                
                .. attribute:: admin_state
                
                	AdminState
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ingress_client_port
                
                	IngressClientPort
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: ingress_physical_channel
                
                	IngressPhysicalChannel
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: logical_channel_ifname
                
                	LogicalChannelIfname
                	**type**\:  str
                
                	**length:** 0..128
                
                .. attribute:: logical_channel_index
                
                	LogicalChannelIndex
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loopback_mode
                
                	LoopbackMode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	ProtocolType
                	**type**\:   :py:class:`LogicalProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.LogicalProtocol>`
                
                .. attribute:: trib_protocol
                
                	TribProtocol
                	**type**\:   :py:class:`TribProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribProtocol>`
                
                .. attribute:: trib_rate_class
                
                	TribRateClass
                	**type**\:   :py:class:`TribRateClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribRateClass>`
                
                .. attribute:: tti_expected
                
                	TtiExpected
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: tti_transmit
                
                	TtiTransmit
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: type
                
                	Type
                	**type**\:  str
                
                	**length:** 0..32
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, self).__init__()

                    self.yang_name = "optical-logical-interface-attr"
                    self.yang_parent_name = "optical-logical-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_state = YLeaf(YType.uint32, "admin-state")

                    self.ingress_client_port = YLeaf(YType.str, "ingress-client-port")

                    self.ingress_physical_channel = YLeaf(YType.uint32, "ingress-physical-channel")

                    self.logical_channel_ifname = YLeaf(YType.str, "logical-channel-ifname")

                    self.logical_channel_index = YLeaf(YType.uint32, "logical-channel-index")

                    self.loopback_mode = YLeaf(YType.uint32, "loopback-mode")

                    self.protocol_type = YLeaf(YType.enumeration, "protocol-type")

                    self.trib_protocol = YLeaf(YType.enumeration, "trib-protocol")

                    self.trib_rate_class = YLeaf(YType.enumeration, "trib-rate-class")

                    self.tti_expected = YLeaf(YType.str, "tti-expected")

                    self.tti_transmit = YLeaf(YType.str, "tti-transmit")

                    self.type = YLeaf(YType.str, "type")
                    self._segment_path = lambda: "optical-logical-interface-attr"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, ['admin_state', 'ingress_client_port', 'ingress_physical_channel', 'logical_channel_ifname', 'logical_channel_index', 'loopback_mode', 'protocol_type', 'trib_protocol', 'trib_rate_class', 'tti_expected', 'tti_transmit', 'type'], name, value)


            class OpticalLogicalInterfaceLogicalChannelAssignments(Entity):
                """
                The operational attributes for a particular
                interface
                
                .. attribute:: optical_logical_interface_logical_channel_assignment
                
                	The operational attributes for a logical channel assignment
                	**type**\: list of    :py:class:`OpticalLogicalInterfaceLogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, self).__init__()

                    self.yang_name = "optical-logical-interface-logical-channel-assignments"
                    self.yang_parent_name = "optical-logical-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"optical-logical-interface-logical-channel-assignment" : ("optical_logical_interface_logical_channel_assignment", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment)}

                    self.optical_logical_interface_logical_channel_assignment = YList(self)
                    self._segment_path = lambda: "optical-logical-interface-logical-channel-assignments"

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, [], name, value)


                class OpticalLogicalInterfaceLogicalChannelAssignment(Entity):
                    """
                    The operational attributes for a logical
                    channel assignment
                    
                    .. attribute:: index  <key>
                    
                    	The index of the logical\-channel
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: optical_logical_interface_logical_channel_assignment_attr
                    
                    	The operational attributes for a logical channel assignment
                    	**type**\:   :py:class:`OpticalLogicalInterfaceLogicalChannelAssignmentAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr>`
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, self).__init__()

                        self.yang_name = "optical-logical-interface-logical-channel-assignment"
                        self.yang_parent_name = "optical-logical-interface-logical-channel-assignments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"optical-logical-interface-logical-channel-assignment-attr" : ("optical_logical_interface_logical_channel_assignment_attr", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr)}
                        self._child_list_classes = {}

                        self.index = YLeaf(YType.int32, "index")

                        self.optical_logical_interface_logical_channel_assignment_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr()
                        self.optical_logical_interface_logical_channel_assignment_attr.parent = self
                        self._children_name_map["optical_logical_interface_logical_channel_assignment_attr"] = "optical-logical-interface-logical-channel-assignment-attr"
                        self._children_yang_names.add("optical-logical-interface-logical-channel-assignment-attr")
                        self._segment_path = lambda: "optical-logical-interface-logical-channel-assignment" + "[index='" + self.index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, ['index'], name, value)


                    class OpticalLogicalInterfaceLogicalChannelAssignmentAttr(Entity):
                        """
                        The operational attributes for a logical
                        channel assignment
                        
                        .. attribute:: allocation
                        
                        	Allocation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: assignment_type
                        
                        	AssignmentType
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_logical_link
                        
                        	IsLogicalLink
                        	**type**\:  bool
                        
                        .. attribute:: logical_channel
                        
                        	LogicalChannel
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	Name
                        	**type**\:  str
                        
                        	**length:** 0..128
                        
                        .. attribute:: optical_channel
                        
                        	OpticalChannel
                        	**type**\:  str
                        
                        	**length:** 0..128
                        
                        

                        """

                        _prefix = 'terminal-device-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, self).__init__()

                            self.yang_name = "optical-logical-interface-logical-channel-assignment-attr"
                            self.yang_parent_name = "optical-logical-interface-logical-channel-assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.allocation = YLeaf(YType.uint32, "allocation")

                            self.assignment_type = YLeaf(YType.uint32, "assignment-type")

                            self.index = YLeaf(YType.uint32, "index")

                            self.is_logical_link = YLeaf(YType.boolean, "is-logical-link")

                            self.logical_channel = YLeaf(YType.uint32, "logical-channel")

                            self.name = YLeaf(YType.str, "name")

                            self.optical_channel = YLeaf(YType.str, "optical-channel")
                            self._segment_path = lambda: "optical-logical-interface-logical-channel-assignment-attr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, ['allocation', 'assignment_type', 'index', 'is_logical_link', 'logical_channel', 'name', 'optical_channel'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticalInterface()
        return self._top_entity

