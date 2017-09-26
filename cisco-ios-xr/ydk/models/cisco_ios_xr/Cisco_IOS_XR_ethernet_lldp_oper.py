""" Cisco_IOS_XR_ethernet_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\: Link Layer Discovery Protocol operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global-lldp" : ("global_lldp", Lldp.GlobalLldp), "nodes" : ("nodes", Lldp.Nodes)}
        self._child_list_classes = {}

        self.global_lldp = Lldp.GlobalLldp()
        self.global_lldp.parent = self
        self._children_name_map["global_lldp"] = "global-lldp"
        self._children_yang_names.add("global-lldp")

        self.nodes = Lldp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"lldp-info" : ("lldp_info", Lldp.GlobalLldp.LldpInfo)}
            self._child_list_classes = {}

            self.lldp_info = Lldp.GlobalLldp.LldpInfo()
            self.lldp_info.parent = self
            self._children_name_map["lldp_info"] = "lldp-info"
            self._children_yang_names.add("lldp-info")
            self._segment_path = lambda: "global-lldp"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self._segment_path()


        class LldpInfo(Entity):
            """
            The LLDP Global Information of this box
            
            .. attribute:: chassis_id
            
            	Chassis identifier
            	**type**\:  str
            
            .. attribute:: chassis_id_sub_type
            
            	Chassis ID sub type
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: hold_time
            
            	Length  of time  (in sec)that receiver must keep thispacket
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: re_init
            
            	Delay (in sec) for LLDPinitialization on anyinterface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: system_name
            
            	System Name
            	**type**\:  str
            
            .. attribute:: timer
            
            	Rate at which LLDP packets re sent (in sec)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.GlobalLldp.LldpInfo, self).__init__()

                self.yang_name = "lldp-info"
                self.yang_parent_name = "global-lldp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.chassis_id = YLeaf(YType.str, "chassis-id")

                self.chassis_id_sub_type = YLeaf(YType.uint8, "chassis-id-sub-type")

                self.hold_time = YLeaf(YType.uint32, "hold-time")

                self.re_init = YLeaf(YType.uint32, "re-init")

                self.system_name = YLeaf(YType.str, "system-name")

                self.timer = YLeaf(YType.uint32, "timer")
                self._segment_path = lambda: "lldp-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/global-lldp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.GlobalLldp.LldpInfo, ['chassis_id', 'chassis_id_sub_type', 'hold_time', 're_init', 'system_name', 'timer'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Lldp.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.Nodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", Lldp.Nodes.Node.Interfaces), "neighbors" : ("neighbors", Lldp.Nodes.Node.Neighbors), "statistics" : ("statistics", Lldp.Nodes.Node.Statistics)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.Nodes.Node, ['node_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Lldp.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Operational data for an interface on which
                    LLDP is running
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: if_index
                    
                    	ifIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"local-network-addresses" : ("local_network_addresses", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface, ['interface_name', 'if_index', 'interface_name_xr', 'port_description', 'port_id', 'port_id_sub_type', 'rx_enabled', 'rx_state', 'tx_enabled', 'tx_state'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lldp-addr-entry" : ("lldp_addr_entry", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry)}

                            self.lldp_addr_entry = YList(self)
                            self._segment_path = lambda: "local-network-addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"address" : ("address", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address)}
                                self._child_list_classes = {}

                                self.if_num = YLeaf(YType.uint32, "if-num")

                                self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                self.address = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")
                                self._segment_path = lambda: "lldp-addr-entry"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, ['if_num', 'ma_subtype'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address_type = YLeaf(YType.enumeration, "address-type")

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"details" : ("details", Lldp.Nodes.Node.Neighbors.Details), "devices" : ("devices", Lldp.Nodes.Node.Neighbors.Devices), "summaries" : ("summaries", Lldp.Nodes.Node.Neighbors.Summaries)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "neighbors"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"detail" : ("detail", Lldp.Nodes.Node.Neighbors.Details.Detail)}

                        self.detail = YList(self)
                        self._segment_path = lambda: "details"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details, [], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lldp-neighbor" : ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor)}

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail, ['device_id', 'interface_name'], name, value)


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
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"detail" : ("detail", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail), "mib" : ("mib", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "lldp-neighbor"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, ['chassis_id', 'device_id', 'enabled_capabilities', 'header_version', 'hold_time', 'platform', 'port_id_detail', 'receiving_interface_name', 'receiving_parent_interface_name'], name, value)


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
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"network-addresses" : ("network_addresses", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses)}
                                    self._child_list_classes = {}

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.peer_mac_address = YLeaf(YType.str, "peer-mac-address")

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
                                    self._segment_path = lambda: "detail"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail, ['auto_negotiation', 'enabled_capabilities', 'media_attachment_unit_type', 'peer_mac_address', 'physical_media_capabilities', 'port_description', 'port_vlan_id', 'system_capabilities', 'system_description', 'system_name', 'time_remaining'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-addr-entry" : ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry)}

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"address" : ("address", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address)}
                                            self._child_list_classes = {}

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")
                                            self._segment_path = lambda: "lldp-addr-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, ['if_num', 'ma_subtype'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.address_type = YLeaf(YType.enumeration, "address-type")

                                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                                self._segment_path = lambda: "address"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"org-def-tlv-list" : ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList), "unknown-tlv-list" : ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "mib"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, ['chassis_id_len', 'chassis_id_sub_type', 'combined_capabilities', 'port_id_len', 'port_id_sub_type', 'rem_index', 'rem_local_port_num', 'rem_time_mark'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-org-def-tlv-entry" : ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry)}

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_info_indes', 'tlv_subtype', 'tlv_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-unknown-tlv-entry" : ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry)}

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"device" : ("device", Lldp.Nodes.Node.Neighbors.Devices.Device)}

                        self.device = YList(self)
                        self._segment_path = lambda: "devices"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices, [], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lldp-neighbor" : ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor)}

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "device"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device, ['device_id', 'interface_name'], name, value)


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
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "device"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"detail" : ("detail", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail), "mib" : ("mib", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "lldp-neighbor"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, ['chassis_id', 'device_id', 'enabled_capabilities', 'header_version', 'hold_time', 'platform', 'port_id_detail', 'receiving_interface_name', 'receiving_parent_interface_name'], name, value)


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
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"network-addresses" : ("network_addresses", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses)}
                                    self._child_list_classes = {}

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.peer_mac_address = YLeaf(YType.str, "peer-mac-address")

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
                                    self._segment_path = lambda: "detail"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, ['auto_negotiation', 'enabled_capabilities', 'media_attachment_unit_type', 'peer_mac_address', 'physical_media_capabilities', 'port_description', 'port_vlan_id', 'system_capabilities', 'system_description', 'system_name', 'time_remaining'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-addr-entry" : ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry)}

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"address" : ("address", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address)}
                                            self._child_list_classes = {}

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")
                                            self._segment_path = lambda: "lldp-addr-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, ['if_num', 'ma_subtype'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.address_type = YLeaf(YType.enumeration, "address-type")

                                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                                self._segment_path = lambda: "address"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"org-def-tlv-list" : ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList), "unknown-tlv-list" : ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "mib"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, ['chassis_id_len', 'chassis_id_sub_type', 'combined_capabilities', 'port_id_len', 'port_id_sub_type', 'rem_index', 'rem_local_port_num', 'rem_time_mark'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-org-def-tlv-entry" : ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry)}

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_info_indes', 'tlv_subtype', 'tlv_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-unknown-tlv-entry" : ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry)}

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"summary" : ("summary", Lldp.Nodes.Node.Neighbors.Summaries.Summary)}

                        self.summary = YList(self)
                        self._segment_path = lambda: "summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries, [], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lldp-neighbor" : ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor)}

                            self.device_id = YLeaf(YType.str, "device-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary, ['device_id', 'interface_name'], name, value)


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
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"detail" : ("detail", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail), "mib" : ("mib", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "lldp-neighbor"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, ['chassis_id', 'device_id', 'enabled_capabilities', 'header_version', 'hold_time', 'platform', 'port_id_detail', 'receiving_interface_name', 'receiving_parent_interface_name'], name, value)


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
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"network-addresses" : ("network_addresses", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses)}
                                    self._child_list_classes = {}

                                    self.auto_negotiation = YLeaf(YType.str, "auto-negotiation")

                                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                                    self.media_attachment_unit_type = YLeaf(YType.uint32, "media-attachment-unit-type")

                                    self.peer_mac_address = YLeaf(YType.str, "peer-mac-address")

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
                                    self._segment_path = lambda: "detail"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, ['auto_negotiation', 'enabled_capabilities', 'media_attachment_unit_type', 'peer_mac_address', 'physical_media_capabilities', 'port_description', 'port_vlan_id', 'system_capabilities', 'system_description', 'system_name', 'time_remaining'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-addr-entry" : ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry)}

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"address" : ("address", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address)}
                                            self._child_list_classes = {}

                                            self.if_num = YLeaf(YType.uint32, "if-num")

                                            self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                                            self.address = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._children_yang_names.add("address")
                                            self._segment_path = lambda: "lldp-addr-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, ['if_num', 'ma_subtype'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.address_type = YLeaf(YType.enumeration, "address-type")

                                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                                self._segment_path = lambda: "address"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"org-def-tlv-list" : ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList), "unknown-tlv-list" : ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "mib"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, ['chassis_id_len', 'chassis_id_sub_type', 'combined_capabilities', 'port_id_len', 'port_id_sub_type', 'rem_index', 'rem_local_port_num', 'rem_time_mark'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-org-def-tlv-entry" : ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry)}

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.oui = YLeaf(YType.uint32, "oui")

                                            self.tlv_info_indes = YLeaf(YType.uint32, "tlv-info-indes")

                                            self.tlv_subtype = YLeaf(YType.uint8, "tlv-subtype")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_info_indes', 'tlv_subtype', 'tlv_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"lldp-unknown-tlv-entry" : ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry)}

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.tlv_type = YLeaf(YType.uint8, "tlv-type")

                                            self.tlv_value = YLeaf(YType.str, "tlv-value")
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Nodes.Node.Statistics, ['aged_out_entries', 'bad_packets', 'discarded_packets', 'discarded_tl_vs', 'encapsulation_errors', 'out_of_memory_errors', 'queue_overflow_errors', 'received_packets', 'table_overflow_errors', 'transmitted_packets', 'unrecognized_tl_vs'], name, value)

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity

