""" Cisco_IOS_XR_syncc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR syncc package operational data.

This module contains definitions
for the following management objects\:
  timing\-controller\: Timing controller operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClockModes(Enum):
    """
    ClockModes

    Different clock modes

    .. data:: t1 = 0

    	T1 mode

    .. data:: e1 = 1

    	E1 mode

    .. data:: two_m = 2

    	2048M mode

    .. data:: input64k = 3

    	64kCC input

    .. data:: output6m = 4

    	6312M output

    .. data:: uti = 5

    	Universal transport interface(UTI)

    .. data:: none = 6

    	No mode is selected

    """

    t1 = Enum.YLeaf(0, "t1")

    e1 = Enum.YLeaf(1, "e1")

    two_m = Enum.YLeaf(2, "two-m")

    input64k = Enum.YLeaf(3, "input64k")

    output6m = Enum.YLeaf(4, "output6m")

    uti = Enum.YLeaf(5, "uti")

    none = Enum.YLeaf(6, "none")


class Direct(Enum):
    """
    Direct

    Direction status

    .. data:: receive_transmit = 0

    	Receive or transmit

    .. data:: transmit = 1

    	Transmit

    .. data:: receive = 2

    	Receive

    """

    receive_transmit = Enum.YLeaf(0, "receive-transmit")

    transmit = Enum.YLeaf(1, "transmit")

    receive = Enum.YLeaf(2, "receive")


class InterfaceState(Enum):
    """
    InterfaceState

    Interface state

    .. data:: up = 0

    	Up state

    .. data:: down = 1

    	Down state

    .. data:: admin_down = 2

    	Admin down state

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")

    admin_down = Enum.YLeaf(2, "admin-down")


class NodeState(Enum):
    """
    NodeState

    Different modes of a node

    .. data:: active = 1

    	Node in active mode

    .. data:: standby = 2

    	Node in standby mode

    """

    active = Enum.YLeaf(1, "active")

    standby = Enum.YLeaf(2, "standby")


class QlOption1(Enum):
    """
    QlOption1

    Quality level options

    .. data:: quality_level_none = 0

    	No value

    .. data:: o1 = 1

    	Option 1

    .. data:: o2_g1 = 2

    	Option 2 Gen 1

    .. data:: o2_g2 = 3

    	Option 2 Gen 2

    """

    quality_level_none = Enum.YLeaf(0, "quality-level-none")

    o1 = Enum.YLeaf(1, "o1")

    o2_g1 = Enum.YLeaf(2, "o2-g1")

    o2_g2 = Enum.YLeaf(3, "o2-g2")


class Smode1(Enum):
    """
    Smode1

    First mode type

    .. data:: extended_super_frame = 0

    	Extended Superframe(ESF)

    .. data:: d4 = 1

    	D4 channel unit

    .. data:: non_crc4 = 2

    	Non CRC 4 mode

    .. data:: crc4 = 3

    	CRC 4

    .. data:: submode1_none = 4

    	No mode is selected

    """

    extended_super_frame = Enum.YLeaf(0, "extended-super-frame")

    d4 = Enum.YLeaf(1, "d4")

    non_crc4 = Enum.YLeaf(2, "non-crc4")

    crc4 = Enum.YLeaf(3, "crc4")

    submode1_none = Enum.YLeaf(4, "submode1-none")


class Smode2(Enum):
    """
    Smode2

    Second mode type

    .. data:: ami_mode = 0

    	AMI

    .. data:: b8zs = 1

    	B8ZS submode

    .. data:: hdb3 = 2

    	HDB3 submode

    .. data:: submode2_none = 3

    	No mode is selected

    """

    ami_mode = Enum.YLeaf(0, "ami-mode")

    b8zs = Enum.YLeaf(1, "b8zs")

    hdb3 = Enum.YLeaf(2, "hdb3")

    submode2_none = Enum.YLeaf(3, "submode2-none")


