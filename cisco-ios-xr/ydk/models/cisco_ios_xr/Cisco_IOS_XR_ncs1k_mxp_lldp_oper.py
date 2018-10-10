""" Cisco_IOS_XR_ncs1k_mxp_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\-snoop\-data\: Information related to LLDP Snoop

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LldpL3AddrProtocol(Enum):
    """
    LldpL3AddrProtocol (Enum Class)

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
    	**type**\:  :py:class:`EthernetControllerNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ethernet-controller-names", ("ethernet_controller_names", LldpSnoopData.EthernetControllerNames))])
        self._leafs = OrderedDict()

        self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
        self.ethernet_controller_names.parent = self
        self._children_name_map["ethernet_controller_names"] = "ethernet-controller-names"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LldpSnoopData, [], name, value)


    class EthernetControllerNames(Entity):
        """
        Ethernet controller snoop data
        
        .. attribute:: ethernet_controller_name
        
        	port Name
        	**type**\: list of  		 :py:class:`EthernetControllerName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName>`
        
        

        """

        _prefix = 'ncs1k-mxp-lldp-oper'
        _revision = '2016-10-13'

        def __init__(self):
            super(LldpSnoopData.EthernetControllerNames, self).__init__()

            self.yang_name = "ethernet-controller-names"
            self.yang_parent_name = "lldp-snoop-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ethernet-controller-name", ("ethernet_controller_name", LldpSnoopData.EthernetControllerNames.EthernetControllerName))])
            self._leafs = OrderedDict()

            self.ethernet_controller_name = YList(self)
            self._segment_path = lambda: "ethernet-controller-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LldpSnoopData.EthernetControllerNames, [], name, value)


        class EthernetControllerName(Entity):
            """
            port Name
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: network_addresses
            
            	Management Addresses
            	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses>`
            
            .. attribute:: source_mac
            
            	Mac address of the neighbor
            	**type**\: str
            
            .. attribute:: chassis_id
            
            	Chassis id
            	**type**\: str
            
            .. attribute:: port_id_detail
            
            	Outgoing port identifier
            	**type**\: str
            
            .. attribute:: hold_time
            
            	Remaining hold time
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: port_description
            
            	Port Description
            	**type**\: str
            
            .. attribute:: system_name
            
            	System Name
            	**type**\: str
            
            .. attribute:: system_description
            
            	System Description
            	**type**\: str
            
            .. attribute:: system_capabilities
            
            	System Capabilities
            	**type**\: str
            
            .. attribute:: enabled_capabilities
            
            	Enabled Capabilities
            	**type**\: str
            
            .. attribute:: lldp_neighbor
            
            	LldpNeighbor
            	**type**\: str
            
            	**length:** 0..40
            
            .. attribute:: drop_enabled
            
            	LLDP Packet Drop Enabled
            	**type**\: bool
            
            .. attribute:: rx_lldp_pkts
            
            	Received LLDP Packets count
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'ncs1k-mxp-lldp-oper'
            _revision = '2016-10-13'

            def __init__(self):
                super(LldpSnoopData.EthernetControllerNames.EthernetControllerName, self).__init__()

                self.yang_name = "ethernet-controller-name"
                self.yang_parent_name = "ethernet-controller-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("network-addresses", ("network_addresses", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('source_mac', (YLeaf(YType.str, 'source-mac'), ['str'])),
                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                    ('port_id_detail', (YLeaf(YType.str, 'port-id-detail'), ['str'])),
                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                    ('port_description', (YLeaf(YType.str, 'port-description'), ['str'])),
                    ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                    ('system_description', (YLeaf(YType.str, 'system-description'), ['str'])),
                    ('system_capabilities', (YLeaf(YType.str, 'system-capabilities'), ['str'])),
                    ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                    ('lldp_neighbor', (YLeaf(YType.str, 'lldp-neighbor'), ['str'])),
                    ('drop_enabled', (YLeaf(YType.boolean, 'drop-enabled'), ['bool'])),
                    ('rx_lldp_pkts', (YLeaf(YType.uint64, 'rx-lldp-pkts'), ['int'])),
                ])
                self.name = None
                self.source_mac = None
                self.chassis_id = None
                self.port_id_detail = None
                self.hold_time = None
                self.port_description = None
                self.system_name = None
                self.system_description = None
                self.system_capabilities = None
                self.enabled_capabilities = None
                self.lldp_neighbor = None
                self.drop_enabled = None
                self.rx_lldp_pkts = None

                self.network_addresses = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses()
                self.network_addresses.parent = self
                self._children_name_map["network_addresses"] = "network-addresses"
                self._segment_path = lambda: "ethernet-controller-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/ethernet-controller-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName, ['name', 'source_mac', 'chassis_id', 'port_id_detail', 'hold_time', 'port_description', 'system_name', 'system_description', 'system_capabilities', 'enabled_capabilities', 'lldp_neighbor', 'drop_enabled', 'rx_lldp_pkts'], name, value)


            class NetworkAddresses(Entity):
                """
                Management Addresses
                
                .. attribute:: lldp_addr_entry
                
                	lldp addr entry
                	**type**\: list of  		 :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry>`
                
                

                """

                _prefix = 'ncs1k-mxp-lldp-oper'
                _revision = '2016-10-13'

                def __init__(self):
                    super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, self).__init__()

                    self.yang_name = "network-addresses"
                    self.yang_parent_name = "ethernet-controller-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lldp-addr-entry", ("lldp_addr_entry", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry))])
                    self._leafs = OrderedDict()

                    self.lldp_addr_entry = YList(self)
                    self._segment_path = lambda: "network-addresses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses, [], name, value)


                class LldpAddrEntry(Entity):
                    """
                    lldp addr entry
                    
                    .. attribute:: address
                    
                    	Network layer address
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address>`
                    
                    .. attribute:: ma_subtype
                    
                    	MA sub type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: if_num
                    
                    	Interface num
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-lldp-oper'
                    _revision = '2016-10-13'

                    def __init__(self):
                        super(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, self).__init__()

                        self.yang_name = "lldp-addr-entry"
                        self.yang_parent_name = "network-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address))])
                        self._leafs = OrderedDict([
                            ('ma_subtype', (YLeaf(YType.uint8, 'ma-subtype'), ['int'])),
                            ('if_num', (YLeaf(YType.uint32, 'if-num'), ['int'])),
                        ])
                        self.ma_subtype = None
                        self.if_num = None

                        self.address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "lldp-addr-entry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry, ['ma_subtype', 'if_num'], name, value)


                    class Address(Entity):
                        """
                        Network layer address
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpL3AddrProtocol>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpL3AddrProtocol', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = LldpSnoopData()
        return self._top_entity

