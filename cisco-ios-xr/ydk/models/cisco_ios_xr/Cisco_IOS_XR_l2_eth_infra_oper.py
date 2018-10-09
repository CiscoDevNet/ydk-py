""" Cisco_IOS_XR_l2_eth_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package operational data.

This module contains definitions
for the following management objects\:
  mac\-accounting\: MAC accounting operational data
  vlan\: vlan
  ethernet\-encapsulation\: ethernet encapsulation

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EfpPayloadEtype(Enum):
    """
    EfpPayloadEtype (Enum Class)

    Payload ethertype match

    .. data:: payload_ethertype_any = 0

    	Any

    .. data:: payload_ethertype_ip = 1

    	IP

    .. data:: payload_ethertype_pppoe = 2

    	PPPoE

    """

    payload_ethertype_any = Enum.YLeaf(0, "payload-ethertype-any")

    payload_ethertype_ip = Enum.YLeaf(1, "payload-ethertype-ip")

    payload_ethertype_pppoe = Enum.YLeaf(2, "payload-ethertype-pppoe")


class EfpTagEtype(Enum):
    """
    EfpTagEtype (Enum Class)

    Tag ethertype

    .. data:: untagged = 0

    	Untagged

    .. data:: dot1q = 33024

    	Dot1Q

    .. data:: dot1ad = 34984

    	Dot1ad

    """

    untagged = Enum.YLeaf(0, "untagged")

    dot1q = Enum.YLeaf(33024, "dot1q")

    dot1ad = Enum.YLeaf(34984, "dot1ad")


class EfpTagPriority(Enum):
    """
    EfpTagPriority (Enum Class)

    Priority

    .. data:: priority0 = 0

    	Priority 0

    .. data:: priority1 = 1

    	Priority 1

    .. data:: priority2 = 2

    	Priority 2

    .. data:: priority3 = 3

    	Priority 3

    .. data:: priority4 = 4

    	Priority 4

    .. data:: priority5 = 5

    	Priority 5

    .. data:: priority6 = 6

    	Priority 6

    .. data:: priority7 = 7

    	Priority 7

    .. data:: priority_any = 8

    	Any priority

    """

    priority0 = Enum.YLeaf(0, "priority0")

    priority1 = Enum.YLeaf(1, "priority1")

    priority2 = Enum.YLeaf(2, "priority2")

    priority3 = Enum.YLeaf(3, "priority3")

    priority4 = Enum.YLeaf(4, "priority4")

    priority5 = Enum.YLeaf(5, "priority5")

    priority6 = Enum.YLeaf(6, "priority6")

    priority7 = Enum.YLeaf(7, "priority7")

    priority_any = Enum.YLeaf(8, "priority-any")


class EthCapsUcastMacMode(Enum):
    """
    EthCapsUcastMacMode (Enum Class)

    Eth caps ucast mac mode

    .. data:: reserved = 0

    	Reserved

    .. data:: permit = 1

    	Permit

    """

    reserved = Enum.YLeaf(0, "reserved")

    permit = Enum.YLeaf(1, "permit")


class EthFiltering(Enum):
    """
    EthFiltering (Enum Class)

    Ethernet frame filtering

    .. data:: no_filtering = 0

    	No IEEE 802.1Q/802.1ad/MAC relay multicast MAC

    	address filtering

    .. data:: dot1q_filtering = 1

    	IEEE 802.1q C-VLAN filtering

    .. data:: dot1ad_filtering = 2

    	IEEE 802.1ad S-VLAN filtering

    .. data:: two_port_mac_relay_filtering = 3

    	IEEE 802.1aj 2-Port MAC relay filtering

    """

    no_filtering = Enum.YLeaf(0, "no-filtering")

    dot1q_filtering = Enum.YLeaf(1, "dot1q-filtering")

    dot1ad_filtering = Enum.YLeaf(2, "dot1ad-filtering")

    two_port_mac_relay_filtering = Enum.YLeaf(3, "two-port-mac-relay-filtering")


class ImStateEnum(Enum):
    """
    ImStateEnum (Enum Class)

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")


class VlanEncaps(Enum):
    """
    VlanEncaps (Enum Class)

    VLAN encapsulation

    .. data:: no_encapsulation = 0

    	No encapsulation

    .. data:: dot1q = 1

    	IEEE 802.1Q encapsulation

    .. data:: qinq = 2

    	Double 802.1Q encapsulation

    .. data:: qin_any = 3

    	Double 802.1Q wildcarded encapsulation

    .. data:: dot1q_native = 4

    	IEEE 802.1Q native VLAN encapsulation

    .. data:: dot1ad = 5

    	IEEE 802.1ad encapsulation

    .. data:: dot1ad_native = 6

    	IEEE 802.1ad native VLAN encapsulation

    .. data:: service_instance = 7

    	Ethernet Service Instance

    .. data:: dot1ad_dot1q = 8

    	IEEE 802.1ad 802.1Q encapsulation

    .. data:: dot1ad_any = 9

    	IEEE 802.1ad wildcard 802.1Q encapsulation

    """

    no_encapsulation = Enum.YLeaf(0, "no-encapsulation")

    dot1q = Enum.YLeaf(1, "dot1q")

    qinq = Enum.YLeaf(2, "qinq")

    qin_any = Enum.YLeaf(3, "qin-any")

    dot1q_native = Enum.YLeaf(4, "dot1q-native")

    dot1ad = Enum.YLeaf(5, "dot1ad")

    dot1ad_native = Enum.YLeaf(6, "dot1ad-native")

    service_instance = Enum.YLeaf(7, "service-instance")

    dot1ad_dot1q = Enum.YLeaf(8, "dot1ad-dot1q")

    dot1ad_any = Enum.YLeaf(9, "dot1ad-any")