class Source(Enum):
    """
    Source

    Syncc source type

    .. data:: invalid = 0

    	Invalid state

    .. data:: ethernet_line_interface = 1

    	Ethernet interface 

    .. data:: sonet_line_interface = 2

    	SONET interface 

    .. data:: clock_interface = 3

    	Clock interface state

    .. data:: internal = 4

    	Internal state

    """

    invalid = Enum.YLeaf(0, "invalid")

    ethernet_line_interface = Enum.YLeaf(1, "ethernet-line-interface")

    sonet_line_interface = Enum.YLeaf(2, "sonet-line-interface")

    clock_interface = Enum.YLeaf(3, "clock-interface")

    internal = Enum.YLeaf(4, "internal")


class SourceStateName(Enum):
    """
    SourceStateName

    Syncc source state name

    .. data:: not_valid = 0

    	Invalid

    .. data:: unqualified = 1

    	Unqualified state

    .. data:: available = 2

    	Available state

    .. data:: failed = 3

    	Failed state

    .. data:: unmonitored = 4

    	Unmonitored state

    .. data:: error = 5

    	Error state

    """

    not_valid = Enum.YLeaf(0, "not-valid")

    unqualified = Enum.YLeaf(1, "unqualified")

    available = Enum.YLeaf(2, "available")

    failed = Enum.YLeaf(3, "failed")

    unmonitored = Enum.YLeaf(4, "unmonitored")

    error = Enum.YLeaf(5, "error")


class SynccStates(Enum):
    """
    SynccStates

    Different syncc states

    .. data:: initializing = 0

    	Initial  state

    .. data:: running = 1

    	Running  state

    .. data:: normal = 2

    	Normal  state

    .. data:: shutdown = 3

    	Shutdown  state

    """

    initializing = Enum.YLeaf(0, "initializing")

    running = Enum.YLeaf(1, "running")

    normal = Enum.YLeaf(2, "normal")

    shutdown = Enum.YLeaf(3, "shutdown")



