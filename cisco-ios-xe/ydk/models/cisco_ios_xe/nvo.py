""" nvo 

This module contains a collection of YANG definitions
for Cisco VxLAN feature configuration.

Copyright (c) 2013\-2014 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OverlayEncapType(Identity):
    """
    Base identity from which identities describing different
    encapsulationtypes are derived.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(OverlayEncapType, self).__init__("urn:ietf:params:xml:ns:yang:nvo", "nvo", "nvo:overlay-encap-type")


class NvoInstances(Entity):
    """
    vxlan instances
    
    .. attribute:: nvo_instance
    
    	List of instances
    	**type**\: list of  		 :py:class:`NvoInstance <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance>`
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(NvoInstances, self).__init__()
        self._top_entity = None

        self.yang_name = "nvo-instances"
        self.yang_parent_name = "nvo"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("nvo-instance", ("nvo_instance", NvoInstances.NvoInstance))])
        self._leafs = OrderedDict()

        self.nvo_instance = YList(self)
        self._segment_path = lambda: "nvo:nvo-instances"

    def __setattr__(self, name, value):
        self._perform_setattr(NvoInstances, [], name, value)


    class NvoInstance(Entity):
        """
        List of instances
        
        .. attribute:: nvo_id  (key)
        
        	Network Virtualization Overlay Instance  Identifier
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: virtual_network
        
        	VNI member attributes
        	**type**\: list of  		 :py:class:`VirtualNetwork <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork>`
        
        .. attribute:: overlay_encapsulation
        
        	Encapsulation type
        	**type**\:  :py:class:`OverlayEncapType <ydk.models.cisco_ios_xe.nvo.OverlayEncapType>`
        
        .. attribute:: source_interface
        
        	Source interface name
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nvo'
        _revision = '2015-06-02'

        def __init__(self):
            super(NvoInstances.NvoInstance, self).__init__()

            self.yang_name = "nvo-instance"
            self.yang_parent_name = "nvo-instances"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['nvo_id']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("virtual-network", ("virtual_network", NvoInstances.NvoInstance.VirtualNetwork))])
            self._leafs = OrderedDict([
                ('nvo_id', YLeaf(YType.uint16, 'nvo-id')),
                ('overlay_encapsulation', YLeaf(YType.identityref, 'overlay-encapsulation')),
                ('source_interface', YLeaf(YType.str, 'source-interface')),
            ])
            self.nvo_id = None
            self.overlay_encapsulation = None
            self.source_interface = None

            self.virtual_network = YList(self)
            self._segment_path = lambda: "nvo-instance" + "[nvo-id='" + str(self.nvo_id) + "']"
            self._absolute_path = lambda: "nvo:nvo-instances/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvoInstances.NvoInstance, ['nvo_id', 'overlay_encapsulation', 'source_interface'], name, value)


        class VirtualNetwork(Entity):
            """
            VNI member attributes
            
            .. attribute:: vni_start  (key)
            
            	Single Virtual Network Identifier  or start of range
            	**type**\: int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: vni_end  (key)
            
            	End of Virtual Network Identifier range  (make equal to vni\-start for single vni
            	**type**\: int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: suppress_arp
            
            	Enable ARP request suppression for this VNI
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: peers
            
            	List of VTEP peers
            	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Peers>`
            
            .. attribute:: multicast
            
            	Mulitcast group range associated  with the VxLAN segment(s)
            	**type**\:  :py:class:`Multicast <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Multicast>`
            
            .. attribute:: bgp
            
            	Use control protocol BGP to discover  peers
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: end_host_discovery
            
            	How to peform endpoint discovery
            	**type**\:  :py:class:`EndHostDiscovery <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscovery>`
            
            	**default value**\: flood-and-learn
            
            .. attribute:: routing_instance
            
            	VRF Name
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
            
            

            """

            _prefix = 'nvo'
            _revision = '2015-06-02'

            def __init__(self):
                super(NvoInstances.NvoInstance.VirtualNetwork, self).__init__()

                self.yang_name = "virtual-network"
                self.yang_parent_name = "nvo-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['vni_start','vni_end']
                self._child_container_classes = OrderedDict([("multicast", ("multicast", NvoInstances.NvoInstance.VirtualNetwork.Multicast))])
                self._child_list_classes = OrderedDict([("peers", ("peers", NvoInstances.NvoInstance.VirtualNetwork.Peers))])
                self._leafs = OrderedDict([
                    ('vni_start', YLeaf(YType.uint32, 'vni-start')),
                    ('vni_end', YLeaf(YType.uint32, 'vni-end')),
                    ('suppress_arp', YLeaf(YType.empty, 'suppress-arp')),
                    ('bgp', YLeaf(YType.empty, 'bgp')),
                    ('end_host_discovery', YLeaf(YType.enumeration, 'end-host-discovery')),
                    ('routing_instance', YLeaf(YType.str, 'routing-instance')),
                ])
                self.vni_start = None
                self.vni_end = None
                self.suppress_arp = None
                self.bgp = None
                self.end_host_discovery = None
                self.routing_instance = None

                self.multicast = NvoInstances.NvoInstance.VirtualNetwork.Multicast()
                self.multicast.parent = self
                self._children_name_map["multicast"] = "multicast"
                self._children_yang_names.add("multicast")

                self.peers = YList(self)
                self._segment_path = lambda: "virtual-network" + "[vni-start='" + str(self.vni_start) + "']" + "[vni-end='" + str(self.vni_end) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(NvoInstances.NvoInstance.VirtualNetwork, ['vni_start', 'vni_end', 'suppress_arp', 'bgp', 'end_host_discovery', 'routing_instance'], name, value)

            class EndHostDiscovery(Enum):
                """
                EndHostDiscovery (Enum Class)

                How to peform endpoint discovery

                .. data:: flood_and_learn = 0

                	Discover end-hosts using data plane 

                	              flood and learn

                .. data:: bgp = 1

                	Discover end-hosts using bgp-evpn

                """

                flood_and_learn = Enum.YLeaf(0, "flood-and-learn")

                bgp = Enum.YLeaf(1, "bgp")



            class Peers(Entity):
                """
                List of VTEP peers
                
                .. attribute:: peer_ip  (key)
                
                	VTEP peer IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    super(NvoInstances.NvoInstance.VirtualNetwork.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "virtual-network"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['peer_ip']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_ip', YLeaf(YType.str, 'peer-ip')),
                    ])
                    self.peer_ip = None
                    self._segment_path = lambda: "peers" + "[peer-ip='" + str(self.peer_ip) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvoInstances.NvoInstance.VirtualNetwork.Peers, ['peer_ip'], name, value)


            class Multicast(Entity):
                """
                Mulitcast group range associated 
                with the VxLAN segment(s)
                
                .. attribute:: multicast_group_min
                
                	Single IPV4 Multicast group  address or start of range
                	**type**\: str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: multicast_group_max
                
                	End of IPV4 Multicast group  address (leave unspecified for single value
                	**type**\: str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    super(NvoInstances.NvoInstance.VirtualNetwork.Multicast, self).__init__()

                    self.yang_name = "multicast"
                    self.yang_parent_name = "virtual-network"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('multicast_group_min', YLeaf(YType.str, 'multicast-group-min')),
                        ('multicast_group_max', YLeaf(YType.str, 'multicast-group-max')),
                    ])
                    self.multicast_group_min = None
                    self.multicast_group_max = None
                    self._segment_path = lambda: "multicast"

                def __setattr__(self, name, value):
                    self._perform_setattr(NvoInstances.NvoInstance.VirtualNetwork.Multicast, ['multicast_group_min', 'multicast_group_max'], name, value)

    def clone_ptr(self):
        self._top_entity = NvoInstances()
        return self._top_entity

class VxlanType(Identity):
    """
    This identity represents vxlan encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(VxlanType, self).__init__("urn:ietf:params:xml:ns:yang:nvo", "nvo", "nvo:vxlan-type")


class NvgreType(Identity):
    """
    This identity represents nvgre encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(NvgreType, self).__init__("urn:ietf:params:xml:ns:yang:nvo", "nvo", "nvo:nvgre-type")


