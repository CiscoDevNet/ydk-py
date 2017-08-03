""" Cisco_IOS_XR_ncs1001_ots_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-ots package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class OtsAmplifierGridMode(Enum):
    """
    OtsAmplifierGridMode

    Ots amplifier grid mode

    .. data:: Y_100g_hz = 0

    	100GHz mode

    .. data:: Y_50g_hz = 1

    	50GHz mode

    .. data:: gr_idle_ss = 2

    	Gridless mode

    """

    Y_100g_hz = Enum.YLeaf(0, "100g-hz")

    Y_50g_hz = Enum.YLeaf(1, "50g-hz")

    gr_idle_ss = Enum.YLeaf(2, "gr-idle-ss")


class OtsAmplifierNode(Enum):
    """
    OtsAmplifierNode

    Ots amplifier node

    .. data:: term = 0

    	Nodetype TERM

    .. data:: ila = 1

    	Nodetype InLine Amplifier

    .. data:: roadm = 2

    	Nodetype ROADM

    """

    term = Enum.YLeaf(0, "term")

    ila = Enum.YLeaf(1, "ila")

    roadm = Enum.YLeaf(2, "roadm")


class OtsPsmLockoutFrom(Enum):
    """
    OtsPsmLockoutFrom

    Ots psm lockout from

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = Enum.YLeaf(1, "working")

    protected = Enum.YLeaf(2, "protected")


