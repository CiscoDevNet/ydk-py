""" Cisco_IOS_XR_asr9k_prm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-prm package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-qos\-mode\: QoS mode in hardware module port(s)
  hardware\-module\-tcp\-mss\-adjust\: hardware module tcp mss adjust
  hardware\-module\-load\-balance\: hardware module load balance
  hardware\-module\-tcam\: hardware module tcam
  hardware\-module\-efd\: hardware module efd

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Asr9KEfdMode(Enum):
    """
    Asr9KEfdMode

    Asr9k efd mode

    .. data:: only_outer_encap = 0

    	Only check outer encap

    .. data:: include_inner_encap = 1

    	Check outer and inner encap

    """

    only_outer_encap = Enum.YLeaf(0, "only-outer-encap")

    include_inner_encap = Enum.YLeaf(1, "include-inner-encap")


class Asr9KEfdOperation(Enum):
    """
    Asr9KEfdOperation

    Asr9k efd operation

    .. data:: less_than = 2

    	Less than

    .. data:: greater_than_or_equal = 3

    	Greater than or equal

    """

    less_than = Enum.YLeaf(2, "less-than")

    greater_than_or_equal = Enum.YLeaf(3, "greater-than-or-equal")


class PrmTcamProfile(Enum):
    """
    PrmTcamProfile

    Prm tcam profile

    .. data:: profile0 = 0

    	Profile 0

    .. data:: profile1 = 1

    	Profile 1

    .. data:: profile2 = 2

    	Profile 2

    """

    profile0 = Enum.YLeaf(0, "profile0")

    profile1 = Enum.YLeaf(1, "profile1")

    profile2 = Enum.YLeaf(2, "profile2")



class HardwareModuleQosMode(Entity):
    """
    QoS mode in hardware module port(s)
    
    .. attribute:: nodes
    
    	QoS applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleQosMode, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-qos-mode"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"

        self.nodes = HardwareModuleQosMode.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        QoS applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleQosMode.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-qos-mode"

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
                        super(HardwareModuleQosMode.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleQosMode.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: child_shaping_disable
            
            	Disable child level/flat policy shaping
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lowburst_enable
            
            	Enable low burst mode for TM entity
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleQosMode.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.child_shaping_disable = YLeaf(YType.empty, "child-shaping-disable")

                self.lowburst_enable = YLeaf(YType.empty, "lowburst-enable")

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
                                "child_shaping_disable",
                                "lowburst_enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleQosMode.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleQosMode.Nodes.Node, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.node_name.is_set or
                    self.child_shaping_disable.is_set or
                    self.lowburst_enable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.child_shaping_disable.yfilter != YFilter.not_set or
                    self.lowburst_enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.child_shaping_disable.is_set or self.child_shaping_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.child_shaping_disable.get_name_leafdata())
                if (self.lowburst_enable.is_set or self.lowburst_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lowburst_enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node-name" or name == "child-shaping-disable" or name == "lowburst-enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "child-shaping-disable"):
                    self.child_shaping_disable = value
                    self.child_shaping_disable.value_namespace = name_space
                    self.child_shaping_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "lowburst-enable"):
                    self.lowburst_enable = value
                    self.lowburst_enable.value_namespace = name_space
                    self.lowburst_enable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/%s" % self.get_segment_path()
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
                c = HardwareModuleQosMode.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode" + path_buffer

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
                self.nodes = HardwareModuleQosMode.Nodes()
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
        self._top_entity = HardwareModuleQosMode()
        return self._top_entity

