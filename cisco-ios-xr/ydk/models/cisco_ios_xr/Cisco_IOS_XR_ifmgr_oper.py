""" Cisco_IOS_XR_ifmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ifmgr package operational data.

This module contains definitions
for the following management objects\:
  interface\-dampening\: Interface dampening data
  interface\-properties\: interface properties

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.interfaces = InterfaceDampening.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.nodes = InterfaceDampening.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


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
                        super(InterfaceDampening.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfaceDampening.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            The interface for which dampening info is being
            queried
            
            .. attribute:: interface_name  <key>
            
            	The name of the
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.if_dampening = InterfaceDampening.Interfaces.Interface.IfDampening()
                self.if_dampening.parent = self
                self._children_name_map["if_dampening"] = "if-dampening"
                self._children_yang_names.add("if-dampening")

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
                            super(InterfaceDampening.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfaceDampening.Interfaces.Interface, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("half_life",
                                    "is_dampening_enabled",
                                    "last_state_transition_time",
                                    "maximum_suppress_time",
                                    "restart_penalty",
                                    "reuse_threshold",
                                    "state_transition_count",
                                    "suppress_threshold") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfaceDampening.Interfaces.Interface.IfDampening, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfaceDampening.Interfaces.Interface.IfDampening, self).__setattr__(name, value)


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

                        self.flaps = YLeaf(YType.uint32, "flaps")

                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                        self.penalty = YLeaf(YType.uint32, "penalty")

                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("flaps",
                                        "is_suppressed_enabled",
                                        "penalty",
                                        "seconds_remaining",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.flaps.is_set or
                            self.is_suppressed_enabled.is_set or
                            self.penalty.is_set or
                            self.seconds_remaining.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.flaps.yfilter != YFilter.not_set or
                            self.is_suppressed_enabled.yfilter != YFilter.not_set or
                            self.penalty.yfilter != YFilter.not_set or
                            self.seconds_remaining.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-dampening" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flaps.get_name_leafdata())
                        if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                        if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.penalty.get_name_leafdata())
                        if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "flaps"):
                            self.flaps = value
                            self.flaps.value_namespace = name_space
                            self.flaps.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-suppressed-enabled"):
                            self.is_suppressed_enabled = value
                            self.is_suppressed_enabled.value_namespace = name_space
                            self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "penalty"):
                            self.penalty = value
                            self.penalty.value_namespace = name_space
                            self.penalty.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds-remaining"):
                            self.seconds_remaining = value
                            self.seconds_remaining.value_namespace = name_space
                            self.seconds_remaining.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix


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

                        self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                        self.capsulation_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening()
                        self.capsulation_dampening.parent = self
                        self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                        self._children_yang_names.add("capsulation-dampening")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("capsulation_number") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation, self).__setattr__(name, value)


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

                            self.flaps = YLeaf(YType.uint32, "flaps")

                            self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                            self.penalty = YLeaf(YType.uint32, "penalty")

                            self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                            self.state = YLeaf(YType.enumeration, "state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("flaps",
                                            "is_suppressed_enabled",
                                            "penalty",
                                            "seconds_remaining",
                                            "state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.flaps.is_set or
                                self.is_suppressed_enabled.is_set or
                                self.penalty.is_set or
                                self.seconds_remaining.is_set or
                                self.state.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.flaps.yfilter != YFilter.not_set or
                                self.is_suppressed_enabled.yfilter != YFilter.not_set or
                                self.penalty.yfilter != YFilter.not_set or
                                self.seconds_remaining.yfilter != YFilter.not_set or
                                self.state.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "capsulation-dampening" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flaps.get_name_leafdata())
                            if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                            if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.penalty.get_name_leafdata())
                            if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "flaps"):
                                self.flaps = value
                                self.flaps.value_namespace = name_space
                                self.flaps.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-suppressed-enabled"):
                                self.is_suppressed_enabled = value
                                self.is_suppressed_enabled.value_namespace = name_space
                                self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "penalty"):
                                self.penalty = value
                                self.penalty.value_namespace = name_space
                                self.penalty.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds-remaining"):
                                self.seconds_remaining = value
                                self.seconds_remaining.value_namespace = name_space
                                self.seconds_remaining.value_namespace_prefix = name_space_prefix
                            if(value_path == "state"):
                                self.state = value
                                self.state.value_namespace = name_space
                                self.state.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.capsulation_number.is_set or
                            (self.capsulation_dampening is not None and self.capsulation_dampening.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.capsulation_number.yfilter != YFilter.not_set or
                            (self.capsulation_dampening is not None and self.capsulation_dampening.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "capsulation" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.capsulation_number.is_set or self.capsulation_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.capsulation_number.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "capsulation-dampening"):
                            if (self.capsulation_dampening is None):
                                self.capsulation_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening()
                                self.capsulation_dampening.parent = self
                                self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                            return self.capsulation_dampening

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "capsulation-dampening" or name == "capsulation-number"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "capsulation-number"):
                            self.capsulation_number = value
                            self.capsulation_number.value_namespace = name_space
                            self.capsulation_number.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.capsulation:
                        if (c.has_data()):
                            return True
                    return (
                        self.half_life.is_set or
                        self.is_dampening_enabled.is_set or
                        self.last_state_transition_time.is_set or
                        self.maximum_suppress_time.is_set or
                        self.restart_penalty.is_set or
                        self.reuse_threshold.is_set or
                        self.state_transition_count.is_set or
                        self.suppress_threshold.is_set or
                        (self.interface_dampening is not None and self.interface_dampening.has_data()))

                def has_operation(self):
                    for c in self.capsulation:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.half_life.yfilter != YFilter.not_set or
                        self.is_dampening_enabled.yfilter != YFilter.not_set or
                        self.last_state_transition_time.yfilter != YFilter.not_set or
                        self.maximum_suppress_time.yfilter != YFilter.not_set or
                        self.restart_penalty.yfilter != YFilter.not_set or
                        self.reuse_threshold.yfilter != YFilter.not_set or
                        self.state_transition_count.yfilter != YFilter.not_set or
                        self.suppress_threshold.yfilter != YFilter.not_set or
                        (self.interface_dampening is not None and self.interface_dampening.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "if-dampening" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.half_life.is_set or self.half_life.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.half_life.get_name_leafdata())
                    if (self.is_dampening_enabled.is_set or self.is_dampening_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_dampening_enabled.get_name_leafdata())
                    if (self.last_state_transition_time.is_set or self.last_state_transition_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_state_transition_time.get_name_leafdata())
                    if (self.maximum_suppress_time.is_set or self.maximum_suppress_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_suppress_time.get_name_leafdata())
                    if (self.restart_penalty.is_set or self.restart_penalty.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.restart_penalty.get_name_leafdata())
                    if (self.reuse_threshold.is_set or self.reuse_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reuse_threshold.get_name_leafdata())
                    if (self.state_transition_count.is_set or self.state_transition_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_transition_count.get_name_leafdata())
                    if (self.suppress_threshold.is_set or self.suppress_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppress_threshold.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "capsulation"):
                        for c in self.capsulation:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.capsulation.append(c)
                        return c

                    if (child_yang_name == "interface-dampening"):
                        if (self.interface_dampening is None):
                            self.interface_dampening = InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening()
                            self.interface_dampening.parent = self
                            self._children_name_map["interface_dampening"] = "interface-dampening"
                        return self.interface_dampening

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "capsulation" or name == "interface-dampening" or name == "half-life" or name == "is-dampening-enabled" or name == "last-state-transition-time" or name == "maximum-suppress-time" or name == "restart-penalty" or name == "reuse-threshold" or name == "state-transition-count" or name == "suppress-threshold"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "half-life"):
                        self.half_life = value
                        self.half_life.value_namespace = name_space
                        self.half_life.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-dampening-enabled"):
                        self.is_dampening_enabled = value
                        self.is_dampening_enabled.value_namespace = name_space
                        self.is_dampening_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-state-transition-time"):
                        self.last_state_transition_time = value
                        self.last_state_transition_time.value_namespace = name_space
                        self.last_state_transition_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-suppress-time"):
                        self.maximum_suppress_time = value
                        self.maximum_suppress_time.value_namespace = name_space
                        self.maximum_suppress_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "restart-penalty"):
                        self.restart_penalty = value
                        self.restart_penalty.value_namespace = name_space
                        self.restart_penalty.value_namespace_prefix = name_space_prefix
                    if(value_path == "reuse-threshold"):
                        self.reuse_threshold = value
                        self.reuse_threshold.value_namespace = name_space
                        self.reuse_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-transition-count"):
                        self.state_transition_count = value
                        self.state_transition_count.value_namespace = name_space
                        self.state_transition_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppress-threshold"):
                        self.suppress_threshold = value
                        self.suppress_threshold.value_namespace = name_space
                        self.suppress_threshold.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.if_dampening is not None and self.if_dampening.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.if_dampening is not None and self.if_dampening.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-dampening/interfaces/%s" % self.get_segment_path()
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

                if (child_yang_name == "if-dampening"):
                    if (self.if_dampening is None):
                        self.if_dampening = InterfaceDampening.Interfaces.Interface.IfDampening()
                        self.if_dampening.parent = self
                        self._children_name_map["if_dampening"] = "if-dampening"
                    return self.if_dampening

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "if-dampening" or name == "interface-name"):
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
                path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self.get_segment_path()
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
                c = InterfaceDampening.Interfaces.Interface()
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
                        super(InterfaceDampening.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfaceDampening.Nodes, self).__setattr__(name, value)


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

                self.node_name = YLeaf(YType.str, "node-name")

                self.show = InterfaceDampening.Nodes.Node.Show()
                self.show.parent = self
                self._children_name_map["show"] = "show"
                self._children_yang_names.add("show")

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
                            super(InterfaceDampening.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfaceDampening.Nodes.Node, self).__setattr__(name, value)


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

                    self.dampening = InterfaceDampening.Nodes.Node.Show.Dampening()
                    self.dampening.parent = self
                    self._children_name_map["dampening"] = "dampening"
                    self._children_yang_names.add("dampening")


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

                        self.if_handles = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles()
                        self.if_handles.parent = self
                        self._children_name_map["if_handles"] = "if-handles"
                        self._children_yang_names.add("if-handles")

                        self.interfaces = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")


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

                            self.if_handle = YList(self)

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
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface_handle_name",
                                                "half_life",
                                                "is_dampening_enabled",
                                                "last_state_transition_time",
                                                "maximum_suppress_time",
                                                "restart_penalty",
                                                "reuse_threshold",
                                                "state_transition_count",
                                                "suppress_threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle, self).__setattr__(name, value)


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

                                    self.flaps = YLeaf(YType.uint32, "flaps")

                                    self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                    self.penalty = YLeaf(YType.uint32, "penalty")

                                    self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("flaps",
                                                    "is_suppressed_enabled",
                                                    "penalty",
                                                    "seconds_remaining",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.flaps.is_set or
                                        self.is_suppressed_enabled.is_set or
                                        self.penalty.is_set or
                                        self.seconds_remaining.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.flaps.yfilter != YFilter.not_set or
                                        self.is_suppressed_enabled.yfilter != YFilter.not_set or
                                        self.penalty.yfilter != YFilter.not_set or
                                        self.seconds_remaining.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interface-dampening" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flaps.get_name_leafdata())
                                    if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                                    if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.penalty.get_name_leafdata())
                                    if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "flaps"):
                                        self.flaps = value
                                        self.flaps.value_namespace = name_space
                                        self.flaps.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-suppressed-enabled"):
                                        self.is_suppressed_enabled = value
                                        self.is_suppressed_enabled.value_namespace = name_space
                                        self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "penalty"):
                                        self.penalty = value
                                        self.penalty.value_namespace = name_space
                                        self.penalty.value_namespace_prefix = name_space_prefix
                                    if(value_path == "seconds-remaining"):
                                        self.seconds_remaining = value
                                        self.seconds_remaining.value_namespace = name_space
                                        self.seconds_remaining.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix


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

                                    self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._children_yang_names.add("capsulation-dampening")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("capsulation_number") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation, self).__setattr__(name, value)


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

                                        self.flaps = YLeaf(YType.uint32, "flaps")

                                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                        self.penalty = YLeaf(YType.uint32, "penalty")

                                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                        self.state = YLeaf(YType.enumeration, "state")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("flaps",
                                                        "is_suppressed_enabled",
                                                        "penalty",
                                                        "seconds_remaining",
                                                        "state") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.flaps.is_set or
                                            self.is_suppressed_enabled.is_set or
                                            self.penalty.is_set or
                                            self.seconds_remaining.is_set or
                                            self.state.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.flaps.yfilter != YFilter.not_set or
                                            self.is_suppressed_enabled.yfilter != YFilter.not_set or
                                            self.penalty.yfilter != YFilter.not_set or
                                            self.seconds_remaining.yfilter != YFilter.not_set or
                                            self.state.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "capsulation-dampening" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flaps.get_name_leafdata())
                                        if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                                        if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.penalty.get_name_leafdata())
                                        if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.state.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "flaps"):
                                            self.flaps = value
                                            self.flaps.value_namespace = name_space
                                            self.flaps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-suppressed-enabled"):
                                            self.is_suppressed_enabled = value
                                            self.is_suppressed_enabled.value_namespace = name_space
                                            self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                                        if(value_path == "penalty"):
                                            self.penalty = value
                                            self.penalty.value_namespace = name_space
                                            self.penalty.value_namespace_prefix = name_space_prefix
                                        if(value_path == "seconds-remaining"):
                                            self.seconds_remaining = value
                                            self.seconds_remaining.value_namespace = name_space
                                            self.seconds_remaining.value_namespace_prefix = name_space_prefix
                                        if(value_path == "state"):
                                            self.state = value
                                            self.state.value_namespace = name_space
                                            self.state.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.capsulation_number.is_set or
                                        (self.capsulation_dampening is not None and self.capsulation_dampening.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.capsulation_number.yfilter != YFilter.not_set or
                                        (self.capsulation_dampening is not None and self.capsulation_dampening.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "capsulation" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.capsulation_number.is_set or self.capsulation_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.capsulation_number.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "capsulation-dampening"):
                                        if (self.capsulation_dampening is None):
                                            self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening()
                                            self.capsulation_dampening.parent = self
                                            self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                        return self.capsulation_dampening

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "capsulation-dampening" or name == "capsulation-number"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "capsulation-number"):
                                        self.capsulation_number = value
                                        self.capsulation_number.value_namespace = name_space
                                        self.capsulation_number.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.capsulation:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.interface_handle_name.is_set or
                                    self.half_life.is_set or
                                    self.is_dampening_enabled.is_set or
                                    self.last_state_transition_time.is_set or
                                    self.maximum_suppress_time.is_set or
                                    self.restart_penalty.is_set or
                                    self.reuse_threshold.is_set or
                                    self.state_transition_count.is_set or
                                    self.suppress_threshold.is_set or
                                    (self.interface_dampening is not None and self.interface_dampening.has_data()))

                            def has_operation(self):
                                for c in self.capsulation:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_handle_name.yfilter != YFilter.not_set or
                                    self.half_life.yfilter != YFilter.not_set or
                                    self.is_dampening_enabled.yfilter != YFilter.not_set or
                                    self.last_state_transition_time.yfilter != YFilter.not_set or
                                    self.maximum_suppress_time.yfilter != YFilter.not_set or
                                    self.restart_penalty.yfilter != YFilter.not_set or
                                    self.reuse_threshold.yfilter != YFilter.not_set or
                                    self.state_transition_count.yfilter != YFilter.not_set or
                                    self.suppress_threshold.yfilter != YFilter.not_set or
                                    (self.interface_dampening is not None and self.interface_dampening.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "if-handle" + "[interface-handle-name='" + self.interface_handle_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface_handle_name.is_set or self.interface_handle_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_handle_name.get_name_leafdata())
                                if (self.half_life.is_set or self.half_life.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.half_life.get_name_leafdata())
                                if (self.is_dampening_enabled.is_set or self.is_dampening_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_dampening_enabled.get_name_leafdata())
                                if (self.last_state_transition_time.is_set or self.last_state_transition_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_state_transition_time.get_name_leafdata())
                                if (self.maximum_suppress_time.is_set or self.maximum_suppress_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum_suppress_time.get_name_leafdata())
                                if (self.restart_penalty.is_set or self.restart_penalty.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.restart_penalty.get_name_leafdata())
                                if (self.reuse_threshold.is_set or self.reuse_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reuse_threshold.get_name_leafdata())
                                if (self.state_transition_count.is_set or self.state_transition_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state_transition_count.get_name_leafdata())
                                if (self.suppress_threshold.is_set or self.suppress_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "capsulation"):
                                    for c in self.capsulation:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.capsulation.append(c)
                                    return c

                                if (child_yang_name == "interface-dampening"):
                                    if (self.interface_dampening is None):
                                        self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening()
                                        self.interface_dampening.parent = self
                                        self._children_name_map["interface_dampening"] = "interface-dampening"
                                    return self.interface_dampening

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "capsulation" or name == "interface-dampening" or name == "interface-handle-name" or name == "half-life" or name == "is-dampening-enabled" or name == "last-state-transition-time" or name == "maximum-suppress-time" or name == "restart-penalty" or name == "reuse-threshold" or name == "state-transition-count" or name == "suppress-threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-handle-name"):
                                    self.interface_handle_name = value
                                    self.interface_handle_name.value_namespace = name_space
                                    self.interface_handle_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "half-life"):
                                    self.half_life = value
                                    self.half_life.value_namespace = name_space
                                    self.half_life.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-dampening-enabled"):
                                    self.is_dampening_enabled = value
                                    self.is_dampening_enabled.value_namespace = name_space
                                    self.is_dampening_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-state-transition-time"):
                                    self.last_state_transition_time = value
                                    self.last_state_transition_time.value_namespace = name_space
                                    self.last_state_transition_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum-suppress-time"):
                                    self.maximum_suppress_time = value
                                    self.maximum_suppress_time.value_namespace = name_space
                                    self.maximum_suppress_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "restart-penalty"):
                                    self.restart_penalty = value
                                    self.restart_penalty.value_namespace = name_space
                                    self.restart_penalty.value_namespace_prefix = name_space_prefix
                                if(value_path == "reuse-threshold"):
                                    self.reuse_threshold = value
                                    self.reuse_threshold.value_namespace = name_space
                                    self.reuse_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "state-transition-count"):
                                    self.state_transition_count = value
                                    self.state_transition_count.value_namespace = name_space
                                    self.state_transition_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-threshold"):
                                    self.suppress_threshold = value
                                    self.suppress_threshold.value_namespace = name_space
                                    self.suppress_threshold.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.if_handle:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.if_handle:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-handles" + path_buffer

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

                            if (child_yang_name == "if-handle"):
                                for c in self.if_handle:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.if_handle.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "if-handle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            Dampening info for the interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                                                "half_life",
                                                "is_dampening_enabled",
                                                "last_state_transition_time",
                                                "maximum_suppress_time",
                                                "restart_penalty",
                                                "reuse_threshold",
                                                "state_transition_count",
                                                "suppress_threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface, self).__setattr__(name, value)


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

                                    self.flaps = YLeaf(YType.uint32, "flaps")

                                    self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                    self.penalty = YLeaf(YType.uint32, "penalty")

                                    self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                    self.state = YLeaf(YType.enumeration, "state")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("flaps",
                                                    "is_suppressed_enabled",
                                                    "penalty",
                                                    "seconds_remaining",
                                                    "state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.flaps.is_set or
                                        self.is_suppressed_enabled.is_set or
                                        self.penalty.is_set or
                                        self.seconds_remaining.is_set or
                                        self.state.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.flaps.yfilter != YFilter.not_set or
                                        self.is_suppressed_enabled.yfilter != YFilter.not_set or
                                        self.penalty.yfilter != YFilter.not_set or
                                        self.seconds_remaining.yfilter != YFilter.not_set or
                                        self.state.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interface-dampening" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flaps.get_name_leafdata())
                                    if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                                    if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.penalty.get_name_leafdata())
                                    if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "flaps"):
                                        self.flaps = value
                                        self.flaps.value_namespace = name_space
                                        self.flaps.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-suppressed-enabled"):
                                        self.is_suppressed_enabled = value
                                        self.is_suppressed_enabled.value_namespace = name_space
                                        self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "penalty"):
                                        self.penalty = value
                                        self.penalty.value_namespace = name_space
                                        self.penalty.value_namespace_prefix = name_space_prefix
                                    if(value_path == "seconds-remaining"):
                                        self.seconds_remaining = value
                                        self.seconds_remaining.value_namespace = name_space
                                        self.seconds_remaining.value_namespace_prefix = name_space_prefix
                                    if(value_path == "state"):
                                        self.state = value
                                        self.state.value_namespace = name_space
                                        self.state.value_namespace_prefix = name_space_prefix


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

                                    self.capsulation_number = YLeaf(YType.str, "capsulation-number")

                                    self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening()
                                    self.capsulation_dampening.parent = self
                                    self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                    self._children_yang_names.add("capsulation-dampening")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("capsulation_number") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation, self).__setattr__(name, value)


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

                                        self.flaps = YLeaf(YType.uint32, "flaps")

                                        self.is_suppressed_enabled = YLeaf(YType.boolean, "is-suppressed-enabled")

                                        self.penalty = YLeaf(YType.uint32, "penalty")

                                        self.seconds_remaining = YLeaf(YType.uint32, "seconds-remaining")

                                        self.state = YLeaf(YType.enumeration, "state")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("flaps",
                                                        "is_suppressed_enabled",
                                                        "penalty",
                                                        "seconds_remaining",
                                                        "state") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.flaps.is_set or
                                            self.is_suppressed_enabled.is_set or
                                            self.penalty.is_set or
                                            self.seconds_remaining.is_set or
                                            self.state.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.flaps.yfilter != YFilter.not_set or
                                            self.is_suppressed_enabled.yfilter != YFilter.not_set or
                                            self.penalty.yfilter != YFilter.not_set or
                                            self.seconds_remaining.yfilter != YFilter.not_set or
                                            self.state.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "capsulation-dampening" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.flaps.is_set or self.flaps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.flaps.get_name_leafdata())
                                        if (self.is_suppressed_enabled.is_set or self.is_suppressed_enabled.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_suppressed_enabled.get_name_leafdata())
                                        if (self.penalty.is_set or self.penalty.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.penalty.get_name_leafdata())
                                        if (self.seconds_remaining.is_set or self.seconds_remaining.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.seconds_remaining.get_name_leafdata())
                                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.state.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "flaps" or name == "is-suppressed-enabled" or name == "penalty" or name == "seconds-remaining" or name == "state"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "flaps"):
                                            self.flaps = value
                                            self.flaps.value_namespace = name_space
                                            self.flaps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-suppressed-enabled"):
                                            self.is_suppressed_enabled = value
                                            self.is_suppressed_enabled.value_namespace = name_space
                                            self.is_suppressed_enabled.value_namespace_prefix = name_space_prefix
                                        if(value_path == "penalty"):
                                            self.penalty = value
                                            self.penalty.value_namespace = name_space
                                            self.penalty.value_namespace_prefix = name_space_prefix
                                        if(value_path == "seconds-remaining"):
                                            self.seconds_remaining = value
                                            self.seconds_remaining.value_namespace = name_space
                                            self.seconds_remaining.value_namespace_prefix = name_space_prefix
                                        if(value_path == "state"):
                                            self.state = value
                                            self.state.value_namespace = name_space
                                            self.state.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.capsulation_number.is_set or
                                        (self.capsulation_dampening is not None and self.capsulation_dampening.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.capsulation_number.yfilter != YFilter.not_set or
                                        (self.capsulation_dampening is not None and self.capsulation_dampening.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "capsulation" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.capsulation_number.is_set or self.capsulation_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.capsulation_number.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "capsulation-dampening"):
                                        if (self.capsulation_dampening is None):
                                            self.capsulation_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening()
                                            self.capsulation_dampening.parent = self
                                            self._children_name_map["capsulation_dampening"] = "capsulation-dampening"
                                        return self.capsulation_dampening

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "capsulation-dampening" or name == "capsulation-number"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "capsulation-number"):
                                        self.capsulation_number = value
                                        self.capsulation_number.value_namespace = name_space
                                        self.capsulation_number.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.capsulation:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.interface_name.is_set or
                                    self.half_life.is_set or
                                    self.is_dampening_enabled.is_set or
                                    self.last_state_transition_time.is_set or
                                    self.maximum_suppress_time.is_set or
                                    self.restart_penalty.is_set or
                                    self.reuse_threshold.is_set or
                                    self.state_transition_count.is_set or
                                    self.suppress_threshold.is_set or
                                    (self.interface_dampening is not None and self.interface_dampening.has_data()))

                            def has_operation(self):
                                for c in self.capsulation:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.half_life.yfilter != YFilter.not_set or
                                    self.is_dampening_enabled.yfilter != YFilter.not_set or
                                    self.last_state_transition_time.yfilter != YFilter.not_set or
                                    self.maximum_suppress_time.yfilter != YFilter.not_set or
                                    self.restart_penalty.yfilter != YFilter.not_set or
                                    self.reuse_threshold.yfilter != YFilter.not_set or
                                    self.state_transition_count.yfilter != YFilter.not_set or
                                    self.suppress_threshold.yfilter != YFilter.not_set or
                                    (self.interface_dampening is not None and self.interface_dampening.has_operation()))

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
                                if (self.half_life.is_set or self.half_life.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.half_life.get_name_leafdata())
                                if (self.is_dampening_enabled.is_set or self.is_dampening_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_dampening_enabled.get_name_leafdata())
                                if (self.last_state_transition_time.is_set or self.last_state_transition_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_state_transition_time.get_name_leafdata())
                                if (self.maximum_suppress_time.is_set or self.maximum_suppress_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum_suppress_time.get_name_leafdata())
                                if (self.restart_penalty.is_set or self.restart_penalty.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.restart_penalty.get_name_leafdata())
                                if (self.reuse_threshold.is_set or self.reuse_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reuse_threshold.get_name_leafdata())
                                if (self.state_transition_count.is_set or self.state_transition_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state_transition_count.get_name_leafdata())
                                if (self.suppress_threshold.is_set or self.suppress_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "capsulation"):
                                    for c in self.capsulation:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.capsulation.append(c)
                                    return c

                                if (child_yang_name == "interface-dampening"):
                                    if (self.interface_dampening is None):
                                        self.interface_dampening = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening()
                                        self.interface_dampening.parent = self
                                        self._children_name_map["interface_dampening"] = "interface-dampening"
                                    return self.interface_dampening

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "capsulation" or name == "interface-dampening" or name == "interface-name" or name == "half-life" or name == "is-dampening-enabled" or name == "last-state-transition-time" or name == "maximum-suppress-time" or name == "restart-penalty" or name == "reuse-threshold" or name == "state-transition-count" or name == "suppress-threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "half-life"):
                                    self.half_life = value
                                    self.half_life.value_namespace = name_space
                                    self.half_life.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-dampening-enabled"):
                                    self.is_dampening_enabled = value
                                    self.is_dampening_enabled.value_namespace = name_space
                                    self.is_dampening_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-state-transition-time"):
                                    self.last_state_transition_time = value
                                    self.last_state_transition_time.value_namespace = name_space
                                    self.last_state_transition_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum-suppress-time"):
                                    self.maximum_suppress_time = value
                                    self.maximum_suppress_time.value_namespace = name_space
                                    self.maximum_suppress_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "restart-penalty"):
                                    self.restart_penalty = value
                                    self.restart_penalty.value_namespace = name_space
                                    self.restart_penalty.value_namespace_prefix = name_space_prefix
                                if(value_path == "reuse-threshold"):
                                    self.reuse_threshold = value
                                    self.reuse_threshold.value_namespace = name_space
                                    self.reuse_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "state-transition-count"):
                                    self.state_transition_count = value
                                    self.state_transition_count.value_namespace = name_space
                                    self.state_transition_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-threshold"):
                                    self.suppress_threshold = value
                                    self.suppress_threshold.value_namespace = name_space
                                    self.suppress_threshold.value_namespace_prefix = name_space_prefix

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
                                c = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface()
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
                        return (
                            (self.if_handles is not None and self.if_handles.has_data()) or
                            (self.interfaces is not None and self.interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.if_handles is not None and self.if_handles.has_operation()) or
                            (self.interfaces is not None and self.interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dampening" + path_buffer

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

                        if (child_yang_name == "if-handles"):
                            if (self.if_handles is None):
                                self.if_handles = InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles()
                                self.if_handles.parent = self
                                self._children_name_map["if_handles"] = "if-handles"
                            return self.if_handles

                        if (child_yang_name == "interfaces"):
                            if (self.interfaces is None):
                                self.interfaces = InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                            return self.interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-handles" or name == "interfaces"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.dampening is not None and self.dampening.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.dampening is not None and self.dampening.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "show" + path_buffer

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

                    if (child_yang_name == "dampening"):
                        if (self.dampening is None):
                            self.dampening = InterfaceDampening.Nodes.Node.Show.Dampening()
                            self.dampening.parent = self
                            self._children_name_map["dampening"] = "dampening"
                        return self.dampening

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dampening"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.show is not None and self.show.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.show is not None and self.show.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-dampening/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "show"):
                    if (self.show is None):
                        self.show = InterfaceDampening.Nodes.Node.Show()
                        self.show.parent = self
                        self._children_name_map["show"] = "show"
                    return self.show

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "show" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-dampening/%s" % self.get_segment_path()
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
                c = InterfaceDampening.Nodes.Node()
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
        return (
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-dampening" + path_buffer

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

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = InterfaceDampening.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = InterfaceDampening.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

        self.data_nodes = InterfaceProperties.DataNodes()
        self.data_nodes.parent = self
        self._children_name_map["data_nodes"] = "data-nodes"
        self._children_yang_names.add("data-nodes")


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

            self.data_node = YList(self)

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
                        super(InterfaceProperties.DataNodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfaceProperties.DataNodes, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("data_node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InterfaceProperties.DataNodes.DataNode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfaceProperties.DataNodes.DataNode, self).__setattr__(name, value)


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

                    self.locationview = YList(self)

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
                                super(InterfaceProperties.DataNodes.DataNode.Locationviews, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfaceProperties.DataNodes.DataNode.Locationviews, self).__setattr__(name, value)


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

                        self.locationview_name = YLeaf(YType.str, "locationview-name")

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("locationview_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview, self).__setattr__(name, value)


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
                                        super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                                                "actual_line_state",
                                                "actual_state",
                                                "bandwidth",
                                                "encapsulation",
                                                "encapsulation_type_string",
                                                "interface",
                                                "l2_transport",
                                                "line_state",
                                                "mtu",
                                                "parent_interface",
                                                "state",
                                                "sub_interface_mtu_overhead",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface_name.is_set or
                                    self.actual_line_state.is_set or
                                    self.actual_state.is_set or
                                    self.bandwidth.is_set or
                                    self.encapsulation.is_set or
                                    self.encapsulation_type_string.is_set or
                                    self.interface.is_set or
                                    self.l2_transport.is_set or
                                    self.line_state.is_set or
                                    self.mtu.is_set or
                                    self.parent_interface.is_set or
                                    self.state.is_set or
                                    self.sub_interface_mtu_overhead.is_set or
                                    self.type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.actual_line_state.yfilter != YFilter.not_set or
                                    self.actual_state.yfilter != YFilter.not_set or
                                    self.bandwidth.yfilter != YFilter.not_set or
                                    self.encapsulation.yfilter != YFilter.not_set or
                                    self.encapsulation_type_string.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.l2_transport.yfilter != YFilter.not_set or
                                    self.line_state.yfilter != YFilter.not_set or
                                    self.mtu.yfilter != YFilter.not_set or
                                    self.parent_interface.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set or
                                    self.sub_interface_mtu_overhead.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set)

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
                                if (self.actual_line_state.is_set or self.actual_line_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.actual_line_state.get_name_leafdata())
                                if (self.actual_state.is_set or self.actual_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.actual_state.get_name_leafdata())
                                if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bandwidth.get_name_leafdata())
                                if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation.get_name_leafdata())
                                if (self.encapsulation_type_string.is_set or self.encapsulation_type_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation_type_string.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.l2_transport.is_set or self.l2_transport.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.l2_transport.get_name_leafdata())
                                if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_state.get_name_leafdata())
                                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mtu.get_name_leafdata())
                                if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_interface.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())
                                if (self.sub_interface_mtu_overhead.is_set or self.sub_interface_mtu_overhead.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sub_interface_mtu_overhead.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name" or name == "actual-line-state" or name == "actual-state" or name == "bandwidth" or name == "encapsulation" or name == "encapsulation-type-string" or name == "interface" or name == "l2-transport" or name == "line-state" or name == "mtu" or name == "parent-interface" or name == "state" or name == "sub-interface-mtu-overhead" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "actual-line-state"):
                                    self.actual_line_state = value
                                    self.actual_line_state.value_namespace = name_space
                                    self.actual_line_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "actual-state"):
                                    self.actual_state = value
                                    self.actual_state.value_namespace = name_space
                                    self.actual_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "bandwidth"):
                                    self.bandwidth = value
                                    self.bandwidth.value_namespace = name_space
                                    self.bandwidth.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation"):
                                    self.encapsulation = value
                                    self.encapsulation.value_namespace = name_space
                                    self.encapsulation.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation-type-string"):
                                    self.encapsulation_type_string = value
                                    self.encapsulation_type_string.value_namespace = name_space
                                    self.encapsulation_type_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "l2-transport"):
                                    self.l2_transport = value
                                    self.l2_transport.value_namespace = name_space
                                    self.l2_transport.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-state"):
                                    self.line_state = value
                                    self.line_state.value_namespace = name_space
                                    self.line_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "mtu"):
                                    self.mtu = value
                                    self.mtu.value_namespace = name_space
                                    self.mtu.value_namespace_prefix = name_space_prefix
                                if(value_path == "parent-interface"):
                                    self.parent_interface = value
                                    self.parent_interface.value_namespace = name_space
                                    self.parent_interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix
                                if(value_path == "sub-interface-mtu-overhead"):
                                    self.sub_interface_mtu_overhead = value
                                    self.sub_interface_mtu_overhead.value_namespace = name_space
                                    self.sub_interface_mtu_overhead.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

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
                                c = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface()
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
                        return (
                            self.locationview_name.is_set or
                            (self.interfaces is not None and self.interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.locationview_name.yfilter != YFilter.not_set or
                            (self.interfaces is not None and self.interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "locationview" + "[locationview-name='" + self.locationview_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.locationview_name.is_set or self.locationview_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.locationview_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interfaces"):
                            if (self.interfaces is None):
                                self.interfaces = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                            return self.interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interfaces" or name == "locationview-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "locationview-name"):
                            self.locationview_name = value
                            self.locationview_name.value_namespace = name_space
                            self.locationview_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.locationview:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.locationview:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "locationviews" + path_buffer

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

                    if (child_yang_name == "locationview"):
                        for c in self.locationview:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.locationview.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "locationview"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.pq_node_location = YList(self)

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
                                super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations, self).__setattr__(name, value)


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

                        self.pq_node_name = YLeaf(YType.str, "pq-node-name")

                        self.interfaces = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pq_node_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation, self).__setattr__(name, value)


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
                                        super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            The operational attributes for a particular
                            interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	The name of the interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                                                "actual_line_state",
                                                "actual_state",
                                                "bandwidth",
                                                "encapsulation",
                                                "encapsulation_type_string",
                                                "interface",
                                                "l2_transport",
                                                "line_state",
                                                "mtu",
                                                "parent_interface",
                                                "state",
                                                "sub_interface_mtu_overhead",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface_name.is_set or
                                    self.actual_line_state.is_set or
                                    self.actual_state.is_set or
                                    self.bandwidth.is_set or
                                    self.encapsulation.is_set or
                                    self.encapsulation_type_string.is_set or
                                    self.interface.is_set or
                                    self.l2_transport.is_set or
                                    self.line_state.is_set or
                                    self.mtu.is_set or
                                    self.parent_interface.is_set or
                                    self.state.is_set or
                                    self.sub_interface_mtu_overhead.is_set or
                                    self.type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.actual_line_state.yfilter != YFilter.not_set or
                                    self.actual_state.yfilter != YFilter.not_set or
                                    self.bandwidth.yfilter != YFilter.not_set or
                                    self.encapsulation.yfilter != YFilter.not_set or
                                    self.encapsulation_type_string.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.l2_transport.yfilter != YFilter.not_set or
                                    self.line_state.yfilter != YFilter.not_set or
                                    self.mtu.yfilter != YFilter.not_set or
                                    self.parent_interface.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set or
                                    self.sub_interface_mtu_overhead.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set)

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
                                if (self.actual_line_state.is_set or self.actual_line_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.actual_line_state.get_name_leafdata())
                                if (self.actual_state.is_set or self.actual_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.actual_state.get_name_leafdata())
                                if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bandwidth.get_name_leafdata())
                                if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation.get_name_leafdata())
                                if (self.encapsulation_type_string.is_set or self.encapsulation_type_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation_type_string.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.l2_transport.is_set or self.l2_transport.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.l2_transport.get_name_leafdata())
                                if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_state.get_name_leafdata())
                                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mtu.get_name_leafdata())
                                if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.parent_interface.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())
                                if (self.sub_interface_mtu_overhead.is_set or self.sub_interface_mtu_overhead.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sub_interface_mtu_overhead.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name" or name == "actual-line-state" or name == "actual-state" or name == "bandwidth" or name == "encapsulation" or name == "encapsulation-type-string" or name == "interface" or name == "l2-transport" or name == "line-state" or name == "mtu" or name == "parent-interface" or name == "state" or name == "sub-interface-mtu-overhead" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "actual-line-state"):
                                    self.actual_line_state = value
                                    self.actual_line_state.value_namespace = name_space
                                    self.actual_line_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "actual-state"):
                                    self.actual_state = value
                                    self.actual_state.value_namespace = name_space
                                    self.actual_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "bandwidth"):
                                    self.bandwidth = value
                                    self.bandwidth.value_namespace = name_space
                                    self.bandwidth.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation"):
                                    self.encapsulation = value
                                    self.encapsulation.value_namespace = name_space
                                    self.encapsulation.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation-type-string"):
                                    self.encapsulation_type_string = value
                                    self.encapsulation_type_string.value_namespace = name_space
                                    self.encapsulation_type_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "l2-transport"):
                                    self.l2_transport = value
                                    self.l2_transport.value_namespace = name_space
                                    self.l2_transport.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-state"):
                                    self.line_state = value
                                    self.line_state.value_namespace = name_space
                                    self.line_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "mtu"):
                                    self.mtu = value
                                    self.mtu.value_namespace = name_space
                                    self.mtu.value_namespace_prefix = name_space_prefix
                                if(value_path == "parent-interface"):
                                    self.parent_interface = value
                                    self.parent_interface.value_namespace = name_space
                                    self.parent_interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix
                                if(value_path == "sub-interface-mtu-overhead"):
                                    self.sub_interface_mtu_overhead = value
                                    self.sub_interface_mtu_overhead.value_namespace = name_space
                                    self.sub_interface_mtu_overhead.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

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
                                c = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface()
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
                        return (
                            self.pq_node_name.is_set or
                            (self.interfaces is not None and self.interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pq_node_name.yfilter != YFilter.not_set or
                            (self.interfaces is not None and self.interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pq-node-location" + "[pq-node-name='" + self.pq_node_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pq_node_name.is_set or self.pq_node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pq_node_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interfaces"):
                            if (self.interfaces is None):
                                self.interfaces = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                            return self.interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interfaces" or name == "pq-node-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pq-node-name"):
                            self.pq_node_name = value
                            self.pq_node_name.value_namespace = name_space
                            self.pq_node_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.pq_node_location:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.pq_node_location:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pq-node-locations" + path_buffer

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

                    if (child_yang_name == "pq-node-location"):
                        for c in self.pq_node_location:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pq_node_location.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pq-node-location"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.interfaces = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")


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
                                    super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        The operational attributes for a particular
                        interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
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
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
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
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
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
                                            "actual_line_state",
                                            "actual_state",
                                            "bandwidth",
                                            "encapsulation",
                                            "encapsulation_type_string",
                                            "interface",
                                            "l2_transport",
                                            "line_state",
                                            "mtu",
                                            "parent_interface",
                                            "state",
                                            "sub_interface_mtu_overhead",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.actual_line_state.is_set or
                                self.actual_state.is_set or
                                self.bandwidth.is_set or
                                self.encapsulation.is_set or
                                self.encapsulation_type_string.is_set or
                                self.interface.is_set or
                                self.l2_transport.is_set or
                                self.line_state.is_set or
                                self.mtu.is_set or
                                self.parent_interface.is_set or
                                self.state.is_set or
                                self.sub_interface_mtu_overhead.is_set or
                                self.type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.actual_line_state.yfilter != YFilter.not_set or
                                self.actual_state.yfilter != YFilter.not_set or
                                self.bandwidth.yfilter != YFilter.not_set or
                                self.encapsulation.yfilter != YFilter.not_set or
                                self.encapsulation_type_string.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.l2_transport.yfilter != YFilter.not_set or
                                self.line_state.yfilter != YFilter.not_set or
                                self.mtu.yfilter != YFilter.not_set or
                                self.parent_interface.yfilter != YFilter.not_set or
                                self.state.yfilter != YFilter.not_set or
                                self.sub_interface_mtu_overhead.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set)

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
                            if (self.actual_line_state.is_set or self.actual_line_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.actual_line_state.get_name_leafdata())
                            if (self.actual_state.is_set or self.actual_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.actual_state.get_name_leafdata())
                            if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bandwidth.get_name_leafdata())
                            if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encapsulation.get_name_leafdata())
                            if (self.encapsulation_type_string.is_set or self.encapsulation_type_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encapsulation_type_string.get_name_leafdata())
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.l2_transport.is_set or self.l2_transport.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.l2_transport.get_name_leafdata())
                            if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.line_state.get_name_leafdata())
                            if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mtu.get_name_leafdata())
                            if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.parent_interface.get_name_leafdata())
                            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.state.get_name_leafdata())
                            if (self.sub_interface_mtu_overhead.is_set or self.sub_interface_mtu_overhead.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sub_interface_mtu_overhead.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "actual-line-state" or name == "actual-state" or name == "bandwidth" or name == "encapsulation" or name == "encapsulation-type-string" or name == "interface" or name == "l2-transport" or name == "line-state" or name == "mtu" or name == "parent-interface" or name == "state" or name == "sub-interface-mtu-overhead" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "actual-line-state"):
                                self.actual_line_state = value
                                self.actual_line_state.value_namespace = name_space
                                self.actual_line_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "actual-state"):
                                self.actual_state = value
                                self.actual_state.value_namespace = name_space
                                self.actual_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "bandwidth"):
                                self.bandwidth = value
                                self.bandwidth.value_namespace = name_space
                                self.bandwidth.value_namespace_prefix = name_space_prefix
                            if(value_path == "encapsulation"):
                                self.encapsulation = value
                                self.encapsulation.value_namespace = name_space
                                self.encapsulation.value_namespace_prefix = name_space_prefix
                            if(value_path == "encapsulation-type-string"):
                                self.encapsulation_type_string = value
                                self.encapsulation_type_string.value_namespace = name_space
                                self.encapsulation_type_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "l2-transport"):
                                self.l2_transport = value
                                self.l2_transport.value_namespace = name_space
                                self.l2_transport.value_namespace_prefix = name_space_prefix
                            if(value_path == "line-state"):
                                self.line_state = value
                                self.line_state.value_namespace = name_space
                                self.line_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "mtu"):
                                self.mtu = value
                                self.mtu.value_namespace = name_space
                                self.mtu.value_namespace_prefix = name_space_prefix
                            if(value_path == "parent-interface"):
                                self.parent_interface = value
                                self.parent_interface.value_namespace = name_space
                                self.parent_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "state"):
                                self.state = value
                                self.state.value_namespace = name_space
                                self.state.value_namespace_prefix = name_space_prefix
                            if(value_path == "sub-interface-mtu-overhead"):
                                self.sub_interface_mtu_overhead = value
                                self.sub_interface_mtu_overhead.value_namespace = name_space
                                self.sub_interface_mtu_overhead.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

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
                            c = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface()
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
                    path_buffer = "system-view" + path_buffer

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
                            self.interfaces = InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces()
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
                    self.data_node_name.is_set or
                    (self.locationviews is not None and self.locationviews.has_data()) or
                    (self.pq_node_locations is not None and self.pq_node_locations.has_data()) or
                    (self.system_view is not None and self.system_view.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.data_node_name.yfilter != YFilter.not_set or
                    (self.locationviews is not None and self.locationviews.has_operation()) or
                    (self.pq_node_locations is not None and self.pq_node_locations.has_operation()) or
                    (self.system_view is not None and self.system_view.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "data-node" + "[data-node-name='" + self.data_node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-properties/data-nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.data_node_name.is_set or self.data_node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.data_node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "locationviews"):
                    if (self.locationviews is None):
                        self.locationviews = InterfaceProperties.DataNodes.DataNode.Locationviews()
                        self.locationviews.parent = self
                        self._children_name_map["locationviews"] = "locationviews"
                    return self.locationviews

                if (child_yang_name == "pq-node-locations"):
                    if (self.pq_node_locations is None):
                        self.pq_node_locations = InterfaceProperties.DataNodes.DataNode.PqNodeLocations()
                        self.pq_node_locations.parent = self
                        self._children_name_map["pq_node_locations"] = "pq-node-locations"
                    return self.pq_node_locations

                if (child_yang_name == "system-view"):
                    if (self.system_view is None):
                        self.system_view = InterfaceProperties.DataNodes.DataNode.SystemView()
                        self.system_view.parent = self
                        self._children_name_map["system_view"] = "system-view"
                    return self.system_view

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "locationviews" or name == "pq-node-locations" or name == "system-view" or name == "data-node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "data-node-name"):
                    self.data_node_name = value
                    self.data_node_name.value_namespace = name_space
                    self.data_node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.data_node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.data_node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "data-nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-properties/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "data-node"):
                for c in self.data_node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = InterfaceProperties.DataNodes.DataNode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.data_node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "data-node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.data_nodes is not None and self.data_nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.data_nodes is not None and self.data_nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ifmgr-oper:interface-properties" + path_buffer

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

        if (child_yang_name == "data-nodes"):
            if (self.data_nodes is None):
                self.data_nodes = InterfaceProperties.DataNodes()
                self.data_nodes.parent = self
                self._children_name_map["data_nodes"] = "data-nodes"
            return self.data_nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "data-nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InterfaceProperties()
        return self._top_entity