class TimingController(Entity):
    """
    Timing controller operational data
    
    .. attribute:: nodes
    
    	List of nodes applicable to timing controller
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes>`
    
    

    """

    _prefix = 'syncc-oper'
    _revision = '2016-06-08'

    def __init__(self):
        super(TimingController, self).__init__()
        self._top_entity = None

        self.yang_name = "timing-controller"
        self.yang_parent_name = "Cisco-IOS-XR-syncc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", TimingController.Nodes)}
        self._child_list_classes = {}

        self.nodes = TimingController.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-syncc-oper:timing-controller"


    class Nodes(Entity):
        """
        List of nodes applicable to timing controller
        
        .. attribute:: node
        
        	Syncc operational data for a single node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node>`
        
        

        """

        _prefix = 'syncc-oper'
        _revision = '2016-06-08'

        def __init__(self):
            super(TimingController.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "timing-controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", TimingController.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-syncc-oper:timing-controller/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TimingController.Nodes, [], name, value)


        class Node(Entity):
            """
            Syncc operational data for a single node
            
            .. attribute:: node_name  <key>
            
            	Node Name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: clock
            
            	Syncc clock information for a node
            	**type**\:   :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.Clock>`
            
            .. attribute:: state
            
            	Syncc state for a node
            	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.State>`
            
            .. attribute:: timing_source
            
            	Syncc timing information for a node
            	**type**\:   :py:class:`TimingSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.TimingSource>`
            
            

            """

            _prefix = 'syncc-oper'
            _revision = '2016-06-08'

            def __init__(self):
                super(TimingController.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"clock" : ("clock", TimingController.Nodes.Node.Clock), "state" : ("state", TimingController.Nodes.Node.State), "timing-source" : ("timing_source", TimingController.Nodes.Node.TimingSource)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.clock = TimingController.Nodes.Node.Clock()
                self.clock.parent = self
                self._children_name_map["clock"] = "clock"
                self._children_yang_names.add("clock")

                self.state = TimingController.Nodes.Node.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.timing_source = TimingController.Nodes.Node.TimingSource()
                self.timing_source.parent = self
                self._children_name_map["timing_source"] = "timing-source"
                self._children_yang_names.add("timing-source")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-syncc-oper:timing-controller/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TimingController.Nodes.Node, ['node_name'], name, value)


            class Clock(Entity):
                """
                Syncc clock information for a node
                
                .. attribute:: syncc_instance
                
                	List of syncc clock information 
                	**type**\: list of    :py:class:`SynccInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.Clock.SynccInstance>`
                
                

                """

                _prefix = 'syncc-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(TimingController.Nodes.Node.Clock, self).__init__()

                    self.yang_name = "clock"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"syncc-instance" : ("syncc_instance", TimingController.Nodes.Node.Clock.SynccInstance)}

                    self.syncc_instance = YList(self)
                    self._segment_path = lambda: "clock"

                def __setattr__(self, name, value):
                    self._perform_setattr(TimingController.Nodes.Node.Clock, [], name, value)


                class SynccInstance(Entity):
                    """
                    List of syncc clock information 
                    
                    .. attribute:: clock
                    
                    	Clock table for an RP
                    	**type**\: list of    :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.Clock.SynccInstance.Clock>`
                    
                    

                    """

                    _prefix = 'syncc-oper'
                    _revision = '2016-06-08'

                    def __init__(self):
                        super(TimingController.Nodes.Node.Clock.SynccInstance, self).__init__()

                        self.yang_name = "syncc-instance"
                        self.yang_parent_name = "clock"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"clock" : ("clock", TimingController.Nodes.Node.Clock.SynccInstance.Clock)}

                        self.clock = YList(self)
                        self._segment_path = lambda: "syncc-instance"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TimingController.Nodes.Node.Clock.SynccInstance, [], name, value)


                    class Clock(Entity):
                        """
                        Clock table for an RP
                        
                        .. attribute:: baudrate_port0
                        
                        	Baudrate for port 0
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baudrate_port1
                        
                        	Baudrate for port 1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baudrate_port2
                        
                        	Baudrate for port 2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baudrate_port3
                        
                        	Baudrate for port 3
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: direction_port0
                        
                        	Direction of interface for port 0
                        	**type**\:   :py:class:`Direct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Direct>`
                        
                        .. attribute:: direction_port1
                        
                        	Direction of interface for port 1
                        	**type**\:   :py:class:`Direct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Direct>`
                        
                        .. attribute:: direction_port2
                        
                        	Direction of interface for port 2
                        	**type**\:   :py:class:`Direct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Direct>`
                        
                        .. attribute:: direction_port3
                        
                        	Direction of interface for port 3
                        	**type**\:   :py:class:`Direct <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Direct>`
                        
                        .. attribute:: interface_state_port0
                        
                        	Interface state for port 0
                        	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.InterfaceState>`
                        
                        .. attribute:: interface_state_port1
                        
                        	Interface state for port 1
                        	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.InterfaceState>`
                        
                        .. attribute:: interface_state_port2
                        
                        	Interface state for port 2
                        	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.InterfaceState>`
                        
                        .. attribute:: interface_state_port3
                        
                        	Interface state for port 3
                        	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.InterfaceState>`
                        
                        .. attribute:: is_configured_port0
                        
                        	True if clock is configured for port 0
                        	**type**\:  bool
                        
                        .. attribute:: is_configured_port1
                        
                        	True if clock is configured for port 1
                        	**type**\:  bool
                        
                        .. attribute:: is_configured_port2
                        
                        	True if clock is configured for port 2
                        	**type**\:  bool
                        
                        .. attribute:: is_configured_port3
                        
                        	True if clock is configured for port 3
                        	**type**\:  bool
                        
                        .. attribute:: mode_port0
                        
                        	Clock setting mode for port 0
                        	**type**\:   :py:class:`ClockModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.ClockModes>`
                        
                        .. attribute:: mode_port1
                        
                        	Clock setting mode for port 1
                        	**type**\:   :py:class:`ClockModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.ClockModes>`
                        
                        .. attribute:: mode_port2
                        
                        	Clock setting mode for port 2
                        	**type**\:   :py:class:`ClockModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.ClockModes>`
                        
                        .. attribute:: mode_port3
                        
                        	Clock setting mode for port 3
                        	**type**\:   :py:class:`ClockModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.ClockModes>`
                        
                        .. attribute:: quality_option_port0
                        
                        	Quality Level option of port 0
                        	**type**\:   :py:class:`QlOption1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.QlOption1>`
                        
                        .. attribute:: quality_option_port1
                        
                        	Quality Level option of the port 1
                        	**type**\:   :py:class:`QlOption1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.QlOption1>`
                        
                        .. attribute:: quality_option_port2
                        
                        	Quality Level option of the port 2
                        	**type**\:   :py:class:`QlOption1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.QlOption1>`
                        
                        .. attribute:: quality_option_port3
                        
                        	Quality Level option of the port 3
                        	**type**\:   :py:class:`QlOption1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.QlOption1>`
                        
                        .. attribute:: recieve_ssm_port0
                        
                        	Receive SSM for port 0
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recieve_ssm_port1
                        
                        	Receive SSM for port 1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recieve_ssm_port2
                        
                        	Receive SSM for port 2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recieve_ssm_port3
                        
                        	Receive SSM for port 3
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: shutdown_port0
                        
                        	Configure disable value for port 0
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: shutdown_port1
                        
                        	Configure disable value for port 1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: shutdown_port2
                        
                        	Configure disable value for port 2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: shutdown_port3
                        
                        	Configure disable value for port 3
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: submode1_port0
                        
                        	First submode for port 0
                        	**type**\:   :py:class:`Smode1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode1>`
                        
                        .. attribute:: submode1_port1
                        
                        	First submode for port 1
                        	**type**\:   :py:class:`Smode1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode1>`
                        
                        .. attribute:: submode1_port2
                        
                        	First submode for port 2
                        	**type**\:   :py:class:`Smode1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode1>`
                        
                        .. attribute:: submode1_port3
                        
                        	First submode for port 3
                        	**type**\:   :py:class:`Smode1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode1>`
                        
                        .. attribute:: submode2_port0
                        
                        	Second submode for port 0
                        	**type**\:   :py:class:`Smode2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode2>`
                        
                        .. attribute:: submode2_port1
                        
                        	Second submode for port 1
                        	**type**\:   :py:class:`Smode2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode2>`
                        
                        .. attribute:: submode2_port2
                        
                        	Second submode for port 2
                        	**type**\:   :py:class:`Smode2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode2>`
                        
                        .. attribute:: submode2_port3
                        
                        	Second submode for port 3
                        	**type**\:   :py:class:`Smode2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Smode2>`
                        
                        .. attribute:: submode3_port0
                        
                        	Third submode for port 0
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: submode3_port1
                        
                        	Third submode for port 1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: submode3_port2
                        
                        	Third submode for port 2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: submode3_port3
                        
                        	Third submode for port 3
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit_ssm_port0
                        
                        	Transmit SSM for port 0
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit_ssm_port1
                        
                        	Transmit SSM for port 1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit_ssm_port2
                        
                        	Transmit SSM for port 2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit_ssm_port3
                        
                        	Transmit SSM for port 3
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'syncc-oper'
                        _revision = '2016-06-08'

                        def __init__(self):
                            super(TimingController.Nodes.Node.Clock.SynccInstance.Clock, self).__init__()

                            self.yang_name = "clock"
                            self.yang_parent_name = "syncc-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.baudrate_port0 = YLeaf(YType.uint32, "baudrate-port0")

                            self.baudrate_port1 = YLeaf(YType.uint32, "baudrate-port1")

                            self.baudrate_port2 = YLeaf(YType.uint32, "baudrate-port2")

                            self.baudrate_port3 = YLeaf(YType.uint32, "baudrate-port3")

                            self.direction_port0 = YLeaf(YType.enumeration, "direction-port0")

                            self.direction_port1 = YLeaf(YType.enumeration, "direction-port1")

                            self.direction_port2 = YLeaf(YType.enumeration, "direction-port2")

                            self.direction_port3 = YLeaf(YType.enumeration, "direction-port3")

                            self.interface_state_port0 = YLeaf(YType.enumeration, "interface-state-port0")

                            self.interface_state_port1 = YLeaf(YType.enumeration, "interface-state-port1")

                            self.interface_state_port2 = YLeaf(YType.enumeration, "interface-state-port2")

                            self.interface_state_port3 = YLeaf(YType.enumeration, "interface-state-port3")

                            self.is_configured_port0 = YLeaf(YType.boolean, "is-configured-port0")

                            self.is_configured_port1 = YLeaf(YType.boolean, "is-configured-port1")

                            self.is_configured_port2 = YLeaf(YType.boolean, "is-configured-port2")

                            self.is_configured_port3 = YLeaf(YType.boolean, "is-configured-port3")

                            self.mode_port0 = YLeaf(YType.enumeration, "mode-port0")

                            self.mode_port1 = YLeaf(YType.enumeration, "mode-port1")

                            self.mode_port2 = YLeaf(YType.enumeration, "mode-port2")

                            self.mode_port3 = YLeaf(YType.enumeration, "mode-port3")

                            self.quality_option_port0 = YLeaf(YType.enumeration, "quality-option-port0")

                            self.quality_option_port1 = YLeaf(YType.enumeration, "quality-option-port1")

                            self.quality_option_port2 = YLeaf(YType.enumeration, "quality-option-port2")

                            self.quality_option_port3 = YLeaf(YType.enumeration, "quality-option-port3")

                            self.recieve_ssm_port0 = YLeaf(YType.uint32, "recieve-ssm-port0")

                            self.recieve_ssm_port1 = YLeaf(YType.uint32, "recieve-ssm-port1")

                            self.recieve_ssm_port2 = YLeaf(YType.uint32, "recieve-ssm-port2")

                            self.recieve_ssm_port3 = YLeaf(YType.uint32, "recieve-ssm-port3")

                            self.shutdown_port0 = YLeaf(YType.uint32, "shutdown-port0")

                            self.shutdown_port1 = YLeaf(YType.uint32, "shutdown-port1")

                            self.shutdown_port2 = YLeaf(YType.uint32, "shutdown-port2")

                            self.shutdown_port3 = YLeaf(YType.uint32, "shutdown-port3")

                            self.submode1_port0 = YLeaf(YType.enumeration, "submode1-port0")

                            self.submode1_port1 = YLeaf(YType.enumeration, "submode1-port1")

                            self.submode1_port2 = YLeaf(YType.enumeration, "submode1-port2")

                            self.submode1_port3 = YLeaf(YType.enumeration, "submode1-port3")

                            self.submode2_port0 = YLeaf(YType.enumeration, "submode2-port0")

                            self.submode2_port1 = YLeaf(YType.enumeration, "submode2-port1")

                            self.submode2_port2 = YLeaf(YType.enumeration, "submode2-port2")

                            self.submode2_port3 = YLeaf(YType.enumeration, "submode2-port3")

                            self.submode3_port0 = YLeaf(YType.uint32, "submode3-port0")

                            self.submode3_port1 = YLeaf(YType.uint32, "submode3-port1")

                            self.submode3_port2 = YLeaf(YType.uint32, "submode3-port2")

                            self.submode3_port3 = YLeaf(YType.uint32, "submode3-port3")

                            self.transmit_ssm_port0 = YLeaf(YType.uint32, "transmit-ssm-port0")

                            self.transmit_ssm_port1 = YLeaf(YType.uint32, "transmit-ssm-port1")

                            self.transmit_ssm_port2 = YLeaf(YType.uint32, "transmit-ssm-port2")

                            self.transmit_ssm_port3 = YLeaf(YType.uint32, "transmit-ssm-port3")
                            self._segment_path = lambda: "clock"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TimingController.Nodes.Node.Clock.SynccInstance.Clock, ['baudrate_port0', 'baudrate_port1', 'baudrate_port2', 'baudrate_port3', 'direction_port0', 'direction_port1', 'direction_port2', 'direction_port3', 'interface_state_port0', 'interface_state_port1', 'interface_state_port2', 'interface_state_port3', 'is_configured_port0', 'is_configured_port1', 'is_configured_port2', 'is_configured_port3', 'mode_port0', 'mode_port1', 'mode_port2', 'mode_port3', 'quality_option_port0', 'quality_option_port1', 'quality_option_port2', 'quality_option_port3', 'recieve_ssm_port0', 'recieve_ssm_port1', 'recieve_ssm_port2', 'recieve_ssm_port3', 'shutdown_port0', 'shutdown_port1', 'shutdown_port2', 'shutdown_port3', 'submode1_port0', 'submode1_port1', 'submode1_port2', 'submode1_port3', 'submode2_port0', 'submode2_port1', 'submode2_port2', 'submode2_port3', 'submode3_port0', 'submode3_port1', 'submode3_port2', 'submode3_port3', 'transmit_ssm_port0', 'transmit_ssm_port1', 'transmit_ssm_port2', 'transmit_ssm_port3'], name, value)


            class State(Entity):
                """
                Syncc state for a node
                
                .. attribute:: syncc_instance
                
                	List of syncc states
                	**type**\: list of    :py:class:`SynccInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.State.SynccInstance>`
                
                

                """

                _prefix = 'syncc-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(TimingController.Nodes.Node.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"syncc-instance" : ("syncc_instance", TimingController.Nodes.Node.State.SynccInstance)}

                    self.syncc_instance = YList(self)
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(TimingController.Nodes.Node.State, [], name, value)


                class SynccInstance(Entity):
                    """
                    List of syncc states
                    
                    .. attribute:: capability_count
                    
                    	Interface capability count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: capability_notification
                    
                    	Value of interface capability notification
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: controller_state
                    
                    	Syncc controller state
                    	**type**\:   :py:class:`SynccStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.SynccStates>`
                    
                    .. attribute:: get_clock_count
                    
                    	Clock count number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: initial_count
                    
                    	Initial count number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_notification
                    
                    	Selects proper input result notification
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resync_notification
                    
                    	Value of resync notification
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: set_capability_count
                    
                    	Set the value of display count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: set_clock_out_count
                    
                    	Set clock count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: set_input_count
                    
                    	Set the value of input count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: set_quality_level_count
                    
                    	Value of quality level count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shutdown_count
                    
                    	Shutdown count number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_notification
                    
                    	Notification of source status
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_disable_count
                    
                    	Sync disable count number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sync_enable_count
                    
                    	Sync enable count number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syncc_node_state
                    
                    	Status of syncc node mode
                    	**type**\:   :py:class:`NodeState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.NodeState>`
                    
                    .. attribute:: verbose_level
                    
                    	Verbose level number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'syncc-oper'
                    _revision = '2016-06-08'

                    def __init__(self):
                        super(TimingController.Nodes.Node.State.SynccInstance, self).__init__()

                        self.yang_name = "syncc-instance"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.capability_count = YLeaf(YType.uint32, "capability-count")

                        self.capability_notification = YLeaf(YType.uint32, "capability-notification")

                        self.controller_state = YLeaf(YType.enumeration, "controller-state")

                        self.get_clock_count = YLeaf(YType.uint32, "get-clock-count")

                        self.initial_count = YLeaf(YType.uint32, "initial-count")

                        self.input_notification = YLeaf(YType.uint32, "input-notification")

                        self.resync_notification = YLeaf(YType.uint32, "resync-notification")

                        self.set_capability_count = YLeaf(YType.uint32, "set-capability-count")

                        self.set_clock_out_count = YLeaf(YType.uint32, "set-clock-out-count")

                        self.set_input_count = YLeaf(YType.uint32, "set-input-count")

                        self.set_quality_level_count = YLeaf(YType.uint32, "set-quality-level-count")

                        self.shutdown_count = YLeaf(YType.uint32, "shutdown-count")

                        self.status_notification = YLeaf(YType.uint32, "status-notification")

                        self.sync_disable_count = YLeaf(YType.uint32, "sync-disable-count")

                        self.sync_enable_count = YLeaf(YType.uint32, "sync-enable-count")

                        self.syncc_node_state = YLeaf(YType.enumeration, "syncc-node-state")

                        self.verbose_level = YLeaf(YType.uint32, "verbose-level")
                        self._segment_path = lambda: "syncc-instance"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TimingController.Nodes.Node.State.SynccInstance, ['capability_count', 'capability_notification', 'controller_state', 'get_clock_count', 'initial_count', 'input_notification', 'resync_notification', 'set_capability_count', 'set_clock_out_count', 'set_input_count', 'set_quality_level_count', 'shutdown_count', 'status_notification', 'sync_disable_count', 'sync_enable_count', 'syncc_node_state', 'verbose_level'], name, value)


            class TimingSource(Entity):
                """
                Syncc timing information for a node
                
                .. attribute:: syncc_instance
                
                	List of syncc timing table information
                	**type**\: list of    :py:class:`SynccInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.TimingSource.SynccInstance>`
                
                

                """

                _prefix = 'syncc-oper'
                _revision = '2016-06-08'

                def __init__(self):
                    super(TimingController.Nodes.Node.TimingSource, self).__init__()

                    self.yang_name = "timing-source"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"syncc-instance" : ("syncc_instance", TimingController.Nodes.Node.TimingSource.SynccInstance)}

                    self.syncc_instance = YList(self)
                    self._segment_path = lambda: "timing-source"

                def __setattr__(self, name, value):
                    self._perform_setattr(TimingController.Nodes.Node.TimingSource, [], name, value)


                class SynccInstance(Entity):
                    """
                    List of syncc timing table information
                    
                    .. attribute:: timing_status1588
                    
                    	Scheduling PLL 1588 
                    	**type**\: list of    :py:class:`TimingStatus1588 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatus1588>`
                    
                    .. attribute:: timing_status_t0
                    
                    	Scheduling PLL T0 
                    	**type**\: list of    :py:class:`TimingStatusT0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT0>`
                    
                    .. attribute:: timing_status_t4
                    
                    	Scheduling PLL T4 
                    	**type**\: list of    :py:class:`TimingStatusT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT4>`
                    
                    

                    """

                    _prefix = 'syncc-oper'
                    _revision = '2016-06-08'

                    def __init__(self):
                        super(TimingController.Nodes.Node.TimingSource.SynccInstance, self).__init__()

                        self.yang_name = "syncc-instance"
                        self.yang_parent_name = "timing-source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"timing-status1588" : ("timing_status1588", TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatus1588), "timing-status-t0" : ("timing_status_t0", TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT0), "timing-status-t4" : ("timing_status_t4", TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT4)}

                        self.timing_status1588 = YList(self)
                        self.timing_status_t0 = YList(self)
                        self.timing_status_t4 = YList(self)
                        self._segment_path = lambda: "syncc-instance"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TimingController.Nodes.Node.TimingSource.SynccInstance, [], name, value)


                    class TimingStatus1588(Entity):
                        """
                        Scheduling PLL 1588 
                        
                        .. attribute:: clock_source
                        
                        	Status of syncc source type
                        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Source>`
                        
                        .. attribute:: clock_state
                        
                        	Status of clock state
                        	**type**\:   :py:class:`SourceStateName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.SourceStateName>`
                        
                        .. attribute:: input
                        
                        	Input number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_select
                        
                        	True if selected
                        	**type**\:  bool
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_option
                        
                        	Quality level option
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_value
                        
                        	Quality level value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rank
                        
                        	Rank of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: slot
                        
                        	Slot number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: user_priority
                        
                        	User priority of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'syncc-oper'
                        _revision = '2016-06-08'

                        def __init__(self):
                            super(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatus1588, self).__init__()

                            self.yang_name = "timing-status1588"
                            self.yang_parent_name = "syncc-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clock_source = YLeaf(YType.enumeration, "clock-source")

                            self.clock_state = YLeaf(YType.enumeration, "clock-state")

                            self.input = YLeaf(YType.uint8, "input")

                            self.is_select = YLeaf(YType.boolean, "is-select")

                            self.port = YLeaf(YType.uint8, "port")

                            self.quality_level_option = YLeaf(YType.uint8, "quality-level-option")

                            self.quality_level_value = YLeaf(YType.uint8, "quality-level-value")

                            self.rank = YLeaf(YType.uint8, "rank")

                            self.slot = YLeaf(YType.uint8, "slot")

                            self.user_priority = YLeaf(YType.uint8, "user-priority")
                            self._segment_path = lambda: "timing-status1588"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatus1588, ['clock_source', 'clock_state', 'input', 'is_select', 'port', 'quality_level_option', 'quality_level_value', 'rank', 'slot', 'user_priority'], name, value)


                    class TimingStatusT0(Entity):
                        """
                        Scheduling PLL T0 
                        
                        .. attribute:: clock_source
                        
                        	Status of syncc source type
                        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Source>`
                        
                        .. attribute:: clock_state
                        
                        	Status of clock state
                        	**type**\:   :py:class:`SourceStateName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.SourceStateName>`
                        
                        .. attribute:: input
                        
                        	Input number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_select
                        
                        	True if selected
                        	**type**\:  bool
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_option
                        
                        	Quality level option
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_value
                        
                        	Quality level value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rank
                        
                        	Rank of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: slot
                        
                        	Slot number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: user_priority
                        
                        	User priority of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'syncc-oper'
                        _revision = '2016-06-08'

                        def __init__(self):
                            super(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT0, self).__init__()

                            self.yang_name = "timing-status-t0"
                            self.yang_parent_name = "syncc-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clock_source = YLeaf(YType.enumeration, "clock-source")

                            self.clock_state = YLeaf(YType.enumeration, "clock-state")

                            self.input = YLeaf(YType.uint8, "input")

                            self.is_select = YLeaf(YType.boolean, "is-select")

                            self.port = YLeaf(YType.uint8, "port")

                            self.quality_level_option = YLeaf(YType.uint8, "quality-level-option")

                            self.quality_level_value = YLeaf(YType.uint8, "quality-level-value")

                            self.rank = YLeaf(YType.uint8, "rank")

                            self.slot = YLeaf(YType.uint8, "slot")

                            self.user_priority = YLeaf(YType.uint8, "user-priority")
                            self._segment_path = lambda: "timing-status-t0"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT0, ['clock_source', 'clock_state', 'input', 'is_select', 'port', 'quality_level_option', 'quality_level_value', 'rank', 'slot', 'user_priority'], name, value)


                    class TimingStatusT4(Entity):
                        """
                        Scheduling PLL T4 
                        
                        .. attribute:: clock_source
                        
                        	Status of syncc source type
                        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.Source>`
                        
                        .. attribute:: clock_state
                        
                        	Status of clock state
                        	**type**\:   :py:class:`SourceStateName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syncc_oper.SourceStateName>`
                        
                        .. attribute:: input
                        
                        	Input number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_select
                        
                        	True if selected
                        	**type**\:  bool
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_option
                        
                        	Quality level option
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: quality_level_value
                        
                        	Quality level value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rank
                        
                        	Rank of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: slot
                        
                        	Slot number
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: user_priority
                        
                        	User priority of sync timing source table
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'syncc-oper'
                        _revision = '2016-06-08'

                        def __init__(self):
                            super(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT4, self).__init__()

                            self.yang_name = "timing-status-t4"
                            self.yang_parent_name = "syncc-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.clock_source = YLeaf(YType.enumeration, "clock-source")

                            self.clock_state = YLeaf(YType.enumeration, "clock-state")

                            self.input = YLeaf(YType.uint8, "input")

                            self.is_select = YLeaf(YType.boolean, "is-select")

                            self.port = YLeaf(YType.uint8, "port")

                            self.quality_level_option = YLeaf(YType.uint8, "quality-level-option")

                            self.quality_level_value = YLeaf(YType.uint8, "quality-level-value")

                            self.rank = YLeaf(YType.uint8, "rank")

                            self.slot = YLeaf(YType.uint8, "slot")

                            self.user_priority = YLeaf(YType.uint8, "user-priority")
                            self._segment_path = lambda: "timing-status-t4"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TimingController.Nodes.Node.TimingSource.SynccInstance.TimingStatusT4, ['clock_source', 'clock_state', 'input', 'is_select', 'port', 'quality_level_option', 'quality_level_value', 'rank', 'slot', 'user_priority'], name, value)

    def clone_ptr(self):
        self._top_entity = TimingController()
        return self._top_entity

