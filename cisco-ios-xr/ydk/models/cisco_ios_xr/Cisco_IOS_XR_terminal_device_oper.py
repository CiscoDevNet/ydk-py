""" Cisco_IOS_XR_terminal_device_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package operational data.

This module contains definitions
for the following management objects\:
  optical\-interface\: System\-wide view of interface operational
    data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LogicalProtocol(Enum):
    """
    LogicalProtocol (Enum Class)

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
    TribProtocol (Enum Class)

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
    TribRateClass (Enum Class)

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
    	**type**\:  :py:class:`ConfigStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus>`
    
    .. attribute:: optical_channel_interfaces
    
    	The operational attributes for a particular optical channel
    	**type**\:  :py:class:`OpticalChannelInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces>`
    
    .. attribute:: graph
    
    	Table containing Graph Structure and related info
    	**type**\:  :py:class:`Graph <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph>`
    
    .. attribute:: operational_modes
    
    	The Operational Mode Table
    	**type**\:  :py:class:`OperationalModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes>`
    
    .. attribute:: optical_logical_interfaces
    
    	The operational attributes for a logical channel
    	**type**\:  :py:class:`OpticalLogicalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config-status", ("config_status", OpticalInterface.ConfigStatus)), ("optical-channel-interfaces", ("optical_channel_interfaces", OpticalInterface.OpticalChannelInterfaces)), ("graph", ("graph", OpticalInterface.Graph)), ("operational-modes", ("operational_modes", OpticalInterface.OperationalModes)), ("optical-logical-interfaces", ("optical_logical_interfaces", OpticalInterface.OpticalLogicalInterfaces))])
        self._leafs = OrderedDict()

        self.config_status = OpticalInterface.ConfigStatus()
        self.config_status.parent = self
        self._children_name_map["config_status"] = "config-status"

        self.optical_channel_interfaces = OpticalInterface.OpticalChannelInterfaces()
        self.optical_channel_interfaces.parent = self
        self._children_name_map["optical_channel_interfaces"] = "optical-channel-interfaces"

        self.graph = OpticalInterface.Graph()
        self.graph.parent = self
        self._children_name_map["graph"] = "graph"

        self.operational_modes = OpticalInterface.OperationalModes()
        self.operational_modes.parent = self
        self._children_name_map["operational_modes"] = "operational-modes"

        self.optical_logical_interfaces = OpticalInterface.OpticalLogicalInterfaces()
        self.optical_logical_interfaces.parent = self
        self._children_name_map["optical_logical_interfaces"] = "optical-logical-interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OpticalInterface, [], name, value)


    class ConfigStatus(Entity):
        """
        Table containing status information
        
        .. attribute:: partial_config
        
        	The bag containing partial config status
        	**type**\:  :py:class:`PartialConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.PartialConfig>`
        
        .. attribute:: slice_tables
        
        	The container containing slice status information
        	**type**\:  :py:class:`SliceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.ConfigStatus, self).__init__()

            self.yang_name = "config-status"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("partial-config", ("partial_config", OpticalInterface.ConfigStatus.PartialConfig)), ("slice-tables", ("slice_tables", OpticalInterface.ConfigStatus.SliceTables))])
            self._leafs = OrderedDict()

            self.partial_config = OpticalInterface.ConfigStatus.PartialConfig()
            self.partial_config.parent = self
            self._children_name_map["partial_config"] = "partial-config"

            self.slice_tables = OpticalInterface.ConfigStatus.SliceTables()
            self.slice_tables.parent = self
            self._children_name_map["slice_tables"] = "slice-tables"
            self._segment_path = lambda: "config-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.ConfigStatus, [], name, value)


        class PartialConfig(Entity):
            """
            The bag containing partial config status
            
            .. attribute:: partial_config
            
            	PartialConfig
            	**type**\: int
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('partial_config', (YLeaf(YType.uint8, 'partial-config'), ['int'])),
                ])
                self.partial_config = None
                self._segment_path = lambda: "partial-config"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.ConfigStatus.PartialConfig, [u'partial_config'], name, value)


        class SliceTables(Entity):
            """
            The container containing slice status
            information
            
            .. attribute:: slice_table
            
            	The table contains list of slices present
            	**type**\: list of  		 :py:class:`SliceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.ConfigStatus.SliceTables, self).__init__()

                self.yang_name = "slice-tables"
                self.yang_parent_name = "config-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("slice-table", ("slice_table", OpticalInterface.ConfigStatus.SliceTables.SliceTable))])
                self._leafs = OrderedDict()

                self.slice_table = YList(self)
                self._segment_path = lambda: "slice-tables"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables, [], name, value)


            class SliceTable(Entity):
                """
                The table contains list of slices present
                
                .. attribute:: index  (key)
                
                	The index of slice
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: slice_status_attr
                
                	The bag containing slice config status
                	**type**\:  :py:class:`SliceStatusAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.ConfigStatus.SliceTables.SliceTable, self).__init__()

                    self.yang_name = "slice-table"
                    self.yang_parent_name = "slice-tables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['index']
                    self._child_classes = OrderedDict([("slice-status-attr", ("slice_status_attr", OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr))])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                    ])
                    self.index = None

                    self.slice_status_attr = OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr()
                    self.slice_status_attr.parent = self
                    self._children_name_map["slice_status_attr"] = "slice-status-attr"
                    self._segment_path = lambda: "slice-table" + "[index='" + str(self.index) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/slice-tables/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables.SliceTable, ['index'], name, value)


                class SliceStatusAttr(Entity):
                    """
                    The bag containing slice config status
                    
                    .. attribute:: slice
                    
                    	Slice
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: prov_status
                    
                    	ProvStatus
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_config
                    
                    	PresentConfig
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: present_timestamp
                    
                    	PresentTimestamp
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_config
                    
                    	PastConfig
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: past_timestamp
                    
                    	PastTimestamp
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: err_str
                    
                    	ErrStr
                    	**type**\: str
                    
                    	**length:** 0..1024
                    
                    .. attribute:: err_timestamp
                    
                    	ErrTimestamp
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, self).__init__()

                        self.yang_name = "slice-status-attr"
                        self.yang_parent_name = "slice-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('slice', (YLeaf(YType.uint8, 'slice'), ['int'])),
                            ('prov_status', (YLeaf(YType.str, 'prov-status'), ['str'])),
                            ('present_config', (YLeaf(YType.str, 'present-config'), ['str'])),
                            ('present_timestamp', (YLeaf(YType.str, 'present-timestamp'), ['str'])),
                            ('past_config', (YLeaf(YType.str, 'past-config'), ['str'])),
                            ('past_timestamp', (YLeaf(YType.str, 'past-timestamp'), ['str'])),
                            ('err_str', (YLeaf(YType.str, 'err-str'), ['str'])),
                            ('err_timestamp', (YLeaf(YType.str, 'err-timestamp'), ['str'])),
                        ])
                        self.slice = None
                        self.prov_status = None
                        self.present_config = None
                        self.present_timestamp = None
                        self.past_config = None
                        self.past_timestamp = None
                        self.err_str = None
                        self.err_timestamp = None
                        self._segment_path = lambda: "slice-status-attr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, [u'slice', u'prov_status', u'present_config', u'present_timestamp', u'past_config', u'past_timestamp', u'err_str', u'err_timestamp'], name, value)


    class OpticalChannelInterfaces(Entity):
        """
        The operational attributes for a particular
        optical channel
        
        .. attribute:: optical_channel_interface
        
        	The operational attributes for an optical channel
        	**type**\: list of  		 :py:class:`OpticalChannelInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OpticalChannelInterfaces, self).__init__()

            self.yang_name = "optical-channel-interfaces"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("optical-channel-interface", ("optical_channel_interface", OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface))])
            self._leafs = OrderedDict()

            self.optical_channel_interface = YList(self)
            self._segment_path = lambda: "optical-channel-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OpticalChannelInterfaces, [], name, value)


        class OpticalChannelInterface(Entity):
            """
            The operational attributes for an optical
            channel
            
            .. attribute:: location  (key)
            
            	The name of the optical\-channel
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: optical_channel_interface_attr
            
            	The operational attributes for an optical channel
            	**type**\:  :py:class:`OpticalChannelInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, self).__init__()

                self.yang_name = "optical-channel-interface"
                self.yang_parent_name = "optical-channel-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("optical-channel-interface-attr", ("optical_channel_interface_attr", OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.optical_channel_interface_attr = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr()
                self.optical_channel_interface_attr.parent = self
                self._children_name_map["optical_channel_interface_attr"] = "optical-channel-interface-attr"
                self._segment_path = lambda: "optical-channel-interface" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-channel-interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, ['location'], name, value)


            class OpticalChannelInterfaceAttr(Entity):
                """
                The operational attributes for an optical
                channel
                
                .. attribute:: name
                
                	Name
                	**type**\: str
                
                	**length:** 0..128
                
                .. attribute:: index
                
                	Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: frequency
                
                	Frequency
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: power
                
                	Power
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: oper_mode
                
                	OperMode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: line_port
                
                	LinePort
                	**type**\: str
                
                	**length:** 0..128
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, self).__init__()

                    self.yang_name = "optical-channel-interface-attr"
                    self.yang_parent_name = "optical-channel-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('frequency', (YLeaf(YType.uint64, 'frequency'), ['int'])),
                        ('power', (YLeaf(YType.uint64, 'power'), ['int'])),
                        ('oper_mode', (YLeaf(YType.uint32, 'oper-mode'), ['int'])),
                        ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
                    ])
                    self.name = None
                    self.index = None
                    self.frequency = None
                    self.power = None
                    self.oper_mode = None
                    self.line_port = None
                    self._segment_path = lambda: "optical-channel-interface-attr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, [u'name', u'index', u'frequency', u'power', u'oper_mode', u'line_port'], name, value)


    class Graph(Entity):
        """
        Table containing Graph Structure and related
        info
        
        .. attribute:: adj_list_path
        
        	The path containg file which has adjacency list stored
        	**type**\:  :py:class:`AdjListPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.AdjListPath>`
        
        .. attribute:: graph_structure_path
        
        	The path containg file which has graph structure stored
        	**type**\:  :py:class:`GraphStructurePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.Graph.GraphStructurePath>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.Graph, self).__init__()

            self.yang_name = "graph"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("adj-list-path", ("adj_list_path", OpticalInterface.Graph.AdjListPath)), ("graph-structure-path", ("graph_structure_path", OpticalInterface.Graph.GraphStructurePath))])
            self._leafs = OrderedDict()

            self.adj_list_path = OpticalInterface.Graph.AdjListPath()
            self.adj_list_path.parent = self
            self._children_name_map["adj_list_path"] = "adj-list-path"

            self.graph_structure_path = OpticalInterface.Graph.GraphStructurePath()
            self.graph_structure_path.parent = self
            self._children_name_map["graph_structure_path"] = "graph-structure-path"
            self._segment_path = lambda: "graph"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.Graph, [], name, value)


        class AdjListPath(Entity):
            """
            The path containg file which has adjacency list
            stored
            
            .. attribute:: path
            
            	Path
            	**type**\: str
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                ])
                self.path = None
                self._segment_path = lambda: "adj-list-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.Graph.AdjListPath, [u'path'], name, value)


        class GraphStructurePath(Entity):
            """
            The path containg file which has graph
            structure stored
            
            .. attribute:: path
            
            	Path
            	**type**\: str
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                ])
                self.path = None
                self._segment_path = lambda: "graph-structure-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.Graph.GraphStructurePath, [u'path'], name, value)


    class OperationalModes(Entity):
        """
        The Operational Mode Table
        
        .. attribute:: operational_mode
        
        	Mode supported on Device
        	**type**\: list of  		 :py:class:`OperationalMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OperationalModes, self).__init__()

            self.yang_name = "operational-modes"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("operational-mode", ("operational_mode", OpticalInterface.OperationalModes.OperationalMode))])
            self._leafs = OrderedDict()

            self.operational_mode = YList(self)
            self._segment_path = lambda: "operational-modes"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OperationalModes, [], name, value)


        class OperationalMode(Entity):
            """
            Mode supported on Device
            
            .. attribute:: mode_id  (key)
            
            	Mode\-id for supported mode on Device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operational_mode_attributes
            
            	The operational attributes for mxp driver fec\-mode
            	**type**\:  :py:class:`OperationalModeAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OperationalModes.OperationalMode, self).__init__()

                self.yang_name = "operational-mode"
                self.yang_parent_name = "operational-modes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mode_id']
                self._child_classes = OrderedDict([("operational-mode-attributes", ("operational_mode_attributes", OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes))])
                self._leafs = OrderedDict([
                    ('mode_id', (YLeaf(YType.uint32, 'mode-id'), ['int'])),
                ])
                self.mode_id = None

                self.operational_mode_attributes = OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes()
                self.operational_mode_attributes.parent = self
                self._children_name_map["operational_mode_attributes"] = "operational-mode-attributes"
                self._segment_path = lambda: "operational-mode" + "[mode-id='" + str(self.mode_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/operational-modes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OperationalModes.OperationalMode, ['mode_id'], name, value)


            class OperationalModeAttributes(Entity):
                """
                The operational attributes for mxp driver
                fec\-mode
                
                .. attribute:: description
                
                	Description
                	**type**\: str
                
                	**length:** 0..128
                
                .. attribute:: vendor_id
                
                	VendorId
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('vendor_id', (YLeaf(YType.str, 'vendor-id'), ['str'])),
                    ])
                    self.description = None
                    self.vendor_id = None
                    self._segment_path = lambda: "operational-mode-attributes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes, [u'description', u'vendor_id'], name, value)


    class OpticalLogicalInterfaces(Entity):
        """
        The operational attributes for a logical channel
        
        .. attribute:: optical_logical_interface
        
        	The operational attributes for a logical channel
        	**type**\: list of  		 :py:class:`OpticalLogicalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface>`
        
        

        """

        _prefix = 'terminal-device-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(OpticalInterface.OpticalLogicalInterfaces, self).__init__()

            self.yang_name = "optical-logical-interfaces"
            self.yang_parent_name = "optical-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("optical-logical-interface", ("optical_logical_interface", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface))])
            self._leafs = OrderedDict()

            self.optical_logical_interface = YList(self)
            self._segment_path = lambda: "optical-logical-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces, [], name, value)


        class OpticalLogicalInterface(Entity):
            """
            The operational attributes for a logical
            channel
            
            .. attribute:: index  (key)
            
            	The index of the logical\-channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: optical_logical_interface_attr
            
            	The operational attributes for a particular logical channel
            	**type**\:  :py:class:`OpticalLogicalInterfaceAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr>`
            
            .. attribute:: optical_logical_interface_logical_channel_assignments
            
            	The operational attributes for a particular interface
            	**type**\:  :py:class:`OpticalLogicalInterfaceLogicalChannelAssignments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments>`
            
            

            """

            _prefix = 'terminal-device-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, self).__init__()

                self.yang_name = "optical-logical-interface"
                self.yang_parent_name = "optical-logical-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['index']
                self._child_classes = OrderedDict([("optical-logical-interface-attr", ("optical_logical_interface_attr", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr)), ("optical-logical-interface-logical-channel-assignments", ("optical_logical_interface_logical_channel_assignments", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments))])
                self._leafs = OrderedDict([
                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ])
                self.index = None

                self.optical_logical_interface_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr()
                self.optical_logical_interface_attr.parent = self
                self._children_name_map["optical_logical_interface_attr"] = "optical-logical-interface-attr"

                self.optical_logical_interface_logical_channel_assignments = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments()
                self.optical_logical_interface_logical_channel_assignments.parent = self
                self._children_name_map["optical_logical_interface_logical_channel_assignments"] = "optical-logical-interface-logical-channel-assignments"
                self._segment_path = lambda: "optical-logical-interface" + "[index='" + str(self.index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-logical-interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, ['index'], name, value)


            class OpticalLogicalInterfaceAttr(Entity):
                """
                The operational attributes for a particular
                logical channel
                
                .. attribute:: logical_channel_index
                
                	LogicalChannelIndex
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: logical_channel_ifname
                
                	LogicalChannelIfname
                	**type**\: str
                
                	**length:** 0..128
                
                .. attribute:: type
                
                	Type
                	**type**\: str
                
                	**length:** 0..32
                
                .. attribute:: trib_rate_class
                
                	TribRateClass
                	**type**\:  :py:class:`TribRateClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribRateClass>`
                
                .. attribute:: trib_protocol
                
                	TribProtocol
                	**type**\:  :py:class:`TribProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.TribProtocol>`
                
                .. attribute:: protocol_type
                
                	ProtocolType
                	**type**\:  :py:class:`LogicalProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.LogicalProtocol>`
                
                .. attribute:: admin_state
                
                	AdminState
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: loopback_mode
                
                	LoopbackMode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ingress_client_port
                
                	IngressClientPort
                	**type**\: str
                
                	**length:** 0..128
                
                .. attribute:: ingress_physical_channel
                
                	IngressPhysicalChannel
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tti_transmit
                
                	TtiTransmit
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: tti_expected
                
                	TtiExpected
                	**type**\: str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, self).__init__()

                    self.yang_name = "optical-logical-interface-attr"
                    self.yang_parent_name = "optical-logical-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('logical_channel_index', (YLeaf(YType.uint32, 'logical-channel-index'), ['int'])),
                        ('logical_channel_ifname', (YLeaf(YType.str, 'logical-channel-ifname'), ['str'])),
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('trib_rate_class', (YLeaf(YType.enumeration, 'trib-rate-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'TribRateClass', '')])),
                        ('trib_protocol', (YLeaf(YType.enumeration, 'trib-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'TribProtocol', '')])),
                        ('protocol_type', (YLeaf(YType.enumeration, 'protocol-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'LogicalProtocol', '')])),
                        ('admin_state', (YLeaf(YType.uint32, 'admin-state'), ['int'])),
                        ('loopback_mode', (YLeaf(YType.uint32, 'loopback-mode'), ['int'])),
                        ('ingress_client_port', (YLeaf(YType.str, 'ingress-client-port'), ['str'])),
                        ('ingress_physical_channel', (YLeaf(YType.uint32, 'ingress-physical-channel'), ['int'])),
                        ('tti_transmit', (YLeaf(YType.str, 'tti-transmit'), ['str'])),
                        ('tti_expected', (YLeaf(YType.str, 'tti-expected'), ['str'])),
                    ])
                    self.logical_channel_index = None
                    self.logical_channel_ifname = None
                    self.type = None
                    self.trib_rate_class = None
                    self.trib_protocol = None
                    self.protocol_type = None
                    self.admin_state = None
                    self.loopback_mode = None
                    self.ingress_client_port = None
                    self.ingress_physical_channel = None
                    self.tti_transmit = None
                    self.tti_expected = None
                    self._segment_path = lambda: "optical-logical-interface-attr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, [u'logical_channel_index', u'logical_channel_ifname', u'type', u'trib_rate_class', u'trib_protocol', u'protocol_type', u'admin_state', u'loopback_mode', u'ingress_client_port', u'ingress_physical_channel', u'tti_transmit', u'tti_expected'], name, value)


            class OpticalLogicalInterfaceLogicalChannelAssignments(Entity):
                """
                The operational attributes for a particular
                interface
                
                .. attribute:: optical_logical_interface_logical_channel_assignment
                
                	The operational attributes for a logical channel assignment
                	**type**\: list of  		 :py:class:`OpticalLogicalInterfaceLogicalChannelAssignment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment>`
                
                

                """

                _prefix = 'terminal-device-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, self).__init__()

                    self.yang_name = "optical-logical-interface-logical-channel-assignments"
                    self.yang_parent_name = "optical-logical-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("optical-logical-interface-logical-channel-assignment", ("optical_logical_interface_logical_channel_assignment", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment))])
                    self._leafs = OrderedDict()

                    self.optical_logical_interface_logical_channel_assignment = YList(self)
                    self._segment_path = lambda: "optical-logical-interface-logical-channel-assignments"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, [], name, value)


                class OpticalLogicalInterfaceLogicalChannelAssignment(Entity):
                    """
                    The operational attributes for a logical
                    channel assignment
                    
                    .. attribute:: index  (key)
                    
                    	The index of the logical\-channel
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: optical_logical_interface_logical_channel_assignment_attr
                    
                    	The operational attributes for a logical channel assignment
                    	**type**\:  :py:class:`OpticalLogicalInterfaceLogicalChannelAssignmentAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper.OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr>`
                    
                    

                    """

                    _prefix = 'terminal-device-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, self).__init__()

                        self.yang_name = "optical-logical-interface-logical-channel-assignment"
                        self.yang_parent_name = "optical-logical-interface-logical-channel-assignments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([("optical-logical-interface-logical-channel-assignment-attr", ("optical_logical_interface_logical_channel_assignment_attr", OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ])
                        self.index = None

                        self.optical_logical_interface_logical_channel_assignment_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr()
                        self.optical_logical_interface_logical_channel_assignment_attr.parent = self
                        self._children_name_map["optical_logical_interface_logical_channel_assignment_attr"] = "optical-logical-interface-logical-channel-assignment-attr"
                        self._segment_path = lambda: "optical-logical-interface-logical-channel-assignment" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, ['index'], name, value)


                    class OpticalLogicalInterfaceLogicalChannelAssignmentAttr(Entity):
                        """
                        The operational attributes for a logical
                        channel assignment
                        
                        .. attribute:: index
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	Name
                        	**type**\: str
                        
                        	**length:** 0..128
                        
                        .. attribute:: is_logical_link
                        
                        	IsLogicalLink
                        	**type**\: bool
                        
                        .. attribute:: logical_channel
                        
                        	LogicalChannel
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: optical_channel
                        
                        	OpticalChannel
                        	**type**\: str
                        
                        	**length:** 0..128
                        
                        .. attribute:: allocation
                        
                        	Allocation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: assignment_type
                        
                        	AssignmentType
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'terminal-device-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, self).__init__()

                            self.yang_name = "optical-logical-interface-logical-channel-assignment-attr"
                            self.yang_parent_name = "optical-logical-interface-logical-channel-assignment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('is_logical_link', (YLeaf(YType.boolean, 'is-logical-link'), ['bool'])),
                                ('logical_channel', (YLeaf(YType.uint32, 'logical-channel'), ['int'])),
                                ('optical_channel', (YLeaf(YType.str, 'optical-channel'), ['str'])),
                                ('allocation', (YLeaf(YType.uint32, 'allocation'), ['int'])),
                                ('assignment_type', (YLeaf(YType.uint32, 'assignment-type'), ['int'])),
                            ])
                            self.index = None
                            self.name = None
                            self.is_logical_link = None
                            self.logical_channel = None
                            self.optical_channel = None
                            self.allocation = None
                            self.assignment_type = None
                            self._segment_path = lambda: "optical-logical-interface-logical-channel-assignment-attr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, [u'index', u'name', u'is_logical_link', u'logical_channel', u'optical_channel', u'allocation', u'assignment_type'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticalInterface()
        return self._top_entity

