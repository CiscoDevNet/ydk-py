""" Cisco_IOS_XR_ifmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ifmgr package operational data.

This module contains definitions
for the following management objects\:
  interface\-dampening\: Interface dampening data
  interface\-properties\: interface properties

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


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



class InterfaceDampening(Entity):
    """
    Interface dampening data
    
    .. attribute:: interfaces
    
    	The interface list for which dampening info is available
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces>`
    
    .. attribute:: nodes
    
    	The location of the interface(s) being queried
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes>`
    
    

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
        self._child_container_classes = {"interfaces" : ("interfaces", InterfaceDampening.Interfaces), "nodes" : ("nodes", InterfaceDampening.Nodes)}
        self._child_list_classes = {}

        self.interfaces = InterfaceDampening.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.nodes = InterfaceDampening.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening"


    class Interfaces(Entity):
        """
        The interface list for which dampening info is
        available
        
        .. attribute:: interface
        
        	The interface for which dampening info is being queried
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceDampening.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "interface-dampening"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", InterfaceDampening.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceDampening.Interfaces, [], name, value)


        class Interface(Entity):
            """
            The interface for which dampening info is being
            queried
            
            .. attribute:: interface_name  <key>
            
            	The name of the
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: if_dampening
            
            	Dampening info for the interface
            	**type**\:   :py:class:`IfDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceDampening.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"if-dampening" : ("if_dampening", InterfaceDampening.Interfaces.Interface.IfDampening)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.if_dampening = InterfaceDampening.Interfaces.Interface.IfDampening()
                self.if_dampening.parent = self
                self._children_name_map["if_dampening"] = "if-dampening"
                self._children_yang_names.add("if-dampening")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceDampening.Interfaces.Interface, ['interface_name'], name, value)


            class IfDampening(Entity):
                """
                Dampening info for the interface
                
                .. attribute:: capsulation
                
                	Dampening information for capsulations
                	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation>`
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: interface_dampening
                
                	Interface dampening
                	**type**\:   :py:class:`InterfaceDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening>`
                
                .. attribute:: is_dampening_enabled
                
                	Flag showing if dampening is enabled
                	**type**\:  bool
                
                .. attribute:: last_state_transition_time
                
                	The time elasped after the last state transition
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_transition_count
                
                	The number of times the state has changed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceDampening.Interfaces.Interface.IfDampening, self).__init__()

                    self.yang_name = "if-dampening"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interface-dampening" : ("interface_dampening", InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening)}
                    self._child_list_classes = {"capsulation" : ("capsulation", InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation)}

                    self.half_life = YLeaf(YType.uint32, "half-life")

                    self.is_dampening_enabled = YLeaf(YType.boolean, "is-dampening-enabled")

                    self.last_state_transition_time = YLeaf(YType.uint32, "last-state-transition-time")

                    self.maximum_suppress_time = YLeaf(YType.uint32, "maximum-suppress-time")

                    self.restart_penalty = YLeaf(YType.uint32, "restart-penalty")

                    self.reuse_threshold = YLeaf(YType.uint32, "reuse-threshold")

                    self.state_transition_count = YLeaf(YType.uint32, "state-transition-count")

                    self.suppress_threshold = YLeaf(YType.uint32, "suppress-threshold")

                    self.interface_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening()
                    self.interface_dampening.parent = self
                    self._children_name_map["interface_dampening"] = "interface-dampening"
                    self._children_yang_names.add("interface-dampening")

                    self.capsulation = YList(self)
                    self._segment_path = lambda: "if-dampening"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening, ['half_life', 'is_dampening_enabled', 'last_state_transition_time', 'maximum_suppress_time', 'restart_penalty', 'reuse_threshold', 'state_transition_count', 'suppress_threshold'], name, value)


                class Capsulation(Entity):
                    """
                    Dampening information for capsulations
                    
                    .. attribute:: capsulation_dampening
                    
                    	Capsulation dampening
                    	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening>`
                    
                    .. attribute:: capsulation_number
                    
                    	Capsulation number
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, self).__init__()

                        self.yang_name = "capsulation"
                        self.yang_parent_name = "if-dampening"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"capsulation-dampening" : ("capsulation_dampening", InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening)}
                        self._child_list_classes = {}

                        self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                        self.capsulation_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening()
                        self.capsulation_dampening.parent = self
                        self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                        self._children_yang_names.add("capsulation-dampening")
                        self._segment_path = lambda: "capsulation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, ['capsulation_number'], name, value)


                    class CapsulationDampening(Entity):
                        """
                        Capsulation dampening
                        
                        .. attribute:: flaps
                        
                        	Number of underlying state flaps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_suppressed_enabled
                        
                        	Flag showing if state is suppressed
                        	**type**\:  bool
                        
                        .. attribute:: penalty
                        
                        	Dampening penalty of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: seconds_remaining
                        
                        	Remaining period of suppression in secs
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: state
                        
                        	Underlying state of the node
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, self).__init__()

                            self.yang_name = "capsulation-dampening"
                            self.yang_parent_name = "capsulation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.flaps = YLeaf(YType.uint32, "flaps")

                            self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                            self.penalty = YLeaf(YType.uint32, "penalty")

                            self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                            self.state = YLeaf(YType.enumeration, "state")
                            self._segment_path = lambda: "capsulation-dampening"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)


                class InterfaceDampening(Entity):
                    """
                    Interface dampening
                    
                    .. attribute:: flaps
                    
                    	Number of underlying state flaps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_suppressed_enabled
                    
                    	Flag showing if state is suppressed
                    	**type**\:  bool
                    
                    .. attribute:: penalty
                    
                    	Dampening penalty of the interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_remaining
                    
                    	Remaining period of suppression in secs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	Underlying state of the node
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening, self).__init__()

                        self.yang_name = "interface-dampening"
                        self.yang_parent_name = "if-dampening"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.flaps = YLeaf(YType.uint32, "flaps")

                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                        self.penalty = YLeaf(YType.uint32, "penalty")

                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "interface-dampening"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)


    class Nodes(Entity):
        """
        The location of the interface(s) being queried
        
        .. attribute:: node
        
        	The location of the interface(s) being queried
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceDampening.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "interface-dampening"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", InterfaceDampening.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceDampening.Nodes, [], name, value)


        class Node(Entity):
            """
            The location of the interface(s) being queried
            
            .. attribute:: node_name  <key>
            
            	The location of the interface(s)
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: show
            
            	Show details for the interfaces
            	**type**\:   :py:class:`Show <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceDampening.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"show" : ("show", InterfaceDampening.Nodes.Node.Show)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.show = InterfaceDampening.Nodes.Node.Show()
                self.show.parent = self
                self._children_name_map["show"] = "show"
                self._children_yang_names.add("show")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-dampening/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceDampening.Nodes.Node, ['node_name'], name, value)


            class Show(Entity):
                """
                Show details for the interfaces
                
                .. attribute:: dampening
                
                	Dampening information of the interface(s) being queried
                	**type**\:   :py:class:`Dampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceDampening.Nodes.Node.Show, self).__init__()

                    self.yang_name = "show"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"dampening" : ("dampening", InterfaceDampening.Nodes.Node.Show.Dampening)}
                    self._child_list_classes = {}

                    self.dampening = InterfaceDampening.Nodes.Node.Show.Dampening()
                    self.dampening.parent = self
                    self._children_name_map["dampening"] = "dampening"
                    self._children_yang_names.add("dampening")
                    self._segment_path = lambda: "show"


                class Dampening(Entity):
                    """
                    Dampening information of the interface(s)
                    being queried
                    
                    .. attribute:: if_handles
                    
                    	Interface handle for which dampening info queried
                    	**type**\:   :py:class:`IfHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles>`
                    
                    .. attribute:: interfaces
                    
                    	Table of interfaces for which dampening info can be queried
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceDampening.Nodes.Node.Show.Dampening, self).__init__()

                        self.yang_name = "dampening"
                        self.yang_parent_name = "show"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"if-handles" : ("if_handles", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles), "interfaces" : ("interfaces", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces)}
                        self._child_list_classes = {}

                        self.if_handles = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles()
                        self.if_handles.parent = self
                        self._children_name_map["if_handles"] = "if-handles"
                        self._children_yang_names.add("if-handles")

                        self.interfaces = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")
                        self._segment_path = lambda: "dampening"


                    class IfHandles(Entity):
                        """
                        Interface handle for which dampening info
                        queried
                        
                        .. attribute:: if_handle
                        
                        	Dampening info for the interface handle
                        	**type**\: list of    :py:class:`IfHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, self).__init__()

                            self.yang_name = "if-handles"
                            self.yang_parent_name = "dampening"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"if-handle" : ("if_handle", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle)}

                            self.if_handle = YList(self)
                            self._segment_path = lambda: "if-handles"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, [], name, value)


                        class IfHandle(Entity):
                            """
                            Dampening info for the interface handle
                            
                            .. attribute:: interface_handle_name  <key>
                            
                            	The interface handle
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation>`
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:   :py:class:`InterfaceDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening>`
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\:  bool
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, self).__init__()

                                self.yang_name = "if-handle"
                                self.yang_parent_name = "if-handles"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"interface-dampening" : ("interface_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening)}
                                self._child_list_classes = {"capsulation" : ("capsulation", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation)}

                                self.interface_handle_name = YLeaf(YType.str, "interface-handle-name")

                                self.half_life = YLeaf(YType.uint32, "half-life")

                                self.is_dampening_enabled = YLeaf(YType.boolean, "is-dampening-enabled")

                                self.last_state_transition_time = YLeaf(YType.uint32, "last-state-transition-time")

                                self.maximum_suppress_time = YLeaf(YType.uint32, "maximum-suppress-time")

                                self.restart_penalty = YLeaf(YType.uint32, "restart-penalty")

                                self.reuse_threshold = YLeaf(YType.uint32, "reuse-threshold")

                                self.state_transition_count = YLeaf(YType.uint32, "state-transition-count")

                                self.suppress_threshold = YLeaf(YType.uint32, "suppress-threshold")

                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening()
                                self.interface_dampening.parent = self
                                self._children_name_map["interface_dampening"] = "interface-dampening"
                                self._children_yang_names.add("interface-dampening")

                                self.capsulation = YList(self)
                                self._segment_path = lambda: "if-handle" + "[interface-handle-name='" + self.interface_handle_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, ['interface_handle_name', 'half_life', 'is_dampening_enabled', 'last_state_transition_time', 'maximum_suppress_time', 'restart_penalty', 'reuse_threshold', 'state_transition_count', 'suppress_threshold'], name, value)


                            class Capsulation(Entity):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, self).__init__()

                                    self.yang_name = "capsulation"
                                    self.yang_parent_name = "if-handle"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"capsulation-dampening" : ("capsulation_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening)}
                                    self._child_list_classes = {}

                                    self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._children_yang_names.add("capsulation-dampening")
                                    self._segment_path = lambda: "capsulation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, ['capsulation_number'], name, value)


                                class CapsulationDampening(Entity):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\:  bool
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, self).__init__()

                                        self.yang_name = "capsulation-dampening"
                                        self.yang_parent_name = "capsulation"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flaps = YLeaf(YType.uint32, "flaps")

                                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                        self.penalty = YLeaf(YType.uint32, "penalty")

                                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                        self.state = YLeaf(YType.enumeration, "state")
                                        self._segment_path = lambda: "capsulation-dampening"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)


                            class InterfaceDampening(Entity):
                                """
                                Interface dampening
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\:  bool
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening, self).__init__()

                                    self.yang_name = "interface-dampening"
                                    self.yang_parent_name = "if-handle"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.flaps = YLeaf(YType.uint32, "flaps")

                                    self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                    self.penalty = YLeaf(YType.uint32, "penalty")

                                    self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "interface-dampening"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)


                    class Interfaces(Entity):
                        """
                        Table of interfaces for which dampening info
                        can be queried
                        
                        .. attribute:: interface
                        
                        	Dampening info for the interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "dampening"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"interface" : ("interface", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface)}

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            Dampening info for the interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: capsulation
                            
                            	Dampening information for capsulations
                            	**type**\: list of    :py:class:`Capsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation>`
                            
                            .. attribute:: half_life
                            
                            	Configured decay half life in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: interface_dampening
                            
                            	Interface dampening
                            	**type**\:   :py:class:`InterfaceDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening>`
                            
                            .. attribute:: is_dampening_enabled
                            
                            	Flag showing if dampening is enabled
                            	**type**\:  bool
                            
                            .. attribute:: last_state_transition_time
                            
                            	The time elasped after the last state transition
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: maximum_suppress_time
                            
                            	Maximum suppress time in mins
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: minute
                            
                            .. attribute:: restart_penalty
                            
                            	Configured restart penalty
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reuse_threshold
                            
                            	Configured reuse threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state_transition_count
                            
                            	The number of times the state has changed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: suppress_threshold
                            
                            	Value of suppress threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"interface-dampening" : ("interface_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening)}
                                self._child_list_classes = {"capsulation" : ("capsulation", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation)}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.half_life = YLeaf(YType.uint32, "half-life")

                                self.is_dampening_enabled = YLeaf(YType.boolean, "is-dampening-enabled")

                                self.last_state_transition_time = YLeaf(YType.uint32, "last-state-transition-time")

                                self.maximum_suppress_time = YLeaf(YType.uint32, "maximum-suppress-time")

                                self.restart_penalty = YLeaf(YType.uint32, "restart-penalty")

                                self.reuse_threshold = YLeaf(YType.uint32, "reuse-threshold")

                                self.state_transition_count = YLeaf(YType.uint32, "state-transition-count")

                                self.suppress_threshold = YLeaf(YType.uint32, "suppress-threshold")

                                self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening()
                                self.interface_dampening.parent = self
                                self._children_name_map["interface_dampening"] = "interface-dampening"
                                self._children_yang_names.add("interface-dampening")

                                self.capsulation = YList(self)
                                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, ['interface_name', 'half_life', 'is_dampening_enabled', 'last_state_transition_time', 'maximum_suppress_time', 'restart_penalty', 'reuse_threshold', 'state_transition_count', 'suppress_threshold'], name, value)


                            class Capsulation(Entity):
                                """
                                Dampening information for capsulations
                                
                                .. attribute:: capsulation_dampening
                                
                                	Capsulation dampening
                                	**type**\:   :py:class:`CapsulationDampening <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening>`
                                
                                .. attribute:: capsulation_number
                                
                                	Capsulation number
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, self).__init__()

                                    self.yang_name = "capsulation"
                                    self.yang_parent_name = "interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"capsulation-dampening" : ("capsulation_dampening", InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening)}
                                    self._child_list_classes = {}

                                    self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._children_yang_names.add("capsulation-dampening")
                                    self._segment_path = lambda: "capsulation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, ['capsulation_number'], name, value)


                                class CapsulationDampening(Entity):
                                    """
                                    Capsulation dampening
                                    
                                    .. attribute:: flaps
                                    
                                    	Number of underlying state flaps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_suppressed_enabled
                                    
                                    	Flag showing if state is suppressed
                                    	**type**\:  bool
                                    
                                    .. attribute:: penalty
                                    
                                    	Dampening penalty of the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seconds_remaining
                                    
                                    	Remaining period of suppression in secs
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: state
                                    
                                    	Underlying state of the node
                                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ifmgr-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, self).__init__()

                                        self.yang_name = "capsulation-dampening"
                                        self.yang_parent_name = "capsulation"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flaps = YLeaf(YType.uint32, "flaps")

                                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                        self.penalty = YLeaf(YType.uint32, "penalty")

                                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                        self.state = YLeaf(YType.enumeration, "state")
                                        self._segment_path = lambda: "capsulation-dampening"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)


                            class InterfaceDampening(Entity):
                                """
                                Interface dampening
                                
                                .. attribute:: flaps
                                
                                	Number of underlying state flaps
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_suppressed_enabled
                                
                                	Flag showing if state is suppressed
                                	**type**\:  bool
                                
                                .. attribute:: penalty
                                
                                	Dampening penalty of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seconds_remaining
                                
                                	Remaining period of suppression in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: state
                                
                                	Underlying state of the node
                                	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                                
                                

                                """

                                _prefix = 'ifmgr-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening, self).__init__()

                                    self.yang_name = "interface-dampening"
                                    self.yang_parent_name = "interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.flaps = YLeaf(YType.uint32, "flaps")

                                    self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                    self.penalty = YLeaf(YType.uint32, "penalty")

                                    self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                    self.state = YLeaf(YType.enumeration, "state")
                                    self._segment_path = lambda: "interface-dampening"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening, ['flaps', 'is_suppressed_enabled', 'penalty', 'seconds_remaining', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceDampening()
        return self._top_entity

class InterfaceProperties(Entity):
    """
    interface properties
    
    .. attribute:: data_nodes
    
    	Operational data for interfaces
    	**type**\:   :py:class:`DataNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes>`
    
    

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
        self._child_container_classes = {"data-nodes" : ("data_nodes", InterfaceProperties.DataNodes)}
        self._child_list_classes = {}

        self.data_nodes = InterfaceProperties.DataNodes()
        self.data_nodes.parent = self
        self._children_name_map["data_nodes"] = "data-nodes"
        self._children_yang_names.add("data-nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties"


    class DataNodes(Entity):
        """
        Operational data for interfaces
        
        .. attribute:: data_node
        
        	The location of a (D)RP in the same LR as the interface being queried
        	**type**\: list of    :py:class:`DataNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode>`
        
        

        """

        _prefix = 'ifmgr-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(InterfaceProperties.DataNodes, self).__init__()

            self.yang_name = "data-nodes"
            self.yang_parent_name = "interface-properties"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"data-node" : ("data_node", InterfaceProperties.DataNodes.DataNode)}

            self.data_node = YList(self)
            self._segment_path = lambda: "data-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceProperties.DataNodes, [], name, value)


        class DataNode(Entity):
            """
            The location of a (D)RP in the same LR as the
            interface being queried
            
            .. attribute:: data_node_name  <key>
            
            	The location of the (D)RP
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: locationviews
            
            	Location\-specific view of interface operational data
            	**type**\:   :py:class:`Locationviews <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews>`
            
            .. attribute:: pq_node_locations
            
            	Partially qualified Location\-specific view of interface operational data
            	**type**\:   :py:class:`PqNodeLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations>`
            
            .. attribute:: system_view
            
            	System\-wide view of interface operational data
            	**type**\:   :py:class:`SystemView <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView>`
            
            

            """

            _prefix = 'ifmgr-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(InterfaceProperties.DataNodes.DataNode, self).__init__()

                self.yang_name = "data-node"
                self.yang_parent_name = "data-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"locationviews" : ("locationviews", InterfaceProperties.DataNodes.DataNode.Locationviews), "pq-node-locations" : ("pq_node_locations", InterfaceProperties.DataNodes.DataNode.PqNodeLocations), "system-view" : ("system_view", InterfaceProperties.DataNodes.DataNode.SystemView)}
                self._child_list_classes = {}

                self.data_node_name = YLeaf(YType.str, "data-node-name")

                self.locationviews = InterfaceProperties.DataNodes.DataNode.Locationviews()
                self.locationviews.parent = self
                self._children_name_map["locationviews"] = "locationviews"
                self._children_yang_names.add("locationviews")

                self.pq_node_locations = InterfaceProperties.DataNodes.DataNode.PqNodeLocations()
                self.pq_node_locations.parent = self
                self._children_name_map["pq_node_locations"] = "pq-node-locations"
                self._children_yang_names.add("pq-node-locations")

                self.system_view = InterfaceProperties.DataNodes.DataNode.SystemView()
                self.system_view.parent = self
                self._children_name_map["system_view"] = "system-view"
                self._children_yang_names.add("system-view")
                self._segment_path = lambda: "data-node" + "[data-node-name='" + self.data_node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ifmgr-oper:interface-properties/data-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(InterfaceProperties.DataNodes.DataNode, ['data_node_name'], name, value)


            class Locationviews(Entity):
                """
                Location\-specific view of interface
                operational data
                
                .. attribute:: locationview
                
                	Operational data for all interfaces and controllers on a particular node
                	**type**\: list of    :py:class:`Locationview <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.Locationviews, self).__init__()

                    self.yang_name = "locationviews"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"locationview" : ("locationview", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview)}

                    self.locationview = YList(self)
                    self._segment_path = lambda: "locationviews"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews, [], name, value)


                class Locationview(Entity):
                    """
                    Operational data for all interfaces and
                    controllers on a particular node
                    
                    .. attribute:: locationview_name  <key>
                    
                    	The location to filter on
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, self).__init__()

                        self.yang_name = "locationview"
                        self.yang_parent_name = "locationviews"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"interfaces" : ("interfaces", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces)}
                        self._child_list_classes = {}

                        self.locationview_name = YLeaf(YType.str, "locationview-name")

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")
                        self._segment_path = lambda: "locationview" + "[locationview-name='" + self.locationview_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, ['locationview_name'], name, value)


                    class Interfaces(Entity):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "locationview"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"interface" : ("interface", InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface)}

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\:  str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\:  bool
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.actual_line_state = YLeaf(YType.enumeration, "actual-line-state")

                                self.actual_state = YLeaf(YType.enumeration, "actual-state")

                                self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                self.encapsulation = YLeaf(YType.str, "encapsulation")

                                self.encapsulation_type_string = YLeaf(YType.str, "encapsulation-type-string")

                                self.interface = YLeaf(YType.str, "interface")

                                self.l2_transport = YLeaf(YType.boolean, "l2-transport")

                                self.line_state = YLeaf(YType.enumeration, "line-state")

                                self.mtu = YLeaf(YType.uint32, "mtu")

                                self.parent_interface = YLeaf(YType.str, "parent-interface")

                                self.state = YLeaf(YType.enumeration, "state")

                                self.sub_interface_mtu_overhead = YLeaf(YType.uint32, "sub-interface-mtu-overhead")

                                self.type = YLeaf(YType.str, "type")
                                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, ['interface_name', 'actual_line_state', 'actual_state', 'bandwidth', 'encapsulation', 'encapsulation_type_string', 'interface', 'l2_transport', 'line_state', 'mtu', 'parent_interface', 'state', 'sub_interface_mtu_overhead', 'type'], name, value)


            class PqNodeLocations(Entity):
                """
                Partially qualified Location\-specific view of
                interface operational data
                
                .. attribute:: pq_node_location
                
                	Operational data for all interfaces and controllers on a particular pq\_node
                	**type**\: list of    :py:class:`PqNodeLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, self).__init__()

                    self.yang_name = "pq-node-locations"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"pq-node-location" : ("pq_node_location", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation)}

                    self.pq_node_location = YList(self)
                    self._segment_path = lambda: "pq-node-locations"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, [], name, value)


                class PqNodeLocation(Entity):
                    """
                    Operational data for all interfaces and
                    controllers on a particular pq\_node
                    
                    .. attribute:: pq_node_name  <key>
                    
                    	The partially qualified location to filter on
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: interfaces
                    
                    	Operational data for all interfaces and controllers
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, self).__init__()

                        self.yang_name = "pq-node-location"
                        self.yang_parent_name = "pq-node-locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"interfaces" : ("interfaces", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces)}
                        self._child_list_classes = {}

                        self.pq_node_name = YLeaf(YType.str, "pq-node-name")

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")
                        self._segment_path = lambda: "pq-node-location" + "[pq-node-name='" + self.pq_node_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, ['pq_node_name'], name, value)


                    class Interfaces(Entity):
                        """
                        Operational data for all interfaces and
                        controllers
                        
                        .. attribute:: interface
                        
                        	The operational attributes for a particular interface
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "pq-node-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"interface" : ("interface", InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface)}

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: actual_line_state
                            
                            	Line protocol state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: actual_state
                            
                            	Operational state with no translation of error disable or shutdown
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: bandwidth
                            
                            	Interface bandwidth (Kb/s)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: encapsulation
                            
                            	Interface encapsulation
                            	**type**\:  str
                            
                            .. attribute:: encapsulation_type_string
                            
                            	Interface encapsulation description string
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            .. attribute:: interface
                            
                            	Interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: l2_transport
                            
                            	L2 transport
                            	**type**\:  bool
                            
                            .. attribute:: line_state
                            
                            	Line protocol state
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: mtu
                            
                            	MTU in bytes
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: parent_interface
                            
                            	Parent Interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: state
                            
                            	Operational state
                            	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                            
                            .. attribute:: sub_interface_mtu_overhead
                            
                            	Subif MTU overhead
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Interface type
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ifmgr-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.actual_line_state = YLeaf(YType.enumeration, "actual-line-state")

                                self.actual_state = YLeaf(YType.enumeration, "actual-state")

                                self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                self.encapsulation = YLeaf(YType.str, "encapsulation")

                                self.encapsulation_type_string = YLeaf(YType.str, "encapsulation-type-string")

                                self.interface = YLeaf(YType.str, "interface")

                                self.l2_transport = YLeaf(YType.boolean, "l2-transport")

                                self.line_state = YLeaf(YType.enumeration, "line-state")

                                self.mtu = YLeaf(YType.uint32, "mtu")

                                self.parent_interface = YLeaf(YType.str, "parent-interface")

                                self.state = YLeaf(YType.enumeration, "state")

                                self.sub_interface_mtu_overhead = YLeaf(YType.uint32, "sub-interface-mtu-overhead")

                                self.type = YLeaf(YType.str, "type")
                                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, ['interface_name', 'actual_line_state', 'actual_state', 'bandwidth', 'encapsulation', 'encapsulation_type_string', 'interface', 'l2_transport', 'line_state', 'mtu', 'parent_interface', 'state', 'sub_interface_mtu_overhead', 'type'], name, value)


            class SystemView(Entity):
                """
                System\-wide view of interface operational data
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces and controllers
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces>`
                
                

                """

                _prefix = 'ifmgr-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(InterfaceProperties.DataNodes.DataNode.SystemView, self).__init__()

                    self.yang_name = "system-view"
                    self.yang_parent_name = "data-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interfaces" : ("interfaces", InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces)}
                    self._child_list_classes = {}

                    self.interfaces = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")
                    self._segment_path = lambda: "system-view"


                class Interfaces(Entity):
                    """
                    Operational data for all interfaces and
                    controllers
                    
                    .. attribute:: interface
                    
                    	The operational attributes for a particular interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ifmgr-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "system-view"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The operational attributes for a particular
                        interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: actual_line_state
                        
                        	Line protocol state with no translation of error disable or shutdown
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: actual_state
                        
                        	Operational state with no translation of error disable or shutdown
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: bandwidth
                        
                        	Interface bandwidth (Kb/s)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encapsulation
                        
                        	Interface encapsulation
                        	**type**\:  str
                        
                        .. attribute:: encapsulation_type_string
                        
                        	Interface encapsulation description string
                        	**type**\:  str
                        
                        	**length:** 0..32
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: l2_transport
                        
                        	L2 transport
                        	**type**\:  bool
                        
                        .. attribute:: line_state
                        
                        	Line protocol state
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: mtu
                        
                        	MTU in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: parent_interface
                        
                        	Parent Interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: state
                        
                        	Operational state
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper.ImStateEnum>`
                        
                        .. attribute:: sub_interface_mtu_overhead
                        
                        	Subif MTU overhead
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Interface type
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ifmgr-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.actual_line_state = YLeaf(YType.enumeration, "actual-line-state")

                            self.actual_state = YLeaf(YType.enumeration, "actual-state")

                            self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                            self.encapsulation = YLeaf(YType.str, "encapsulation")

                            self.encapsulation_type_string = YLeaf(YType.str, "encapsulation-type-string")

                            self.interface = YLeaf(YType.str, "interface")

                            self.l2_transport = YLeaf(YType.boolean, "l2-transport")

                            self.line_state = YLeaf(YType.enumeration, "line-state")

                            self.mtu = YLeaf(YType.uint32, "mtu")

                            self.parent_interface = YLeaf(YType.str, "parent-interface")

                            self.state = YLeaf(YType.enumeration, "state")

                            self.sub_interface_mtu_overhead = YLeaf(YType.uint32, "sub-interface-mtu-overhead")

                            self.type = YLeaf(YType.str, "type")
                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, ['interface_name', 'actual_line_state', 'actual_state', 'bandwidth', 'encapsulation', 'encapsulation_type_string', 'interface', 'l2_transport', 'line_state', 'mtu', 'parent_interface', 'state', 'sub_interface_mtu_overhead', 'type'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceProperties()
        return self._top_entity

