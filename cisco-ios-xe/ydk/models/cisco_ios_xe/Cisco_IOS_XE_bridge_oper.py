""" Cisco_IOS_XE_bridge_oper 

This module contains a collection of YANG definitions
for bridge data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BridgeMacType(Enum):
    """
    BridgeMacType (Enum Class)

    MAC address type

    .. data:: bridge_mac_type_static = 0

    .. data:: bridge_mac_type_dynamic = 1

    """

    bridge_mac_type_static = Enum.YLeaf(0, "bridge-mac-type-static")

    bridge_mac_type_dynamic = Enum.YLeaf(1, "bridge-mac-type-dynamic")


class IntfStatusType(Enum):
    """
    IntfStatusType (Enum Class)

    Interface status type

    .. data:: up = 0

    .. data:: down = 1

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")



class BridgeInstances(Entity):
    """
    This is top level container for bridge table. It can have one
    or more bridge entry.
    
    .. attribute:: bridge_entry
    
    	The bridge lists is an ordered list of bridge entries. Each bridge entries has a list of bridge interface members, and bridge attributes
    	**type**\: list of  		 :py:class:`BridgeEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeInstances.BridgeEntry>`
    
    

    """

    _prefix = 'bridge-ios-xe-oper'
    _revision = '2018-03-10'

    def __init__(self):
        super(BridgeInstances, self).__init__()
        self._top_entity = None

        self.yang_name = "bridge-instances"
        self.yang_parent_name = "Cisco-IOS-XE-bridge-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("bridge-entry", ("bridge_entry", BridgeInstances.BridgeEntry))])
        self._leafs = OrderedDict()

        self.bridge_entry = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-bridge-oper:bridge-instances"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(BridgeInstances, [], name, value)


    class BridgeEntry(Entity):
        """
        The bridge lists is an ordered list of bridge entries.
        Each bridge entries has a list of bridge interface members,
        and bridge attributes.
        
        .. attribute:: bridge_id  (key)
        
        	Bridge id <1..4094>
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	VLAN name
        	**type**\: str
        
        .. attribute:: vlan
        
        	VLAN identifier <1..4094>
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: routing_interface
        
        	The name of VLAN routing interface
        	**type**\: str
        
        .. attribute:: max_macs
        
        	The maximum number of MAC learn limit for bridge
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_macs
        
        	The number of MAC learned in bridge
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: age_time
        
        	The aging time of MAC address,0 or <10..1000000> second
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rx_packets
        
        	The number of received packets in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: rx_octets
        
        	The number of received bytes in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tx_packets
        
        	The number of transmited packets out of bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tx_octets
        
        	The number of transmited bytes out of bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flood_packets
        
        	The number of flood packets in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flood_octets
        
        	The number of flood bytes in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: rx_routed_packets
        
        	L3 packets received from bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tx_routed_packets
        
        	L3 packets transmit from bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: learn
        
        	MAC learned counter in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: age
        
        	MAC aging counter in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: move
        
        	MAC move counter in bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: bridge_intf_entries
        
        	Bridge interface member information
        	**type**\:  :py:class:`BridgeIntfEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeInstances.BridgeEntry.BridgeIntfEntries>`
        
        .. attribute:: bridge_matm_entries
        
        	Bridge matm member information
        	**type**\:  :py:class:`BridgeMatmEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeInstances.BridgeEntry.BridgeMatmEntries>`
        
        

        """

        _prefix = 'bridge-ios-xe-oper'
        _revision = '2018-03-10'

        def __init__(self):
            super(BridgeInstances.BridgeEntry, self).__init__()

            self.yang_name = "bridge-entry"
            self.yang_parent_name = "bridge-instances"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['bridge_id']
            self._child_classes = OrderedDict([("bridge-intf-entries", ("bridge_intf_entries", BridgeInstances.BridgeEntry.BridgeIntfEntries)), ("bridge-matm-entries", ("bridge_matm_entries", BridgeInstances.BridgeEntry.BridgeMatmEntries))])
            self._leafs = OrderedDict([
                ('bridge_id', (YLeaf(YType.uint32, 'bridge-id'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('vlan', (YLeaf(YType.uint32, 'vlan'), ['int'])),
                ('routing_interface', (YLeaf(YType.str, 'routing-interface'), ['str'])),
                ('max_macs', (YLeaf(YType.uint32, 'max-macs'), ['int'])),
                ('num_macs', (YLeaf(YType.uint32, 'num-macs'), ['int'])),
                ('age_time', (YLeaf(YType.uint32, 'age-time'), ['int'])),
                ('rx_packets', (YLeaf(YType.uint64, 'rx-packets'), ['int'])),
                ('rx_octets', (YLeaf(YType.uint64, 'rx-octets'), ['int'])),
                ('tx_packets', (YLeaf(YType.uint64, 'tx-packets'), ['int'])),
                ('tx_octets', (YLeaf(YType.uint64, 'tx-octets'), ['int'])),
                ('flood_packets', (YLeaf(YType.uint64, 'flood-packets'), ['int'])),
                ('flood_octets', (YLeaf(YType.uint64, 'flood-octets'), ['int'])),
                ('rx_routed_packets', (YLeaf(YType.uint64, 'rx-routed-packets'), ['int'])),
                ('tx_routed_packets', (YLeaf(YType.uint64, 'tx-routed-packets'), ['int'])),
                ('learn', (YLeaf(YType.uint64, 'learn'), ['int'])),
                ('age', (YLeaf(YType.uint64, 'age'), ['int'])),
                ('move', (YLeaf(YType.uint64, 'move'), ['int'])),
            ])
            self.bridge_id = None
            self.name = None
            self.vlan = None
            self.routing_interface = None
            self.max_macs = None
            self.num_macs = None
            self.age_time = None
            self.rx_packets = None
            self.rx_octets = None
            self.tx_packets = None
            self.tx_octets = None
            self.flood_packets = None
            self.flood_octets = None
            self.rx_routed_packets = None
            self.tx_routed_packets = None
            self.learn = None
            self.age = None
            self.move = None

            self.bridge_intf_entries = BridgeInstances.BridgeEntry.BridgeIntfEntries()
            self.bridge_intf_entries.parent = self
            self._children_name_map["bridge_intf_entries"] = "bridge-intf-entries"

            self.bridge_matm_entries = BridgeInstances.BridgeEntry.BridgeMatmEntries()
            self.bridge_matm_entries.parent = self
            self._children_name_map["bridge_matm_entries"] = "bridge-matm-entries"
            self._segment_path = lambda: "bridge-entry" + "[bridge-id='" + str(self.bridge_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-bridge-oper:bridge-instances/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeInstances.BridgeEntry, ['bridge_id', 'name', 'vlan', 'routing_interface', 'max_macs', 'num_macs', 'age_time', 'rx_packets', 'rx_octets', 'tx_packets', 'tx_octets', 'flood_packets', 'flood_octets', 'rx_routed_packets', 'tx_routed_packets', 'learn', 'age', 'move'], name, value)


        class BridgeIntfEntries(Entity):
            """
            Bridge interface member information
            
            .. attribute:: bridge_intf_entry
            
            	A list of bridge interface
            	**type**\: list of  		 :py:class:`BridgeIntfEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeInstances.BridgeEntry.BridgeIntfEntries.BridgeIntfEntry>`
            
            

            """

            _prefix = 'bridge-ios-xe-oper'
            _revision = '2018-03-10'

            def __init__(self):
                super(BridgeInstances.BridgeEntry.BridgeIntfEntries, self).__init__()

                self.yang_name = "bridge-intf-entries"
                self.yang_parent_name = "bridge-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bridge-intf-entry", ("bridge_intf_entry", BridgeInstances.BridgeEntry.BridgeIntfEntries.BridgeIntfEntry))])
                self._leafs = OrderedDict()

                self.bridge_intf_entry = YList(self)
                self._segment_path = lambda: "bridge-intf-entries"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeInstances.BridgeEntry.BridgeIntfEntries, [], name, value)


            class BridgeIntfEntry(Entity):
                """
                A list of bridge interface
                
                .. attribute:: if_name  (key)
                
                	Switch port name belong to the bridge
                	**type**\: str
                
                .. attribute:: vlan
                
                	VLAN identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: native_vlan
                
                	If the VLAN is native VLAN
                	**type**\: bool
                
                .. attribute:: admin_status
                
                	Bridge interface administration status
                	**type**\:  :py:class:`IntfStatusType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.IntfStatusType>`
                
                .. attribute:: oper_status
                
                	Bridge interface operational status
                	**type**\:  :py:class:`IntfStatusType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.IntfStatusType>`
                
                .. attribute:: encap_type
                
                	Bridge interface encapsulation type
                	**type**\: str
                
                .. attribute:: ifindex
                
                	Bridge interface index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mtu
                
                	The Maximum Transmission Unit(byte) of Bridge interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bridge-ios-xe-oper'
                _revision = '2018-03-10'

                def __init__(self):
                    super(BridgeInstances.BridgeEntry.BridgeIntfEntries.BridgeIntfEntry, self).__init__()

                    self.yang_name = "bridge-intf-entry"
                    self.yang_parent_name = "bridge-intf-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['if_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('if_name', (YLeaf(YType.str, 'if-name'), ['str'])),
                        ('vlan', (YLeaf(YType.uint32, 'vlan'), ['int'])),
                        ('native_vlan', (YLeaf(YType.boolean, 'native-vlan'), ['bool'])),
                        ('admin_status', (YLeaf(YType.enumeration, 'admin-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper', 'IntfStatusType', '')])),
                        ('oper_status', (YLeaf(YType.enumeration, 'oper-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper', 'IntfStatusType', '')])),
                        ('encap_type', (YLeaf(YType.str, 'encap-type'), ['str'])),
                        ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                    ])
                    self.if_name = None
                    self.vlan = None
                    self.native_vlan = None
                    self.admin_status = None
                    self.oper_status = None
                    self.encap_type = None
                    self.ifindex = None
                    self.mtu = None
                    self._segment_path = lambda: "bridge-intf-entry" + "[if-name='" + str(self.if_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeInstances.BridgeEntry.BridgeIntfEntries.BridgeIntfEntry, ['if_name', 'vlan', 'native_vlan', 'admin_status', 'oper_status', 'encap_type', 'ifindex', 'mtu'], name, value)


        class BridgeMatmEntries(Entity):
            """
            Bridge matm member information
            
            .. attribute:: bridge_matm_entry
            
            	A list of mac table
            	**type**\: list of  		 :py:class:`BridgeMatmEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeInstances.BridgeEntry.BridgeMatmEntries.BridgeMatmEntry>`
            
            

            """

            _prefix = 'bridge-ios-xe-oper'
            _revision = '2018-03-10'

            def __init__(self):
                super(BridgeInstances.BridgeEntry.BridgeMatmEntries, self).__init__()

                self.yang_name = "bridge-matm-entries"
                self.yang_parent_name = "bridge-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bridge-matm-entry", ("bridge_matm_entry", BridgeInstances.BridgeEntry.BridgeMatmEntries.BridgeMatmEntry))])
                self._leafs = OrderedDict()

                self.bridge_matm_entry = YList(self)
                self._segment_path = lambda: "bridge-matm-entries"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeInstances.BridgeEntry.BridgeMatmEntries, [], name, value)


            class BridgeMatmEntry(Entity):
                """
                A list of mac table
                
                .. attribute:: mac_address  (key)
                
                	MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: interface
                
                	Interface name which MAC learnt from
                	**type**\: list of str
                
                .. attribute:: vlan
                
                	VLAN identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	MAC type
                	**type**\:  :py:class:`BridgeMacType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper.BridgeMacType>`
                
                

                """

                _prefix = 'bridge-ios-xe-oper'
                _revision = '2018-03-10'

                def __init__(self):
                    super(BridgeInstances.BridgeEntry.BridgeMatmEntries.BridgeMatmEntry, self).__init__()

                    self.yang_name = "bridge-matm-entry"
                    self.yang_parent_name = "bridge-matm-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['mac_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('interface', (YLeafList(YType.str, 'interface'), ['str'])),
                        ('vlan', (YLeaf(YType.uint32, 'vlan'), ['int'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_bridge_oper', 'BridgeMacType', '')])),
                    ])
                    self.mac_address = None
                    self.interface = []
                    self.vlan = None
                    self.type = None
                    self._segment_path = lambda: "bridge-matm-entry" + "[mac-address='" + str(self.mac_address) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeInstances.BridgeEntry.BridgeMatmEntries.BridgeMatmEntry, ['mac_address', 'interface', 'vlan', 'type'], name, value)

    def clone_ptr(self):
        self._top_entity = BridgeInstances()
        return self._top_entity

