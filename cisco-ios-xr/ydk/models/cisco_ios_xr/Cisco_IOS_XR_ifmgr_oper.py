""" Cisco_IOS_XR_ifmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ifmgr package operational data.

This module contains definitions
for the following management objects\:
  interface\-dampening\: Interface dampening data
  interface\-properties\: interface properties

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



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



class InterfaceDampening(Entity):
    """
    Interface dampening data
    
    .. attribute:: interfaces
    
    	The interface list for which dampening info is available
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces>`
    
    .. attribute:: nodes
    
    	The location of the interface(s) being queried
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes>`
    
    

    """

    _prefix = 'ifmgr-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(InterfaceDampening, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-dampening"
        self.yang_parent_name = "Cisco-IOS-XR-ifmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", InterfaceDampening.Interfaces)), ("nodes", ("nodes", InterfaceDampening.Nodes))])
        self._leafs = OrderedDict()

        self.interfaces = InterfaceDampening.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.nodes = InterfaceDampening.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(InterfaceDampening, [], name, value)


    class Interfaces(Entity):
        """
        The interface list for which dampening info is
        available
        
        .. attribute:: interface
        
        	The interface for which dampening info is being queried
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceDampening.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "interface-dampening"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", InterfaceDampening.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceDampening.Interfaces, [], name, value)


        class Interface(Entity):
            """
            The interface for which dampening info is being
            queried
            
            .. attribute:: interface_name  (key)
            
            	The name of the
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: if_dampening
            
            	Dampening info for the interface
            	**type**\:  :py:class:`IfDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceDampening.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("if-dampening", ("if_dampening", InterfaceDampening.Interfaces.Interface.IfDampening))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.if_dampening = InterfaceDampening.Interfaces.Interface.IfDampening()
                self.if_dampening.parent = self
                self._children_name_map["if_dampening"] = "if-dampening"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceDampening.Interfaces.Interface, ['interface_name'], name, value)


            class IfDampening(Entity):
                """
                Dampening info for the interface
                
                .. attribute:: interface_dampening
                
                	Interface dampening
                	**type**\:  :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_>`
                
                .. attribute:: state_transition_count
                
                	The number of times the state has changed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_state_transition_time
                
                	The time elasped after the last state transition
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_dampening_enabled
                
                	Flag showing if dampening is enabled
                	**type**\: bool
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: capsulation
                
                	Dampening information for capsulations
                	**type**\: list of  		 :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceDampening.Interfaces.Interface.IfDampening, self).__init__()

                    self.yang_name = "if-dampening"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-dampening", ("interface_dampening", InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_)), ("capsulation", ("capsulation", InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation))])
                    self._leafs = OrderedDict([
                        ('state_transition_count', (YLeaf(YType.uint32, 'state-transition-count'), ['int'])),
                        ('last_state_transition_time', (YLeaf(YType.uint32, 'last-state-transition-time'), ['int'])),
                        ('is_dampening_enabled', (YLeaf(YType.boolean, 'is-dampening-enabled'), ['bool'])),
                        ('half_life', (YLeaf(YType.uint32, 'half-life'), ['int'])),
                        ('reuse_threshold', (YLeaf(YType.uint32, 'reuse-threshold'), ['int'])),
                        ('suppress_threshold', (YLeaf(YType.uint32, 'suppress-threshold'), ['int'])),
                        ('maximum_suppress_time', (YLeaf(YType.uint32, 'maximum-suppress-time'), ['int'])),
                        ('restart_penalty', (YLeaf(YType.uint32, 'restart-penalty'), ['int'])),
                    ])
                    self.state_transition_count = None
                    self.last_state_transition_time = None
                    self.is_dampening_enabled = None
                    self.half_life = None
                    self.reuse_threshold = None
                    self.suppress_threshold = None
                    self.maximum_suppress_time = None
                    self.restart_penalty = None

                    self.interface_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_()
                    self.interface_dampening.parent = self
                    self._children_name_map["interface_dampening"] = "interface-dampening"

                    self.capsulation = YList(self)
                    self._segment_path = lambda: "if-dampening"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening, ['state_transition_count', 'last_state_transition_time', 'is_dampening_enabled', 'half_life', 'reuse_threshold', 'suppress_threshold', 'maximum_suppress_time', 'restart_penalty'], name, value)


                class InterfaceDampening_(Entity):
                    """
                    Interface dampening
                    
                    .. attribute:: penalty
                    
                    	Dampening penalty of the interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_suppressed_enabled
                    
                    	Flag showing if state is suppressed
                    	**type**\: bool
                    
                    .. attribute:: seconds_remaining
                    
                    	Remaining period of suppression in secs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: flaps
                    
                    	Number of underlying state flaps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Underlying state of the node
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_, self).__init__()

                        self.yang_name = "interface-dampening"
                        self.yang_parent_name = "if-dampening"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                            ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                            ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                            ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                        ])
                        self.penalty = None
                        self.is_suppressed_enabled = None
                        self.seconds_remaining = None
                        self.flaps = None
                        self.state = None
                        self._segment_path = lambda: "interface-dampening"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)


                class Capsulation(Entity):
                    """
                    Dampening information for capsulations
                    
                    .. attribute:: capsulation_dampening
                    
                    	Capsulation dampening
                    	**type**\:  :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening>`
                    
                    .. attribute:: capsulation_number
                    
                    	Capsulation number
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, self).__init__()

                        self.yang_name = "capsulation"
                        self.yang_parent_name = "if-dampening"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("capsulation-dampening", ("capsulation_dampening", InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening))])
                        self._leafs = OrderedDict([
                            ('capsulation_number', (YLeaf(YType.str, 'capsulation-number'), ['str'])),
                        ])
                        self.capsulation_number = None

                        self.capsulation_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening()
                        self.capsulation_dampening.parent = self
                        self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                        self._segment_path = lambda: "capsulation"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, ['capsulation_number'], name, value)


                    class CapsulationDampening(Entity):
                        """
                        Capsulation dampening
                        
                        .. attribute:: penalty
                        
                        	Dampening penalty of the interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_suppressed_enabled
                        
                        	Flag showing if state is suppressed
                        	**type**\: bool
                        
                        .. attribute:: seconds_remaining
                        
                        	Remaining period of suppression in secs
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: flaps
                        
                        	Number of underlying state flaps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	Underlying state of the node
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, self).__init__()

                            self.yang_name = "capsulation-dampening"
                            self.yang_parent_name = "capsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                                ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                                ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                                ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                            ])
                            self.penalty = None
                            self.is_suppressed_enabled = None
                            self.seconds_remaining = None
                            self.flaps = None
                            self.state = None
                            self._segment_path = lambda: "capsulation-dampening"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)


    class Nodes(Entity):
        """
        The location of the interface(s) being queried
        
        .. attribute:: node
        
        	The location of the interface(s) being queried
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceDampening.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "interface-dampening"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", InterfaceDampening.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceDampening.Nodes, [], name, value)


        class Node(Entity):
            """
            The location of the interface(s) being queried
            
            .. attribute:: node_name  (key)
            
            	The location of the interface(s)
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: show
            
            	Show details for the interfaces
            	**type**\:  :py:class:`Show <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceDampening.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("show", ("show", InterfaceDampening.Nodes.Node.Show))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.show = InterfaceDampening.Nodes.Node.Show()
                self.show.parent = self
                self._children_name_map["show"] = "show"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceDampening.Nodes.Node, ['node_name'], name, value)


            class Show(Entity):
                """
                Show details for the interfaces
                
                .. attribute:: dampening
                
                	Dampening information of the interface(s) being queried
                	**type**\:  :py:class:`Dampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceDampening.Nodes.Node.Show, self).__init__()

                    self.yang_name = "show"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dampening", ("dampening", InterfaceDampening.Nodes.Node.Show.Dampening))])
                    self._leafs = OrderedDict()

                    self.dampening = InterfaceDampening.Nodes.Node.Show.Dampening()
                    self.dampening.parent = self
                    self._children_name_map["dampening"] = "dampening"
                    self._segment_path = lambda: "show"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show, [], name, value)


                class Dampening(Entity):
                    """
                    Dampening information of the interface(s)
                    being queried
                    
                    .. attribute:: if_handles
                    
                    	Interface handle for which dampening info queried
                    	**type**\:  :py:class:`IfHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles>`
                    
                    .. attribute:: interfaces
                    
                    	Table of interfaces for which dampening info can be queried
                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Nodes.Node.Show.Dampening, self).__init__()

                        self.yang_name = "dampening"
                        self.yang_parent_name = "show"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("if-handles", ("if_handles", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles)), ("interfaces", ("interfaces", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces))])
                        self._leafs = OrderedDict()

                        self.if_handles = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles()
                        self.if_handles.parent = self
                        self._children_name_map["if_handles"] = "if-handles"

                        self.interfaces = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._segment_path = lambda: "dampening"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening, [], name, value)


                    class IfHandles(Entity):
                        """
                        Interface handle for which dampening info
                        queried
                        
                        .. attribute:: if_handle
                        
                        	Dampening info for the interface handle
                        	**type**\: list of  		 :py:class:`IfHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, self).__init__()

                            self.yang_name = "if-handles"
                            self.yang_parent_name = "dampening"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("if-handle", ("if_handle", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle))])
                            self._leafs = OrderedDict()

                            self.if_handle = YList(self)
                            self._segment_path = lambda: "if-handles"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, [], name, value)


                        class IfHandle(Entity):
                            """
                            Dampening info for the interface handle
                            
                            .. attribute:: interface_handle_name  (key)
                            
                            	The interface handle
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:  :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_>`
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\: bool
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of  		 :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation>`
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, self).__init__()

                                self.yang_name = "if-handle"
                                self.yang_parent_name = "if-handles"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_handle_name']
                                self._child_classes = OrderedDict([("interface-dampening", ("interface_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_)), ("capsulation", ("capsulation", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation))])
                                self._leafs = OrderedDict([
                                    ('interface_handle_name', (YLeaf(YType.str, 'interface-handle-name'), ['str'])),
                                    ('state_transition_count', (YLeaf(YType.uint32, 'state-transition-count'), ['int'])),
                                    ('last_state_transition_time', (YLeaf(YType.uint32, 'last-state-transition-time'), ['int'])),
                                    ('is_dampening_enabled', (YLeaf(YType.boolean, 'is-dampening-enabled'), ['bool'])),
                                    ('half_life', (YLeaf(YType.uint32, 'half-life'), ['int'])),
                                    ('reuse_threshold', (YLeaf(YType.uint32, 'reuse-threshold'), ['int'])),
                                    ('suppress_threshold', (YLeaf(YType.uint32, 'suppress-threshold'), ['int'])),
                                    ('maximum_suppress_time', (YLeaf(YType.uint32, 'maximum-suppress-time'), ['int'])),
                                    ('restart_penalty', (YLeaf(YType.uint32, 'restart-penalty'), ['int'])),
                                ])
                                self.interface_handle_name = None
                                self.state_transition_count = None
                                self.last_state_transition_time = None
                                self.is_dampening_enabled = None
                                self.half_life = None
                                self.reuse_threshold = None
                                self.suppress_threshold = None
                                self.maximum_suppress_time = None
                                self.restart_penalty = None

                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_()
                                self.interface_dampening.parent = self
                                self._children_name_map["interface_dampening"] = "interface-dampening"

                                self.capsulation = YList(self)
                                self._segment_path = lambda: "if-handle" + "[interface-handle-name='" + str(self.interface_handle_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, ['interface_handle_name', 'state_transition_count', 'last_state_transition_time', 'is_dampening_enabled', 'half_life', 'reuse_threshold', 'suppress_threshold', 'maximum_suppress_time', 'restart_penalty'], name, value)


                            class InterfaceDampening_(Entity):
                                """
                                Interface dampening
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\: bool
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_, self).__init__()

                                    self.yang_name = "interface-dampening"
                                    self.yang_parent_name = "if-handle"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                                        ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                                        ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                                        ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ])
                                    self.penalty = None
                                    self.is_suppressed_enabled = None
                                    self.seconds_remaining = None
                                    self.flaps = None
                                    self.state = None
                                    self._segment_path = lambda: "interface-dampening"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)


                            class Capsulation(Entity):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:  :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, self).__init__()

                                    self.yang_name = "capsulation"
                                    self.yang_parent_name = "if-handle"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("capsulation-dampening", ("capsulation_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening))])
                                    self._leafs = OrderedDict([
                                        ('capsulation_number', (YLeaf(YType.str, 'capsulation-number'), ['str'])),
                                    ])
                                    self.capsulation_number = None

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._segment_path = lambda: "capsulation"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, ['capsulation_number'], name, value)


                                class CapsulationDampening(Entity):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\: bool
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, self).__init__()

                                        self.yang_name = "capsulation-dampening"
                                        self.yang_parent_name = "capsulation"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                                            ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                                            ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                                            ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                        ])
                                        self.penalty = None
                                        self.is_suppressed_enabled = None
                                        self.seconds_remaining = None
                                        self.flaps = None
                                        self.state = None
                                        self._segment_path = lambda: "capsulation-dampening"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)


                    class Interfaces(Entity):
                        """
                        Table of interfaces for which dampening info
                        can be queried
                        
                        .. attribute:: interface
                        
                        	Dampening info for the interface
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "dampening"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface))])
                            self._leafs = OrderedDict()

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            Dampening info for the interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	The name of the
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:  :py:class:`InterfaceDampening_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_>`
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\: bool
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of  		 :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation>`
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("interface-dampening", ("interface_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_)), ("capsulation", ("capsulation", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('state_transition_count', (YLeaf(YType.uint32, 'state-transition-count'), ['int'])),
                                    ('last_state_transition_time', (YLeaf(YType.uint32, 'last-state-transition-time'), ['int'])),
                                    ('is_dampening_enabled', (YLeaf(YType.boolean, 'is-dampening-enabled'), ['bool'])),
                                    ('half_life', (YLeaf(YType.uint32, 'half-life'), ['int'])),
                                    ('reuse_threshold', (YLeaf(YType.uint32, 'reuse-threshold'), ['int'])),
                                    ('suppress_threshold', (YLeaf(YType.uint32, 'suppress-threshold'), ['int'])),
                                    ('maximum_suppress_time', (YLeaf(YType.uint32, 'maximum-suppress-time'), ['int'])),
                                    ('restart_penalty', (YLeaf(YType.uint32, 'restart-penalty'), ['int'])),
                                ])
                                self.interface_name = None
                                self.state_transition_count = None
                                self.last_state_transition_time = None
                                self.is_dampening_enabled = None
                                self.half_life = None
                                self.reuse_threshold = None
                                self.suppress_threshold = None
                                self.maximum_suppress_time = None
                                self.restart_penalty = None

                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_()
                                self.interface_dampening.parent = self
                                self._children_name_map["interface_dampening"] = "interface-dampening"

                                self.capsulation = YList(self)
                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, ['interface_name', 'state_transition_count', 'last_state_transition_time', 'is_dampening_enabled', 'half_life', 'reuse_threshold', 'suppress_threshold', 'maximum_suppress_time', 'restart_penalty'], name, value)


                            class InterfaceDampening_(Entity):
                                """
                                Interface dampening
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\: bool
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_, self).__init__()

                                    self.yang_name = "interface-dampening"
                                    self.yang_parent_name = "interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                                        ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                                        ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                                        ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ])
                                    self.penalty = None
                                    self.is_suppressed_enabled = None
                                    self.seconds_remaining = None
                                    self.flaps = None
                                    self.state = None
                                    self._segment_path = lambda: "interface-dampening"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)


                            class Capsulation(Entity):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:  :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, self).__init__()

                                    self.yang_name = "capsulation"
                                    self.yang_parent_name = "interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("capsulation-dampening", ("capsulation_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening))])
                                    self._leafs = OrderedDict([
                                        ('capsulation_number', (YLeaf(YType.str, 'capsulation-number'), ['str'])),
                                    ])
                                    self.capsulation_number = None

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._segment_path = lambda: "capsulation"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, ['capsulation_number'], name, value)


                                class CapsulationDampening(Entity):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\: bool
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, self).__init__()

                                        self.yang_name = "capsulation-dampening"
                                        self.yang_parent_name = "capsulation"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('penalty', (YLeaf(YType.uint32, 'penalty'), ['int'])),
                                            ('is_suppressed_enabled', (YLeaf(YType.boolean, 'is-suppressed-enabled'), ['bool'])),
                                            ('seconds_remaining', (YLeaf(YType.uint32, 'seconds-remaining'), ['int'])),
                                            ('flaps', (YLeaf(YType.uint32, 'flaps'), ['int'])),
                                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                        ])
                                        self.penalty = None
                                        self.is_suppressed_enabled = None
                                        self.seconds_remaining = None
                                        self.flaps = None
                                        self.state = None
                                        self._segment_path = lambda: "capsulation-dampening"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, ['penalty', 'is_suppressed_enabled', 'seconds_remaining', 'flaps', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceDampening()
        return self._top_entity

class InterfaceProperties(Entity):
    """
    interface properties
    
    .. attribute:: data_nodes
    
    	Operational data for interfaces
    	**type**\:  :py:class:`DataNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes>`
    
    

    """

    _prefix = 'ifmgr-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(InterfaceProperties, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-properties"
        self.yang_parent_name = "Cisco-IOS-XR-ifmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("data-nodes", ("data_nodes", InterfaceProperties.DataNodes))])
        self._leafs = OrderedDict()

        self.data_nodes = InterfaceProperties.DataNodes()
        self.data_nodes.parent = self
        self._children_name_map["data_nodes"] = "data-nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(InterfaceProperties, [], name, value)


    class DataNodes(Entity):
        """
        Operational data for interfaces
        
        .. attribute:: data_node
        
        	The location of a (D)RP in the same LR as the interface being queried
        	**type**\: list of  		 :py:class:`DataNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceProperties.DataNodes, self).__init__()

            self.yang_name = "data-nodes"
            self.yang_parent_name = "interface-properties"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("data-node", ("data_node", InterfaceProperties.DataNodes.DataNode))])
            self._leafs = OrderedDict()

            self.data_node = YList(self)
            self._segment_path = lambda: "data-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceProperties.DataNodes, [], name, value)


        class DataNode(Entity):
            """
            The location of a (D)RP in the same LR as the
            interface being queried
            
            .. attribute:: data_node_name  (key)
            
            	The location of the (D)RP
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: locationviews
            
            	Location\-specific view of interface operational data
            	**type**\:  :py:class:`Locationviews <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews>`
            
            .. attribute:: pq_node_locations
            
            	Partially qualified Location\-specific view of interface operational data
            	**type**\:  :py:class:`PqNodeLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations>`
            
            .. attribute:: system_view
            
            	System\-wide view of interface operational data
            	**type**\:  :py:class:`SystemView <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceProperties.DataNodes.DataNode, self).__init__()

                self.yang_name = "data-node"
                self.yang_parent_name = "data-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['data_node_name']
                self._child_classes = OrderedDict([("locationviews", ("locationviews", InterfaceProperties.DataNodes.DataNode.Locationviews)), ("pq-node-locations", ("pq_node_locations", InterfaceProperties.DataNodes.DataNode.PqNodeLocations)), ("system-view", ("system_view", InterfaceProperties.DataNodes.DataNode.SystemView))])
                self._leafs = OrderedDict([
                    ('data_node_name', (YLeaf(YType.str, 'data-node-name'), ['str'])),
                ])
                self.data_node_name = None

                self.locationviews = InterfaceProperties.DataNodes.DataNode.Locationviews()
                self.locationviews.parent = self
                self._children_name_map["locationviews"] = "locationviews"

                self.pq_node_locations = InterfaceProperties.DataNodes.DataNode.PqNodeLocations()
                self.pq_node_locations.parent = self
                self._children_name_map["pq_node_locations"] = "pq-node-locations"

                self.system_view = InterfaceProperties.DataNodes.DataNode.SystemView()
                self.system_view.parent = self
                self._children_name_map["system_view"] = "system-view"
                self._segment_path = lambda: "data-node" + "[data-node-name='" + str(self.data_node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties/data-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceProperties.DataNodes.DataNode, ['data_node_name'], name, value)


            class Locationviews(Entity):
                """
                Location\-specific view of interface
                operational data
                
                .. attribute:: locationview
                
                	Operational data for all interfaces and controllers on a particular node
                	**type**\: list of  		 :py:class:`Locationview <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.Locationviews, self).__init__()

                    self.yang_name = "locationviews"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("locationview", ("locationview", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview))])
                    self._leafs = OrderedDict()

                    self.locationview = YList(self)
                    self._segment_path = lambda: "locationviews"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews, [], name, value)


                class Locationview(Entity):
                    """
                    Operational data for all interfaces and
                    controllers on a particular node
                    
                    .. attribute:: locationview_name  (key)
                    
                    	The location to filter on
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, self).__init__()

                        self.yang_name = "locationview"
                        self.yang_parent_name = "locationviews"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['locationview_name']
                        self._child_classes = OrderedDict([("interfaces", ("interfaces", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces))])
                        self._leafs = OrderedDict([
                            ('locationview_name', (YLeaf(YType.str, 'locationview-name'), ['str'])),
                        ])
                        self.locationview_name = None

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._segment_path = lambda: "locationview" + "[locationview-name='" + str(self.locationview_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, ['locationview_name'], name, value)


                    class Interfaces(Entity):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "locationview"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface))])
                            self._leafs = OrderedDict()

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	The name of the interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\: str
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\: str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\: str
                            
                            	**length:** 0..32
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\: bool
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('actual_state', (YLeaf(YType.enumeration, 'actual-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('actual_line_state', (YLeaf(YType.enumeration, 'actual-line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('encapsulation', (YLeaf(YType.str, 'encapsulation'), ['str'])),
                                    ('encapsulation_type_string', (YLeaf(YType.str, 'encapsulation-type-string'), ['str'])),
                                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                    ('sub_interface_mtu_overhead', (YLeaf(YType.uint32, 'sub-interface-mtu-overhead'), ['int'])),
                                    ('l2_transport', (YLeaf(YType.boolean, 'l2-transport'), ['bool'])),
                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ])
                                self.interface_name = None
                                self.interface = None
                                self.parent_interface = None
                                self.type = None
                                self.state = None
                                self.actual_state = None
                                self.line_state = None
                                self.actual_line_state = None
                                self.encapsulation = None
                                self.encapsulation_type_string = None
                                self.mtu = None
                                self.sub_interface_mtu_overhead = None
                                self.l2_transport = None
                                self.bandwidth = None
                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, ['interface_name', 'interface', 'parent_interface', 'type', 'state', 'actual_state', 'line_state', 'actual_line_state', 'encapsulation', 'encapsulation_type_string', 'mtu', 'sub_interface_mtu_overhead', 'l2_transport', 'bandwidth'], name, value)


            class PqNodeLocations(Entity):
                """
                Partially qualified Location\-specific view of
                interface operational data
                
                .. attribute:: pq_node_location
                
                	Operational data for all interfaces and controllers on a particular pq\_node
                	**type**\: list of  		 :py:class:`PqNodeLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, self).__init__()

                    self.yang_name = "pq-node-locations"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pq-node-location", ("pq_node_location", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation))])
                    self._leafs = OrderedDict()

                    self.pq_node_location = YList(self)
                    self._segment_path = lambda: "pq-node-locations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, [], name, value)


                class PqNodeLocation(Entity):
                    """
                    Operational data for all interfaces and
                    controllers on a particular pq\_node
                    
                    .. attribute:: pq_node_name  (key)
                    
                    	The partially qualified location to filter on
                    	**type**\: str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, self).__init__()

                        self.yang_name = "pq-node-location"
                        self.yang_parent_name = "pq-node-locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pq_node_name']
                        self._child_classes = OrderedDict([("interfaces", ("interfaces", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces))])
                        self._leafs = OrderedDict([
                            ('pq_node_name', (YLeaf(YType.str, 'pq-node-name'), ['str'])),
                        ])
                        self.pq_node_name = None

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._segment_path = lambda: "pq-node-location" + "[pq-node-name='" + str(self.pq_node_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, ['pq_node_name'], name, value)


                    class Interfaces(Entity):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "pq-node-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface))])
                            self._leafs = OrderedDict()

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	The name of the interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\: str
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\: str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\: str
                            
                            	**length:** 0..32
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\: bool
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('actual_state', (YLeaf(YType.enumeration, 'actual-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('actual_line_state', (YLeaf(YType.enumeration, 'actual-line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                    ('encapsulation', (YLeaf(YType.str, 'encapsulation'), ['str'])),
                                    ('encapsulation_type_string', (YLeaf(YType.str, 'encapsulation-type-string'), ['str'])),
                                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                    ('sub_interface_mtu_overhead', (YLeaf(YType.uint32, 'sub-interface-mtu-overhead'), ['int'])),
                                    ('l2_transport', (YLeaf(YType.boolean, 'l2-transport'), ['bool'])),
                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ])
                                self.interface_name = None
                                self.interface = None
                                self.parent_interface = None
                                self.type = None
                                self.state = None
                                self.actual_state = None
                                self.line_state = None
                                self.actual_line_state = None
                                self.encapsulation = None
                                self.encapsulation_type_string = None
                                self.mtu = None
                                self.sub_interface_mtu_overhead = None
                                self.l2_transport = None
                                self.bandwidth = None
                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, ['interface_name', 'interface', 'parent_interface', 'type', 'state', 'actual_state', 'line_state', 'actual_line_state', 'encapsulation', 'encapsulation_type_string', 'mtu', 'sub_interface_mtu_overhead', 'l2_transport', 'bandwidth'], name, value)


            class SystemView(Entity):
                """
                System\-wide view of interface operational data
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces and controllers
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.SystemView, self).__init__()

                    self.yang_name = "system-view"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces))])
                    self._leafs = OrderedDict()

                    self.interfaces = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "system-view"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceProperties.DataNodes.DataNode.SystemView, [], name, value)


                class Interfaces(Entity):
                    """
                    Operational data for all interfaces and
                    controllers
                    
                    .. attribute:: interface
                    
                    	The operational attributes for a particular interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "system-view"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The operational attributes for a particular
                        interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	The name of the interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: parent_interface
                        
                        	Parent Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: type
                        
                        	Interface type
                        	**type**\: str
                        
                        .. attribute:: state
                        
                        	Operational state
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: actual_state
                        
                        	Operational state with no translation of error disable or shutdown
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: line_state
                        
                        	Line protocol state
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: actual_line_state
                        
                        	Line protocol state with no translation of error disable or shutdown
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: encapsulation
                        
                        	Interface encapsulation
                        	**type**\: str
                        
                        .. attribute:: encapsulation_type_string
                        
                        	Interface encapsulation description string
                        	**type**\: str
                        
                        	**length:** 0..32
                        
                        .. attribute:: mtu
                        
                        	MTU in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: sub_interface_mtu_overhead
                        
                        	Subif MTU overhead
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l2_transport
                        
                        	L2 transport
                        	**type**\: bool
                        
                        .. attribute:: bandwidth
                        
                        	Interface bandwidth (Kb/s)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                                ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                ('actual_state', (YLeaf(YType.enumeration, 'actual-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                ('actual_line_state', (YLeaf(YType.enumeration, 'actual-line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnum', '')])),
                                ('encapsulation', (YLeaf(YType.str, 'encapsulation'), ['str'])),
                                ('encapsulation_type_string', (YLeaf(YType.str, 'encapsulation-type-string'), ['str'])),
                                ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                ('sub_interface_mtu_overhead', (YLeaf(YType.uint32, 'sub-interface-mtu-overhead'), ['int'])),
                                ('l2_transport', (YLeaf(YType.boolean, 'l2-transport'), ['bool'])),
                                ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                            ])
                            self.interface_name = None
                            self.interface = None
                            self.parent_interface = None
                            self.type = None
                            self.state = None
                            self.actual_state = None
                            self.line_state = None
                            self.actual_line_state = None
                            self.encapsulation = None
                            self.encapsulation_type_string = None
                            self.mtu = None
                            self.sub_interface_mtu_overhead = None
                            self.l2_transport = None
                            self.bandwidth = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, ['interface_name', 'interface', 'parent_interface', 'type', 'state', 'actual_state', 'line_state', 'actual_line_state', 'encapsulation', 'encapsulation_type_string', 'mtu', 'sub_interface_mtu_overhead', 'l2_transport', 'bandwidth'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceProperties()
        return self._top_entity

