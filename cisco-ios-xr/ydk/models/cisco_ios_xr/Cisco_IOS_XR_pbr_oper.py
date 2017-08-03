""" Cisco_IOS_XR_pbr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr package operational data.

This module contains definitions
for the following management objects\:
  pbr\: PBR operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PolicyState(Enum):
    """
    PolicyState

    Different Interface states

    .. data:: active = 0

    	active

    .. data:: suspended = 1

    	suspended

    """

    active = Enum.YLeaf(0, "active")

    suspended = Enum.YLeaf(1, "suspended")



class Pbr(Entity):
    """
    PBR operational data
    
    .. attribute:: nodes
    
    	Node\-specific PBR operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes>`
    
    

    """

    _prefix = 'pbr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Pbr, self).__init__()
        self._top_entity = None

        self.yang_name = "pbr"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-oper"

        self.nodes = Pbr.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific PBR operational data
        
        .. attribute:: node
        
        	PBR operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node>`
        
        

        """

        _prefix = 'pbr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pbr.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pbr"

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
                        super(Pbr.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pbr.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            PBR operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: policy_map
            
            	Operational data for policymaps
            	**type**\:   :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap>`
            
            

            """

            _prefix = 'pbr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pbr.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.policy_map = Pbr.Nodes.Node.PolicyMap()
                self.policy_map.parent = self
                self._children_name_map["policy_map"] = "policy-map"
                self._children_yang_names.add("policy-map")

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
                            super(Pbr.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pbr.Nodes.Node, self).__setattr__(name, value)


            class PolicyMap(Entity):
                """
                Operational data for policymaps
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces>`
                
                

                """

                _prefix = 'pbr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pbr.Nodes.Node.PolicyMap, self).__init__()

                    self.yang_name = "policy-map"
                    self.yang_parent_name = "node"

                    self.interfaces = Pbr.Nodes.Node.PolicyMap.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")


                class Interfaces(Entity):
                    """
                    Operational data for all interfaces
                    
                    .. attribute:: interface
                    
                    	PBR action data for a particular interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'pbr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pbr.Nodes.Node.PolicyMap.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "policy-map"

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
                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pbr.Nodes.Node.PolicyMap.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        PBR action data for a particular interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Name of the interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: direction
                        
                        	PBR direction
                        	**type**\:   :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction>`
                        
                        

                        """

                        _prefix = 'pbr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.direction = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction()
                            self.direction.parent = self
                            self._children_name_map["direction"] = "direction"
                            self._children_yang_names.add("direction")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface, self).__setattr__(name, value)


                        class Direction(Entity):
                            """
                            PBR direction
                            
                            .. attribute:: input
                            
                            	PBR policy statistics
                            	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input>`
                            
                            

                            """

                            _prefix = 'pbr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction, self).__init__()

                                self.yang_name = "direction"
                                self.yang_parent_name = "interface"

                                self.input = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                                self._children_yang_names.add("input")


                            class Input(Entity):
                                """
                                PBR policy statistics
                                
                                .. attribute:: class_stat
                                
                                	Array of classes contained in policy
                                	**type**\: list of    :py:class:`ClassStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat>`
                                
                                .. attribute:: node_name
                                
                                	NodeName
                                	**type**\:  str
                                
                                	**length:** 0..42
                                
                                .. attribute:: policy_name
                                
                                	PolicyName
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State
                                	**type**\:   :py:class:`PolicyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.PolicyState>`
                                
                                .. attribute:: state_description
                                
                                	StateDescription
                                	**type**\:  str
                                
                                	**length:** 0..128
                                
                                

                                """

                                _prefix = 'pbr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input, self).__init__()

                                    self.yang_name = "input"
                                    self.yang_parent_name = "direction"

                                    self.node_name = YLeaf(YType.str, "node-name")

                                    self.policy_name = YLeaf(YType.str, "policy-name")

                                    self.state = YLeaf(YType.enumeration, "state")

                                    self.state_description = YLeaf(YType.str, "state-description")

                                    self.class_stat = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("node_name",
                                                    "policy_name",
                                                    "state",
                                                    "state_description") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input, self).__setattr__(name, value)


                                class ClassStat(Entity):
                                    """
                                    Array of classes contained in policy
                                    
                                    .. attribute:: class_id
                                    
                                    	ClassId
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_name
                                    
                                    	ClassName
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: counter_validity_bitmask
                                    
                                    	 Bitmask to indicate which counter or counters are undetermined. Counters will be marked undetermined when one or more classes share queues with class\-default because in such cases the value of counters for each class is invalid. Based on the flag(s) set, the following counters will be marked undetermined. For example, if value of this object returned is 0x00000101, counters TransmitPackets/TransmitBytes/TotalTransmitRate and DropPackets/DropBytes are undetermined .0x00000001 \- Transmit (TransmitPackets/TransmitBytes/TotalTransmitRate ), 0x00000002 \- Drop (TotalDropPackets/TotalDropBytes/TotalDropRate), 0x00000004 \- Httpr (HttprTransmitPackets/HttprTransmitBytes), 
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: general_stats
                                    
                                    	general stats
                                    	**type**\:   :py:class:`GeneralStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats>`
                                    
                                    .. attribute:: httpr_stats
                                    
                                    	HTTPR stats
                                    	**type**\:   :py:class:`HttprStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat, self).__init__()

                                        self.yang_name = "class-stat"
                                        self.yang_parent_name = "input"

                                        self.class_id = YLeaf(YType.uint32, "class-id")

                                        self.class_name = YLeaf(YType.str, "class-name")

                                        self.counter_validity_bitmask = YLeaf(YType.uint64, "counter-validity-bitmask")

                                        self.general_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats()
                                        self.general_stats.parent = self
                                        self._children_name_map["general_stats"] = "general-stats"
                                        self._children_yang_names.add("general-stats")

                                        self.httpr_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats()
                                        self.httpr_stats.parent = self
                                        self._children_name_map["httpr_stats"] = "httpr-stats"
                                        self._children_yang_names.add("httpr-stats")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("class_id",
                                                        "class_name",
                                                        "counter_validity_bitmask") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat, self).__setattr__(name, value)


                                    class GeneralStats(Entity):
                                        """
                                        general stats
                                        
                                        .. attribute:: match_data_rate
                                        
                                        	Incoming matched data rate in kbps
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: pre_policy_matched_bytes
                                        
                                        	Matched bytes before applying policy
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: pre_policy_matched_packets
                                        
                                        	Matched pkts before applying policy
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: total_drop_bytes
                                        
                                        	Dropped bytes (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_packets
                                        
                                        	Dropped packets (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_rate
                                        
                                        	Total drop rate (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_transmit_rate
                                        
                                        	Total transmit rate in kbps
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: transmit_bytes
                                        
                                        	Transmitted bytes (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_packets
                                        
                                        	Transmitted packets (packets/bytes)
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats, self).__init__()

                                            self.yang_name = "general-stats"
                                            self.yang_parent_name = "class-stat"

                                            self.match_data_rate = YLeaf(YType.uint32, "match-data-rate")

                                            self.pre_policy_matched_bytes = YLeaf(YType.uint64, "pre-policy-matched-bytes")

                                            self.pre_policy_matched_packets = YLeaf(YType.uint64, "pre-policy-matched-packets")

                                            self.total_drop_bytes = YLeaf(YType.uint64, "total-drop-bytes")

                                            self.total_drop_packets = YLeaf(YType.uint64, "total-drop-packets")

                                            self.total_drop_rate = YLeaf(YType.uint32, "total-drop-rate")

                                            self.total_transmit_rate = YLeaf(YType.uint32, "total-transmit-rate")

                                            self.transmit_bytes = YLeaf(YType.uint64, "transmit-bytes")

                                            self.transmit_packets = YLeaf(YType.uint64, "transmit-packets")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("match_data_rate",
                                                            "pre_policy_matched_bytes",
                                                            "pre_policy_matched_packets",
                                                            "total_drop_bytes",
                                                            "total_drop_packets",
                                                            "total_drop_rate",
                                                            "total_transmit_rate",
                                                            "transmit_bytes",
                                                            "transmit_packets") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.match_data_rate.is_set or
                                                self.pre_policy_matched_bytes.is_set or
                                                self.pre_policy_matched_packets.is_set or
                                                self.total_drop_bytes.is_set or
                                                self.total_drop_packets.is_set or
                                                self.total_drop_rate.is_set or
                                                self.total_transmit_rate.is_set or
                                                self.transmit_bytes.is_set or
                                                self.transmit_packets.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.match_data_rate.yfilter != YFilter.not_set or
                                                self.pre_policy_matched_bytes.yfilter != YFilter.not_set or
                                                self.pre_policy_matched_packets.yfilter != YFilter.not_set or
                                                self.total_drop_bytes.yfilter != YFilter.not_set or
                                                self.total_drop_packets.yfilter != YFilter.not_set or
                                                self.total_drop_rate.yfilter != YFilter.not_set or
                                                self.total_transmit_rate.yfilter != YFilter.not_set or
                                                self.transmit_bytes.yfilter != YFilter.not_set or
                                                self.transmit_packets.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "general-stats" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.match_data_rate.is_set or self.match_data_rate.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.match_data_rate.get_name_leafdata())
                                            if (self.pre_policy_matched_bytes.is_set or self.pre_policy_matched_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.pre_policy_matched_bytes.get_name_leafdata())
                                            if (self.pre_policy_matched_packets.is_set or self.pre_policy_matched_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.pre_policy_matched_packets.get_name_leafdata())
                                            if (self.total_drop_bytes.is_set or self.total_drop_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.total_drop_bytes.get_name_leafdata())
                                            if (self.total_drop_packets.is_set or self.total_drop_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.total_drop_packets.get_name_leafdata())
                                            if (self.total_drop_rate.is_set or self.total_drop_rate.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.total_drop_rate.get_name_leafdata())
                                            if (self.total_transmit_rate.is_set or self.total_transmit_rate.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.total_transmit_rate.get_name_leafdata())
                                            if (self.transmit_bytes.is_set or self.transmit_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_bytes.get_name_leafdata())
                                            if (self.transmit_packets.is_set or self.transmit_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_packets.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "match-data-rate" or name == "pre-policy-matched-bytes" or name == "pre-policy-matched-packets" or name == "total-drop-bytes" or name == "total-drop-packets" or name == "total-drop-rate" or name == "total-transmit-rate" or name == "transmit-bytes" or name == "transmit-packets"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "match-data-rate"):
                                                self.match_data_rate = value
                                                self.match_data_rate.value_namespace = name_space
                                                self.match_data_rate.value_namespace_prefix = name_space_prefix
                                            if(value_path == "pre-policy-matched-bytes"):
                                                self.pre_policy_matched_bytes = value
                                                self.pre_policy_matched_bytes.value_namespace = name_space
                                                self.pre_policy_matched_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "pre-policy-matched-packets"):
                                                self.pre_policy_matched_packets = value
                                                self.pre_policy_matched_packets.value_namespace = name_space
                                                self.pre_policy_matched_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "total-drop-bytes"):
                                                self.total_drop_bytes = value
                                                self.total_drop_bytes.value_namespace = name_space
                                                self.total_drop_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "total-drop-packets"):
                                                self.total_drop_packets = value
                                                self.total_drop_packets.value_namespace = name_space
                                                self.total_drop_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "total-drop-rate"):
                                                self.total_drop_rate = value
                                                self.total_drop_rate.value_namespace = name_space
                                                self.total_drop_rate.value_namespace_prefix = name_space_prefix
                                            if(value_path == "total-transmit-rate"):
                                                self.total_transmit_rate = value
                                                self.total_transmit_rate.value_namespace = name_space
                                                self.total_transmit_rate.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-bytes"):
                                                self.transmit_bytes = value
                                                self.transmit_bytes.value_namespace = name_space
                                                self.transmit_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-packets"):
                                                self.transmit_packets = value
                                                self.transmit_packets.value_namespace = name_space
                                                self.transmit_packets.value_namespace_prefix = name_space_prefix


                                    class HttprStats(Entity):
                                        """
                                        HTTPR stats
                                        
                                        .. attribute:: drop_bytes
                                        
                                        	Dropped bytes
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: drop_packets
                                        
                                        	Dropped  packets
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: resp_sent_bytes
                                        
                                        	TotalNum of Bytes HTTPR response sent
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: resp_sent_packets
                                        
                                        	TotalNum of pkts HTTPR response sent
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: rqst_rcvd_bytes
                                        
                                        	TotalNum of Bytes HTTP request received
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: rqst_rcvd_packets
                                        
                                        	TotalNum of pkts HTTP request received
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats, self).__init__()

                                            self.yang_name = "httpr-stats"
                                            self.yang_parent_name = "class-stat"

                                            self.drop_bytes = YLeaf(YType.uint64, "drop-bytes")

                                            self.drop_packets = YLeaf(YType.uint64, "drop-packets")

                                            self.resp_sent_bytes = YLeaf(YType.uint64, "resp-sent-bytes")

                                            self.resp_sent_packets = YLeaf(YType.uint64, "resp-sent-packets")

                                            self.rqst_rcvd_bytes = YLeaf(YType.uint64, "rqst-rcvd-bytes")

                                            self.rqst_rcvd_packets = YLeaf(YType.uint64, "rqst-rcvd-packets")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("drop_bytes",
                                                            "drop_packets",
                                                            "resp_sent_bytes",
                                                            "resp_sent_packets",
                                                            "rqst_rcvd_bytes",
                                                            "rqst_rcvd_packets") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.drop_bytes.is_set or
                                                self.drop_packets.is_set or
                                                self.resp_sent_bytes.is_set or
                                                self.resp_sent_packets.is_set or
                                                self.rqst_rcvd_bytes.is_set or
                                                self.rqst_rcvd_packets.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.drop_bytes.yfilter != YFilter.not_set or
                                                self.drop_packets.yfilter != YFilter.not_set or
                                                self.resp_sent_bytes.yfilter != YFilter.not_set or
                                                self.resp_sent_packets.yfilter != YFilter.not_set or
                                                self.rqst_rcvd_bytes.yfilter != YFilter.not_set or
                                                self.rqst_rcvd_packets.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "httpr-stats" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.drop_bytes.is_set or self.drop_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.drop_bytes.get_name_leafdata())
                                            if (self.drop_packets.is_set or self.drop_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.drop_packets.get_name_leafdata())
                                            if (self.resp_sent_bytes.is_set or self.resp_sent_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.resp_sent_bytes.get_name_leafdata())
                                            if (self.resp_sent_packets.is_set or self.resp_sent_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.resp_sent_packets.get_name_leafdata())
                                            if (self.rqst_rcvd_bytes.is_set or self.rqst_rcvd_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rqst_rcvd_bytes.get_name_leafdata())
                                            if (self.rqst_rcvd_packets.is_set or self.rqst_rcvd_packets.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rqst_rcvd_packets.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "drop-bytes" or name == "drop-packets" or name == "resp-sent-bytes" or name == "resp-sent-packets" or name == "rqst-rcvd-bytes" or name == "rqst-rcvd-packets"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "drop-bytes"):
                                                self.drop_bytes = value
                                                self.drop_bytes.value_namespace = name_space
                                                self.drop_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "drop-packets"):
                                                self.drop_packets = value
                                                self.drop_packets.value_namespace = name_space
                                                self.drop_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "resp-sent-bytes"):
                                                self.resp_sent_bytes = value
                                                self.resp_sent_bytes.value_namespace = name_space
                                                self.resp_sent_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "resp-sent-packets"):
                                                self.resp_sent_packets = value
                                                self.resp_sent_packets.value_namespace = name_space
                                                self.resp_sent_packets.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rqst-rcvd-bytes"):
                                                self.rqst_rcvd_bytes = value
                                                self.rqst_rcvd_bytes.value_namespace = name_space
                                                self.rqst_rcvd_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rqst-rcvd-packets"):
                                                self.rqst_rcvd_packets = value
                                                self.rqst_rcvd_packets.value_namespace = name_space
                                                self.rqst_rcvd_packets.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.class_id.is_set or
                                            self.class_name.is_set or
                                            self.counter_validity_bitmask.is_set or
                                            (self.general_stats is not None and self.general_stats.has_data()) or
                                            (self.httpr_stats is not None and self.httpr_stats.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.class_id.yfilter != YFilter.not_set or
                                            self.class_name.yfilter != YFilter.not_set or
                                            self.counter_validity_bitmask.yfilter != YFilter.not_set or
                                            (self.general_stats is not None and self.general_stats.has_operation()) or
                                            (self.httpr_stats is not None and self.httpr_stats.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "class-stat" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.class_id.is_set or self.class_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.class_id.get_name_leafdata())
                                        if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.class_name.get_name_leafdata())
                                        if (self.counter_validity_bitmask.is_set or self.counter_validity_bitmask.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.counter_validity_bitmask.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "general-stats"):
                                            if (self.general_stats is None):
                                                self.general_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats()
                                                self.general_stats.parent = self
                                                self._children_name_map["general_stats"] = "general-stats"
                                            return self.general_stats

                                        if (child_yang_name == "httpr-stats"):
                                            if (self.httpr_stats is None):
                                                self.httpr_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats()
                                                self.httpr_stats.parent = self
                                                self._children_name_map["httpr_stats"] = "httpr-stats"
                                            return self.httpr_stats

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "general-stats" or name == "httpr-stats" or name == "class-id" or name == "class-name" or name == "counter-validity-bitmask"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "class-id"):
                                            self.class_id = value
                                            self.class_id.value_namespace = name_space
                                            self.class_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "class-name"):
                                            self.class_name = value
                                            self.class_name.value_namespace = name_space
                                            self.class_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "counter-validity-bitmask"):
                                            self.counter_validity_bitmask = value
                                            self.counter_validity_bitmask.value_namespace = name_space
                                            self.counter_validity_bitmask.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.class_stat:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.node_name.is_set or
                                        self.policy_name.is_set or
                                        self.state.is_set or
                                        self.state_description.is_set)

                                def has_operation(self):
                                    for c in self.class_stat:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.node_name.yfilter != YFilter.not_set or
                                        self.policy_name.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set or
                                        self.state_description.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "input" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.node_name.get_name_leafdata())
                                    if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_name.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())
                                    if (self.state_description.is_set or self.state_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state_description.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "class-stat"):
                                        for c in self.class_stat:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.class_stat.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "class-stat" or name == "node-name" or name == "policy-name" or name == "state" or name == "state-description"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "node-name"):
                                        self.node_name = value
                                        self.node_name.value_namespace = name_space
                                        self.node_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-name"):
                                        self.policy_name = value
                                        self.policy_name.value_namespace = name_space
                                        self.policy_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state-description"):
                                        self.state_description = value
                                        self.state_description.value_namespace = name_space
                                        self.state_description.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.input is not None and self.input.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.input is not None and self.input.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "direction" + path_buffer

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

                                if (child_yang_name == "input"):
                                    if (self.input is None):
                                        self.input = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                    return self.input

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "input"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                (self.direction is not None and self.direction.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                (self.direction is not None and self.direction.has_operation()))

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

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "direction"):
                                if (self.direction is None):
                                    self.direction = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction()
                                    self.direction.parent = self
                                    self._children_name_map["direction"] = "direction"
                                return self.direction

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix

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
                            c = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface()
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

                def has_data(self):
                    return (self.interfaces is not None and self.interfaces.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.interfaces is not None and self.interfaces.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-map" + path_buffer

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

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = Pbr.Nodes.Node.PolicyMap.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interfaces"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.policy_map is not None and self.policy_map.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.policy_map is not None and self.policy_map.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-pbr-oper:pbr/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "policy-map"):
                    if (self.policy_map is None):
                        self.policy_map = Pbr.Nodes.Node.PolicyMap()
                        self.policy_map.parent = self
                        self._children_name_map["policy_map"] = "policy-map"
                    return self.policy_map

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "policy-map" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-pbr-oper:pbr/%s" % self.get_segment_path()
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
                c = Pbr.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-pbr-oper:pbr" + path_buffer

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
                self.nodes = Pbr.Nodes()
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
        self._top_entity = Pbr()
        return self._top_entity

