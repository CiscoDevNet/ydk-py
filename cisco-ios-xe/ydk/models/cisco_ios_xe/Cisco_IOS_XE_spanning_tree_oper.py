""" Cisco_IOS_XE_spanning_tree_oper 

This module contains a collection of YANG definitions for
monitoring vlans in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class StpLinkRole(Enum):
    """
    StpLinkRole (Enum Class)

    Type definition for the different link types

    .. data:: stp_auto = 0

    .. data:: stp_point_to_point = 1

    .. data:: stp_shared = 2

    """

    stp_auto = Enum.YLeaf(0, "stp-auto")

    stp_point_to_point = Enum.YLeaf(1, "stp-point-to-point")

    stp_shared = Enum.YLeaf(2, "stp-shared")


class StpMode(Enum):
    """
    StpMode (Enum Class)

    Spanning tree operating mode

    .. data:: stp_mode_pvst = 0

    .. data:: stp_mode_rapid_pvst = 1

    .. data:: stp_mode_mst = 2

    """

    stp_mode_pvst = Enum.YLeaf(0, "stp-mode-pvst")

    stp_mode_rapid_pvst = Enum.YLeaf(1, "stp-mode-rapid-pvst")

    stp_mode_mst = Enum.YLeaf(2, "stp-mode-mst")


class StpPortBpdufilter(Enum):
    """
    StpPortBpdufilter (Enum Class)

    Send or receive BPDUs on this interface

    .. data:: stp_port_bpdufilter_disable = 0

    .. data:: stp_port_bpdufilter_enable = 1

    .. data:: stp_port_bpdufilter_default = 2

    """

    stp_port_bpdufilter_disable = Enum.YLeaf(0, "stp-port-bpdufilter-disable")

    stp_port_bpdufilter_enable = Enum.YLeaf(1, "stp-port-bpdufilter-enable")

    stp_port_bpdufilter_default = Enum.YLeaf(2, "stp-port-bpdufilter-default")


class StpPortBpduguard(Enum):
    """
    StpPortBpduguard (Enum Class)

    Accept BPDUs on this interface

    .. data:: stp_port_bpduguard_disable = 0

    .. data:: stp_port_bpduguard_enable = 1

    .. data:: stp_port_bpduguard_default = 2

    """

    stp_port_bpduguard_disable = Enum.YLeaf(0, "stp-port-bpduguard-disable")

    stp_port_bpduguard_enable = Enum.YLeaf(1, "stp-port-bpduguard-enable")

    stp_port_bpduguard_default = Enum.YLeaf(2, "stp-port-bpduguard-default")


class StpPortGuard(Enum):
    """
    StpPortGuard (Enum Class)

    Interface's spanning tree guard mode

    .. data:: stp_port_guard_default = 0

    .. data:: stp_port_guard_root = 1

    .. data:: stp_port_guard_loop = 2

    .. data:: stp_port_guard_none = 3

    """

    stp_port_guard_default = Enum.YLeaf(0, "stp-port-guard-default")

    stp_port_guard_root = Enum.YLeaf(1, "stp-port-guard-root")

    stp_port_guard_loop = Enum.YLeaf(2, "stp-port-guard-loop")

    stp_port_guard_none = Enum.YLeaf(3, "stp-port-guard-none")


class StpPortRole(Enum):
    """
    StpPortRole (Enum Class)

    Spanning Tree Protocol port roles

    .. data:: stp_master = 0

    .. data:: stp_alternate = 1

    .. data:: stp_root = 2

    .. data:: stp_designated = 3

    .. data:: stp_backup = 4

    """

    stp_master = Enum.YLeaf(0, "stp-master")

    stp_alternate = Enum.YLeaf(1, "stp-alternate")

    stp_root = Enum.YLeaf(2, "stp-root")

    stp_designated = Enum.YLeaf(3, "stp-designated")

    stp_backup = Enum.YLeaf(4, "stp-backup")


class StpPortState(Enum):
    """
    StpPortState (Enum Class)

    Spanning Tree Protocol port states

    .. data:: stp_disabled = 0

    .. data:: stp_blocking = 1

    .. data:: stp_listening = 2

    .. data:: stp_learning = 3

    .. data:: stp_forwarding = 4

    .. data:: stp_broken = 5

    .. data:: stp_invalid = 6

    """

    stp_disabled = Enum.YLeaf(0, "stp-disabled")

    stp_blocking = Enum.YLeaf(1, "stp-blocking")

    stp_listening = Enum.YLeaf(2, "stp-listening")

    stp_learning = Enum.YLeaf(3, "stp-learning")

    stp_forwarding = Enum.YLeaf(4, "stp-forwarding")

    stp_broken = Enum.YLeaf(5, "stp-broken")

    stp_invalid = Enum.YLeaf(6, "stp-invalid")



class StpDetails(Entity):
    """
    Top\-level container for spanning tree operational data
    
    .. attribute:: stp_detail
    
    	List of mst/rapid\-pvst spanning\-tree, keyed by instance name
    	**type**\: list of  		 :py:class:`StpDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpDetails.StpDetail>`
    
    .. attribute:: stp_global
    
    	Global state data
    	**type**\:  :py:class:`StpGlobal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpDetails.StpGlobal>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'stp-ios-xe-oper'
    _revision = '2017-08-10'

    def __init__(self):
        super(StpDetails, self).__init__()
        self._top_entity = None

        self.yang_name = "stp-details"
        self.yang_parent_name = "Cisco-IOS-XE-spanning-tree-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("stp-global", ("stp_global", StpDetails.StpGlobal))])
        self._child_list_classes = OrderedDict([("stp-detail", ("stp_detail", StpDetails.StpDetail))])
        self._leafs = OrderedDict()

        self.stp_global = None
        self._children_name_map["stp_global"] = "stp-global"
        self._children_yang_names.add("stp-global")

        self.stp_detail = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-spanning-tree-oper:stp-details"

    def __setattr__(self, name, value):
        self._perform_setattr(StpDetails, [], name, value)


    class StpDetail(Entity):
        """
        List of mst/rapid\-pvst spanning\-tree, keyed by instance name
        
        .. attribute:: instance  (key)
        
        	Spanning\-tree enabled mode and id
        	**type**\: str
        
        .. attribute:: hello_time
        
        	The interval between periodic transmissions of configuration messages by designated ports
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: max_age
        
        	The maximum age of the information transmitted by the bridge when it is the root bridge
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: forwarding_delay
        
        	The delay used by STP bridges to transition root and designated ports to forwarding
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: hold_count
        
        	The maximum number of BPDUs per second that the switch can send from an interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bridge_priority
        
        	The manageable component of the Bridge Identifier
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: bridge_address
        
        	A unique 48\-bit Universally Administered MAC Address assigned to the bridge
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: designated_root_priority
        
        	The bridge priority of the root of the spanning tree, as determined by the Spanning Tree Protocol, as executed by this node
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: designated_root_address
        
        	The bridge address of the root of the spanning tree, as determined by the Spanning Tree Protocol, as executed by this node
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: root_port
        
        	The port number of the port which offers the lowest cost path from this bridge to the root bridge
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: root_cost
        
        	The cost of the path to the root as seen from this bridge
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: hold_time
        
        	This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: topology_changes
        
        	The total number of topology changes detected by this bridge since the management entity was last reset or initialized
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: time_of_last_topology_change
        
        	The time of the last topology change that was detected by the bridge entity.The time is POSIX time UTC
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: interfaces
        
        	List of interfaces on which STP is enable
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpDetails.StpDetail.Interfaces>`
        
        

        """

        _prefix = 'stp-ios-xe-oper'
        _revision = '2017-08-10'

        def __init__(self):
            super(StpDetails.StpDetail, self).__init__()

            self.yang_name = "stp-detail"
            self.yang_parent_name = "stp-details"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['instance']
            self._child_container_classes = OrderedDict([("interfaces", ("interfaces", StpDetails.StpDetail.Interfaces))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('instance', YLeaf(YType.str, 'instance')),
                ('hello_time', YLeaf(YType.int32, 'hello-time')),
                ('max_age', YLeaf(YType.int32, 'max-age')),
                ('forwarding_delay', YLeaf(YType.int32, 'forwarding-delay')),
                ('hold_count', YLeaf(YType.uint32, 'hold-count')),
                ('bridge_priority', YLeaf(YType.uint16, 'bridge-priority')),
                ('bridge_address', YLeaf(YType.str, 'bridge-address')),
                ('designated_root_priority', YLeaf(YType.uint32, 'designated-root-priority')),
                ('designated_root_address', YLeaf(YType.str, 'designated-root-address')),
                ('root_port', YLeaf(YType.uint16, 'root-port')),
                ('root_cost', YLeaf(YType.uint64, 'root-cost')),
                ('hold_time', YLeaf(YType.uint64, 'hold-time')),
                ('topology_changes', YLeaf(YType.uint64, 'topology-changes')),
                ('time_of_last_topology_change', YLeaf(YType.str, 'time-of-last-topology-change')),
            ])
            self.instance = None
            self.hello_time = None
            self.max_age = None
            self.forwarding_delay = None
            self.hold_count = None
            self.bridge_priority = None
            self.bridge_address = None
            self.designated_root_priority = None
            self.designated_root_address = None
            self.root_port = None
            self.root_cost = None
            self.hold_time = None
            self.topology_changes = None
            self.time_of_last_topology_change = None

            self.interfaces = StpDetails.StpDetail.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "stp-detail" + "[instance='" + str(self.instance) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-spanning-tree-oper:stp-details/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StpDetails.StpDetail, ['instance', 'hello_time', 'max_age', 'forwarding_delay', 'hold_count', 'bridge_priority', 'bridge_address', 'designated_root_priority', 'designated_root_address', 'root_port', 'root_cost', 'hold_time', 'topology_changes', 'time_of_last_topology_change'], name, value)


        class Interfaces(Entity):
            """
            List of interfaces on which STP is enable
            
            .. attribute:: interface
            
            	List of interfaces on which STP is enable
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpDetails.StpDetail.Interfaces.Interface>`
            
            

            """

            _prefix = 'stp-ios-xe-oper'
            _revision = '2017-08-10'

            def __init__(self):
                super(StpDetails.StpDetail.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "stp-detail"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", StpDetails.StpDetail.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(StpDetails.StpDetail.Interfaces, [], name, value)


            class Interface(Entity):
                """
                List of interfaces on which STP is enable
                
                .. attribute:: name  (key)
                
                	Reference to the STP ethernet interface
                	**type**\: str
                
                .. attribute:: cost
                
                	The port's contribution, when it is the Root Port, to the Root Path Cost for the Bridge
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: port_priority
                
                	The manageable component of the Port Identifier, also known as the Port Priority
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: port_num
                
                	The port number of the bridge port
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: role
                
                	The current role of the bridge port
                	**type**\:  :py:class:`StpPortRole <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpPortRole>`
                
                .. attribute:: state
                
                	The current state of the bridge port
                	**type**\:  :py:class:`StpPortState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpPortState>`
                
                .. attribute:: designated_root_priority
                
                	The bridge priority of the bridge recorded as the root in the configuration BPDUs transmitted by the designated bridge for the segment to which the port is attached
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: designated_root_address
                
                	The bridge address of the bridge recorded as the root in the configuration BPDUs transmitted by the designated bridge for the segment to which the port is attached
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: designated_cost
                
                	The path cost of the Designated Port of the segment connected to this port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: designated_bridge_priority
                
                	The bridge priority of the bridge that this port considers to be the designated bridge for this port's segment
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: designated_bridge_address
                
                	The bridge address of the bridge that this port considers to be the designated bridge for this port's segment
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: designated_port_priority
                
                	The Port priority of the port on the Designated Bridge for this port's segment, two octet string
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: designated_port_num
                
                	The Port number of the port on the Designated Bridge for this port's segment, two octet string
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: forward_transitions
                
                	The number of times this port has transitioned from the Learning state to the Forwarding state
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: link_type
                
                	Interface's link type
                	**type**\:  :py:class:`StpLinkRole <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpLinkRole>`
                
                .. attribute:: guard
                
                	Interface's spanning tree guard mode
                	**type**\:  :py:class:`StpPortGuard <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpPortGuard>`
                
                .. attribute:: bpdu_guard
                
                	BPDU guard on this interface
                	**type**\:  :py:class:`StpPortBpduguard <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpPortBpduguard>`
                
                .. attribute:: bpdu_filter
                
                	BPDU filter on this interface
                	**type**\:  :py:class:`StpPortBpdufilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpPortBpdufilter>`
                
                .. attribute:: bpdu_sent
                
                	The number of BPDU packet sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bpdu_received
                
                	The number of BPDU packet received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'stp-ios-xe-oper'
                _revision = '2017-08-10'

                def __init__(self):
                    super(StpDetails.StpDetail.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('cost', YLeaf(YType.uint64, 'cost')),
                        ('port_priority', YLeaf(YType.uint16, 'port-priority')),
                        ('port_num', YLeaf(YType.uint16, 'port-num')),
                        ('role', YLeaf(YType.enumeration, 'role')),
                        ('state', YLeaf(YType.enumeration, 'state')),
                        ('designated_root_priority', YLeaf(YType.uint32, 'designated-root-priority')),
                        ('designated_root_address', YLeaf(YType.str, 'designated-root-address')),
                        ('designated_cost', YLeaf(YType.uint32, 'designated-cost')),
                        ('designated_bridge_priority', YLeaf(YType.uint32, 'designated-bridge-priority')),
                        ('designated_bridge_address', YLeaf(YType.str, 'designated-bridge-address')),
                        ('designated_port_priority', YLeaf(YType.uint16, 'designated-port-priority')),
                        ('designated_port_num', YLeaf(YType.uint16, 'designated-port-num')),
                        ('forward_transitions', YLeaf(YType.uint64, 'forward-transitions')),
                        ('link_type', YLeaf(YType.enumeration, 'link-type')),
                        ('guard', YLeaf(YType.enumeration, 'guard')),
                        ('bpdu_guard', YLeaf(YType.enumeration, 'bpdu-guard')),
                        ('bpdu_filter', YLeaf(YType.enumeration, 'bpdu-filter')),
                        ('bpdu_sent', YLeaf(YType.uint64, 'bpdu-sent')),
                        ('bpdu_received', YLeaf(YType.uint64, 'bpdu-received')),
                    ])
                    self.name = None
                    self.cost = None
                    self.port_priority = None
                    self.port_num = None
                    self.role = None
                    self.state = None
                    self.designated_root_priority = None
                    self.designated_root_address = None
                    self.designated_cost = None
                    self.designated_bridge_priority = None
                    self.designated_bridge_address = None
                    self.designated_port_priority = None
                    self.designated_port_num = None
                    self.forward_transitions = None
                    self.link_type = None
                    self.guard = None
                    self.bpdu_guard = None
                    self.bpdu_filter = None
                    self.bpdu_sent = None
                    self.bpdu_received = None
                    self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(StpDetails.StpDetail.Interfaces.Interface, ['name', 'cost', 'port_priority', 'port_num', 'role', 'state', 'designated_root_priority', 'designated_root_address', 'designated_cost', 'designated_bridge_priority', 'designated_bridge_address', 'designated_port_priority', 'designated_port_num', 'forward_transitions', 'link_type', 'guard', 'bpdu_guard', 'bpdu_filter', 'bpdu_sent', 'bpdu_received'], name, value)


    class StpGlobal(Entity):
        """
        Global state data
        
        .. attribute:: mode
        
        	Spanning tree mode enabled on the device
        	**type**\:  :py:class:`StpMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpMode>`
        
        .. attribute:: bridge_assurance
        
        	Enable STP Bridge Assurance feature
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: loop_guard
        
        	Enable loopguard by default
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: bpdu_guard
        
        	Enable portfast bpdu guard
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: bpdu_filter
        
        	Enable portfast bpdu filter
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: etherchannel_misconfig_guard
        
        	Enable guard to protect against etherchannel misconfiguration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: mst_only
        
        	Global state for MST ONLY
        	**type**\:  :py:class:`MstOnly <ydk.models.cisco_ios_xe.Cisco_IOS_XE_spanning_tree_oper.StpDetails.StpGlobal.MstOnly>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'stp-ios-xe-oper'
        _revision = '2017-08-10'

        def __init__(self):
            super(StpDetails.StpGlobal, self).__init__()

            self.yang_name = "stp-global"
            self.yang_parent_name = "stp-details"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("mst-only", ("mst_only", StpDetails.StpGlobal.MstOnly))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('mode', YLeaf(YType.enumeration, 'mode')),
                ('bridge_assurance', YLeaf(YType.empty, 'bridge-assurance')),
                ('loop_guard', YLeaf(YType.empty, 'loop-guard')),
                ('bpdu_guard', YLeaf(YType.empty, 'bpdu-guard')),
                ('bpdu_filter', YLeaf(YType.empty, 'bpdu-filter')),
                ('etherchannel_misconfig_guard', YLeaf(YType.empty, 'etherchannel-misconfig-guard')),
            ])
            self.mode = None
            self.bridge_assurance = None
            self.loop_guard = None
            self.bpdu_guard = None
            self.bpdu_filter = None
            self.etherchannel_misconfig_guard = None

            self.mst_only = StpDetails.StpGlobal.MstOnly()
            self.mst_only.parent = self
            self._children_name_map["mst_only"] = "mst-only"
            self._children_yang_names.add("mst-only")
            self._segment_path = lambda: "stp-global"
            self._absolute_path = lambda: "Cisco-IOS-XE-spanning-tree-oper:stp-details/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StpDetails.StpGlobal, ['mode', 'bridge_assurance', 'loop_guard', 'bpdu_guard', 'bpdu_filter', 'etherchannel_misconfig_guard'], name, value)


        class MstOnly(Entity):
            """
            Global state for MST ONLY
            
            .. attribute:: mst_config_revision
            
            	Configuration revision number(used by MSTP only)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mst_config_name
            
            	Configuration name(used by MSTP only)
            	**type**\: str
            
            .. attribute:: max_hops
            
            	The max hops value for the spanning tree(used by MSTP only)
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'stp-ios-xe-oper'
            _revision = '2017-08-10'

            def __init__(self):
                super(StpDetails.StpGlobal.MstOnly, self).__init__()

                self.yang_name = "mst-only"
                self.yang_parent_name = "stp-global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mst_config_revision', YLeaf(YType.uint16, 'mst-config-revision')),
                    ('mst_config_name', YLeaf(YType.str, 'mst-config-name')),
                    ('max_hops', YLeaf(YType.uint16, 'max-hops')),
                ])
                self.mst_config_revision = None
                self.mst_config_name = None
                self.max_hops = None
                self._segment_path = lambda: "mst-only"
                self._absolute_path = lambda: "Cisco-IOS-XE-spanning-tree-oper:stp-details/stp-global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(StpDetails.StpGlobal.MstOnly, ['mst_config_revision', 'mst_config_name', 'max_hops'], name, value)

    def clone_ptr(self):
        self._top_entity = StpDetails()
        return self._top_entity

