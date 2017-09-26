""" Cisco_IOS_XR_ncs1k_mxp_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\-snoop\-data\: Information related to LLDP Snoop

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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ethernet-controller-names" : ("ethernet_controller_names", LldpSnoopData.EthernetControllerNames), "lldp-neighbor-brief" : ("lldp_neighbor_brief", LldpSnoopData.LldpNeighborBrief)}
        self._child_list_classes = {}

        self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
        self.ethernet_controller_names.parent = self
        self._children_name_map["ethernet_controller_names"] = "ethernet-controller-names"
        self._children_yang_names.add("ethernet-controller-names")

        self.lldp_neighbor_brief = LldpSnoopData.LldpNeighborBrief()
        self.lldp_neighbor_brief.parent = self
        self._children_name_map["lldp_neighbor_brief"] = "lldp-neighbor-brief"
        self._children_yang_names.add("lldp-neighbor-brief")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ethernet-controller-name" : ("ethernet_controller_name", LldpSnoopData.EthernetControllerNames.EthernetControllerName)}

            self.ethernet_controller_name = YList(self)
            self._segment_path = lambda: "ethernet-controller-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LldpSnoopData.EthernetControllerNames, [], name, value)


        class EthernetControllerName(Entity):
            """
            port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"network-addresses" : ("network_addresses", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "ethernet-controller-name" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/ethernet-controller-names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName, ['name', 'chassis_id', 'drop_enabled', 'enabled_capabilities', 'hold_time', 'lldp_neighbor', 'port_description', 'port_id_detail', 'rx_lldp_pkts', 'source_mac', 'system_capabilities', 'system_description', 'system_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lldp-addr-entry" : ("lldp_addr_entry", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry)}

                    self.lldp_addr_entry = YList(self)
                    self._segment_path = lambda: "network-addresses"

                def __setattr__(self, name, value):
                    self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"address" : ("address", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address)}
                        self._child_list_classes = {}

                        self.if_num = YLeaf(YType.uint32, "if-num")

                        self.ma_subtype = YLeaf(YType.uint8, "ma-subtype")

                        self.address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._children_yang_names.add("address")
                        self._segment_path = lambda: "lldp-addr-entry"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, ['if_num', 'ma_subtype'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address_type = YLeaf(YType.enumeration, "address-type")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"neighbours" : ("neighbours", LldpSnoopData.LldpNeighborBrief.Neighbours)}
            self._child_list_classes = {}

            self.number_of_entries = YLeaf(YType.uint16, "number-of-entries")

            self.neighbours = LldpSnoopData.LldpNeighborBrief.Neighbours()
            self.neighbours.parent = self
            self._children_name_map["neighbours"] = "neighbours"
            self._children_yang_names.add("neighbours")
            self._segment_path = lambda: "lldp-neighbor-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LldpSnoopData.LldpNeighborBrief, ['number_of_entries'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"lldp-neighbor-brief-entry" : ("lldp_neighbor_brief_entry", LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry)}

                self.lldp_neighbor_brief_entry = YList(self)
                self._segment_path = lambda: "neighbours"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/lldp-neighbor-brief/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LldpSnoopData.LldpNeighborBrief.Neighbours, [], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.chassis_id = YLeaf(YType.str, "chassis-id")

                    self.enabled_capabilities = YLeaf(YType.str, "enabled-capabilities")

                    self.hold_time = YLeaf(YType.uint16, "hold-time")

                    self.port_id_detail = YLeaf(YType.str, "port-id-detail")

                    self.recv_intf = YLeaf(YType.str, "recv-intf")

                    self.system_name = YLeaf(YType.str, "system-name")
                    self._segment_path = lambda: "lldp-neighbor-brief-entry"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/lldp-neighbor-brief/neighbours/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry, ['chassis_id', 'enabled_capabilities', 'hold_time', 'port_id_detail', 'recv_intf', 'system_name'], name, value)

    def clone_ptr(self):
        self._top_entity = LldpSnoopData()
        return self._top_entity

