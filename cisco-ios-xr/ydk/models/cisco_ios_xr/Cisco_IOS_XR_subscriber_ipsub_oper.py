""" Cisco_IOS_XR_subscriber_ipsub_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-ipsub package operational data.

This module contains definitions
for the following management objects\:
  ip\-subscriber\: IP subscriber operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpsubMaIntfInitiatorData(Enum):
    """
    IpsubMaIntfInitiatorData

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
    IpsubMaIntfStateData

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
    IpsubMaParentIntfStateData

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
    IpsubMaParentIntfVlan

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes>`
    
    

    """

    _prefix = 'subscriber-ipsub-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(IpSubscriber, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-subscriber"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-ipsub-oper"

        self.nodes = IpSubscriber.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        IP subscriber operational data for a particular
        location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-ipsub-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpSubscriber.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ip-subscriber"

            self.node = YList(self)

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
                        super(IpSubscriber.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpSubscriber.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: node_name  <key>
            
            	The node ID to filter on. For eg., 0/1/CPU0
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: access_interfaces
            
            	IP subscriber access interface table
            	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces>`
            
            .. attribute:: interfaces
            
            	IP subscriber interface table
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces>`
            
            .. attribute:: summary
            
            	IP subscriber interface summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'subscriber-ipsub-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpSubscriber.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.access_interfaces = IpSubscriber.Nodes.Node.AccessInterfaces()
                self.access_interfaces.parent = self
                self._children_name_map["access_interfaces"] = "access-interfaces"
                self._children_yang_names.add("access-interfaces")

                self.interfaces = IpSubscriber.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.summary = IpSubscriber.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpSubscriber.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpSubscriber.Nodes.Node, self).__setattr__(name, value)


            class Summary(Entity):
                """
                IP subscriber interface summary
                
                .. attribute:: access_interface_summary
                
                	Access interface summary statistics
                	**type**\:   :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary>`
                
                .. attribute:: interface_counts
                
                	Initiator interface counts
                	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts>`
                
                .. attribute:: vrf
                
                	Array of VRFs with IPSUB interfaces
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.Vrf>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"

                    self.access_interface_summary = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary()
                    self.access_interface_summary.parent = self
                    self._children_name_map["access_interface_summary"] = "access-interface-summary"
                    self._children_yang_names.add("access-interface-summary")

                    self.interface_counts = IpSubscriber.Nodes.Node.Summary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self._children_name_map["interface_counts"] = "interface-counts"
                    self._children_yang_names.add("interface-counts")

                    self.vrf = YList(self)

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
                                super(IpSubscriber.Nodes.Node.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSubscriber.Nodes.Node.Summary, self).__setattr__(name, value)


                class AccessInterfaceSummary(Entity):
                    """
                    Access interface summary statistics
                    
                    .. attribute:: initiators
                    
                    	Summary counts per initiator
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators>`
                    
                    .. attribute:: interfaces
                    
                    	Number of interfaces with subscriber configuration
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6_initiators
                    
                    	Summary counts per initiator for ipv6 session
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary, self).__init__()

                        self.yang_name = "access-interface-summary"
                        self.yang_parent_name = "summary"

                        self.interfaces = YLeaf(YType.uint32, "interfaces")

                        self.initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators()
                        self.initiators.parent = self
                        self._children_name_map["initiators"] = "initiators"
                        self._children_yang_names.add("initiators")

                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                        self._children_yang_names.add("ipv6-initiators")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interfaces") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary, self).__setattr__(name, value)


                    class Initiators(Entity):
                        """
                        Summary counts per initiator
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "access-interface-summary"

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv6Initiators(Entity):
                        """
                        Summary counts per initiator for ipv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "access-interface-summary"

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interfaces.is_set or
                            (self.initiators is not None and self.initiators.has_data()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interfaces.yfilter != YFilter.not_set or
                            (self.initiators is not None and self.initiators.has_operation()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-interface-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interfaces.is_set or self.interfaces.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interfaces.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "initiators"):
                            if (self.initiators is None):
                                self.initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators()
                                self.initiators.parent = self
                                self._children_name_map["initiators"] = "initiators"
                            return self.initiators

                        if (child_yang_name == "ipv6-initiators"):
                            if (self.ipv6_initiators is None):
                                self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators()
                                self.ipv6_initiators.parent = self
                                self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                            return self.ipv6_initiators

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "initiators" or name == "ipv6-initiators" or name == "interfaces"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interfaces"):
                            self.interfaces = value
                            self.interfaces.value_namespace = name_space
                            self.interfaces.value_namespace_prefix = name_space_prefix


                class InterfaceCounts(Entity):
                    """
                    Initiator interface counts
                    
                    .. attribute:: initiators
                    
                    	Initiators
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators>`
                    
                    .. attribute:: ipv6_initiators
                    
                    	IPv6 Initiators
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts, self).__init__()

                        self.yang_name = "interface-counts"
                        self.yang_parent_name = "summary"

                        self.initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators()
                        self.initiators.parent = self
                        self._children_name_map["initiators"] = "initiators"
                        self._children_yang_names.add("initiators")

                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                        self._children_yang_names.add("ipv6-initiators")


                    class Initiators(Entity):
                        """
                        Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "interface-counts"

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"

                                self.adding_adjacency = YLeaf(YType.uint32, "adding-adjacency")

                                self.adjacency_added = YLeaf(YType.uint32, "adjacency-added")

                                self.control_policy_executed = YLeaf(YType.uint32, "control-policy-executed")

                                self.control_policy_executing = YLeaf(YType.uint32, "control-policy-executing")

                                self.disconnected = YLeaf(YType.uint32, "disconnected")

                                self.disconnecting = YLeaf(YType.uint32, "disconnecting")

                                self.down = YLeaf(YType.uint32, "down")

                                self.error = YLeaf(YType.uint32, "error")

                                self.initialized = YLeaf(YType.uint32, "initialized")

                                self.invalid = YLeaf(YType.uint32, "invalid")

                                self.session_creation_started = YLeaf(YType.uint32, "session-creation-started")

                                self.session_features_applied = YLeaf(YType.uint32, "session-features-applied")

                                self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                                self.up = YLeaf(YType.uint32, "up")

                                self.vrf_configured = YLeaf(YType.uint32, "vrf-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("adding_adjacency",
                                                "adjacency_added",
                                                "control_policy_executed",
                                                "control_policy_executing",
                                                "disconnected",
                                                "disconnecting",
                                                "down",
                                                "error",
                                                "initialized",
                                                "invalid",
                                                "session_creation_started",
                                                "session_features_applied",
                                                "total_interfaces",
                                                "up",
                                                "vrf_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.adding_adjacency.is_set or
                                    self.adjacency_added.is_set or
                                    self.control_policy_executed.is_set or
                                    self.control_policy_executing.is_set or
                                    self.disconnected.is_set or
                                    self.disconnecting.is_set or
                                    self.down.is_set or
                                    self.error.is_set or
                                    self.initialized.is_set or
                                    self.invalid.is_set or
                                    self.session_creation_started.is_set or
                                    self.session_features_applied.is_set or
                                    self.total_interfaces.is_set or
                                    self.up.is_set or
                                    self.vrf_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.adding_adjacency.yfilter != YFilter.not_set or
                                    self.adjacency_added.yfilter != YFilter.not_set or
                                    self.control_policy_executed.yfilter != YFilter.not_set or
                                    self.control_policy_executing.yfilter != YFilter.not_set or
                                    self.disconnected.yfilter != YFilter.not_set or
                                    self.disconnecting.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.error.yfilter != YFilter.not_set or
                                    self.initialized.yfilter != YFilter.not_set or
                                    self.invalid.yfilter != YFilter.not_set or
                                    self.session_creation_started.yfilter != YFilter.not_set or
                                    self.session_features_applied.yfilter != YFilter.not_set or
                                    self.total_interfaces.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.vrf_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.adding_adjacency.is_set or self.adding_adjacency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adding_adjacency.get_name_leafdata())
                                if (self.adjacency_added.is_set or self.adjacency_added.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adjacency_added.get_name_leafdata())
                                if (self.control_policy_executed.is_set or self.control_policy_executed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executed.get_name_leafdata())
                                if (self.control_policy_executing.is_set or self.control_policy_executing.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executing.get_name_leafdata())
                                if (self.disconnected.is_set or self.disconnected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnected.get_name_leafdata())
                                if (self.disconnecting.is_set or self.disconnecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnecting.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.error.get_name_leafdata())
                                if (self.initialized.is_set or self.initialized.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.initialized.get_name_leafdata())
                                if (self.invalid.is_set or self.invalid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid.get_name_leafdata())
                                if (self.session_creation_started.is_set or self.session_creation_started.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_creation_started.get_name_leafdata())
                                if (self.session_features_applied.is_set or self.session_features_applied.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_features_applied.get_name_leafdata())
                                if (self.total_interfaces.is_set or self.total_interfaces.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_interfaces.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.vrf_configured.is_set or self.vrf_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "adding-adjacency" or name == "adjacency-added" or name == "control-policy-executed" or name == "control-policy-executing" or name == "disconnected" or name == "disconnecting" or name == "down" or name == "error" or name == "initialized" or name == "invalid" or name == "session-creation-started" or name == "session-features-applied" or name == "total-interfaces" or name == "up" or name == "vrf-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "adding-adjacency"):
                                    self.adding_adjacency = value
                                    self.adding_adjacency.value_namespace = name_space
                                    self.adding_adjacency.value_namespace_prefix = name_space_prefix
                                if(value_path == "adjacency-added"):
                                    self.adjacency_added = value
                                    self.adjacency_added.value_namespace = name_space
                                    self.adjacency_added.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executed"):
                                    self.control_policy_executed = value
                                    self.control_policy_executed.value_namespace = name_space
                                    self.control_policy_executed.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executing"):
                                    self.control_policy_executing = value
                                    self.control_policy_executing.value_namespace = name_space
                                    self.control_policy_executing.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnected"):
                                    self.disconnected = value
                                    self.disconnected.value_namespace = name_space
                                    self.disconnected.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnecting"):
                                    self.disconnecting = value
                                    self.disconnecting.value_namespace = name_space
                                    self.disconnecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "error"):
                                    self.error = value
                                    self.error.value_namespace = name_space
                                    self.error.value_namespace_prefix = name_space_prefix
                                if(value_path == "initialized"):
                                    self.initialized = value
                                    self.initialized.value_namespace = name_space
                                    self.initialized.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid"):
                                    self.invalid = value
                                    self.invalid.value_namespace = name_space
                                    self.invalid.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-creation-started"):
                                    self.session_creation_started = value
                                    self.session_creation_started.value_namespace = name_space
                                    self.session_creation_started.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-features-applied"):
                                    self.session_features_applied = value
                                    self.session_features_applied.value_namespace = name_space
                                    self.session_features_applied.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-interfaces"):
                                    self.total_interfaces = value
                                    self.total_interfaces.value_namespace = name_space
                                    self.total_interfaces.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-configured"):
                                    self.vrf_configured = value
                                    self.vrf_configured.value_namespace = name_space
                                    self.vrf_configured.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            Packet trigger
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"

                                self.adding_adjacency = YLeaf(YType.uint32, "adding-adjacency")

                                self.adjacency_added = YLeaf(YType.uint32, "adjacency-added")

                                self.control_policy_executed = YLeaf(YType.uint32, "control-policy-executed")

                                self.control_policy_executing = YLeaf(YType.uint32, "control-policy-executing")

                                self.disconnected = YLeaf(YType.uint32, "disconnected")

                                self.disconnecting = YLeaf(YType.uint32, "disconnecting")

                                self.down = YLeaf(YType.uint32, "down")

                                self.error = YLeaf(YType.uint32, "error")

                                self.initialized = YLeaf(YType.uint32, "initialized")

                                self.invalid = YLeaf(YType.uint32, "invalid")

                                self.session_creation_started = YLeaf(YType.uint32, "session-creation-started")

                                self.session_features_applied = YLeaf(YType.uint32, "session-features-applied")

                                self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                                self.up = YLeaf(YType.uint32, "up")

                                self.vrf_configured = YLeaf(YType.uint32, "vrf-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("adding_adjacency",
                                                "adjacency_added",
                                                "control_policy_executed",
                                                "control_policy_executing",
                                                "disconnected",
                                                "disconnecting",
                                                "down",
                                                "error",
                                                "initialized",
                                                "invalid",
                                                "session_creation_started",
                                                "session_features_applied",
                                                "total_interfaces",
                                                "up",
                                                "vrf_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.adding_adjacency.is_set or
                                    self.adjacency_added.is_set or
                                    self.control_policy_executed.is_set or
                                    self.control_policy_executing.is_set or
                                    self.disconnected.is_set or
                                    self.disconnecting.is_set or
                                    self.down.is_set or
                                    self.error.is_set or
                                    self.initialized.is_set or
                                    self.invalid.is_set or
                                    self.session_creation_started.is_set or
                                    self.session_features_applied.is_set or
                                    self.total_interfaces.is_set or
                                    self.up.is_set or
                                    self.vrf_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.adding_adjacency.yfilter != YFilter.not_set or
                                    self.adjacency_added.yfilter != YFilter.not_set or
                                    self.control_policy_executed.yfilter != YFilter.not_set or
                                    self.control_policy_executing.yfilter != YFilter.not_set or
                                    self.disconnected.yfilter != YFilter.not_set or
                                    self.disconnecting.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.error.yfilter != YFilter.not_set or
                                    self.initialized.yfilter != YFilter.not_set or
                                    self.invalid.yfilter != YFilter.not_set or
                                    self.session_creation_started.yfilter != YFilter.not_set or
                                    self.session_features_applied.yfilter != YFilter.not_set or
                                    self.total_interfaces.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.vrf_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.adding_adjacency.is_set or self.adding_adjacency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adding_adjacency.get_name_leafdata())
                                if (self.adjacency_added.is_set or self.adjacency_added.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adjacency_added.get_name_leafdata())
                                if (self.control_policy_executed.is_set or self.control_policy_executed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executed.get_name_leafdata())
                                if (self.control_policy_executing.is_set or self.control_policy_executing.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executing.get_name_leafdata())
                                if (self.disconnected.is_set or self.disconnected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnected.get_name_leafdata())
                                if (self.disconnecting.is_set or self.disconnecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnecting.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.error.get_name_leafdata())
                                if (self.initialized.is_set or self.initialized.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.initialized.get_name_leafdata())
                                if (self.invalid.is_set or self.invalid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid.get_name_leafdata())
                                if (self.session_creation_started.is_set or self.session_creation_started.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_creation_started.get_name_leafdata())
                                if (self.session_features_applied.is_set or self.session_features_applied.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_features_applied.get_name_leafdata())
                                if (self.total_interfaces.is_set or self.total_interfaces.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_interfaces.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.vrf_configured.is_set or self.vrf_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "adding-adjacency" or name == "adjacency-added" or name == "control-policy-executed" or name == "control-policy-executing" or name == "disconnected" or name == "disconnecting" or name == "down" or name == "error" or name == "initialized" or name == "invalid" or name == "session-creation-started" or name == "session-features-applied" or name == "total-interfaces" or name == "up" or name == "vrf-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "adding-adjacency"):
                                    self.adding_adjacency = value
                                    self.adding_adjacency.value_namespace = name_space
                                    self.adding_adjacency.value_namespace_prefix = name_space_prefix
                                if(value_path == "adjacency-added"):
                                    self.adjacency_added = value
                                    self.adjacency_added.value_namespace = name_space
                                    self.adjacency_added.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executed"):
                                    self.control_policy_executed = value
                                    self.control_policy_executed.value_namespace = name_space
                                    self.control_policy_executed.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executing"):
                                    self.control_policy_executing = value
                                    self.control_policy_executing.value_namespace = name_space
                                    self.control_policy_executing.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnected"):
                                    self.disconnected = value
                                    self.disconnected.value_namespace = name_space
                                    self.disconnected.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnecting"):
                                    self.disconnecting = value
                                    self.disconnecting.value_namespace = name_space
                                    self.disconnecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "error"):
                                    self.error = value
                                    self.error.value_namespace = name_space
                                    self.error.value_namespace_prefix = name_space_prefix
                                if(value_path == "initialized"):
                                    self.initialized = value
                                    self.initialized.value_namespace = name_space
                                    self.initialized.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid"):
                                    self.invalid = value
                                    self.invalid.value_namespace = name_space
                                    self.invalid.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-creation-started"):
                                    self.session_creation_started = value
                                    self.session_creation_started.value_namespace = name_space
                                    self.session_creation_started.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-features-applied"):
                                    self.session_features_applied = value
                                    self.session_features_applied.value_namespace = name_space
                                    self.session_features_applied.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-interfaces"):
                                    self.total_interfaces = value
                                    self.total_interfaces.value_namespace = name_space
                                    self.total_interfaces.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-configured"):
                                    self.vrf_configured = value
                                    self.vrf_configured.value_namespace = name_space
                                    self.vrf_configured.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv6Initiators(Entity):
                        """
                        IPv6 Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "interface-counts"

                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"

                                self.adding_adjacency = YLeaf(YType.uint32, "adding-adjacency")

                                self.adjacency_added = YLeaf(YType.uint32, "adjacency-added")

                                self.control_policy_executed = YLeaf(YType.uint32, "control-policy-executed")

                                self.control_policy_executing = YLeaf(YType.uint32, "control-policy-executing")

                                self.disconnected = YLeaf(YType.uint32, "disconnected")

                                self.disconnecting = YLeaf(YType.uint32, "disconnecting")

                                self.down = YLeaf(YType.uint32, "down")

                                self.error = YLeaf(YType.uint32, "error")

                                self.initialized = YLeaf(YType.uint32, "initialized")

                                self.invalid = YLeaf(YType.uint32, "invalid")

                                self.session_creation_started = YLeaf(YType.uint32, "session-creation-started")

                                self.session_features_applied = YLeaf(YType.uint32, "session-features-applied")

                                self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                                self.up = YLeaf(YType.uint32, "up")

                                self.vrf_configured = YLeaf(YType.uint32, "vrf-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("adding_adjacency",
                                                "adjacency_added",
                                                "control_policy_executed",
                                                "control_policy_executing",
                                                "disconnected",
                                                "disconnecting",
                                                "down",
                                                "error",
                                                "initialized",
                                                "invalid",
                                                "session_creation_started",
                                                "session_features_applied",
                                                "total_interfaces",
                                                "up",
                                                "vrf_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.adding_adjacency.is_set or
                                    self.adjacency_added.is_set or
                                    self.control_policy_executed.is_set or
                                    self.control_policy_executing.is_set or
                                    self.disconnected.is_set or
                                    self.disconnecting.is_set or
                                    self.down.is_set or
                                    self.error.is_set or
                                    self.initialized.is_set or
                                    self.invalid.is_set or
                                    self.session_creation_started.is_set or
                                    self.session_features_applied.is_set or
                                    self.total_interfaces.is_set or
                                    self.up.is_set or
                                    self.vrf_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.adding_adjacency.yfilter != YFilter.not_set or
                                    self.adjacency_added.yfilter != YFilter.not_set or
                                    self.control_policy_executed.yfilter != YFilter.not_set or
                                    self.control_policy_executing.yfilter != YFilter.not_set or
                                    self.disconnected.yfilter != YFilter.not_set or
                                    self.disconnecting.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.error.yfilter != YFilter.not_set or
                                    self.initialized.yfilter != YFilter.not_set or
                                    self.invalid.yfilter != YFilter.not_set or
                                    self.session_creation_started.yfilter != YFilter.not_set or
                                    self.session_features_applied.yfilter != YFilter.not_set or
                                    self.total_interfaces.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.vrf_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.adding_adjacency.is_set or self.adding_adjacency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adding_adjacency.get_name_leafdata())
                                if (self.adjacency_added.is_set or self.adjacency_added.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adjacency_added.get_name_leafdata())
                                if (self.control_policy_executed.is_set or self.control_policy_executed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executed.get_name_leafdata())
                                if (self.control_policy_executing.is_set or self.control_policy_executing.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executing.get_name_leafdata())
                                if (self.disconnected.is_set or self.disconnected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnected.get_name_leafdata())
                                if (self.disconnecting.is_set or self.disconnecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnecting.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.error.get_name_leafdata())
                                if (self.initialized.is_set or self.initialized.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.initialized.get_name_leafdata())
                                if (self.invalid.is_set or self.invalid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid.get_name_leafdata())
                                if (self.session_creation_started.is_set or self.session_creation_started.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_creation_started.get_name_leafdata())
                                if (self.session_features_applied.is_set or self.session_features_applied.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_features_applied.get_name_leafdata())
                                if (self.total_interfaces.is_set or self.total_interfaces.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_interfaces.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.vrf_configured.is_set or self.vrf_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "adding-adjacency" or name == "adjacency-added" or name == "control-policy-executed" or name == "control-policy-executing" or name == "disconnected" or name == "disconnecting" or name == "down" or name == "error" or name == "initialized" or name == "invalid" or name == "session-creation-started" or name == "session-features-applied" or name == "total-interfaces" or name == "up" or name == "vrf-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "adding-adjacency"):
                                    self.adding_adjacency = value
                                    self.adding_adjacency.value_namespace = name_space
                                    self.adding_adjacency.value_namespace_prefix = name_space_prefix
                                if(value_path == "adjacency-added"):
                                    self.adjacency_added = value
                                    self.adjacency_added.value_namespace = name_space
                                    self.adjacency_added.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executed"):
                                    self.control_policy_executed = value
                                    self.control_policy_executed.value_namespace = name_space
                                    self.control_policy_executed.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executing"):
                                    self.control_policy_executing = value
                                    self.control_policy_executing.value_namespace = name_space
                                    self.control_policy_executing.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnected"):
                                    self.disconnected = value
                                    self.disconnected.value_namespace = name_space
                                    self.disconnected.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnecting"):
                                    self.disconnecting = value
                                    self.disconnecting.value_namespace = name_space
                                    self.disconnecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "error"):
                                    self.error = value
                                    self.error.value_namespace = name_space
                                    self.error.value_namespace_prefix = name_space_prefix
                                if(value_path == "initialized"):
                                    self.initialized = value
                                    self.initialized.value_namespace = name_space
                                    self.initialized.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid"):
                                    self.invalid = value
                                    self.invalid.value_namespace = name_space
                                    self.invalid.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-creation-started"):
                                    self.session_creation_started = value
                                    self.session_creation_started.value_namespace = name_space
                                    self.session_creation_started.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-features-applied"):
                                    self.session_features_applied = value
                                    self.session_features_applied.value_namespace = name_space
                                    self.session_features_applied.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-interfaces"):
                                    self.total_interfaces = value
                                    self.total_interfaces.value_namespace = name_space
                                    self.total_interfaces.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-configured"):
                                    self.vrf_configured = value
                                    self.vrf_configured.value_namespace = name_space
                                    self.vrf_configured.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            Packet trigger
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"

                                self.adding_adjacency = YLeaf(YType.uint32, "adding-adjacency")

                                self.adjacency_added = YLeaf(YType.uint32, "adjacency-added")

                                self.control_policy_executed = YLeaf(YType.uint32, "control-policy-executed")

                                self.control_policy_executing = YLeaf(YType.uint32, "control-policy-executing")

                                self.disconnected = YLeaf(YType.uint32, "disconnected")

                                self.disconnecting = YLeaf(YType.uint32, "disconnecting")

                                self.down = YLeaf(YType.uint32, "down")

                                self.error = YLeaf(YType.uint32, "error")

                                self.initialized = YLeaf(YType.uint32, "initialized")

                                self.invalid = YLeaf(YType.uint32, "invalid")

                                self.session_creation_started = YLeaf(YType.uint32, "session-creation-started")

                                self.session_features_applied = YLeaf(YType.uint32, "session-features-applied")

                                self.total_interfaces = YLeaf(YType.uint32, "total-interfaces")

                                self.up = YLeaf(YType.uint32, "up")

                                self.vrf_configured = YLeaf(YType.uint32, "vrf-configured")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("adding_adjacency",
                                                "adjacency_added",
                                                "control_policy_executed",
                                                "control_policy_executing",
                                                "disconnected",
                                                "disconnecting",
                                                "down",
                                                "error",
                                                "initialized",
                                                "invalid",
                                                "session_creation_started",
                                                "session_features_applied",
                                                "total_interfaces",
                                                "up",
                                                "vrf_configured") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.adding_adjacency.is_set or
                                    self.adjacency_added.is_set or
                                    self.control_policy_executed.is_set or
                                    self.control_policy_executing.is_set or
                                    self.disconnected.is_set or
                                    self.disconnecting.is_set or
                                    self.down.is_set or
                                    self.error.is_set or
                                    self.initialized.is_set or
                                    self.invalid.is_set or
                                    self.session_creation_started.is_set or
                                    self.session_features_applied.is_set or
                                    self.total_interfaces.is_set or
                                    self.up.is_set or
                                    self.vrf_configured.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.adding_adjacency.yfilter != YFilter.not_set or
                                    self.adjacency_added.yfilter != YFilter.not_set or
                                    self.control_policy_executed.yfilter != YFilter.not_set or
                                    self.control_policy_executing.yfilter != YFilter.not_set or
                                    self.disconnected.yfilter != YFilter.not_set or
                                    self.disconnecting.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.error.yfilter != YFilter.not_set or
                                    self.initialized.yfilter != YFilter.not_set or
                                    self.invalid.yfilter != YFilter.not_set or
                                    self.session_creation_started.yfilter != YFilter.not_set or
                                    self.session_features_applied.yfilter != YFilter.not_set or
                                    self.total_interfaces.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.vrf_configured.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.adding_adjacency.is_set or self.adding_adjacency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adding_adjacency.get_name_leafdata())
                                if (self.adjacency_added.is_set or self.adjacency_added.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.adjacency_added.get_name_leafdata())
                                if (self.control_policy_executed.is_set or self.control_policy_executed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executed.get_name_leafdata())
                                if (self.control_policy_executing.is_set or self.control_policy_executing.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.control_policy_executing.get_name_leafdata())
                                if (self.disconnected.is_set or self.disconnected.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnected.get_name_leafdata())
                                if (self.disconnecting.is_set or self.disconnecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disconnecting.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.error.get_name_leafdata())
                                if (self.initialized.is_set or self.initialized.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.initialized.get_name_leafdata())
                                if (self.invalid.is_set or self.invalid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid.get_name_leafdata())
                                if (self.session_creation_started.is_set or self.session_creation_started.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_creation_started.get_name_leafdata())
                                if (self.session_features_applied.is_set or self.session_features_applied.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_features_applied.get_name_leafdata())
                                if (self.total_interfaces.is_set or self.total_interfaces.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_interfaces.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.vrf_configured.is_set or self.vrf_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_configured.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "adding-adjacency" or name == "adjacency-added" or name == "control-policy-executed" or name == "control-policy-executing" or name == "disconnected" or name == "disconnecting" or name == "down" or name == "error" or name == "initialized" or name == "invalid" or name == "session-creation-started" or name == "session-features-applied" or name == "total-interfaces" or name == "up" or name == "vrf-configured"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "adding-adjacency"):
                                    self.adding_adjacency = value
                                    self.adding_adjacency.value_namespace = name_space
                                    self.adding_adjacency.value_namespace_prefix = name_space_prefix
                                if(value_path == "adjacency-added"):
                                    self.adjacency_added = value
                                    self.adjacency_added.value_namespace = name_space
                                    self.adjacency_added.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executed"):
                                    self.control_policy_executed = value
                                    self.control_policy_executed.value_namespace = name_space
                                    self.control_policy_executed.value_namespace_prefix = name_space_prefix
                                if(value_path == "control-policy-executing"):
                                    self.control_policy_executing = value
                                    self.control_policy_executing.value_namespace = name_space
                                    self.control_policy_executing.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnected"):
                                    self.disconnected = value
                                    self.disconnected.value_namespace = name_space
                                    self.disconnected.value_namespace_prefix = name_space_prefix
                                if(value_path == "disconnecting"):
                                    self.disconnecting = value
                                    self.disconnecting.value_namespace = name_space
                                    self.disconnecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "error"):
                                    self.error = value
                                    self.error.value_namespace = name_space
                                    self.error.value_namespace_prefix = name_space_prefix
                                if(value_path == "initialized"):
                                    self.initialized = value
                                    self.initialized.value_namespace = name_space
                                    self.initialized.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid"):
                                    self.invalid = value
                                    self.invalid.value_namespace = name_space
                                    self.invalid.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-creation-started"):
                                    self.session_creation_started = value
                                    self.session_creation_started.value_namespace = name_space
                                    self.session_creation_started.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-features-applied"):
                                    self.session_features_applied = value
                                    self.session_features_applied.value_namespace = name_space
                                    self.session_features_applied.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-interfaces"):
                                    self.total_interfaces = value
                                    self.total_interfaces.value_namespace = name_space
                                    self.total_interfaces.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-configured"):
                                    self.vrf_configured = value
                                    self.vrf_configured.value_namespace = name_space
                                    self.vrf_configured.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.initiators is not None and self.initiators.has_data()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.initiators is not None and self.initiators.has_operation()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-counts" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "initiators"):
                            if (self.initiators is None):
                                self.initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators()
                                self.initiators.parent = self
                                self._children_name_map["initiators"] = "initiators"
                            return self.initiators

                        if (child_yang_name == "ipv6-initiators"):
                            if (self.ipv6_initiators is None):
                                self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators()
                                self.ipv6_initiators.parent = self
                                self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                            return self.ipv6_initiators

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "initiators" or name == "ipv6-initiators"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Vrf(Entity):
                    """
                    Array of VRFs with IPSUB interfaces
                    
                    .. attribute:: interfaces
                    
                    	Number of IP subscriber interfaces in the VRF table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_interfaces
                    
                    	Number of IPv6 subscriber interfaces in the VRF table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6vrf_name
                    
                    	IPv6 VRF
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	IPv4 VRF
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Summary.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "summary"

                        self.interfaces = YLeaf(YType.uint64, "interfaces")

                        self.ipv6_interfaces = YLeaf(YType.uint64, "ipv6-interfaces")

                        self.ipv6vrf_name = YLeaf(YType.str, "ipv6vrf-name")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interfaces",
                                        "ipv6_interfaces",
                                        "ipv6vrf_name",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSubscriber.Nodes.Node.Summary.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSubscriber.Nodes.Node.Summary.Vrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interfaces.is_set or
                            self.ipv6_interfaces.is_set or
                            self.ipv6vrf_name.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interfaces.yfilter != YFilter.not_set or
                            self.ipv6_interfaces.yfilter != YFilter.not_set or
                            self.ipv6vrf_name.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interfaces.is_set or self.interfaces.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interfaces.get_name_leafdata())
                        if (self.ipv6_interfaces.is_set or self.ipv6_interfaces.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_interfaces.get_name_leafdata())
                        if (self.ipv6vrf_name.is_set or self.ipv6vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6vrf_name.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interfaces" or name == "ipv6-interfaces" or name == "ipv6vrf-name" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interfaces"):
                            self.interfaces = value
                            self.interfaces.value_namespace = name_space
                            self.interfaces.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-interfaces"):
                            self.ipv6_interfaces = value
                            self.ipv6_interfaces.value_namespace = name_space
                            self.ipv6_interfaces.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6vrf-name"):
                            self.ipv6vrf_name = value
                            self.ipv6vrf_name.value_namespace = name_space
                            self.ipv6vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return (
                        (self.access_interface_summary is not None and self.access_interface_summary.has_data()) or
                        (self.interface_counts is not None and self.interface_counts.has_data()))

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.access_interface_summary is not None and self.access_interface_summary.has_operation()) or
                        (self.interface_counts is not None and self.interface_counts.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "access-interface-summary"):
                        if (self.access_interface_summary is None):
                            self.access_interface_summary = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary()
                            self.access_interface_summary.parent = self
                            self._children_name_map["access_interface_summary"] = "access-interface-summary"
                        return self.access_interface_summary

                    if (child_yang_name == "interface-counts"):
                        if (self.interface_counts is None):
                            self.interface_counts = IpSubscriber.Nodes.Node.Summary.InterfaceCounts()
                            self.interface_counts.parent = self
                            self._children_name_map["interface_counts"] = "interface-counts"
                        return self.interface_counts

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpSubscriber.Nodes.Node.Summary.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-interface-summary" or name == "interface-counts" or name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                IP subscriber interface table
                
                .. attribute:: interface
                
                	IP subscriber interface entry
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

                    self.interface = YList(self)

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
                                super(IpSubscriber.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSubscriber.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    IP subscriber interface entry
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_interface
                    
                    	Access interface through which this subscriber is accessible
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: age
                    
                    	Age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: current_change_age
                    
                    	Current change age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: initiator
                    
                    	Protocol trigger for creation of this subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfInitiatorData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorData>`
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_current_change_age
                    
                    	IPV6 Current change age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_initiator
                    
                    	Protocol trigger for creation of this subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfInitiatorData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorData>`
                    
                    .. attribute:: ipv6_last_state_change_time
                    
                    	Interface's IPV6 last state change time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_old_state
                    
                    	Previous state of the subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: ipv6_state
                    
                    	State of the subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: ipv6vrf
                    
                    	IPv6 VRF details
                    	**type**\:   :py:class:`Ipv6Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf>`
                    
                    .. attribute:: is_l2_connected
                    
                    	True if L2 connected
                    	**type**\:  bool
                    
                    .. attribute:: last_state_change_time
                    
                    	Interface's last state change time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: old_state
                    
                    	Previous state of the subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: session_type
                    
                    	Session Type
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	State of the subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateData>`
                    
                    .. attribute:: subscriber_ipv4_address
                    
                    	IPv4 Address of the subscriber
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: subscriber_ipv6_address
                    
                    	IPv6 Address of the subscriber
                    	**type**\:  str
                    
                    .. attribute:: subscriber_label
                    
                    	Subscriber label for this subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscriber_mac_addres
                    
                    	MAC address of the subscriber
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: vrf
                    
                    	IPv4 VRF details
                    	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_interface = YLeaf(YType.str, "access-interface")

                        self.age = YLeaf(YType.str, "age")

                        self.current_change_age = YLeaf(YType.str, "current-change-age")

                        self.initiator = YLeaf(YType.enumeration, "initiator")

                        self.interface_creation_time = YLeaf(YType.str, "interface-creation-time")

                        self.ipv6_current_change_age = YLeaf(YType.str, "ipv6-current-change-age")

                        self.ipv6_initiator = YLeaf(YType.enumeration, "ipv6-initiator")

                        self.ipv6_last_state_change_time = YLeaf(YType.str, "ipv6-last-state-change-time")

                        self.ipv6_old_state = YLeaf(YType.enumeration, "ipv6-old-state")

                        self.ipv6_state = YLeaf(YType.enumeration, "ipv6-state")

                        self.is_l2_connected = YLeaf(YType.boolean, "is-l2-connected")

                        self.last_state_change_time = YLeaf(YType.str, "last-state-change-time")

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.session_type = YLeaf(YType.str, "session-type")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.subscriber_ipv4_address = YLeaf(YType.str, "subscriber-ipv4-address")

                        self.subscriber_ipv6_address = YLeaf(YType.str, "subscriber-ipv6-address")

                        self.subscriber_label = YLeaf(YType.uint32, "subscriber-label")

                        self.subscriber_mac_addres = YLeaf(YType.str, "subscriber-mac-addres")

                        self.ipv6vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf()
                        self.ipv6vrf.parent = self
                        self._children_name_map["ipv6vrf"] = "ipv6vrf"
                        self._children_yang_names.add("ipv6vrf")

                        self.vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf()
                        self.vrf.parent = self
                        self._children_name_map["vrf"] = "vrf"
                        self._children_yang_names.add("vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "access_interface",
                                        "age",
                                        "current_change_age",
                                        "initiator",
                                        "interface_creation_time",
                                        "ipv6_current_change_age",
                                        "ipv6_initiator",
                                        "ipv6_last_state_change_time",
                                        "ipv6_old_state",
                                        "ipv6_state",
                                        "is_l2_connected",
                                        "last_state_change_time",
                                        "old_state",
                                        "session_type",
                                        "state",
                                        "subscriber_ipv4_address",
                                        "subscriber_ipv6_address",
                                        "subscriber_label",
                                        "subscriber_mac_addres") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSubscriber.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSubscriber.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class Vrf(Entity):
                        """
                        IPv4 VRF details
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "interface"

                            self.table_name = YLeaf(YType.str, "table-name")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("table_name",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.table_name.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.table_name.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vrf" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.table_name.is_set or self.table_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.table_name.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "table-name" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "table-name"):
                                self.table_name = value
                                self.table_name.value_namespace = name_space
                                self.table_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix


                    class Ipv6Vrf(Entity):
                        """
                        IPv6 VRF details
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf, self).__init__()

                            self.yang_name = "ipv6vrf"
                            self.yang_parent_name = "interface"

                            self.table_name = YLeaf(YType.str, "table-name")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("table_name",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.table_name.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.table_name.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6vrf" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.table_name.is_set or self.table_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.table_name.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "table-name" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "table-name"):
                                self.table_name = value
                                self.table_name.value_namespace = name_space
                                self.table_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.access_interface.is_set or
                            self.age.is_set or
                            self.current_change_age.is_set or
                            self.initiator.is_set or
                            self.interface_creation_time.is_set or
                            self.ipv6_current_change_age.is_set or
                            self.ipv6_initiator.is_set or
                            self.ipv6_last_state_change_time.is_set or
                            self.ipv6_old_state.is_set or
                            self.ipv6_state.is_set or
                            self.is_l2_connected.is_set or
                            self.last_state_change_time.is_set or
                            self.old_state.is_set or
                            self.session_type.is_set or
                            self.state.is_set or
                            self.subscriber_ipv4_address.is_set or
                            self.subscriber_ipv6_address.is_set or
                            self.subscriber_label.is_set or
                            self.subscriber_mac_addres.is_set or
                            (self.ipv6vrf is not None and self.ipv6vrf.has_data()) or
                            (self.vrf is not None and self.vrf.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.access_interface.yfilter != YFilter.not_set or
                            self.age.yfilter != YFilter.not_set or
                            self.current_change_age.yfilter != YFilter.not_set or
                            self.initiator.yfilter != YFilter.not_set or
                            self.interface_creation_time.yfilter != YFilter.not_set or
                            self.ipv6_current_change_age.yfilter != YFilter.not_set or
                            self.ipv6_initiator.yfilter != YFilter.not_set or
                            self.ipv6_last_state_change_time.yfilter != YFilter.not_set or
                            self.ipv6_old_state.yfilter != YFilter.not_set or
                            self.ipv6_state.yfilter != YFilter.not_set or
                            self.is_l2_connected.yfilter != YFilter.not_set or
                            self.last_state_change_time.yfilter != YFilter.not_set or
                            self.old_state.yfilter != YFilter.not_set or
                            self.session_type.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.subscriber_ipv4_address.yfilter != YFilter.not_set or
                            self.subscriber_ipv6_address.yfilter != YFilter.not_set or
                            self.subscriber_label.yfilter != YFilter.not_set or
                            self.subscriber_mac_addres.yfilter != YFilter.not_set or
                            (self.ipv6vrf is not None and self.ipv6vrf.has_operation()) or
                            (self.vrf is not None and self.vrf.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.access_interface.is_set or self.access_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_interface.get_name_leafdata())
                        if (self.age.is_set or self.age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.age.get_name_leafdata())
                        if (self.current_change_age.is_set or self.current_change_age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_change_age.get_name_leafdata())
                        if (self.initiator.is_set or self.initiator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.initiator.get_name_leafdata())
                        if (self.interface_creation_time.is_set or self.interface_creation_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_creation_time.get_name_leafdata())
                        if (self.ipv6_current_change_age.is_set or self.ipv6_current_change_age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_current_change_age.get_name_leafdata())
                        if (self.ipv6_initiator.is_set or self.ipv6_initiator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_initiator.get_name_leafdata())
                        if (self.ipv6_last_state_change_time.is_set or self.ipv6_last_state_change_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_last_state_change_time.get_name_leafdata())
                        if (self.ipv6_old_state.is_set or self.ipv6_old_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_old_state.get_name_leafdata())
                        if (self.ipv6_state.is_set or self.ipv6_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_state.get_name_leafdata())
                        if (self.is_l2_connected.is_set or self.is_l2_connected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_l2_connected.get_name_leafdata())
                        if (self.last_state_change_time.is_set or self.last_state_change_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change_time.get_name_leafdata())
                        if (self.old_state.is_set or self.old_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.old_state.get_name_leafdata())
                        if (self.session_type.is_set or self.session_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_type.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.subscriber_ipv4_address.is_set or self.subscriber_ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscriber_ipv4_address.get_name_leafdata())
                        if (self.subscriber_ipv6_address.is_set or self.subscriber_ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscriber_ipv6_address.get_name_leafdata())
                        if (self.subscriber_label.is_set or self.subscriber_label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscriber_label.get_name_leafdata())
                        if (self.subscriber_mac_addres.is_set or self.subscriber_mac_addres.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscriber_mac_addres.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipv6vrf"):
                            if (self.ipv6vrf is None):
                                self.ipv6vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf()
                                self.ipv6vrf.parent = self
                                self._children_name_map["ipv6vrf"] = "ipv6vrf"
                            return self.ipv6vrf

                        if (child_yang_name == "vrf"):
                            if (self.vrf is None):
                                self.vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf()
                                self.vrf.parent = self
                                self._children_name_map["vrf"] = "vrf"
                            return self.vrf

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6vrf" or name == "vrf" or name == "interface-name" or name == "access-interface" or name == "age" or name == "current-change-age" or name == "initiator" or name == "interface-creation-time" or name == "ipv6-current-change-age" or name == "ipv6-initiator" or name == "ipv6-last-state-change-time" or name == "ipv6-old-state" or name == "ipv6-state" or name == "is-l2-connected" or name == "last-state-change-time" or name == "old-state" or name == "session-type" or name == "state" or name == "subscriber-ipv4-address" or name == "subscriber-ipv6-address" or name == "subscriber-label" or name == "subscriber-mac-addres"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-interface"):
                            self.access_interface = value
                            self.access_interface.value_namespace = name_space
                            self.access_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "age"):
                            self.age = value
                            self.age.value_namespace = name_space
                            self.age.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-change-age"):
                            self.current_change_age = value
                            self.current_change_age.value_namespace = name_space
                            self.current_change_age.value_namespace_prefix = name_space_prefix
                        if(value_path == "initiator"):
                            self.initiator = value
                            self.initiator.value_namespace = name_space
                            self.initiator.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-creation-time"):
                            self.interface_creation_time = value
                            self.interface_creation_time.value_namespace = name_space
                            self.interface_creation_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-current-change-age"):
                            self.ipv6_current_change_age = value
                            self.ipv6_current_change_age.value_namespace = name_space
                            self.ipv6_current_change_age.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-initiator"):
                            self.ipv6_initiator = value
                            self.ipv6_initiator.value_namespace = name_space
                            self.ipv6_initiator.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-last-state-change-time"):
                            self.ipv6_last_state_change_time = value
                            self.ipv6_last_state_change_time.value_namespace = name_space
                            self.ipv6_last_state_change_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-old-state"):
                            self.ipv6_old_state = value
                            self.ipv6_old_state.value_namespace = name_space
                            self.ipv6_old_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-state"):
                            self.ipv6_state = value
                            self.ipv6_state.value_namespace = name_space
                            self.ipv6_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-l2-connected"):
                            self.is_l2_connected = value
                            self.is_l2_connected.value_namespace = name_space
                            self.is_l2_connected.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change-time"):
                            self.last_state_change_time = value
                            self.last_state_change_time.value_namespace = name_space
                            self.last_state_change_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "old-state"):
                            self.old_state = value
                            self.old_state.value_namespace = name_space
                            self.old_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-type"):
                            self.session_type = value
                            self.session_type.value_namespace = name_space
                            self.session_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscriber-ipv4-address"):
                            self.subscriber_ipv4_address = value
                            self.subscriber_ipv4_address.value_namespace = name_space
                            self.subscriber_ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscriber-ipv6-address"):
                            self.subscriber_ipv6_address = value
                            self.subscriber_ipv6_address.value_namespace = name_space
                            self.subscriber_ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscriber-label"):
                            self.subscriber_label = value
                            self.subscriber_label.value_namespace = name_space
                            self.subscriber_label.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscriber-mac-addres"):
                            self.subscriber_mac_addres = value
                            self.subscriber_mac_addres.value_namespace = name_space
                            self.subscriber_mac_addres.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpSubscriber.Nodes.Node.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AccessInterfaces(Entity):
                """
                IP subscriber access interface table
                
                .. attribute:: access_interface
                
                	IP subscriber access interface entry
                	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IpSubscriber.Nodes.Node.AccessInterfaces, self).__init__()

                    self.yang_name = "access-interfaces"
                    self.yang_parent_name = "node"

                    self.access_interface = YList(self)

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
                                super(IpSubscriber.Nodes.Node.AccessInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSubscriber.Nodes.Node.AccessInterfaces, self).__setattr__(name, value)


                class AccessInterface(Entity):
                    """
                    IP subscriber access interface entry
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: age
                    
                    	Age in HH\:MM\:SS format
                    	**type**\:  str
                    
                    .. attribute:: initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators>`
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in Month Date HH\:MM\:SS format
                    	**type**\:  str
                    
                    .. attribute:: interface_type
                    
                    	Interface Type
                    	**type**\:  str
                    
                    .. attribute:: ipv6_initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface for IPv6 session
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators>`
                    
                    .. attribute:: ipv6_state
                    
                    	Operational ipv6 state of this interface
                    	**type**\:   :py:class:`IpsubMaParentIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateData>`
                    
                    .. attribute:: session_limit
                    
                    	Configuration session limits for each session limit source and type
                    	**type**\:   :py:class:`SessionLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit>`
                    
                    .. attribute:: state
                    
                    	Operational state of this interface
                    	**type**\:   :py:class:`IpsubMaParentIntfStateData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateData>`
                    
                    .. attribute:: vlan_type
                    
                    	The VLAN type on the access interface
                    	**type**\:   :py:class:`IpsubMaParentIntfVlan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfVlan>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface, self).__init__()

                        self.yang_name = "access-interface"
                        self.yang_parent_name = "access-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.age = YLeaf(YType.str, "age")

                        self.interface_creation_time = YLeaf(YType.str, "interface-creation-time")

                        self.interface_type = YLeaf(YType.str, "interface-type")

                        self.ipv6_state = YLeaf(YType.enumeration, "ipv6-state")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.vlan_type = YLeaf(YType.enumeration, "vlan-type")

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "age",
                                        "interface_creation_time",
                                        "interface_type",
                                        "ipv6_state",
                                        "state",
                                        "vlan_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface, self).__setattr__(name, value)


                    class Initiators(Entity):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators, self).__init__()

                            self.yang_name = "initiators"
                            self.yang_parent_name = "access-interface"

                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_dropped_bytes = YLeaf(YType.uint32, "fsol-dropped-bytes")

                                self.fsol_dropped_packets = YLeaf(YType.uint32, "fsol-dropped-packets")

                                self.fsol_dropped_packets_dup_addr = YLeaf(YType.uint32, "fsol-dropped-packets-dup-addr")

                                self.fsol_dropped_packets_flow = YLeaf(YType.uint32, "fsol-dropped-packets-flow")

                                self.fsol_dropped_packets_session_limit = YLeaf(YType.uint32, "fsol-dropped-packets-session-limit")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                                self.is_configured = YLeaf(YType.boolean, "is-configured")

                                self.sessions = YLeaf(YType.uint32, "sessions")

                                self.unique_ip_check = YLeaf(YType.boolean, "unique-ip-check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_dropped_bytes",
                                                "fsol_dropped_packets",
                                                "fsol_dropped_packets_dup_addr",
                                                "fsol_dropped_packets_flow",
                                                "fsol_dropped_packets_session_limit",
                                                "fsol_packets",
                                                "is_configured",
                                                "sessions",
                                                "unique_ip_check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_dropped_bytes.is_set or
                                    self.fsol_dropped_packets.is_set or
                                    self.fsol_dropped_packets_dup_addr.is_set or
                                    self.fsol_dropped_packets_flow.is_set or
                                    self.fsol_dropped_packets_session_limit.is_set or
                                    self.fsol_packets.is_set or
                                    self.is_configured.is_set or
                                    self.sessions.is_set or
                                    self.unique_ip_check.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_flow.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set or
                                    self.is_configured.yfilter != YFilter.not_set or
                                    self.sessions.yfilter != YFilter.not_set or
                                    self.unique_ip_check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_dropped_bytes.is_set or self.fsol_dropped_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_bytes.get_name_leafdata())
                                if (self.fsol_dropped_packets.is_set or self.fsol_dropped_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets.get_name_leafdata())
                                if (self.fsol_dropped_packets_dup_addr.is_set or self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_dup_addr.get_name_leafdata())
                                if (self.fsol_dropped_packets_flow.is_set or self.fsol_dropped_packets_flow.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_flow.get_name_leafdata())
                                if (self.fsol_dropped_packets_session_limit.is_set or self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_session_limit.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())
                                if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_configured.get_name_leafdata())
                                if (self.sessions.is_set or self.sessions.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sessions.get_name_leafdata())
                                if (self.unique_ip_check.is_set or self.unique_ip_check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unique_ip_check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-dropped-bytes" or name == "fsol-dropped-packets" or name == "fsol-dropped-packets-dup-addr" or name == "fsol-dropped-packets-flow" or name == "fsol-dropped-packets-session-limit" or name == "fsol-packets" or name == "is-configured" or name == "sessions" or name == "unique-ip-check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-bytes"):
                                    self.fsol_dropped_bytes = value
                                    self.fsol_dropped_bytes.value_namespace = name_space
                                    self.fsol_dropped_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets"):
                                    self.fsol_dropped_packets = value
                                    self.fsol_dropped_packets.value_namespace = name_space
                                    self.fsol_dropped_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-dup-addr"):
                                    self.fsol_dropped_packets_dup_addr = value
                                    self.fsol_dropped_packets_dup_addr.value_namespace = name_space
                                    self.fsol_dropped_packets_dup_addr.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-flow"):
                                    self.fsol_dropped_packets_flow = value
                                    self.fsol_dropped_packets_flow.value_namespace = name_space
                                    self.fsol_dropped_packets_flow.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-session-limit"):
                                    self.fsol_dropped_packets_session_limit = value
                                    self.fsol_dropped_packets_session_limit.value_namespace = name_space
                                    self.fsol_dropped_packets_session_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-configured"):
                                    self.is_configured = value
                                    self.is_configured.value_namespace = name_space
                                    self.is_configured.value_namespace_prefix = name_space_prefix
                                if(value_path == "sessions"):
                                    self.sessions = value
                                    self.sessions.value_namespace = name_space
                                    self.sessions.value_namespace_prefix = name_space_prefix
                                if(value_path == "unique-ip-check"):
                                    self.unique_ip_check = value
                                    self.unique_ip_check.value_namespace = name_space
                                    self.unique_ip_check.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            packet trigger information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_dropped_bytes = YLeaf(YType.uint32, "fsol-dropped-bytes")

                                self.fsol_dropped_packets = YLeaf(YType.uint32, "fsol-dropped-packets")

                                self.fsol_dropped_packets_dup_addr = YLeaf(YType.uint32, "fsol-dropped-packets-dup-addr")

                                self.fsol_dropped_packets_flow = YLeaf(YType.uint32, "fsol-dropped-packets-flow")

                                self.fsol_dropped_packets_session_limit = YLeaf(YType.uint32, "fsol-dropped-packets-session-limit")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                                self.is_configured = YLeaf(YType.boolean, "is-configured")

                                self.sessions = YLeaf(YType.uint32, "sessions")

                                self.unique_ip_check = YLeaf(YType.boolean, "unique-ip-check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_dropped_bytes",
                                                "fsol_dropped_packets",
                                                "fsol_dropped_packets_dup_addr",
                                                "fsol_dropped_packets_flow",
                                                "fsol_dropped_packets_session_limit",
                                                "fsol_packets",
                                                "is_configured",
                                                "sessions",
                                                "unique_ip_check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_dropped_bytes.is_set or
                                    self.fsol_dropped_packets.is_set or
                                    self.fsol_dropped_packets_dup_addr.is_set or
                                    self.fsol_dropped_packets_flow.is_set or
                                    self.fsol_dropped_packets_session_limit.is_set or
                                    self.fsol_packets.is_set or
                                    self.is_configured.is_set or
                                    self.sessions.is_set or
                                    self.unique_ip_check.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_flow.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set or
                                    self.is_configured.yfilter != YFilter.not_set or
                                    self.sessions.yfilter != YFilter.not_set or
                                    self.unique_ip_check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_dropped_bytes.is_set or self.fsol_dropped_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_bytes.get_name_leafdata())
                                if (self.fsol_dropped_packets.is_set or self.fsol_dropped_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets.get_name_leafdata())
                                if (self.fsol_dropped_packets_dup_addr.is_set or self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_dup_addr.get_name_leafdata())
                                if (self.fsol_dropped_packets_flow.is_set or self.fsol_dropped_packets_flow.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_flow.get_name_leafdata())
                                if (self.fsol_dropped_packets_session_limit.is_set or self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_session_limit.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())
                                if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_configured.get_name_leafdata())
                                if (self.sessions.is_set or self.sessions.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sessions.get_name_leafdata())
                                if (self.unique_ip_check.is_set or self.unique_ip_check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unique_ip_check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-dropped-bytes" or name == "fsol-dropped-packets" or name == "fsol-dropped-packets-dup-addr" or name == "fsol-dropped-packets-flow" or name == "fsol-dropped-packets-session-limit" or name == "fsol-packets" or name == "is-configured" or name == "sessions" or name == "unique-ip-check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-bytes"):
                                    self.fsol_dropped_bytes = value
                                    self.fsol_dropped_bytes.value_namespace = name_space
                                    self.fsol_dropped_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets"):
                                    self.fsol_dropped_packets = value
                                    self.fsol_dropped_packets.value_namespace = name_space
                                    self.fsol_dropped_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-dup-addr"):
                                    self.fsol_dropped_packets_dup_addr = value
                                    self.fsol_dropped_packets_dup_addr.value_namespace = name_space
                                    self.fsol_dropped_packets_dup_addr.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-flow"):
                                    self.fsol_dropped_packets_flow = value
                                    self.fsol_dropped_packets_flow.value_namespace = name_space
                                    self.fsol_dropped_packets_flow.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-session-limit"):
                                    self.fsol_dropped_packets_session_limit = value
                                    self.fsol_dropped_packets_session_limit.value_namespace = name_space
                                    self.fsol_dropped_packets_session_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-configured"):
                                    self.is_configured = value
                                    self.is_configured.value_namespace = name_space
                                    self.is_configured.value_namespace_prefix = name_space_prefix
                                if(value_path == "sessions"):
                                    self.sessions = value
                                    self.sessions.value_namespace = name_space
                                    self.sessions.value_namespace_prefix = name_space_prefix
                                if(value_path == "unique-ip-check"):
                                    self.unique_ip_check = value
                                    self.unique_ip_check.value_namespace = name_space
                                    self.unique_ip_check.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv6Initiators(Entity):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface for IPv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators, self).__init__()

                            self.yang_name = "ipv6-initiators"
                            self.yang_parent_name = "access-interface"

                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self._children_name_map["dhcp"] = "dhcp"
                            self._children_yang_names.add("dhcp")

                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self
                            self._children_name_map["packet_trigger"] = "packet-trigger"
                            self._children_yang_names.add("packet-trigger")


                        class Dhcp(Entity):
                            """
                            DHCP information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp, self).__init__()

                                self.yang_name = "dhcp"
                                self.yang_parent_name = "ipv6-initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_dropped_bytes = YLeaf(YType.uint32, "fsol-dropped-bytes")

                                self.fsol_dropped_packets = YLeaf(YType.uint32, "fsol-dropped-packets")

                                self.fsol_dropped_packets_dup_addr = YLeaf(YType.uint32, "fsol-dropped-packets-dup-addr")

                                self.fsol_dropped_packets_flow = YLeaf(YType.uint32, "fsol-dropped-packets-flow")

                                self.fsol_dropped_packets_session_limit = YLeaf(YType.uint32, "fsol-dropped-packets-session-limit")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                                self.is_configured = YLeaf(YType.boolean, "is-configured")

                                self.sessions = YLeaf(YType.uint32, "sessions")

                                self.unique_ip_check = YLeaf(YType.boolean, "unique-ip-check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_dropped_bytes",
                                                "fsol_dropped_packets",
                                                "fsol_dropped_packets_dup_addr",
                                                "fsol_dropped_packets_flow",
                                                "fsol_dropped_packets_session_limit",
                                                "fsol_packets",
                                                "is_configured",
                                                "sessions",
                                                "unique_ip_check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_dropped_bytes.is_set or
                                    self.fsol_dropped_packets.is_set or
                                    self.fsol_dropped_packets_dup_addr.is_set or
                                    self.fsol_dropped_packets_flow.is_set or
                                    self.fsol_dropped_packets_session_limit.is_set or
                                    self.fsol_packets.is_set or
                                    self.is_configured.is_set or
                                    self.sessions.is_set or
                                    self.unique_ip_check.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_flow.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set or
                                    self.is_configured.yfilter != YFilter.not_set or
                                    self.sessions.yfilter != YFilter.not_set or
                                    self.unique_ip_check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_dropped_bytes.is_set or self.fsol_dropped_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_bytes.get_name_leafdata())
                                if (self.fsol_dropped_packets.is_set or self.fsol_dropped_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets.get_name_leafdata())
                                if (self.fsol_dropped_packets_dup_addr.is_set or self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_dup_addr.get_name_leafdata())
                                if (self.fsol_dropped_packets_flow.is_set or self.fsol_dropped_packets_flow.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_flow.get_name_leafdata())
                                if (self.fsol_dropped_packets_session_limit.is_set or self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_session_limit.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())
                                if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_configured.get_name_leafdata())
                                if (self.sessions.is_set or self.sessions.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sessions.get_name_leafdata())
                                if (self.unique_ip_check.is_set or self.unique_ip_check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unique_ip_check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-dropped-bytes" or name == "fsol-dropped-packets" or name == "fsol-dropped-packets-dup-addr" or name == "fsol-dropped-packets-flow" or name == "fsol-dropped-packets-session-limit" or name == "fsol-packets" or name == "is-configured" or name == "sessions" or name == "unique-ip-check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-bytes"):
                                    self.fsol_dropped_bytes = value
                                    self.fsol_dropped_bytes.value_namespace = name_space
                                    self.fsol_dropped_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets"):
                                    self.fsol_dropped_packets = value
                                    self.fsol_dropped_packets.value_namespace = name_space
                                    self.fsol_dropped_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-dup-addr"):
                                    self.fsol_dropped_packets_dup_addr = value
                                    self.fsol_dropped_packets_dup_addr.value_namespace = name_space
                                    self.fsol_dropped_packets_dup_addr.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-flow"):
                                    self.fsol_dropped_packets_flow = value
                                    self.fsol_dropped_packets_flow.value_namespace = name_space
                                    self.fsol_dropped_packets_flow.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-session-limit"):
                                    self.fsol_dropped_packets_session_limit = value
                                    self.fsol_dropped_packets_session_limit.value_namespace = name_space
                                    self.fsol_dropped_packets_session_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-configured"):
                                    self.is_configured = value
                                    self.is_configured.value_namespace = name_space
                                    self.is_configured.value_namespace_prefix = name_space_prefix
                                if(value_path == "sessions"):
                                    self.sessions = value
                                    self.sessions.value_namespace = name_space
                                    self.sessions.value_namespace_prefix = name_space_prefix
                                if(value_path == "unique-ip-check"):
                                    self.unique_ip_check = value
                                    self.unique_ip_check.value_namespace = name_space
                                    self.unique_ip_check.value_namespace_prefix = name_space_prefix


                        class PacketTrigger(Entity):
                            """
                            packet trigger information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger, self).__init__()

                                self.yang_name = "packet-trigger"
                                self.yang_parent_name = "ipv6-initiators"

                                self.fsol_bytes = YLeaf(YType.uint32, "fsol-bytes")

                                self.fsol_dropped_bytes = YLeaf(YType.uint32, "fsol-dropped-bytes")

                                self.fsol_dropped_packets = YLeaf(YType.uint32, "fsol-dropped-packets")

                                self.fsol_dropped_packets_dup_addr = YLeaf(YType.uint32, "fsol-dropped-packets-dup-addr")

                                self.fsol_dropped_packets_flow = YLeaf(YType.uint32, "fsol-dropped-packets-flow")

                                self.fsol_dropped_packets_session_limit = YLeaf(YType.uint32, "fsol-dropped-packets-session-limit")

                                self.fsol_packets = YLeaf(YType.uint32, "fsol-packets")

                                self.is_configured = YLeaf(YType.boolean, "is-configured")

                                self.sessions = YLeaf(YType.uint32, "sessions")

                                self.unique_ip_check = YLeaf(YType.boolean, "unique-ip-check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fsol_bytes",
                                                "fsol_dropped_bytes",
                                                "fsol_dropped_packets",
                                                "fsol_dropped_packets_dup_addr",
                                                "fsol_dropped_packets_flow",
                                                "fsol_dropped_packets_session_limit",
                                                "fsol_packets",
                                                "is_configured",
                                                "sessions",
                                                "unique_ip_check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.fsol_bytes.is_set or
                                    self.fsol_dropped_bytes.is_set or
                                    self.fsol_dropped_packets.is_set or
                                    self.fsol_dropped_packets_dup_addr.is_set or
                                    self.fsol_dropped_packets_flow.is_set or
                                    self.fsol_dropped_packets_session_limit.is_set or
                                    self.fsol_packets.is_set or
                                    self.is_configured.is_set or
                                    self.sessions.is_set or
                                    self.unique_ip_check.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fsol_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_bytes.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_flow.yfilter != YFilter.not_set or
                                    self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set or
                                    self.fsol_packets.yfilter != YFilter.not_set or
                                    self.is_configured.yfilter != YFilter.not_set or
                                    self.sessions.yfilter != YFilter.not_set or
                                    self.unique_ip_check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-trigger" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fsol_bytes.is_set or self.fsol_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_bytes.get_name_leafdata())
                                if (self.fsol_dropped_bytes.is_set or self.fsol_dropped_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_bytes.get_name_leafdata())
                                if (self.fsol_dropped_packets.is_set or self.fsol_dropped_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets.get_name_leafdata())
                                if (self.fsol_dropped_packets_dup_addr.is_set or self.fsol_dropped_packets_dup_addr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_dup_addr.get_name_leafdata())
                                if (self.fsol_dropped_packets_flow.is_set or self.fsol_dropped_packets_flow.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_flow.get_name_leafdata())
                                if (self.fsol_dropped_packets_session_limit.is_set or self.fsol_dropped_packets_session_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_dropped_packets_session_limit.get_name_leafdata())
                                if (self.fsol_packets.is_set or self.fsol_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fsol_packets.get_name_leafdata())
                                if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_configured.get_name_leafdata())
                                if (self.sessions.is_set or self.sessions.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sessions.get_name_leafdata())
                                if (self.unique_ip_check.is_set or self.unique_ip_check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unique_ip_check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "fsol-bytes" or name == "fsol-dropped-bytes" or name == "fsol-dropped-packets" or name == "fsol-dropped-packets-dup-addr" or name == "fsol-dropped-packets-flow" or name == "fsol-dropped-packets-session-limit" or name == "fsol-packets" or name == "is-configured" or name == "sessions" or name == "unique-ip-check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fsol-bytes"):
                                    self.fsol_bytes = value
                                    self.fsol_bytes.value_namespace = name_space
                                    self.fsol_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-bytes"):
                                    self.fsol_dropped_bytes = value
                                    self.fsol_dropped_bytes.value_namespace = name_space
                                    self.fsol_dropped_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets"):
                                    self.fsol_dropped_packets = value
                                    self.fsol_dropped_packets.value_namespace = name_space
                                    self.fsol_dropped_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-dup-addr"):
                                    self.fsol_dropped_packets_dup_addr = value
                                    self.fsol_dropped_packets_dup_addr.value_namespace = name_space
                                    self.fsol_dropped_packets_dup_addr.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-flow"):
                                    self.fsol_dropped_packets_flow = value
                                    self.fsol_dropped_packets_flow.value_namespace = name_space
                                    self.fsol_dropped_packets_flow.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-dropped-packets-session-limit"):
                                    self.fsol_dropped_packets_session_limit = value
                                    self.fsol_dropped_packets_session_limit.value_namespace = name_space
                                    self.fsol_dropped_packets_session_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "fsol-packets"):
                                    self.fsol_packets = value
                                    self.fsol_packets.value_namespace = name_space
                                    self.fsol_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-configured"):
                                    self.is_configured = value
                                    self.is_configured.value_namespace = name_space
                                    self.is_configured.value_namespace_prefix = name_space_prefix
                                if(value_path == "sessions"):
                                    self.sessions = value
                                    self.sessions.value_namespace = name_space
                                    self.sessions.value_namespace_prefix = name_space_prefix
                                if(value_path == "unique-ip-check"):
                                    self.unique_ip_check = value
                                    self.unique_ip_check.value_namespace = name_space
                                    self.unique_ip_check.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.dhcp is not None and self.dhcp.has_data()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.dhcp is not None and self.dhcp.has_operation()) or
                                (self.packet_trigger is not None and self.packet_trigger.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-initiators" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dhcp"):
                                if (self.dhcp is None):
                                    self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp()
                                    self.dhcp.parent = self
                                    self._children_name_map["dhcp"] = "dhcp"
                                return self.dhcp

                            if (child_yang_name == "packet-trigger"):
                                if (self.packet_trigger is None):
                                    self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger()
                                    self.packet_trigger.parent = self
                                    self._children_name_map["packet_trigger"] = "packet-trigger"
                                return self.packet_trigger

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dhcp" or name == "packet-trigger"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class SessionLimit(Entity):
                        """
                        Configuration session limits for each session
                        limit source and type
                        
                        .. attribute:: total
                        
                        	All sources session limits
                        	**type**\:   :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total>`
                        
                        .. attribute:: unclassified_source
                        
                        	Unclassified source session limits
                        	**type**\:   :py:class:`UnclassifiedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit, self).__init__()

                            self.yang_name = "session-limit"
                            self.yang_parent_name = "access-interface"

                            self.total = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total()
                            self.total.parent = self
                            self._children_name_map["total"] = "total"
                            self._children_yang_names.add("total")

                            self.unclassified_source = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource()
                            self.unclassified_source.parent = self
                            self._children_name_map["unclassified_source"] = "unclassified-source"
                            self._children_yang_names.add("unclassified-source")


                        class UnclassifiedSource(Entity):
                            """
                            Unclassified source session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource, self).__init__()

                                self.yang_name = "unclassified-source"
                                self.yang_parent_name = "session-limit"

                                self.per_vlan = YLeaf(YType.uint32, "per-vlan")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("per_vlan") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource, self).__setattr__(name, value)

                            def has_data(self):
                                return self.per_vlan.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.per_vlan.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "unclassified-source" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.per_vlan.is_set or self.per_vlan.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_vlan.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "per-vlan"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "per-vlan"):
                                    self.per_vlan = value
                                    self.per_vlan.value_namespace = name_space
                                    self.per_vlan.value_namespace_prefix = name_space_prefix


                        class Total(Entity):
                            """
                            All sources session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total, self).__init__()

                                self.yang_name = "total"
                                self.yang_parent_name = "session-limit"

                                self.per_vlan = YLeaf(YType.uint32, "per-vlan")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("per_vlan") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total, self).__setattr__(name, value)

                            def has_data(self):
                                return self.per_vlan.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.per_vlan.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "total" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.per_vlan.is_set or self.per_vlan.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_vlan.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "per-vlan"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "per-vlan"):
                                    self.per_vlan = value
                                    self.per_vlan.value_namespace = name_space
                                    self.per_vlan.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.total is not None and self.total.has_data()) or
                                (self.unclassified_source is not None and self.unclassified_source.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.total is not None and self.total.has_operation()) or
                                (self.unclassified_source is not None and self.unclassified_source.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-limit" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "total"):
                                if (self.total is None):
                                    self.total = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total()
                                    self.total.parent = self
                                    self._children_name_map["total"] = "total"
                                return self.total

                            if (child_yang_name == "unclassified-source"):
                                if (self.unclassified_source is None):
                                    self.unclassified_source = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource()
                                    self.unclassified_source.parent = self
                                    self._children_name_map["unclassified_source"] = "unclassified-source"
                                return self.unclassified_source

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "total" or name == "unclassified-source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.age.is_set or
                            self.interface_creation_time.is_set or
                            self.interface_type.is_set or
                            self.ipv6_state.is_set or
                            self.state.is_set or
                            self.vlan_type.is_set or
                            (self.initiators is not None and self.initiators.has_data()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_data()) or
                            (self.session_limit is not None and self.session_limit.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.age.yfilter != YFilter.not_set or
                            self.interface_creation_time.yfilter != YFilter.not_set or
                            self.interface_type.yfilter != YFilter.not_set or
                            self.ipv6_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.vlan_type.yfilter != YFilter.not_set or
                            (self.initiators is not None and self.initiators.has_operation()) or
                            (self.ipv6_initiators is not None and self.ipv6_initiators.has_operation()) or
                            (self.session_limit is not None and self.session_limit.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.age.is_set or self.age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.age.get_name_leafdata())
                        if (self.interface_creation_time.is_set or self.interface_creation_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_creation_time.get_name_leafdata())
                        if (self.interface_type.is_set or self.interface_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_type.get_name_leafdata())
                        if (self.ipv6_state.is_set or self.ipv6_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.vlan_type.is_set or self.vlan_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "initiators"):
                            if (self.initiators is None):
                                self.initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators()
                                self.initiators.parent = self
                                self._children_name_map["initiators"] = "initiators"
                            return self.initiators

                        if (child_yang_name == "ipv6-initiators"):
                            if (self.ipv6_initiators is None):
                                self.ipv6_initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators()
                                self.ipv6_initiators.parent = self
                                self._children_name_map["ipv6_initiators"] = "ipv6-initiators"
                            return self.ipv6_initiators

                        if (child_yang_name == "session-limit"):
                            if (self.session_limit is None):
                                self.session_limit = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit()
                                self.session_limit.parent = self
                                self._children_name_map["session_limit"] = "session-limit"
                            return self.session_limit

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "initiators" or name == "ipv6-initiators" or name == "session-limit" or name == "interface-name" or name == "age" or name == "interface-creation-time" or name == "interface-type" or name == "ipv6-state" or name == "state" or name == "vlan-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "age"):
                            self.age = value
                            self.age.value_namespace = name_space
                            self.age.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-creation-time"):
                            self.interface_creation_time = value
                            self.interface_creation_time.value_namespace = name_space
                            self.interface_creation_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-type"):
                            self.interface_type = value
                            self.interface_type.value_namespace = name_space
                            self.interface_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-state"):
                            self.ipv6_state = value
                            self.ipv6_state.value_namespace = name_space
                            self.ipv6_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-type"):
                            self.vlan_type = value
                            self.vlan_type.value_namespace = name_space
                            self.vlan_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.access_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.access_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "access-interface"):
                        for c in self.access_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.access_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.access_interfaces is not None and self.access_interfaces.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.access_interfaces is not None and self.access_interfaces.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "access-interfaces"):
                    if (self.access_interfaces is None):
                        self.access_interfaces = IpSubscriber.Nodes.Node.AccessInterfaces()
                        self.access_interfaces.parent = self
                        self._children_name_map["access_interfaces"] = "access-interfaces"
                    return self.access_interfaces

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = IpSubscriber.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = IpSubscriber.Nodes.Node.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-interfaces" or name == "interfaces" or name == "summary" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpSubscriber.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = IpSubscriber.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpSubscriber()
        return self._top_entity

