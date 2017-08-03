""" Cisco_IOS_XR_terminal_device_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR terminal\-device package operational data.

This module contains definitions
for the following management objects\:
  optical\-interface\: System\-wide view of interface operational
    data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.partial_config = OpticalInterface.ConfigStatus.PartialConfig()
            self.partial_config.parent = self
            self._children_name_map["partial_config"] = "partial-config"
            self._children_yang_names.add("partial-config")

            self.slice_tables = OpticalInterface.ConfigStatus.SliceTables()
            self.slice_tables.parent = self
            self._children_name_map["slice_tables"] = "slice-tables"
            self._children_yang_names.add("slice-tables")


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

                self.partial_config = YLeaf(YType.uint8, "partial-config")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("partial_config") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.ConfigStatus.PartialConfig, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.ConfigStatus.PartialConfig, self).__setattr__(name, value)

            def has_data(self):
                return self.partial_config.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.partial_config.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "partial-config" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.partial_config.is_set or self.partial_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.partial_config.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "partial-config"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "partial-config"):
                    self.partial_config = value
                    self.partial_config.value_namespace = name_space
                    self.partial_config.value_namespace_prefix = name_space_prefix


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

                self.slice_table = YList(self)

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
                            super(OpticalInterface.ConfigStatus.SliceTables, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.ConfigStatus.SliceTables, self).__setattr__(name, value)


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

                    self.index = YLeaf(YType.int32, "index")

                    self.slice_status_attr = OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr()
                    self.slice_status_attr.parent = self
                    self._children_name_map["slice_status_attr"] = "slice-status-attr"
                    self._children_yang_names.add("slice-status-attr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("index") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticalInterface.ConfigStatus.SliceTables.SliceTable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticalInterface.ConfigStatus.SliceTables.SliceTable, self).__setattr__(name, value)


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

                        self.err_str = YLeaf(YType.str, "err-str")

                        self.err_timestamp = YLeaf(YType.str, "err-timestamp")

                        self.past_config = YLeaf(YType.str, "past-config")

                        self.past_timestamp = YLeaf(YType.str, "past-timestamp")

                        self.present_config = YLeaf(YType.str, "present-config")

                        self.present_timestamp = YLeaf(YType.str, "present-timestamp")

                        self.prov_status = YLeaf(YType.str, "prov-status")

                        self.slice = YLeaf(YType.uint8, "slice")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("err_str",
                                        "err_timestamp",
                                        "past_config",
                                        "past_timestamp",
                                        "present_config",
                                        "present_timestamp",
                                        "prov_status",
                                        "slice") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.err_str.is_set or
                            self.err_timestamp.is_set or
                            self.past_config.is_set or
                            self.past_timestamp.is_set or
                            self.present_config.is_set or
                            self.present_timestamp.is_set or
                            self.prov_status.is_set or
                            self.slice.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.err_str.yfilter != YFilter.not_set or
                            self.err_timestamp.yfilter != YFilter.not_set or
                            self.past_config.yfilter != YFilter.not_set or
                            self.past_timestamp.yfilter != YFilter.not_set or
                            self.present_config.yfilter != YFilter.not_set or
                            self.present_timestamp.yfilter != YFilter.not_set or
                            self.prov_status.yfilter != YFilter.not_set or
                            self.slice.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slice-status-attr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.err_str.is_set or self.err_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.err_str.get_name_leafdata())
                        if (self.err_timestamp.is_set or self.err_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.err_timestamp.get_name_leafdata())
                        if (self.past_config.is_set or self.past_config.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.past_config.get_name_leafdata())
                        if (self.past_timestamp.is_set or self.past_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.past_timestamp.get_name_leafdata())
                        if (self.present_config.is_set or self.present_config.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.present_config.get_name_leafdata())
                        if (self.present_timestamp.is_set or self.present_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.present_timestamp.get_name_leafdata())
                        if (self.prov_status.is_set or self.prov_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prov_status.get_name_leafdata())
                        if (self.slice.is_set or self.slice.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slice.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "err-str" or name == "err-timestamp" or name == "past-config" or name == "past-timestamp" or name == "present-config" or name == "present-timestamp" or name == "prov-status" or name == "slice"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "err-str"):
                            self.err_str = value
                            self.err_str.value_namespace = name_space
                            self.err_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "err-timestamp"):
                            self.err_timestamp = value
                            self.err_timestamp.value_namespace = name_space
                            self.err_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "past-config"):
                            self.past_config = value
                            self.past_config.value_namespace = name_space
                            self.past_config.value_namespace_prefix = name_space_prefix
                        if(value_path == "past-timestamp"):
                            self.past_timestamp = value
                            self.past_timestamp.value_namespace = name_space
                            self.past_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "present-config"):
                            self.present_config = value
                            self.present_config.value_namespace = name_space
                            self.present_config.value_namespace_prefix = name_space_prefix
                        if(value_path == "present-timestamp"):
                            self.present_timestamp = value
                            self.present_timestamp.value_namespace = name_space
                            self.present_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "prov-status"):
                            self.prov_status = value
                            self.prov_status.value_namespace = name_space
                            self.prov_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "slice"):
                            self.slice = value
                            self.slice.value_namespace = name_space
                            self.slice.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.index.is_set or
                        (self.slice_status_attr is not None and self.slice_status_attr.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        (self.slice_status_attr is not None and self.slice_status_attr.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slice-table" + "[index='" + self.index.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/slice-tables/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slice-status-attr"):
                        if (self.slice_status_attr is None):
                            self.slice_status_attr = OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr()
                            self.slice_status_attr.parent = self
                            self._children_name_map["slice_status_attr"] = "slice-status-attr"
                        return self.slice_status_attr

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slice-status-attr" or name == "index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.slice_table:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.slice_table:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "slice-tables" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/config-status/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slice-table"):
                    for c in self.slice_table:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = OpticalInterface.ConfigStatus.SliceTables.SliceTable()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.slice_table.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slice-table"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.partial_config is not None and self.partial_config.has_data()) or
                (self.slice_tables is not None and self.slice_tables.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.partial_config is not None and self.partial_config.has_operation()) or
                (self.slice_tables is not None and self.slice_tables.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "config-status" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "partial-config"):
                if (self.partial_config is None):
                    self.partial_config = OpticalInterface.ConfigStatus.PartialConfig()
                    self.partial_config.parent = self
                    self._children_name_map["partial_config"] = "partial-config"
                return self.partial_config

            if (child_yang_name == "slice-tables"):
                if (self.slice_tables is None):
                    self.slice_tables = OpticalInterface.ConfigStatus.SliceTables()
                    self.slice_tables.parent = self
                    self._children_name_map["slice_tables"] = "slice-tables"
                return self.slice_tables

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "partial-config" or name == "slice-tables"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.optical_channel_interface = YList(self)

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
                        super(OpticalInterface.OpticalChannelInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OpticalInterface.OpticalChannelInterfaces, self).__setattr__(name, value)


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

                self.location = YLeaf(YType.str, "location")

                self.optical_channel_interface_attr = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr()
                self.optical_channel_interface_attr.parent = self
                self._children_name_map["optical_channel_interface_attr"] = "optical-channel-interface-attr"
                self._children_yang_names.add("optical-channel-interface-attr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("location") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface, self).__setattr__(name, value)


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

                    self.frequency = YLeaf(YType.uint64, "frequency")

                    self.index = YLeaf(YType.uint32, "index")

                    self.line_port = YLeaf(YType.str, "line-port")

                    self.name = YLeaf(YType.str, "name")

                    self.oper_mode = YLeaf(YType.uint32, "oper-mode")

                    self.power = YLeaf(YType.uint64, "power")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("frequency",
                                    "index",
                                    "line_port",
                                    "name",
                                    "oper_mode",
                                    "power") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.frequency.is_set or
                        self.index.is_set or
                        self.line_port.is_set or
                        self.name.is_set or
                        self.oper_mode.is_set or
                        self.power.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.frequency.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.line_port.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.oper_mode.yfilter != YFilter.not_set or
                        self.power.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optical-channel-interface-attr" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.frequency.is_set or self.frequency.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.frequency.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.line_port.is_set or self.line_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_port.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.oper_mode.is_set or self.oper_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oper_mode.get_name_leafdata())
                    if (self.power.is_set or self.power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.power.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "frequency" or name == "index" or name == "line-port" or name == "name" or name == "oper-mode" or name == "power"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "frequency"):
                        self.frequency = value
                        self.frequency.value_namespace = name_space
                        self.frequency.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-port"):
                        self.line_port = value
                        self.line_port.value_namespace = name_space
                        self.line_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "oper-mode"):
                        self.oper_mode = value
                        self.oper_mode.value_namespace = name_space
                        self.oper_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "power"):
                        self.power = value
                        self.power.value_namespace = name_space
                        self.power.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.location.is_set or
                    (self.optical_channel_interface_attr is not None and self.optical_channel_interface_attr.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    (self.optical_channel_interface_attr is not None and self.optical_channel_interface_attr.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "optical-channel-interface" + "[location='" + self.location.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-channel-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "optical-channel-interface-attr"):
                    if (self.optical_channel_interface_attr is None):
                        self.optical_channel_interface_attr = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr()
                        self.optical_channel_interface_attr.parent = self
                        self._children_name_map["optical_channel_interface_attr"] = "optical-channel-interface-attr"
                    return self.optical_channel_interface_attr

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "optical-channel-interface-attr" or name == "location"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.optical_channel_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.optical_channel_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "optical-channel-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "optical-channel-interface"):
                for c in self.optical_channel_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.optical_channel_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "optical-channel-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.adj_list_path = OpticalInterface.Graph.AdjListPath()
            self.adj_list_path.parent = self
            self._children_name_map["adj_list_path"] = "adj-list-path"
            self._children_yang_names.add("adj-list-path")

            self.graph_structure_path = OpticalInterface.Graph.GraphStructurePath()
            self.graph_structure_path.parent = self
            self._children_name_map["graph_structure_path"] = "graph-structure-path"
            self._children_yang_names.add("graph-structure-path")


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

                self.path = YLeaf(YType.str, "path")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("path") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.Graph.AdjListPath, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.Graph.AdjListPath, self).__setattr__(name, value)

            def has_data(self):
                return self.path.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.path.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "adj-list-path" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "path"):
                    self.path = value
                    self.path.value_namespace = name_space
                    self.path.value_namespace_prefix = name_space_prefix


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

                self.path = YLeaf(YType.str, "path")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("path") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.Graph.GraphStructurePath, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.Graph.GraphStructurePath, self).__setattr__(name, value)

            def has_data(self):
                return self.path.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.path.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "graph-structure-path" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/graph/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "path"):
                    self.path = value
                    self.path.value_namespace = name_space
                    self.path.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.adj_list_path is not None and self.adj_list_path.has_data()) or
                (self.graph_structure_path is not None and self.graph_structure_path.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.adj_list_path is not None and self.adj_list_path.has_operation()) or
                (self.graph_structure_path is not None and self.graph_structure_path.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "graph" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "adj-list-path"):
                if (self.adj_list_path is None):
                    self.adj_list_path = OpticalInterface.Graph.AdjListPath()
                    self.adj_list_path.parent = self
                    self._children_name_map["adj_list_path"] = "adj-list-path"
                return self.adj_list_path

            if (child_yang_name == "graph-structure-path"):
                if (self.graph_structure_path is None):
                    self.graph_structure_path = OpticalInterface.Graph.GraphStructurePath()
                    self.graph_structure_path.parent = self
                    self._children_name_map["graph_structure_path"] = "graph-structure-path"
                return self.graph_structure_path

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "adj-list-path" or name == "graph-structure-path"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.operational_mode = YList(self)

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
                        super(OpticalInterface.OperationalModes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OpticalInterface.OperationalModes, self).__setattr__(name, value)


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

                self.mode_id = YLeaf(YType.int32, "mode-id")

                self.operational_mode_attributes = OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes()
                self.operational_mode_attributes.parent = self
                self._children_name_map["operational_mode_attributes"] = "operational-mode-attributes"
                self._children_yang_names.add("operational-mode-attributes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mode_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.OperationalModes.OperationalMode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.OperationalModes.OperationalMode, self).__setattr__(name, value)


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

                    self.description = YLeaf(YType.str, "description")

                    self.vendor_id = YLeaf(YType.str, "vendor-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("description",
                                    "vendor_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.description.is_set or
                        self.vendor_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.vendor_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "operational-mode-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.vendor_id.is_set or self.vendor_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vendor_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "description" or name == "vendor-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "vendor-id"):
                        self.vendor_id = value
                        self.vendor_id.value_namespace = name_space
                        self.vendor_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.mode_id.is_set or
                    (self.operational_mode_attributes is not None and self.operational_mode_attributes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mode_id.yfilter != YFilter.not_set or
                    (self.operational_mode_attributes is not None and self.operational_mode_attributes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "operational-mode" + "[mode-id='" + self.mode_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/operational-modes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mode_id.is_set or self.mode_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "operational-mode-attributes"):
                    if (self.operational_mode_attributes is None):
                        self.operational_mode_attributes = OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes()
                        self.operational_mode_attributes.parent = self
                        self._children_name_map["operational_mode_attributes"] = "operational-mode-attributes"
                    return self.operational_mode_attributes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "operational-mode-attributes" or name == "mode-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mode-id"):
                    self.mode_id = value
                    self.mode_id.value_namespace = name_space
                    self.mode_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.operational_mode:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.operational_mode:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "operational-modes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "operational-mode"):
                for c in self.operational_mode:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OpticalInterface.OperationalModes.OperationalMode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.operational_mode.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "operational-mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.optical_logical_interface = YList(self)

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
                        super(OpticalInterface.OpticalLogicalInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OpticalInterface.OpticalLogicalInterfaces, self).__setattr__(name, value)


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

                self.index = YLeaf(YType.int32, "index")

                self.optical_logical_interface_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr()
                self.optical_logical_interface_attr.parent = self
                self._children_name_map["optical_logical_interface_attr"] = "optical-logical-interface-attr"
                self._children_yang_names.add("optical-logical-interface-attr")

                self.optical_logical_interface_logical_channel_assignments = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments()
                self.optical_logical_interface_logical_channel_assignments.parent = self
                self._children_name_map["optical_logical_interface_logical_channel_assignments"] = "optical-logical-interface-logical-channel-assignments"
                self._children_yang_names.add("optical-logical-interface-logical-channel-assignments")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("index") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("admin_state",
                                    "ingress_client_port",
                                    "ingress_physical_channel",
                                    "logical_channel_ifname",
                                    "logical_channel_index",
                                    "loopback_mode",
                                    "protocol_type",
                                    "trib_protocol",
                                    "trib_rate_class",
                                    "tti_expected",
                                    "tti_transmit",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.admin_state.is_set or
                        self.ingress_client_port.is_set or
                        self.ingress_physical_channel.is_set or
                        self.logical_channel_ifname.is_set or
                        self.logical_channel_index.is_set or
                        self.loopback_mode.is_set or
                        self.protocol_type.is_set or
                        self.trib_protocol.is_set or
                        self.trib_rate_class.is_set or
                        self.tti_expected.is_set or
                        self.tti_transmit.is_set or
                        self.type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.admin_state.yfilter != YFilter.not_set or
                        self.ingress_client_port.yfilter != YFilter.not_set or
                        self.ingress_physical_channel.yfilter != YFilter.not_set or
                        self.logical_channel_ifname.yfilter != YFilter.not_set or
                        self.logical_channel_index.yfilter != YFilter.not_set or
                        self.loopback_mode.yfilter != YFilter.not_set or
                        self.protocol_type.yfilter != YFilter.not_set or
                        self.trib_protocol.yfilter != YFilter.not_set or
                        self.trib_rate_class.yfilter != YFilter.not_set or
                        self.tti_expected.yfilter != YFilter.not_set or
                        self.tti_transmit.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optical-logical-interface-attr" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.admin_state.get_name_leafdata())
                    if (self.ingress_client_port.is_set or self.ingress_client_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ingress_client_port.get_name_leafdata())
                    if (self.ingress_physical_channel.is_set or self.ingress_physical_channel.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ingress_physical_channel.get_name_leafdata())
                    if (self.logical_channel_ifname.is_set or self.logical_channel_ifname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logical_channel_ifname.get_name_leafdata())
                    if (self.logical_channel_index.is_set or self.logical_channel_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logical_channel_index.get_name_leafdata())
                    if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                    if (self.protocol_type.is_set or self.protocol_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_type.get_name_leafdata())
                    if (self.trib_protocol.is_set or self.trib_protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trib_protocol.get_name_leafdata())
                    if (self.trib_rate_class.is_set or self.trib_rate_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trib_rate_class.get_name_leafdata())
                    if (self.tti_expected.is_set or self.tti_expected.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tti_expected.get_name_leafdata())
                    if (self.tti_transmit.is_set or self.tti_transmit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tti_transmit.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "admin-state" or name == "ingress-client-port" or name == "ingress-physical-channel" or name == "logical-channel-ifname" or name == "logical-channel-index" or name == "loopback-mode" or name == "protocol-type" or name == "trib-protocol" or name == "trib-rate-class" or name == "tti-expected" or name == "tti-transmit" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "admin-state"):
                        self.admin_state = value
                        self.admin_state.value_namespace = name_space
                        self.admin_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "ingress-client-port"):
                        self.ingress_client_port = value
                        self.ingress_client_port.value_namespace = name_space
                        self.ingress_client_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "ingress-physical-channel"):
                        self.ingress_physical_channel = value
                        self.ingress_physical_channel.value_namespace = name_space
                        self.ingress_physical_channel.value_namespace_prefix = name_space_prefix
                    if(value_path == "logical-channel-ifname"):
                        self.logical_channel_ifname = value
                        self.logical_channel_ifname.value_namespace = name_space
                        self.logical_channel_ifname.value_namespace_prefix = name_space_prefix
                    if(value_path == "logical-channel-index"):
                        self.logical_channel_index = value
                        self.logical_channel_index.value_namespace = name_space
                        self.logical_channel_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "loopback-mode"):
                        self.loopback_mode = value
                        self.loopback_mode.value_namespace = name_space
                        self.loopback_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-type"):
                        self.protocol_type = value
                        self.protocol_type.value_namespace = name_space
                        self.protocol_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "trib-protocol"):
                        self.trib_protocol = value
                        self.trib_protocol.value_namespace = name_space
                        self.trib_protocol.value_namespace_prefix = name_space_prefix
                    if(value_path == "trib-rate-class"):
                        self.trib_rate_class = value
                        self.trib_rate_class.value_namespace = name_space
                        self.trib_rate_class.value_namespace_prefix = name_space_prefix
                    if(value_path == "tti-expected"):
                        self.tti_expected = value
                        self.tti_expected.value_namespace = name_space
                        self.tti_expected.value_namespace_prefix = name_space_prefix
                    if(value_path == "tti-transmit"):
                        self.tti_transmit = value
                        self.tti_transmit.value_namespace = name_space
                        self.tti_transmit.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix


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

                    self.optical_logical_interface_logical_channel_assignment = YList(self)

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
                                super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments, self).__setattr__(name, value)


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

                        self.index = YLeaf(YType.int32, "index")

                        self.optical_logical_interface_logical_channel_assignment_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr()
                        self.optical_logical_interface_logical_channel_assignment_attr.parent = self
                        self._children_name_map["optical_logical_interface_logical_channel_assignment_attr"] = "optical-logical-interface-logical-channel-assignment-attr"
                        self._children_yang_names.add("optical-logical-interface-logical-channel-assignment-attr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment, self).__setattr__(name, value)


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

                            self.allocation = YLeaf(YType.uint32, "allocation")

                            self.assignment_type = YLeaf(YType.uint32, "assignment-type")

                            self.index = YLeaf(YType.uint32, "index")

                            self.is_logical_link = YLeaf(YType.boolean, "is-logical-link")

                            self.logical_channel = YLeaf(YType.uint32, "logical-channel")

                            self.name = YLeaf(YType.str, "name")

                            self.optical_channel = YLeaf(YType.str, "optical-channel")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("allocation",
                                            "assignment_type",
                                            "index",
                                            "is_logical_link",
                                            "logical_channel",
                                            "name",
                                            "optical_channel") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.allocation.is_set or
                                self.assignment_type.is_set or
                                self.index.is_set or
                                self.is_logical_link.is_set or
                                self.logical_channel.is_set or
                                self.name.is_set or
                                self.optical_channel.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.allocation.yfilter != YFilter.not_set or
                                self.assignment_type.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.is_logical_link.yfilter != YFilter.not_set or
                                self.logical_channel.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.optical_channel.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "optical-logical-interface-logical-channel-assignment-attr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.allocation.is_set or self.allocation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.allocation.get_name_leafdata())
                            if (self.assignment_type.is_set or self.assignment_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.assignment_type.get_name_leafdata())
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.is_logical_link.is_set or self.is_logical_link.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_logical_link.get_name_leafdata())
                            if (self.logical_channel.is_set or self.logical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.logical_channel.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.optical_channel.is_set or self.optical_channel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.optical_channel.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allocation" or name == "assignment-type" or name == "index" or name == "is-logical-link" or name == "logical-channel" or name == "name" or name == "optical-channel"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "allocation"):
                                self.allocation = value
                                self.allocation.value_namespace = name_space
                                self.allocation.value_namespace_prefix = name_space_prefix
                            if(value_path == "assignment-type"):
                                self.assignment_type = value
                                self.assignment_type.value_namespace = name_space
                                self.assignment_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-logical-link"):
                                self.is_logical_link = value
                                self.is_logical_link.value_namespace = name_space
                                self.is_logical_link.value_namespace_prefix = name_space_prefix
                            if(value_path == "logical-channel"):
                                self.logical_channel = value
                                self.logical_channel.value_namespace = name_space
                                self.logical_channel.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "optical-channel"):
                                self.optical_channel = value
                                self.optical_channel.value_namespace = name_space
                                self.optical_channel.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.index.is_set or
                            (self.optical_logical_interface_logical_channel_assignment_attr is not None and self.optical_logical_interface_logical_channel_assignment_attr.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            (self.optical_logical_interface_logical_channel_assignment_attr is not None and self.optical_logical_interface_logical_channel_assignment_attr.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "optical-logical-interface-logical-channel-assignment" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "optical-logical-interface-logical-channel-assignment-attr"):
                            if (self.optical_logical_interface_logical_channel_assignment_attr is None):
                                self.optical_logical_interface_logical_channel_assignment_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr()
                                self.optical_logical_interface_logical_channel_assignment_attr.parent = self
                                self._children_name_map["optical_logical_interface_logical_channel_assignment_attr"] = "optical-logical-interface-logical-channel-assignment-attr"
                            return self.optical_logical_interface_logical_channel_assignment_attr

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "optical-logical-interface-logical-channel-assignment-attr" or name == "index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.optical_logical_interface_logical_channel_assignment:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.optical_logical_interface_logical_channel_assignment:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "optical-logical-interface-logical-channel-assignments" + path_buffer

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

                    if (child_yang_name == "optical-logical-interface-logical-channel-assignment"):
                        for c in self.optical_logical_interface_logical_channel_assignment:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.optical_logical_interface_logical_channel_assignment.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "optical-logical-interface-logical-channel-assignment"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.index.is_set or
                    (self.optical_logical_interface_attr is not None and self.optical_logical_interface_attr.has_data()) or
                    (self.optical_logical_interface_logical_channel_assignments is not None and self.optical_logical_interface_logical_channel_assignments.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.index.yfilter != YFilter.not_set or
                    (self.optical_logical_interface_attr is not None and self.optical_logical_interface_attr.has_operation()) or
                    (self.optical_logical_interface_logical_channel_assignments is not None and self.optical_logical_interface_logical_channel_assignments.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "optical-logical-interface" + "[index='" + self.index.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/optical-logical-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.index.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "optical-logical-interface-attr"):
                    if (self.optical_logical_interface_attr is None):
                        self.optical_logical_interface_attr = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr()
                        self.optical_logical_interface_attr.parent = self
                        self._children_name_map["optical_logical_interface_attr"] = "optical-logical-interface-attr"
                    return self.optical_logical_interface_attr

                if (child_yang_name == "optical-logical-interface-logical-channel-assignments"):
                    if (self.optical_logical_interface_logical_channel_assignments is None):
                        self.optical_logical_interface_logical_channel_assignments = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments()
                        self.optical_logical_interface_logical_channel_assignments.parent = self
                        self._children_name_map["optical_logical_interface_logical_channel_assignments"] = "optical-logical-interface-logical-channel-assignments"
                    return self.optical_logical_interface_logical_channel_assignments

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "optical-logical-interface-attr" or name == "optical-logical-interface-logical-channel-assignments" or name == "index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "index"):
                    self.index = value
                    self.index.value_namespace = name_space
                    self.index.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.optical_logical_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.optical_logical_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "optical-logical-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "optical-logical-interface"):
                for c in self.optical_logical_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.optical_logical_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "optical-logical-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.config_status is not None and self.config_status.has_data()) or
            (self.graph is not None and self.graph.has_data()) or
            (self.operational_modes is not None and self.operational_modes.has_data()) or
            (self.optical_channel_interfaces is not None and self.optical_channel_interfaces.has_data()) or
            (self.optical_logical_interfaces is not None and self.optical_logical_interfaces.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.config_status is not None and self.config_status.has_operation()) or
            (self.graph is not None and self.graph.has_operation()) or
            (self.operational_modes is not None and self.operational_modes.has_operation()) or
            (self.optical_channel_interfaces is not None and self.optical_channel_interfaces.has_operation()) or
            (self.optical_logical_interfaces is not None and self.optical_logical_interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-terminal-device-oper:optical-interface" + path_buffer

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

        if (child_yang_name == "config-status"):
            if (self.config_status is None):
                self.config_status = OpticalInterface.ConfigStatus()
                self.config_status.parent = self
                self._children_name_map["config_status"] = "config-status"
            return self.config_status

        if (child_yang_name == "graph"):
            if (self.graph is None):
                self.graph = OpticalInterface.Graph()
                self.graph.parent = self
                self._children_name_map["graph"] = "graph"
            return self.graph

        if (child_yang_name == "operational-modes"):
            if (self.operational_modes is None):
                self.operational_modes = OpticalInterface.OperationalModes()
                self.operational_modes.parent = self
                self._children_name_map["operational_modes"] = "operational-modes"
            return self.operational_modes

        if (child_yang_name == "optical-channel-interfaces"):
            if (self.optical_channel_interfaces is None):
                self.optical_channel_interfaces = OpticalInterface.OpticalChannelInterfaces()
                self.optical_channel_interfaces.parent = self
                self._children_name_map["optical_channel_interfaces"] = "optical-channel-interfaces"
            return self.optical_channel_interfaces

        if (child_yang_name == "optical-logical-interfaces"):
            if (self.optical_logical_interfaces is None):
                self.optical_logical_interfaces = OpticalInterface.OpticalLogicalInterfaces()
                self.optical_logical_interfaces.parent = self
                self._children_name_map["optical_logical_interfaces"] = "optical-logical-interfaces"
            return self.optical_logical_interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "config-status" or name == "graph" or name == "operational-modes" or name == "optical-channel-interfaces" or name == "optical-logical-interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = OpticalInterface()
        return self._top_entity