class HardwareModuleTcpMssAdjust(Entity):
    """
    hardware module tcp mss adjust
    
    .. attribute:: nodes
    
    	TCP MSS Adjust applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleTcpMssAdjust, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-tcp-mss-adjust"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"

        self.nodes = HardwareModuleTcpMssAdjust.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        TCP MSS Adjust applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleTcpMssAdjust.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-tcp-mss-adjust"

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
                        super(HardwareModuleTcpMssAdjust.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleTcpMssAdjust.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	TCP MSS Adjust NPs
            	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleTcpMssAdjust.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.nps = HardwareModuleTcpMssAdjust.Nodes.Node.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._children_yang_names.add("nps")

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
                            super(HardwareModuleTcpMssAdjust.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleTcpMssAdjust.Nodes.Node, self).__setattr__(name, value)


            class Nps(Entity):
                """
                TCP MSS Adjust NPs
                
                .. attribute:: np
                
                	NP number
                	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node"

                    self.np = YList(self)

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
                                super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps, self).__setattr__(name, value)


                class Np(Entity):
                    """
                    NP number
                    
                    .. attribute:: np_id  <key>
                    
                    	Number between 0\-7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: adjust_value
                    
                    	TCP MSS Adjust value
                    	**type**\:  int
                    
                    	**range:** 1280..1535
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'asr9k-prm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"

                        self.np_id = YLeaf(YType.uint32, "np-id")

                        self.adjust_value = YLeaf(YType.uint32, "adjust-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("np_id",
                                        "adjust_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.np_id.is_set or
                            self.adjust_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.np_id.yfilter != YFilter.not_set or
                            self.adjust_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "np" + "[np-id='" + self.np_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.np_id.is_set or self.np_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.np_id.get_name_leafdata())
                        if (self.adjust_value.is_set or self.adjust_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.adjust_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "np-id" or name == "adjust-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "np-id"):
                            self.np_id = value
                            self.np_id.value_namespace = name_space
                            self.np_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "adjust-value"):
                            self.adjust_value = value
                            self.adjust_value.value_namespace = name_space
                            self.adjust_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.np:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.np:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nps" + path_buffer

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

                    if (child_yang_name == "np"):
                        for c in self.np:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.np.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "np"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.nps is not None and self.nps.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.nps is not None and self.nps.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "nps"):
                    if (self.nps is None):
                        self.nps = HardwareModuleTcpMssAdjust.Nodes.Node.Nps()
                        self.nps.parent = self
                        self._children_name_map["nps"] = "nps"
                    return self.nps

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nps" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/%s" % self.get_segment_path()
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
                c = HardwareModuleTcpMssAdjust.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust" + path_buffer

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
                self.nodes = HardwareModuleTcpMssAdjust.Nodes()
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
        self._top_entity = HardwareModuleTcpMssAdjust()
        return self._top_entity

class HardwareModuleLoadBalance(Entity):
    """
    hardware module load balance
    
    .. attribute:: bundle
    
    	Bundle load balance options
    	**type**\:   :py:class:`Bundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleLoadBalance.Bundle>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleLoadBalance, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-load-balance"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"

        self.bundle = HardwareModuleLoadBalance.Bundle()
        self.bundle.parent = self
        self._children_name_map["bundle"] = "bundle"
        self._children_yang_names.add("bundle")


    class Bundle(Entity):
        """
        Bundle load balance options
        
        .. attribute:: l2_service
        
        	Load balance for L2 services
        	**type**\:   :py:class:`L2Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleLoadBalance.Bundle.L2Service>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleLoadBalance.Bundle, self).__init__()

            self.yang_name = "bundle"
            self.yang_parent_name = "hardware-module-load-balance"

            self.l2_service = HardwareModuleLoadBalance.Bundle.L2Service()
            self.l2_service.parent = self
            self._children_name_map["l2_service"] = "l2-service"
            self._children_yang_names.add("l2-service")


        class L2Service(Entity):
            """
            Load balance for L2 services
            
            .. attribute:: l3_parameters
            
            	Load balance L2 services over bundle with L3 parameters
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleLoadBalance.Bundle.L2Service, self).__init__()

                self.yang_name = "l2-service"
                self.yang_parent_name = "bundle"

                self.l3_parameters = YLeaf(YType.empty, "l3-parameters")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("l3_parameters") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleLoadBalance.Bundle.L2Service, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleLoadBalance.Bundle.L2Service, self).__setattr__(name, value)

            def has_data(self):
                return self.l3_parameters.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.l3_parameters.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "l2-service" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance/bundle/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.l3_parameters.is_set or self.l3_parameters.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.l3_parameters.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "l3-parameters"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "l3-parameters"):
                    self.l3_parameters = value
                    self.l3_parameters.value_namespace = name_space
                    self.l3_parameters.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.l2_service is not None and self.l2_service.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.l2_service is not None and self.l2_service.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bundle" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "l2-service"):
                if (self.l2_service is None):
                    self.l2_service = HardwareModuleLoadBalance.Bundle.L2Service()
                    self.l2_service.parent = self
                    self._children_name_map["l2_service"] = "l2-service"
                return self.l2_service

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "l2-service"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.bundle is not None and self.bundle.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.bundle is not None and self.bundle.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance" + path_buffer

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

        if (child_yang_name == "bundle"):
            if (self.bundle is None):
                self.bundle = HardwareModuleLoadBalance.Bundle()
                self.bundle.parent = self
                self._children_name_map["bundle"] = "bundle"
            return self.bundle

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bundle"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HardwareModuleLoadBalance()
        return self._top_entity

class HardwareModuleTcam(Entity):
    """
    hardware module tcam
    
    .. attribute:: global_profile
    
    	Global TCAM partition profile for all TCAM applicable nodes
    	**type**\:   :py:class:`PrmTcamProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfile>`
    
    	**default value**\: profile0
    
    .. attribute:: nodes
    
    	TCAM applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleTcam, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-tcam"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"

        self.global_profile = YLeaf(YType.enumeration, "global-profile")

        self.nodes = HardwareModuleTcam.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("global_profile") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(HardwareModuleTcam, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(HardwareModuleTcam, self).__setattr__(name, value)


    class Nodes(Entity):
        """
        TCAM applicable nodes
        
        .. attribute:: node
        
        	A TCAM applicable node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleTcam.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-tcam"

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
                        super(HardwareModuleTcam.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleTcam.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            A TCAM applicable node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: profile
            
            	A TCAM partition profile
            	**type**\:   :py:class:`PrmTcamProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfile>`
            
            	**default value**\: profile0
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleTcam.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.profile = YLeaf(YType.enumeration, "profile")

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
                                "profile") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleTcam.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleTcam.Nodes.Node, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.node_name.is_set or
                    self.profile.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.profile.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.profile.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node-name" or name == "profile"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "profile"):
                    self.profile = value
                    self.profile.value_namespace = name_space
                    self.profile.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/%s" % self.get_segment_path()
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
                c = HardwareModuleTcam.Nodes.Node()
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
            self.global_profile.is_set or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.global_profile.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.global_profile.is_set or self.global_profile.yfilter != YFilter.not_set):
            leaf_name_data.append(self.global_profile.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = HardwareModuleTcam.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes" or name == "global-profile"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "global-profile"):
            self.global_profile = value
            self.global_profile.value_namespace = name_space
            self.global_profile.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = HardwareModuleTcam()
        return self._top_entity

class HardwareModuleEfd(Entity):
    """
    hardware module efd
    
    .. attribute:: node_all
    
    	All nodes
    	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll>`
    
    .. attribute:: nodes
    
    	EFD applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleEfd, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-efd"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-prm-cfg"

        self.node_all = HardwareModuleEfd.NodeAll()
        self.node_all.parent = self
        self._children_name_map["node_all"] = "node-all"
        self._children_yang_names.add("node-all")

        self.nodes = HardwareModuleEfd.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class NodeAll(Entity):
        """
        All nodes
        
        .. attribute:: enable
        
        	Enable EFD for this node
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_precedence
        
        	EFD IP parameters
        	**type**\:   :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.IpPrecedence>`
        
        	**presence node**\: True
        
        .. attribute:: ip_priority_mask
        
        	IP Priority Mask
        	**type**\:   :py:class:`IpPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.IpPriorityMask>`
        
        	**presence node**\: True
        
        .. attribute:: mode
        
        	EFD mode parameter
        	**type**\:   :py:class:`Asr9KEfdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdMode>`
        
        .. attribute:: mpls_exp
        
        	EFD MPLS parameters
        	**type**\:   :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.MplsExp>`
        
        	**presence node**\: True
        
        .. attribute:: mpls_priority_mask
        
        	MPLS Priority Mask
        	**type**\:   :py:class:`MplsPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.MplsPriorityMask>`
        
        	**presence node**\: True
        
        .. attribute:: vlan_cos
        
        	EFD VLAN parameters
        	**type**\:   :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.VlanCos>`
        
        	**presence node**\: True
        
        .. attribute:: vlan_priority_mask
        
        	VLAN Priority Mask
        	**type**\:   :py:class:`VlanPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.VlanPriorityMask>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleEfd.NodeAll, self).__init__()

            self.yang_name = "node-all"
            self.yang_parent_name = "hardware-module-efd"

            self.enable = YLeaf(YType.empty, "enable")

            self.mode = YLeaf(YType.enumeration, "mode")

            self.ip_precedence = None
            self._children_name_map["ip_precedence"] = "ip-precedence"
            self._children_yang_names.add("ip-precedence")

            self.ip_priority_mask = None
            self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
            self._children_yang_names.add("ip-priority-mask")

            self.mpls_exp = None
            self._children_name_map["mpls_exp"] = "mpls-exp"
            self._children_yang_names.add("mpls-exp")

            self.mpls_priority_mask = None
            self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
            self._children_yang_names.add("mpls-priority-mask")

            self.vlan_cos = None
            self._children_name_map["vlan_cos"] = "vlan-cos"
            self._children_yang_names.add("vlan-cos")

            self.vlan_priority_mask = None
            self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
            self._children_yang_names.add("vlan-priority-mask")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable",
                            "mode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(HardwareModuleEfd.NodeAll, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleEfd.NodeAll, self).__setattr__(name, value)


        class VlanPriorityMask(Entity):
            """
            VLAN Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.VlanPriorityMask, self).__init__()

                self.yang_name = "vlan-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.prec0 = YLeaf(YType.uint32, "prec0")

                self.prec1 = YLeaf(YType.uint32, "prec1")

                self.prec2 = YLeaf(YType.uint32, "prec2")

                self.prec3 = YLeaf(YType.uint32, "prec3")

                self.prec4 = YLeaf(YType.uint32, "prec4")

                self.prec5 = YLeaf(YType.uint32, "prec5")

                self.prec6 = YLeaf(YType.uint32, "prec6")

                self.prec7 = YLeaf(YType.uint32, "prec7")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prec0",
                                "prec1",
                                "prec2",
                                "prec3",
                                "prec4",
                                "prec5",
                                "prec6",
                                "prec7") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.VlanPriorityMask, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.VlanPriorityMask, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.prec0.is_set or
                    self.prec1.is_set or
                    self.prec2.is_set or
                    self.prec3.is_set or
                    self.prec4.is_set or
                    self.prec5.is_set or
                    self.prec6.is_set or
                    self.prec7.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prec0.yfilter != YFilter.not_set or
                    self.prec1.yfilter != YFilter.not_set or
                    self.prec2.yfilter != YFilter.not_set or
                    self.prec3.yfilter != YFilter.not_set or
                    self.prec4.yfilter != YFilter.not_set or
                    self.prec5.yfilter != YFilter.not_set or
                    self.prec6.yfilter != YFilter.not_set or
                    self.prec7.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vlan-priority-mask" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec0.get_name_leafdata())
                if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec1.get_name_leafdata())
                if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec2.get_name_leafdata())
                if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec3.get_name_leafdata())
                if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec4.get_name_leafdata())
                if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec5.get_name_leafdata())
                if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec6.get_name_leafdata())
                if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec7.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prec0"):
                    self.prec0 = value
                    self.prec0.value_namespace = name_space
                    self.prec0.value_namespace_prefix = name_space_prefix
                if(value_path == "prec1"):
                    self.prec1 = value
                    self.prec1.value_namespace = name_space
                    self.prec1.value_namespace_prefix = name_space_prefix
                if(value_path == "prec2"):
                    self.prec2 = value
                    self.prec2.value_namespace = name_space
                    self.prec2.value_namespace_prefix = name_space_prefix
                if(value_path == "prec3"):
                    self.prec3 = value
                    self.prec3.value_namespace = name_space
                    self.prec3.value_namespace_prefix = name_space_prefix
                if(value_path == "prec4"):
                    self.prec4 = value
                    self.prec4.value_namespace = name_space
                    self.prec4.value_namespace_prefix = name_space_prefix
                if(value_path == "prec5"):
                    self.prec5 = value
                    self.prec5.value_namespace = name_space
                    self.prec5.value_namespace_prefix = name_space_prefix
                if(value_path == "prec6"):
                    self.prec6 = value
                    self.prec6.value_namespace = name_space
                    self.prec6.value_namespace_prefix = name_space_prefix
                if(value_path == "prec7"):
                    self.prec7 = value
                    self.prec7.value_namespace = name_space
                    self.prec7.value_namespace_prefix = name_space_prefix


        class IpPrecedence(Entity):
            """
            EFD IP parameters
            
            .. attribute:: operation_
            
            	IP operation
            	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            .. attribute:: precedence
            
            	IP TOS precedence threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.IpPrecedence, self).__init__()

                self.yang_name = "ip-precedence"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.operation_ = YLeaf(YType.enumeration, "operation")

                self.precedence = YLeaf(YType.uint32, "precedence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("operation_",
                                "precedence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.IpPrecedence, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.IpPrecedence, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.operation_.is_set or
                    self.precedence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.operation_.yfilter != YFilter.not_set or
                    self.precedence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ip-precedence" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_.get_name_leafdata())
                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.precedence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "operation" or name == "precedence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "operation"):
                    self.operation_ = value
                    self.operation_.value_namespace = name_space
                    self.operation_.value_namespace_prefix = name_space_prefix
                if(value_path == "precedence"):
                    self.precedence = value
                    self.precedence.value_namespace = name_space
                    self.precedence.value_namespace_prefix = name_space_prefix


        class VlanCos(Entity):
            """
            EFD VLAN parameters
            
            .. attribute:: cos
            
            	VLAN COS threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation_
            
            	VLAN operation
            	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.VlanCos, self).__init__()

                self.yang_name = "vlan-cos"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.cos = YLeaf(YType.uint32, "cos")

                self.operation_ = YLeaf(YType.enumeration, "operation")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cos",
                                "operation_") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.VlanCos, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.VlanCos, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cos.is_set or
                    self.operation_.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cos.yfilter != YFilter.not_set or
                    self.operation_.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vlan-cos" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cos.get_name_leafdata())
                if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cos" or name == "operation"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cos"):
                    self.cos = value
                    self.cos.value_namespace = name_space
                    self.cos.value_namespace_prefix = name_space_prefix
                if(value_path == "operation"):
                    self.operation_ = value
                    self.operation_.value_namespace = name_space
                    self.operation_.value_namespace_prefix = name_space_prefix


        class IpPriorityMask(Entity):
            """
            IP Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.IpPriorityMask, self).__init__()

                self.yang_name = "ip-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.prec0 = YLeaf(YType.uint32, "prec0")

                self.prec1 = YLeaf(YType.uint32, "prec1")

                self.prec2 = YLeaf(YType.uint32, "prec2")

                self.prec3 = YLeaf(YType.uint32, "prec3")

                self.prec4 = YLeaf(YType.uint32, "prec4")

                self.prec5 = YLeaf(YType.uint32, "prec5")

                self.prec6 = YLeaf(YType.uint32, "prec6")

                self.prec7 = YLeaf(YType.uint32, "prec7")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prec0",
                                "prec1",
                                "prec2",
                                "prec3",
                                "prec4",
                                "prec5",
                                "prec6",
                                "prec7") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.IpPriorityMask, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.IpPriorityMask, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.prec0.is_set or
                    self.prec1.is_set or
                    self.prec2.is_set or
                    self.prec3.is_set or
                    self.prec4.is_set or
                    self.prec5.is_set or
                    self.prec6.is_set or
                    self.prec7.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prec0.yfilter != YFilter.not_set or
                    self.prec1.yfilter != YFilter.not_set or
                    self.prec2.yfilter != YFilter.not_set or
                    self.prec3.yfilter != YFilter.not_set or
                    self.prec4.yfilter != YFilter.not_set or
                    self.prec5.yfilter != YFilter.not_set or
                    self.prec6.yfilter != YFilter.not_set or
                    self.prec7.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ip-priority-mask" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec0.get_name_leafdata())
                if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec1.get_name_leafdata())
                if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec2.get_name_leafdata())
                if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec3.get_name_leafdata())
                if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec4.get_name_leafdata())
                if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec5.get_name_leafdata())
                if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec6.get_name_leafdata())
                if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec7.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prec0"):
                    self.prec0 = value
                    self.prec0.value_namespace = name_space
                    self.prec0.value_namespace_prefix = name_space_prefix
                if(value_path == "prec1"):
                    self.prec1 = value
                    self.prec1.value_namespace = name_space
                    self.prec1.value_namespace_prefix = name_space_prefix
                if(value_path == "prec2"):
                    self.prec2 = value
                    self.prec2.value_namespace = name_space
                    self.prec2.value_namespace_prefix = name_space_prefix
                if(value_path == "prec3"):
                    self.prec3 = value
                    self.prec3.value_namespace = name_space
                    self.prec3.value_namespace_prefix = name_space_prefix
                if(value_path == "prec4"):
                    self.prec4 = value
                    self.prec4.value_namespace = name_space
                    self.prec4.value_namespace_prefix = name_space_prefix
                if(value_path == "prec5"):
                    self.prec5 = value
                    self.prec5.value_namespace = name_space
                    self.prec5.value_namespace_prefix = name_space_prefix
                if(value_path == "prec6"):
                    self.prec6 = value
                    self.prec6.value_namespace = name_space
                    self.prec6.value_namespace_prefix = name_space_prefix
                if(value_path == "prec7"):
                    self.prec7 = value
                    self.prec7.value_namespace = name_space
                    self.prec7.value_namespace_prefix = name_space_prefix


        class MplsPriorityMask(Entity):
            """
            MPLS Priority Mask
            
            .. attribute:: prec0
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec1
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec2
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec3
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec4
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec5
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec6
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            .. attribute:: prec7
            
            	Prec
            	**type**\:  int
            
            	**range:** 0..1
            
            	**default value**\: 0
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.MplsPriorityMask, self).__init__()

                self.yang_name = "mpls-priority-mask"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.prec0 = YLeaf(YType.uint32, "prec0")

                self.prec1 = YLeaf(YType.uint32, "prec1")

                self.prec2 = YLeaf(YType.uint32, "prec2")

                self.prec3 = YLeaf(YType.uint32, "prec3")

                self.prec4 = YLeaf(YType.uint32, "prec4")

                self.prec5 = YLeaf(YType.uint32, "prec5")

                self.prec6 = YLeaf(YType.uint32, "prec6")

                self.prec7 = YLeaf(YType.uint32, "prec7")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prec0",
                                "prec1",
                                "prec2",
                                "prec3",
                                "prec4",
                                "prec5",
                                "prec6",
                                "prec7") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.MplsPriorityMask, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.MplsPriorityMask, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.prec0.is_set or
                    self.prec1.is_set or
                    self.prec2.is_set or
                    self.prec3.is_set or
                    self.prec4.is_set or
                    self.prec5.is_set or
                    self.prec6.is_set or
                    self.prec7.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prec0.yfilter != YFilter.not_set or
                    self.prec1.yfilter != YFilter.not_set or
                    self.prec2.yfilter != YFilter.not_set or
                    self.prec3.yfilter != YFilter.not_set or
                    self.prec4.yfilter != YFilter.not_set or
                    self.prec5.yfilter != YFilter.not_set or
                    self.prec6.yfilter != YFilter.not_set or
                    self.prec7.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mpls-priority-mask" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec0.get_name_leafdata())
                if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec1.get_name_leafdata())
                if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec2.get_name_leafdata())
                if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec3.get_name_leafdata())
                if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec4.get_name_leafdata())
                if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec5.get_name_leafdata())
                if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec6.get_name_leafdata())
                if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prec7.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prec0"):
                    self.prec0 = value
                    self.prec0.value_namespace = name_space
                    self.prec0.value_namespace_prefix = name_space_prefix
                if(value_path == "prec1"):
                    self.prec1 = value
                    self.prec1.value_namespace = name_space
                    self.prec1.value_namespace_prefix = name_space_prefix
                if(value_path == "prec2"):
                    self.prec2 = value
                    self.prec2.value_namespace = name_space
                    self.prec2.value_namespace_prefix = name_space_prefix
                if(value_path == "prec3"):
                    self.prec3 = value
                    self.prec3.value_namespace = name_space
                    self.prec3.value_namespace_prefix = name_space_prefix
                if(value_path == "prec4"):
                    self.prec4 = value
                    self.prec4.value_namespace = name_space
                    self.prec4.value_namespace_prefix = name_space_prefix
                if(value_path == "prec5"):
                    self.prec5 = value
                    self.prec5.value_namespace = name_space
                    self.prec5.value_namespace_prefix = name_space_prefix
                if(value_path == "prec6"):
                    self.prec6 = value
                    self.prec6.value_namespace = name_space
                    self.prec6.value_namespace_prefix = name_space_prefix
                if(value_path == "prec7"):
                    self.prec7 = value
                    self.prec7.value_namespace = name_space
                    self.prec7.value_namespace_prefix = name_space_prefix


        class MplsExp(Entity):
            """
            EFD MPLS parameters
            
            .. attribute:: exp
            
            	MPLS EXP threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation_
            
            	MPLS operation
            	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
            
            	**default value**\: greater-than-or-equal
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.NodeAll.MplsExp, self).__init__()

                self.yang_name = "mpls-exp"
                self.yang_parent_name = "node-all"
                self.is_presence_container = True

                self.exp = YLeaf(YType.uint32, "exp")

                self.operation_ = YLeaf(YType.enumeration, "operation")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("exp",
                                "operation_") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.NodeAll.MplsExp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.NodeAll.MplsExp, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.exp.is_set or
                    self.operation_.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.exp.yfilter != YFilter.not_set or
                    self.operation_.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mpls-exp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/node-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.exp.is_set or self.exp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.exp.get_name_leafdata())
                if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operation_.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "exp" or name == "operation"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "exp"):
                    self.exp = value
                    self.exp.value_namespace = name_space
                    self.exp.value_namespace_prefix = name_space_prefix
                if(value_path == "operation"):
                    self.operation_ = value
                    self.operation_.value_namespace = name_space
                    self.operation_.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.enable.is_set or
                self.mode.is_set or
                (self.ip_precedence is not None) or
                (self.ip_priority_mask is not None) or
                (self.mpls_exp is not None) or
                (self.mpls_priority_mask is not None) or
                (self.vlan_cos is not None) or
                (self.vlan_priority_mask is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.mode.yfilter != YFilter.not_set or
                (self.ip_precedence is not None and self.ip_precedence.has_operation()) or
                (self.ip_priority_mask is not None and self.ip_priority_mask.has_operation()) or
                (self.mpls_exp is not None and self.mpls_exp.has_operation()) or
                (self.mpls_priority_mask is not None and self.mpls_priority_mask.has_operation()) or
                (self.vlan_cos is not None and self.vlan_cos.has_operation()) or
                (self.vlan_priority_mask is not None and self.vlan_priority_mask.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node-all" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ip-precedence"):
                if (self.ip_precedence is None):
                    self.ip_precedence = HardwareModuleEfd.NodeAll.IpPrecedence()
                    self.ip_precedence.parent = self
                    self._children_name_map["ip_precedence"] = "ip-precedence"
                return self.ip_precedence

            if (child_yang_name == "ip-priority-mask"):
                if (self.ip_priority_mask is None):
                    self.ip_priority_mask = HardwareModuleEfd.NodeAll.IpPriorityMask()
                    self.ip_priority_mask.parent = self
                    self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
                return self.ip_priority_mask

            if (child_yang_name == "mpls-exp"):
                if (self.mpls_exp is None):
                    self.mpls_exp = HardwareModuleEfd.NodeAll.MplsExp()
                    self.mpls_exp.parent = self
                    self._children_name_map["mpls_exp"] = "mpls-exp"
                return self.mpls_exp

            if (child_yang_name == "mpls-priority-mask"):
                if (self.mpls_priority_mask is None):
                    self.mpls_priority_mask = HardwareModuleEfd.NodeAll.MplsPriorityMask()
                    self.mpls_priority_mask.parent = self
                    self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
                return self.mpls_priority_mask

            if (child_yang_name == "vlan-cos"):
                if (self.vlan_cos is None):
                    self.vlan_cos = HardwareModuleEfd.NodeAll.VlanCos()
                    self.vlan_cos.parent = self
                    self._children_name_map["vlan_cos"] = "vlan-cos"
                return self.vlan_cos

            if (child_yang_name == "vlan-priority-mask"):
                if (self.vlan_priority_mask is None):
                    self.vlan_priority_mask = HardwareModuleEfd.NodeAll.VlanPriorityMask()
                    self.vlan_priority_mask.parent = self
                    self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
                return self.vlan_priority_mask

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ip-precedence" or name == "ip-priority-mask" or name == "mpls-exp" or name == "mpls-priority-mask" or name == "vlan-cos" or name == "vlan-priority-mask" or name == "enable" or name == "mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "mode"):
                self.mode = value
                self.mode.value_namespace = name_space
                self.mode.value_namespace_prefix = name_space_prefix


    class Nodes(Entity):
        """
        EFD applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleEfd.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-efd"

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
                        super(HardwareModuleEfd.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModuleEfd.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node Name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: enable
            
            	Enable EFD for this node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip_precedence
            
            	EFD IP parameters
            	**type**\:   :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.IpPrecedence>`
            
            	**presence node**\: True
            
            .. attribute:: ip_priority_mask
            
            	IP Priority Mask
            	**type**\:   :py:class:`IpPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.IpPriorityMask>`
            
            	**presence node**\: True
            
            .. attribute:: mode
            
            	EFD mode parameter
            	**type**\:   :py:class:`Asr9KEfdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdMode>`
            
            .. attribute:: mpls_exp
            
            	EFD MPLS parameters
            	**type**\:   :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.MplsExp>`
            
            	**presence node**\: True
            
            .. attribute:: mpls_priority_mask
            
            	MPLS Priority Mask
            	**type**\:   :py:class:`MplsPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.MplsPriorityMask>`
            
            	**presence node**\: True
            
            .. attribute:: vlan_cos
            
            	EFD VLAN parameters
            	**type**\:   :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.VlanCos>`
            
            	**presence node**\: True
            
            .. attribute:: vlan_priority_mask
            
            	VLAN Priority Mask
            	**type**\:   :py:class:`VlanPriorityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.VlanPriorityMask>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleEfd.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.mode = YLeaf(YType.enumeration, "mode")

                self.ip_precedence = None
                self._children_name_map["ip_precedence"] = "ip-precedence"
                self._children_yang_names.add("ip-precedence")

                self.ip_priority_mask = None
                self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
                self._children_yang_names.add("ip-priority-mask")

                self.mpls_exp = None
                self._children_name_map["mpls_exp"] = "mpls-exp"
                self._children_yang_names.add("mpls-exp")

                self.mpls_priority_mask = None
                self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
                self._children_yang_names.add("mpls-priority-mask")

                self.vlan_cos = None
                self._children_name_map["vlan_cos"] = "vlan-cos"
                self._children_yang_names.add("vlan-cos")

                self.vlan_priority_mask = None
                self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
                self._children_yang_names.add("vlan-priority-mask")

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
                                "enable",
                                "mode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModuleEfd.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModuleEfd.Nodes.Node, self).__setattr__(name, value)


            class VlanPriorityMask(Entity):
                """
                VLAN Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.VlanPriorityMask, self).__init__()

                    self.yang_name = "vlan-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.prec0 = YLeaf(YType.uint32, "prec0")

                    self.prec1 = YLeaf(YType.uint32, "prec1")

                    self.prec2 = YLeaf(YType.uint32, "prec2")

                    self.prec3 = YLeaf(YType.uint32, "prec3")

                    self.prec4 = YLeaf(YType.uint32, "prec4")

                    self.prec5 = YLeaf(YType.uint32, "prec5")

                    self.prec6 = YLeaf(YType.uint32, "prec6")

                    self.prec7 = YLeaf(YType.uint32, "prec7")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prec0",
                                    "prec1",
                                    "prec2",
                                    "prec3",
                                    "prec4",
                                    "prec5",
                                    "prec6",
                                    "prec7") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.VlanPriorityMask, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.VlanPriorityMask, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prec0.is_set or
                        self.prec1.is_set or
                        self.prec2.is_set or
                        self.prec3.is_set or
                        self.prec4.is_set or
                        self.prec5.is_set or
                        self.prec6.is_set or
                        self.prec7.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prec0.yfilter != YFilter.not_set or
                        self.prec1.yfilter != YFilter.not_set or
                        self.prec2.yfilter != YFilter.not_set or
                        self.prec3.yfilter != YFilter.not_set or
                        self.prec4.yfilter != YFilter.not_set or
                        self.prec5.yfilter != YFilter.not_set or
                        self.prec6.yfilter != YFilter.not_set or
                        self.prec7.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vlan-priority-mask" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec0.get_name_leafdata())
                    if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec1.get_name_leafdata())
                    if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec2.get_name_leafdata())
                    if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec3.get_name_leafdata())
                    if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec4.get_name_leafdata())
                    if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec5.get_name_leafdata())
                    if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec6.get_name_leafdata())
                    if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec7.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prec0"):
                        self.prec0 = value
                        self.prec0.value_namespace = name_space
                        self.prec0.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec1"):
                        self.prec1 = value
                        self.prec1.value_namespace = name_space
                        self.prec1.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec2"):
                        self.prec2 = value
                        self.prec2.value_namespace = name_space
                        self.prec2.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec3"):
                        self.prec3 = value
                        self.prec3.value_namespace = name_space
                        self.prec3.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec4"):
                        self.prec4 = value
                        self.prec4.value_namespace = name_space
                        self.prec4.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec5"):
                        self.prec5 = value
                        self.prec5.value_namespace = name_space
                        self.prec5.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec6"):
                        self.prec6 = value
                        self.prec6.value_namespace = name_space
                        self.prec6.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec7"):
                        self.prec7 = value
                        self.prec7.value_namespace = name_space
                        self.prec7.value_namespace_prefix = name_space_prefix


            class IpPrecedence(Entity):
                """
                EFD IP parameters
                
                .. attribute:: operation_
                
                	IP operation
                	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                .. attribute:: precedence
                
                	IP TOS precedence threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.IpPrecedence, self).__init__()

                    self.yang_name = "ip-precedence"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.operation_ = YLeaf(YType.enumeration, "operation")

                    self.precedence = YLeaf(YType.uint32, "precedence")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("operation_",
                                    "precedence") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.IpPrecedence, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.IpPrecedence, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.operation_.is_set or
                        self.precedence.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.operation_.yfilter != YFilter.not_set or
                        self.precedence.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-precedence" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operation_.get_name_leafdata())
                    if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.precedence.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "operation" or name == "precedence"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "operation"):
                        self.operation_ = value
                        self.operation_.value_namespace = name_space
                        self.operation_.value_namespace_prefix = name_space_prefix
                    if(value_path == "precedence"):
                        self.precedence = value
                        self.precedence.value_namespace = name_space
                        self.precedence.value_namespace_prefix = name_space_prefix


            class VlanCos(Entity):
                """
                EFD VLAN parameters
                
                .. attribute:: cos
                
                	VLAN COS threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation_
                
                	VLAN operation
                	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.VlanCos, self).__init__()

                    self.yang_name = "vlan-cos"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.cos = YLeaf(YType.uint32, "cos")

                    self.operation_ = YLeaf(YType.enumeration, "operation")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cos",
                                    "operation_") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.VlanCos, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.VlanCos, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cos.is_set or
                        self.operation_.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cos.yfilter != YFilter.not_set or
                        self.operation_.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vlan-cos" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cos.get_name_leafdata())
                    if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operation_.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cos" or name == "operation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cos"):
                        self.cos = value
                        self.cos.value_namespace = name_space
                        self.cos.value_namespace_prefix = name_space_prefix
                    if(value_path == "operation"):
                        self.operation_ = value
                        self.operation_.value_namespace = name_space
                        self.operation_.value_namespace_prefix = name_space_prefix


            class IpPriorityMask(Entity):
                """
                IP Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.IpPriorityMask, self).__init__()

                    self.yang_name = "ip-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.prec0 = YLeaf(YType.uint32, "prec0")

                    self.prec1 = YLeaf(YType.uint32, "prec1")

                    self.prec2 = YLeaf(YType.uint32, "prec2")

                    self.prec3 = YLeaf(YType.uint32, "prec3")

                    self.prec4 = YLeaf(YType.uint32, "prec4")

                    self.prec5 = YLeaf(YType.uint32, "prec5")

                    self.prec6 = YLeaf(YType.uint32, "prec6")

                    self.prec7 = YLeaf(YType.uint32, "prec7")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prec0",
                                    "prec1",
                                    "prec2",
                                    "prec3",
                                    "prec4",
                                    "prec5",
                                    "prec6",
                                    "prec7") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.IpPriorityMask, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.IpPriorityMask, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prec0.is_set or
                        self.prec1.is_set or
                        self.prec2.is_set or
                        self.prec3.is_set or
                        self.prec4.is_set or
                        self.prec5.is_set or
                        self.prec6.is_set or
                        self.prec7.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prec0.yfilter != YFilter.not_set or
                        self.prec1.yfilter != YFilter.not_set or
                        self.prec2.yfilter != YFilter.not_set or
                        self.prec3.yfilter != YFilter.not_set or
                        self.prec4.yfilter != YFilter.not_set or
                        self.prec5.yfilter != YFilter.not_set or
                        self.prec6.yfilter != YFilter.not_set or
                        self.prec7.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-priority-mask" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec0.get_name_leafdata())
                    if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec1.get_name_leafdata())
                    if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec2.get_name_leafdata())
                    if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec3.get_name_leafdata())
                    if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec4.get_name_leafdata())
                    if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec5.get_name_leafdata())
                    if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec6.get_name_leafdata())
                    if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec7.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prec0"):
                        self.prec0 = value
                        self.prec0.value_namespace = name_space
                        self.prec0.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec1"):
                        self.prec1 = value
                        self.prec1.value_namespace = name_space
                        self.prec1.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec2"):
                        self.prec2 = value
                        self.prec2.value_namespace = name_space
                        self.prec2.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec3"):
                        self.prec3 = value
                        self.prec3.value_namespace = name_space
                        self.prec3.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec4"):
                        self.prec4 = value
                        self.prec4.value_namespace = name_space
                        self.prec4.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec5"):
                        self.prec5 = value
                        self.prec5.value_namespace = name_space
                        self.prec5.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec6"):
                        self.prec6 = value
                        self.prec6.value_namespace = name_space
                        self.prec6.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec7"):
                        self.prec7 = value
                        self.prec7.value_namespace = name_space
                        self.prec7.value_namespace_prefix = name_space_prefix


            class MplsPriorityMask(Entity):
                """
                MPLS Priority Mask
                
                .. attribute:: prec0
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec1
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec2
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec3
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec4
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec5
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec6
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                .. attribute:: prec7
                
                	Prec
                	**type**\:  int
                
                	**range:** 0..1
                
                	**default value**\: 0
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.MplsPriorityMask, self).__init__()

                    self.yang_name = "mpls-priority-mask"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.prec0 = YLeaf(YType.uint32, "prec0")

                    self.prec1 = YLeaf(YType.uint32, "prec1")

                    self.prec2 = YLeaf(YType.uint32, "prec2")

                    self.prec3 = YLeaf(YType.uint32, "prec3")

                    self.prec4 = YLeaf(YType.uint32, "prec4")

                    self.prec5 = YLeaf(YType.uint32, "prec5")

                    self.prec6 = YLeaf(YType.uint32, "prec6")

                    self.prec7 = YLeaf(YType.uint32, "prec7")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prec0",
                                    "prec1",
                                    "prec2",
                                    "prec3",
                                    "prec4",
                                    "prec5",
                                    "prec6",
                                    "prec7") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.MplsPriorityMask, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.MplsPriorityMask, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prec0.is_set or
                        self.prec1.is_set or
                        self.prec2.is_set or
                        self.prec3.is_set or
                        self.prec4.is_set or
                        self.prec5.is_set or
                        self.prec6.is_set or
                        self.prec7.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prec0.yfilter != YFilter.not_set or
                        self.prec1.yfilter != YFilter.not_set or
                        self.prec2.yfilter != YFilter.not_set or
                        self.prec3.yfilter != YFilter.not_set or
                        self.prec4.yfilter != YFilter.not_set or
                        self.prec5.yfilter != YFilter.not_set or
                        self.prec6.yfilter != YFilter.not_set or
                        self.prec7.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mpls-priority-mask" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prec0.is_set or self.prec0.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec0.get_name_leafdata())
                    if (self.prec1.is_set or self.prec1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec1.get_name_leafdata())
                    if (self.prec2.is_set or self.prec2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec2.get_name_leafdata())
                    if (self.prec3.is_set or self.prec3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec3.get_name_leafdata())
                    if (self.prec4.is_set or self.prec4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec4.get_name_leafdata())
                    if (self.prec5.is_set or self.prec5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec5.get_name_leafdata())
                    if (self.prec6.is_set or self.prec6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec6.get_name_leafdata())
                    if (self.prec7.is_set or self.prec7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prec7.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prec0" or name == "prec1" or name == "prec2" or name == "prec3" or name == "prec4" or name == "prec5" or name == "prec6" or name == "prec7"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prec0"):
                        self.prec0 = value
                        self.prec0.value_namespace = name_space
                        self.prec0.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec1"):
                        self.prec1 = value
                        self.prec1.value_namespace = name_space
                        self.prec1.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec2"):
                        self.prec2 = value
                        self.prec2.value_namespace = name_space
                        self.prec2.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec3"):
                        self.prec3 = value
                        self.prec3.value_namespace = name_space
                        self.prec3.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec4"):
                        self.prec4 = value
                        self.prec4.value_namespace = name_space
                        self.prec4.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec5"):
                        self.prec5 = value
                        self.prec5.value_namespace = name_space
                        self.prec5.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec6"):
                        self.prec6 = value
                        self.prec6.value_namespace = name_space
                        self.prec6.value_namespace_prefix = name_space_prefix
                    if(value_path == "prec7"):
                        self.prec7 = value
                        self.prec7.value_namespace = name_space
                        self.prec7.value_namespace_prefix = name_space_prefix


            class MplsExp(Entity):
                """
                EFD MPLS parameters
                
                .. attribute:: exp
                
                	MPLS EXP threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation_
                
                	MPLS operation
                	**type**\:   :py:class:`Asr9KEfdOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperation>`
                
                	**default value**\: greater-than-or-equal
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleEfd.Nodes.Node.MplsExp, self).__init__()

                    self.yang_name = "mpls-exp"
                    self.yang_parent_name = "node"
                    self.is_presence_container = True

                    self.exp = YLeaf(YType.uint32, "exp")

                    self.operation_ = YLeaf(YType.enumeration, "operation")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("exp",
                                    "operation_") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModuleEfd.Nodes.Node.MplsExp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModuleEfd.Nodes.Node.MplsExp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.exp.is_set or
                        self.operation_.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.exp.yfilter != YFilter.not_set or
                        self.operation_.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mpls-exp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.exp.is_set or self.exp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.exp.get_name_leafdata())
                    if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operation_.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "exp" or name == "operation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "exp"):
                        self.exp = value
                        self.exp.value_namespace = name_space
                        self.exp.value_namespace_prefix = name_space_prefix
                    if(value_path == "operation"):
                        self.operation_ = value
                        self.operation_.value_namespace = name_space
                        self.operation_.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    self.enable.is_set or
                    self.mode.is_set or
                    (self.ip_precedence is not None) or
                    (self.ip_priority_mask is not None) or
                    (self.mpls_exp is not None) or
                    (self.mpls_priority_mask is not None) or
                    (self.vlan_cos is not None) or
                    (self.vlan_priority_mask is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.mode.yfilter != YFilter.not_set or
                    (self.ip_precedence is not None and self.ip_precedence.has_operation()) or
                    (self.ip_priority_mask is not None and self.ip_priority_mask.has_operation()) or
                    (self.mpls_exp is not None and self.mpls_exp.has_operation()) or
                    (self.mpls_priority_mask is not None and self.mpls_priority_mask.has_operation()) or
                    (self.vlan_cos is not None and self.vlan_cos.has_operation()) or
                    (self.vlan_priority_mask is not None and self.vlan_priority_mask.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ip-precedence"):
                    if (self.ip_precedence is None):
                        self.ip_precedence = HardwareModuleEfd.Nodes.Node.IpPrecedence()
                        self.ip_precedence.parent = self
                        self._children_name_map["ip_precedence"] = "ip-precedence"
                    return self.ip_precedence

                if (child_yang_name == "ip-priority-mask"):
                    if (self.ip_priority_mask is None):
                        self.ip_priority_mask = HardwareModuleEfd.Nodes.Node.IpPriorityMask()
                        self.ip_priority_mask.parent = self
                        self._children_name_map["ip_priority_mask"] = "ip-priority-mask"
                    return self.ip_priority_mask

                if (child_yang_name == "mpls-exp"):
                    if (self.mpls_exp is None):
                        self.mpls_exp = HardwareModuleEfd.Nodes.Node.MplsExp()
                        self.mpls_exp.parent = self
                        self._children_name_map["mpls_exp"] = "mpls-exp"
                    return self.mpls_exp

                if (child_yang_name == "mpls-priority-mask"):
                    if (self.mpls_priority_mask is None):
                        self.mpls_priority_mask = HardwareModuleEfd.Nodes.Node.MplsPriorityMask()
                        self.mpls_priority_mask.parent = self
                        self._children_name_map["mpls_priority_mask"] = "mpls-priority-mask"
                    return self.mpls_priority_mask

                if (child_yang_name == "vlan-cos"):
                    if (self.vlan_cos is None):
                        self.vlan_cos = HardwareModuleEfd.Nodes.Node.VlanCos()
                        self.vlan_cos.parent = self
                        self._children_name_map["vlan_cos"] = "vlan-cos"
                    return self.vlan_cos

                if (child_yang_name == "vlan-priority-mask"):
                    if (self.vlan_priority_mask is None):
                        self.vlan_priority_mask = HardwareModuleEfd.Nodes.Node.VlanPriorityMask()
                        self.vlan_priority_mask.parent = self
                        self._children_name_map["vlan_priority_mask"] = "vlan-priority-mask"
                    return self.vlan_priority_mask

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ip-precedence" or name == "ip-priority-mask" or name == "mpls-exp" or name == "mpls-priority-mask" or name == "vlan-cos" or name == "vlan-priority-mask" or name == "node-name" or name == "enable" or name == "mode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "mode"):
                    self.mode = value
                    self.mode.value_namespace = name_space
                    self.mode.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/%s" % self.get_segment_path()
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
                c = HardwareModuleEfd.Nodes.Node()
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
            (self.node_all is not None and self.node_all.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.node_all is not None and self.node_all.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd" + path_buffer

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

        if (child_yang_name == "node-all"):
            if (self.node_all is None):
                self.node_all = HardwareModuleEfd.NodeAll()
                self.node_all.parent = self
                self._children_name_map["node_all"] = "node-all"
            return self.node_all

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = HardwareModuleEfd.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "node-all" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HardwareModuleEfd()
        return self._top_entity

