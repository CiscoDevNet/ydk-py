""" Cisco_IOS_XR_cmproxy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cmproxy package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\-vm\: Platform VM information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SdrInventoryVm(Entity):
    """
    Platform VM information
    
    .. attribute:: nodes
    
    	Node directory
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes>`
    
    

    """

    _prefix = 'cmproxy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SdrInventoryVm, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory-vm"
        self.yang_parent_name = "Cisco-IOS-XR-cmproxy-oper"

        self.nodes = SdrInventoryVm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node directory
        
        .. attribute:: node
        
        	Node name
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node>`
        
        

        """

        _prefix = 'cmproxy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SdrInventoryVm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "sdr-inventory-vm"

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
                        super(SdrInventoryVm.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SdrInventoryVm.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node name
            
            .. attribute:: name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: node_entries
            
            	VM Information
            	**type**\:   :py:class:`NodeEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries>`
            
            

            """

            _prefix = 'cmproxy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SdrInventoryVm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.name = YLeaf(YType.str, "name")

                self.node_entries = SdrInventoryVm.Nodes.Node.NodeEntries()
                self.node_entries.parent = self
                self._children_name_map["node_entries"] = "node-entries"
                self._children_yang_names.add("node-entries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SdrInventoryVm.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SdrInventoryVm.Nodes.Node, self).__setattr__(name, value)


            class NodeEntries(Entity):
                """
                VM Information
                
                .. attribute:: node_entry
                
                	VM information for a node
                	**type**\: list of    :py:class:`NodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry>`
                
                

                """

                _prefix = 'cmproxy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SdrInventoryVm.Nodes.Node.NodeEntries, self).__init__()

                    self.yang_name = "node-entries"
                    self.yang_parent_name = "node"

                    self.node_entry = YList(self)

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
                                super(SdrInventoryVm.Nodes.Node.NodeEntries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SdrInventoryVm.Nodes.Node.NodeEntries, self).__setattr__(name, value)


                class NodeEntry(Entity):
                    """
                    VM information for a node
                    
                    .. attribute:: name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: card_type_string
                    
                    	card type string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_ip
                    
                    	node IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_ipv4_string
                    
                    	node IPv4 address string
                    	**type**\:  str
                    
                    	**length:** 0..16
                    
                    .. attribute:: node_name
                    
                    	node name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_sw_state
                    
                    	current software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_sw_state_string
                    
                    	current software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: nodeid
                    
                    	node ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_id
                    
                    	partner node id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_name
                    
                    	partner name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prev_sw_state
                    
                    	previous software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prev_sw_state_string
                    
                    	previous software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: red_state
                    
                    	redundancy state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: red_state_string
                    
                    	redundancy state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: valid
                    
                    	valid flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cmproxy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, self).__init__()

                        self.yang_name = "node-entry"
                        self.yang_parent_name = "node-entries"

                        self.name = YLeaf(YType.str, "name")

                        self.card_type = YLeaf(YType.uint32, "card-type")

                        self.card_type_string = YLeaf(YType.str, "card-type-string")

                        self.node_ip = YLeaf(YType.uint32, "node-ip")

                        self.node_ipv4_string = YLeaf(YType.str, "node-ipv4-string")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.node_sw_state = YLeaf(YType.uint32, "node-sw-state")

                        self.node_sw_state_string = YLeaf(YType.str, "node-sw-state-string")

                        self.nodeid = YLeaf(YType.int32, "nodeid")

                        self.partner_id = YLeaf(YType.int32, "partner-id")

                        self.partner_name = YLeaf(YType.str, "partner-name")

                        self.prev_sw_state = YLeaf(YType.uint32, "prev-sw-state")

                        self.prev_sw_state_string = YLeaf(YType.str, "prev-sw-state-string")

                        self.red_state = YLeaf(YType.uint32, "red-state")

                        self.red_state_string = YLeaf(YType.str, "red-state-string")

                        self.valid = YLeaf(YType.uint32, "valid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name",
                                        "card_type",
                                        "card_type_string",
                                        "node_ip",
                                        "node_ipv4_string",
                                        "node_name",
                                        "node_sw_state",
                                        "node_sw_state_string",
                                        "nodeid",
                                        "partner_id",
                                        "partner_name",
                                        "prev_sw_state",
                                        "prev_sw_state_string",
                                        "red_state",
                                        "red_state_string",
                                        "valid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.card_type.is_set or
                            self.card_type_string.is_set or
                            self.node_ip.is_set or
                            self.node_ipv4_string.is_set or
                            self.node_name.is_set or
                            self.node_sw_state.is_set or
                            self.node_sw_state_string.is_set or
                            self.nodeid.is_set or
                            self.partner_id.is_set or
                            self.partner_name.is_set or
                            self.prev_sw_state.is_set or
                            self.prev_sw_state_string.is_set or
                            self.red_state.is_set or
                            self.red_state_string.is_set or
                            self.valid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.card_type.yfilter != YFilter.not_set or
                            self.card_type_string.yfilter != YFilter.not_set or
                            self.node_ip.yfilter != YFilter.not_set or
                            self.node_ipv4_string.yfilter != YFilter.not_set or
                            self.node_name.yfilter != YFilter.not_set or
                            self.node_sw_state.yfilter != YFilter.not_set or
                            self.node_sw_state_string.yfilter != YFilter.not_set or
                            self.nodeid.yfilter != YFilter.not_set or
                            self.partner_id.yfilter != YFilter.not_set or
                            self.partner_name.yfilter != YFilter.not_set or
                            self.prev_sw_state.yfilter != YFilter.not_set or
                            self.prev_sw_state_string.yfilter != YFilter.not_set or
                            self.red_state.yfilter != YFilter.not_set or
                            self.red_state_string.yfilter != YFilter.not_set or
                            self.valid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node-entry" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_type.get_name_leafdata())
                        if (self.card_type_string.is_set or self.card_type_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_type_string.get_name_leafdata())
                        if (self.node_ip.is_set or self.node_ip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_ip.get_name_leafdata())
                        if (self.node_ipv4_string.is_set or self.node_ipv4_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_ipv4_string.get_name_leafdata())
                        if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_name.get_name_leafdata())
                        if (self.node_sw_state.is_set or self.node_sw_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_sw_state.get_name_leafdata())
                        if (self.node_sw_state_string.is_set or self.node_sw_state_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_sw_state_string.get_name_leafdata())
                        if (self.nodeid.is_set or self.nodeid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nodeid.get_name_leafdata())
                        if (self.partner_id.is_set or self.partner_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.partner_id.get_name_leafdata())
                        if (self.partner_name.is_set or self.partner_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.partner_name.get_name_leafdata())
                        if (self.prev_sw_state.is_set or self.prev_sw_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prev_sw_state.get_name_leafdata())
                        if (self.prev_sw_state_string.is_set or self.prev_sw_state_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prev_sw_state_string.get_name_leafdata())
                        if (self.red_state.is_set or self.red_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.red_state.get_name_leafdata())
                        if (self.red_state_string.is_set or self.red_state_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.red_state_string.get_name_leafdata())
                        if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.valid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name" or name == "card-type" or name == "card-type-string" or name == "node-ip" or name == "node-ipv4-string" or name == "node-name" or name == "node-sw-state" or name == "node-sw-state-string" or name == "nodeid" or name == "partner-id" or name == "partner-name" or name == "prev-sw-state" or name == "prev-sw-state-string" or name == "red-state" or name == "red-state-string" or name == "valid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "card-type"):
                            self.card_type = value
                            self.card_type.value_namespace = name_space
                            self.card_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "card-type-string"):
                            self.card_type_string = value
                            self.card_type_string.value_namespace = name_space
                            self.card_type_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-ip"):
                            self.node_ip = value
                            self.node_ip.value_namespace = name_space
                            self.node_ip.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-ipv4-string"):
                            self.node_ipv4_string = value
                            self.node_ipv4_string.value_namespace = name_space
                            self.node_ipv4_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-name"):
                            self.node_name = value
                            self.node_name.value_namespace = name_space
                            self.node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-sw-state"):
                            self.node_sw_state = value
                            self.node_sw_state.value_namespace = name_space
                            self.node_sw_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "node-sw-state-string"):
                            self.node_sw_state_string = value
                            self.node_sw_state_string.value_namespace = name_space
                            self.node_sw_state_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "nodeid"):
                            self.nodeid = value
                            self.nodeid.value_namespace = name_space
                            self.nodeid.value_namespace_prefix = name_space_prefix
                        if(value_path == "partner-id"):
                            self.partner_id = value
                            self.partner_id.value_namespace = name_space
                            self.partner_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "partner-name"):
                            self.partner_name = value
                            self.partner_name.value_namespace = name_space
                            self.partner_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "prev-sw-state"):
                            self.prev_sw_state = value
                            self.prev_sw_state.value_namespace = name_space
                            self.prev_sw_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "prev-sw-state-string"):
                            self.prev_sw_state_string = value
                            self.prev_sw_state_string.value_namespace = name_space
                            self.prev_sw_state_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "red-state"):
                            self.red_state = value
                            self.red_state.value_namespace = name_space
                            self.red_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "red-state-string"):
                            self.red_state_string = value
                            self.red_state_string.value_namespace = name_space
                            self.red_state_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "valid"):
                            self.valid = value
                            self.valid.value_namespace = name_space
                            self.valid.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.node_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.node_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node-entries" + path_buffer

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

                    if (child_yang_name == "node-entry"):
                        for c in self.node_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.node_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.node_entries is not None and self.node_entries.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.node_entries is not None and self.node_entries.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node-entries"):
                    if (self.node_entries is None):
                        self.node_entries = SdrInventoryVm.Nodes.Node.NodeEntries()
                        self.node_entries.parent = self
                        self._children_name_map["node_entries"] = "node-entries"
                    return self.node_entries

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node-entries" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/%s" % self.get_segment_path()
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
                c = SdrInventoryVm.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm" + path_buffer

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
                self.nodes = SdrInventoryVm.Nodes()
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
        self._top_entity = SdrInventoryVm()
        return self._top_entity

