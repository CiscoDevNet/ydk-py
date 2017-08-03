""" Cisco_IOS_XR_lpts_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-ifib\: lpts ifib database

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LptsIfib(Entity):
    """
    lpts ifib database
    
    .. attribute:: nodes
    
    	Node ifib database
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes>`
    
    

    """

    _prefix = 'lpts-ifib-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(LptsIfib, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-ifib"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-ifib-oper"

        self.nodes = LptsIfib.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node ifib database
        
        .. attribute:: node
        
        	Per node slice 
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node>`
        
        

        """

        _prefix = 'lpts-ifib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(LptsIfib.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lpts-ifib"

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
                        super(LptsIfib.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LptsIfib.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Per node slice 
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: slice_ids
            
            	Slice specific
            	**type**\:   :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds>`
            
            

            """

            _prefix = 'lpts-ifib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(LptsIfib.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.slice_ids = LptsIfib.Nodes.Node.SliceIds()
                self.slice_ids.parent = self
                self._children_name_map["slice_ids"] = "slice-ids"
                self._children_yang_names.add("slice-ids")

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
                            super(LptsIfib.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LptsIfib.Nodes.Node, self).__setattr__(name, value)


            class SliceIds(Entity):
                """
                Slice specific
                
                .. attribute:: slice_id
                
                	slice types
                	**type**\: list of    :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds.SliceId>`
                
                

                """

                _prefix = 'lpts-ifib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LptsIfib.Nodes.Node.SliceIds, self).__init__()

                    self.yang_name = "slice-ids"
                    self.yang_parent_name = "node"

                    self.slice_id = YList(self)

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
                                super(LptsIfib.Nodes.Node.SliceIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LptsIfib.Nodes.Node.SliceIds, self).__setattr__(name, value)


                class SliceId(Entity):
                    """
                    slice types
                    
                    .. attribute:: slice_name  <key>
                    
                    	Type value
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds.SliceId.Entry>`
                    
                    

                    """

                    _prefix = 'lpts-ifib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(LptsIfib.Nodes.Node.SliceIds.SliceId, self).__init__()

                        self.yang_name = "slice-id"
                        self.yang_parent_name = "slice-ids"

                        self.slice_name = YLeaf(YType.str, "slice-name")

                        self.entry = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("slice_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(LptsIfib.Nodes.Node.SliceIds.SliceId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsIfib.Nodes.Node.SliceIds.SliceId, self).__setattr__(name, value)


                    class Entry(Entity):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  <key>
                        
                        	Single Pre\-ifib entry
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: accepts
                        
                        	Packets matched to accept
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: deliver_list_long
                        
                        	Deliver List Long Format
                        	**type**\:  str
                        
                        .. attribute:: deliver_list_short
                        
                        	Deliver List Short Format
                        	**type**\:  str
                        
                        .. attribute:: destination_addr
                        
                        	Destination IP Address
                        	**type**\:  str
                        
                        .. attribute:: destination_type
                        
                        	Destination Key Type
                        	**type**\:  str
                        
                        .. attribute:: destination_value
                        
                        	Destination Port/ICMP Type/IGMP Type
                        	**type**\:  str
                        
                        .. attribute:: drops
                        
                        	Packets matched to drop
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\:  str
                        
                        .. attribute:: ifib_program_time
                        
                        	ifib program time in netio
                        	**type**\:  str
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\:  str
                        
                        .. attribute:: local_flag
                        
                        	Local Flag
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: opcode
                        
                        	Opcode
                        	**type**\:  str
                        
                        .. attribute:: pending_ifibq_delay
                        
                        	pending ifib queue delay
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sl_ifibq_delay
                        
                        	sl\_ifibq delay
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\:  str
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\:  str
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lpts-ifib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(LptsIfib.Nodes.Node.SliceIds.SliceId.Entry, self).__init__()

                            self.yang_name = "entry"
                            self.yang_parent_name = "slice-id"

                            self.entry = YLeaf(YType.int32, "entry")

                            self.accepts = YLeaf(YType.uint64, "accepts")

                            self.deliver_list_long = YLeaf(YType.str, "deliver-list-long")

                            self.deliver_list_short = YLeaf(YType.str, "deliver-list-short")

                            self.destination_addr = YLeaf(YType.str, "destination-addr")

                            self.destination_type = YLeaf(YType.str, "destination-type")

                            self.destination_value = YLeaf(YType.str, "destination-value")

                            self.drops = YLeaf(YType.uint64, "drops")

                            self.flow_type = YLeaf(YType.str, "flow-type")

                            self.ifib_program_time = YLeaf(YType.str, "ifib-program-time")

                            self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                            self.intf_name = YLeaf(YType.str, "intf-name")

                            self.is_fgid = YLeaf(YType.uint8, "is-fgid")

                            self.is_syn = YLeaf(YType.uint8, "is-syn")

                            self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                            self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                            self.listener_tag = YLeaf(YType.str, "listener-tag")

                            self.local_flag = YLeaf(YType.uint8, "local-flag")

                            self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                            self.opcode = YLeaf(YType.str, "opcode")

                            self.pending_ifibq_delay = YLeaf(YType.uint32, "pending-ifibq-delay")

                            self.sl_ifibq_delay = YLeaf(YType.uint32, "sl-ifibq-delay")

                            self.source_addr = YLeaf(YType.str, "source-addr")

                            self.source_port = YLeaf(YType.str, "source-port")

                            self.vid = YLeaf(YType.uint32, "vid")

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
                                if name in ("entry",
                                            "accepts",
                                            "deliver_list_long",
                                            "deliver_list_short",
                                            "destination_addr",
                                            "destination_type",
                                            "destination_value",
                                            "drops",
                                            "flow_type",
                                            "ifib_program_time",
                                            "intf_handle",
                                            "intf_name",
                                            "is_fgid",
                                            "is_syn",
                                            "l3protocol",
                                            "l4protocol",
                                            "listener_tag",
                                            "local_flag",
                                            "min_ttl",
                                            "opcode",
                                            "pending_ifibq_delay",
                                            "sl_ifibq_delay",
                                            "source_addr",
                                            "source_port",
                                            "vid",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsIfib.Nodes.Node.SliceIds.SliceId.Entry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsIfib.Nodes.Node.SliceIds.SliceId.Entry, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.entry.is_set or
                                self.accepts.is_set or
                                self.deliver_list_long.is_set or
                                self.deliver_list_short.is_set or
                                self.destination_addr.is_set or
                                self.destination_type.is_set or
                                self.destination_value.is_set or
                                self.drops.is_set or
                                self.flow_type.is_set or
                                self.ifib_program_time.is_set or
                                self.intf_handle.is_set or
                                self.intf_name.is_set or
                                self.is_fgid.is_set or
                                self.is_syn.is_set or
                                self.l3protocol.is_set or
                                self.l4protocol.is_set or
                                self.listener_tag.is_set or
                                self.local_flag.is_set or
                                self.min_ttl.is_set or
                                self.opcode.is_set or
                                self.pending_ifibq_delay.is_set or
                                self.sl_ifibq_delay.is_set or
                                self.source_addr.is_set or
                                self.source_port.is_set or
                                self.vid.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.entry.yfilter != YFilter.not_set or
                                self.accepts.yfilter != YFilter.not_set or
                                self.deliver_list_long.yfilter != YFilter.not_set or
                                self.deliver_list_short.yfilter != YFilter.not_set or
                                self.destination_addr.yfilter != YFilter.not_set or
                                self.destination_type.yfilter != YFilter.not_set or
                                self.destination_value.yfilter != YFilter.not_set or
                                self.drops.yfilter != YFilter.not_set or
                                self.flow_type.yfilter != YFilter.not_set or
                                self.ifib_program_time.yfilter != YFilter.not_set or
                                self.intf_handle.yfilter != YFilter.not_set or
                                self.intf_name.yfilter != YFilter.not_set or
                                self.is_fgid.yfilter != YFilter.not_set or
                                self.is_syn.yfilter != YFilter.not_set or
                                self.l3protocol.yfilter != YFilter.not_set or
                                self.l4protocol.yfilter != YFilter.not_set or
                                self.listener_tag.yfilter != YFilter.not_set or
                                self.local_flag.yfilter != YFilter.not_set or
                                self.min_ttl.yfilter != YFilter.not_set or
                                self.opcode.yfilter != YFilter.not_set or
                                self.pending_ifibq_delay.yfilter != YFilter.not_set or
                                self.sl_ifibq_delay.yfilter != YFilter.not_set or
                                self.source_addr.yfilter != YFilter.not_set or
                                self.source_port.yfilter != YFilter.not_set or
                                self.vid.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "entry" + "[entry='" + self.entry.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.entry.is_set or self.entry.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entry.get_name_leafdata())
                            if (self.accepts.is_set or self.accepts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accepts.get_name_leafdata())
                            if (self.deliver_list_long.is_set or self.deliver_list_long.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.deliver_list_long.get_name_leafdata())
                            if (self.deliver_list_short.is_set or self.deliver_list_short.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.deliver_list_short.get_name_leafdata())
                            if (self.destination_addr.is_set or self.destination_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_addr.get_name_leafdata())
                            if (self.destination_type.is_set or self.destination_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_type.get_name_leafdata())
                            if (self.destination_value.is_set or self.destination_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_value.get_name_leafdata())
                            if (self.drops.is_set or self.drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drops.get_name_leafdata())
                            if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_type.get_name_leafdata())
                            if (self.ifib_program_time.is_set or self.ifib_program_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ifib_program_time.get_name_leafdata())
                            if (self.intf_handle.is_set or self.intf_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_handle.get_name_leafdata())
                            if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_name.get_name_leafdata())
                            if (self.is_fgid.is_set or self.is_fgid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_fgid.get_name_leafdata())
                            if (self.is_syn.is_set or self.is_syn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_syn.get_name_leafdata())
                            if (self.l3protocol.is_set or self.l3protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.l3protocol.get_name_leafdata())
                            if (self.l4protocol.is_set or self.l4protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.l4protocol.get_name_leafdata())
                            if (self.listener_tag.is_set or self.listener_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.listener_tag.get_name_leafdata())
                            if (self.local_flag.is_set or self.local_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_flag.get_name_leafdata())
                            if (self.min_ttl.is_set or self.min_ttl.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min_ttl.get_name_leafdata())
                            if (self.opcode.is_set or self.opcode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.opcode.get_name_leafdata())
                            if (self.pending_ifibq_delay.is_set or self.pending_ifibq_delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pending_ifibq_delay.get_name_leafdata())
                            if (self.sl_ifibq_delay.is_set or self.sl_ifibq_delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sl_ifibq_delay.get_name_leafdata())
                            if (self.source_addr.is_set or self.source_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_addr.get_name_leafdata())
                            if (self.source_port.is_set or self.source_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port.get_name_leafdata())
                            if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vid.get_name_leafdata())
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
                            if(name == "entry" or name == "accepts" or name == "deliver-list-long" or name == "deliver-list-short" or name == "destination-addr" or name == "destination-type" or name == "destination-value" or name == "drops" or name == "flow-type" or name == "ifib-program-time" or name == "intf-handle" or name == "intf-name" or name == "is-fgid" or name == "is-syn" or name == "l3protocol" or name == "l4protocol" or name == "listener-tag" or name == "local-flag" or name == "min-ttl" or name == "opcode" or name == "pending-ifibq-delay" or name == "sl-ifibq-delay" or name == "source-addr" or name == "source-port" or name == "vid" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "entry"):
                                self.entry = value
                                self.entry.value_namespace = name_space
                                self.entry.value_namespace_prefix = name_space_prefix
                            if(value_path == "accepts"):
                                self.accepts = value
                                self.accepts.value_namespace = name_space
                                self.accepts.value_namespace_prefix = name_space_prefix
                            if(value_path == "deliver-list-long"):
                                self.deliver_list_long = value
                                self.deliver_list_long.value_namespace = name_space
                                self.deliver_list_long.value_namespace_prefix = name_space_prefix
                            if(value_path == "deliver-list-short"):
                                self.deliver_list_short = value
                                self.deliver_list_short.value_namespace = name_space
                                self.deliver_list_short.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-addr"):
                                self.destination_addr = value
                                self.destination_addr.value_namespace = name_space
                                self.destination_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-type"):
                                self.destination_type = value
                                self.destination_type.value_namespace = name_space
                                self.destination_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-value"):
                                self.destination_value = value
                                self.destination_value.value_namespace = name_space
                                self.destination_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "drops"):
                                self.drops = value
                                self.drops.value_namespace = name_space
                                self.drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-type"):
                                self.flow_type = value
                                self.flow_type.value_namespace = name_space
                                self.flow_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "ifib-program-time"):
                                self.ifib_program_time = value
                                self.ifib_program_time.value_namespace = name_space
                                self.ifib_program_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "intf-handle"):
                                self.intf_handle = value
                                self.intf_handle.value_namespace = name_space
                                self.intf_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "intf-name"):
                                self.intf_name = value
                                self.intf_name.value_namespace = name_space
                                self.intf_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-fgid"):
                                self.is_fgid = value
                                self.is_fgid.value_namespace = name_space
                                self.is_fgid.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-syn"):
                                self.is_syn = value
                                self.is_syn.value_namespace = name_space
                                self.is_syn.value_namespace_prefix = name_space_prefix
                            if(value_path == "l3protocol"):
                                self.l3protocol = value
                                self.l3protocol.value_namespace = name_space
                                self.l3protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "l4protocol"):
                                self.l4protocol = value
                                self.l4protocol.value_namespace = name_space
                                self.l4protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "listener-tag"):
                                self.listener_tag = value
                                self.listener_tag.value_namespace = name_space
                                self.listener_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "local-flag"):
                                self.local_flag = value
                                self.local_flag.value_namespace = name_space
                                self.local_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "min-ttl"):
                                self.min_ttl = value
                                self.min_ttl.value_namespace = name_space
                                self.min_ttl.value_namespace_prefix = name_space_prefix
                            if(value_path == "opcode"):
                                self.opcode = value
                                self.opcode.value_namespace = name_space
                                self.opcode.value_namespace_prefix = name_space_prefix
                            if(value_path == "pending-ifibq-delay"):
                                self.pending_ifibq_delay = value
                                self.pending_ifibq_delay.value_namespace = name_space
                                self.pending_ifibq_delay.value_namespace_prefix = name_space_prefix
                            if(value_path == "sl-ifibq-delay"):
                                self.sl_ifibq_delay = value
                                self.sl_ifibq_delay.value_namespace = name_space
                                self.sl_ifibq_delay.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-addr"):
                                self.source_addr = value
                                self.source_addr.value_namespace = name_space
                                self.source_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port"):
                                self.source_port = value
                                self.source_port.value_namespace = name_space
                                self.source_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "vid"):
                                self.vid = value
                                self.vid.value_namespace = name_space
                                self.vid.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.entry:
                            if (c.has_data()):
                                return True
                        return self.slice_name.is_set

                    def has_operation(self):
                        for c in self.entry:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.slice_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slice-id" + "[slice-name='" + self.slice_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.slice_name.is_set or self.slice_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slice_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "entry"):
                            for c in self.entry:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsIfib.Nodes.Node.SliceIds.SliceId.Entry()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.entry.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "entry" or name == "slice-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "slice-name"):
                            self.slice_name = value
                            self.slice_name.value_namespace = name_space
                            self.slice_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.slice_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.slice_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slice-ids" + path_buffer

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

                    if (child_yang_name == "slice-id"):
                        for c in self.slice_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = LptsIfib.Nodes.Node.SliceIds.SliceId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.slice_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slice-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.slice_ids is not None and self.slice_ids.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.slice_ids is not None and self.slice_ids.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "slice-ids"):
                    if (self.slice_ids is None):
                        self.slice_ids = LptsIfib.Nodes.Node.SliceIds()
                        self.slice_ids.parent = self
                        self._children_name_map["slice_ids"] = "slice-ids"
                    return self.slice_ids

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slice-ids" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/%s" % self.get_segment_path()
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
                c = LptsIfib.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib" + path_buffer

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
                self.nodes = LptsIfib.Nodes()
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
        self._top_entity = LptsIfib()
        return self._top_entity

