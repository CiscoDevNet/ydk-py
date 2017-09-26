""" Cisco_IOS_XR_l2_eth_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package operational data.

This module contains definitions
for the following management objects\:
  mac\-accounting\: MAC accounting operational data
  vlan\: vlan
  ethernet\-encapsulation\: ethernet encapsulation

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EfpPayloadEtype(Enum):
    """
    EfpPayloadEtype

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
    EfpTagEtype

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
    EfpTagPriority

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
    EthCapsUcastMacMode

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
    EthFiltering

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
    ImStateEnum

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
    VlanEncaps

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
    VlanQinqOuterEtype

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
    VlanService

    Layer 2 vs. Layer 3 Terminated Service

    .. data:: vlan_service_l2 = 1

    	Layer 2 Transport Service

    .. data:: vlan_service_l3 = 2

    	Layer 3 Terminated Service

    """

    vlan_service_l2 = Enum.YLeaf(1, "vlan-service-l2")

    vlan_service_l3 = Enum.YLeaf(2, "vlan-service-l3")



class EthernetEncapsulation(Entity):
    """
    ethernet encapsulation
    
    .. attribute:: nodes
    
    	Per node Ethernet encapsulation operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", EthernetEncapsulation.Nodes)}
        self._child_list_classes = {}

        self.nodes = EthernetEncapsulation.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation"


    class Nodes(Entity):
        """
        Per node Ethernet encapsulation operational data
        
        .. attribute:: node
        
        	The Ethernet encaps operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetEncapsulation.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ethernet-encapsulation"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", EthernetEncapsulation.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EthernetEncapsulation.Nodes, [], name, value)


        class Node(Entity):
            """
            The Ethernet encaps operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: unicast_mac_filters
            
            	Unicast MAC filter table (specific to this node)
            	**type**\:   :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetEncapsulation.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"unicast-mac-filters" : ("unicast_mac_filters", EthernetEncapsulation.Nodes.Node.UnicastMacFilters)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.unicast_mac_filters = EthernetEncapsulation.Nodes.Node.UnicastMacFilters()
                self.unicast_mac_filters.parent = self
                self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                self._children_yang_names.add("unicast-mac-filters")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EthernetEncapsulation.Nodes.Node, ['node_name'], name, value)


            class UnicastMacFilters(Entity):
                """
                Unicast MAC filter table (specific to this
                node)
                
                .. attribute:: unicast_mac_filter
                
                	Operational data for interface with MAC filters configured
                	**type**\: list of    :py:class:`UnicastMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, self).__init__()

                    self.yang_name = "unicast-mac-filters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"unicast-mac-filter" : ("unicast_mac_filter", EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter)}

                    self.unicast_mac_filter = YList(self)
                    self._segment_path = lambda: "unicast-mac-filters"

                def __setattr__(self, name, value):
                    self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, [], name, value)


                class UnicastMacFilter(Entity):
                    """
                    Operational data for interface with MAC
                    filters configured
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: unicast_filter
                    
                    	Unicast MAC filter information
                    	**type**\: list of    :py:class:`UnicastFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter>`
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, self).__init__()

                        self.yang_name = "unicast-mac-filter"
                        self.yang_parent_name = "unicast-mac-filters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"unicast-filter" : ("unicast_filter", EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.unicast_filter = YList(self)
                        self._segment_path = lambda: "unicast-mac-filter" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, ['interface_name'], name, value)


                    class UnicastFilter(Entity):
                        """
                        Unicast MAC filter information
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mode
                        
                        	Unicast MAC mode
                        	**type**\:   :py:class:`EthCapsUcastMacMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthCapsUcastMacMode>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, self).__init__()

                            self.yang_name = "unicast-filter"
                            self.yang_parent_name = "unicast-mac-filter"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "unicast-filter"

                        def __setattr__(self, name, value):
                            self._perform_setattr(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, ['mac_address', 'mode'], name, value)

    def clone_ptr(self):
        self._top_entity = EthernetEncapsulation()
        return self._top_entity

class MacAccounting(Entity):
    """
    MAC accounting operational data
    
    .. attribute:: interfaces
    
    	MAC accounting interface table in MIB lexicographic order
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces>`
    
    

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
        self._child_container_classes = {"interfaces" : ("interfaces", MacAccounting.Interfaces)}
        self._child_list_classes = {}

        self.interfaces = MacAccounting.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting"


    class Interfaces(Entity):
        """
        MAC accounting interface table in MIB
        lexicographic order
        
        .. attribute:: interface
        
        	Operational data and statistics for an interface configured with MAC accounting enabled
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacAccounting.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mac-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", MacAccounting.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MacAccounting.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Operational data and statistics for an
            interface configured with MAC accounting
            enabled
            
            .. attribute:: interface_name  <key>
            
            	The interface name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: egress_statistic
            
            	Egress MAC accounting statistics
            	**type**\: list of    :py:class:`EgressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.EgressStatistic>`
            
            .. attribute:: ingress_statistic
            
            	Ingress MAC accounting statistics
            	**type**\: list of    :py:class:`IngressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.IngressStatistic>`
            
            .. attribute:: state
            
            	MAC accounting state for the interface
            	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.State>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacAccounting.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"state" : ("state", MacAccounting.Interfaces.Interface.State)}
                self._child_list_classes = {"egress-statistic" : ("egress_statistic", MacAccounting.Interfaces.Interface.EgressStatistic), "ingress-statistic" : ("ingress_statistic", MacAccounting.Interfaces.Interface.IngressStatistic)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.state = MacAccounting.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.egress_statistic = YList(self)
                self.ingress_statistic = YList(self)
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MacAccounting.Interfaces.Interface, ['interface_name'], name, value)


            class EgressStatistic(Entity):
                """
                Egress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.EgressStatistic, self).__init__()

                    self.yang_name = "egress-statistic"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "egress-statistic"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.EgressStatistic, ['bytes', 'mac_address', 'packets'], name, value)


            class IngressStatistic(Entity):
                """
                Ingress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.IngressStatistic, self).__init__()

                    self.yang_name = "ingress-statistic"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.packets = YLeaf(YType.uint64, "packets")
                    self._segment_path = lambda: "ingress-statistic"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.IngressStatistic, ['bytes', 'mac_address', 'packets'], name, value)


            class State(Entity):
                """
                MAC accounting state for the interface
                
                .. attribute:: is_egress_enabled
                
                	MAC accounting on on egress
                	**type**\:  bool
                
                .. attribute:: is_ingress_enabled
                
                	MAC accounting on on ingress
                	**type**\:  bool
                
                .. attribute:: number_available_egress
                
                	MAC accounting entries available on egress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_ingress
                
                	MAC accounting entries available on ingress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_on_node
                
                	MAC accountng entries available across the node
                	**type**\:  int
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.is_egress_enabled = YLeaf(YType.boolean, "is-egress-enabled")

                    self.is_ingress_enabled = YLeaf(YType.boolean, "is-ingress-enabled")

                    self.number_available_egress = YLeaf(YType.uint32, "number-available-egress")

                    self.number_available_ingress = YLeaf(YType.uint32, "number-available-ingress")

                    self.number_available_on_node = YLeaf(YType.uint32, "number-available-on-node")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacAccounting.Interfaces.Interface.State, ['is_egress_enabled', 'is_ingress_enabled', 'number_available_egress', 'number_available_ingress', 'number_available_on_node'], name, value)

    def clone_ptr(self):
        self._top_entity = MacAccounting()
        return self._top_entity

class Vlan(Entity):
    """
    vlan
    
    .. attribute:: nodes
    
    	Per node VLAN operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", Vlan.Nodes)}
        self._child_list_classes = {}

        self.nodes = Vlan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan"


    class Nodes(Entity):
        """
        Per node VLAN operational data
        
        .. attribute:: node
        
        	The VLAN operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vlan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vlan"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Vlan.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vlan.Nodes, [], name, value)


        class Node(Entity):
            """
            The VLAN operational data for a particular node
            
            .. attribute:: node_id  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	VLAN interface table (specific to this node)
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces>`
            
            .. attribute:: tag_allocations
            
            	VLAN tag allocation table (specific to this node)
            	**type**\:   :py:class:`TagAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations>`
            
            .. attribute:: trunks
            
            	VLAN trunk table (specific to this node)
            	**type**\:   :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vlan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", Vlan.Nodes.Node.Interfaces), "tag-allocations" : ("tag_allocations", Vlan.Nodes.Node.TagAllocations), "trunks" : ("trunks", Vlan.Nodes.Node.Trunks)}
                self._child_list_classes = {}

                self.node_id = YLeaf(YType.str, "node-id")

                self.interfaces = Vlan.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.tag_allocations = Vlan.Nodes.Node.TagAllocations()
                self.tag_allocations.parent = self
                self._children_name_map["tag_allocations"] = "tag-allocations"
                self._children_yang_names.add("tag-allocations")

                self.trunks = Vlan.Nodes.Node.Trunks()
                self.trunks.parent = self
                self._children_name_map["trunks"] = "trunks"
                self._children_yang_names.add("trunks")
                self._segment_path = lambda: "node" + "[node-id='" + self.node_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2-eth-infra-oper:vlan/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vlan.Nodes.Node, ['node_id'], name, value)


            class Interfaces(Entity):
                """
                VLAN interface table (specific to this node)
                
                .. attribute:: interface
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Vlan.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
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
                        self._child_container_classes = {"encapsulation-details" : ("encapsulation_details", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails)}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.service = YLeaf(YType.enumeration, "service")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.switched_mtu = YLeaf(YType.uint16, "switched-mtu")

                        self.encapsulation_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._children_yang_names.add("encapsulation-details")
                        self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface, ['interface', 'interface_xr', 'mtu', 'parent_interface', 'service', 'state', 'switched_mtu'], name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"dot1ad-dot1q-stack" : ("dot1ad_dot1q_stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack), "service-instance-details" : ("service_instance_details", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails), "stack" : ("stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack)}
                            self._child_list_classes = {}

                            self.dot1ad_native_tag = YLeaf(YType.uint16, "dot1ad-native-tag")

                            self.dot1ad_outer_tag = YLeaf(YType.uint16, "dot1ad-outer-tag")

                            self.dot1ad_tag = YLeaf(YType.uint16, "dot1ad-tag")

                            self.native_tag = YLeaf(YType.uint16, "native-tag")

                            self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.vlan_encapsulation = YLeaf(YType.enumeration, "vlan-encapsulation")

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._children_yang_names.add("dot1ad-dot1q-stack")

                            self.service_instance_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"
                            self._children_yang_names.add("service-instance-details")

                            self.stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"
                            self._children_yang_names.add("stack")
                            self._segment_path = lambda: "encapsulation-details"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, ['dot1ad_native_tag', 'dot1ad_outer_tag', 'dot1ad_tag', 'native_tag', 'outer_tag', 'tag', 'vlan_encapsulation'], name, value)


                        class Dot1AdDot1QStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")
                                self._segment_path = lambda: "dot1ad-dot1q-stack"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack, ['outer_tag', 'second_tag'], name, value)


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"local-traffic-stack" : ("local_traffic_stack", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack)}
                                self._child_list_classes = {"pushe" : ("pushe", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe), "tags-to-match" : ("tags_to_match", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch)}

                                self.destination_mac_match = YLeaf(YType.str, "destination-mac-match")

                                self.is_exact_match = YLeaf(YType.boolean, "is-exact-match")

                                self.is_native_preserving = YLeaf(YType.boolean, "is-native-preserving")

                                self.is_native_vlan = YLeaf(YType.boolean, "is-native-vlan")

                                self.payload_ethertype = YLeaf(YType.enumeration, "payload-ethertype")

                                self.source_mac_match = YLeaf(YType.str, "source-mac-match")

                                self.tags_popped = YLeaf(YType.uint16, "tags-popped")

                                self.local_traffic_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                self._children_yang_names.add("local-traffic-stack")

                                self.pushe = YList(self)
                                self.tags_to_match = YList(self)
                                self._segment_path = lambda: "service-instance-details"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, ['destination_mac_match', 'is_exact_match', 'is_native_preserving', 'is_native_vlan', 'payload_ethertype', 'source_mac_match', 'tags_popped'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"local-traffic-tag" : ("local_traffic_tag", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag)}

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                        self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                                        self._segment_path = lambda: "local-traffic-tag"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                                    self._segment_path = lambda: "pushe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"vlan-range" : ("vlan_range", Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange)}

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.priority = YLeaf(YType.enumeration, "priority")

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.vlan_id_high = YLeaf(YType.uint16, "vlan-id-high")

                                        self.vlan_id_low = YLeaf(YType.uint16, "vlan-id-low")
                                        self._segment_path = lambda: "vlan-range"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, ['vlan_id_high', 'vlan_id_low'], name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")
                                self._segment_path = lambda: "stack"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, ['outer_tag', 'second_tag'], name, value)


            class TagAllocations(Entity):
                """
                VLAN tag allocation table (specific to this
                node)
                
                .. attribute:: tag_allocation
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`TagAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.TagAllocations, self).__init__()

                    self.yang_name = "tag-allocations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"tag-allocation" : ("tag_allocation", Vlan.Nodes.Node.TagAllocations.TagAllocation)}

                    self.tag_allocation = YList(self)
                    self._segment_path = lambda: "tag-allocations"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations, [], name, value)


                class TagAllocation(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails>`
                    
                    .. attribute:: first_tag
                    
                    	The first (outermost) tag
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: interface
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: second_tag
                    
                    	The second tag
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`VlanTagOrAny <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes.VlanTagOrAny>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 1..4096
                    
                    
                    ----
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
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
                        self._child_container_classes = {"encapsulation-details" : ("encapsulation_details", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails)}
                        self._child_list_classes = {}

                        self.first_tag = YLeaf(YType.uint32, "first-tag")

                        self.interface = YLeaf(YType.str, "interface")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.second_tag = YLeaf(YType.str, "second-tag")

                        self.service = YLeaf(YType.enumeration, "service")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.switched_mtu = YLeaf(YType.uint16, "switched-mtu")

                        self.encapsulation_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._children_yang_names.add("encapsulation-details")
                        self._segment_path = lambda: "tag-allocation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation, ['first_tag', 'interface', 'interface_xr', 'mtu', 'parent_interface', 'second_tag', 'service', 'state', 'switched_mtu'], name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "tag-allocation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"dot1ad-dot1q-stack" : ("dot1ad_dot1q_stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack), "service-instance-details" : ("service_instance_details", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails), "stack" : ("stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack)}
                            self._child_list_classes = {}

                            self.dot1ad_native_tag = YLeaf(YType.uint16, "dot1ad-native-tag")

                            self.dot1ad_outer_tag = YLeaf(YType.uint16, "dot1ad-outer-tag")

                            self.dot1ad_tag = YLeaf(YType.uint16, "dot1ad-tag")

                            self.native_tag = YLeaf(YType.uint16, "native-tag")

                            self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.vlan_encapsulation = YLeaf(YType.enumeration, "vlan-encapsulation")

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._children_yang_names.add("dot1ad-dot1q-stack")

                            self.service_instance_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"
                            self._children_yang_names.add("service-instance-details")

                            self.stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"
                            self._children_yang_names.add("stack")
                            self._segment_path = lambda: "encapsulation-details"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, ['dot1ad_native_tag', 'dot1ad_outer_tag', 'dot1ad_tag', 'native_tag', 'outer_tag', 'tag', 'vlan_encapsulation'], name, value)


                        class Dot1AdDot1QStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")
                                self._segment_path = lambda: "dot1ad-dot1q-stack"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack, ['outer_tag', 'second_tag'], name, value)


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"local-traffic-stack" : ("local_traffic_stack", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack)}
                                self._child_list_classes = {"pushe" : ("pushe", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe), "tags-to-match" : ("tags_to_match", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch)}

                                self.destination_mac_match = YLeaf(YType.str, "destination-mac-match")

                                self.is_exact_match = YLeaf(YType.boolean, "is-exact-match")

                                self.is_native_preserving = YLeaf(YType.boolean, "is-native-preserving")

                                self.is_native_vlan = YLeaf(YType.boolean, "is-native-vlan")

                                self.payload_ethertype = YLeaf(YType.enumeration, "payload-ethertype")

                                self.source_mac_match = YLeaf(YType.str, "source-mac-match")

                                self.tags_popped = YLeaf(YType.uint16, "tags-popped")

                                self.local_traffic_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                self._children_yang_names.add("local-traffic-stack")

                                self.pushe = YList(self)
                                self.tags_to_match = YList(self)
                                self._segment_path = lambda: "service-instance-details"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, ['destination_mac_match', 'is_exact_match', 'is_native_preserving', 'is_native_vlan', 'payload_ethertype', 'source_mac_match', 'tags_popped'], name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"local-traffic-tag" : ("local_traffic_tag", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag)}

                                    self.local_traffic_tag = YList(self)
                                    self._segment_path = lambda: "local-traffic-stack"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, [], name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                        self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                                        self._segment_path = lambda: "local-traffic-tag"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, ['ethertype', 'vlan_id'], name, value)


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                                    self._segment_path = lambda: "pushe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, ['ethertype', 'vlan_id'], name, value)


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"vlan-range" : ("vlan_range", Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange)}

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.priority = YLeaf(YType.enumeration, "priority")

                                    self.vlan_range = YList(self)
                                    self._segment_path = lambda: "tags-to-match"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, ['ethertype', 'priority'], name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
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
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.vlan_id_high = YLeaf(YType.uint16, "vlan-id-high")

                                        self.vlan_id_low = YLeaf(YType.uint16, "vlan-id-low")
                                        self._segment_path = lambda: "vlan-range"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, ['vlan_id_high', 'vlan_id_low'], name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")
                                self._segment_path = lambda: "stack"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, ['outer_tag', 'second_tag'], name, value)


            class Trunks(Entity):
                """
                VLAN trunk table (specific to this node)
                
                .. attribute:: trunk
                
                	Operational data for trunk interfaces configured with VLANs
                	**type**\: list of    :py:class:`Trunk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Trunks, self).__init__()

                    self.yang_name = "trunks"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"trunk" : ("trunk", Vlan.Nodes.Node.Trunks.Trunk)}

                    self.trunk = YList(self)
                    self._segment_path = lambda: "trunks"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vlan.Nodes.Node.Trunks, [], name, value)


                class Trunk(Entity):
                    """
                    Operational data for trunk interfaces
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: dot1ad_count
                    
                    	Number of subinterfaces with 802.1ad outer tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: layer2_sub_interfaces
                    
                    	Layer 2 Transport Subinterfaces
                    	**type**\:   :py:class:`Layer2SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces>`
                    
                    .. attribute:: layer3_sub_interfaces
                    
                    	Layer 3 Terminated Subinterfaces
                    	**type**\:   :py:class:`Layer3SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces>`
                    
                    .. attribute:: mac_filtering
                    
                    	IEEE 802.1Q/802.1ad multicast MAC address filtering
                    	**type**\:   :py:class:`EthFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthFiltering>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: qinq_outer_ether_type
                    
                    	QinQ Outer Tag Ether Type
                    	**type**\:   :py:class:`VlanQinqOuterEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanQinqOuterEtype>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: untagged_interface
                    
                    	Interface/Sub\-interface handling untagged frames
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.Trunks.Trunk, self).__init__()

                        self.yang_name = "trunk"
                        self.yang_parent_name = "trunks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"layer2-sub-interfaces" : ("layer2_sub_interfaces", Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces), "layer3-sub-interfaces" : ("layer3_sub_interfaces", Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces)}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.dot1ad_count = YLeaf(YType.uint32, "dot1ad-count")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mac_filtering = YLeaf(YType.enumeration, "mac-filtering")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.qinq_outer_ether_type = YLeaf(YType.enumeration, "qinq-outer-ether-type")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.untagged_interface = YLeaf(YType.str, "untagged-interface")

                        self.layer2_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces()
                        self.layer2_sub_interfaces.parent = self
                        self._children_name_map["layer2_sub_interfaces"] = "layer2-sub-interfaces"
                        self._children_yang_names.add("layer2-sub-interfaces")

                        self.layer3_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces()
                        self.layer3_sub_interfaces.parent = self
                        self._children_name_map["layer3_sub_interfaces"] = "layer3-sub-interfaces"
                        self._children_yang_names.add("layer3-sub-interfaces")
                        self._segment_path = lambda: "trunk" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk, ['interface', 'dot1ad_count', 'interface_xr', 'mac_filtering', 'mtu', 'qinq_outer_ether_type', 'state', 'untagged_interface'], name, value)


                    class Layer2SubInterfaces(Entity):
                        """
                        Layer 2 Transport Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_any_count
                        
                        	Number of double tagged subinterfaces with wildcarded inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces with explicit inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 2 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
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
                            self._child_container_classes = {"state-counters" : ("state_counters", Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters)}
                            self._child_list_classes = {}

                            self.dot1q_count = YLeaf(YType.uint32, "dot1q-count")

                            self.qin_any_count = YLeaf(YType.uint32, "qin-any-count")

                            self.qin_q_count = YLeaf(YType.uint32, "qin-q-count")

                            self.total_count = YLeaf(YType.uint32, "total-count")

                            self.untagged_count = YLeaf(YType.uint32, "untagged-count")

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._children_yang_names.add("state-counters")
                            self._segment_path = lambda: "layer2-sub-interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, ['dot1q_count', 'qin_any_count', 'qin_q_count', 'total_count', 'untagged_count'], name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.admin_down = YLeaf(YType.uint32, "admin-down")

                                self.down = YLeaf(YType.uint32, "down")

                                self.up = YLeaf(YType.uint32, "up")
                                self._segment_path = lambda: "state-counters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, ['admin_down', 'down', 'up'], name, value)


                    class Layer3SubInterfaces(Entity):
                        """
                        Layer 3 Terminated Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: native_vlan
                        
                        	Native VLAN ID configured on trunk
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 3 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, self).__init__()

                            self.yang_name = "layer3-sub-interfaces"
                            self.yang_parent_name = "trunk"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-counters" : ("state_counters", Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters)}
                            self._child_list_classes = {}

                            self.dot1q_count = YLeaf(YType.uint32, "dot1q-count")

                            self.native_vlan = YLeaf(YType.uint16, "native-vlan")

                            self.qin_q_count = YLeaf(YType.uint32, "qin-q-count")

                            self.total_count = YLeaf(YType.uint32, "total-count")

                            self.untagged_count = YLeaf(YType.uint32, "untagged-count")

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._children_yang_names.add("state-counters")
                            self._segment_path = lambda: "layer3-sub-interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, ['dot1q_count', 'native_vlan', 'qin_q_count', 'total_count', 'untagged_count'], name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.admin_down = YLeaf(YType.uint32, "admin-down")

                                self.down = YLeaf(YType.uint32, "down")

                                self.up = YLeaf(YType.uint32, "up")
                                self._segment_path = lambda: "state-counters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, ['admin_down', 'down', 'up'], name, value)

    def clone_ptr(self):
        self._top_entity = Vlan()
        return self._top_entity