class VlanQinqOuterEtype(Enum):
    """
    VlanQinqOuterEtype (Enum Class)

    QinQ Outer Tag Ethertype

    .. data:: ether_type8100 = 33024

    	Dot1Q (0x8100)

    .. data:: ether_type9100 = 37120

    	0x9100

    .. data:: ether_type9200 = 37376

    	0x9200

    """

    ether_type8100 = Enum.YLeaf(33024, "ether-type8100")

    ether_type9100 = Enum.YLeaf(37120, "ether-type9100")

    ether_type9200 = Enum.YLeaf(37376, "ether-type9200")


class VlanService(Enum):
    """
    VlanService (Enum Class)

    Layer 2 vs. Layer 3 Terminated Service

    .. data:: vlan_service_l2 = 1

    	Layer 2 Transport Service

    .. data:: vlan_service_l3 = 2

    	Layer 3 Terminated Service

    """

    vlan_service_l2 = Enum.YLeaf(1, "vlan-service-l2")

    vlan_service_l3 = Enum.YLeaf(2, "vlan-service-l3")


class VlanSwitchedMode(Enum):
    """
    VlanSwitchedMode (Enum Class)

    VLAN\-Switched mode

    .. data:: none = 0

    	Disabled

    .. data:: trunk_port = 1

    	Trunk port

    .. data:: access_port = 2

    	Access port

    """

    none = Enum.YLeaf(0, "none")

    trunk_port = Enum.YLeaf(1, "trunk-port")

    access_port = Enum.YLeaf(2, "access-port")



class MacAccounting(Entity):
    """
    MAC accounting operational data
    
    .. attribute:: interfaces
    
    	MAC accounting interface table in MIB lexicographic order
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MacAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "mac-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", MacAccounting.Interfaces))])
        self._leafs = OrderedDict()

        self.interfaces = MacAccounting.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MacAccounting, [], name, value)


    class Interfaces(Entity):
        """
        MAC accounting interface table in MIB
        lexicographic order
        
        .. attribute:: interface
        
        	Operational data and statistics for an interface configured with MAC accounting enabled
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacAccounting.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mac-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", MacAccounting.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MacAccounting.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Operational data and statistics for an
            interface configured with MAC accounting
            enabled
            
            .. attribute:: interface_name  (key)
            
            	The interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: state
            
            	MAC accounting state for the interface
            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.State>`
            
            .. attribute:: ingress_statistic
            
            	Ingress MAC accounting statistics
            	**type**\: list of  		 :py:class:`IngressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.IngressStatistic>`
            
            .. attribute:: egress_statistic
            
            	Egress MAC accounting statistics
            	**type**\: list of  		 :py:class:`EgressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.EgressStatistic>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacAccounting.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("state", ("state", MacAccounting.Interfaces.Interface.State)), ("ingress-statistic", ("ingress_statistic", MacAccounting.Interfaces.Interface.IngressStatistic)), ("egress-statistic", ("egress_statistic", MacAccounting.Interfaces.Interface.EgressStatistic))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.state = MacAccounting.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.ingress_statistic = YList(self)
                self.egress_statistic = YList(self)
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MacAccounting.Interfaces.Interface, ['interface_name'], name, value)


            class State(Entity):
                """
                MAC accounting state for the interface
                
                .. attribute:: is_ingress_enabled
                
                	MAC accounting on on ingress
                	**type**\: bool
                
                .. attribute:: is_egress_enabled
                
                	MAC accounting on on egress
                	**type**\: bool
                
                .. attribute:: number_available_ingress
                
                	MAC accounting entries available on ingress
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_egress
                
                	MAC accounting entries available on egress
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_on_node
                
                	MAC accountng entries available across the node
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_ingress_enabled', (YLeaf(YType.boolean, 'is-ingress-enabled'), ['bool'])),
                        ('is_egress_enabled', (YLeaf(YType.boolean, 'is-egress-enabled'), ['bool'])),
                        ('number_available_ingress', (YLeaf(YType.uint32, 'number-available-ingress'), ['int'])),
                        ('number_available_egress', (YLeaf(YType.uint32, 'number-available-egress'), ['int'])),
                        ('number_available_on_node', (YLeaf(YType.uint32, 'number-available-on-node'), ['int'])),
                    ])
                    self.is_ingress_enabled = None
                    self.is_egress_enabled = None
                    self.number_available_ingress = None
                    self.number_available_egress = None
                    self.number_available_on_node = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.State, [u'is_ingress_enabled', u'is_egress_enabled', u'number_available_ingress', u'number_available_egress', u'number_available_on_node'], name, value)


            class IngressStatistic(Entity):
                """
                Ingress MAC accounting statistics
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.IngressStatistic, self).__init__()

                    self.yang_name = "ingress-statistic"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.mac_address = None
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "ingress-statistic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.IngressStatistic, [u'mac_address', u'packets', u'bytes'], name, value)


            class EgressStatistic(Entity):
                """
                Egress MAC accounting statistics
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.EgressStatistic, self).__init__()

                    self.yang_name = "egress-statistic"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.mac_address = None
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "egress-statistic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.EgressStatistic, [u'mac_address', u'packets', u'bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = MacAccounting()
        return self._top_entity

class Vlan(Entity):
    """
    vlan
    
    .. attribute:: nodes
    
    	Per node VLAN operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vlan, self).__init__()
        self._top_entity = None

        self.yang_name = "vlan"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Vlan.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Vlan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vlan, [], name, value)


    class Nodes(Entity):
        """
        Per node VLAN operational data
        
        .. attribute:: node
        
        	The VLAN operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vlan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vlan"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Vlan.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vlan.Nodes, [], name, value)


        class Node(Entity):
            """
            The VLAN operational data for a particular node
            
            .. attribute:: node_id  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: trunks
            
            	VLAN trunk table (specific to this node)
            	**type**\:  :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks>`
            
            .. attribute:: interfaces
            
            	VLAN interface table (specific to this node)
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces>`
            
            .. attribute:: tag_allocations
            
            	VLAN tag allocation table (specific to this node)
            	**type**\:  :py:class:`TagAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vlan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_id']
                self._child_classes = OrderedDict([("trunks", ("trunks", Vlan.Nodes.Node.Trunks)), ("interfaces", ("interfaces", Vlan.Nodes.Node.Interfaces)), ("tag-allocations", ("tag_allocations", Vlan.Nodes.Node.TagAllocations))])
                self._leafs = OrderedDict([
                    ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                ])
                self.node_id = None

                self.trunks = Vlan.Nodes.Node.Trunks()
                self.trunks.parent = self
                self._children_name_map["trunks"] = "trunks"

                self.interfaces = Vlan.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.tag_allocations = Vlan.Nodes.Node.TagAllocations()
                self.tag_allocations.parent = self
                self._children_name_map["tag_allocations"] = "tag-allocations"
                self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vlan.Nodes.Node, ['node_id'], name, value)


            class Trunks(Entity):
                """
                VLAN trunk table (specific to this node)
                
                .. attribute:: trunk
                
                	Operational data for trunk interfaces configured with VLANs
                	**type**\: list of  		 :py:class:`Trunk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Trunks, self).__init__()

                    self.yang_name = "trunks"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trunk", ("trunk", Vlan.Nodes.Node.Trunks.Trunk))])
                    self._leafs = OrderedDict()

                    self.trunk = YList(self)
                    self._segment_path = lambda: "trunks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.Trunks, [], name, value)


                class Trunk(Entity):
                    """
                    Operational data for trunk interfaces
                    configured with VLANs
                    
                    .. attribute:: interface  (key)
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: layer2_sub_interfaces
                    
                    	Layer 2 Transport Subinterfaces
                    	**type**\:  :py:class:`Layer2SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces>`
                    
                    .. attribute:: layer3_sub_interfaces
                    
                    	Layer 3 Terminated Subinterfaces
                    	**type**\:  :py:class:`Layer3SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces>`
                    
                    .. attribute:: vlan_switched
                    
                    	VLAN\-Switched information
                    	**type**\:  :py:class:`VlanSwitched <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: qinq_outer_ether_type
                    
                    	QinQ Outer Tag Ether Type
                    	**type**\:  :py:class:`VlanQinqOuterEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanQinqOuterEtype>`
                    
                    .. attribute:: dot1ad_count
                    
                    	Number of subinterfaces with 802.1ad outer tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: untagged_interface
                    
                    	Interface/Sub\-interface handling untagged frames
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mac_filtering
                    
                    	IEEE 802.1Q/802.1ad multicast MAC address filtering
                    	**type**\:  :py:class:`EthFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthFiltering>`
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.Trunks.Trunk, self).__init__()

                        self.yang_name = "trunk"
                        self.yang_parent_name = "trunks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_classes = OrderedDict([("layer2-sub-interfaces", ("layer2_sub_interfaces", Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces)), ("layer3-sub-interfaces", ("layer3_sub_interfaces", Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces)), ("vlan-switched", ("vlan_switched", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnum', '')])),
                            ('mtu', (YLeaf(YType.uint16, 'mtu'), ['int'])),
                            ('qinq_outer_ether_type', (YLeaf(YType.enumeration, 'qinq-outer-ether-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanQinqOuterEtype', '')])),
                            ('dot1ad_count', (YLeaf(YType.uint32, 'dot1ad-count'), ['int'])),
                            ('untagged_interface', (YLeaf(YType.str, 'untagged-interface'), ['str'])),
                            ('mac_filtering', (YLeaf(YType.enumeration, 'mac-filtering'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthFiltering', '')])),
                        ])
                        self.interface = None
                        self.interface_xr = None
                        self.state = None
                        self.mtu = None
                        self.qinq_outer_ether_type = None
                        self.dot1ad_count = None
                        self.untagged_interface = None
                        self.mac_filtering = None

                        self.layer2_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces()
                        self.layer2_sub_interfaces.parent = self
                        self._children_name_map["layer2_sub_interfaces"] = "layer2-sub-interfaces"

                        self.layer3_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces()
                        self.layer3_sub_interfaces.parent = self
                        self._children_name_map["layer3_sub_interfaces"] = "layer3-sub-interfaces"

                        self.vlan_switched = Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched()
                        self.vlan_switched.parent = self
                        self._children_name_map["vlan_switched"] = "vlan-switched"
                        self._segment_path = lambda: "trunk" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk, ['interface', 'interface_xr', 'state', 'mtu', 'qinq_outer_ether_type', 'dot1ad_count', 'untagged_interface', 'mac_filtering'], name, value)


                    class Layer2SubInterfaces(Entity):
                        """
                        Layer 2 Transport Subinterfaces
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:  :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 2 subinterfaces configured
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces with explicit inner tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_any_count
                        
                        	Number of double tagged subinterfaces with wildcarded inner tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, self).__init__()

                            self.yang_name = "layer2-sub-interfaces"
                            self.yang_parent_name = "trunk"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("state-counters", ("state_counters", Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters))])
                            self._leafs = OrderedDict([
                                ('total_count', (YLeaf(YType.uint32, 'total-count'), ['int'])),
                                ('dot1q_count', (YLeaf(YType.uint32, 'dot1q-count'), ['int'])),
                                ('qin_q_count', (YLeaf(YType.uint32, 'qin-q-count'), ['int'])),
                                ('qin_any_count', (YLeaf(YType.uint32, 'qin-any-count'), ['int'])),
                                ('untagged_count', (YLeaf(YType.uint32, 'untagged-count'), ['int'])),
                            ])
                            self.total_count = None
                            self.dot1q_count = None
                            self.qin_q_count = None
                            self.qin_any_count = None
                            self.untagged_count = None

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._segment_path = lambda: "layer2-sub-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, ['total_count', 'dot1q_count', 'qin_q_count', 'qin_any_count', 'untagged_count'], name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, self).__init__()

                                self.yang_name = "state-counters"
                                self.yang_parent_name = "layer2-sub-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('up', (YLeaf(YType.uint32, 'up'), ['int'])),
                                    ('down', (YLeaf(YType.uint32, 'down'), ['int'])),
                                    ('admin_down', (YLeaf(YType.uint32, 'admin-down'), ['int'])),
                                ])
                                self.up = None
                                self.down = None
                                self.admin_down = None
                                self._segment_path = lambda: "state-counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, ['up', 'down', 'admin_down'], name, value)


                    class Layer3SubInterfaces(Entity):
                        """
                        Layer 3 Terminated Subinterfaces
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:  :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 3 subinterfaces configured
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: native_vlan
                        
                        	Native VLAN ID configured on trunk
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, self).__init__()

                            self.yang_name = "layer3-sub-interfaces"
                            self.yang_parent_name = "trunk"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("state-counters", ("state_counters", Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters))])
                            self._leafs = OrderedDict([
                                ('total_count', (YLeaf(YType.uint32, 'total-count'), ['int'])),
                                ('dot1q_count', (YLeaf(YType.uint32, 'dot1q-count'), ['int'])),
                                ('qin_q_count', (YLeaf(YType.uint32, 'qin-q-count'), ['int'])),
                                ('untagged_count', (YLeaf(YType.uint32, 'untagged-count'), ['int'])),
                                ('native_vlan', (YLeaf(YType.uint16, 'native-vlan'), ['int'])),
                            ])
                            self.total_count = None
                            self.dot1q_count = None
                            self.qin_q_count = None
                            self.untagged_count = None
                            self.native_vlan = None

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._segment_path = lambda: "layer3-sub-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, ['total_count', 'dot1q_count', 'qin_q_count', 'untagged_count', 'native_vlan'], name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, self).__init__()

                                self.yang_name = "state-counters"
                                self.yang_parent_name = "layer3-sub-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('up', (YLeaf(YType.uint32, 'up'), ['int'])),
                                    ('down', (YLeaf(YType.uint32, 'down'), ['int'])),
                                    ('admin_down', (YLeaf(YType.uint32, 'admin-down'), ['int'])),
                                ])
                                self.up = None
                                self.down = None
                                self.admin_down = None
                                self._segment_path = lambda: "state-counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, ['up', 'down', 'admin_down'], name, value)


                    class VlanSwitched(Entity):
                        """
                        VLAN\-Switched information
                        
                        .. attribute:: trunk_vlan_ranges
                        
                        	VLAN\-Switched Trunk VLAN ranges
                        	**type**\:  :py:class:`TrunkVlanRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges>`
                        
                        .. attribute:: mode
                        
                        	VLAN\-Switched mode
                        	**type**\:  :py:class:`VlanSwitchedMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanSwitchedMode>`
                        
                        .. attribute:: access_vlan
                        
                        	VLAN\-Switched Access VLAN
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched, self).__init__()

                            self.yang_name = "vlan-switched"
                            self.yang_parent_name = "trunk"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("trunk-vlan-ranges", ("trunk_vlan_ranges", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges))])
                            self._leafs = OrderedDict([
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanSwitchedMode', '')])),
                                ('access_vlan', (YLeaf(YType.uint16, 'access-vlan'), ['int'])),
                            ])
                            self.mode = None
                            self.access_vlan = None

                            self.trunk_vlan_ranges = Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges()
                            self.trunk_vlan_ranges.parent = self
                            self._children_name_map["trunk_vlan_ranges"] = "trunk-vlan-ranges"
                            self._segment_path = lambda: "vlan-switched"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched, ['mode', 'access_vlan'], name, value)


                        class TrunkVlanRanges(Entity):
                            """
                            VLAN\-Switched Trunk VLAN ranges
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:  :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:  :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: bool
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of  		 :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of  		 :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.Pushe>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges, self).__init__()

                                self.yang_name = "trunk-vlan-ranges"
                                self.yang_parent_name = "vlan-switched"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-traffic-stack", ("local_traffic_stack", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack)), ("tags-to-match", ("tags_to_match", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch)), ("pushe", ("pushe", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.Pushe))])
                                self._leafs = OrderedDict([
                                    ('payload_ethertype', (YLeaf(YType.enumeration, 'payload-ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpPayloadEtype', '')])),
                                    ('tags_popped', (YLeaf(YType.uint16, 'tags-popped'), ['int'])),
                                    ('is_exact_match', (YLeaf(YType.boolean, 'is-exact-match'), ['bool'])),
                                    ('is_native_vlan', (YLeaf(YType.boolean, 'is-native-vlan'), ['bool'])),
                                    ('is_native_preserving', (YLeaf(YType.boolean, 'is-native-preserving'), ['bool'])),
                                    ('source_mac_match', (YLeaf(YType.str, 'source-mac-match'), ['str'])),
                                    ('destination_mac_match', (YLeaf(YType.str, 'destination-mac-match'), ['str'])),
                                ])
                                self.payload_ethertype = None
                                self.tags_popped = None
                                self.is_exact_match = None
                                self.is_native_vlan = None
                                self.is_native_preserving = None
                                self.source_mac_match = None
                                self.destination_mac_match = None

                                self.local_traffic_stack = Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"

                                self.tags_to_match = YList(self)
                                self.pushe = YList(self)
                                self._segment_path = lambda: "trunk-vlan-ranges"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges, ['payload_ethertype', 'tags_popped', 'is_exact_match', 'is_native_vlan', 'is_native_preserving', 'source_mac_match', 'destination_mac_match'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of  		 :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("local-traffic-tag", ("local_traffic_tag", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag))])
                                    self._leafs = OrderedDict()

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                            ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                        ])
                                        self.ethertype = None
                                        self.vlan_id = None
                                        self._segment_path = lambda: "local-traffic-tag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:  :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of  		 :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vlan-range", ("vlan_range", Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange))])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagPriority', '')])),
                                    ])
                                    self.ethertype = None
                                    self.priority = None

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vlan_id_low', (YLeaf(YType.uint16, 'vlan-id-low'), ['int'])),
                                            ('vlan_id_high', (YLeaf(YType.uint16, 'vlan-id-high'), ['int'])),
                                        ])
                                        self.vlan_id_low = None
                                        self.vlan_id_high = None
                                        self._segment_path = lambda: "vlan-range"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.TagsToMatch.VlanRange, ['vlan_id_low', 'vlan_id_high'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "trunk-vlan-ranges"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                    ])
                                    self.ethertype = None
                                    self.vlan_id = None
                                    self._segment_path = lambda: "pushe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.VlanSwitched.TrunkVlanRanges.Pushe, ['ethertype', 'vlan_id'], name, value)


            class Interfaces(Entity):
                """
                VLAN interface table (specific to this node)
                
                .. attribute:: interface
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Vlan.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: interface  (key)
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:  :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:  :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_classes = OrderedDict([("encapsulation-details", ("encapsulation_details", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                            ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                            ('service', (YLeaf(YType.enumeration, 'service'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanService', '')])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnum', '')])),
                            ('mtu', (YLeaf(YType.uint16, 'mtu'), ['int'])),
                            ('switched_mtu', (YLeaf(YType.uint16, 'switched-mtu'), ['int'])),
                        ])
                        self.interface = None
                        self.interface_xr = None
                        self.parent_interface = None
                        self.service = None
                        self.state = None
                        self.mtu = None
                        self.switched_mtu = None

                        self.encapsulation_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface, ['interface', 'interface_xr', 'parent_interface', 'service', 'state', 'mtu', 'switched_mtu'], name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack>`
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:  :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:  :py:class:`Dot1adDot1qStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1adDot1qStack>`
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:  :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stack", ("stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack)), ("service-instance-details", ("service_instance_details", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails)), ("dot1ad-dot1q-stack", ("dot1ad_dot1q_stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1adDot1qStack))])
                            self._leafs = OrderedDict([
                                ('vlan_encapsulation', (YLeaf(YType.enumeration, 'vlan-encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanEncaps', '')])),
                                ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                                ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                ('native_tag', (YLeaf(YType.uint16, 'native-tag'), ['int'])),
                                ('dot1ad_tag', (YLeaf(YType.uint16, 'dot1ad-tag'), ['int'])),
                                ('dot1ad_native_tag', (YLeaf(YType.uint16, 'dot1ad-native-tag'), ['int'])),
                                ('dot1ad_outer_tag', (YLeaf(YType.uint16, 'dot1ad-outer-tag'), ['int'])),
                            ])
                            self.vlan_encapsulation = None
                            self.tag = None
                            self.outer_tag = None
                            self.native_tag = None
                            self.dot1ad_tag = None
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None

                            self.stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"

                            self.service_instance_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1adDot1qStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._segment_path = lambda: "encapsulation-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, ['vlan_encapsulation', 'tag', 'outer_tag', 'native_tag', 'dot1ad_tag', 'dot1ad_native_tag', 'dot1ad_outer_tag'], name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, self).__init__()

                                self.yang_name = "stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, ['outer_tag', 'second_tag'], name, value)


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:  :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:  :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: bool
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of  		 :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of  		 :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-traffic-stack", ("local_traffic_stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack)), ("tags-to-match", ("tags_to_match", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch)), ("pushe", ("pushe", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe))])
                                self._leafs = OrderedDict([
                                    ('payload_ethertype', (YLeaf(YType.enumeration, 'payload-ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpPayloadEtype', '')])),
                                    ('tags_popped', (YLeaf(YType.uint16, 'tags-popped'), ['int'])),
                                    ('is_exact_match', (YLeaf(YType.boolean, 'is-exact-match'), ['bool'])),
                                    ('is_native_vlan', (YLeaf(YType.boolean, 'is-native-vlan'), ['bool'])),
                                    ('is_native_preserving', (YLeaf(YType.boolean, 'is-native-preserving'), ['bool'])),
                                    ('source_mac_match', (YLeaf(YType.str, 'source-mac-match'), ['str'])),
                                    ('destination_mac_match', (YLeaf(YType.str, 'destination-mac-match'), ['str'])),
                                ])
                                self.payload_ethertype = None
                                self.tags_popped = None
                                self.is_exact_match = None
                                self.is_native_vlan = None
                                self.is_native_preserving = None
                                self.source_mac_match = None
                                self.destination_mac_match = None

                                self.local_traffic_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"

                                self.tags_to_match = YList(self)
                                self.pushe = YList(self)
                                self._segment_path = lambda: "service-instance-details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, ['payload_ethertype', 'tags_popped', 'is_exact_match', 'is_native_vlan', 'is_native_preserving', 'source_mac_match', 'destination_mac_match'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of  		 :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("local-traffic-tag", ("local_traffic_tag", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag))])
                                    self._leafs = OrderedDict()

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                            ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                        ])
                                        self.ethertype = None
                                        self.vlan_id = None
                                        self._segment_path = lambda: "local-traffic-tag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:  :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of  		 :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vlan-range", ("vlan_range", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange))])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagPriority', '')])),
                                    ])
                                    self.ethertype = None
                                    self.priority = None

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vlan_id_low', (YLeaf(YType.uint16, 'vlan-id-low'), ['int'])),
                                            ('vlan_id_high', (YLeaf(YType.uint16, 'vlan-id-high'), ['int'])),
                                        ])
                                        self.vlan_id_low = None
                                        self.vlan_id_high = None
                                        self._segment_path = lambda: "vlan-range"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, ['vlan_id_low', 'vlan_id_high'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                    ])
                                    self.ethertype = None
                                    self.vlan_id = None
                                    self._segment_path = lambda: "pushe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, ['ethertype', 'vlan_id'], name, value)


                        class Dot1adDot1qStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1adDot1qStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "dot1ad-dot1q-stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1adDot1qStack, ['outer_tag', 'second_tag'], name, value)


            class TagAllocations(Entity):
                """
                VLAN tag allocation table (specific to this
                node)
                
                .. attribute:: tag_allocation
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of  		 :py:class:`TagAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.TagAllocations, self).__init__()

                    self.yang_name = "tag-allocations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tag-allocation", ("tag_allocation", Vlan.Nodes.Node.TagAllocations.TagAllocation))])
                    self._leafs = OrderedDict()

                    self.tag_allocation = YList(self)
                    self._segment_path = lambda: "tag-allocations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations, [], name, value)


                class TagAllocation(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: interface
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: first_tag
                    
                    	The first (outermost) tag
                    	**type**\: int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: second_tag
                    
                    	The second tag
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`VlanTagOrAny <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes.VlanTagOrAny>`
                    
                    		**type**\: int
                    
                    			**range:** 1..4096
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:  :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:  :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation, self).__init__()

                        self.yang_name = "tag-allocation"
                        self.yang_parent_name = "tag-allocations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("encapsulation-details", ("encapsulation_details", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('first_tag', (YLeaf(YType.uint32, 'first-tag'), ['int'])),
                            ('second_tag', (YLeaf(YType.str, 'second-tag'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny', ''),'int'])),
                            ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                            ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                            ('service', (YLeaf(YType.enumeration, 'service'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanService', '')])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnum', '')])),
                            ('mtu', (YLeaf(YType.uint16, 'mtu'), ['int'])),
                            ('switched_mtu', (YLeaf(YType.uint16, 'switched-mtu'), ['int'])),
                        ])
                        self.interface = None
                        self.first_tag = None
                        self.second_tag = None
                        self.interface_xr = None
                        self.parent_interface = None
                        self.service = None
                        self.state = None
                        self.mtu = None
                        self.switched_mtu = None

                        self.encapsulation_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._segment_path = lambda: "tag-allocation"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation, ['interface', 'first_tag', 'second_tag', 'interface_xr', 'parent_interface', 'service', 'state', 'mtu', 'switched_mtu'], name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:  :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:  :py:class:`Dot1adDot1qStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1adDot1qStack>`
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:  :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "tag-allocation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stack", ("stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack)), ("service-instance-details", ("service_instance_details", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails)), ("dot1ad-dot1q-stack", ("dot1ad_dot1q_stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1adDot1qStack))])
                            self._leafs = OrderedDict([
                                ('vlan_encapsulation', (YLeaf(YType.enumeration, 'vlan-encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanEncaps', '')])),
                                ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                                ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                ('native_tag', (YLeaf(YType.uint16, 'native-tag'), ['int'])),
                                ('dot1ad_tag', (YLeaf(YType.uint16, 'dot1ad-tag'), ['int'])),
                                ('dot1ad_native_tag', (YLeaf(YType.uint16, 'dot1ad-native-tag'), ['int'])),
                                ('dot1ad_outer_tag', (YLeaf(YType.uint16, 'dot1ad-outer-tag'), ['int'])),
                            ])
                            self.vlan_encapsulation = None
                            self.tag = None
                            self.outer_tag = None
                            self.native_tag = None
                            self.dot1ad_tag = None
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None

                            self.stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"

                            self.service_instance_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1adDot1qStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._segment_path = lambda: "encapsulation-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, ['vlan_encapsulation', 'tag', 'outer_tag', 'native_tag', 'dot1ad_tag', 'dot1ad_native_tag', 'dot1ad_outer_tag'], name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, self).__init__()

                                self.yang_name = "stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, ['outer_tag', 'second_tag'], name, value)


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:  :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:  :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: bool
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of  		 :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of  		 :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-traffic-stack", ("local_traffic_stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack)), ("tags-to-match", ("tags_to_match", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch)), ("pushe", ("pushe", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe))])
                                self._leafs = OrderedDict([
                                    ('payload_ethertype', (YLeaf(YType.enumeration, 'payload-ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpPayloadEtype', '')])),
                                    ('tags_popped', (YLeaf(YType.uint16, 'tags-popped'), ['int'])),
                                    ('is_exact_match', (YLeaf(YType.boolean, 'is-exact-match'), ['bool'])),
                                    ('is_native_vlan', (YLeaf(YType.boolean, 'is-native-vlan'), ['bool'])),
                                    ('is_native_preserving', (YLeaf(YType.boolean, 'is-native-preserving'), ['bool'])),
                                    ('source_mac_match', (YLeaf(YType.str, 'source-mac-match'), ['str'])),
                                    ('destination_mac_match', (YLeaf(YType.str, 'destination-mac-match'), ['str'])),
                                ])
                                self.payload_ethertype = None
                                self.tags_popped = None
                                self.is_exact_match = None
                                self.is_native_vlan = None
                                self.is_native_preserving = None
                                self.source_mac_match = None
                                self.destination_mac_match = None

                                self.local_traffic_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"

                                self.tags_to_match = YList(self)
                                self.pushe = YList(self)
                                self._segment_path = lambda: "service-instance-details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, ['payload_ethertype', 'tags_popped', 'is_exact_match', 'is_native_vlan', 'is_native_preserving', 'source_mac_match', 'destination_mac_match'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of  		 :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("local-traffic-tag", ("local_traffic_tag", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag))])
                                    self._leafs = OrderedDict()

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                            ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                        ])
                                        self.ethertype = None
                                        self.vlan_id = None
                                        self._segment_path = lambda: "local-traffic-tag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:  :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of  		 :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vlan-range", ("vlan_range", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange))])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagPriority', '')])),
                                    ])
                                    self.ethertype = None
                                    self.priority = None

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('vlan_id_low', (YLeaf(YType.uint16, 'vlan-id-low'), ['int'])),
                                            ('vlan_id_high', (YLeaf(YType.uint16, 'vlan-id-high'), ['int'])),
                                        ])
                                        self.vlan_id_low = None
                                        self.vlan_id_high = None
                                        self._segment_path = lambda: "vlan-range"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, ['vlan_id_low', 'vlan_id_high'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:  :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ethertype', (YLeaf(YType.enumeration, 'ethertype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtype', '')])),
                                        ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                    ])
                                    self.ethertype = None
                                    self.vlan_id = None
                                    self._segment_path = lambda: "pushe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, ['ethertype', 'vlan_id'], name, value)


                        class Dot1adDot1qStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1adDot1qStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outer_tag', (YLeaf(YType.uint16, 'outer-tag'), ['int'])),
                                    ('second_tag', (YLeaf(YType.uint16, 'second-tag'), ['int'])),
                                ])
                                self.outer_tag = None
                                self.second_tag = None
                                self._segment_path = lambda: "dot1ad-dot1q-stack"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1adDot1qStack, ['outer_tag', 'second_tag'], name, value)

    def clone_ptr(self):
        self._top_entity = Vlan()
        return self._top_entity

