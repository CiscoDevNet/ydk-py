""" nvo 

This module contains a collection of YANG definitions
for Cisco VxLAN feature configuration.

Copyright (c) 2013\-2014 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
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
        self._child_container_classes = {}
        self._child_list_classes = {"nvo-instance" : ("nvo_instance", NvoInstances.NvoInstance)}

        self.nvo_instance = YList(self)
        self._segment_path = lambda: "nvo:nvo-instances"

    def __setattr__(self, name, value):
        self._perform_setattr(NvoInstances, [], name, value)


    class NvoInstance(Entity):
        """
        List of instances
        
        .. attribute:: nvo_id  <key>
        
        	Network Virtualization Overlay Instance  Identifier
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: overlay_encapsulation
        
        	Encapsulation type
        	**type**\:  :py:class:`OverlayEncapType <ydk.models.cisco_ios_xe.nvo.OverlayEncapType>`
        
        .. attribute:: virtual_network
        
        	VNI member attributes
        	**type**\: list of  		 :py:class:`VirtualNetwork <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork>`
        
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
            self._child_container_classes = {}
            self._child_list_classes = {"virtual-network" : ("virtual_network", NvoInstances.NvoInstance.VirtualNetwork)}

            self.nvo_id = YLeaf(YType.uint16, "nvo-id")

            self.overlay_encapsulation = YLeaf(YType.identityref, "overlay-encapsulation")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.virtual_network = YList(self)
            self._segment_path = lambda: "nvo-instance" + "[nvo-id='" + self.nvo_id.get() + "']"
            self._absolute_path = lambda: "nvo:nvo-instances/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NvoInstances.NvoInstance, ['nvo_id', 'overlay_encapsulation', 'source_interface'], name, value)


        class VirtualNetwork(Entity):
            """
            VNI member attributes
            
            .. attribute:: vni_start  <key>
            
            	Single Virtual Network Identifier  or start of range
            	**type**\: int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: vni_end  <key>
            
            	End of Virtual Network Identifier range  (make equal to vni\-start for single vni
            	**type**\: int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: end_host_discovery
            
            	How to peform endpoint discovery
            	**type**\:  :py:class:`EndHostDiscovery <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscovery>`
            
            	**default value**\: flood-and-learn
            
            .. attribute:: routing_instance
            
            	VRF Name
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
            
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
            
            

            """

            _prefix = 'nvo'
            _revision = '2015-06-02'

            def __init__(self):
                super(NvoInstances.NvoInstance.VirtualNetwork, self).__init__()

                self.yang_name = "virtual-network"
                self.yang_parent_name = "nvo-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"multicast" : ("multicast", NvoInstances.NvoInstance.VirtualNetwork.Multicast)}
                self._child_list_classes = {"peers" : ("peers", NvoInstances.NvoInstance.VirtualNetwork.Peers)}

                self.vni_start = YLeaf(YType.uint32, "vni-start")

                self.vni_end = YLeaf(YType.uint32, "vni-end")

                self.end_host_discovery = YLeaf(YType.enumeration, "end-host-discovery")

                self.routing_instance = YLeaf(YType.str, "routing-instance")

                self.suppress_arp = YLeaf(YType.empty, "suppress-arp")

                self.bgp = YLeaf(YType.empty, "bgp")

                self.multicast = NvoInstances.NvoInstance.VirtualNetwork.Multicast()
                self.multicast.parent = self
                self._children_name_map["multicast"] = "multicast"
                self._children_yang_names.add("multicast")

                self.peers = YList(self)
                self._segment_path = lambda: "virtual-network" + "[vni-start='" + self.vni_start.get() + "']" + "[vni-end='" + self.vni_end.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(NvoInstances.NvoInstance.VirtualNetwork, ['vni_start', 'vni_end', 'end_host_discovery', 'routing_instance', 'suppress_arp', 'bgp'], name, value)

            class EndHostDiscovery(Enum):
                """
                EndHostDiscovery

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
                
                .. attribute:: peer_ip  <key>
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.peer_ip = YLeaf(YType.str, "peer-ip")
                    self._segment_path = lambda: "peers" + "[peer-ip='" + self.peer_ip.get() + "']"

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.multicast_group_min = YLeaf(YType.str, "multicast-group-min")

                    self.multicast_group_max = YLeaf(YType.str, "multicast-group-max")
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


