""" Cisco_IOS_XR_ethernet_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\: Link Layer Discovery Protocol operational data

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



class Lldp(Entity):
    """
    Link Layer Discovery Protocol operational data
    
    .. attribute:: global_lldp
    
    	Global LLDP data
    	**type**\:  :py:class:`GlobalLldp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp>`
    
    .. attribute:: nodes
    
    	Per node LLDP operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes>`
    
    

    """

    _prefix = 'ethernet-lldp-oper'
    _revision = '2017-11-13'

    def __init__(self):
        super(Lldp, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-lldp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global-lldp", ("global_lldp", Lldp.GlobalLldp)), ("nodes", ("nodes", Lldp.Nodes))])
        self._leafs = OrderedDict()

        self.global_lldp = Lldp.GlobalLldp()
        self.global_lldp.parent = self
        self._children_name_map["global_lldp"] = "global-lldp"

        self.nodes = Lldp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lldp, [], name, value)


    class GlobalLldp(Entity):
        """
        Global LLDP data
        
        .. attribute:: lldp_info
        
        	The LLDP Global Information of this box
        	**type**\:  :py:class:`LldpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp.LldpInfo>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2017-11-13'

        def __init__(self):
            super(Lldp.GlobalLldp, self).__init__()

            self.yang_name = "global-lldp"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldp-info", ("lldp_info", Lldp.GlobalLldp.LldpInfo))])
            self._leafs = OrderedDict()

            self.lldp_info = Lldp.GlobalLldp.LldpInfo()
            self.lldp_info.parent = self
            self._children_name_map["lldp_info"] = "lldp-info"
            self._segment_path = lambda: "global-lldp"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.GlobalLldp, [], name, value)


        class LldpInfo(Entity):
            """
            The LLDP Global Information of this box
            
            .. attribute:: chassis_id
            
            	Chassis identifier
            	**type**\: str
            
            .. attribute:: chassis_id_sub_type
            
            	Chassis ID sub type
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: system_name
            
            	System Name
            	**type**\: str
            
            .. attribute:: timer
            
            	Rate at which LLDP packets re sent (in sec)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hold_time
            
            	Length  of time  (in sec)that receiver must keep thispacket
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: re_init
            
            	Delay (in sec) for LLDPinitialization on anyinterface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Lldp.GlobalLldp.LldpInfo, self).__init__()

                self.yang_name = "lldp-info"
                self.yang_parent_name = "global-lldp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                    ('chassis_id_sub_type', (YLeaf(YType.uint8, 'chassis-id-sub-type'), ['int'])),
                    ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                    ('timer', (YLeaf(YType.uint32, 'timer'), ['int'])),
                    ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                    ('re_init', (YLeaf(YType.uint32, 're-init'), ['int'])),
                ])
                self.chassis_id = None
                self.chassis_id_sub_type = None
                self.system_name = None
                self.timer = None
                self.hold_time = None
                self.re_init = None
                self._segment_path = lambda: "lldp-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/global-lldp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.GlobalLldp.LldpInfo, [u'chassis_id', u'chassis_id_sub_type', u'system_name', u'timer', u'hold_time', u're_init'], name, value)


    class Nodes(Entity):
        """
        Per node LLDP operational data
        
        .. attribute:: node
        
        	The LLDP operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2017-11-13'

        def __init__(self):
            super(Lldp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Lldp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.Nodes, [], name, value)


        class Node(Entity):
            """
            The LLDP operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: neighbors
            
            	The LLDP neighbor tables on this node
            	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors>`
            
            .. attribute:: interfaces
            
            	The table of interfaces on which LLDP is running on this node
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces>`
            
            .. attribute:: statistics
            
            	The LLDP traffic statistics for this node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Lldp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("neighbors", ("neighbors", Lldp.Nodes.Node.Neighbors)), ("interfaces", ("interfaces", Lldp.Nodes.Node.Interfaces)), ("statistics", ("statistics", Lldp.Nodes.Node.Statistics))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.neighbors = Lldp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"

                self.interfaces = Lldp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.statistics = Lldp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-lldp-oper:lldp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.Nodes.Node, ['node_name'], name, value)


            class Neighbors(Entity):
                """
                The LLDP neighbor tables on this node
                
                .. attribute:: devices
                
                	The detailed LLDP neighbor table on this device
                	**type**\:  :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: details
                
                	The detailed LLDP neighbor table
                	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: summaries
                
                	The LLDP neighbor summary table
                	**type**\:  :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Lldp.Nodes.Node.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("devices", ("devices", Lldp.Nodes.Node.Neighbors.Devices)), ("details", ("details", Lldp.Nodes.Node.Neighbors.Details)), ("summaries", ("summaries", Lldp.Nodes.Node.Neighbors.Summaries))])
                    self._leafs = OrderedDict()

                    self.devices = Lldp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self._children_name_map["devices"] = "devices"

                    self.details = Lldp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"

                    self.summaries = Lldp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._segment_path = lambda: "neighbors"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Nodes.Node.Neighbors, [], name, value)


                class Devices(Entity):
                    """
                    The detailed LLDP neighbor table on this
                    device
                    
                    .. attribute:: device
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of  		 :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Devices, self).__init__()

                        self.yang_name = "devices"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("device", ("device", Lldp.Nodes.Node.Neighbors.Devices.Device))])
                        self._leafs = OrderedDict()

                        self.device = YList(self)
                        self._segment_path = lambda: "devices"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices, [], name, value)


                    class Device(Entity):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of  		 :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Devices.Device, self).__init__()

                            self.yang_name = "device"
                            self.yang_parent_name = "devices"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lldp-neighbor", ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor))])
                            self._leafs = OrderedDict([
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.device_id = None
                            self.interface_name = None

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "device"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device, ['device_id', 'interface_name'], name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail>`
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:  :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\: str
                            
                            .. attribute:: port_id_detail
                            
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
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "device"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail)), ("mib", ("mib", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('receiving_parent_interface_name', (YLeaf(YType.str, 'receiving-parent-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                    ('port_id_detail', (YLeaf(YType.str, 'port-id-detail'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None
                                self.device_id = None
                                self.chassis_id = None
                                self.port_id_detail = None
                                self.header_version = None
                                self.hold_time = None
                                self.enabled_capabilities = None
                                self.platform = None

                                self.detail = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"

                                self.mib = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._segment_path = lambda: "lldp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor, ['receiving_interface_name', 'receiving_parent_interface_name', 'device_id', 'chassis_id', 'port_id_detail', 'header_version', 'hold_time', 'enabled_capabilities', 'platform'], name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\: str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\: str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\: str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\: str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\: str
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\: str
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\: str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses))])
                                    self._leafs = OrderedDict([
                                        ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                                        ('port_description', (YLeaf(YType.str, 'port-description'), ['str'])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                        ('system_description', (YLeaf(YType.str, 'system-description'), ['str'])),
                                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                                        ('system_capabilities', (YLeaf(YType.str, 'system-capabilities'), ['str'])),
                                        ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                        ('auto_negotiation', (YLeaf(YType.str, 'auto-negotiation'), ['str'])),
                                        ('physical_media_capabilities', (YLeaf(YType.str, 'physical-media-capabilities'), ['str'])),
                                        ('media_attachment_unit_type', (YLeaf(YType.uint32, 'media-attachment-unit-type'), ['int'])),
                                        ('port_vlan_id', (YLeaf(YType.uint32, 'port-vlan-id'), ['int'])),
                                    ])
                                    self.peer_mac_address = None
                                    self.port_description = None
                                    self.system_name = None
                                    self.system_description = None
                                    self.time_remaining = None
                                    self.system_capabilities = None
                                    self.enabled_capabilities = None
                                    self.auto_negotiation = None
                                    self.physical_media_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.port_vlan_id = None

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail, ['peer_mac_address', 'port_description', 'system_name', 'system_description', 'time_remaining', 'system_capabilities', 'enabled_capabilities', 'auto_negotiation', 'physical_media_capabilities', 'media_attachment_unit_type', 'port_vlan_id'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of  		 :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-addr-entry", ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses, [], name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address))])
                                            self._leafs = OrderedDict([
                                                ('ma_subtype', (YLeaf(YType.uint8, 'ma-subtype'), ['int'])),
                                                ('if_num', (YLeaf(YType.uint32, 'if-num'), ['int'])),
                                            ])
                                            self.ma_subtype = None
                                            self.if_num = None

                                            self.address = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "lldp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, ['ma_subtype', 'if_num'], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2017-11-13'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "lldp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:  :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:  :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("unknown-tlv-list", ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList)), ("org-def-tlv-list", ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList))])
                                    self._leafs = OrderedDict([
                                        ('rem_time_mark', (YLeaf(YType.uint32, 'rem-time-mark'), ['int'])),
                                        ('rem_local_port_num', (YLeaf(YType.uint32, 'rem-local-port-num'), ['int'])),
                                        ('rem_index', (YLeaf(YType.uint32, 'rem-index'), ['int'])),
                                        ('chassis_id_sub_type', (YLeaf(YType.uint8, 'chassis-id-sub-type'), ['int'])),
                                        ('chassis_id_len', (YLeaf(YType.uint16, 'chassis-id-len'), ['int'])),
                                        ('port_id_sub_type', (YLeaf(YType.uint8, 'port-id-sub-type'), ['int'])),
                                        ('port_id_len', (YLeaf(YType.uint16, 'port-id-len'), ['int'])),
                                        ('combined_capabilities', (YLeaf(YType.uint32, 'combined-capabilities'), ['int'])),
                                    ])
                                    self.rem_time_mark = None
                                    self.rem_local_port_num = None
                                    self.rem_index = None
                                    self.chassis_id_sub_type = None
                                    self.chassis_id_len = None
                                    self.port_id_sub_type = None
                                    self.port_id_len = None
                                    self.combined_capabilities = None

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._segment_path = lambda: "mib"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib, ['rem_time_mark', 'rem_local_port_num', 'rem_index', 'chassis_id_sub_type', 'chassis_id_len', 'port_id_sub_type', 'port_id_len', 'combined_capabilities'], name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of  		 :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-unknown-tlv-entry", ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('tlv_type', (YLeaf(YType.uint8, 'tlv-type'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.tlv_type = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of  		 :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-org-def-tlv-entry", ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('oui', (YLeaf(YType.uint32, 'oui'), ['int'])),
                                                ('tlv_subtype', (YLeaf(YType.uint8, 'tlv-subtype'), ['int'])),
                                                ('tlv_info_indes', (YLeaf(YType.uint32, 'tlv-info-indes'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.oui = None
                                            self.tlv_subtype = None
                                            self.tlv_info_indes = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_subtype', 'tlv_info_indes', 'tlv_value'], name, value)


                class Details(Entity):
                    """
                    The detailed LLDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Details, self).__init__()

                        self.yang_name = "details"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("detail", ("detail", Lldp.Nodes.Node.Neighbors.Details.Detail))])
                        self._leafs = OrderedDict()

                        self.detail = YList(self)
                        self._segment_path = lambda: "details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details, [], name, value)


                    class Detail(Entity):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of  		 :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Details.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lldp-neighbor", ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                            ])
                            self.interface_name = None
                            self.device_id = None

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail, ['interface_name', 'device_id'], name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_>`
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:  :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\: str
                            
                            .. attribute:: port_id_detail
                            
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
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_)), ("mib", ("mib", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('receiving_parent_interface_name', (YLeaf(YType.str, 'receiving-parent-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                    ('port_id_detail', (YLeaf(YType.str, 'port-id-detail'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None
                                self.device_id = None
                                self.chassis_id = None
                                self.port_id_detail = None
                                self.header_version = None
                                self.hold_time = None
                                self.enabled_capabilities = None
                                self.platform = None

                                self.detail = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"

                                self.mib = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._segment_path = lambda: "lldp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor, ['receiving_interface_name', 'receiving_parent_interface_name', 'device_id', 'chassis_id', 'port_id_detail', 'header_version', 'hold_time', 'enabled_capabilities', 'platform'], name, value)


                            class Detail_(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses>`
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\: str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\: str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\: str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\: str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\: str
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\: str
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\: str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses))])
                                    self._leafs = OrderedDict([
                                        ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                                        ('port_description', (YLeaf(YType.str, 'port-description'), ['str'])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                        ('system_description', (YLeaf(YType.str, 'system-description'), ['str'])),
                                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                                        ('system_capabilities', (YLeaf(YType.str, 'system-capabilities'), ['str'])),
                                        ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                        ('auto_negotiation', (YLeaf(YType.str, 'auto-negotiation'), ['str'])),
                                        ('physical_media_capabilities', (YLeaf(YType.str, 'physical-media-capabilities'), ['str'])),
                                        ('media_attachment_unit_type', (YLeaf(YType.uint32, 'media-attachment-unit-type'), ['int'])),
                                        ('port_vlan_id', (YLeaf(YType.uint32, 'port-vlan-id'), ['int'])),
                                    ])
                                    self.peer_mac_address = None
                                    self.port_description = None
                                    self.system_name = None
                                    self.system_description = None
                                    self.time_remaining = None
                                    self.system_capabilities = None
                                    self.enabled_capabilities = None
                                    self.auto_negotiation = None
                                    self.physical_media_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.port_vlan_id = None

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_, ['peer_mac_address', 'port_description', 'system_name', 'system_description', 'time_remaining', 'system_capabilities', 'enabled_capabilities', 'auto_negotiation', 'physical_media_capabilities', 'media_attachment_unit_type', 'port_vlan_id'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of  		 :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-addr-entry", ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses, [], name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address))])
                                            self._leafs = OrderedDict([
                                                ('ma_subtype', (YLeaf(YType.uint8, 'ma-subtype'), ['int'])),
                                                ('if_num', (YLeaf(YType.uint32, 'if-num'), ['int'])),
                                            ])
                                            self.ma_subtype = None
                                            self.if_num = None

                                            self.address = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "lldp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry, ['ma_subtype', 'if_num'], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2017-11-13'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "lldp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:  :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:  :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("unknown-tlv-list", ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList)), ("org-def-tlv-list", ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList))])
                                    self._leafs = OrderedDict([
                                        ('rem_time_mark', (YLeaf(YType.uint32, 'rem-time-mark'), ['int'])),
                                        ('rem_local_port_num', (YLeaf(YType.uint32, 'rem-local-port-num'), ['int'])),
                                        ('rem_index', (YLeaf(YType.uint32, 'rem-index'), ['int'])),
                                        ('chassis_id_sub_type', (YLeaf(YType.uint8, 'chassis-id-sub-type'), ['int'])),
                                        ('chassis_id_len', (YLeaf(YType.uint16, 'chassis-id-len'), ['int'])),
                                        ('port_id_sub_type', (YLeaf(YType.uint8, 'port-id-sub-type'), ['int'])),
                                        ('port_id_len', (YLeaf(YType.uint16, 'port-id-len'), ['int'])),
                                        ('combined_capabilities', (YLeaf(YType.uint32, 'combined-capabilities'), ['int'])),
                                    ])
                                    self.rem_time_mark = None
                                    self.rem_local_port_num = None
                                    self.rem_index = None
                                    self.chassis_id_sub_type = None
                                    self.chassis_id_len = None
                                    self.port_id_sub_type = None
                                    self.port_id_len = None
                                    self.combined_capabilities = None

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._segment_path = lambda: "mib"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib, ['rem_time_mark', 'rem_local_port_num', 'rem_index', 'chassis_id_sub_type', 'chassis_id_len', 'port_id_sub_type', 'port_id_len', 'combined_capabilities'], name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of  		 :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-unknown-tlv-entry", ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('tlv_type', (YLeaf(YType.uint8, 'tlv-type'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.tlv_type = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of  		 :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-org-def-tlv-entry", ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('oui', (YLeaf(YType.uint32, 'oui'), ['int'])),
                                                ('tlv_subtype', (YLeaf(YType.uint8, 'tlv-subtype'), ['int'])),
                                                ('tlv_info_indes', (YLeaf(YType.uint32, 'tlv-info-indes'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.oui = None
                                            self.tlv_subtype = None
                                            self.tlv_info_indes = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_subtype', 'tlv_info_indes', 'tlv_value'], name, value)


                class Summaries(Entity):
                    """
                    The LLDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a LLDP neighbor entry
                    	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Neighbors.Summaries, self).__init__()

                        self.yang_name = "summaries"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("summary", ("summary", Lldp.Nodes.Node.Neighbors.Summaries.Summary))])
                        self._leafs = OrderedDict()

                        self.summary = YList(self)
                        self._segment_path = lambda: "summaries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries, [], name, value)


                    class Summary(Entity):
                        """
                        Brief information about a LLDP neighbor
                        entry
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\: str
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of  		 :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lldp-neighbor", ("lldp_neighbor", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                            ])
                            self.interface_name = None
                            self.device_id = None

                            self.lldp_neighbor = YList(self)
                            self._segment_path = lambda: "summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary, ['interface_name', 'device_id'], name, value)


                        class LldpNeighbor(Entity):
                            """
                            lldp neighbor
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail>`
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:  :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib>`
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\: str
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\: str
                            
                            .. attribute:: port_id_detail
                            
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
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\: str
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, self).__init__()

                                self.yang_name = "lldp-neighbor"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail)), ("mib", ("mib", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib))])
                                self._leafs = OrderedDict([
                                    ('receiving_interface_name', (YLeaf(YType.str, 'receiving-interface-name'), ['str'])),
                                    ('receiving_parent_interface_name', (YLeaf(YType.str, 'receiving-parent-interface-name'), ['str'])),
                                    ('device_id', (YLeaf(YType.str, 'device-id'), ['str'])),
                                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                    ('port_id_detail', (YLeaf(YType.str, 'port-id-detail'), ['str'])),
                                    ('header_version', (YLeaf(YType.uint8, 'header-version'), ['int'])),
                                    ('hold_time', (YLeaf(YType.uint16, 'hold-time'), ['int'])),
                                    ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                    ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                                ])
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None
                                self.device_id = None
                                self.chassis_id = None
                                self.port_id_detail = None
                                self.header_version = None
                                self.hold_time = None
                                self.enabled_capabilities = None
                                self.platform = None

                                self.detail = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"

                                self.mib = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self._children_name_map["mib"] = "mib"
                                self._segment_path = lambda: "lldp-neighbor"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor, ['receiving_interface_name', 'receiving_parent_interface_name', 'device_id', 'chassis_id', 'port_id_detail', 'header_version', 'hold_time', 'enabled_capabilities', 'platform'], name, value)


                            class Detail(Entity):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:  :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: peer_mac_address
                                
                                	Peer Mac Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\: str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\: str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\: str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\: str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\: str
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\: str
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\: str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network-addresses", ("network_addresses", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses))])
                                    self._leafs = OrderedDict([
                                        ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                                        ('port_description', (YLeaf(YType.str, 'port-description'), ['str'])),
                                        ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                                        ('system_description', (YLeaf(YType.str, 'system-description'), ['str'])),
                                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                                        ('system_capabilities', (YLeaf(YType.str, 'system-capabilities'), ['str'])),
                                        ('enabled_capabilities', (YLeaf(YType.str, 'enabled-capabilities'), ['str'])),
                                        ('auto_negotiation', (YLeaf(YType.str, 'auto-negotiation'), ['str'])),
                                        ('physical_media_capabilities', (YLeaf(YType.str, 'physical-media-capabilities'), ['str'])),
                                        ('media_attachment_unit_type', (YLeaf(YType.uint32, 'media-attachment-unit-type'), ['int'])),
                                        ('port_vlan_id', (YLeaf(YType.uint32, 'port-vlan-id'), ['int'])),
                                    ])
                                    self.peer_mac_address = None
                                    self.port_description = None
                                    self.system_name = None
                                    self.system_description = None
                                    self.time_remaining = None
                                    self.system_capabilities = None
                                    self.enabled_capabilities = None
                                    self.auto_negotiation = None
                                    self.physical_media_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.port_vlan_id = None

                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self._children_name_map["network_addresses"] = "network-addresses"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail, ['peer_mac_address', 'port_description', 'system_name', 'system_description', 'time_remaining', 'system_capabilities', 'enabled_capabilities', 'auto_negotiation', 'physical_media_capabilities', 'media_attachment_unit_type', 'port_vlan_id'], name, value)


                                class NetworkAddresses(Entity):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of  		 :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, self).__init__()

                                        self.yang_name = "network-addresses"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-addr-entry", ("lldp_addr_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_addr_entry = YList(self)
                                        self._segment_path = lambda: "network-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses, [], name, value)


                                    class LldpAddrEntry(Entity):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, self).__init__()

                                            self.yang_name = "lldp-addr-entry"
                                            self.yang_parent_name = "network-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("address", ("address", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address))])
                                            self._leafs = OrderedDict([
                                                ('ma_subtype', (YLeaf(YType.uint8, 'ma-subtype'), ['int'])),
                                                ('if_num', (YLeaf(YType.uint32, 'if-num'), ['int'])),
                                            ])
                                            self.ma_subtype = None
                                            self.if_num = None

                                            self.address = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                            self._segment_path = lambda: "lldp-addr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry, ['ma_subtype', 'if_num'], name, value)


                                        class Address(Entity):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:  :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2017-11-13'

                                            def __init__(self):
                                                super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, self).__init__()

                                                self.yang_name = "address"
                                                self.yang_parent_name = "lldp-addr-entry"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocol', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "address"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


                            class Mib(Entity):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:  :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:  :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, self).__init__()

                                    self.yang_name = "mib"
                                    self.yang_parent_name = "lldp-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("unknown-tlv-list", ("unknown_tlv_list", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList)), ("org-def-tlv-list", ("org_def_tlv_list", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList))])
                                    self._leafs = OrderedDict([
                                        ('rem_time_mark', (YLeaf(YType.uint32, 'rem-time-mark'), ['int'])),
                                        ('rem_local_port_num', (YLeaf(YType.uint32, 'rem-local-port-num'), ['int'])),
                                        ('rem_index', (YLeaf(YType.uint32, 'rem-index'), ['int'])),
                                        ('chassis_id_sub_type', (YLeaf(YType.uint8, 'chassis-id-sub-type'), ['int'])),
                                        ('chassis_id_len', (YLeaf(YType.uint16, 'chassis-id-len'), ['int'])),
                                        ('port_id_sub_type', (YLeaf(YType.uint8, 'port-id-sub-type'), ['int'])),
                                        ('port_id_len', (YLeaf(YType.uint16, 'port-id-len'), ['int'])),
                                        ('combined_capabilities', (YLeaf(YType.uint32, 'combined-capabilities'), ['int'])),
                                    ])
                                    self.rem_time_mark = None
                                    self.rem_local_port_num = None
                                    self.rem_index = None
                                    self.chassis_id_sub_type = None
                                    self.chassis_id_len = None
                                    self.port_id_sub_type = None
                                    self.port_id_len = None
                                    self.combined_capabilities = None

                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self
                                    self._children_name_map["unknown_tlv_list"] = "unknown-tlv-list"

                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self._children_name_map["org_def_tlv_list"] = "org-def-tlv-list"
                                    self._segment_path = lambda: "mib"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib, ['rem_time_mark', 'rem_local_port_num', 'rem_index', 'chassis_id_sub_type', 'chassis_id_len', 'port_id_sub_type', 'port_id_len', 'combined_capabilities'], name, value)


                                class UnknownTlvList(Entity):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of  		 :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, self).__init__()

                                        self.yang_name = "unknown-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-unknown-tlv-entry", ("lldp_unknown_tlv_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_unknown_tlv_entry = YList(self)
                                        self._segment_path = lambda: "unknown-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList, [], name, value)


                                    class LldpUnknownTlvEntry(Entity):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, self).__init__()

                                            self.yang_name = "lldp-unknown-tlv-entry"
                                            self.yang_parent_name = "unknown-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('tlv_type', (YLeaf(YType.uint8, 'tlv-type'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.tlv_type = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-unknown-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry, ['tlv_type', 'tlv_value'], name, value)


                                class OrgDefTlvList(Entity):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of  		 :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2017-11-13'

                                    def __init__(self):
                                        super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, self).__init__()

                                        self.yang_name = "org-def-tlv-list"
                                        self.yang_parent_name = "mib"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lldp-org-def-tlv-entry", ("lldp_org_def_tlv_entry", Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry))])
                                        self._leafs = OrderedDict()

                                        self.lldp_org_def_tlv_entry = YList(self)
                                        self._segment_path = lambda: "org-def-tlv-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList, [], name, value)


                                    class LldpOrgDefTlvEntry(Entity):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2017-11-13'

                                        def __init__(self):
                                            super(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, self).__init__()

                                            self.yang_name = "lldp-org-def-tlv-entry"
                                            self.yang_parent_name = "org-def-tlv-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('oui', (YLeaf(YType.uint32, 'oui'), ['int'])),
                                                ('tlv_subtype', (YLeaf(YType.uint8, 'tlv-subtype'), ['int'])),
                                                ('tlv_info_indes', (YLeaf(YType.uint32, 'tlv-info-indes'), ['int'])),
                                                ('tlv_value', (YLeaf(YType.str, 'tlv-value'), ['str'])),
                                            ])
                                            self.oui = None
                                            self.tlv_subtype = None
                                            self.tlv_info_indes = None
                                            self.tlv_value = None
                                            self._segment_path = lambda: "lldp-org-def-tlv-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry, ['oui', 'tlv_subtype', 'tlv_info_indes', 'tlv_value'], name, value)


            class Interfaces(Entity):
                """
                The table of interfaces on which LLDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which LLDP is running
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Lldp.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Lldp.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Operational data for an interface on which
                    LLDP is running
                    
                    .. attribute:: interface_name  (key)
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: local_network_addresses
                    
                    	Local Management Addresses
                    	**type**\:  :py:class:`LocalNetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses>`
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: tx_enabled
                    
                    	TX Enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_enabled
                    
                    	RX Enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tx_state
                    
                    	TX State
                    	**type**\: str
                    
                    .. attribute:: rx_state
                    
                    	RX State
                    	**type**\: str
                    
                    .. attribute:: if_index
                    
                    	ifIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port_id
                    
                    	Outgoing port identifier
                    	**type**\: str
                    
                    .. attribute:: port_id_sub_type
                    
                    	Port ID sub type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: port_description
                    
                    	Port Description
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Lldp.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("local-network-addresses", ("local_network_addresses", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('tx_enabled', (YLeaf(YType.uint8, 'tx-enabled'), ['int'])),
                            ('rx_enabled', (YLeaf(YType.uint8, 'rx-enabled'), ['int'])),
                            ('tx_state', (YLeaf(YType.str, 'tx-state'), ['str'])),
                            ('rx_state', (YLeaf(YType.str, 'rx-state'), ['str'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                            ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                            ('port_id_sub_type', (YLeaf(YType.uint8, 'port-id-sub-type'), ['int'])),
                            ('port_description', (YLeaf(YType.str, 'port-description'), ['str'])),
                        ])
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.tx_enabled = None
                        self.rx_enabled = None
                        self.tx_state = None
                        self.rx_state = None
                        self.if_index = None
                        self.port_id = None
                        self.port_id_sub_type = None
                        self.port_description = None

                        self.local_network_addresses = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses()
                        self.local_network_addresses.parent = self
                        self._children_name_map["local_network_addresses"] = "local-network-addresses"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'tx_enabled', 'rx_enabled', 'tx_state', 'rx_state', 'if_index', 'port_id', 'port_id_sub_type', 'port_description'], name, value)


                    class LocalNetworkAddresses(Entity):
                        """
                        Local Management Addresses
                        
                        .. attribute:: lldp_addr_entry
                        
                        	lldp addr entry
                        	**type**\: list of  		 :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, self).__init__()

                            self.yang_name = "local-network-addresses"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lldp-addr-entry", ("lldp_addr_entry", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry))])
                            self._leafs = OrderedDict()

                            self.lldp_addr_entry = YList(self)
                            self._segment_path = lambda: "local-network-addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses, [], name, value)


                        class LldpAddrEntry(Entity):
                            """
                            lldp addr entry
                            
                            .. attribute:: address
                            
                            	Network layer address
                            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address>`
                            
                            .. attribute:: ma_subtype
                            
                            	MA sub type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: if_num
                            
                            	Interface num
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, self).__init__()

                                self.yang_name = "lldp-addr-entry"
                                self.yang_parent_name = "local-network-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("address", ("address", Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address))])
                                self._leafs = OrderedDict([
                                    ('ma_subtype', (YLeaf(YType.uint8, 'ma-subtype'), ['int'])),
                                    ('if_num', (YLeaf(YType.uint32, 'if-num'), ['int'])),
                                ])
                                self.ma_subtype = None
                                self.if_num = None

                                self.address = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._segment_path = lambda: "lldp-addr-entry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry, ['ma_subtype', 'if_num'], name, value)


                            class Address(Entity):
                                """
                                Network layer address
                                
                                .. attribute:: address_type
                                
                                	AddressType
                                	**type**\:  :py:class:`LldpL3AddrProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocol>`
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2017-11-13'

                                def __init__(self):
                                    super(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "lldp-addr-entry"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocol', '')])),
                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ])
                                    self.address_type = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address, ['address_type', 'ipv4_address', 'ipv6_address'], name, value)


            class Statistics(Entity):
                """
                The LLDP traffic statistics for this node
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: aged_out_entries
                
                	Aged out entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_packets
                
                	Discarded packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_packets
                
                	Bad packet received and dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_tl_vs
                
                	Discarded TLVs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unrecognized_tl_vs
                
                	Unrecognized TLVs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: queue_overflow_errors
                
                	Queue overflows
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: table_overflow_errors
                
                	Table overflows
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Lldp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('transmitted_packets', (YLeaf(YType.uint32, 'transmitted-packets'), ['int'])),
                        ('aged_out_entries', (YLeaf(YType.uint32, 'aged-out-entries'), ['int'])),
                        ('discarded_packets', (YLeaf(YType.uint32, 'discarded-packets'), ['int'])),
                        ('bad_packets', (YLeaf(YType.uint32, 'bad-packets'), ['int'])),
                        ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                        ('discarded_tl_vs', (YLeaf(YType.uint32, 'discarded-tl-vs'), ['int'])),
                        ('unrecognized_tl_vs', (YLeaf(YType.uint32, 'unrecognized-tl-vs'), ['int'])),
                        ('out_of_memory_errors', (YLeaf(YType.uint32, 'out-of-memory-errors'), ['int'])),
                        ('encapsulation_errors', (YLeaf(YType.uint32, 'encapsulation-errors'), ['int'])),
                        ('queue_overflow_errors', (YLeaf(YType.uint32, 'queue-overflow-errors'), ['int'])),
                        ('table_overflow_errors', (YLeaf(YType.uint32, 'table-overflow-errors'), ['int'])),
                    ])
                    self.transmitted_packets = None
                    self.aged_out_entries = None
                    self.discarded_packets = None
                    self.bad_packets = None
                    self.received_packets = None
                    self.discarded_tl_vs = None
                    self.unrecognized_tl_vs = None
                    self.out_of_memory_errors = None
                    self.encapsulation_errors = None
                    self.queue_overflow_errors = None
                    self.table_overflow_errors = None
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Nodes.Node.Statistics, ['transmitted_packets', 'aged_out_entries', 'discarded_packets', 'bad_packets', 'received_packets', 'discarded_tl_vs', 'unrecognized_tl_vs', 'out_of_memory_errors', 'encapsulation_errors', 'queue_overflow_errors', 'table_overflow_errors'], name, value)

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity

