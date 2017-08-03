""" Cisco_IOS_XR_cdp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package operational data.

This module contains definitions
for the following management objects\:
  cdp\: CDP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CdpDuplex(Enum):
    """
    CdpDuplex

    Cdp duplex

    .. data:: cdp_dplx_none = 0

    	cdp dplx none

    .. data:: cdp_dplx_half = 1

    	cdp dplx half

    .. data:: cdp_dplx_full = 2

    	cdp dplx full

    """

    cdp_dplx_none = Enum.YLeaf(0, "cdp-dplx-none")

    cdp_dplx_half = Enum.YLeaf(1, "cdp-dplx-half")

    cdp_dplx_full = Enum.YLeaf(2, "cdp-dplx-full")


class CdpL3AddrProtocol(Enum):
    """
    CdpL3AddrProtocol

    Cdp l3 addr protocol

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")



class Cdp(Entity):
    """
    CDP operational data
    
    .. attribute:: nodes
    
    	Per node CDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes>`
    
    

    """

    _prefix = 'cdp-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(Cdp, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp"
        self.yang_parent_name = "Cisco-IOS-XR-cdp-oper"

        self.nodes = Cdp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Per node CDP operational data
        
        .. attribute:: node
        
        	The CDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node>`
        
        

        """

        _prefix = 'cdp-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Cdp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cdp"

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
                        super(Cdp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Cdp.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The CDP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	The table of interfaces on which CDP is running on this node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces>`
            
            .. attribute:: neighbors
            
            	The CDP neighbor tables on this node
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors>`
            
            .. attribute:: statistics
            
            	The CDP traffic statistics for this node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'cdp-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Cdp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interfaces = Cdp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.neighbors = Cdp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")

                self.statistics = Cdp.Nodes.Node.Statistics()
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
                            super(Cdp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Cdp.Nodes.Node, self).__setattr__(name, value)


            class Neighbors(Entity):
                """
                The CDP neighbor tables on this node
                
                .. attribute:: details
                
                	The detailed CDP neighbor table
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: devices
                
                	The detailed CDP neighbor table
                	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: summaries
                
                	The CDP neighbor summary table
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "node"

                    self.details = Cdp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                    self._children_yang_names.add("details")

                    self.devices = Cdp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self._children_name_map["devices"] = "devices"
                    self._children_yang_names.add("devices")

                    self.summaries = Cdp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._children_yang_names.add("summaries")


                class Details(Entity):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Details, self).__init__()

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
                                    super(Cdp.Nodes.Node.Neighbors.Details, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Cdp.Nodes.Node.Neighbors.Details, self).__setattr__(name, value)


                    class Detail(Entity):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor>`
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Details.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "details"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.cdp_neighbor = YList(self)

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
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail, self).__setattr__(name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "detail"

                                self.capabilities = YLeaf(YType.str, "capabilities")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id = YLeaf(YType.str, "port-id")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.detail = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("capabilities",
                                                "device_id",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id",
                                                "receiving_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"

                                    self.duplex = YLeaf(YType.enumeration, "duplex")

                                    self.native_vlan = YLeaf(YType.uint32, "native-vlan")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.version = YLeaf(YType.str, "version")

                                    self.vtp_domain = YLeaf(YType.str, "vtp-domain")

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._children_yang_names.add("network-addresses")

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._children_yang_names.add("protocol-hello-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("duplex",
                                                    "native_vlan",
                                                    "system_name",
                                                    "version",
                                                    "vtp_domain") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

                                        self.cdp_addr_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.address = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"

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
                                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)

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
                                            return (self.address is not None and self.address.has_data())

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                (self.address is not None and self.address.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-addr-entry" + path_buffer

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

                                            if (child_yang_name == "address"):
                                                if (self.address is None):
                                                    self.address = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                                    self.address.parent = self
                                                    self._children_name_map["address"] = "address"
                                                return self.address

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        for c in self.cdp_addr_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_addr_entry:
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

                                        if (child_yang_name == "cdp-addr-entry"):
                                            for c in self.cdp_addr_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_addr_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-addr-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"

                                        self.cdp_prot_hello_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"

                                            self.hello_message = YLeaf(YType.str, "hello-message")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("hello_message") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.hello_message.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.hello_message.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-prot-hello-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.hello_message.is_set or self.hello_message.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hello_message.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "hello-message"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "hello-message"):
                                                self.hello_message = value
                                                self.hello_message.value_namespace = name_space
                                                self.hello_message.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "protocol-hello-list" + path_buffer

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

                                        if (child_yang_name == "cdp-prot-hello-entry"):
                                            for c in self.cdp_prot_hello_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_prot_hello_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-prot-hello-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.duplex.is_set or
                                        self.native_vlan.is_set or
                                        self.system_name.is_set or
                                        self.version.is_set or
                                        self.vtp_domain.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.duplex.yfilter != YFilter.not_set or
                                        self.native_vlan.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.version.yfilter != YFilter.not_set or
                                        self.vtp_domain.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_operation()))

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
                                    if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.duplex.get_name_leafdata())
                                    if (self.native_vlan.is_set or self.native_vlan.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.native_vlan.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.version.get_name_leafdata())
                                    if (self.vtp_domain.is_set or self.vtp_domain.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vtp_domain.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    if (child_yang_name == "protocol-hello-list"):
                                        if (self.protocol_hello_list is None):
                                            self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail.ProtocolHelloList()
                                            self.protocol_hello_list.parent = self
                                            self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                        return self.protocol_hello_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "protocol-hello-list" or name == "duplex" or name == "native-vlan" or name == "system-name" or name == "version" or name == "vtp-domain"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "duplex"):
                                        self.duplex = value
                                        self.duplex.value_namespace = name_space
                                        self.duplex.value_namespace_prefix = name_space_prefix
                                    if(value_path == "native-vlan"):
                                        self.native_vlan = value
                                        self.native_vlan.value_namespace = name_space
                                        self.native_vlan.value_namespace_prefix = name_space_prefix
                                    if(value_path == "system-name"):
                                        self.system_name = value
                                        self.system_name.value_namespace = name_space
                                        self.system_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "version"):
                                        self.version = value
                                        self.version.value_namespace = name_space
                                        self.version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vtp-domain"):
                                        self.vtp_domain = value
                                        self.vtp_domain.value_namespace = name_space
                                        self.vtp_domain.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.capabilities.is_set or
                                    self.device_id.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id.is_set or
                                    self.receiving_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.capabilities.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "cdp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.capabilities.is_set or self.capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.capabilities.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "capabilities" or name == "device-id" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id" or name == "receiving-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "capabilities"):
                                    self.capabilities = value
                                    self.capabilities.value_namespace = name_space
                                    self.capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "port-id"):
                                    self.port_id = value
                                    self.port_id.value_namespace = name_space
                                    self.port_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.cdp_neighbor:
                                if (c.has_data()):
                                    return True
                            return (
                                self.device_id.is_set or
                                self.interface_name.is_set)

                        def has_operation(self):
                            for c in self.cdp_neighbor:
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

                            if (child_yang_name == "cdp-neighbor"):
                                for c in self.cdp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.cdp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cdp-neighbor" or name == "device-id" or name == "interface-name"):
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
                            c = Cdp.Nodes.Node.Neighbors.Details.Detail()
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


                class Devices(Entity):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: device
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Devices, self).__init__()

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
                                    super(Cdp.Nodes.Node.Neighbors.Devices, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Cdp.Nodes.Node.Neighbors.Devices, self).__setattr__(name, value)


                    class Device(Entity):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: device_id  <key>
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor>`
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Devices.Device, self).__init__()

                            self.yang_name = "device"
                            self.yang_parent_name = "devices"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.cdp_neighbor = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("device_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device, self).__setattr__(name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "device"

                                self.capabilities = YLeaf(YType.str, "capabilities")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id = YLeaf(YType.str, "port-id")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.detail = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("capabilities",
                                                "device_id",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id",
                                                "receiving_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"

                                    self.duplex = YLeaf(YType.enumeration, "duplex")

                                    self.native_vlan = YLeaf(YType.uint32, "native-vlan")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.version = YLeaf(YType.str, "version")

                                    self.vtp_domain = YLeaf(YType.str, "vtp-domain")

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._children_yang_names.add("network-addresses")

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._children_yang_names.add("protocol-hello-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("duplex",
                                                    "native_vlan",
                                                    "system_name",
                                                    "version",
                                                    "vtp_domain") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

                                        self.cdp_addr_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.address = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"

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
                                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)

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
                                            return (self.address is not None and self.address.has_data())

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                (self.address is not None and self.address.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-addr-entry" + path_buffer

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

                                            if (child_yang_name == "address"):
                                                if (self.address is None):
                                                    self.address = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                                    self.address.parent = self
                                                    self._children_name_map["address"] = "address"
                                                return self.address

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        for c in self.cdp_addr_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_addr_entry:
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

                                        if (child_yang_name == "cdp-addr-entry"):
                                            for c in self.cdp_addr_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_addr_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-addr-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"

                                        self.cdp_prot_hello_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"

                                            self.hello_message = YLeaf(YType.str, "hello-message")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("hello_message") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.hello_message.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.hello_message.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-prot-hello-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.hello_message.is_set or self.hello_message.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hello_message.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "hello-message"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "hello-message"):
                                                self.hello_message = value
                                                self.hello_message.value_namespace = name_space
                                                self.hello_message.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "protocol-hello-list" + path_buffer

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

                                        if (child_yang_name == "cdp-prot-hello-entry"):
                                            for c in self.cdp_prot_hello_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_prot_hello_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-prot-hello-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.duplex.is_set or
                                        self.native_vlan.is_set or
                                        self.system_name.is_set or
                                        self.version.is_set or
                                        self.vtp_domain.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.duplex.yfilter != YFilter.not_set or
                                        self.native_vlan.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.version.yfilter != YFilter.not_set or
                                        self.vtp_domain.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_operation()))

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
                                    if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.duplex.get_name_leafdata())
                                    if (self.native_vlan.is_set or self.native_vlan.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.native_vlan.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.version.get_name_leafdata())
                                    if (self.vtp_domain.is_set or self.vtp_domain.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vtp_domain.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    if (child_yang_name == "protocol-hello-list"):
                                        if (self.protocol_hello_list is None):
                                            self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList()
                                            self.protocol_hello_list.parent = self
                                            self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                        return self.protocol_hello_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "protocol-hello-list" or name == "duplex" or name == "native-vlan" or name == "system-name" or name == "version" or name == "vtp-domain"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "duplex"):
                                        self.duplex = value
                                        self.duplex.value_namespace = name_space
                                        self.duplex.value_namespace_prefix = name_space_prefix
                                    if(value_path == "native-vlan"):
                                        self.native_vlan = value
                                        self.native_vlan.value_namespace = name_space
                                        self.native_vlan.value_namespace_prefix = name_space_prefix
                                    if(value_path == "system-name"):
                                        self.system_name = value
                                        self.system_name.value_namespace = name_space
                                        self.system_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "version"):
                                        self.version = value
                                        self.version.value_namespace = name_space
                                        self.version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vtp-domain"):
                                        self.vtp_domain = value
                                        self.vtp_domain.value_namespace = name_space
                                        self.vtp_domain.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.capabilities.is_set or
                                    self.device_id.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id.is_set or
                                    self.receiving_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.capabilities.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "cdp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.capabilities.is_set or self.capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.capabilities.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "capabilities" or name == "device-id" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id" or name == "receiving-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "capabilities"):
                                    self.capabilities = value
                                    self.capabilities.value_namespace = name_space
                                    self.capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "port-id"):
                                    self.port_id = value
                                    self.port_id.value_namespace = name_space
                                    self.port_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.cdp_neighbor:
                                if (c.has_data()):
                                    return True
                            return self.device_id.is_set

                        def has_operation(self):
                            for c in self.cdp_neighbor:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.device_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "device" + "[device-id='" + self.device_id.get() + "']" + path_buffer

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

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "cdp-neighbor"):
                                for c in self.cdp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.cdp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cdp-neighbor" or name == "device-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "device-id"):
                                self.device_id = value
                                self.device_id.value_namespace = name_space
                                self.device_id.value_namespace_prefix = name_space_prefix

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
                            c = Cdp.Nodes.Node.Neighbors.Devices.Device()
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


                class Summaries(Entity):
                    """
                    The CDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Summaries, self).__init__()

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
                                    super(Cdp.Nodes.Node.Neighbors.Summaries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Cdp.Nodes.Node.Neighbors.Summaries, self).__setattr__(name, value)


                    class Summary(Entity):
                        """
                        Brief information about a CDP neighbor entry
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor>`
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.cdp_neighbor = YList(self)

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
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary, self).__setattr__(name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "summary"

                                self.capabilities = YLeaf(YType.str, "capabilities")

                                self.device_id = YLeaf(YType.str, "device-id")

                                self.header_version = YLeaf(YType.uint8, "header-version")

                                self.hold_time = YLeaf(YType.uint16, "hold-time")

                                self.platform = YLeaf(YType.str, "platform")

                                self.port_id = YLeaf(YType.str, "port-id")

                                self.receiving_interface_name = YLeaf(YType.str, "receiving-interface-name")

                                self.detail = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("capabilities",
                                                "device_id",
                                                "header_version",
                                                "hold_time",
                                                "platform",
                                                "port_id",
                                                "receiving_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"

                                    self.duplex = YLeaf(YType.enumeration, "duplex")

                                    self.native_vlan = YLeaf(YType.uint32, "native-vlan")

                                    self.system_name = YLeaf(YType.str, "system-name")

                                    self.version = YLeaf(YType.str, "version")

                                    self.vtp_domain = YLeaf(YType.str, "vtp-domain")

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._children_yang_names.add("network-addresses")

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._children_yang_names.add("protocol-hello-list")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("duplex",
                                                    "native_vlan",
                                                    "system_name",
                                                    "version",
                                                    "vtp_domain") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail, self).__setattr__(name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"

                                        self.cdp_addr_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses, self).__setattr__(name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"

                                            self.address = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"

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
                                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__setattr__(name, value)

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
                                            return (self.address is not None and self.address.has_data())

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                (self.address is not None and self.address.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-addr-entry" + path_buffer

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

                                            if (child_yang_name == "address"):
                                                if (self.address is None):
                                                    self.address = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                                    self.address.parent = self
                                                    self._children_name_map["address"] = "address"
                                                return self.address

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        for c in self.cdp_addr_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_addr_entry:
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

                                        if (child_yang_name == "cdp-addr-entry"):
                                            for c in self.cdp_addr_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_addr_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-addr-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"

                                        self.cdp_prot_hello_entry = YList(self)

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
                                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList, self).__setattr__(name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"

                                            self.hello_message = YLeaf(YType.str, "hello-message")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("hello_message") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.hello_message.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.hello_message.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "cdp-prot-hello-entry" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.hello_message.is_set or self.hello_message.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hello_message.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "hello-message"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "hello-message"):
                                                self.hello_message = value
                                                self.hello_message.value_namespace = name_space
                                                self.hello_message.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.cdp_prot_hello_entry:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "protocol-hello-list" + path_buffer

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

                                        if (child_yang_name == "cdp-prot-hello-entry"):
                                            for c in self.cdp_prot_hello_entry:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.cdp_prot_hello_entry.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "cdp-prot-hello-entry"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.duplex.is_set or
                                        self.native_vlan.is_set or
                                        self.system_name.is_set or
                                        self.version.is_set or
                                        self.vtp_domain.is_set or
                                        (self.network_addresses is not None and self.network_addresses.has_data()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.duplex.yfilter != YFilter.not_set or
                                        self.native_vlan.yfilter != YFilter.not_set or
                                        self.system_name.yfilter != YFilter.not_set or
                                        self.version.yfilter != YFilter.not_set or
                                        self.vtp_domain.yfilter != YFilter.not_set or
                                        (self.network_addresses is not None and self.network_addresses.has_operation()) or
                                        (self.protocol_hello_list is not None and self.protocol_hello_list.has_operation()))

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
                                    if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.duplex.get_name_leafdata())
                                    if (self.native_vlan.is_set or self.native_vlan.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.native_vlan.get_name_leafdata())
                                    if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.system_name.get_name_leafdata())
                                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.version.get_name_leafdata())
                                    if (self.vtp_domain.is_set or self.vtp_domain.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vtp_domain.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "network-addresses"):
                                        if (self.network_addresses is None):
                                            self.network_addresses = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses()
                                            self.network_addresses.parent = self
                                            self._children_name_map["network_addresses"] = "network-addresses"
                                        return self.network_addresses

                                    if (child_yang_name == "protocol-hello-list"):
                                        if (self.protocol_hello_list is None):
                                            self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList()
                                            self.protocol_hello_list.parent = self
                                            self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                        return self.protocol_hello_list

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "network-addresses" or name == "protocol-hello-list" or name == "duplex" or name == "native-vlan" or name == "system-name" or name == "version" or name == "vtp-domain"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "duplex"):
                                        self.duplex = value
                                        self.duplex.value_namespace = name_space
                                        self.duplex.value_namespace_prefix = name_space_prefix
                                    if(value_path == "native-vlan"):
                                        self.native_vlan = value
                                        self.native_vlan.value_namespace = name_space
                                        self.native_vlan.value_namespace_prefix = name_space_prefix
                                    if(value_path == "system-name"):
                                        self.system_name = value
                                        self.system_name.value_namespace = name_space
                                        self.system_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "version"):
                                        self.version = value
                                        self.version.value_namespace = name_space
                                        self.version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vtp-domain"):
                                        self.vtp_domain = value
                                        self.vtp_domain.value_namespace = name_space
                                        self.vtp_domain.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.capabilities.is_set or
                                    self.device_id.is_set or
                                    self.header_version.is_set or
                                    self.hold_time.is_set or
                                    self.platform.is_set or
                                    self.port_id.is_set or
                                    self.receiving_interface_name.is_set or
                                    (self.detail is not None and self.detail.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.capabilities.yfilter != YFilter.not_set or
                                    self.device_id.yfilter != YFilter.not_set or
                                    self.header_version.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.platform.yfilter != YFilter.not_set or
                                    self.port_id.yfilter != YFilter.not_set or
                                    self.receiving_interface_name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "cdp-neighbor" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.capabilities.is_set or self.capabilities.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.capabilities.get_name_leafdata())
                                if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.device_id.get_name_leafdata())
                                if (self.header_version.is_set or self.header_version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.header_version.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.platform.is_set or self.platform.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.platform.get_name_leafdata())
                                if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_id.get_name_leafdata())
                                if (self.receiving_interface_name.is_set or self.receiving_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.receiving_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "capabilities" or name == "device-id" or name == "header-version" or name == "hold-time" or name == "platform" or name == "port-id" or name == "receiving-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "capabilities"):
                                    self.capabilities = value
                                    self.capabilities.value_namespace = name_space
                                    self.capabilities.value_namespace_prefix = name_space_prefix
                                if(value_path == "device-id"):
                                    self.device_id = value
                                    self.device_id.value_namespace = name_space
                                    self.device_id.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "port-id"):
                                    self.port_id = value
                                    self.port_id.value_namespace = name_space
                                    self.port_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "receiving-interface-name"):
                                    self.receiving_interface_name = value
                                    self.receiving_interface_name.value_namespace = name_space
                                    self.receiving_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.cdp_neighbor:
                                if (c.has_data()):
                                    return True
                            return (
                                self.device_id.is_set or
                                self.interface_name.is_set)

                        def has_operation(self):
                            for c in self.cdp_neighbor:
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

                            if (child_yang_name == "cdp-neighbor"):
                                for c in self.cdp_neighbor:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.cdp_neighbor.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "cdp-neighbor" or name == "device-id" or name == "interface-name"):
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
                            c = Cdp.Nodes.Node.Neighbors.Summaries.Summary()
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
                            self.details = Cdp.Nodes.Node.Neighbors.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                        return self.details

                    if (child_yang_name == "devices"):
                        if (self.devices is None):
                            self.devices = Cdp.Nodes.Node.Neighbors.Devices()
                            self.devices.parent = self
                            self._children_name_map["devices"] = "devices"
                        return self.devices

                    if (child_yang_name == "summaries"):
                        if (self.summaries is None):
                            self.summaries = Cdp.Nodes.Node.Neighbors.Summaries()
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


            class Statistics(Entity):
                """
                The CDP traffic statistics for this node
                
                .. attribute:: bad_packet_errors
                
                	Bad packet received and dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: checksum_errors
                
                	Checksum errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_errors
                
                	Header syntax errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_version_errors
                
                	Can't handle receive version
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: open_file_errors
                
                	Cannot open file
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v1
                
                	Received v1 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v2
                
                	Received v2 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v1
                
                	Transmitted v1 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v2
                
                	Transmitted v2 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: truncated_packet_errors
                
                	Truncated messages
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.bad_packet_errors = YLeaf(YType.uint32, "bad-packet-errors")

                    self.checksum_errors = YLeaf(YType.uint32, "checksum-errors")

                    self.encapsulation_errors = YLeaf(YType.uint32, "encapsulation-errors")

                    self.header_errors = YLeaf(YType.uint32, "header-errors")

                    self.header_version_errors = YLeaf(YType.uint32, "header-version-errors")

                    self.open_file_errors = YLeaf(YType.uint32, "open-file-errors")

                    self.out_of_memory_errors = YLeaf(YType.uint32, "out-of-memory-errors")

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.received_packets_v1 = YLeaf(YType.uint32, "received-packets-v1")

                    self.received_packets_v2 = YLeaf(YType.uint32, "received-packets-v2")

                    self.transmitted_packets = YLeaf(YType.uint32, "transmitted-packets")

                    self.transmitted_packets_v1 = YLeaf(YType.uint32, "transmitted-packets-v1")

                    self.transmitted_packets_v2 = YLeaf(YType.uint32, "transmitted-packets-v2")

                    self.truncated_packet_errors = YLeaf(YType.uint32, "truncated-packet-errors")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bad_packet_errors",
                                    "checksum_errors",
                                    "encapsulation_errors",
                                    "header_errors",
                                    "header_version_errors",
                                    "open_file_errors",
                                    "out_of_memory_errors",
                                    "received_packets",
                                    "received_packets_v1",
                                    "received_packets_v2",
                                    "transmitted_packets",
                                    "transmitted_packets_v1",
                                    "transmitted_packets_v2",
                                    "truncated_packet_errors") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Cdp.Nodes.Node.Statistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Cdp.Nodes.Node.Statistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bad_packet_errors.is_set or
                        self.checksum_errors.is_set or
                        self.encapsulation_errors.is_set or
                        self.header_errors.is_set or
                        self.header_version_errors.is_set or
                        self.open_file_errors.is_set or
                        self.out_of_memory_errors.is_set or
                        self.received_packets.is_set or
                        self.received_packets_v1.is_set or
                        self.received_packets_v2.is_set or
                        self.transmitted_packets.is_set or
                        self.transmitted_packets_v1.is_set or
                        self.transmitted_packets_v2.is_set or
                        self.truncated_packet_errors.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bad_packet_errors.yfilter != YFilter.not_set or
                        self.checksum_errors.yfilter != YFilter.not_set or
                        self.encapsulation_errors.yfilter != YFilter.not_set or
                        self.header_errors.yfilter != YFilter.not_set or
                        self.header_version_errors.yfilter != YFilter.not_set or
                        self.open_file_errors.yfilter != YFilter.not_set or
                        self.out_of_memory_errors.yfilter != YFilter.not_set or
                        self.received_packets.yfilter != YFilter.not_set or
                        self.received_packets_v1.yfilter != YFilter.not_set or
                        self.received_packets_v2.yfilter != YFilter.not_set or
                        self.transmitted_packets.yfilter != YFilter.not_set or
                        self.transmitted_packets_v1.yfilter != YFilter.not_set or
                        self.transmitted_packets_v2.yfilter != YFilter.not_set or
                        self.truncated_packet_errors.yfilter != YFilter.not_set)

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
                    if (self.bad_packet_errors.is_set or self.bad_packet_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_packet_errors.get_name_leafdata())
                    if (self.checksum_errors.is_set or self.checksum_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.checksum_errors.get_name_leafdata())
                    if (self.encapsulation_errors.is_set or self.encapsulation_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encapsulation_errors.get_name_leafdata())
                    if (self.header_errors.is_set or self.header_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.header_errors.get_name_leafdata())
                    if (self.header_version_errors.is_set or self.header_version_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.header_version_errors.get_name_leafdata())
                    if (self.open_file_errors.is_set or self.open_file_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.open_file_errors.get_name_leafdata())
                    if (self.out_of_memory_errors.is_set or self.out_of_memory_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_memory_errors.get_name_leafdata())
                    if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets.get_name_leafdata())
                    if (self.received_packets_v1.is_set or self.received_packets_v1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets_v1.get_name_leafdata())
                    if (self.received_packets_v2.is_set or self.received_packets_v2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets_v2.get_name_leafdata())
                    if (self.transmitted_packets.is_set or self.transmitted_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmitted_packets.get_name_leafdata())
                    if (self.transmitted_packets_v1.is_set or self.transmitted_packets_v1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmitted_packets_v1.get_name_leafdata())
                    if (self.transmitted_packets_v2.is_set or self.transmitted_packets_v2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmitted_packets_v2.get_name_leafdata())
                    if (self.truncated_packet_errors.is_set or self.truncated_packet_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.truncated_packet_errors.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bad-packet-errors" or name == "checksum-errors" or name == "encapsulation-errors" or name == "header-errors" or name == "header-version-errors" or name == "open-file-errors" or name == "out-of-memory-errors" or name == "received-packets" or name == "received-packets-v1" or name == "received-packets-v2" or name == "transmitted-packets" or name == "transmitted-packets-v1" or name == "transmitted-packets-v2" or name == "truncated-packet-errors"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bad-packet-errors"):
                        self.bad_packet_errors = value
                        self.bad_packet_errors.value_namespace = name_space
                        self.bad_packet_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "checksum-errors"):
                        self.checksum_errors = value
                        self.checksum_errors.value_namespace = name_space
                        self.checksum_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "encapsulation-errors"):
                        self.encapsulation_errors = value
                        self.encapsulation_errors.value_namespace = name_space
                        self.encapsulation_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "header-errors"):
                        self.header_errors = value
                        self.header_errors.value_namespace = name_space
                        self.header_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "header-version-errors"):
                        self.header_version_errors = value
                        self.header_version_errors.value_namespace = name_space
                        self.header_version_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "open-file-errors"):
                        self.open_file_errors = value
                        self.open_file_errors.value_namespace = name_space
                        self.open_file_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-memory-errors"):
                        self.out_of_memory_errors = value
                        self.out_of_memory_errors.value_namespace = name_space
                        self.out_of_memory_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets"):
                        self.received_packets = value
                        self.received_packets.value_namespace = name_space
                        self.received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets-v1"):
                        self.received_packets_v1 = value
                        self.received_packets_v1.value_namespace = name_space
                        self.received_packets_v1.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets-v2"):
                        self.received_packets_v2 = value
                        self.received_packets_v2.value_namespace = name_space
                        self.received_packets_v2.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmitted-packets"):
                        self.transmitted_packets = value
                        self.transmitted_packets.value_namespace = name_space
                        self.transmitted_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmitted-packets-v1"):
                        self.transmitted_packets_v1 = value
                        self.transmitted_packets_v1.value_namespace = name_space
                        self.transmitted_packets_v1.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmitted-packets-v2"):
                        self.transmitted_packets_v2 = value
                        self.transmitted_packets_v2.value_namespace = name_space
                        self.transmitted_packets_v2.value_namespace_prefix = name_space_prefix
                    if(value_path == "truncated-packet-errors"):
                        self.truncated_packet_errors = value
                        self.truncated_packet_errors.value_namespace = name_space
                        self.truncated_packet_errors.value_namespace_prefix = name_space_prefix


            class Interfaces(Entity):
                """
                The table of interfaces on which CDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which CDP is running
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Interfaces, self).__init__()

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
                                super(Cdp.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Cdp.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Operational data for an interface on which
                    CDP is running
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: basecaps_state
                    
                    	Interface basecaps state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdp_protocol_state
                    
                    	CDP protocol state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_encaps
                    
                    	Interface encapsulation
                    	**type**\:  str
                    
                    .. attribute:: interface_handle
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.basecaps_state = YLeaf(YType.uint32, "basecaps-state")

                        self.cdp_protocol_state = YLeaf(YType.uint32, "cdp-protocol-state")

                        self.interface_encaps = YLeaf(YType.str, "interface-encaps")

                        self.interface_handle = YLeaf(YType.str, "interface-handle")

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
                                        "basecaps_state",
                                        "cdp_protocol_state",
                                        "interface_encaps",
                                        "interface_handle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Cdp.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Cdp.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.basecaps_state.is_set or
                            self.cdp_protocol_state.is_set or
                            self.interface_encaps.is_set or
                            self.interface_handle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.basecaps_state.yfilter != YFilter.not_set or
                            self.cdp_protocol_state.yfilter != YFilter.not_set or
                            self.interface_encaps.yfilter != YFilter.not_set or
                            self.interface_handle.yfilter != YFilter.not_set)

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
                        if (self.basecaps_state.is_set or self.basecaps_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.basecaps_state.get_name_leafdata())
                        if (self.cdp_protocol_state.is_set or self.cdp_protocol_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cdp_protocol_state.get_name_leafdata())
                        if (self.interface_encaps.is_set or self.interface_encaps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_encaps.get_name_leafdata())
                        if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_handle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "basecaps-state" or name == "cdp-protocol-state" or name == "interface-encaps" or name == "interface-handle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "basecaps-state"):
                            self.basecaps_state = value
                            self.basecaps_state.value_namespace = name_space
                            self.basecaps_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "cdp-protocol-state"):
                            self.cdp_protocol_state = value
                            self.cdp_protocol_state.value_namespace = name_space
                            self.cdp_protocol_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-encaps"):
                            self.interface_encaps = value
                            self.interface_encaps.value_namespace = name_space
                            self.interface_encaps.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-handle"):
                            self.interface_handle = value
                            self.interface_handle.value_namespace = name_space
                            self.interface_handle.value_namespace_prefix = name_space_prefix

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
                        c = Cdp.Nodes.Node.Interfaces.Interface()
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
                    path_buffer = "Cisco-IOS-XR-cdp-oper:cdp/nodes/%s" % self.get_segment_path()
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
                        self.interfaces = Cdp.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "neighbors"):
                    if (self.neighbors is None):
                        self.neighbors = Cdp.Nodes.Node.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                    return self.neighbors

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Cdp.Nodes.Node.Statistics()
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
                path_buffer = "Cisco-IOS-XR-cdp-oper:cdp/%s" % self.get_segment_path()
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
                c = Cdp.Nodes.Node()
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
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cdp-oper:cdp" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Cdp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Cdp()
        return self._top_entity

