""" Cisco_IOS_XR_cdp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package operational data.

This module contains definitions
for the following management objects\:
  cdp\: CDP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CdpDuplex(Enum):
    """
    CdpDuplex (Enum Class)

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
    CdpL3AddrProtocol (Enum Class)

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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes>`
    
    

    """

    _prefix = 'cdp-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(Cdp, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp"
        self.yang_parent_name = "Cisco-IOS-XR-cdp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Cdp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Cdp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-cdp-oper:cdp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cdp, [], name, value)


    class Nodes(Entity):
        """
        Per node CDP operational data
        
        .. attribute:: node
        
        	The CDP operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node>`
        
        

        """

        _prefix = 'cdp-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Cdp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cdp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Cdp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-cdp-oper:cdp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cdp.Nodes, [], name, value)


        class Node(Entity):
            """
            The CDP operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: neighbors
            
            	The CDP neighbor tables on this node
            	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors>`
            
            .. attribute:: statistics
            
            	The CDP traffic statistics for this node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Statistics>`
            
            .. attribute:: interfaces
            
            	The table of interfaces on which CDP is running on this node
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'cdp-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Cdp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("neighbors", ("neighbors", Cdp.Nodes.Node.Neighbors)), ("statistics", ("statistics", Cdp.Nodes.Node.Statistics)), ("interfaces", ("interfaces", Cdp.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.neighbors = Cdp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"

                self.statistics = Cdp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.interfaces = Cdp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-cdp-oper:cdp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cdp.Nodes.Node, ['node_name'], name, value)


            class Neighbors(Entity):
                """
                The CDP neighbor tables on this node
                
                .. attribute:: details
                
                	The detailed CDP neighbor table
                	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: devices
                
                	The detailed CDP neighbor table
                	**type**\:  :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: summaries
                
                	The CDP neighbor summary table
                	**type**\:  :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("details", ("details", Cdp.Nodes.Node.Neighbors.Details)), ("devices", ("devices", Cdp.Nodes.Node.Neighbors.Devices)), ("summaries", ("summaries", Cdp.Nodes.Node.Neighbors.Summaries))])
                    self._leafs = OrderedDict()

                    self.details = Cdp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"

                    self.devices = Cdp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self._children_name_map["devices"] = "devices"

                    self.summaries = Cdp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._segment_path = lambda: "neighbors"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cdp.Nodes.Node.Neighbors, [], name, value)


                class Details(Entity):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Details, self).__init__()

                        self.yang_name = "details"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("detail", ("detail", Cdp.Nodes.Node.Neighbors.Details.Detail))])
                        self._leafs = OrderedDict()

                        self.detail = YList(self)
                        self._segment_path = lambda: "details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details, [], name, value)


                    class Detail(Entity):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of  		 :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor>`
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Details.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("cdp-neighbor", ("cdp_neighbor", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                            ])
                            self.interface_name = None
                            self.device_id = None

                            self.cdp_neighbor = YList(self)
                            self._segment_path = lambda: "detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail, ['interface_name', 'device_id'], name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\: str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('capabilities', (YLeaf(YType.str, 'capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.device_id = None
                                self.port_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.capabilities = None
                                self.platform = None

                                self.detail = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._segment_path = lambda: "cdp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor, ['receiving_interface_name', 'device_id', 'port_id', 'header_version', 'hold_time', 'capabilities', 'platform'], name, value)


                            class Detail_(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:  :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList>`
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\: str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\: str
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:  :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses)), ("protocol-hello-list", ("protocol_hello_list", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList))])
                                    self._leafs = OrderedDict([
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('vtp_domain', (YLeaf(YType.str, 'vtp-domain'), ['str'])),
                                        ('native_vlan', (YLeaf(YType.uint32, 'native-vlan'), ['int'])),
                                        ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplex', '')])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                    ])
                                    self.version = None
                                    self.vtp_domain = None
                                    self.native_vlan = None
                                    self.duplex = None
                                    self.system_name = None

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_, ['version', 'vtp_domain', 'native_vlan', 'duplex', 'system_name'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of  		 :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-addr-entry", ("cdp_addr_entry", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses, [], name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address))])
                                            self._leafs = OrderedDict()

                                            self.address = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "cdp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry, [], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of  		 :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-prot-hello-entry", ("cdp_prot_hello_entry", Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_prot_hello_entry = YList(self)
                                        self._segment_path = lambda: "protocol-hello-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList, [], name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hello_message', (YLeaf(YType.str, 'hello-message'), ['str'])),
                                            ])
                                            self.hello_message = None
                                            self._segment_path = lambda: "cdp-prot-hello-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry, ['hello_message'], name, value)


                class Devices(Entity):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: device
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of  		 :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Devices, self).__init__()

                        self.yang_name = "devices"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("device", ("device", Cdp.Nodes.Node.Neighbors.Devices.Device))])
                        self._leafs = OrderedDict()

                        self.device = YList(self)
                        self._segment_path = lambda: "devices"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices, [], name, value)


                    class Device(Entity):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: device_id  (key)
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of  		 :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor>`
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Devices.Device, self).__init__()

                            self.yang_name = "device"
                            self.yang_parent_name = "devices"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['device_id']
                            self._child_classes = OrderedDict([("cdp-neighbor", ("cdp_neighbor", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor))])
                            self._leafs = OrderedDict([
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                            ])
                            self.device_id = None

                            self.cdp_neighbor = YList(self)
                            self._segment_path = lambda: "device" + "[device-id='" + str(self.device_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device, ['device_id'], name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\: str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "device"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('capabilities', (YLeaf(YType.str, 'capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.device_id = None
                                self.port_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.capabilities = None
                                self.platform = None

                                self.detail = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._segment_path = lambda: "cdp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor, ['receiving_interface_name', 'device_id', 'port_id', 'header_version', 'hold_time', 'capabilities', 'platform'], name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:  :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\: str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\: str
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:  :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses)), ("protocol-hello-list", ("protocol_hello_list", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList))])
                                    self._leafs = OrderedDict([
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('vtp_domain', (YLeaf(YType.str, 'vtp-domain'), ['str'])),
                                        ('native_vlan', (YLeaf(YType.uint32, 'native-vlan'), ['int'])),
                                        ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplex', '')])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                    ])
                                    self.version = None
                                    self.vtp_domain = None
                                    self.native_vlan = None
                                    self.duplex = None
                                    self.system_name = None

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail, ['version', 'vtp_domain', 'native_vlan', 'duplex', 'system_name'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of  		 :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-addr-entry", ("cdp_addr_entry", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses, [], name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address))])
                                            self._leafs = OrderedDict()

                                            self.address = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "cdp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, [], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of  		 :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-prot-hello-entry", ("cdp_prot_hello_entry", Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_prot_hello_entry = YList(self)
                                        self._segment_path = lambda: "protocol-hello-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList, [], name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hello_message', (YLeaf(YType.str, 'hello-message'), ['str'])),
                                            ])
                                            self.hello_message = None
                                            self._segment_path = lambda: "cdp-prot-hello-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, ['hello_message'], name, value)


                class Summaries(Entity):
                    """
                    The CDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a CDP neighbor entry
                    	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Neighbors.Summaries, self).__init__()

                        self.yang_name = "summaries"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("summary", ("summary", Cdp.Nodes.Node.Neighbors.Summaries.Summary))])
                        self._leafs = OrderedDict()

                        self.summary = YList(self)
                        self._segment_path = lambda: "summaries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries, [], name, value)


                    class Summary(Entity):
                        """
                        Brief information about a CDP neighbor entry
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of  		 :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor>`
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("cdp-neighbor", ("cdp_neighbor", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                            ])
                            self.interface_name = None
                            self.device_id = None

                            self.cdp_neighbor = YList(self)
                            self._segment_path = lambda: "summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary, ['interface_name', 'device_id'], name, value)


                        class CdpNeighbor(Entity):
                            """
                            cdp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\: str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor, self).__init__()

                                self.yang_name = "cdp-neighbor"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('capabilities', (YLeaf(YType.str, 'capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.device_id = None
                                self.port_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.capabilities = None
                                self.platform = None

                                self.detail = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._segment_path = lambda: "cdp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor, ['receiving_interface_name', 'device_id', 'port_id', 'header_version', 'hold_time', 'capabilities', 'platform'], name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:  :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\: str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\: str
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:  :py:class:`CdpDuplex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplex>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "cdp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses)), ("protocol-hello-list", ("protocol_hello_list", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList))])
                                    self._leafs = OrderedDict([
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('vtp_domain', (YLeaf(YType.str, 'vtp-domain'), ['str'])),
                                        ('native_vlan', (YLeaf(YType.uint32, 'native-vlan'), ['int'])),
                                        ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplex', '')])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                    ])
                                    self.version = None
                                    self.vtp_domain = None
                                    self.native_vlan = None
                                    self.duplex = None
                                    self.system_name = None

                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"

                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self._children_name_map["protocol_hello_list"] = "protocol-hello-list"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail, ['version', 'vtp_domain', 'native_vlan', 'duplex', 'system_name'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of  		 :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-addr-entry", ("cdp_addr_entry", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses, [], name, value)


                                    class CdpAddrEntry(Entity):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, self).__init__()

                                            self.yang_name = "cdp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address))])
                                            self._leafs = OrderedDict()

                                            self.address = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "cdp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry, [], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`CdpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "cdp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                                class ProtocolHelloList(Entity):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of  		 :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList, self).__init__()

                                        self.yang_name = "protocol-hello-list"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cdp-prot-hello-entry", ("cdp_prot_hello_entry", Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry))])
                                        self._leafs = OrderedDict()

                                        self.cdp_prot_hello_entry = YList(self)
                                        self._segment_path = lambda: "protocol-hello-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList, [], name, value)


                                    class CdpProtHelloEntry(Entity):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            super(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, self).__init__()

                                            self.yang_name = "cdp-prot-hello-entry"
                                            self.yang_parent_name = "protocol-hello-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hello_message', (YLeaf(YType.str, 'hello-message'), ['str'])),
                                            ])
                                            self.hello_message = None
                                            self._segment_path = lambda: "cdp-prot-hello-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry, ['hello_message'], name, value)


            class Statistics(Entity):
                """
                The CDP traffic statistics for this node
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v1
                
                	Received v1 packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v2
                
                	Received v2 packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v1
                
                	Transmitted v1 packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v2
                
                	Transmitted v2 packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_errors
                
                	Header syntax errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: checksum_errors
                
                	Checksum errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_packet_errors
                
                	Bad packet received and dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: truncated_packet_errors
                
                	Truncated messages
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_version_errors
                
                	Can't handle receive version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: open_file_errors
                
                	Cannot open file
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                        ('received_packets_v1', (YLeaf(YType.uint32, 'received-packets-v1'), ['int'])),
                        ('received_packets_v2', (YLeaf(YType.uint32, 'received-packets-v2'), ['int'])),
                        ('transmitted_packets', (YLeaf(YType.uint32, 'transmitted-packets'), ['int'])),
                        ('transmitted_packets_v1', (YLeaf(YType.uint32, 'transmitted-packets-v1'), ['int'])),
                        ('transmitted_packets_v2', (YLeaf(YType.uint32, 'transmitted-packets-v2'), ['int'])),
                        ('header_errors', (YLeaf(YType.uint32, 'header-errors'), ['int'])),
                        ('checksum_errors', (YLeaf(YType.uint32, 'checksum-errors'), ['int'])),
                        ('encapsulation_errors', (YLeaf(YType.uint32, 'encapsulation-errors'), ['int'])),
                        ('bad_packet_errors', (YLeaf(YType.uint32, 'bad-packet-errors'), ['int'])),
                        ('out_of_memory_errors', (YLeaf(YType.uint32, 'out-of-memory-errors'), ['int'])),
                        ('truncated_packet_errors', (YLeaf(YType.uint32, 'truncated-packet-errors'), ['int'])),
                        ('header_version_errors', (YLeaf(YType.uint32, 'header-version-errors'), ['int'])),
                        ('open_file_errors', (YLeaf(YType.uint32, 'open-file-errors'), ['int'])),
                    ])
                    self.received_packets = None
                    self.received_packets_v1 = None
                    self.received_packets_v2 = None
                    self.transmitted_packets = None
                    self.transmitted_packets_v1 = None
                    self.transmitted_packets_v2 = None
                    self.header_errors = None
                    self.checksum_errors = None
                    self.encapsulation_errors = None
                    self.bad_packet_errors = None
                    self.out_of_memory_errors = None
                    self.truncated_packet_errors = None
                    self.header_version_errors = None
                    self.open_file_errors = None
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cdp.Nodes.Node.Statistics, ['received_packets', 'received_packets_v1', 'received_packets_v2', 'transmitted_packets', 'transmitted_packets_v1', 'transmitted_packets_v2', 'header_errors', 'checksum_errors', 'encapsulation_errors', 'bad_packet_errors', 'out_of_memory_errors', 'truncated_packet_errors', 'header_version_errors', 'open_file_errors'], name, value)


            class Interfaces(Entity):
                """
                The table of interfaces on which CDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which CDP is running
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Cdp.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Cdp.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cdp.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Operational data for an interface on which
                    CDP is running
                    
                    .. attribute:: interface_name  (key)
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: interface_handle
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: basecaps_state
                    
                    	Interface basecaps state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdp_protocol_state
                    
                    	CDP protocol state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_encaps
                    
                    	Interface encapsulation
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Cdp.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                            ('basecaps_state', (YLeaf(YType.uint32, 'basecaps-state'), ['int'])),
                            ('cdp_protocol_state', (YLeaf(YType.uint32, 'cdp-protocol-state'), ['int'])),
                            ('interface_encaps', (YLeaf(YType.str, 'interface-encaps'), ['str'])),
                        ])
                        self.interface_name = None
                        self.interface_handle = None
                        self.basecaps_state = None
                        self.cdp_protocol_state = None
                        self.interface_encaps = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cdp.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_handle', 'basecaps_state', 'cdp_protocol_state', 'interface_encaps'], name, value)

    def clone_ptr(self):
        self._top_entity = Cdp()
        return self._top_entity