class EthernetEncapsulation(Entity):
    """
    ethernet encapsulation
    
    .. attribute:: nodes
    
    	Per node Ethernet encapsulation operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(EthernetEncapsulation, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-encapsulation"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", EthernetEncapsulation.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = EthernetEncapsulation.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EthernetEncapsulation, [], name, value)


    class Nodes(Entity):
        """
        Per node Ethernet encapsulation operational data
        
        .. attribute:: node
        
        	The Ethernet encaps operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetEncapsulation.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ethernet-encapsulation"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", EthernetEncapsulation.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetEncapsulation.Nodes, [], name, value)


        class Node(Entity):
            """
            The Ethernet encaps operational data for a
            particular node
            
            .. attribute:: node_name  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: unicast_mac_filters
            
            	Unicast MAC filter table (specific to this node)
            	**type**\:  :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetEncapsulation.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("unicast-mac-filters", ("unicast_mac_filters", EthernetEncapsulation.Nodes.Node.UnicastMacFilters))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.unicast_mac_filters = EthernetEncapsulation.Nodes.Node.UnicastMacFilters()
                self.unicast_mac_filters.parent = self
                self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetEncapsulation.Nodes.Node, ['node_name'], name, value)


            class UnicastMacFilters(Entity):
                """
                Unicast MAC filter table (specific to this
                node)
                
                .. attribute:: unicast_mac_filter
                
                	Operational data for interface with MAC filters configured
                	**type**\: list of  		 :py:class:`UnicastMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, self).__init__()

                    self.yang_name = "unicast-mac-filters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("unicast-mac-filter", ("unicast_mac_filter", EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter))])
                    self._leafs = OrderedDict()

                    self.unicast_mac_filter = YList(self)
                    self._segment_path = lambda: "unicast-mac-filters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, [], name, value)


                class UnicastMacFilter(Entity):
                    """
                    Operational data for interface with MAC
                    filters configured
                    
                    .. attribute:: interface_name  (key)
                    
                    	The interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: unicast_filter
                    
                    	Unicast MAC filter information
                    	**type**\: list of  		 :py:class:`UnicastFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter>`
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, self).__init__()

                        self.yang_name = "unicast-mac-filter"
                        self.yang_parent_name = "unicast-mac-filters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("unicast-filter", ("unicast_filter", EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.unicast_filter = YList(self)
                        self._segment_path = lambda: "unicast-mac-filter" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, ['interface_name'], name, value)


                    class UnicastFilter(Entity):
                        """
                        Unicast MAC filter information
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mode
                        
                        	Unicast MAC mode
                        	**type**\:  :py:class:`EthCapsUcastMacMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthCapsUcastMacMode>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, self).__init__()

                            self.yang_name = "unicast-filter"
                            self.yang_parent_name = "unicast-mac-filter"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthCapsUcastMacMode', '')])),
                            ])
                            self.mac_address = None
                            self.mode = None
                            self._segment_path = lambda: "unicast-filter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, [u'mac_address', u'mode'], name, value)

    def clone_ptr(self):
        self._top_entity = EthernetEncapsulation()
        return self._top_entity