class OtsPsmManualSwitch(Enum):
    """
    OtsPsmManualSwitch

    Ots psm manual switch

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = Enum.YLeaf(1, "working")

    protected = Enum.YLeaf(2, "protected")



class HardwareModule(Entity):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'ncs1001-ots-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-ots-cfg"

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
                    super(HardwareModule, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(HardwareModule, self).__setattr__(name, value)


    class Node(Entity):
        """
        Node
        
        .. attribute:: location  <key>
        
        	Fully qualified line card specification
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: slot
        
        	Slot Id
        	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot>`
        
        

        """

        _prefix = 'ncs1001-ots-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModule.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "hardware-module"

            self.location = YLeaf(YType.str, "location")

            self.slot = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("location") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(HardwareModule.Node, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModule.Node, self).__setattr__(name, value)


        class Slot(Entity):
            """
            Slot Id
            
            .. attribute:: slot_id  <key>
            
            	Set Slot
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: amplifier
            
            	Amplifier Configs
            	**type**\:   :py:class:`Amplifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Amplifier>`
            
            .. attribute:: psm
            
            	PSM Configs
            	**type**\:   :py:class:`Psm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Psm>`
            
            

            """

            _prefix = 'ncs1001-ots-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModule.Node.Slot, self).__init__()

                self.yang_name = "slot"
                self.yang_parent_name = "node"

                self.slot_id = YLeaf(YType.str, "slot-id")

                self.amplifier = HardwareModule.Node.Slot.Amplifier()
                self.amplifier.parent = self
                self._children_name_map["amplifier"] = "amplifier"
                self._children_yang_names.add("amplifier")

                self.psm = HardwareModule.Node.Slot.Psm()
                self.psm.parent = self
                self._children_name_map["psm"] = "psm"
                self._children_yang_names.add("psm")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("slot_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModule.Node.Slot, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModule.Node.Slot, self).__setattr__(name, value)


            class Amplifier(Entity):
                """
                Amplifier Configs
                
                .. attribute:: grid_mode
                
                	Define the working mode for the optical module
                	**type**\:   :py:class:`OtsAmplifierGridMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsAmplifierGridMode>`
                
                .. attribute:: node_type
                
                	Define the type of node in which the amplifier is set to work
                	**type**\:   :py:class:`OtsAmplifierNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsAmplifierNode>`
                
                .. attribute:: udc_vlan
                
                	Define the VLAN ID in range <2\-4080>
                	**type**\:  int
                
                	**range:** 2..4080
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Amplifier, self).__init__()

                    self.yang_name = "amplifier"
                    self.yang_parent_name = "slot"

                    self.grid_mode = YLeaf(YType.enumeration, "grid-mode")

                    self.node_type = YLeaf(YType.enumeration, "node-type")

                    self.udc_vlan = YLeaf(YType.uint32, "udc-vlan")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("grid_mode",
                                    "node_type",
                                    "udc_vlan") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModule.Node.Slot.Amplifier, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModule.Node.Slot.Amplifier, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.grid_mode.is_set or
                        self.node_type.is_set or
                        self.udc_vlan.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.grid_mode.yfilter != YFilter.not_set or
                        self.node_type.yfilter != YFilter.not_set or
                        self.udc_vlan.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "amplifier" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.grid_mode.is_set or self.grid_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.grid_mode.get_name_leafdata())
                    if (self.node_type.is_set or self.node_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_type.get_name_leafdata())
                    if (self.udc_vlan.is_set or self.udc_vlan.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.udc_vlan.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "grid-mode" or name == "node-type" or name == "udc-vlan"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "grid-mode"):
                        self.grid_mode = value
                        self.grid_mode.value_namespace = name_space
                        self.grid_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-type"):
                        self.node_type = value
                        self.node_type.value_namespace = name_space
                        self.node_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "udc-vlan"):
                        self.udc_vlan = value
                        self.udc_vlan.value_namespace = name_space
                        self.udc_vlan.value_namespace_prefix = name_space_prefix


            class Psm(Entity):
                """
                PSM Configs
                
                .. attribute:: lockout_from
                
                	Exclude selected port from protection
                	**type**\:   :py:class:`OtsPsmLockoutFrom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsPsmLockoutFrom>`
                
                .. attribute:: manual_switch_to
                
                	Switch active path on selected port
                	**type**\:   :py:class:`OtsPsmManualSwitch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsPsmManualSwitch>`
                
                .. attribute:: section_protection
                
                	Psm section protection configuration
                	**type**\:  bool
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Psm, self).__init__()

                    self.yang_name = "psm"
                    self.yang_parent_name = "slot"

                    self.lockout_from = YLeaf(YType.enumeration, "lockout-from")

                    self.manual_switch_to = YLeaf(YType.enumeration, "manual-switch-to")

                    self.section_protection = YLeaf(YType.boolean, "section-protection")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("lockout_from",
                                    "manual_switch_to",
                                    "section_protection") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModule.Node.Slot.Psm, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModule.Node.Slot.Psm, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.lockout_from.is_set or
                        self.manual_switch_to.is_set or
                        self.section_protection.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.lockout_from.yfilter != YFilter.not_set or
                        self.manual_switch_to.yfilter != YFilter.not_set or
                        self.section_protection.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "psm" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.lockout_from.is_set or self.lockout_from.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lockout_from.get_name_leafdata())
                    if (self.manual_switch_to.is_set or self.manual_switch_to.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.manual_switch_to.get_name_leafdata())
                    if (self.section_protection.is_set or self.section_protection.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.section_protection.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lockout-from" or name == "manual-switch-to" or name == "section-protection"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "lockout-from"):
                        self.lockout_from = value
                        self.lockout_from.value_namespace = name_space
                        self.lockout_from.value_namespace_prefix = name_space_prefix
                    if(value_path == "manual-switch-to"):
                        self.manual_switch_to = value
                        self.manual_switch_to.value_namespace = name_space
                        self.manual_switch_to.value_namespace_prefix = name_space_prefix
                    if(value_path == "section-protection"):
                        self.section_protection = value
                        self.section_protection.value_namespace = name_space
                        self.section_protection.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.slot_id.is_set or
                    (self.amplifier is not None and self.amplifier.has_data()) or
                    (self.psm is not None and self.psm.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.slot_id.yfilter != YFilter.not_set or
                    (self.amplifier is not None and self.amplifier.has_operation()) or
                    (self.psm is not None and self.psm.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "slot" + "[slot-id='" + self.slot_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.slot_id.is_set or self.slot_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slot_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "amplifier"):
                    if (self.amplifier is None):
                        self.amplifier = HardwareModule.Node.Slot.Amplifier()
                        self.amplifier.parent = self
                        self._children_name_map["amplifier"] = "amplifier"
                    return self.amplifier

                if (child_yang_name == "psm"):
                    if (self.psm is None):
                        self.psm = HardwareModule.Node.Slot.Psm()
                        self.psm.parent = self
                        self._children_name_map["psm"] = "psm"
                    return self.psm

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "amplifier" or name == "psm" or name == "slot-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "slot-id"):
                    self.slot_id = value
                    self.slot_id.value_namespace = name_space
                    self.slot_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.slot:
                if (c.has_data()):
                    return True
            return self.location.is_set

        def has_operation(self):
            for c in self.slot:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.location.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node" + "[location='" + self.location.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                leaf_name_data.append(self.location.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "slot"):
                for c in self.slot:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HardwareModule.Node.Slot()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.slot.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "slot" or name == "location"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "location"):
                self.location = value
                self.location.value_namespace = name_space
                self.location.value_namespace_prefix = name_space_prefix

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
        path_buffer = "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module" + path_buffer

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

        if (child_yang_name == "node"):
            for c in self.node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = HardwareModule.Node()
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

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

