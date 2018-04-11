""" Cisco_IOS_XR_subscriber_ipsub_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-ipsub package operational data.

This module contains definitions
for the following management objects\:
  ip\-subscriber\: IP subscriber operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpsubMaIntfInitiatorData(Enum):
    """
    IpsubMaIntfInitiatorData (Enum Class)

    Ipsub ma intf initiator data

    .. data:: dhcp = 0

    	Session creation via DHCP discover packet

    .. data:: packet_trigger = 1

    	Session creation via unclassified IPv4 packet

    .. data:: invalid_trigger = 2

    	Invalid Trigger

    """

    dhcp = Enum.YLeaf(0, "dhcp")

    packet_trigger = Enum.YLeaf(1, "packet-trigger")

    invalid_trigger = Enum.YLeaf(2, "invalid-trigger")


class IpsubMaIntfStateData(Enum):
    """
    IpsubMaIntfStateData (Enum Class)

    Interface states

    .. data:: invalid = 0

    	Invalid state

    .. data:: initialized = 1

    	Initial state

    .. data:: session_creation_started = 2

    	Interface creation started

    .. data:: control_policy_executing = 3

    	Interface created in IM, AAA session start

    	called

    .. data:: control_policy_executed = 4

    	AAA session created

    .. data:: session_features_applied = 5

    	Interface config activated

    .. data:: vrf_configured = 6

    	Interface address and VRF information received

    	from IPv4

    .. data:: adding_adjacency = 7

    	VRF configuration received and interface config

    	activated

    .. data:: adjacency_added = 8

    	Subscriber AIB adjacency added

    .. data:: up = 9

    	Session up

    .. data:: down = 10

    	Session down

    .. data:: address_family_down = 11

    	Session down in progress

    .. data:: address_family_down_complete = 12

    	Session down complete

    .. data:: disconnecting = 13

    	Session teardown in progress

    .. data:: disconnected = 14

    	Session disconnected

    .. data:: error = 15

    	Session in error state

    """

    invalid = Enum.YLeaf(0, "invalid")

    initialized = Enum.YLeaf(1, "initialized")

    session_creation_started = Enum.YLeaf(2, "session-creation-started")

    control_policy_executing = Enum.YLeaf(3, "control-policy-executing")

    control_policy_executed = Enum.YLeaf(4, "control-policy-executed")

    session_features_applied = Enum.YLeaf(5, "session-features-applied")

    vrf_configured = Enum.YLeaf(6, "vrf-configured")

    adding_adjacency = Enum.YLeaf(7, "adding-adjacency")

    adjacency_added = Enum.YLeaf(8, "adjacency-added")

    up = Enum.YLeaf(9, "up")

    down = Enum.YLeaf(10, "down")

    address_family_down = Enum.YLeaf(11, "address-family-down")

    address_family_down_complete = Enum.YLeaf(12, "address-family-down-complete")

    disconnecting = Enum.YLeaf(13, "disconnecting")

    disconnected = Enum.YLeaf(14, "disconnected")

    error = Enum.YLeaf(15, "error")


class IpsubMaParentIntfStateData(Enum):
    """
    IpsubMaParentIntfStateData (Enum Class)

    Parent interface state

    .. data:: deleted = 0

    	Interface being deleted

    .. data:: down = 1

    	Interface operationally down

    .. data:: up = 2

    	Interface up

    """

    deleted = Enum.YLeaf(0, "deleted")

    down = Enum.YLeaf(1, "down")

    up = Enum.YLeaf(2, "up")


class IpsubMaParentIntfVlan(Enum):
    """
    IpsubMaParentIntfVlan (Enum Class)

    Access interface VLAN type

    .. data:: plain = 0

    	Plain

    .. data:: ambiguous = 1

    	Ambiguous

    """

    plain = Enum.YLeaf(0, "plain")

    ambiguous = Enum.YLeaf(1, "ambiguous")



class IpSubscriber(Entity):
    """
    IP subscriber operational data
    
    .. attribute:: nodes
    
    	IP subscriber operational data for a particular location
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes>`
    
    

    """

    _prefix = 'subscriber-ipsub-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(IpSubscriber, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-subscriber"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-ipsub-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", IpSubscriber.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = IpSubscriber.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber"


    class Nodes(Entity):
        """
        IP subscriber operational data for a particular
        location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-ipsub-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpSubscriber.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ip-subscriber"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", IpSubscriber.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IpSubscriber.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: node_name  (key)
            
            	The node ID to filter on. For eg., 0/1/CPU0
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	IP subscriber interface summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary>`
            
            .. attribute:: interfaces
            
            	IP subscriber interface table
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces>`
            
            .. attribute:: access_interfaces
            
            	IP subscriber access interface table
            	**type**\:  :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces>`
            
            

            """

            _prefix = 'subscriber-ipsub-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpSubscriber.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("summary", ("summary", IpSubscriber.Nodes.Node.Summary)), ("interfaces", ("interfaces", IpSubscriber.Nodes.Node.Interfaces)), ("access-interfaces", ("access_interfaces", IpSubscriber.Nodes.Node.AccessInterfaces))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.summary = IpSubscriber.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

                self.interfaces = IpSubscriber.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.access_interfaces = IpSubscriber.Nodes.Node.AccessInterfaces()
                self.access_interfaces.parent = self
                self._children_name_map["access_interfaces"] = "access-interfaces"
                self._children_yang_names.add("access-interfaces")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IpSubscriber.Nodes.Node, ['node_name'], name, value)


            class Summary(Entity):
                """
                IP subscriber interface summary
                
                .. attribute:: access_interface_summary
                
                	Access interface summary statistics
                	**type**\:  :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary>`
                
                .. attribute:: interface_counts
                
                	Initiator interface counts
                	**type**\:  :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts>`
                
                .. attribute:: vrf
                
                	Array of VRFs with IPSUB interfaces
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.Vrf>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("access-interface-summary", ("access_interface_summary", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary)), ("interface-counts", ("interface_counts", IpSubscriber.Nodes.Node.Summary.InterfaceCounts))])
                    self._child_list_classes = OrderedDict([("vrf", ("vrf", IpSubscriber.Nodes.Node.Summary.Vrf))])
                    self._leafs = OrderedDict()

                    self.access_interface_summary = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary()
                    self.access_interface_summary.parent = self
                    self._children_name_map["access_interface_summary"] = "access-interface-summary"
                    self._children_yang_names.add("access-interface-summary")

                    self.interface_counts = IpSubscriber.Nodes.Node.Summary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self._children_name_map["interface_counts"] = "interface-counts"
                    self._children_yang_names.add("interface-counts")

                    self.vrf = YList(self)
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSubscriber.Nodes.Node.Summary, [], name, value)


                class AccessInterfaceSummary(Entity):
                    """
                    Access interface summary statistics
                    
                    .. attribute:: initiators
                    
                    	Summary counts per initiator
                    	**type**\:  :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators>`
                    
                    .. attribute:: ipv6_initiators
                    
                    	Summary counts per initiator for ipv6 session
                    	**type**\:  :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators>`
                    
                    .. attribute:: interfaces
                    
                    	Number of interfaces with subscriber configuration
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary, self).__init__()

                        self.yang_name = "access-interface-summary"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("initiators", ("initiators", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators)), ("ipv6-initiators", ("ipv6_initiators", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interfaces', YLeaf(YType.uint32, 'interfaces')),
                        ])
                        self.interfaces = None

                        self.initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators()
                        self.initiators.parent = self
                        self._children_name_map["initiators"] = "initiators"
                        self._children_yang_names.add("initiators")

                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                        self._children_yang_names.add("ipv6-initiators")
                        self._segment_path = lambda: "access-interface-summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary, ['interfaces'], name, value)


                    class Initiators(Entity):
                        """
                        Summary counts per initiator
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "access-interface-summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "initiators"


                        class Dhcp(Entity):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                ])
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp, ['fsol_packets', 'fsol_bytes'], name, value)


                        class PacketTrigger(Entity):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                ])
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger, ['fsol_packets', 'fsol_bytes'], name, value)


                    class Ipv6Initiators(Entity):
                        """
                        Summary counts per initiator for ipv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "access-interface-summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "ipv6-initiators"


                        class Dhcp(Entity):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                ])
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp, ['fsol_packets', 'fsol_bytes'], name, value)


                        class PacketTrigger(Entity):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                ])
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger, ['fsol_packets', 'fsol_bytes'], name, value)


                class InterfaceCounts(Entity):
                    """
                    Initiator interface counts
                    
                    .. attribute:: initiators
                    
                    	Initiators
                    	**type**\:  :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators>`
                    
                    .. attribute:: ipv6_initiators
                    
                    	IPv6 Initiators
                    	**type**\:  :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts, self).__init__()

                        self.yang_name = "interface-counts"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("initiators", ("initiators", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators)), ("ipv6-initiators", ("ipv6_initiators", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators()
                        self.initiators.parent = self
                        self._children_name_map["initiators"] = "initiators"
                        self._children_yang_names.add("initiators")

                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                        self._children_yang_names.add("ipv6-initiators")
                        self._segment_path = lambda: "interface-counts"


                    class Initiators(Entity):
                        """
                        Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "interface-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "initiators"


                        class Dhcp(Entity):
                            """
                            DHCP
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('invalid', YLeaf(YType.uint32, 'invalid')),
                                    ('initialized', YLeaf(YType.uint32, 'initialized')),
                                    ('session_creation_started', YLeaf(YType.uint32, 'session-creation-started')),
                                    ('control_policy_executing', YLeaf(YType.uint32, 'control-policy-executing')),
                                    ('control_policy_executed', YLeaf(YType.uint32, 'control-policy-executed')),
                                    ('session_features_applied', YLeaf(YType.uint32, 'session-features-applied')),
                                    ('vrf_configured', YLeaf(YType.uint32, 'vrf-configured')),
                                    ('adding_adjacency', YLeaf(YType.uint32, 'adding-adjacency')),
                                    ('adjacency_added', YLeaf(YType.uint32, 'adjacency-added')),
                                    ('up', YLeaf(YType.uint32, 'up')),
                                    ('down', YLeaf(YType.uint32, 'down')),
                                    ('disconnecting', YLeaf(YType.uint32, 'disconnecting')),
                                    ('disconnected', YLeaf(YType.uint32, 'disconnected')),
                                    ('error', YLeaf(YType.uint32, 'error')),
                                    ('total_interfaces', YLeaf(YType.uint32, 'total-interfaces')),
                                ])
                                self.invalid = None
                                self.initialized = None
                                self.session_creation_started = None
                                self.control_policy_executing = None
                                self.control_policy_executed = None
                                self.session_features_applied = None
                                self.vrf_configured = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.up = None
                                self.down = None
                                self.disconnecting = None
                                self.disconnected = None
                                self.error = None
                                self.total_interfaces = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp, ['invalid', 'initialized', 'session_creation_started', 'control_policy_executing', 'control_policy_executed', 'session_features_applied', 'vrf_configured', 'adding_adjacency', 'adjacency_added', 'up', 'down', 'disconnecting', 'disconnected', 'error', 'total_interfaces'], name, value)


                        class PacketTrigger(Entity):
                            """
                            Packet trigger
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('invalid', YLeaf(YType.uint32, 'invalid')),
                                    ('initialized', YLeaf(YType.uint32, 'initialized')),
                                    ('session_creation_started', YLeaf(YType.uint32, 'session-creation-started')),
                                    ('control_policy_executing', YLeaf(YType.uint32, 'control-policy-executing')),
                                    ('control_policy_executed', YLeaf(YType.uint32, 'control-policy-executed')),
                                    ('session_features_applied', YLeaf(YType.uint32, 'session-features-applied')),
                                    ('vrf_configured', YLeaf(YType.uint32, 'vrf-configured')),
                                    ('adding_adjacency', YLeaf(YType.uint32, 'adding-adjacency')),
                                    ('adjacency_added', YLeaf(YType.uint32, 'adjacency-added')),
                                    ('up', YLeaf(YType.uint32, 'up')),
                                    ('down', YLeaf(YType.uint32, 'down')),
                                    ('disconnecting', YLeaf(YType.uint32, 'disconnecting')),
                                    ('disconnected', YLeaf(YType.uint32, 'disconnected')),
                                    ('error', YLeaf(YType.uint32, 'error')),
                                    ('total_interfaces', YLeaf(YType.uint32, 'total-interfaces')),
                                ])
                                self.invalid = None
                                self.initialized = None
                                self.session_creation_started = None
                                self.control_policy_executing = None
                                self.control_policy_executed = None
                                self.session_features_applied = None
                                self.vrf_configured = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.up = None
                                self.down = None
                                self.disconnecting = None
                                self.disconnected = None
                                self.error = None
                                self.total_interfaces = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger, ['invalid', 'initialized', 'session_creation_started', 'control_policy_executing', 'control_policy_executed', 'session_features_applied', 'vrf_configured', 'adding_adjacency', 'adjacency_added', 'up', 'down', 'disconnecting', 'disconnected', 'error', 'total_interfaces'], name, value)


                    class Ipv6Initiators(Entity):
                        """
                        IPv6 Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "interface-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "ipv6-initiators"


                        class Dhcp(Entity):
                            """
                            DHCP
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('invalid', YLeaf(YType.uint32, 'invalid')),
                                    ('initialized', YLeaf(YType.uint32, 'initialized')),
                                    ('session_creation_started', YLeaf(YType.uint32, 'session-creation-started')),
                                    ('control_policy_executing', YLeaf(YType.uint32, 'control-policy-executing')),
                                    ('control_policy_executed', YLeaf(YType.uint32, 'control-policy-executed')),
                                    ('session_features_applied', YLeaf(YType.uint32, 'session-features-applied')),
                                    ('vrf_configured', YLeaf(YType.uint32, 'vrf-configured')),
                                    ('adding_adjacency', YLeaf(YType.uint32, 'adding-adjacency')),
                                    ('adjacency_added', YLeaf(YType.uint32, 'adjacency-added')),
                                    ('up', YLeaf(YType.uint32, 'up')),
                                    ('down', YLeaf(YType.uint32, 'down')),
                                    ('disconnecting', YLeaf(YType.uint32, 'disconnecting')),
                                    ('disconnected', YLeaf(YType.uint32, 'disconnected')),
                                    ('error', YLeaf(YType.uint32, 'error')),
                                    ('total_interfaces', YLeaf(YType.uint32, 'total-interfaces')),
                                ])
                                self.invalid = None
                                self.initialized = None
                                self.session_creation_started = None
                                self.control_policy_executing = None
                                self.control_policy_executed = None
                                self.session_features_applied = None
                                self.vrf_configured = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.up = None
                                self.down = None
                                self.disconnecting = None
                                self.disconnected = None
                                self.error = None
                                self.total_interfaces = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp, ['invalid', 'initialized', 'session_creation_started', 'control_policy_executing', 'control_policy_executed', 'session_features_applied', 'vrf_configured', 'adding_adjacency', 'adjacency_added', 'up', 'down', 'disconnecting', 'disconnected', 'error', 'total_interfaces'], name, value)


                        class PacketTrigger(Entity):
                            """
                            Packet trigger
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('invalid', YLeaf(YType.uint32, 'invalid')),
                                    ('initialized', YLeaf(YType.uint32, 'initialized')),
                                    ('session_creation_started', YLeaf(YType.uint32, 'session-creation-started')),
                                    ('control_policy_executing', YLeaf(YType.uint32, 'control-policy-executing')),
                                    ('control_policy_executed', YLeaf(YType.uint32, 'control-policy-executed')),
                                    ('session_features_applied', YLeaf(YType.uint32, 'session-features-applied')),
                                    ('vrf_configured', YLeaf(YType.uint32, 'vrf-configured')),
                                    ('adding_adjacency', YLeaf(YType.uint32, 'adding-adjacency')),
                                    ('adjacency_added', YLeaf(YType.uint32, 'adjacency-added')),
                                    ('up', YLeaf(YType.uint32, 'up')),
                                    ('down', YLeaf(YType.uint32, 'down')),
                                    ('disconnecting', YLeaf(YType.uint32, 'disconnecting')),
                                    ('disconnected', YLeaf(YType.uint32, 'disconnected')),
                                    ('error', YLeaf(YType.uint32, 'error')),
                                    ('total_interfaces', YLeaf(YType.uint32, 'total-interfaces')),
                                ])
                                self.invalid = None
                                self.initialized = None
                                self.session_creation_started = None
                                self.control_policy_executing = None
                                self.control_policy_executed = None
                                self.session_features_applied = None
                                self.vrf_configured = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.up = None
                                self.down = None
                                self.disconnecting = None
                                self.disconnected = None
                                self.error = None
                                self.total_interfaces = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger, ['invalid', 'initialized', 'session_creation_started', 'control_policy_executing', 'control_policy_executed', 'session_features_applied', 'vrf_configured', 'adding_adjacency', 'adjacency_added', 'up', 'down', 'disconnecting', 'disconnected', 'error', 'total_interfaces'], name, value)


                class Vrf(Entity):
                    """
                    Array of VRFs with IPSUB interfaces
                    
                    .. attribute:: vrf_name
                    
                    	IPv4 VRF
                    	**type**\: str
                    
                    .. attribute:: ipv6vrf_name
                    
                    	IPv6 VRF
                    	**type**\: str
                    
                    .. attribute:: interfaces
                    
                    	Number of IP subscriber interfaces in the VRF table
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_interfaces
                    
                    	Number of IPv6 subscriber interfaces in the VRF table
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('ipv6vrf_name', YLeaf(YType.str, 'ipv6vrf-name')),
                            ('interfaces', YLeaf(YType.uint64, 'interfaces')),
                            ('ipv6_interfaces', YLeaf(YType.uint64, 'ipv6-interfaces')),
                        ])
                        self.vrf_name = None
                        self.ipv6vrf_name = None
                        self.interfaces = None
                        self.ipv6_interfaces = None
                        self._segment_path = lambda: "vrf"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSubscriber.Nodes.Node.Summary.Vrf, ['vrf_name', 'ipv6vrf_name', 'interfaces', 'ipv6_interfaces'], name, value)


            class Interfaces(Entity):
                """
                IP subscriber interface table
                
                .. attribute:: interface
                
                	IP subscriber interface entry
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("interface", ("interface", IpSubscriber.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSubscriber.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    IP subscriber interface entry
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: vrf
                    
                    	IPv4 VRF details
                    	**type**\:  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf>`
                    
                    .. attribute:: ipv6vrf
                    
                    	IPv6 VRF details
                    	**type**\:  :py:class:`Ipv6Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf>`
                    
                    .. attribute:: access_interface
                    
                    	Access interface through which this subscriber is accessible
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: subscriber_ipv4_address
                    
                    	IPv4 Address of the subscriber
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: subscriber_ipv6_address
                    
                    	IPv6 Address of the subscriber
                    	**type**\: str
                    
                    .. attribute:: subscriber_mac_addres
                    
                    	MAC address of the subscriber
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: subscriber_label
                    
                    	Subscriber label for this subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in month day hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: age
                    
                    	Age in hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: initiator
                    
                    	Protocol trigger for creation of this subscriber session
                    	**type**\:  :py:class:`IpsubMaIntfInitiatorData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorData>`
                    
                    .. attribute:: state
                    
                    	State of the subscriber session
                    	**type**\:  :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: old_state
                    
                    	Previous state of the subscriber session
                    	**type**\:  :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: last_state_change_time
                    
                    	Interface's last state change time in month day hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: current_change_age
                    
                    	Current change age in hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: ipv6_initiator
                    
                    	Protocol trigger for creation of this subscriber's IPv6 session
                    	**type**\:  :py:class:`IpsubMaIntfInitiatorData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorData>`
                    
                    .. attribute:: ipv6_state
                    
                    	State of the subscriber's IPv6 session
                    	**type**\:  :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: ipv6_old_state
                    
                    	Previous state of the subscriber's IPv6 session
                    	**type**\:  :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: ipv6_last_state_change_time
                    
                    	Interface's IPV6 last state change time in month day hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: ipv6_current_change_age
                    
                    	IPV6 Current change age in hh\:mm\:ss format
                    	**type**\: str
                    
                    .. attribute:: is_l2_connected
                    
                    	True if L2 connected
                    	**type**\: bool
                    
                    .. attribute:: session_type
                    
                    	Session Type
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("vrf", ("vrf", IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf)), ("ipv6vrf", ("ipv6vrf", IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('access_interface', YLeaf(YType.str, 'access-interface')),
                            ('subscriber_ipv4_address', YLeaf(YType.str, 'subscriber-ipv4-address')),
                            ('subscriber_ipv6_address', YLeaf(YType.str, 'subscriber-ipv6-address')),
                            ('subscriber_mac_addres', YLeaf(YType.str, 'subscriber-mac-addres')),
                            ('subscriber_label', YLeaf(YType.uint32, 'subscriber-label')),
                            ('interface_creation_time', YLeaf(YType.str, 'interface-creation-time')),
                            ('age', YLeaf(YType.str, 'age')),
                            ('initiator', YLeaf(YType.enumeration, 'initiator')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('old_state', YLeaf(YType.enumeration, 'old-state')),
                            ('last_state_change_time', YLeaf(YType.str, 'last-state-change-time')),
                            ('current_change_age', YLeaf(YType.str, 'current-change-age')),
                            ('ipv6_initiator', YLeaf(YType.enumeration, 'ipv6-initiator')),
                            ('ipv6_state', YLeaf(YType.enumeration, 'ipv6-state')),
                            ('ipv6_old_state', YLeaf(YType.enumeration, 'ipv6-old-state')),
                            ('ipv6_last_state_change_time', YLeaf(YType.str, 'ipv6-last-state-change-time')),
                            ('ipv6_current_change_age', YLeaf(YType.str, 'ipv6-current-change-age')),
                            ('is_l2_connected', YLeaf(YType.boolean, 'is-l2-connected')),
                            ('session_type', YLeaf(YType.str, 'session-type')),
                        ])
                        self.interface_name = None
                        self.access_interface = None
                        self.subscriber_ipv4_address = None
                        self.subscriber_ipv6_address = None
                        self.subscriber_mac_addres = None
                        self.subscriber_label = None
                        self.interface_creation_time = None
                        self.age = None
                        self.initiator = None
                        self.state = None
                        self.old_state = None
                        self.last_state_change_time = None
                        self.current_change_age = None
                        self.ipv6_initiator = None
                        self.ipv6_state = None
                        self.ipv6_old_state = None
                        self.ipv6_last_state_change_time = None
                        self.ipv6_current_change_age = None
                        self.is_l2_connected = None
                        self.session_type = None

                        self.vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf()
                        self.vrf.parent = self
                        self._children_name_map["vrf"] = "vrf"
                        self._children_yang_names.add("vrf")

                        self.ipv6vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf()
                        self.ipv6vrf.parent = self
                        self._children_name_map["ipv6vrf"] = "ipv6vrf"
                        self._children_yang_names.add("ipv6vrf")
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSubscriber.Nodes.Node.Interfaces.Interface, ['interface_name', 'access_interface', 'subscriber_ipv4_address', 'subscriber_ipv6_address', 'subscriber_mac_addres', 'subscriber_label', 'interface_creation_time', 'age', 'initiator', 'state', 'old_state', 'last_state_change_time', 'current_change_age', 'ipv6_initiator', 'ipv6_state', 'ipv6_old_state', 'ipv6_last_state_change_time', 'ipv6_current_change_age', 'is_l2_connected', 'session_type'], name, value)


                    class Vrf(Entity):
                        """
                        IPv4 VRF details
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                ('table_name', YLeaf(YType.str, 'table-name')),
                            ])
                            self.vrf_name = None
                            self.table_name = None
                            self._segment_path = lambda: "vrf"

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf, ['vrf_name', 'table_name'], name, value)


                    class Ipv6Vrf(Entity):
                        """
                        IPv6 VRF details
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf, self).__init__()

                            self.yang_name = "ipv6vrf"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                ('table_name', YLeaf(YType.str, 'table-name')),
                            ])
                            self.vrf_name = None
                            self.table_name = None
                            self._segment_path = lambda: "ipv6vrf"

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf, ['vrf_name', 'table_name'], name, value)


            class AccessInterfaces(Entity):
                """
                IP subscriber access interface table
                
                .. attribute:: access_interface
                
                	IP subscriber access interface entry
                	**type**\: list of  		 :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.AccessInterfaces, self).__init__()

                    self.yang_name = "access-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("access-interface", ("access_interface", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface))])
                    self._leafs = OrderedDict()

                    self.access_interface = YList(self)
                    self._segment_path = lambda: "access-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces, [], name, value)


                class AccessInterface(Entity):
                    """
                    IP subscriber access interface entry
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface
                    	**type**\:  :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators>`
                    
                    .. attribute:: ipv6_initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface for IPv6 session
                    	**type**\:  :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators>`
                    
                    .. attribute:: session_limit
                    
                    	Configuration session limits for each session limit source and type
                    	**type**\:  :py:class:`SessionLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit>`
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in Month Date HH\:MM\:SS format
                    	**type**\: str
                    
                    .. attribute:: age
                    
                    	Age in HH\:MM\:SS format
                    	**type**\: str
                    
                    .. attribute:: interface_type
                    
                    	Interface Type
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	Operational state of this interface
                    	**type**\:  :py:class:`IpsubMaParentIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateData>`
                    
                    .. attribute:: ipv6_state
                    
                    	Operational ipv6 state of this interface
                    	**type**\:  :py:class:`IpsubMaParentIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateData>`
                    
                    .. attribute:: vlan_type
                    
                    	The VLAN type on the access interface
                    	**type**\:  :py:class:`IpsubMaParentIntfVlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfVlan>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface, self).__init__()

                        self.yang_name = "access-interface"
                        self.yang_parent_name = "access-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("initiators", ("initiators", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators)), ("ipv6-initiators", ("ipv6_initiators", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators)), ("session-limit", ("session_limit", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('interface_creation_time', YLeaf(YType.str, 'interface-creation-time')),
                            ('age', YLeaf(YType.str, 'age')),
                            ('interface_type', YLeaf(YType.str, 'interface-type')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('ipv6_state', YLeaf(YType.enumeration, 'ipv6-state')),
                            ('vlan_type', YLeaf(YType.enumeration, 'vlan-type')),
                        ])
                        self.interface_name = None
                        self.interface_creation_time = None
                        self.age = None
                        self.interface_type = None
                        self.state = None
                        self.ipv6_state = None
                        self.vlan_type = None

                        self.initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators()
                        self.initiators.parent = self
                        self._children_name_map["initiators"] = "initiators"
                        self._children_yang_names.add("initiators")

                        self.ipv6_initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                        self._children_yang_names.add("ipv6-initiators")

                        self.session_limit = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit()
                        self.session_limit.parent = self
                        self._children_name_map["session_limit"] = "session-limit"
                        self._children_yang_names.add("session-limit")
                        self._segment_path = lambda: "access-interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface, ['interface_name', 'interface_creation_time', 'age', 'interface_type', 'state', 'ipv6_state', 'vlan_type'], name, value)


                    class Initiators(Entity):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "access-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "initiators"


                        class Dhcp(Entity):
                            """
                            DHCP information
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\: bool
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\: bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                                    ('unique_ip_check', YLeaf(YType.boolean, 'unique-ip-check')),
                                    ('sessions', YLeaf(YType.uint32, 'sessions')),
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                    ('fsol_dropped_packets', YLeaf(YType.uint32, 'fsol-dropped-packets')),
                                    ('fsol_dropped_bytes', YLeaf(YType.uint32, 'fsol-dropped-bytes')),
                                    ('fsol_dropped_packets_flow', YLeaf(YType.uint32, 'fsol-dropped-packets-flow')),
                                    ('fsol_dropped_packets_session_limit', YLeaf(YType.uint32, 'fsol-dropped-packets-session-limit')),
                                    ('fsol_dropped_packets_dup_addr', YLeaf(YType.uint32, 'fsol-dropped-packets-dup-addr')),
                                ])
                                self.is_configured = None
                                self.unique_ip_check = None
                                self.sessions = None
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_dropped_packets_dup_addr = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp, ['is_configured', 'unique_ip_check', 'sessions', 'fsol_packets', 'fsol_bytes', 'fsol_dropped_packets', 'fsol_dropped_bytes', 'fsol_dropped_packets_flow', 'fsol_dropped_packets_session_limit', 'fsol_dropped_packets_dup_addr'], name, value)


                        class PacketTrigger(Entity):
                            """
                            packet trigger information
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\: bool
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\: bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                                    ('unique_ip_check', YLeaf(YType.boolean, 'unique-ip-check')),
                                    ('sessions', YLeaf(YType.uint32, 'sessions')),
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                    ('fsol_dropped_packets', YLeaf(YType.uint32, 'fsol-dropped-packets')),
                                    ('fsol_dropped_bytes', YLeaf(YType.uint32, 'fsol-dropped-bytes')),
                                    ('fsol_dropped_packets_flow', YLeaf(YType.uint32, 'fsol-dropped-packets-flow')),
                                    ('fsol_dropped_packets_session_limit', YLeaf(YType.uint32, 'fsol-dropped-packets-session-limit')),
                                    ('fsol_dropped_packets_dup_addr', YLeaf(YType.uint32, 'fsol-dropped-packets-dup-addr')),
                                ])
                                self.is_configured = None
                                self.unique_ip_check = None
                                self.sessions = None
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_dropped_packets_dup_addr = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger, ['is_configured', 'unique_ip_check', 'sessions', 'fsol_packets', 'fsol_bytes', 'fsol_dropped_packets', 'fsol_dropped_bytes', 'fsol_dropped_packets_flow', 'fsol_dropped_packets_session_limit', 'fsol_dropped_packets_dup_addr'], name, value)


                    class Ipv6Initiators(Entity):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface for IPv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:  :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "access-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("dhcp", ("dhcp", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp)), ("packet-trigger", ("packet_trigger", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")
                            self._segment_path = lambda: "ipv6-initiators"


                        class Dhcp(Entity):
                            """
                            DHCP information
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\: bool
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\: bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                                    ('unique_ip_check', YLeaf(YType.boolean, 'unique-ip-check')),
                                    ('sessions', YLeaf(YType.uint32, 'sessions')),
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                    ('fsol_dropped_packets', YLeaf(YType.uint32, 'fsol-dropped-packets')),
                                    ('fsol_dropped_bytes', YLeaf(YType.uint32, 'fsol-dropped-bytes')),
                                    ('fsol_dropped_packets_flow', YLeaf(YType.uint32, 'fsol-dropped-packets-flow')),
                                    ('fsol_dropped_packets_session_limit', YLeaf(YType.uint32, 'fsol-dropped-packets-session-limit')),
                                    ('fsol_dropped_packets_dup_addr', YLeaf(YType.uint32, 'fsol-dropped-packets-dup-addr')),
                                ])
                                self.is_configured = None
                                self.unique_ip_check = None
                                self.sessions = None
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_dropped_packets_dup_addr = None
                                self._segment_path = lambda: "dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp, ['is_configured', 'unique_ip_check', 'sessions', 'fsol_packets', 'fsol_bytes', 'fsol_dropped_packets', 'fsol_dropped_bytes', 'fsol_dropped_packets_flow', 'fsol_dropped_packets_session_limit', 'fsol_dropped_packets_dup_addr'], name, value)


                        class PacketTrigger(Entity):
                            """
                            packet trigger information
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\: bool
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\: bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                                    ('unique_ip_check', YLeaf(YType.boolean, 'unique-ip-check')),
                                    ('sessions', YLeaf(YType.uint32, 'sessions')),
                                    ('fsol_packets', YLeaf(YType.uint32, 'fsol-packets')),
                                    ('fsol_bytes', YLeaf(YType.uint32, 'fsol-bytes')),
                                    ('fsol_dropped_packets', YLeaf(YType.uint32, 'fsol-dropped-packets')),
                                    ('fsol_dropped_bytes', YLeaf(YType.uint32, 'fsol-dropped-bytes')),
                                    ('fsol_dropped_packets_flow', YLeaf(YType.uint32, 'fsol-dropped-packets-flow')),
                                    ('fsol_dropped_packets_session_limit', YLeaf(YType.uint32, 'fsol-dropped-packets-session-limit')),
                                    ('fsol_dropped_packets_dup_addr', YLeaf(YType.uint32, 'fsol-dropped-packets-dup-addr')),
                                ])
                                self.is_configured = None
                                self.unique_ip_check = None
                                self.sessions = None
                                self.fsol_packets = None
                                self.fsol_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_dropped_packets_dup_addr = None
                                self._segment_path = lambda: "packet-trigger"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger, ['is_configured', 'unique_ip_check', 'sessions', 'fsol_packets', 'fsol_bytes', 'fsol_dropped_packets', 'fsol_dropped_bytes', 'fsol_dropped_packets_flow', 'fsol_dropped_packets_session_limit', 'fsol_dropped_packets_dup_addr'], name, value)


                    class SessionLimit(Entity):
                        """
                        Configuration session limits for each session
                        limit source and type
                        
                        .. attribute:: unclassified_source
                        
                        	Unclassified source session limits
                        	**type**\:  :py:class:`UnclassifiedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource>`
                        
                        .. attribute:: total
                        
                        	All sources session limits
                        	**type**\:  :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit, self).__init__()

                            self.yang_name = "session-limit"
                            self.yang_parent_name = "access-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("unclassified-source", ("unclassified_source", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource)), ("total", ("total", IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.unclassified_source = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource()
                            self.unclassified_source.parent = self
                            self._children_name_map["unclassified_source"] = "unclassified-source"
                            self._children_yang_names.add("unclassified-source")

                            self.total = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total()
                            self.total.parent = self
                            self._children_name_map["total"] = "total"
                            self._children_yang_names.add("total")
                            self._segment_path = lambda: "session-limit"


                        class UnclassifiedSource(Entity):
                            """
                            Unclassified source session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource, self).__init__()

                                self.yang_name = "unclassified-source"
                                self.yang_parent_name = "session-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('per_vlan', YLeaf(YType.uint32, 'per-vlan')),
                                ])
                                self.per_vlan = None
                                self._segment_path = lambda: "unclassified-source"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource, ['per_vlan'], name, value)


                        class Total(Entity):
                            """
                            All sources session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total, self).__init__()

                                self.yang_name = "total"
                                self.yang_parent_name = "session-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('per_vlan', YLeaf(YType.uint32, 'per-vlan')),
                                ])
                                self.per_vlan = None
                                self._segment_path = lambda: "total"

                            def __setattr__(self, name, value):
                                self._perform_setattr(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total, ['per_vlan'], name, value)

    def clone_ptr(self):
        self._top_entity = IpSubscriber()
        return self._top_entity

