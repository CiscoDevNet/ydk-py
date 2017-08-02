""" Cisco_IOS_XR_infra_rsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package operational data.

This module contains definitions
for the following management objects\:
  vrf\-group\: VRF group operational data
  srlg\: srlg
  selective\-vrf\-download\: selective vrf download

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Priority(Enum):
    """
    Priority

    Priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: medium = 2

    	Medium

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")


class Source(Enum):
    """
    Source

    Source

    .. data:: configured = 1

    	Configured

    .. data:: from_group = 2

    	From group

    .. data:: inherited = 4

    	Inherited

    .. data:: from_optical = 8

    	From optical

    .. data:: configured_and_notified = 17

    	Configured and notified

    .. data:: from_group_and_notified = 18

    	From group and notified

    .. data:: inherited_and_notified = 20

    	Inherited and notified

    .. data:: from_optical_and_notified = 24

    	From optical and notified

    """

    configured = Enum.YLeaf(1, "configured")

    from_group = Enum.YLeaf(2, "from-group")

    inherited = Enum.YLeaf(4, "inherited")

    from_optical = Enum.YLeaf(8, "from-optical")

    configured_and_notified = Enum.YLeaf(17, "configured-and-notified")

    from_group_and_notified = Enum.YLeaf(18, "from-group-and-notified")

    inherited_and_notified = Enum.YLeaf(20, "inherited-and-notified")

    from_optical_and_notified = Enum.YLeaf(24, "from-optical-and-notified")



