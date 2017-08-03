""" nvo 

This module contains a collection of YANG definitions
for Cisco VxLAN feature configuration.

Copyright (c) 2013\-2014 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    	**type**\: list of    :py:class:`NvoInstance <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance>`
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(NvoInstances, self).__init__()
        self._top_entity = None

        self.yang_name = "nvo-instances"
        self.yang_parent_name = "nvo"

        self.nvo_instance = YList(self)

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in () and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(NvoInstances, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(NvoInstances, self).__setattr__(name, value)


    class NvoInstance(Entity):
        """
        List of instances
        
        .. attribute:: nvo_id  <key>
        
        	Network Virtualization Overlay Instance  Identifier
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: overlay_encapsulation
        
        	Encapsulation type
        	**type**\:   :py:class:`OverlayEncapType <ydk.models.cisco_ios_xe.nvo.OverlayEncapType>`
        
        .. attribute:: source_interface
        
        	Source interface name
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        	**mandatory**\: True
        
        .. attribute:: virtual_network
        
        	VNI member attributes
        	**type**\: list of    :py:class:`VirtualNetwork <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork>`
        
        

        """

        _prefix = 'nvo'
        _revision = '2015-06-02'

        def __init__(self):
            super(NvoInstances.NvoInstance, self).__init__()

            self.yang_name = "nvo-instance"
            self.yang_parent_name = "nvo-instances"

            self.nvo_id = YLeaf(YType.uint16, "nvo-id")

            self.overlay_encapsulation = YLeaf(YType.identityref, "overlay-encapsulation")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.virtual_network = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nvo_id",
                            "overlay_encapsulation",
                            "source_interface") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvoInstances.NvoInstance, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvoInstances.NvoInstance, self).__setattr__(name, value)


        class VirtualNetwork(Entity):
            """
            VNI member attributes
            
            .. attribute:: vni_start  <key>
            
            	Single Virtual Network Identifier  or start of range
            	**type**\:  int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: vni_end  <key>
            
            	End of Virtual Network Identifier range  (make equal to vni\-start for single vni
            	**type**\:  int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: bgp
            
            	Use control protocol BGP to discover  peers
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: end_host_discovery
            
            	How to peform endpoint discovery
            	**type**\:   :py:class:`EndHostDiscovery <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscovery>`
            
            	**default value**\: flood-and-learn
            
            .. attribute:: multicast
            
            	Mulitcast group range associated  with the VxLAN segment(s)
            	**type**\:   :py:class:`Multicast <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Multicast>`
            
            .. attribute:: peers
            
            	List of VTEP peers
            	**type**\: list of    :py:class:`Peers <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Peers>`
            
            .. attribute:: routing_instance
            
            	VRF Name
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
            
            .. attribute:: suppress_arp
            
            	Enable ARP request suppression for this VNI
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nvo'
            _revision = '2015-06-02'

            def __init__(self):
                super(NvoInstances.NvoInstance.VirtualNetwork, self).__init__()

                self.yang_name = "virtual-network"
                self.yang_parent_name = "nvo-instance"

                self.vni_start = YLeaf(YType.uint32, "vni-start")

                self.vni_end = YLeaf(YType.uint32, "vni-end")

                self.bgp = YLeaf(YType.empty, "bgp")

                self.end_host_discovery = YLeaf(YType.enumeration, "end-host-discovery")

                self.routing_instance = YLeaf(YType.str, "routing-instance")

                self.suppress_arp = YLeaf(YType.empty, "suppress-arp")

                self.multicast = NvoInstances.NvoInstance.VirtualNetwork.Multicast()
                self.multicast.parent = self
                self._children_name_map["multicast"] = "multicast"
                self._children_yang_names.add("multicast")

                self.peers = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vni_start",
                                "vni_end",
                                "bgp",
                                "end_host_discovery",
                                "routing_instance",
                                "suppress_arp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvoInstances.NvoInstance.VirtualNetwork, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvoInstances.NvoInstance.VirtualNetwork, self).__setattr__(name, value)

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
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    super(NvoInstances.NvoInstance.VirtualNetwork.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "virtual-network"

                    self.peer_ip = YLeaf(YType.str, "peer-ip")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("peer_ip") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvoInstances.NvoInstance.VirtualNetwork.Peers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvoInstances.NvoInstance.VirtualNetwork.Peers, self).__setattr__(name, value)

                def has_data(self):
                    return self.peer_ip.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.peer_ip.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peers" + "[peer-ip='" + self.peer_ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.peer_ip.is_set or self.peer_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_ip.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-ip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "peer-ip"):
                        self.peer_ip = value
                        self.peer_ip.value_namespace = name_space
                        self.peer_ip.value_namespace_prefix = name_space_prefix


            class Multicast(Entity):
                """
                Mulitcast group range associated 
                with the VxLAN segment(s)
                
                .. attribute:: multicast_group_max
                
                	End of IPV4 Multicast group  address (leave unspecified for single value
                	**type**\:  str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: multicast_group_min
                
                	Single IPV4 Multicast group  address or start of range
                	**type**\:  str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    super(NvoInstances.NvoInstance.VirtualNetwork.Multicast, self).__init__()

                    self.yang_name = "multicast"
                    self.yang_parent_name = "virtual-network"

                    self.multicast_group_max = YLeaf(YType.str, "multicast-group-max")

                    self.multicast_group_min = YLeaf(YType.str, "multicast-group-min")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("multicast_group_max",
                                    "multicast_group_min") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvoInstances.NvoInstance.VirtualNetwork.Multicast, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvoInstances.NvoInstance.VirtualNetwork.Multicast, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.multicast_group_max.is_set or
                        self.multicast_group_min.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.multicast_group_max.yfilter != YFilter.not_set or
                        self.multicast_group_min.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "multicast" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.multicast_group_max.is_set or self.multicast_group_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_group_max.get_name_leafdata())
                    if (self.multicast_group_min.is_set or self.multicast_group_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_group_min.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "multicast-group-max" or name == "multicast-group-min"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "multicast-group-max"):
                        self.multicast_group_max = value
                        self.multicast_group_max.value_namespace = name_space
                        self.multicast_group_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-group-min"):
                        self.multicast_group_min = value
                        self.multicast_group_min.value_namespace = name_space
                        self.multicast_group_min.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.peers:
                    if (c.has_data()):
                        return True
                return (
                    self.vni_start.is_set or
                    self.vni_end.is_set or
                    self.bgp.is_set or
                    self.end_host_discovery.is_set or
                    self.routing_instance.is_set or
                    self.suppress_arp.is_set or
                    (self.multicast is not None and self.multicast.has_data()))

            def has_operation(self):
                for c in self.peers:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.vni_start.yfilter != YFilter.not_set or
                    self.vni_end.yfilter != YFilter.not_set or
                    self.bgp.yfilter != YFilter.not_set or
                    self.end_host_discovery.yfilter != YFilter.not_set or
                    self.routing_instance.yfilter != YFilter.not_set or
                    self.suppress_arp.yfilter != YFilter.not_set or
                    (self.multicast is not None and self.multicast.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "virtual-network" + "[vni-start='" + self.vni_start.get() + "']" + "[vni-end='" + self.vni_end.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vni_start.is_set or self.vni_start.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni_start.get_name_leafdata())
                if (self.vni_end.is_set or self.vni_end.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni_end.get_name_leafdata())
                if (self.bgp.is_set or self.bgp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp.get_name_leafdata())
                if (self.end_host_discovery.is_set or self.end_host_discovery.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.end_host_discovery.get_name_leafdata())
                if (self.routing_instance.is_set or self.routing_instance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.routing_instance.get_name_leafdata())
                if (self.suppress_arp.is_set or self.suppress_arp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.suppress_arp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "multicast"):
                    if (self.multicast is None):
                        self.multicast = NvoInstances.NvoInstance.VirtualNetwork.Multicast()
                        self.multicast.parent = self
                        self._children_name_map["multicast"] = "multicast"
                    return self.multicast

                if (child_yang_name == "peers"):
                    for c in self.peers:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvoInstances.NvoInstance.VirtualNetwork.Peers()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.peers.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "multicast" or name == "peers" or name == "vni-start" or name == "vni-end" or name == "bgp" or name == "end-host-discovery" or name == "routing-instance" or name == "suppress-arp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vni-start"):
                    self.vni_start = value
                    self.vni_start.value_namespace = name_space
                    self.vni_start.value_namespace_prefix = name_space_prefix
                if(value_path == "vni-end"):
                    self.vni_end = value
                    self.vni_end.value_namespace = name_space
                    self.vni_end.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp"):
                    self.bgp = value
                    self.bgp.value_namespace = name_space
                    self.bgp.value_namespace_prefix = name_space_prefix
                if(value_path == "end-host-discovery"):
                    self.end_host_discovery = value
                    self.end_host_discovery.value_namespace = name_space
                    self.end_host_discovery.value_namespace_prefix = name_space_prefix
                if(value_path == "routing-instance"):
                    self.routing_instance = value
                    self.routing_instance.value_namespace = name_space
                    self.routing_instance.value_namespace_prefix = name_space_prefix
                if(value_path == "suppress-arp"):
                    self.suppress_arp = value
                    self.suppress_arp.value_namespace = name_space
                    self.suppress_arp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.virtual_network:
                if (c.has_data()):
                    return True
            return (
                self.nvo_id.is_set or
                self.overlay_encapsulation.is_set or
                self.source_interface.is_set)

        def has_operation(self):
            for c in self.virtual_network:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.nvo_id.yfilter != YFilter.not_set or
                self.overlay_encapsulation.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nvo-instance" + "[nvo-id='" + self.nvo_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "nvo:nvo-instances/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nvo_id.is_set or self.nvo_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nvo_id.get_name_leafdata())
            if (self.overlay_encapsulation.is_set or self.overlay_encapsulation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.overlay_encapsulation.get_name_leafdata())
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "virtual-network"):
                for c in self.virtual_network:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NvoInstances.NvoInstance.VirtualNetwork()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.virtual_network.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "virtual-network" or name == "nvo-id" or name == "overlay-encapsulation" or name == "source-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nvo-id"):
                self.nvo_id = value
                self.nvo_id.value_namespace = name_space
                self.nvo_id.value_namespace_prefix = name_space_prefix
            if(value_path == "overlay-encapsulation"):
                self.overlay_encapsulation = value
                self.overlay_encapsulation.value_namespace = name_space
                self.overlay_encapsulation.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.nvo_instance:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.nvo_instance:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "nvo:nvo-instances" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nvo-instance"):
            for c in self.nvo_instance:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = NvoInstances.NvoInstance()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.nvo_instance.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nvo-instance"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NvoInstances()
        return self._top_entity

class NvgreType(Identity):
    """
    This identity represents nvgre encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(NvgreType, self).__init__("urn:ietf:params:xml:ns:yang:nvo", "nvo", "nvo:nvgre-type")


class VxlanType(Identity):
    """
    This identity represents vxlan encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        super(VxlanType, self).__init__("urn:ietf:params:xml:ns:yang:nvo", "nvo", "nvo:vxlan-type")


