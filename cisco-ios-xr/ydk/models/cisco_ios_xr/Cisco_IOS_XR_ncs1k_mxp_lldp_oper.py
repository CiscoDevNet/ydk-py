""" Cisco_IOS_XR_ncs1k_mxp_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\-snoop\-data\: Information related to LLDP Snoop

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LldpL3AddrProtocol(Enum):
    """
    LldpL3AddrProtocol

    Lldp l3 addr protocol

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")



class LldpSnoopData(Entity):
    """
    Information related to LLDP Snoop
    
    .. attribute:: ethernet_controller_names
    
    	Ethernet controller snoop data
    	**type**\:   :py:class:`EthernetControllerNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames>`
    
    .. attribute:: lldp_neighbor_brief
    
    	NCS1K LLDP Neighbor brief info
    	**type**\:   :py:class:`LldpNeighborBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.LldpNeighborBrief>`
    
    

    """

    _prefix = 'ncs1k-mxp-lldp-oper'
    _revision = '2016-10-13'

    def __init__(self):
        super(LldpSnoopData, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp-snoop-data"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper"

        self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
        self.ethernet_controller_names.parent = self
        self._children_name_map["ethernet_controller_names"] = "ethernet-controller-names"
        self._children_yang_names.add("ethernet-controller-names")

        self.lldp_neighbor_brief = LldpSnoopData.LldpNeighborBrief()
        self.lldp_neighbor_brief.parent = self
        self._children_name_map["lldp_neighbor_brief"] = "lldp-neighbor-brief"
        self._children_yang_names.add("lldp-neighbor-brief")


    class LldpNeighborBrief(Entity):
        """
        NCS1K LLDP Neighbor brief info
        
        .. attribute:: neighbours
        
        	List of LLDP neighbors
        	**type**\:   :py:class:`Neighbours <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.LldpNeighborBrief.Neighbours>`
        
        .. attribute:: number_of_entries
        
        	Number of active neighbors entries
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'ncs1k-mxp-lldp-oper'
        _revision = '2016-10-13'

        def __init__(self):
            super(LldpSnoopData.LldpNeighborBrief, self).__init__()

            self.yang_name = "lldp-neighbor-brief"
            self.yang_parent_name = "lldp-snoop-data"

            self.number_of_entries = YLeaf(YType.uint16, "number-of-entries")

            self.neighbours = LldpSnoopData.LldpNeighborBrief.Neighbours()
            self.neighbours.parent = self
            self._children_name_map["neighbours"] = "neighbours"
            self._children_yang_names.add("neighbours")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("number_of_entries") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LldpSnoopData.LldpNeighborBrief, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpSnoopData.LldpNeighborBrief, self).__setattr__(name, value)


        class Neighbours(Entity):
            """
            List of LLDP neighbors
            
            .. attribute:: lldp_neighbor_brief_entry
            
            	lldp neighbor brief entry
            	**type**\: list of    :py:class:`LldpNeighborBriefEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry>`
            
            

            """

            _prefix = 'ncs1k-mxp-lldp-oper'
            _revision = '2016-10-13'

            def __init__(self):
                super(LldpSnoopData.LldpNeighborBrief.Neighbours, self).__init__()

                self.yang_name = "neighbours"
                self.yang_parent_name = "lldp-neighbor-brief"

                self.lldp_neighbor_brief_entry = YList(self)

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
                            super(LldpSnoopData.LldpNeighborBrief.Neighbours, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpSnoopData.LldpNeighborBrief.Neighbours, self).__setattr__(name, value)


            class LldpNeighborBriefEntry(Entity):
                """
                lldp neighbor brief entry
                
                .. attribute:: chassis_id
                
                	Chassis id
                	**type**\:  str
                
                .. attribute:: enabled_capabilities
                
                	Enabled Capabilities
                	**type**\:  str
                
                .. attribute:: hold_time
                
                	Remaining hold time
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: port_id_detail
                
                	Outgoing port identifier
                	**type**\:  str
                
                .. attribute:: recv_intf
                
                	Receive Interface
                	**type**\:  str
                
                .. attribute:: system_name
                
                	System Name
                	**type**\:  str
                
                

                """

                _prefix = 'ncs1k-mxp-lldp-oper'
                _revision = '2016-10-13'

                def __init__(self):
                    super(LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry, self).__init__()

                    self.yang_name = "lldp-neighbor-brief-entry"
                    self.yang_parent_name = "neighbours"

                    self.chassis_id = YLeaf(YType.str, "chassis-id")

                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                    self.hold_time = YLeaf(YType.uint16, "hold-time")

                    self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                    self.recv_intf = YLeaf(YType.str, "recv-intf")

                    self.system_name = YLeaf(YType.str, "system-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("chassis_id",
                                    "enabled_capabilities",
                                    "hold_time",
                                    "port_id_detail",
                                    "recv_intf",
                                    "system_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.chassis_id.is_set or
                        self.enabled_capabilities.is_set or
                        self.hold_time.is_set or
                        self.port_id_detail.is_set or
                        self.recv_intf.is_set or
                        self.system_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.chassis_id.yfilter != YFilter.not_set or
                        self.enabled_capabilities.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.port_id_detail.yfilter != YFilter.not_set or
                        self.recv_intf.yfilter != YFilter.not_set or
                        self.system_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lldp-neighbor-brief-entry" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/lldp-neighbor-brief/neighbours/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.chassis_id.is_set or self.chassis_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.chassis_id.get_name_leafdata())
                    if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.port_id_detail.is_set or self.port_id_detail.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_id_detail.get_name_leafdata())
                    if (self.recv_intf.is_set or self.recv_intf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.recv_intf.get_name_leafdata())
                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "chassis-id" or name == "enabled-capabilities" or name == "hold-time" or name == "port-id-detail" or name == "recv-intf" or name == "system-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "chassis-id"):
                        self.chassis_id = value
                        self.chassis_id.value_namespace = name_space
                        self.chassis_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled-capabilities"):
                        self.enabled_capabilities = value
                        self.enabled_capabilities.value_namespace = name_space
                        self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-id-detail"):
                        self.port_id_detail = value
                        self.port_id_detail.value_namespace = name_space
                        self.port_id_detail.value_namespace_prefix = name_space_prefix
                    if(value_path == "recv-intf"):
                        self.recv_intf = value
                        self.recv_intf.value_namespace = name_space
                        self.recv_intf.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-name"):
                        self.system_name = value
                        self.system_name.value_namespace = name_space
                        self.system_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.lldp_neighbor_brief_entry:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.lldp_neighbor_brief_entry:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbours" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/lldp-neighbor-brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "lldp-neighbor-brief-entry"):
                    for c in self.lldp_neighbor_brief_entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.lldp_neighbor_brief_entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldp-neighbor-brief-entry"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.number_of_entries.is_set or
                (self.neighbours is not None and self.neighbours.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.number_of_entries.yfilter != YFilter.not_set or
                (self.neighbours is not None and self.neighbours.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldp-neighbor-brief" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.number_of_entries.is_set or self.number_of_entries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.number_of_entries.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "neighbours"):
                if (self.neighbours is None):
                    self.neighbours = LldpSnoopData.LldpNeighborBrief.Neighbours()
                    self.neighbours.parent = self
                    self._children_name_map["neighbours"] = "neighbours"
                return self.neighbours

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "neighbours" or name == "number-of-entries"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "number-of-entries"):
                self.number_of_entries = value
                self.number_of_entries.value_namespace = name_space
                self.number_of_entries.value_namespace_prefix = name_space_prefix


    class EthernetControllerNames(Entity):
        """
        Ethernet controller snoop data
        
        .. attribute:: ethernet_controller_name
        
        	port Name
        	**type**\: list of    :py:class:`EthernetControllerName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName>`
        
        

        """

        _prefix = 'ncs1k-mxp-lldp-oper'
        _revision = '2016-10-13'

        def __init__(self):
            super(LldpSnoopData.EthernetControllerNames, self).__init__()

            self.yang_name = "ethernet-controller-names"
            self.yang_parent_name = "lldp-snoop-data"

            self.ethernet_controller_name = YList(self)

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
                        super(LldpSnoopData.EthernetControllerNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpSnoopData.EthernetControllerNames, self).__setattr__(name, value)


        class EthernetControllerName(Entity):
            """
            port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: chassis_id
            
            	Chassis id
            	**type**\:  str
            
            .. attribute:: drop_enabled
            
            	LLDP Packet Drop Enabled
            	**type**\:  bool
            
            .. attribute:: enabled_capabilities
            
            	Enabled Capabilities
            	**type**\:  str
            
            .. attribute:: hold_time
            
            	Remaining hold time
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: lldp_neighbor
            
            	LldpNeighbor
            	**type**\:  str
            
            	**length:** 0..40
            
            .. attribute:: network_addresses
            
            	Management Addresses
            	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses>`
            
            .. attribute:: port_description
            
            	Port Description
            	**type**\:  str
            
            .. attribute:: port_id_detail
            
            	Outgoing port identifier
            	**type**\:  str
            
            .. attribute:: rx_lldp_pkts
            
            	Received LLDP Packets count
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: source_mac
            
            	Mac address of the neighbor
            	**type**\:  str
            
            .. attribute:: system_capabilities
            
            	System Capabilities
            	**type**\:  str
            
            .. attribute:: system_description
            
            	System Description
            	**type**\:  str
            
            .. attribute:: system_name
            
            	System Name
            	**type**\:  str
            
            

            """

            _prefix = 'ncs1k-mxp-lldp-oper'
            _revision = '2016-10-13'

            def __init__(self):
                super(LldpSnoopData.EthernetControllerNames.EthernetControllerName, self).__init__()

                self.yang_name = "ethernet-controller-name"
                self.yang_parent_name = "ethernet-controller-names"

                self.name = YLeaf(YType.str, "name")

                self.chassis_id = YLeaf(YType.str, "chassis-id")

                self.drop_enabled = YLeaf(YType.boolean, "drop-enabled")

                self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                self.hold_time = YLeaf(YType.uint16, "hold-time")

                self.lldp_neighbor = YLeaf(YType.str, "lldp-neighbor")

                self.port_description = YLeaf(YType.str, "port-description")

                self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                self.rx_lldp_pkts = YLeaf(YType.uint64, "rx-lldp-pkts")

                self.source_mac = YLeaf(YType.str, "source-mac")

                self.system_capabilities = YLeaf(YType.str, "system-capabilities")

                self.system_description = YLeaf(YType.str, "system-description")

                self.system_name = YLeaf(YType.str, "system-name")

                self.network_addresses = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses()
                self.network_addresses.parent = self
                self._children_name_map["network_addresses"] = "network-addresses"
                self._children_yang_names.add("network-addresses")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "chassis_id",
                                "drop_enabled",
                                "enabled_capabilities",
                                "hold_time",
                                "lldp_neighbor",
                                "port_description",
                                "port_id_detail",
                                "rx_lldp_pkts",
                                "source_mac",
                                "system_capabilities",
                                "system_description",
                                "system_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpSnoopData.EthernetControllerNames.EthernetControllerName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpSnoopData.EthernetControllerNames.EthernetControllerName, self).__setattr__(name, value)


            class NetworkAddresses(Entity):
                """
                Management Addresses
                
                .. attribute:: lldp_addr_entry
                
                	lldp addr entry
                	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry>`
                
                

                """

                _prefix = 'ncs1k-mxp-lldp-oper'
                _revision = '2016-10-13'

                def __init__(self):
                    super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, self).__init__()

                    self.yang_name = "network-addresses"
                    self.yang_parent_name = "ethernet-controller-name"

                    self.lldp_addr_entry = YList(self)

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
                                super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, self).__setattr__(name, value)


                class LldpAddrEntry(Entity):
                    """
                    lldp addr entry
                    
                    .. attribute:: address
                    
                    	Network layer address
                    	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address>`
                    
                    .. attribute:: if_num
                    
                    	Interface num
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ma_subtype
                    
                    	MA sub type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-lldp-oper'
                    _revision = '2016-10-13'

                    def __init__(self):
                        super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, self).__init__()

                        self.yang_name = "lldp-addr-entry"
                        self.yang_parent_name = "network-addresses"

                        self.if_num = YLeaf(YType.uint32, "if-num")

                        self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                        self.address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._children_yang_names.add("address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_num",
                                        "ma_subtype") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)


                    class Address(Entity):
                        """
                        Network layer address
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:   :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpL3AddrProtocol>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ncs1k-mxp-lldp-oper'
                        _revision = '2016-10-13'

                        def __init__(self):
                            super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "lldp-addr-entry"

                            self.address_type = YLeaf(YType.enumeration, "address-type")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address_type",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address_type.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address_type.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address_type.is_set or self.address_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_type.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-type" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address-type"):
                                self.address_type = value
                                self.address_type.value_namespace = name_space
                                self.address_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.if_num.is_set or
                            self.ma_subtype.is_set or
                            (self.address is not None and self.address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_num.yfilter != YFilter.not_set or
                            self.ma_subtype.yfilter != YFilter.not_set or
                            (self.address is not None and self.address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lldp-addr-entry" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_num.is_set or self.if_num.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_num.get_name_leafdata())
                        if (self.ma_subtype.is_set or self.ma_subtype.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ma_subtype.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "address"):
                            if (self.address is None):
                                self.address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                            return self.address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "if-num" or name == "ma-subtype"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-num"):
                            self.if_num = value
                            self.if_num.value_namespace = name_space
                            self.if_num.value_namespace_prefix = name_space_prefix
                        if(value_path == "ma-subtype"):
                            self.ma_subtype = value
                            self.ma_subtype.value_namespace = name_space
                            self.ma_subtype.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lldp_addr_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lldp_addr_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "network-addresses" + path_buffer

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

                    if (child_yang_name == "lldp-addr-entry"):
                        for c in self.lldp_addr_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lldp_addr_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lldp-addr-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.chassis_id.is_set or
                    self.drop_enabled.is_set or
                    self.enabled_capabilities.is_set or
                    self.hold_time.is_set or
                    self.lldp_neighbor.is_set or
                    self.port_description.is_set or
                    self.port_id_detail.is_set or
                    self.rx_lldp_pkts.is_set or
                    self.source_mac.is_set or
                    self.system_capabilities.is_set or
                    self.system_description.is_set or
                    self.system_name.is_set or
                    (self.network_addresses is not None and self.network_addresses.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.chassis_id.yfilter != YFilter.not_set or
                    self.drop_enabled.yfilter != YFilter.not_set or
                    self.enabled_capabilities.yfilter != YFilter.not_set or
                    self.hold_time.yfilter != YFilter.not_set or
                    self.lldp_neighbor.yfilter != YFilter.not_set or
                    self.port_description.yfilter != YFilter.not_set or
                    self.port_id_detail.yfilter != YFilter.not_set or
                    self.rx_lldp_pkts.yfilter != YFilter.not_set or
                    self.source_mac.yfilter != YFilter.not_set or
                    self.system_capabilities.yfilter != YFilter.not_set or
                    self.system_description.yfilter != YFilter.not_set or
                    self.system_name.yfilter != YFilter.not_set or
                    (self.network_addresses is not None and self.network_addresses.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ethernet-controller-name" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/ethernet-controller-names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.chassis_id.is_set or self.chassis_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chassis_id.get_name_leafdata())
                if (self.drop_enabled.is_set or self.drop_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.drop_enabled.get_name_leafdata())
                if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                if (self.lldp_neighbor.is_set or self.lldp_neighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldp_neighbor.get_name_leafdata())
                if (self.port_description.is_set or self.port_description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port_description.get_name_leafdata())
                if (self.port_id_detail.is_set or self.port_id_detail.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port_id_detail.get_name_leafdata())
                if (self.rx_lldp_pkts.is_set or self.rx_lldp_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rx_lldp_pkts.get_name_leafdata())
                if (self.source_mac.is_set or self.source_mac.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_mac.get_name_leafdata())
                if (self.system_capabilities.is_set or self.system_capabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_capabilities.get_name_leafdata())
                if (self.system_description.is_set or self.system_description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_description.get_name_leafdata())
                if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "network-addresses"):
                    if (self.network_addresses is None):
                        self.network_addresses = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses()
                        self.network_addresses.parent = self
                        self._children_name_map["network_addresses"] = "network-addresses"
                    return self.network_addresses

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "network-addresses" or name == "name" or name == "chassis-id" or name == "drop-enabled" or name == "enabled-capabilities" or name == "hold-time" or name == "lldp-neighbor" or name == "port-description" or name == "port-id-detail" or name == "rx-lldp-pkts" or name == "source-mac" or name == "system-capabilities" or name == "system-description" or name == "system-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "chassis-id"):
                    self.chassis_id = value
                    self.chassis_id.value_namespace = name_space
                    self.chassis_id.value_namespace_prefix = name_space_prefix
                if(value_path == "drop-enabled"):
                    self.drop_enabled = value
                    self.drop_enabled.value_namespace = name_space
                    self.drop_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled-capabilities"):
                    self.enabled_capabilities = value
                    self.enabled_capabilities.value_namespace = name_space
                    self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-time"):
                    self.hold_time = value
                    self.hold_time.value_namespace = name_space
                    self.hold_time.value_namespace_prefix = name_space_prefix
                if(value_path == "lldp-neighbor"):
                    self.lldp_neighbor = value
                    self.lldp_neighbor.value_namespace = name_space
                    self.lldp_neighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "port-description"):
                    self.port_description = value
                    self.port_description.value_namespace = name_space
                    self.port_description.value_namespace_prefix = name_space_prefix
                if(value_path == "port-id-detail"):
                    self.port_id_detail = value
                    self.port_id_detail.value_namespace = name_space
                    self.port_id_detail.value_namespace_prefix = name_space_prefix
                if(value_path == "rx-lldp-pkts"):
                    self.rx_lldp_pkts = value
                    self.rx_lldp_pkts.value_namespace = name_space
                    self.rx_lldp_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "source-mac"):
                    self.source_mac = value
                    self.source_mac.value_namespace = name_space
                    self.source_mac.value_namespace_prefix = name_space_prefix
                if(value_path == "system-capabilities"):
                    self.system_capabilities = value
                    self.system_capabilities.value_namespace = name_space
                    self.system_capabilities.value_namespace_prefix = name_space_prefix
                if(value_path == "system-description"):
                    self.system_description = value
                    self.system_description.value_namespace = name_space
                    self.system_description.value_namespace_prefix = name_space_prefix
                if(value_path == "system-name"):
                    self.system_name = value
                    self.system_name.value_namespace = name_space
                    self.system_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ethernet_controller_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ethernet_controller_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ethernet-controller-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ethernet-controller-name"):
                for c in self.ethernet_controller_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpSnoopData.EthernetControllerNames.EthernetControllerName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ethernet_controller_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ethernet-controller-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ethernet_controller_names is not None and self.ethernet_controller_names.has_data()) or
            (self.lldp_neighbor_brief is not None and self.lldp_neighbor_brief.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ethernet_controller_names is not None and self.ethernet_controller_names.has_operation()) or
            (self.lldp_neighbor_brief is not None and self.lldp_neighbor_brief.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data" + path_buffer

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

        if (child_yang_name == "ethernet-controller-names"):
            if (self.ethernet_controller_names is None):
                self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
                self.ethernet_controller_names.parent = self
                self._children_name_map["ethernet_controller_names"] = "ethernet-controller-names"
            return self.ethernet_controller_names

        if (child_yang_name == "lldp-neighbor-brief"):
            if (self.lldp_neighbor_brief is None):
                self.lldp_neighbor_brief = LldpSnoopData.LldpNeighborBrief()
                self.lldp_neighbor_brief.parent = self
                self._children_name_map["lldp_neighbor_brief"] = "lldp-neighbor-brief"
            return self.lldp_neighbor_brief

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ethernet-controller-names" or name == "lldp-neighbor-brief"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = LldpSnoopData()
        return self._top_entity