class VrfGroup(Entity):
    """
    VRF group operational data
    
    .. attribute:: nodes
    
    	Node operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(VrfGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"

        self.nodes = VrfGroup.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node operational data
        
        .. attribute:: node
        
        	Node details
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(VrfGroup.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vrf-group"

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
                        super(VrfGroup.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(VrfGroup.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node details
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Group operational data
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(VrfGroup.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.groups = VrfGroup.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")

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
                            super(VrfGroup.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VrfGroup.Nodes.Node, self).__setattr__(name, value)


            class Groups(Entity):
                """
                Group operational data
                
                .. attribute:: group
                
                	Group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(VrfGroup.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"

                    self.group = YList(self)

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
                                super(VrfGroup.Nodes.Node.Groups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VrfGroup.Nodes.Node.Groups, self).__setattr__(name, value)


                class Group(Entity):
                    """
                    Group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: forward_reference
                    
                    	VRF group not present but used
                    	**type**\:  bool
                    
                    .. attribute:: vr_fs
                    
                    	Number of VRFs in this VRF group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF group's VRF
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group.Vrf>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(VrfGroup.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"

                        self.group_name = YLeaf(YType.str, "group-name")

                        self.forward_reference = YLeaf(YType.boolean, "forward-reference")

                        self.vr_fs = YLeaf(YType.uint32, "vr-fs")

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
                            if name in ("group_name",
                                        "forward_reference",
                                        "vr_fs") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(VrfGroup.Nodes.Node.Groups.Group, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(VrfGroup.Nodes.Node.Groups.Group, self).__setattr__(name, value)


                    class Vrf(Entity):
                        """
                        VRF group's VRF
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(VrfGroup.Nodes.Node.Groups.Group.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "group"

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
                                if name in ("vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(VrfGroup.Nodes.Node.Groups.Group.Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(VrfGroup.Nodes.Node.Groups.Group.Vrf, self).__setattr__(name, value)

                        def has_data(self):
                            return self.vrf_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
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
                            if(name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.vrf:
                            if (c.has_data()):
                                return True
                        return (
                            self.group_name.is_set or
                            self.forward_reference.is_set or
                            self.vr_fs.is_set)

                    def has_operation(self):
                        for c in self.vrf:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_name.yfilter != YFilter.not_set or
                            self.forward_reference.yfilter != YFilter.not_set or
                            self.vr_fs.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group" + "[group-name='" + self.group_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name.get_name_leafdata())
                        if (self.forward_reference.is_set or self.forward_reference.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.forward_reference.get_name_leafdata())
                        if (self.vr_fs.is_set or self.vr_fs.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vr_fs.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "vrf"):
                            for c in self.vrf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = VrfGroup.Nodes.Node.Groups.Group.Vrf()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.vrf.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf" or name == "group-name" or name == "forward-reference" or name == "vr-fs"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-name"):
                            self.group_name = value
                            self.group_name.value_namespace = name_space
                            self.group_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "forward-reference"):
                            self.forward_reference = value
                            self.forward_reference.value_namespace = name_space
                            self.forward_reference.value_namespace_prefix = name_space_prefix
                        if(value_path == "vr-fs"):
                            self.vr_fs = value
                            self.vr_fs.value_namespace = name_space
                            self.vr_fs.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "groups" + path_buffer

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

                    if (child_yang_name == "group"):
                        for c in self.group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = VrfGroup.Nodes.Node.Groups.Group()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.groups is not None and self.groups.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.groups is not None and self.groups.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-oper:vrf-group/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "groups"):
                    if (self.groups is None):
                        self.groups = VrfGroup.Nodes.Node.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                    return self.groups

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "groups" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-infra-rsi-oper:vrf-group/%s" % self.get_segment_path()
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
                c = VrfGroup.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-infra-rsi-oper:vrf-group" + path_buffer

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
                self.nodes = VrfGroup.Nodes()
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
        self._top_entity = VrfGroup()
        return self._top_entity

class Srlg(Entity):
    """
    srlg
    
    .. attribute:: interface_srlg_names
    
    	Set of SRLG names configured
    	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames>`
    
    .. attribute:: nodes
    
    	RSI SRLG operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes>`
    
    .. attribute:: srlg_maps
    
    	Set of SRLG name, value maps configured
    	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"

        self.interface_srlg_names = Srlg.InterfaceSrlgNames()
        self.interface_srlg_names.parent = self
        self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
        self._children_yang_names.add("interface-srlg-names")

        self.nodes = Srlg.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.srlg_maps = Srlg.SrlgMaps()
        self.srlg_maps.parent = self
        self._children_name_map["srlg_maps"] = "srlg-maps"
        self._children_yang_names.add("srlg-maps")


    class SrlgMaps(Entity):
        """
        Set of SRLG name, value maps configured
        
        .. attribute:: srlg_map
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps.SrlgMap>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Srlg.SrlgMaps, self).__init__()

            self.yang_name = "srlg-maps"
            self.yang_parent_name = "srlg"

            self.srlg_map = YList(self)

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
                        super(Srlg.SrlgMaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.SrlgMaps, self).__setattr__(name, value)


        class SrlgMap(Entity):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Srlg.SrlgMaps.SrlgMap, self).__init__()

                self.yang_name = "srlg-map"
                self.yang_parent_name = "srlg-maps"

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("srlg_name",
                                "srlg_name_xr",
                                "srlg_value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.SrlgMaps.SrlgMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.SrlgMaps.SrlgMap, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.srlg_name.is_set or
                    self.srlg_name_xr.is_set or
                    self.srlg_value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.srlg_name.yfilter != YFilter.not_set or
                    self.srlg_name_xr.yfilter != YFilter.not_set or
                    self.srlg_value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "srlg-map" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/srlg-maps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_name.get_name_leafdata())
                if (self.srlg_name_xr.is_set or self.srlg_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_name_xr.get_name_leafdata())
                if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "srlg-name" or name == "srlg-name-xr" or name == "srlg-value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "srlg-name"):
                    self.srlg_name = value
                    self.srlg_name.value_namespace = name_space
                    self.srlg_name.value_namespace_prefix = name_space_prefix
                if(value_path == "srlg-name-xr"):
                    self.srlg_name_xr = value
                    self.srlg_name_xr.value_namespace = name_space
                    self.srlg_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "srlg-value"):
                    self.srlg_value = value
                    self.srlg_value.value_namespace = name_space
                    self.srlg_value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.srlg_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.srlg_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "srlg-maps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "srlg-map"):
                for c in self.srlg_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Srlg.SrlgMaps.SrlgMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.srlg_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "srlg-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nodes(Entity):
        """
        RSI SRLG operational data
        
        .. attribute:: node
        
        	RSI SRLG operational data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Srlg.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "srlg"

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
                        super(Srlg.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            RSI SRLG operational data
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Set of Groups configured for SRLG
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups>`
            
            .. attribute:: inherit_nodes
            
            	Set of inherit locations configured for SRLG
            	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes>`
            
            .. attribute:: interface_details
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails>`
            
            .. attribute:: interface_srlg_names
            
            	Set of SRLG names configured
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames>`
            
            .. attribute:: interfaces
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces>`
            
            .. attribute:: srlg_maps
            
            	Set of SRLG name, value maps configured
            	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps>`
            
            .. attribute:: srlg_values
            
            	Set of SRLG values configured
            	**type**\:   :py:class:`SrlgValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Srlg.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.groups = Srlg.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")

                self.inherit_nodes = Srlg.Nodes.Node.InheritNodes()
                self.inherit_nodes.parent = self
                self._children_name_map["inherit_nodes"] = "inherit-nodes"
                self._children_yang_names.add("inherit-nodes")

                self.interface_details = Srlg.Nodes.Node.InterfaceDetails()
                self.interface_details.parent = self
                self._children_name_map["interface_details"] = "interface-details"
                self._children_yang_names.add("interface-details")

                self.interface_srlg_names = Srlg.Nodes.Node.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._children_yang_names.add("interface-srlg-names")

                self.interfaces = Srlg.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.srlg_maps = Srlg.Nodes.Node.SrlgMaps()
                self.srlg_maps.parent = self
                self._children_name_map["srlg_maps"] = "srlg-maps"
                self._children_yang_names.add("srlg-maps")

                self.srlg_values = Srlg.Nodes.Node.SrlgValues()
                self.srlg_values.parent = self
                self._children_name_map["srlg_values"] = "srlg-values"
                self._children_yang_names.add("srlg-values")

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
                            super(Srlg.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.Nodes.Node, self).__setattr__(name, value)


            class SrlgMaps(Entity):
                """
                Set of SRLG name, value maps configured
                
                .. attribute:: srlg_map
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps.SrlgMap>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.SrlgMaps, self).__init__()

                    self.yang_name = "srlg-maps"
                    self.yang_parent_name = "node"

                    self.srlg_map = YList(self)

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
                                super(Srlg.Nodes.Node.SrlgMaps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.SrlgMaps, self).__setattr__(name, value)


                class SrlgMap(Entity):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.SrlgMaps.SrlgMap, self).__init__()

                        self.yang_name = "srlg-map"
                        self.yang_parent_name = "srlg-maps"

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                        self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("srlg_name",
                                        "srlg_name_xr",
                                        "srlg_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.SrlgMaps.SrlgMap, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.SrlgMaps.SrlgMap, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.srlg_name.is_set or
                            self.srlg_name_xr.is_set or
                            self.srlg_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_name.yfilter != YFilter.not_set or
                            self.srlg_name_xr.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "srlg-map" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_name.get_name_leafdata())
                        if (self.srlg_name_xr.is_set or self.srlg_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_name_xr.get_name_leafdata())
                        if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-name" or name == "srlg-name-xr" or name == "srlg-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-name"):
                            self.srlg_name = value
                            self.srlg_name.value_namespace = name_space
                            self.srlg_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-name-xr"):
                            self.srlg_name_xr = value
                            self.srlg_name_xr.value_namespace = name_space
                            self.srlg_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value = value
                            self.srlg_value.value_namespace = name_space
                            self.srlg_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.srlg_map:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.srlg_map:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "srlg-maps" + path_buffer

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

                    if (child_yang_name == "srlg-map"):
                        for c in self.srlg_map:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.SrlgMaps.SrlgMap()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.srlg_map.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "srlg-map"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Groups(Entity):
                """
                Set of Groups configured for SRLG
                
                .. attribute:: group
                
                	SRLG group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"

                    self.group = YList(self)

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
                                super(Srlg.Nodes.Node.Groups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.Groups, self).__setattr__(name, value)


                class Group(Entity):
                    """
                    SRLG group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_name_xr
                    
                    	Group name
                    	**type**\:  str
                    
                    .. attribute:: group_values
                    
                    	Group values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"

                        self.group_name = YLeaf(YType.str, "group-name")

                        self.group_name_xr = YLeaf(YType.str, "group-name-xr")

                        self.group_values = YLeaf(YType.uint32, "group-values")

                        self.srlg_attribute = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group_name",
                                        "group_name_xr",
                                        "group_values") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.Groups.Group, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.Groups.Group, self).__setattr__(name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "group"

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("priority",
                                            "srlg_index",
                                            "srlg_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.priority.is_set or
                                self.srlg_index.is_set or
                                self.srlg_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.srlg_index.yfilter != YFilter.not_set or
                                self.srlg_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srlg-attribute" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_index.get_name_leafdata())
                            if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "priority" or name == "srlg-index" or name == "srlg-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-index"):
                                self.srlg_index = value
                                self.srlg_index.value_namespace = name_space
                                self.srlg_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-value"):
                                self.srlg_value = value
                                self.srlg_value.value_namespace = name_space
                                self.srlg_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.srlg_attribute:
                            if (c.has_data()):
                                return True
                        return (
                            self.group_name.is_set or
                            self.group_name_xr.is_set or
                            self.group_values.is_set)

                    def has_operation(self):
                        for c in self.srlg_attribute:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_name.yfilter != YFilter.not_set or
                            self.group_name_xr.yfilter != YFilter.not_set or
                            self.group_values.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group" + "[group-name='" + self.group_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name.get_name_leafdata())
                        if (self.group_name_xr.is_set or self.group_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_xr.get_name_leafdata())
                        if (self.group_values.is_set or self.group_values.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_values.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "srlg-attribute"):
                            for c in self.srlg_attribute:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Srlg.Nodes.Node.Groups.Group.SrlgAttribute()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.srlg_attribute.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-attribute" or name == "group-name" or name == "group-name-xr" or name == "group-values"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-name"):
                            self.group_name = value
                            self.group_name.value_namespace = name_space
                            self.group_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-xr"):
                            self.group_name_xr = value
                            self.group_name_xr.value_namespace = name_space
                            self.group_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-values"):
                            self.group_values = value
                            self.group_values.value_namespace = name_space
                            self.group_values.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "groups" + path_buffer

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

                    if (child_yang_name == "group"):
                        for c in self.group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.Groups.Group()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InheritNodes(Entity):
                """
                Set of inherit locations configured for SRLG
                
                .. attribute:: inherit_node
                
                	SRLG inherit location details
                	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.InheritNodes, self).__init__()

                    self.yang_name = "inherit-nodes"
                    self.yang_parent_name = "node"

                    self.inherit_node = YList(self)

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
                                super(Srlg.Nodes.Node.InheritNodes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.InheritNodes, self).__setattr__(name, value)


                class InheritNode(Entity):
                    """
                    SRLG inherit location details
                    
                    .. attribute:: inherit_node_name  <key>
                    
                    	Inherit node
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: node_name
                    
                    	Inherit node name
                    	**type**\:  str
                    
                    .. attribute:: node_values
                    
                    	Node values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InheritNodes.InheritNode, self).__init__()

                        self.yang_name = "inherit-node"
                        self.yang_parent_name = "inherit-nodes"

                        self.inherit_node_name = YLeaf(YType.str, "inherit-node-name")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.node_values = YLeaf(YType.uint32, "node-values")

                        self.srlg_attribute = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("inherit_node_name",
                                        "node_name",
                                        "node_values") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.InheritNodes.InheritNode, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.InheritNodes.InheritNode, self).__setattr__(name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "inherit-node"

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("priority",
                                            "srlg_index",
                                            "srlg_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.priority.is_set or
                                self.srlg_index.is_set or
                                self.srlg_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.srlg_index.yfilter != YFilter.not_set or
                                self.srlg_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srlg-attribute" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_index.get_name_leafdata())
                            if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "priority" or name == "srlg-index" or name == "srlg-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-index"):
                                self.srlg_index = value
                                self.srlg_index.value_namespace = name_space
                                self.srlg_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-value"):
                                self.srlg_value = value
                                self.srlg_value.value_namespace = name_space
                                self.srlg_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.srlg_attribute:
                            if (c.has_data()):
                                return True
                        return (
                            self.inherit_node_name.is_set or
                            self.node_name.is_set or
                            self.node_values.is_set)

                    def has_operation(self):
                        for c in self.srlg_attribute:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.inherit_node_name.yfilter != YFilter.not_set or
                            self.node_name.yfilter != YFilter.not_set or
                            self.node_values.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inherit-node" + "[inherit-node-name='" + self.inherit_node_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.inherit_node_name.is_set or self.inherit_node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inherit_node_name.get_name_leafdata())
                        if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_name.get_name_leafdata())
                        if (self.node_values.is_set or self.node_values.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_values.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "srlg-attribute"):
                            for c in self.srlg_attribute:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.srlg_attribute.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-attribute" or name == "inherit-node-name" or name == "node-name" or name == "node-values"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "inherit-node-name"):
                            self.inherit_node_name = value
                            self.inherit_node_name.value_namespace = name_space
                            self.inherit_node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-name"):
                            self.node_name = value
                            self.node_name.value_namespace = name_space
                            self.node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-values"):
                            self.node_values = value
                            self.node_values.value_namespace = name_space
                            self.node_values.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.inherit_node:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.inherit_node:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "inherit-nodes" + path_buffer

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

                    if (child_yang_name == "inherit-node"):
                        for c in self.inherit_node:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.InheritNodes.InheritNode()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.inherit_node.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inherit-node"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface
                
                	SRLG interface summary
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.Interfaces, self).__init__()

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
                                super(Srlg.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    SRLG interface summary
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: registrations
                    
                    	Registrations
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_value
                    
                    	SRLG values
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: value_count
                    
                    	Values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.registrations = YLeaf(YType.uint32, "registrations")

                        self.srlg_value = YLeafList(YType.uint32, "srlg-value")

                        self.value_count = YLeaf(YType.uint32, "value-count")

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
                                        "interface_name_xr",
                                        "registrations",
                                        "srlg_value",
                                        "value_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.srlg_value.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.interface_name_xr.is_set or
                            self.registrations.is_set or
                            self.value_count.is_set)

                    def has_operation(self):
                        for leaf in self.srlg_value.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.registrations.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set or
                            self.value_count.yfilter != YFilter.not_set)

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
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.registrations.is_set or self.registrations.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.registrations.get_name_leafdata())
                        if (self.value_count.is_set or self.value_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value_count.get_name_leafdata())

                        leaf_name_data.extend(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "interface-name-xr" or name == "registrations" or name == "srlg-value" or name == "value-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "registrations"):
                            self.registrations = value
                            self.registrations.value_namespace = name_space
                            self.registrations.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value.append(value)
                        if(value_path == "value-count"):
                            self.value_count = value
                            self.value_count.value_namespace = name_space
                            self.value_count.value_namespace_prefix = name_space_prefix

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
                        c = Srlg.Nodes.Node.Interfaces.Interface()
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


            class InterfaceDetails(Entity):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface_detail
                
                	SRLG interface details
                	**type**\: list of    :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.InterfaceDetails, self).__init__()

                    self.yang_name = "interface-details"
                    self.yang_parent_name = "node"

                    self.interface_detail = YList(self)

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
                                super(Srlg.Nodes.Node.InterfaceDetails, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.InterfaceDetails, self).__setattr__(name, value)


                class InterfaceDetail(Entity):
                    """
                    SRLG interface details
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: groups
                    
                    	Groups
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nodes
                    
                    	Nodes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attributes
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, self).__init__()

                        self.yang_name = "interface-detail"
                        self.yang_parent_name = "interface-details"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.groups = YLeaf(YType.uint32, "groups")

                        self.nodes = YLeaf(YType.uint32, "nodes")

                        self.srlg_attribute = YList(self)

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
                                        "groups",
                                        "nodes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, self).__setattr__(name, value)


                    class SrlgAttribute(Entity):
                        """
                        SRLG attributes
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Source>`
                        
                        .. attribute:: source_name
                        
                        	Source name
                        	**type**\:  str
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "interface-detail"

                            self.priority = YLeaf(YType.enumeration, "priority")

                            self.source = YLeaf(YType.enumeration, "source")

                            self.source_name = YLeaf(YType.str, "source-name")

                            self.srlg_index = YLeaf(YType.uint16, "srlg-index")

                            self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("priority",
                                            "source",
                                            "source_name",
                                            "srlg_index",
                                            "srlg_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.priority.is_set or
                                self.source.is_set or
                                self.source_name.is_set or
                                self.srlg_index.is_set or
                                self.srlg_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.source.yfilter != YFilter.not_set or
                                self.source_name.yfilter != YFilter.not_set or
                                self.srlg_index.yfilter != YFilter.not_set or
                                self.srlg_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srlg-attribute" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source.get_name_leafdata())
                            if (self.source_name.is_set or self.source_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_name.get_name_leafdata())
                            if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_index.get_name_leafdata())
                            if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "priority" or name == "source" or name == "source-name" or name == "srlg-index" or name == "srlg-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "source"):
                                self.source = value
                                self.source.value_namespace = name_space
                                self.source.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-name"):
                                self.source_name = value
                                self.source_name.value_namespace = name_space
                                self.source_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-index"):
                                self.srlg_index = value
                                self.srlg_index.value_namespace = name_space
                                self.srlg_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-value"):
                                self.srlg_value = value
                                self.srlg_value.value_namespace = name_space
                                self.srlg_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.srlg_attribute:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.groups.is_set or
                            self.nodes.is_set)

                    def has_operation(self):
                        for c in self.srlg_attribute:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.groups.yfilter != YFilter.not_set or
                            self.nodes.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-detail" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.groups.is_set or self.groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.groups.get_name_leafdata())
                        if (self.nodes.is_set or self.nodes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nodes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "srlg-attribute"):
                            for c in self.srlg_attribute:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.srlg_attribute.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-attribute" or name == "interface-name" or name == "groups" or name == "nodes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "groups"):
                            self.groups = value
                            self.groups.value_namespace = name_space
                            self.groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "nodes"):
                            self.nodes = value
                            self.nodes.value_namespace = name_space
                            self.nodes.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_detail:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_detail:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-details" + path_buffer

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

                    if (child_yang_name == "interface-detail"):
                        for c in self.interface_detail:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_detail.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-detail"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class SrlgValues(Entity):
                """
                Set of SRLG values configured
                
                .. attribute:: srlg_value
                
                	Configured SRLG value details 
                	**type**\: list of    :py:class:`SrlgValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues.SrlgValue>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.SrlgValues, self).__init__()

                    self.yang_name = "srlg-values"
                    self.yang_parent_name = "node"

                    self.srlg_value = YList(self)

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
                                super(Srlg.Nodes.Node.SrlgValues, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.SrlgValues, self).__setattr__(name, value)


                class SrlgValue(Entity):
                    """
                    Configured SRLG value details 
                    
                    .. attribute:: value  <key>
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.SrlgValues.SrlgValue, self).__init__()

                        self.yang_name = "srlg-value"
                        self.yang_parent_name = "srlg-values"

                        self.value = YLeaf(YType.int32, "value")

                        self.interface_name = YLeafList(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("value",
                                        "interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.SrlgValues.SrlgValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.SrlgValues.SrlgValue, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.interface_name.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.value.is_set

                    def has_operation(self):
                        for leaf in self.interface_name.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "srlg-value" + "[value='" + self.value.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value.get_name_leafdata())

                        leaf_name_data.extend(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "value" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name.append(value)

                def has_data(self):
                    for c in self.srlg_value:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.srlg_value:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "srlg-values" + path_buffer

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

                    if (child_yang_name == "srlg-value"):
                        for c in self.srlg_value:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.SrlgValues.SrlgValue()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.srlg_value.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "srlg-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InterfaceSrlgNames(Entity):
                """
                Set of SRLG names configured
                
                .. attribute:: interface_srlg_name
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.Nodes.Node.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "node"

                    self.interface_srlg_name = YList(self)

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
                                super(Srlg.Nodes.Node.InterfaceSrlgNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Nodes.Node.InterfaceSrlgNames, self).__setattr__(name, value)


                class InterfaceSrlgName(Entity):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interfaces
                    
                    	Interfaces information
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                        self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                        self.interfaces = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
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
                            if name in ("srlg_name",
                                        "srlg_name_xr",
                                        "srlg_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)


                    class Interfaces(Entity):
                        """
                        Interfaces information
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-srlg-name"

                            self.interface_name = YLeafList(YType.str, "interface-name")

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
                                        super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.interface_name.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.interface_name.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

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

                            leaf_name_data.extend(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name.append(value)

                    def has_data(self):
                        return (
                            self.srlg_name.is_set or
                            self.srlg_name_xr.is_set or
                            self.srlg_value.is_set or
                            (self.interfaces is not None and self.interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_name.yfilter != YFilter.not_set or
                            self.srlg_name_xr.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set or
                            (self.interfaces is not None and self.interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_name.get_name_leafdata())
                        if (self.srlg_name_xr.is_set or self.srlg_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_name_xr.get_name_leafdata())
                        if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interfaces"):
                            if (self.interfaces is None):
                                self.interfaces = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                            return self.interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interfaces" or name == "srlg-name" or name == "srlg-name-xr" or name == "srlg-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-name"):
                            self.srlg_name = value
                            self.srlg_name.value_namespace = name_space
                            self.srlg_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-name-xr"):
                            self.srlg_name_xr = value
                            self.srlg_name_xr.value_namespace = name_space
                            self.srlg_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value = value
                            self.srlg_value.value_namespace = name_space
                            self.srlg_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_srlg_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_srlg_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-srlg-names" + path_buffer

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

                    if (child_yang_name == "interface-srlg-name"):
                        for c in self.interface_srlg_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_srlg_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-srlg-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.groups is not None and self.groups.has_data()) or
                    (self.inherit_nodes is not None and self.inherit_nodes.has_data()) or
                    (self.interface_details is not None and self.interface_details.has_data()) or
                    (self.interface_srlg_names is not None and self.interface_srlg_names.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.srlg_maps is not None and self.srlg_maps.has_data()) or
                    (self.srlg_values is not None and self.srlg_values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.groups is not None and self.groups.has_operation()) or
                    (self.inherit_nodes is not None and self.inherit_nodes.has_operation()) or
                    (self.interface_details is not None and self.interface_details.has_operation()) or
                    (self.interface_srlg_names is not None and self.interface_srlg_names.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.srlg_maps is not None and self.srlg_maps.has_operation()) or
                    (self.srlg_values is not None and self.srlg_values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "groups"):
                    if (self.groups is None):
                        self.groups = Srlg.Nodes.Node.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                    return self.groups

                if (child_yang_name == "inherit-nodes"):
                    if (self.inherit_nodes is None):
                        self.inherit_nodes = Srlg.Nodes.Node.InheritNodes()
                        self.inherit_nodes.parent = self
                        self._children_name_map["inherit_nodes"] = "inherit-nodes"
                    return self.inherit_nodes

                if (child_yang_name == "interface-details"):
                    if (self.interface_details is None):
                        self.interface_details = Srlg.Nodes.Node.InterfaceDetails()
                        self.interface_details.parent = self
                        self._children_name_map["interface_details"] = "interface-details"
                    return self.interface_details

                if (child_yang_name == "interface-srlg-names"):
                    if (self.interface_srlg_names is None):
                        self.interface_srlg_names = Srlg.Nodes.Node.InterfaceSrlgNames()
                        self.interface_srlg_names.parent = self
                        self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                    return self.interface_srlg_names

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Srlg.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "srlg-maps"):
                    if (self.srlg_maps is None):
                        self.srlg_maps = Srlg.Nodes.Node.SrlgMaps()
                        self.srlg_maps.parent = self
                        self._children_name_map["srlg_maps"] = "srlg-maps"
                    return self.srlg_maps

                if (child_yang_name == "srlg-values"):
                    if (self.srlg_values is None):
                        self.srlg_values = Srlg.Nodes.Node.SrlgValues()
                        self.srlg_values.parent = self
                        self._children_name_map["srlg_values"] = "srlg-values"
                    return self.srlg_values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "groups" or name == "inherit-nodes" or name == "interface-details" or name == "interface-srlg-names" or name == "interfaces" or name == "srlg-maps" or name == "srlg-values" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self.get_segment_path()
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
                c = Srlg.Nodes.Node()
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


    class InterfaceSrlgNames(Entity):
        """
        Set of SRLG names configured
        
        .. attribute:: interface_srlg_name
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Srlg.InterfaceSrlgNames, self).__init__()

            self.yang_name = "interface-srlg-names"
            self.yang_parent_name = "srlg"

            self.interface_srlg_name = YList(self)

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
                        super(Srlg.InterfaceSrlgNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.InterfaceSrlgNames, self).__setattr__(name, value)


        class InterfaceSrlgName(Entity):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: interfaces
            
            	Interfaces information
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Srlg.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                self.yang_name = "interface-srlg-name"
                self.yang_parent_name = "interface-srlg-names"

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_name_xr = YLeaf(YType.str, "srlg-name-xr")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                self.interfaces = Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
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
                    if name in ("srlg_name",
                                "srlg_name_xr",
                                "srlg_value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)


            class Interfaces(Entity):
                """
                Interfaces information
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  list of str
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "interface-srlg-name"

                    self.interface_name = YLeafList(YType.str, "interface-name")

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
                                super(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.interface_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return False

                def has_operation(self):
                    for leaf in self.interface_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

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

                    leaf_name_data.extend(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name.append(value)

            def has_data(self):
                return (
                    self.srlg_name.is_set or
                    self.srlg_name_xr.is_set or
                    self.srlg_value.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.srlg_name.yfilter != YFilter.not_set or
                    self.srlg_name_xr.yfilter != YFilter.not_set or
                    self.srlg_value.yfilter != YFilter.not_set or
                    (self.interfaces is not None and self.interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/interface-srlg-names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_name.get_name_leafdata())
                if (self.srlg_name_xr.is_set or self.srlg_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_name_xr.get_name_leafdata())
                if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interfaces" or name == "srlg-name" or name == "srlg-name-xr" or name == "srlg-value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "srlg-name"):
                    self.srlg_name = value
                    self.srlg_name.value_namespace = name_space
                    self.srlg_name.value_namespace_prefix = name_space_prefix
                if(value_path == "srlg-name-xr"):
                    self.srlg_name_xr = value
                    self.srlg_name_xr.value_namespace = name_space
                    self.srlg_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "srlg-value"):
                    self.srlg_value = value
                    self.srlg_value.value_namespace = name_space
                    self.srlg_value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface_srlg_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface_srlg_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface-srlg-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface-srlg-name"):
                for c in self.interface_srlg_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Srlg.InterfaceSrlgNames.InterfaceSrlgName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface_srlg_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-srlg-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.interface_srlg_names is not None and self.interface_srlg_names.has_data()) or
            (self.nodes is not None and self.nodes.has_data()) or
            (self.srlg_maps is not None and self.srlg_maps.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interface_srlg_names is not None and self.interface_srlg_names.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()) or
            (self.srlg_maps is not None and self.srlg_maps.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-oper:srlg" + path_buffer

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

        if (child_yang_name == "interface-srlg-names"):
            if (self.interface_srlg_names is None):
                self.interface_srlg_names = Srlg.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
            return self.interface_srlg_names

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Srlg.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        if (child_yang_name == "srlg-maps"):
            if (self.srlg_maps is None):
                self.srlg_maps = Srlg.SrlgMaps()
                self.srlg_maps.parent = self
                self._children_name_map["srlg_maps"] = "srlg-maps"
            return self.srlg_maps

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interface-srlg-names" or name == "nodes" or name == "srlg-maps"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

class SelectiveVrfDownload(Entity):
    """
    selective vrf download
    
    .. attribute:: state
    
    	Selective VRF Download feature state details
    	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.SelectiveVrfDownload.State>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"

        self.state = SelectiveVrfDownload.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")


    class State(Entity):
        """
        Selective VRF Download feature state details
        
        .. attribute:: is_svd_enabled
        
        	Is SVD Enabled Operational
        	**type**\:  bool
        
        .. attribute:: is_svd_enabled_cfg
        
        	Is SVD Enabled Config
        	**type**\:  bool
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(SelectiveVrfDownload.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "selective-vrf-download"

            self.is_svd_enabled = YLeaf(YType.boolean, "is-svd-enabled")

            self.is_svd_enabled_cfg = YLeaf(YType.boolean, "is-svd-enabled-cfg")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("is_svd_enabled",
                            "is_svd_enabled_cfg") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SelectiveVrfDownload.State, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SelectiveVrfDownload.State, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.is_svd_enabled.is_set or
                self.is_svd_enabled_cfg.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.is_svd_enabled.yfilter != YFilter.not_set or
                self.is_svd_enabled_cfg.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "state" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.is_svd_enabled.is_set or self.is_svd_enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.is_svd_enabled.get_name_leafdata())
            if (self.is_svd_enabled_cfg.is_set or self.is_svd_enabled_cfg.yfilter != YFilter.not_set):
                leaf_name_data.append(self.is_svd_enabled_cfg.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "is-svd-enabled" or name == "is-svd-enabled-cfg"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "is-svd-enabled"):
                self.is_svd_enabled = value
                self.is_svd_enabled.value_namespace = name_space
                self.is_svd_enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "is-svd-enabled-cfg"):
                self.is_svd_enabled_cfg = value
                self.is_svd_enabled_cfg.value_namespace = name_space
                self.is_svd_enabled_cfg.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.state is not None and self.state.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.state is not None and self.state.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download" + path_buffer

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

        if (child_yang_name == "state"):
            if (self.state is None):
                self.state = SelectiveVrfDownload.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
            return self.state

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "state"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

