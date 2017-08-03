""" Cisco_IOS_XR_ethernet_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\: Link Layer Discovery Protocol operational data

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



class Lldp(Entity):
    """
    Link Layer Discovery Protocol operational data
    
    .. attribute:: global_lldp
    
    	Global LLDP data
    	**type**\:   :py:class:`GlobalLldp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp>`
    
    .. attribute:: nodes
    
    	Per node LLDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes>`
    
    

    """

    _prefix = 'ethernet-lldp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lldp, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-lldp-oper"

        self.global_lldp = Lldp.GlobalLldp()
        self.global_lldp.parent = self
        self._children_name_map["global_lldp"] = "global-lldp"
        self._children_yang_names.add("global-lldp")

        self.nodes = Lldp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class GlobalLldp(Entity):
        """
        Global LLDP data
        
        .. attribute:: lldp_info
        
        	The LLDP Global Information of this box
        	**type**\:   :py:class:`LldpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp.LldpInfo>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lldp.GlobalLldp, self).__init__()

            self.yang_name = "global-lldp"
            self.yang_parent_name = "lldp"

            self.lldp_info = Lldp.GlobalLldp.LldpInfo()
            self.lldp_info.parent = self
            self._children_name_map["lldp_info"] = "lldp-info"
            self._children_yang_names.add("lldp-info")


        class LldpInfo(Entity):
            """
            The LLDP Global Information of this box
            
            .. attribute:: hold_time
            
            	Length  of time  (in sec)                        that receiver must keep this                     packet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: re_init
            
            	Delay (in sec) for LLDP                          initialization on any                            interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: timer
            
            	Rate at which LLDP packets                       are sent (in sec)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.GlobalLldp.LldpInfo, self).__init__()

                self.yang_name = "lldp-info"
                self.yang_parent_name = "global-lldp"

                self.hold_time = YLeaf(YType.uint32, "hold-time")

                self.re_init = YLeaf(YType.uint32, "re-init")

                self.timer = YLeaf(YType.uint32, "timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hold_time",
                                "re_init",
                                "timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.GlobalLldp.LldpInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.GlobalLldp.LldpInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hold_time.is_set or
                    self.re_init.is_set or
                    self.timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hold_time.yfilter != YFilter.not_set or
                    self.re_init.yfilter != YFilter.not_set or
                    self.timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldp-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-oper:lldp/global-lldp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                if (self.re_init.is_set or self.re_init.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.re_init.get_name_leafdata())
                if (self.timer.is_set or self.timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hold-time" or name == "re-init" or name == "timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hold-time"):
                    self.hold_time = value
                    self.hold_time.value_namespace = name_space
                    self.hold_time.value_namespace_prefix = name_space_prefix
                if(value_path == "re-init"):
                    self.re_init = value
                    self.re_init.value_namespace = name_space
                    self.re_init.value_namespace_prefix = name_space_prefix
                if(value_path == "timer"):
                    self.timer = value
                    self.timer.value_namespace = name_space
                    self.timer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.lldp_info is not None and self.lldp_info.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.lldp_info is not None and self.lldp_info.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global-lldp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldp-info"):
                if (self.lldp_info is None):
                    self.lldp_info = Lldp.GlobalLldp.LldpInfo()
                    self.lldp_info.parent = self
                    self._children_name_map["lldp_info"] = "lldp-info"
                return self.lldp_info

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldp-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nodes(Entity):
        """
        Per node LLDP operational data
        
        .. attribute:: node
        
        	The LLDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lldp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lldp"

            self.node = YList(self)

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
                        super(Lldp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lldp.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The LLDP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	The table of interfaces on which LLDP is running on this node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces>`
            
            .. attribute:: neighbors
            
            	The LLDP neighbor tables on this node
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors>`
            
            .. attribute:: statistics
            
            	The LLDP traffic statistics for this node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interfaces = Lldp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.neighbors = Lldp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")

                self.statistics = Lldp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.Nodes.Node, self).__setattr__(name, value)


            class Neighbors(Entity):
                """
                The LLDP neighbor tables on this node
                
                .. attribute:: details
                
                	The detailed LLDP neighbor table
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: devices
                
                	The detailed LLDP neighbor table on this device
                	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: summaries
                
                	The LLDP neighbor summary table
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lldp.Nodes.Node.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "node"

                    self.details = Lldp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                    self._children_yang_names.add("details")

                    self.devices = Lldp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self._children_name_map["devices"] = "devices"
                    self._children_yang_names.add("devices")

                    self.summaries = Lldp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._children_yang_names.add("summaries")


                class Devices(Entity):
                    """
                    The detailed LLDP neighbor table on this
                    device
                    
                    .. attribute:: device
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Devices, self).__init__()

                        self.yang_name = "devices"
                        self.yang_parent_name = "neighbors"

                        self.device = YList(self)

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
                                    super(Lldp.Nodes.Node.Neighbors.Devices, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lldp.Nodes.Node.Neighbors.Devices, self).__setattr__(name, value)


                    class Device(Entity):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Devices.Device, self).__init__()

                            self.yang_name = "device"
                            self.yang_parent_name = "devices"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("device_id",
                                            "interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device, self).__setattr__(name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "device"

                                self.chassis_id = YLeaf(YType.str, "chassis-id")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.receiving_parent_interface_name = YLeaf(YType.str, "receiving-parent-interface-name")

                                self.detail = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                                self.mib = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._children_yang_names.add("mib")

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
                                                "device_id",
                                                "enabled_capabilities",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id_detail",
                                                "receiving_interface_name",
                                                "receiving_parent_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.physical_media_capabilities = YLeaf(YType.str, "physical-media-capabilities")

                                    self.port_description = YLeaf(YType.str, "port-description")

                                    self.port_vlan_id = YLeaf(YType.uint32, "port-vlan-id")

                                    self.system_capabilities = YLeaf(YType.str, "system-capabilities")

                                    self.system_description = YLeaf(YType.str, "system-description")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses()
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
                                        if name in ("auto_negotiation",
                                                    "enabled_capabilities",
                                                    "media_attachment_unit_type",
                                                    "physical_media_capabilities",
                                                    "port_description",
                                                    "port_vlan_id",
                                                    "system_capabilities",
                                                    "system_description",
                                                    "system_name",
                                                    "time_remaining") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

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
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

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
                                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)

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
                                                    self.address = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                            c = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry()
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
                                        self.auto_negotiation.is_set or
                                        self.enabled_capabilities.is_set or
                                        self.media_attachment_unit_type.is_set or
                                        self.physical_media_capabilities.is_set or
                                        self.port_description.is_set or
                                        self.port_vlan_id.is_set or
                                        self.system_capabilities.is_set or
                                        self.system_description.is_set or
                                        self.system_name.is_set or
                                        self.time_remaining.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.auto_negotiation.yfilter != YFilter.not_set or
                                        self.enabled_capabilities.yfilter != YFilter.not_set or
                                        self.media_attachment_unit_type.yfilter != YFilter.not_set or
                                        self.physical_media_capabilities.yfilter != YFilter.not_set or
                                        self.port_description.yfilter != YFilter.not_set or
                                        self.port_vlan_id.yfilter != YFilter.not_set or
                                        self.system_capabilities.yfilter != YFilter.not_set or
                                        self.system_description.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.time_remaining.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.auto_negotiation.is_set or self.auto_negotiation.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.auto_negotiation.get_name_leafdata())
                                    if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                    if (self.media_attachment_unit_type.is_set or self.media_attachment_unit_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.media_attachment_unit_type.get_name_leafdata())
                                    if (self.physical_media_capabilities.is_set or self.physical_media_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.physical_media_capabilities.get_name_leafdata())
                                    if (self.port_description.is_set or self.port_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_description.get_name_leafdata())
                                    if (self.port_vlan_id.is_set or self.port_vlan_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_vlan_id.get_name_leafdata())
                                    if (self.system_capabilities.is_set or self.system_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_capabilities.get_name_leafdata())
                                    if (self.system_description.is_set or self.system_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_description.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_remaining.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "auto-negotiation" or name == "enabled-capabilities" or name == "media-attachment-unit-type" or name == "physical-media-capabilities" or name == "port-description" or name == "port-vlan-id" or name == "system-capabilities" or name == "system-description" or name == "system-name" or name == "time-remaining"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "auto-negotiation"):
                                        self.auto_negotiation = value
                                        self.auto_negotiation.value_namespace = name_space
                                        self.auto_negotiation.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enabled-capabilities"):
                                        self.enabled_capabilities = value
                                        self.enabled_capabilities.value_namespace = name_space
                                        self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "media-attachment-unit-type"):
                                        self.media_attachment_unit_type = value
                                        self.media_attachment_unit_type.value_namespace = name_space
                                        self.media_attachment_unit_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "physical-media-capabilities"):
                                        self.physical_media_capabilities = value
                                        self.physical_media_capabilities.value_namespace = name_space
                                        self.physical_media_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-description"):
                                        self.port_description = value
                                        self.port_description.value_namespace = name_space
                                        self.port_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-vlan-id"):
                                        self.port_vlan_id = value
                                        self.port_vlan_id.value_namespace = name_space
                                        self.port_vlan_id.value_namespace_prefix = name_space_prefix
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
                                    if(value_path == "time-remaining"):
                                        self.time_remaining = value
                                        self.time_remaining.value_namespace = name_space
                                        self.time_remaining.value_namespace_prefix = name_space_prefix


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.chassis_id_len = YLeaf(YType.uint16, "chassis-id-len")

                                    self.chassis_id_sub_type = YLeaf(YType.uint8, "chassis-id-sub-type")

                                    self.combined_capabilities = YLeaf(YType.uint32, "combined-capabilities")

                                    self.port_id_len = YLeaf(YType.uint16, "port-id-len")

                                    self.port_id_sub_type = YLeaf(YType.uint8, "port-id-sub-type")

                                    self.rem_index = YLeaf(YType.uint32, "rem-index")

                                    self.rem_local_port_num = YLeaf(YType.uint32, "rem-local-port-num")

                                    self.rem_time_mark = YLeaf(YType.uint32, "rem-time-mark")

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._children_yang_names.add("org-def-tlv-list")

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                    self._children_yang_names.add("unknown-tlv-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("chassis_id_len",
                                                    "chassis_id_sub_type",
                                                    "combined_capabilities",
                                                    "port_id_len",
                                                    "port_id_sub_type",
                                                    "rem_index",
                                                    "rem_local_port_num",
                                                    "rem_time_mark") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, self).__setattr__(name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_unknown_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("tlv_type",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.tlv_type.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.tlv_type.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-unknown-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.tlv_type.is_set or self.tlv_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_type.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "tlv-type" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "tlv-type"):
                                                self.tlv_type = value
                                                self.tlv_type.value_namespace = name_space
                                                self.tlv_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unknown-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-unknown-tlv-entry"):
                                            for c in self.lldp_unknown_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_unknown_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-unknown-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_org_def_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("oui",
                                                            "tlv_info_indes",
                                                            "tlv_subtype",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.oui.is_set or
                                                self.tlv_info_indes.is_set or
                                                self.tlv_subtype.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.oui.yfilter != YFilter.not_set or
                                                self.tlv_info_indes.yfilter != YFilter.not_set or
                                                self.tlv_subtype.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-org-def-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.oui.get_name_leafdata())
                                            if (self.tlv_info_indes.is_set or self.tlv_info_indes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_info_indes.get_name_leafdata())
                                            if (self.tlv_subtype.is_set or self.tlv_subtype.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_subtype.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "oui" or name == "tlv-info-indes" or name == "tlv-subtype" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "oui"):
                                                self.oui = value
                                                self.oui.value_namespace = name_space
                                                self.oui.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-info-indes"):
                                                self.tlv_info_indes = value
                                                self.tlv_info_indes.value_namespace = name_space
                                                self.tlv_info_indes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-subtype"):
                                                self.tlv_subtype = value
                                                self.tlv_subtype.value_namespace = name_space
                                                self.tlv_subtype.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "org-def-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-org-def-tlv-entry"):
                                            for c in self.lldp_org_def_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_org_def_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-org-def-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.chassis_id_len.is_set or
                                        self.chassis_id_sub_type.is_set or
                                        self.combined_capabilities.is_set or
                                        self.port_id_len.is_set or
                                        self.port_id_sub_type.is_set or
                                        self.rem_index.is_set or
                                        self.rem_local_port_num.is_set or
                                        self.rem_time_mark.is_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_data()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.chassis_id_len.yfilter != YFilter.not_set or
                                        self.chassis_id_sub_type.yfilter != YFilter.not_set or
                                        self.combined_capabilities.yfilter != YFilter.not_set or
                                        self.port_id_len.yfilter != YFilter.not_set or
                                        self.port_id_sub_type.yfilter != YFilter.not_set or
                                        self.rem_index.yfilter != YFilter.not_set or
                                        self.rem_local_port_num.yfilter != YFilter.not_set or
                                        self.rem_time_mark.yfilter != YFilter.not_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_operation()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mib" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.chassis_id_len.is_set or self.chassis_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_len.get_name_leafdata())
                                    if (self.chassis_id_sub_type.is_set or self.chassis_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_sub_type.get_name_leafdata())
                                    if (self.combined_capabilities.is_set or self.combined_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.combined_capabilities.get_name_leafdata())
                                    if (self.port_id_len.is_set or self.port_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_len.get_name_leafdata())
                                    if (self.port_id_sub_type.is_set or self.port_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_sub_type.get_name_leafdata())
                                    if (self.rem_index.is_set or self.rem_index.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_index.get_name_leafdata())
                                    if (self.rem_local_port_num.is_set or self.rem_local_port_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_local_port_num.get_name_leafdata())
                                    if (self.rem_time_mark.is_set or self.rem_time_mark.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_time_mark.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "org-def-tlv-list"):
                                        if (self.org_def_tlv_list is None):
                                            self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList()
                                            self.org_def_tlv_list.parent = self
                                            self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                        return self.org_def_tlv_list

                                    if (child_yang_name == "unknown-tlv-list"):
                                        if (self.unknown_tlv_list is None):
                                            self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList()
                                            self.unknown_tlv_list.parent = self
                                            self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                        return self.unknown_tlv_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "org-def-tlv-list" or name == "unknown-tlv-list" or name == "chassis-id-len" or name == "chassis-id-sub-type" or name == "combined-capabilities" or name == "port-id-len" or name == "port-id-sub-type" or name == "rem-index" or name == "rem-local-port-num" or name == "rem-time-mark"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "chassis-id-len"):
                                        self.chassis_id_len = value
                                        self.chassis_id_len.value_namespace = name_space
                                        self.chassis_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chassis-id-sub-type"):
                                        self.chassis_id_sub_type = value
                                        self.chassis_id_sub_type.value_namespace = name_space
                                        self.chassis_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "combined-capabilities"):
                                        self.combined_capabilities = value
                                        self.combined_capabilities.value_namespace = name_space
                                        self.combined_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-len"):
                                        self.port_id_len = value
                                        self.port_id_len.value_namespace = name_space
                                        self.port_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-sub-type"):
                                        self.port_id_sub_type = value
                                        self.port_id_sub_type.value_namespace = name_space
                                        self.port_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-index"):
                                        self.rem_index = value
                                        self.rem_index.value_namespace = name_space
                                        self.rem_index.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-local-port-num"):
                                        self.rem_local_port_num = value
                                        self.rem_local_port_num.value_namespace = name_space
                                        self.rem_local_port_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-time-mark"):
                                        self.rem_time_mark = value
                                        self.rem_time_mark.value_namespace = name_space
                                        self.rem_time_mark.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.chassis_id.is_set or
                                    self.device_id.is_set or
                                    self.enabled_capabilities.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id_detail.is_set or
                                    self.receiving_interface_name.is_set or
                                    self.receiving_parent_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()) or
                                    (self.mib is not None and self.mib.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.chassis_id.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.enabled_capabilities.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id_detail.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    self.receiving_parent_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()) or
                                    (self.mib is not None and self.mib.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lldp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.chassis_id.is_set or self.chassis_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.chassis_id.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id_detail.is_set or self.port_id_detail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id_detail.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())
                                if (self.receiving_parent_interface_name.is_set or self.receiving_parent_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_parent_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                if (child_yang_name == "mib"):
                                    if (self.mib is None):
                                        self.mib = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib()
                                        self.mib.parent = self
                                        self._children_name_map["mib"] = "mib"
                                    return self.mib

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "mib" or name == "chassis-id" or name == "device-id" or name == "enabled-capabilities" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id-detail" or name == "receiving-interface-name" or name == "receiving-parent-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "chassis-id"):
                                    self.chassis_id = value
                                    self.chassis_id.value_namespace = name_space
                                    self.chassis_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled-capabilities"):
                                    self.enabled_capabilities = value
                                    self.enabled_capabilities.value_namespace = name_space
                                    self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "header-version"):
                                    self.header_version = value
                                    self.header_version.value_namespace = name_space
                                    self.header_version.value_namespace_prefix = name_space_prefix
                                if(value_path == "hold-time"):
                                    self.hold_time = value
                                    self.hold_time.value_namespace = name_space
                                    self.hold_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "platform"):
                                    self.platform = value
                                    self.platform.value_namespace = name_space
                                    self.platform.value_namespace_prefix = name_space_prefix
                                if(value_path == "port-id-detail"):
                                    self.port_id_detail = value
                                    self.port_id_detail.value_namespace = name_space
                                    self.port_id_detail.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-parent-interface-name"):
                                    self.receiving_parent_interface_name = value
                                    self.receiving_parent_interface_name.value_namespace = name_space
                                    self.receiving_parent_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.lldp_neighbor:
                                if (c.has_data()):
                                    return True
                            return (
                                self.device_id.is_set or
                                self.interface_name.is_set)

                        def has_operation(self):
                            for c in self.lldp_neighbor:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.device_id.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "device" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.device_id.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "lldp-neighbor"):
                                for c in self.lldp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.lldp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "lldp-neighbor" or name == "device-id" or name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "device-id"):
                                self.device_id = value
                                self.device_id.value_namespace = name_space
                                self.device_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.device:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.device:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "devices" + path_buffer

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

                        if (child_yang_name == "device"):
                            for c in self.device:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Lldp.Nodes.Node.Neighbors.Devices.Device()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.device.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "device"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Details(Entity):
                    """
                    The detailed LLDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Details, self).__init__()

                        self.yang_name = "details"
                        self.yang_parent_name = "neighbors"

                        self.detail = YList(self)

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
                                    super(Lldp.Nodes.Node.Neighbors.Details, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lldp.Nodes.Node.Neighbors.Details, self).__setattr__(name, value)


                    class Detail(Entity):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Details.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "details"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("device_id",
                                            "interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail, self).__setattr__(name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "detail"

                                self.chassis_id = YLeaf(YType.str, "chassis-id")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.receiving_parent_interface_name = YLeaf(YType.str, "receiving-parent-interface-name")

                                self.detail = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                                self.mib = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._children_yang_names.add("mib")

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
                                                "device_id",
                                                "enabled_capabilities",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id_detail",
                                                "receiving_interface_name",
                                                "receiving_parent_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.physical_media_capabilities = YLeaf(YType.str, "physical-media-capabilities")

                                    self.port_description = YLeaf(YType.str, "port-description")

                                    self.port_vlan_id = YLeaf(YType.uint32, "port-vlan-id")

                                    self.system_capabilities = YLeaf(YType.str, "system-capabilities")

                                    self.system_description = YLeaf(YType.str, "system-description")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses()
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
                                        if name in ("auto_negotiation",
                                                    "enabled_capabilities",
                                                    "media_attachment_unit_type",
                                                    "physical_media_capabilities",
                                                    "port_description",
                                                    "port_vlan_id",
                                                    "system_capabilities",
                                                    "system_description",
                                                    "system_name",
                                                    "time_remaining") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

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
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

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
                                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)

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
                                                    self.address = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                            c = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry()
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
                                        self.auto_negotiation.is_set or
                                        self.enabled_capabilities.is_set or
                                        self.media_attachment_unit_type.is_set or
                                        self.physical_media_capabilities.is_set or
                                        self.port_description.is_set or
                                        self.port_vlan_id.is_set or
                                        self.system_capabilities.is_set or
                                        self.system_description.is_set or
                                        self.system_name.is_set or
                                        self.time_remaining.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.auto_negotiation.yfilter != YFilter.not_set or
                                        self.enabled_capabilities.yfilter != YFilter.not_set or
                                        self.media_attachment_unit_type.yfilter != YFilter.not_set or
                                        self.physical_media_capabilities.yfilter != YFilter.not_set or
                                        self.port_description.yfilter != YFilter.not_set or
                                        self.port_vlan_id.yfilter != YFilter.not_set or
                                        self.system_capabilities.yfilter != YFilter.not_set or
                                        self.system_description.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.time_remaining.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.auto_negotiation.is_set or self.auto_negotiation.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.auto_negotiation.get_name_leafdata())
                                    if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                    if (self.media_attachment_unit_type.is_set or self.media_attachment_unit_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.media_attachment_unit_type.get_name_leafdata())
                                    if (self.physical_media_capabilities.is_set or self.physical_media_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.physical_media_capabilities.get_name_leafdata())
                                    if (self.port_description.is_set or self.port_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_description.get_name_leafdata())
                                    if (self.port_vlan_id.is_set or self.port_vlan_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_vlan_id.get_name_leafdata())
                                    if (self.system_capabilities.is_set or self.system_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_capabilities.get_name_leafdata())
                                    if (self.system_description.is_set or self.system_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_description.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_remaining.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "auto-negotiation" or name == "enabled-capabilities" or name == "media-attachment-unit-type" or name == "physical-media-capabilities" or name == "port-description" or name == "port-vlan-id" or name == "system-capabilities" or name == "system-description" or name == "system-name" or name == "time-remaining"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "auto-negotiation"):
                                        self.auto_negotiation = value
                                        self.auto_negotiation.value_namespace = name_space
                                        self.auto_negotiation.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enabled-capabilities"):
                                        self.enabled_capabilities = value
                                        self.enabled_capabilities.value_namespace = name_space
                                        self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "media-attachment-unit-type"):
                                        self.media_attachment_unit_type = value
                                        self.media_attachment_unit_type.value_namespace = name_space
                                        self.media_attachment_unit_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "physical-media-capabilities"):
                                        self.physical_media_capabilities = value
                                        self.physical_media_capabilities.value_namespace = name_space
                                        self.physical_media_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-description"):
                                        self.port_description = value
                                        self.port_description.value_namespace = name_space
                                        self.port_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-vlan-id"):
                                        self.port_vlan_id = value
                                        self.port_vlan_id.value_namespace = name_space
                                        self.port_vlan_id.value_namespace_prefix = name_space_prefix
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
                                    if(value_path == "time-remaining"):
                                        self.time_remaining = value
                                        self.time_remaining.value_namespace = name_space
                                        self.time_remaining.value_namespace_prefix = name_space_prefix


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.chassis_id_len = YLeaf(YType.uint16, "chassis-id-len")

                                    self.chassis_id_sub_type = YLeaf(YType.uint8, "chassis-id-sub-type")

                                    self.combined_capabilities = YLeaf(YType.uint32, "combined-capabilities")

                                    self.port_id_len = YLeaf(YType.uint16, "port-id-len")

                                    self.port_id_sub_type = YLeaf(YType.uint8, "port-id-sub-type")

                                    self.rem_index = YLeaf(YType.uint32, "rem-index")

                                    self.rem_local_port_num = YLeaf(YType.uint32, "rem-local-port-num")

                                    self.rem_time_mark = YLeaf(YType.uint32, "rem-time-mark")

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._children_yang_names.add("org-def-tlv-list")

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                    self._children_yang_names.add("unknown-tlv-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("chassis_id_len",
                                                    "chassis_id_sub_type",
                                                    "combined_capabilities",
                                                    "port_id_len",
                                                    "port_id_sub_type",
                                                    "rem_index",
                                                    "rem_local_port_num",
                                                    "rem_time_mark") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, self).__setattr__(name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_unknown_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("tlv_type",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.tlv_type.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.tlv_type.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-unknown-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.tlv_type.is_set or self.tlv_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_type.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "tlv-type" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "tlv-type"):
                                                self.tlv_type = value
                                                self.tlv_type.value_namespace = name_space
                                                self.tlv_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unknown-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-unknown-tlv-entry"):
                                            for c in self.lldp_unknown_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_unknown_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-unknown-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_org_def_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("oui",
                                                            "tlv_info_indes",
                                                            "tlv_subtype",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.oui.is_set or
                                                self.tlv_info_indes.is_set or
                                                self.tlv_subtype.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.oui.yfilter != YFilter.not_set or
                                                self.tlv_info_indes.yfilter != YFilter.not_set or
                                                self.tlv_subtype.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-org-def-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.oui.get_name_leafdata())
                                            if (self.tlv_info_indes.is_set or self.tlv_info_indes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_info_indes.get_name_leafdata())
                                            if (self.tlv_subtype.is_set or self.tlv_subtype.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_subtype.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "oui" or name == "tlv-info-indes" or name == "tlv-subtype" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "oui"):
                                                self.oui = value
                                                self.oui.value_namespace = name_space
                                                self.oui.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-info-indes"):
                                                self.tlv_info_indes = value
                                                self.tlv_info_indes.value_namespace = name_space
                                                self.tlv_info_indes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-subtype"):
                                                self.tlv_subtype = value
                                                self.tlv_subtype.value_namespace = name_space
                                                self.tlv_subtype.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "org-def-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-org-def-tlv-entry"):
                                            for c in self.lldp_org_def_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_org_def_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-org-def-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.chassis_id_len.is_set or
                                        self.chassis_id_sub_type.is_set or
                                        self.combined_capabilities.is_set or
                                        self.port_id_len.is_set or
                                        self.port_id_sub_type.is_set or
                                        self.rem_index.is_set or
                                        self.rem_local_port_num.is_set or
                                        self.rem_time_mark.is_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_data()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.chassis_id_len.yfilter != YFilter.not_set or
                                        self.chassis_id_sub_type.yfilter != YFilter.not_set or
                                        self.combined_capabilities.yfilter != YFilter.not_set or
                                        self.port_id_len.yfilter != YFilter.not_set or
                                        self.port_id_sub_type.yfilter != YFilter.not_set or
                                        self.rem_index.yfilter != YFilter.not_set or
                                        self.rem_local_port_num.yfilter != YFilter.not_set or
                                        self.rem_time_mark.yfilter != YFilter.not_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_operation()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mib" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.chassis_id_len.is_set or self.chassis_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_len.get_name_leafdata())
                                    if (self.chassis_id_sub_type.is_set or self.chassis_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_sub_type.get_name_leafdata())
                                    if (self.combined_capabilities.is_set or self.combined_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.combined_capabilities.get_name_leafdata())
                                    if (self.port_id_len.is_set or self.port_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_len.get_name_leafdata())
                                    if (self.port_id_sub_type.is_set or self.port_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_sub_type.get_name_leafdata())
                                    if (self.rem_index.is_set or self.rem_index.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_index.get_name_leafdata())
                                    if (self.rem_local_port_num.is_set or self.rem_local_port_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_local_port_num.get_name_leafdata())
                                    if (self.rem_time_mark.is_set or self.rem_time_mark.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_time_mark.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "org-def-tlv-list"):
                                        if (self.org_def_tlv_list is None):
                                            self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList()
                                            self.org_def_tlv_list.parent = self
                                            self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                        return self.org_def_tlv_list

                                    if (child_yang_name == "unknown-tlv-list"):
                                        if (self.unknown_tlv_list is None):
                                            self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList()
                                            self.unknown_tlv_list.parent = self
                                            self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                        return self.unknown_tlv_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "org-def-tlv-list" or name == "unknown-tlv-list" or name == "chassis-id-len" or name == "chassis-id-sub-type" or name == "combined-capabilities" or name == "port-id-len" or name == "port-id-sub-type" or name == "rem-index" or name == "rem-local-port-num" or name == "rem-time-mark"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "chassis-id-len"):
                                        self.chassis_id_len = value
                                        self.chassis_id_len.value_namespace = name_space
                                        self.chassis_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chassis-id-sub-type"):
                                        self.chassis_id_sub_type = value
                                        self.chassis_id_sub_type.value_namespace = name_space
                                        self.chassis_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "combined-capabilities"):
                                        self.combined_capabilities = value
                                        self.combined_capabilities.value_namespace = name_space
                                        self.combined_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-len"):
                                        self.port_id_len = value
                                        self.port_id_len.value_namespace = name_space
                                        self.port_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-sub-type"):
                                        self.port_id_sub_type = value
                                        self.port_id_sub_type.value_namespace = name_space
                                        self.port_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-index"):
                                        self.rem_index = value
                                        self.rem_index.value_namespace = name_space
                                        self.rem_index.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-local-port-num"):
                                        self.rem_local_port_num = value
                                        self.rem_local_port_num.value_namespace = name_space
                                        self.rem_local_port_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-time-mark"):
                                        self.rem_time_mark = value
                                        self.rem_time_mark.value_namespace = name_space
                                        self.rem_time_mark.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.chassis_id.is_set or
                                    self.device_id.is_set or
                                    self.enabled_capabilities.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id_detail.is_set or
                                    self.receiving_interface_name.is_set or
                                    self.receiving_parent_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()) or
                                    (self.mib is not None and self.mib.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.chassis_id.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.enabled_capabilities.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id_detail.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    self.receiving_parent_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()) or
                                    (self.mib is not None and self.mib.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lldp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.chassis_id.is_set or self.chassis_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.chassis_id.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id_detail.is_set or self.port_id_detail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id_detail.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())
                                if (self.receiving_parent_interface_name.is_set or self.receiving_parent_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_parent_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                if (child_yang_name == "mib"):
                                    if (self.mib is None):
                                        self.mib = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib()
                                        self.mib.parent = self
                                        self._children_name_map["mib"] = "mib"
                                    return self.mib

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "mib" or name == "chassis-id" or name == "device-id" or name == "enabled-capabilities" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id-detail" or name == "receiving-interface-name" or name == "receiving-parent-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "chassis-id"):
                                    self.chassis_id = value
                                    self.chassis_id.value_namespace = name_space
                                    self.chassis_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled-capabilities"):
                                    self.enabled_capabilities = value
                                    self.enabled_capabilities.value_namespace = name_space
                                    self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "header-version"):
                                    self.header_version = value
                                    self.header_version.value_namespace = name_space
                                    self.header_version.value_namespace_prefix = name_space_prefix
                                if(value_path == "hold-time"):
                                    self.hold_time = value
                                    self.hold_time.value_namespace = name_space
                                    self.hold_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "platform"):
                                    self.platform = value
                                    self.platform.value_namespace = name_space
                                    self.platform.value_namespace_prefix = name_space_prefix
                                if(value_path == "port-id-detail"):
                                    self.port_id_detail = value
                                    self.port_id_detail.value_namespace = name_space
                                    self.port_id_detail.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-parent-interface-name"):
                                    self.receiving_parent_interface_name = value
                                    self.receiving_parent_interface_name.value_namespace = name_space
                                    self.receiving_parent_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.lldp_neighbor:
                                if (c.has_data()):
                                    return True
                            return (
                                self.device_id.is_set or
                                self.interface_name.is_set)

                        def has_operation(self):
                            for c in self.lldp_neighbor:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.device_id.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "detail" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.device_id.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "lldp-neighbor"):
                                for c in self.lldp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.lldp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "lldp-neighbor" or name == "device-id" or name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "device-id"):
                                self.device_id = value
                                self.device_id.value_namespace = name_space
                                self.device_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.detail:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.detail:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "details" + path_buffer

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

                        if (child_yang_name == "detail"):
                            for c in self.detail:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Lldp.Nodes.Node.Neighbors.Details.Detail()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.detail.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "detail"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Summaries(Entity):
                    """
                    The LLDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Summaries, self).__init__()

                        self.yang_name = "summaries"
                        self.yang_parent_name = "neighbors"

                        self.summary = YList(self)

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
                                    super(Lldp.Nodes.Node.Neighbors.Summaries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lldp.Nodes.Node.Neighbors.Summaries, self).__setattr__(name, value)


                    class Summary(Entity):
                        """
                        Brief information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("device_id",
                                            "interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary, self).__setattr__(name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "summary"

                                self.chassis_id = YLeaf(YType.str, "chassis-id")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.receiving_parent_interface_name = YLeaf(YType.str, "receiving-parent-interface-name")

                                self.detail = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                                self.mib = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._children_yang_names.add("mib")

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
                                                "device_id",
                                                "enabled_capabilities",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id_detail",
                                                "receiving_interface_name",
                                                "receiving_parent_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.physical_media_capabilities = YLeaf(YType.str, "physical-media-capabilities")

                                    self.port_description = YLeaf(YType.str, "port-description")

                                    self.port_vlan_id = YLeaf(YType.uint32, "port-vlan-id")

                                    self.system_capabilities = YLeaf(YType.str, "system-capabilities")

                                    self.system_description = YLeaf(YType.str, "system-description")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses()
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
                                        if name in ("auto_negotiation",
                                                    "enabled_capabilities",
                                                    "media_attachment_unit_type",
                                                    "physical_media_capabilities",
                                                    "port_description",
                                                    "port_vlan_id",
                                                    "system_capabilities",
                                                    "system_description",
                                                    "system_name",
                                                    "time_remaining") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

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
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

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
                                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)

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
                                                    self.address = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
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
                                            c = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry()
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
                                        self.auto_negotiation.is_set or
                                        self.enabled_capabilities.is_set or
                                        self.media_attachment_unit_type.is_set or
                                        self.physical_media_capabilities.is_set or
                                        self.port_description.is_set or
                                        self.port_vlan_id.is_set or
                                        self.system_capabilities.is_set or
                                        self.system_description.is_set or
                                        self.system_name.is_set or
                                        self.time_remaining.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.auto_negotiation.yfilter != YFilter.not_set or
                                        self.enabled_capabilities.yfilter != YFilter.not_set or
                                        self.media_attachment_unit_type.yfilter != YFilter.not_set or
                                        self.physical_media_capabilities.yfilter != YFilter.not_set or
                                        self.port_description.yfilter != YFilter.not_set or
                                        self.port_vlan_id.yfilter != YFilter.not_set or
                                        self.system_capabilities.yfilter != YFilter.not_set or
                                        self.system_description.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.time_remaining.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.auto_negotiation.is_set or self.auto_negotiation.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.auto_negotiation.get_name_leafdata())
                                    if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                    if (self.media_attachment_unit_type.is_set or self.media_attachment_unit_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.media_attachment_unit_type.get_name_leafdata())
                                    if (self.physical_media_capabilities.is_set or self.physical_media_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.physical_media_capabilities.get_name_leafdata())
                                    if (self.port_description.is_set or self.port_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_description.get_name_leafdata())
                                    if (self.port_vlan_id.is_set or self.port_vlan_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_vlan_id.get_name_leafdata())
                                    if (self.system_capabilities.is_set or self.system_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_capabilities.get_name_leafdata())
                                    if (self.system_description.is_set or self.system_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_description.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_remaining.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "auto-negotiation" or name == "enabled-capabilities" or name == "media-attachment-unit-type" or name == "physical-media-capabilities" or name == "port-description" or name == "port-vlan-id" or name == "system-capabilities" or name == "system-description" or name == "system-name" or name == "time-remaining"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "auto-negotiation"):
                                        self.auto_negotiation = value
                                        self.auto_negotiation.value_namespace = name_space
                                        self.auto_negotiation.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enabled-capabilities"):
                                        self.enabled_capabilities = value
                                        self.enabled_capabilities.value_namespace = name_space
                                        self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "media-attachment-unit-type"):
                                        self.media_attachment_unit_type = value
                                        self.media_attachment_unit_type.value_namespace = name_space
                                        self.media_attachment_unit_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "physical-media-capabilities"):
                                        self.physical_media_capabilities = value
                                        self.physical_media_capabilities.value_namespace = name_space
                                        self.physical_media_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-description"):
                                        self.port_description = value
                                        self.port_description.value_namespace = name_space
                                        self.port_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-vlan-id"):
                                        self.port_vlan_id = value
                                        self.port_vlan_id.value_namespace = name_space
                                        self.port_vlan_id.value_namespace_prefix = name_space_prefix
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
                                    if(value_path == "time-remaining"):
                                        self.time_remaining = value
                                        self.time_remaining.value_namespace = name_space
                                        self.time_remaining.value_namespace_prefix = name_space_prefix


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"

                                    self.chassis_id_len = YLeaf(YType.uint16, "chassis-id-len")

                                    self.chassis_id_sub_type = YLeaf(YType.uint8, "chassis-id-sub-type")

                                    self.combined_capabilities = YLeaf(YType.uint32, "combined-capabilities")

                                    self.port_id_len = YLeaf(YType.uint16, "port-id-len")

                                    self.port_id_sub_type = YLeaf(YType.uint8, "port-id-sub-type")

                                    self.rem_index = YLeaf(YType.uint32, "rem-index")

                                    self.rem_local_port_num = YLeaf(YType.uint32, "rem-local-port-num")

                                    self.rem_time_mark = YLeaf(YType.uint32, "rem-time-mark")

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._children_yang_names.add("org-def-tlv-list")

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                    self._children_yang_names.add("unknown-tlv-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("chassis_id_len",
                                                    "chassis_id_sub_type",
                                                    "combined_capabilities",
                                                    "port_id_len",
                                                    "port_id_sub_type",
                                                    "rem_index",
                                                    "rem_local_port_num",
                                                    "rem_time_mark") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, self).__setattr__(name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_unknown_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, self).__setattr__(name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("tlv_type",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.tlv_type.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.tlv_type.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-unknown-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.tlv_type.is_set or self.tlv_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_type.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "tlv-type" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "tlv-type"):
                                                self.tlv_type = value
                                                self.tlv_type.value_namespace = name_space
                                                self.tlv_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_unknown_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unknown-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-unknown-tlv-entry"):
                                            for c in self.lldp_unknown_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_unknown_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-unknown-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"

                                        self.lldp_org_def_tlv_entry = YList(self)

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
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, self).__setattr__(name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("oui",
                                                            "tlv_info_indes",
                                                            "tlv_subtype",
                                                            "tlv_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.oui.is_set or
                                                self.tlv_info_indes.is_set or
                                                self.tlv_subtype.is_set or
                                                self.tlv_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.oui.yfilter != YFilter.not_set or
                                                self.tlv_info_indes.yfilter != YFilter.not_set or
                                                self.tlv_subtype.yfilter != YFilter.not_set or
                                                self.tlv_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lldp-org-def-tlv-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.oui.get_name_leafdata())
                                            if (self.tlv_info_indes.is_set or self.tlv_info_indes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_info_indes.get_name_leafdata())
                                            if (self.tlv_subtype.is_set or self.tlv_subtype.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_subtype.get_name_leafdata())
                                            if (self.tlv_value.is_set or self.tlv_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.tlv_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "oui" or name == "tlv-info-indes" or name == "tlv-subtype" or name == "tlv-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "oui"):
                                                self.oui = value
                                                self.oui.value_namespace = name_space
                                                self.oui.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-info-indes"):
                                                self.tlv_info_indes = value
                                                self.tlv_info_indes.value_namespace = name_space
                                                self.tlv_info_indes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-subtype"):
                                                self.tlv_subtype = value
                                                self.tlv_subtype.value_namespace = name_space
                                                self.tlv_subtype.value_namespace_prefix = name_space_prefix
                                            if(value_path == "tlv-value"):
                                                self.tlv_value = value
                                                self.tlv_value.value_namespace = name_space
                                                self.tlv_value.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.lldp_org_def_tlv_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "org-def-tlv-list" + path_buffer

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

                                        if (child_yang_name == "lldp-org-def-tlv-entry"):
                                            for c in self.lldp_org_def_tlv_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.lldp_org_def_tlv_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lldp-org-def-tlv-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.chassis_id_len.is_set or
                                        self.chassis_id_sub_type.is_set or
                                        self.combined_capabilities.is_set or
                                        self.port_id_len.is_set or
                                        self.port_id_sub_type.is_set or
                                        self.rem_index.is_set or
                                        self.rem_local_port_num.is_set or
                                        self.rem_time_mark.is_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_data()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.chassis_id_len.yfilter != YFilter.not_set or
                                        self.chassis_id_sub_type.yfilter != YFilter.not_set or
                                        self.combined_capabilities.yfilter != YFilter.not_set or
                                        self.port_id_len.yfilter != YFilter.not_set or
                                        self.port_id_sub_type.yfilter != YFilter.not_set or
                                        self.rem_index.yfilter != YFilter.not_set or
                                        self.rem_local_port_num.yfilter != YFilter.not_set or
                                        self.rem_time_mark.yfilter != YFilter.not_set or
                                        (self.org_def_tlv_list is not None and self.org_def_tlv_list.has_operation()) or
                                        (self.unknown_tlv_list is not None and self.unknown_tlv_list.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mib" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.chassis_id_len.is_set or self.chassis_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_len.get_name_leafdata())
                                    if (self.chassis_id_sub_type.is_set or self.chassis_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_id_sub_type.get_name_leafdata())
                                    if (self.combined_capabilities.is_set or self.combined_capabilities.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.combined_capabilities.get_name_leafdata())
                                    if (self.port_id_len.is_set or self.port_id_len.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_len.get_name_leafdata())
                                    if (self.port_id_sub_type.is_set or self.port_id_sub_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.port_id_sub_type.get_name_leafdata())
                                    if (self.rem_index.is_set or self.rem_index.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_index.get_name_leafdata())
                                    if (self.rem_local_port_num.is_set or self.rem_local_port_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_local_port_num.get_name_leafdata())
                                    if (self.rem_time_mark.is_set or self.rem_time_mark.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rem_time_mark.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "org-def-tlv-list"):
                                        if (self.org_def_tlv_list is None):
                                            self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList()
                                            self.org_def_tlv_list.parent = self
                                            self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                        return self.org_def_tlv_list

                                    if (child_yang_name == "unknown-tlv-list"):
                                        if (self.unknown_tlv_list is None):
                                            self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList()
                                            self.unknown_tlv_list.parent = self
                                            self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"
                                        return self.unknown_tlv_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "org-def-tlv-list" or name == "unknown-tlv-list" or name == "chassis-id-len" or name == "chassis-id-sub-type" or name == "combined-capabilities" or name == "port-id-len" or name == "port-id-sub-type" or name == "rem-index" or name == "rem-local-port-num" or name == "rem-time-mark"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "chassis-id-len"):
                                        self.chassis_id_len = value
                                        self.chassis_id_len.value_namespace = name_space
                                        self.chassis_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chassis-id-sub-type"):
                                        self.chassis_id_sub_type = value
                                        self.chassis_id_sub_type.value_namespace = name_space
                                        self.chassis_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "combined-capabilities"):
                                        self.combined_capabilities = value
                                        self.combined_capabilities.value_namespace = name_space
                                        self.combined_capabilities.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-len"):
                                        self.port_id_len = value
                                        self.port_id_len.value_namespace = name_space
                                        self.port_id_len.value_namespace_prefix = name_space_prefix
                                    if(value_path == "port-id-sub-type"):
                                        self.port_id_sub_type = value
                                        self.port_id_sub_type.value_namespace = name_space
                                        self.port_id_sub_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-index"):
                                        self.rem_index = value
                                        self.rem_index.value_namespace = name_space
                                        self.rem_index.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-local-port-num"):
                                        self.rem_local_port_num = value
                                        self.rem_local_port_num.value_namespace = name_space
                                        self.rem_local_port_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rem-time-mark"):
                                        self.rem_time_mark = value
                                        self.rem_time_mark.value_namespace = name_space
                                        self.rem_time_mark.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.chassis_id.is_set or
                                    self.device_id.is_set or
                                    self.enabled_capabilities.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id_detail.is_set or
                                    self.receiving_interface_name.is_set or
                                    self.receiving_parent_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()) or
                                    (self.mib is not None and self.mib.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.chassis_id.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.enabled_capabilities.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id_detail.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    self.receiving_parent_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()) or
                                    (self.mib is not None and self.mib.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lldp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.chassis_id.is_set or self.chassis_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.chassis_id.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.enabled_capabilities.is_set or self.enabled_capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled_capabilities.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id_detail.is_set or self.port_id_detail.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id_detail.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())
                                if (self.receiving_parent_interface_name.is_set or self.receiving_parent_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_parent_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                if (child_yang_name == "mib"):
                                    if (self.mib is None):
                                        self.mib = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib()
                                        self.mib.parent = self
                                        self._children_name_map["mib"] = "mib"
                                    return self.mib

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "mib" or name == "chassis-id" or name == "device-id" or name == "enabled-capabilities" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id-detail" or name == "receiving-interface-name" or name == "receiving-parent-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "chassis-id"):
                                    self.chassis_id = value
                                    self.chassis_id.value_namespace = name_space
                                    self.chassis_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled-capabilities"):
                                    self.enabled_capabilities = value
                                    self.enabled_capabilities.value_namespace = name_space
                                    self.enabled_capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "header-version"):
                                    self.header_version = value
                                    self.header_version.value_namespace = name_space
                                    self.header_version.value_namespace_prefix = name_space_prefix
                                if(value_path == "hold-time"):
                                    self.hold_time = value
                                    self.hold_time.value_namespace = name_space
                                    self.hold_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "platform"):
                                    self.platform = value
                                    self.platform.value_namespace = name_space
                                    self.platform.value_namespace_prefix = name_space_prefix
                                if(value_path == "port-id-detail"):
                                    self.port_id_detail = value
                                    self.port_id_detail.value_namespace = name_space
                                    self.port_id_detail.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-parent-interface-name"):
                                    self.receiving_parent_interface_name = value
                                    self.receiving_parent_interface_name.value_namespace = name_space
                                    self.receiving_parent_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.lldp_neighbor:
                                if (c.has_data()):
                                    return True
                            return (
                                self.device_id.is_set or
                                self.interface_name.is_set)

                        def has_operation(self):
                            for c in self.lldp_neighbor:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.device_id.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "summary" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.device_id.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "lldp-neighbor"):
                                for c in self.lldp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.lldp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "lldp-neighbor" or name == "device-id" or name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "device-id"):
                                self.device_id = value
                                self.device_id.value_namespace = name_space
                                self.device_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.summary:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.summary:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "summaries" + path_buffer

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

                        if (child_yang_name == "summary"):
                            for c in self.summary:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Lldp.Nodes.Node.Neighbors.Summaries.Summary()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.summary.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "summary"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.details is not None and self.details.has_data()) or
                        (self.devices is not None and self.devices.has_data()) or
                        (self.summaries is not None and self.summaries.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.details is not None and self.details.has_operation()) or
                        (self.devices is not None and self.devices.has_operation()) or
                        (self.summaries is not None and self.summaries.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbors" + path_buffer

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

                    if (child_yang_name == "details"):
                        if (self.details is None):
                            self.details = Lldp.Nodes.Node.Neighbors.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                        return self.details

                    if (child_yang_name == "devices"):
                        if (self.devices is None):
                            self.devices = Lldp.Nodes.Node.Neighbors.Devices()
                            self.devices.parent = self
                            self._children_name_map["devices"] = "devices"
                        return self.devices

                    if (child_yang_name == "summaries"):
                        if (self.summaries is None):
                            self.summaries = Lldp.Nodes.Node.Neighbors.Summaries()
                            self.summaries.parent = self
                            self._children_name_map["summaries"] = "summaries"
                        return self.summaries

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "details" or name == "devices" or name == "summaries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                The table of interfaces on which LLDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which LLDP is running
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lldp.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

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
                                super(Lldp.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lldp.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Operational data for an interface on which
                    LLDP is running
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: if_index
                    
                    	ifIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: local_network_addresses
                    
                    	Local Management Addresses
                    	**type**\:   :py:class:`LocalNetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses>`
                    
                    .. attribute:: port_description
                    
                    	Port Description
                    	**type**\:  str
                    
                    .. attribute:: port_id
                    
                    	Outgoing port identifier
                    	**type**\:  str
                    
                    .. attribute:: port_id_sub_type
                    
                    	Port ID sub type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_enabled
                    
                    	RX Enabled
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_state
                    
                    	RX State
                    	**type**\:  str
                    
                    .. attribute:: tx_enabled
                    
                    	TX Enabled
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tx_state
                    
                    	TX State
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.if_index = YLeaf(YType.uint32, "if-index")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.port_description = YLeaf(YType.str, "port-description")

                        self.port_id = YLeaf(YType.str, "port-id")

                        self.port_id_sub_type = YLeaf(YType.uint8, "port-id-sub-type")

                        self.rx_enabled = YLeaf(YType.uint8, "rx-enabled")

                        self.rx_state = YLeaf(YType.str, "rx-state")

                        self.tx_enabled = YLeaf(YType.uint8, "tx-enabled")

                        self.tx_state = YLeaf(YType.str, "tx-state")

                        self.local_network_addresses = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses()
                        self.local_network_addresses.parent = self
                        self._children_name_map["local_network_addresses"] = "local-network-addresses"
                        self._children_yang_names.add("local-network-addresses")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "if_index",
                                        "interface_name_xr",
                                        "port_description",
                                        "port_id",
                                        "port_id_sub_type",
                                        "rx_enabled",
                                        "rx_state",
                                        "tx_enabled",
                                        "tx_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Lldp.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lldp.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class LocalNetworkAddresses(Entity):
                        """
                        Local Management Addresses
                        
                        .. attribute:: lldp_addr_entry
                        
                        	lldp addr entry
                        	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, self).__init__()

                            self.yang_name = "local-network-addresses"
                            self.yang_parent_name = "interface"

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
                                        super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, self).__setattr__(name, value)


                        class LldpAddrEntry(Entity):
                            """
                            lldp addr entry
                            
                            .. attribute:: address
                            
                            	Network layer address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address>`
                            
                            .. attribute:: if_num
                            
                            	Interface num
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ma_subtype
                            
                            	MA sub type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, self).__init__()

                                self.yang_name = "lldp-addr-entry"
                                self.yang_parent_name = "local-network-addresses"

                                self.if_num = YLeaf(YType.uint32, "if-num")

                                self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                self.address = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address()
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
                                            super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, self).__setattr__(name, value)


                            class Address(Entity):
                                """
                                Network layer address
                                
                                .. attribute:: address_type
                                
                                	AddressType
                                	**type**\:   :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, self).__init__()

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
                                                super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, self).__setattr__(name, value)

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
                                        self.address = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address()
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
                            path_buffer = "local-network-addresses" + path_buffer

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
                                c = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry()
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
                            self.interface_name.is_set or
                            self.if_index.is_set or
                            self.interface_name_xr.is_set or
                            self.port_description.is_set or
                            self.port_id.is_set or
                            self.port_id_sub_type.is_set or
                            self.rx_enabled.is_set or
                            self.rx_state.is_set or
                            self.tx_enabled.is_set or
                            self.tx_state.is_set or
                            (self.local_network_addresses is not None and self.local_network_addresses.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.if_index.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.port_description.yfilter != YFilter.not_set or
                            self.port_id.yfilter != YFilter.not_set or
                            self.port_id_sub_type.yfilter != YFilter.not_set or
                            self.rx_enabled.yfilter != YFilter.not_set or
                            self.rx_state.yfilter != YFilter.not_set or
                            self.tx_enabled.yfilter != YFilter.not_set or
                            self.tx_state.yfilter != YFilter.not_set or
                            (self.local_network_addresses is not None and self.local_network_addresses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_index.get_name_leafdata())
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.port_description.is_set or self.port_description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_description.get_name_leafdata())
                        if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_id.get_name_leafdata())
                        if (self.port_id_sub_type.is_set or self.port_id_sub_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_id_sub_type.get_name_leafdata())
                        if (self.rx_enabled.is_set or self.rx_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_enabled.get_name_leafdata())
                        if (self.rx_state.is_set or self.rx_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rx_state.get_name_leafdata())
                        if (self.tx_enabled.is_set or self.tx_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_enabled.get_name_leafdata())
                        if (self.tx_state.is_set or self.tx_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local-network-addresses"):
                            if (self.local_network_addresses is None):
                                self.local_network_addresses = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses()
                                self.local_network_addresses.parent = self
                                self._children_name_map["local_network_addresses"] = "local-network-addresses"
                            return self.local_network_addresses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-network-addresses" or name == "interface-name" or name == "if-index" or name == "interface-name-xr" or name == "port-description" or name == "port-id" or name == "port-id-sub-type" or name == "rx-enabled" or name == "rx-state" or name == "tx-enabled" or name == "tx-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "if-index"):
                            self.if_index = value
                            self.if_index.value_namespace = name_space
                            self.if_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-description"):
                            self.port_description = value
                            self.port_description.value_namespace = name_space
                            self.port_description.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-id"):
                            self.port_id = value
                            self.port_id.value_namespace = name_space
                            self.port_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-id-sub-type"):
                            self.port_id_sub_type = value
                            self.port_id_sub_type.value_namespace = name_space
                            self.port_id_sub_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-enabled"):
                            self.rx_enabled = value
                            self.rx_enabled.value_namespace = name_space
                            self.rx_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "rx-state"):
                            self.rx_state = value
                            self.rx_state.value_namespace = name_space
                            self.rx_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-enabled"):
                            self.tx_enabled = value
                            self.tx_enabled.value_namespace = name_space
                            self.tx_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-state"):
                            self.tx_state = value
                            self.tx_state.value_namespace = name_space
                            self.tx_state.value_namespace_prefix = name_space_prefix

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Lldp.Nodes.Node.Interfaces.Interface()
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


            class Statistics(Entity):
                """
                The LLDP traffic statistics for this node
                
                .. attribute:: aged_out_entries
                
                	Aged out entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_packets
                
                	Bad packet received and dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_packets
                
                	Discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_tl_vs
                
                	Discarded TLVs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: queue_overflow_errors
                
                	Queue overflows
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: table_overflow_errors
                
                	Table overflows
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unrecognized_tl_vs
                
                	Unrecognized TLVs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lldp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.aged_out_entries = YLeaf(YType.uint32, "aged-out-entries")

                    self.bad_packets = YLeaf(YType.uint32, "bad-packets")

                    self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                    self.discarded_tl_vs = YLeaf(YType.uint32, "discarded-tl-vs")

                    self.encapsulation_errors = YLeaf(YType.uint32, "encapsulation-errors")

                    self.out_of_memory_errors = YLeaf(YType.uint32, "out-of-memory-errors")

                    self.queue_overflow_errors = YLeaf(YType.uint32, "queue-overflow-errors")

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.table_overflow_errors = YLeaf(YType.uint32, "table-overflow-errors")

                    self.transmitted_packets = YLeaf(YType.uint32, "transmitted-packets")

                    self.unrecognized_tl_vs = YLeaf(YType.uint32, "unrecognized-tl-vs")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aged_out_entries",
                                    "bad_packets",
                                    "discarded_packets",
                                    "discarded_tl_vs",
                                    "encapsulation_errors",
                                    "out_of_memory_errors",
                                    "queue_overflow_errors",
                                    "received_packets",
                                    "table_overflow_errors",
                                    "transmitted_packets",
                                    "unrecognized_tl_vs") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Lldp.Nodes.Node.Statistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lldp.Nodes.Node.Statistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.aged_out_entries.is_set or
                        self.bad_packets.is_set or
                        self.discarded_packets.is_set or
                        self.discarded_tl_vs.is_set or
                        self.encapsulation_errors.is_set or
                        self.out_of_memory_errors.is_set or
                        self.queue_overflow_errors.is_set or
                        self.received_packets.is_set or
                        self.table_overflow_errors.is_set or
                        self.transmitted_packets.is_set or
                        self.unrecognized_tl_vs.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aged_out_entries.yfilter != YFilter.not_set or
                        self.bad_packets.yfilter != YFilter.not_set or
                        self.discarded_packets.yfilter != YFilter.not_set or
                        self.discarded_tl_vs.yfilter != YFilter.not_set or
                        self.encapsulation_errors.yfilter != YFilter.not_set or
                        self.out_of_memory_errors.yfilter != YFilter.not_set or
                        self.queue_overflow_errors.yfilter != YFilter.not_set or
                        self.received_packets.yfilter != YFilter.not_set or
                        self.table_overflow_errors.yfilter != YFilter.not_set or
                        self.transmitted_packets.yfilter != YFilter.not_set or
                        self.unrecognized_tl_vs.yfilter != YFilter.not_set)

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
                    if (self.aged_out_entries.is_set or self.aged_out_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aged_out_entries.get_name_leafdata())
                    if (self.bad_packets.is_set or self.bad_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_packets.get_name_leafdata())
                    if (self.discarded_packets.is_set or self.discarded_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_packets.get_name_leafdata())
                    if (self.discarded_tl_vs.is_set or self.discarded_tl_vs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_tl_vs.get_name_leafdata())
                    if (self.encapsulation_errors.is_set or self.encapsulation_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encapsulation_errors.get_name_leafdata())
                    if (self.out_of_memory_errors.is_set or self.out_of_memory_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_memory_errors.get_name_leafdata())
                    if (self.queue_overflow_errors.is_set or self.queue_overflow_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.queue_overflow_errors.get_name_leafdata())
                    if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets.get_name_leafdata())
                    if (self.table_overflow_errors.is_set or self.table_overflow_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.table_overflow_errors.get_name_leafdata())
                    if (self.transmitted_packets.is_set or self.transmitted_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmitted_packets.get_name_leafdata())
                    if (self.unrecognized_tl_vs.is_set or self.unrecognized_tl_vs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unrecognized_tl_vs.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aged-out-entries" or name == "bad-packets" or name == "discarded-packets" or name == "discarded-tl-vs" or name == "encapsulation-errors" or name == "out-of-memory-errors" or name == "queue-overflow-errors" or name == "received-packets" or name == "table-overflow-errors" or name == "transmitted-packets" or name == "unrecognized-tl-vs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aged-out-entries"):
                        self.aged_out_entries = value
                        self.aged_out_entries.value_namespace = name_space
                        self.aged_out_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "bad-packets"):
                        self.bad_packets = value
                        self.bad_packets.value_namespace = name_space
                        self.bad_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "discarded-packets"):
                        self.discarded_packets = value
                        self.discarded_packets.value_namespace = name_space
                        self.discarded_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "discarded-tl-vs"):
                        self.discarded_tl_vs = value
                        self.discarded_tl_vs.value_namespace = name_space
                        self.discarded_tl_vs.value_namespace_prefix = name_space_prefix
                    if(value_path == "encapsulation-errors"):
                        self.encapsulation_errors = value
                        self.encapsulation_errors.value_namespace = name_space
                        self.encapsulation_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-memory-errors"):
                        self.out_of_memory_errors = value
                        self.out_of_memory_errors.value_namespace = name_space
                        self.out_of_memory_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "queue-overflow-errors"):
                        self.queue_overflow_errors = value
                        self.queue_overflow_errors.value_namespace = name_space
                        self.queue_overflow_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets"):
                        self.received_packets = value
                        self.received_packets.value_namespace = name_space
                        self.received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "table-overflow-errors"):
                        self.table_overflow_errors = value
                        self.table_overflow_errors.value_namespace = name_space
                        self.table_overflow_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmitted-packets"):
                        self.transmitted_packets = value
                        self.transmitted_packets.value_namespace = name_space
                        self.transmitted_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "unrecognized-tl-vs"):
                        self.unrecognized_tl_vs = value
                        self.unrecognized_tl_vs.value_namespace = name_space
                        self.unrecognized_tl_vs.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.neighbors is not None and self.neighbors.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.neighbors is not None and self.neighbors.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-oper:lldp/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Lldp.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "neighbors"):
                    if (self.neighbors is None):
                        self.neighbors = Lldp.Nodes.Node.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                    return self.neighbors

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Lldp.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interfaces" or name == "neighbors" or name == "statistics" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Lldp.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.global_lldp is not None and self.global_lldp.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.global_lldp is not None and self.global_lldp.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ethernet-lldp-oper:lldp" + path_buffer

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

        if (child_yang_name == "global-lldp"):
            if (self.global_lldp is None):
                self.global_lldp = Lldp.GlobalLldp()
                self.global_lldp.parent = self
                self._children_name_map["global_lldp"] = "global-lldp"
            return self.global_lldp

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Lldp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "global-lldp" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity

