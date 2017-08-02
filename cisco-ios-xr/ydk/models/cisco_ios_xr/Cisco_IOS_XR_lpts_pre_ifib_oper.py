""" Cisco_IOS_XR_lpts_pre_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pifib\: lpts pre\-ifib data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LptsPifib(Enum):
    """
    LptsPifib

    Lpts pifib

    .. data:: isis = 0

    	ISIS packets

    .. data:: ipv4_frag = 1

    	IPv4 fragmented packets

    .. data:: ipv4_echo = 2

    	IPv4 ICMP Echo packets

    .. data:: ipv4_any = 3

    	All IPv4 packets

    .. data:: ipv6_frag = 4

    	IPv6 fragmented packets

    .. data:: ipv6_echo = 5

    	IPv6 ICMP Echo packets

    .. data:: ipv6_nd = 6

    	IPv6 ND packets

    .. data:: ipv6_any = 7

    	All IPv6 packets

    .. data:: bfd_any = 8

    	BFD packets

    .. data:: all = 9

    	All packets

    """

    isis = Enum.YLeaf(0, "isis")

    ipv4_frag = Enum.YLeaf(1, "ipv4-frag")

    ipv4_echo = Enum.YLeaf(2, "ipv4-echo")

    ipv4_any = Enum.YLeaf(3, "ipv4-any")

    ipv6_frag = Enum.YLeaf(4, "ipv6-frag")

    ipv6_echo = Enum.YLeaf(5, "ipv6-echo")

    ipv6_nd = Enum.YLeaf(6, "ipv6-nd")

    ipv6_any = Enum.YLeaf(7, "ipv6-any")

    bfd_any = Enum.YLeaf(8, "bfd-any")

    all = Enum.YLeaf(9, "all")



class LptsPifib_(Entity):
    """
    lpts pre\-ifib data
    
    .. attribute:: nodes
    
    	List of Pre\-ifib Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes>`
    
    

    """

    _prefix = 'lpts-pre-ifib-oper'
    _revision = '2016-02-22'

    def __init__(self):
        super(LptsPifib_, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-pifib"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-pre-ifib-oper"

        self.nodes = LptsPifib_.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of Pre\-ifib Nodes
        
        .. attribute:: node
        
        	Pre\-ifib data for particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node>`
        
        

        """

        _prefix = 'lpts-pre-ifib-oper'
        _revision = '2016-02-22'

        def __init__(self):
            super(LptsPifib_.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lpts-pifib"

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
                        super(LptsPifib_.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LptsPifib_.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Pre\-ifib data for particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: hardware
            
            	Hardware specific
            	**type**\:   :py:class:`Hardware <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware>`
            
            .. attribute:: type_values
            
            	Type specific
            	**type**\:   :py:class:`TypeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues>`
            
            

            """

            _prefix = 'lpts-pre-ifib-oper'
            _revision = '2016-02-22'

            def __init__(self):
                super(LptsPifib_.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.hardware = LptsPifib_.Nodes.Node.Hardware()
                self.hardware.parent = self
                self._children_name_map["hardware"] = "hardware"
                self._children_yang_names.add("hardware")

                self.type_values = LptsPifib_.Nodes.Node.TypeValues()
                self.type_values.parent = self
                self._children_name_map["type_values"] = "type-values"
                self._children_yang_names.add("type-values")

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
                            super(LptsPifib_.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LptsPifib_.Nodes.Node, self).__setattr__(name, value)


            class TypeValues(Entity):
                """
                Type specific
                
                .. attribute:: type_value
                
                	pifib types
                	**type**\: list of    :py:class:`TypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue>`
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(LptsPifib_.Nodes.Node.TypeValues, self).__init__()

                    self.yang_name = "type-values"
                    self.yang_parent_name = "node"

                    self.type_value = YList(self)

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
                                super(LptsPifib_.Nodes.Node.TypeValues, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LptsPifib_.Nodes.Node.TypeValues, self).__setattr__(name, value)


                class TypeValue(Entity):
                    """
                    pifib types
                    
                    .. attribute:: pifib_type  <key>
                    
                    	Type value
                    	**type**\:   :py:class:`LptsPifib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib>`
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.TypeValues.TypeValue, self).__init__()

                        self.yang_name = "type-value"
                        self.yang_parent_name = "type-values"

                        self.pifib_type = YLeaf(YType.enumeration, "pifib-type")

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
                            if name in ("pifib_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(LptsPifib_.Nodes.Node.TypeValues.TypeValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.TypeValues.TypeValue, self).__setattr__(name, value)


                    class Entry(Entity):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  <key>
                        
                        	Single Pre\-ifib entry
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
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
                        
                        	Packets matched for drop
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_type
                        
                        	Flow type
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
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
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
                        
                        .. attribute:: pifib_program_time
                        
                        	Creation or Update Time
                        	**type**\:  str
                        
                        .. attribute:: pifib_type
                        
                        	sub Pre\-IFIB type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\:  str
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\:  str
                        
                        .. attribute:: stale
                        
                        	Is Stale
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, self).__init__()

                            self.yang_name = "entry"
                            self.yang_parent_name = "type-value"

                            self.entry = YLeaf(YType.str, "entry")

                            self.accepts = YLeaf(YType.uint64, "accepts")

                            self.deliver_list_long = YLeaf(YType.str, "deliver-list-long")

                            self.deliver_list_short = YLeaf(YType.str, "deliver-list-short")

                            self.destination_addr = YLeaf(YType.str, "destination-addr")

                            self.destination_type = YLeaf(YType.str, "destination-type")

                            self.destination_value = YLeaf(YType.str, "destination-value")

                            self.drops = YLeaf(YType.uint64, "drops")

                            self.flow_type = YLeaf(YType.str, "flow-type")

                            self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                            self.intf_name = YLeaf(YType.str, "intf-name")

                            self.is_fgid = YLeaf(YType.uint8, "is-fgid")

                            self.is_frag = YLeaf(YType.uint8, "is-frag")

                            self.is_syn = YLeaf(YType.uint8, "is-syn")

                            self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                            self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                            self.listener_tag = YLeaf(YType.str, "listener-tag")

                            self.local_flag = YLeaf(YType.uint8, "local-flag")

                            self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                            self.opcode = YLeaf(YType.str, "opcode")

                            self.pifib_program_time = YLeaf(YType.str, "pifib-program-time")

                            self.pifib_type = YLeaf(YType.uint8, "pifib-type")

                            self.source_addr = YLeaf(YType.str, "source-addr")

                            self.source_port = YLeaf(YType.str, "source-port")

                            self.stale = YLeaf(YType.uint8, "stale")

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
                                            "intf_handle",
                                            "intf_name",
                                            "is_fgid",
                                            "is_frag",
                                            "is_syn",
                                            "l3protocol",
                                            "l4protocol",
                                            "listener_tag",
                                            "local_flag",
                                            "min_ttl",
                                            "opcode",
                                            "pifib_program_time",
                                            "pifib_type",
                                            "source_addr",
                                            "source_port",
                                            "stale",
                                            "vid",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, self).__setattr__(name, value)

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
                                self.intf_handle.is_set or
                                self.intf_name.is_set or
                                self.is_fgid.is_set or
                                self.is_frag.is_set or
                                self.is_syn.is_set or
                                self.l3protocol.is_set or
                                self.l4protocol.is_set or
                                self.listener_tag.is_set or
                                self.local_flag.is_set or
                                self.min_ttl.is_set or
                                self.opcode.is_set or
                                self.pifib_program_time.is_set or
                                self.pifib_type.is_set or
                                self.source_addr.is_set or
                                self.source_port.is_set or
                                self.stale.is_set or
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
                                self.intf_handle.yfilter != YFilter.not_set or
                                self.intf_name.yfilter != YFilter.not_set or
                                self.is_fgid.yfilter != YFilter.not_set or
                                self.is_frag.yfilter != YFilter.not_set or
                                self.is_syn.yfilter != YFilter.not_set or
                                self.l3protocol.yfilter != YFilter.not_set or
                                self.l4protocol.yfilter != YFilter.not_set or
                                self.listener_tag.yfilter != YFilter.not_set or
                                self.local_flag.yfilter != YFilter.not_set or
                                self.min_ttl.yfilter != YFilter.not_set or
                                self.opcode.yfilter != YFilter.not_set or
                                self.pifib_program_time.yfilter != YFilter.not_set or
                                self.pifib_type.yfilter != YFilter.not_set or
                                self.source_addr.yfilter != YFilter.not_set or
                                self.source_port.yfilter != YFilter.not_set or
                                self.stale.yfilter != YFilter.not_set or
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
                            if (self.intf_handle.is_set or self.intf_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_handle.get_name_leafdata())
                            if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_name.get_name_leafdata())
                            if (self.is_fgid.is_set or self.is_fgid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_fgid.get_name_leafdata())
                            if (self.is_frag.is_set or self.is_frag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_frag.get_name_leafdata())
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
                            if (self.pifib_program_time.is_set or self.pifib_program_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pifib_program_time.get_name_leafdata())
                            if (self.pifib_type.is_set or self.pifib_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pifib_type.get_name_leafdata())
                            if (self.source_addr.is_set or self.source_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_addr.get_name_leafdata())
                            if (self.source_port.is_set or self.source_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port.get_name_leafdata())
                            if (self.stale.is_set or self.stale.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stale.get_name_leafdata())
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
                            if(name == "entry" or name == "accepts" or name == "deliver-list-long" or name == "deliver-list-short" or name == "destination-addr" or name == "destination-type" or name == "destination-value" or name == "drops" or name == "flow-type" or name == "intf-handle" or name == "intf-name" or name == "is-fgid" or name == "is-frag" or name == "is-syn" or name == "l3protocol" or name == "l4protocol" or name == "listener-tag" or name == "local-flag" or name == "min-ttl" or name == "opcode" or name == "pifib-program-time" or name == "pifib-type" or name == "source-addr" or name == "source-port" or name == "stale" or name == "vid" or name == "vrf-name"):
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
                            if(value_path == "is-frag"):
                                self.is_frag = value
                                self.is_frag.value_namespace = name_space
                                self.is_frag.value_namespace_prefix = name_space_prefix
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
                            if(value_path == "pifib-program-time"):
                                self.pifib_program_time = value
                                self.pifib_program_time.value_namespace = name_space
                                self.pifib_program_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "pifib-type"):
                                self.pifib_type = value
                                self.pifib_type.value_namespace = name_space
                                self.pifib_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-addr"):
                                self.source_addr = value
                                self.source_addr.value_namespace = name_space
                                self.source_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port"):
                                self.source_port = value
                                self.source_port.value_namespace = name_space
                                self.source_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "stale"):
                                self.stale = value
                                self.stale.value_namespace = name_space
                                self.stale.value_namespace_prefix = name_space_prefix
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
                        return self.pifib_type.is_set

                    def has_operation(self):
                        for c in self.entry:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pifib_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "type-value" + "[pifib-type='" + self.pifib_type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pifib_type.is_set or self.pifib_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pifib_type.get_name_leafdata())

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
                            c = LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.entry.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "entry" or name == "pifib-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pifib-type"):
                            self.pifib_type = value
                            self.pifib_type.value_namespace = name_space
                            self.pifib_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.type_value:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.type_value:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "type-values" + path_buffer

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

                    if (child_yang_name == "type-value"):
                        for c in self.type_value:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = LptsPifib_.Nodes.Node.TypeValues.TypeValue()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.type_value.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "type-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Hardware(Entity):
                """
                Hardware specific
                
                .. attribute:: bfd
                
                	Bfd details
                	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd>`
                
                .. attribute:: index_entries
                
                	Hardware Entry options
                	**type**\:   :py:class:`IndexEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries>`
                
                .. attribute:: police
                
                	Police details
                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police>`
                
                .. attribute:: static_police
                
                	Static Police details
                	**type**\:   :py:class:`StaticPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice>`
                
                .. attribute:: statistics
                
                	Hardware Entry type
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Statistics>`
                
                .. attribute:: usage_entries
                
                	Usage Table options
                	**type**\:   :py:class:`UsageEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries>`
                
                

                """

                _prefix = 'platform-pifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(LptsPifib_.Nodes.Node.Hardware, self).__init__()

                    self.yang_name = "hardware"
                    self.yang_parent_name = "node"

                    self.bfd = LptsPifib_.Nodes.Node.Hardware.Bfd()
                    self.bfd.parent = self
                    self._children_name_map["bfd"] = "bfd"
                    self._children_yang_names.add("bfd")

                    self.index_entries = LptsPifib_.Nodes.Node.Hardware.IndexEntries()
                    self.index_entries.parent = self
                    self._children_name_map["index_entries"] = "index-entries"
                    self._children_yang_names.add("index-entries")

                    self.police = LptsPifib_.Nodes.Node.Hardware.Police()
                    self.police.parent = self
                    self._children_name_map["police"] = "police"
                    self._children_yang_names.add("police")

                    self.static_police = LptsPifib_.Nodes.Node.Hardware.StaticPolice()
                    self.static_police.parent = self
                    self._children_name_map["static_police"] = "static-police"
                    self._children_yang_names.add("static-police")

                    self.statistics = LptsPifib_.Nodes.Node.Hardware.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.usage_entries = LptsPifib_.Nodes.Node.Hardware.UsageEntries()
                    self.usage_entries.parent = self
                    self._children_name_map["usage_entries"] = "usage-entries"
                    self._children_yang_names.add("usage-entries")


                class UsageEntries(Entity):
                    """
                    Usage Table options
                    
                    .. attribute:: usage_entry
                    
                    	Usage details
                    	**type**\: list of    :py:class:`UsageEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.UsageEntries, self).__init__()

                        self.yang_name = "usage-entries"
                        self.yang_parent_name = "hardware"

                        self.usage_entry = YList(self)

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
                                    super(LptsPifib_.Nodes.Node.Hardware.UsageEntries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.UsageEntries, self).__setattr__(name, value)


                    class UsageEntry(Entity):
                        """
                        Usage details
                        
                        .. attribute:: region_id  <key>
                        
                        	Region ID
                        	**type**\:   :py:class:`UsageAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper.UsageAddressFamily>`
                        
                        .. attribute:: usage_info
                        
                        	Per TCAM type usage info
                        	**type**\: list of    :py:class:`UsageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo>`
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, self).__init__()

                            self.yang_name = "usage-entry"
                            self.yang_parent_name = "usage-entries"

                            self.region_id = YLeaf(YType.enumeration, "region-id")

                            self.usage_info = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("region_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, self).__setattr__(name, value)


                        class UsageInfo(Entity):
                            """
                            Per TCAM type usage info
                            
                            .. attribute:: pipe_id
                            
                            	Pipe ID
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region
                            
                            	Region Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region_id
                            
                            	Region ID
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: size
                            
                            	Maximum Number of Entries in the Region
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used Number of Entries in the Region
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, self).__init__()

                                self.yang_name = "usage-info"
                                self.yang_parent_name = "usage-entry"

                                self.pipe_id = YLeaf(YType.uint8, "pipe-id")

                                self.region = YLeaf(YType.uint8, "region")

                                self.region_id = YLeaf(YType.uint8, "region-id")

                                self.size = YLeaf(YType.uint32, "size")

                                self.used = YLeaf(YType.uint32, "used")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pipe_id",
                                                "region",
                                                "region_id",
                                                "size",
                                                "used") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.pipe_id.is_set or
                                    self.region.is_set or
                                    self.region_id.is_set or
                                    self.size.is_set or
                                    self.used.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pipe_id.yfilter != YFilter.not_set or
                                    self.region.yfilter != YFilter.not_set or
                                    self.region_id.yfilter != YFilter.not_set or
                                    self.size.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "usage-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pipe_id.is_set or self.pipe_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pipe_id.get_name_leafdata())
                                if (self.region.is_set or self.region.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.region.get_name_leafdata())
                                if (self.region_id.is_set or self.region_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.region_id.get_name_leafdata())
                                if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.size.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "pipe-id" or name == "region" or name == "region-id" or name == "size" or name == "used"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pipe-id"):
                                    self.pipe_id = value
                                    self.pipe_id.value_namespace = name_space
                                    self.pipe_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "region"):
                                    self.region = value
                                    self.region.value_namespace = name_space
                                    self.region.value_namespace_prefix = name_space_prefix
                                if(value_path == "region-id"):
                                    self.region_id = value
                                    self.region_id.value_namespace = name_space
                                    self.region_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "size"):
                                    self.size = value
                                    self.size.value_namespace = name_space
                                    self.size.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.usage_info:
                                if (c.has_data()):
                                    return True
                            return self.region_id.is_set

                        def has_operation(self):
                            for c in self.usage_info:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.region_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "usage-entry" + "[region-id='" + self.region_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.region_id.is_set or self.region_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.region_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "usage-info"):
                                for c in self.usage_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.usage_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "usage-info" or name == "region-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "region-id"):
                                self.region_id = value
                                self.region_id.value_namespace = name_space
                                self.region_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.usage_entry:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.usage_entry:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "usage-entries" + path_buffer

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

                        if (child_yang_name == "usage-entry"):
                            for c in self.usage_entry:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.usage_entry.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "usage-entry"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Police(Entity):
                    """
                    Police details
                    
                    .. attribute:: police_info
                    
                    	Per flow type police info
                    	**type**\: list of    :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "hardware"

                        self.police_info = YList(self)

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
                                    super(LptsPifib_.Nodes.Node.Hardware.Police, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.Police, self).__setattr__(name, value)


                    class PoliceInfo(Entity):
                        """
                        Per flow type police info
                        
                        .. attribute:: accepted_stats
                        
                        	accepted stats
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: acl_config
                        
                        	acl config
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: acl_str
                        
                        	acl str
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: avgrate
                        
                        	avgrate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: avgrate_type
                        
                        	avgrate type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: burst
                        
                        	burst
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dropped_stats
                        
                        	dropped stats
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: iptos_value
                        
                        	iptos value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policer
                        
                        	policer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: static_avgrate
                        
                        	static avgrate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, self).__init__()

                            self.yang_name = "police-info"
                            self.yang_parent_name = "police"

                            self.accepted_stats = YLeaf(YType.uint64, "accepted-stats")

                            self.acl_config = YLeaf(YType.uint8, "acl-config")

                            self.acl_str = YLeaf(YType.str, "acl-str")

                            self.avgrate = YLeaf(YType.uint32, "avgrate")

                            self.avgrate_type = YLeaf(YType.uint32, "avgrate-type")

                            self.burst = YLeaf(YType.uint32, "burst")

                            self.change_type = YLeaf(YType.uint8, "change-type")

                            self.dropped_stats = YLeaf(YType.uint64, "dropped-stats")

                            self.iptos_value = YLeaf(YType.uint8, "iptos-value")

                            self.policer = YLeaf(YType.uint32, "policer")

                            self.static_avgrate = YLeaf(YType.uint32, "static-avgrate")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accepted_stats",
                                            "acl_config",
                                            "acl_str",
                                            "avgrate",
                                            "avgrate_type",
                                            "burst",
                                            "change_type",
                                            "dropped_stats",
                                            "iptos_value",
                                            "policer",
                                            "static_avgrate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.accepted_stats.is_set or
                                self.acl_config.is_set or
                                self.acl_str.is_set or
                                self.avgrate.is_set or
                                self.avgrate_type.is_set or
                                self.burst.is_set or
                                self.change_type.is_set or
                                self.dropped_stats.is_set or
                                self.iptos_value.is_set or
                                self.policer.is_set or
                                self.static_avgrate.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accepted_stats.yfilter != YFilter.not_set or
                                self.acl_config.yfilter != YFilter.not_set or
                                self.acl_str.yfilter != YFilter.not_set or
                                self.avgrate.yfilter != YFilter.not_set or
                                self.avgrate_type.yfilter != YFilter.not_set or
                                self.burst.yfilter != YFilter.not_set or
                                self.change_type.yfilter != YFilter.not_set or
                                self.dropped_stats.yfilter != YFilter.not_set or
                                self.iptos_value.yfilter != YFilter.not_set or
                                self.policer.yfilter != YFilter.not_set or
                                self.static_avgrate.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "police-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accepted_stats.is_set or self.accepted_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accepted_stats.get_name_leafdata())
                            if (self.acl_config.is_set or self.acl_config.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_config.get_name_leafdata())
                            if (self.acl_str.is_set or self.acl_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_str.get_name_leafdata())
                            if (self.avgrate.is_set or self.avgrate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avgrate.get_name_leafdata())
                            if (self.avgrate_type.is_set or self.avgrate_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avgrate_type.get_name_leafdata())
                            if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst.get_name_leafdata())
                            if (self.change_type.is_set or self.change_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.change_type.get_name_leafdata())
                            if (self.dropped_stats.is_set or self.dropped_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_stats.get_name_leafdata())
                            if (self.iptos_value.is_set or self.iptos_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.iptos_value.get_name_leafdata())
                            if (self.policer.is_set or self.policer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policer.get_name_leafdata())
                            if (self.static_avgrate.is_set or self.static_avgrate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.static_avgrate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accepted-stats" or name == "acl-config" or name == "acl-str" or name == "avgrate" or name == "avgrate-type" or name == "burst" or name == "change-type" or name == "dropped-stats" or name == "iptos-value" or name == "policer" or name == "static-avgrate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accepted-stats"):
                                self.accepted_stats = value
                                self.accepted_stats.value_namespace = name_space
                                self.accepted_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-config"):
                                self.acl_config = value
                                self.acl_config.value_namespace = name_space
                                self.acl_config.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-str"):
                                self.acl_str = value
                                self.acl_str.value_namespace = name_space
                                self.acl_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "avgrate"):
                                self.avgrate = value
                                self.avgrate.value_namespace = name_space
                                self.avgrate.value_namespace_prefix = name_space_prefix
                            if(value_path == "avgrate-type"):
                                self.avgrate_type = value
                                self.avgrate_type.value_namespace = name_space
                                self.avgrate_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst"):
                                self.burst = value
                                self.burst.value_namespace = name_space
                                self.burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "change-type"):
                                self.change_type = value
                                self.change_type.value_namespace = name_space
                                self.change_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-stats"):
                                self.dropped_stats = value
                                self.dropped_stats.value_namespace = name_space
                                self.dropped_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "iptos-value"):
                                self.iptos_value = value
                                self.iptos_value.value_namespace = name_space
                                self.iptos_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "policer"):
                                self.policer = value
                                self.policer.value_namespace = name_space
                                self.policer.value_namespace_prefix = name_space_prefix
                            if(value_path == "static-avgrate"):
                                self.static_avgrate = value
                                self.static_avgrate.value_namespace = name_space
                                self.static_avgrate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.police_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.police_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "police" + path_buffer

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

                        if (child_yang_name == "police-info"):
                            for c in self.police_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.police_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "police-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class StaticPolice(Entity):
                    """
                    Static Police details
                    
                    .. attribute:: static_info
                    
                    	Per punt reason info
                    	**type**\: list of    :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.StaticPolice, self).__init__()

                        self.yang_name = "static-police"
                        self.yang_parent_name = "hardware"

                        self.static_info = YList(self)

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
                                    super(LptsPifib_.Nodes.Node.Hardware.StaticPolice, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.StaticPolice, self).__setattr__(name, value)


                    class StaticInfo(Entity):
                        """
                        Per punt reason info
                        
                        .. attribute:: accepted
                        
                        	accepted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: burst_rate
                        
                        	burst rate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dropped
                        
                        	dropped
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_rate
                        
                        	flow rate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punt_reason
                        
                        	punt reason
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punt_reason_string
                        
                        	punt reason string
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: sid
                        
                        	sid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, self).__init__()

                            self.yang_name = "static-info"
                            self.yang_parent_name = "static-police"

                            self.accepted = YLeaf(YType.uint64, "accepted")

                            self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                            self.change_type = YLeaf(YType.uint8, "change-type")

                            self.dropped = YLeaf(YType.uint64, "dropped")

                            self.flow_rate = YLeaf(YType.uint32, "flow-rate")

                            self.punt_reason = YLeaf(YType.uint32, "punt-reason")

                            self.punt_reason_string = YLeaf(YType.str, "punt-reason-string")

                            self.sid = YLeaf(YType.uint32, "sid")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accepted",
                                            "burst_rate",
                                            "change_type",
                                            "dropped",
                                            "flow_rate",
                                            "punt_reason",
                                            "punt_reason_string",
                                            "sid") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.accepted.is_set or
                                self.burst_rate.is_set or
                                self.change_type.is_set or
                                self.dropped.is_set or
                                self.flow_rate.is_set or
                                self.punt_reason.is_set or
                                self.punt_reason_string.is_set or
                                self.sid.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accepted.yfilter != YFilter.not_set or
                                self.burst_rate.yfilter != YFilter.not_set or
                                self.change_type.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.flow_rate.yfilter != YFilter.not_set or
                                self.punt_reason.yfilter != YFilter.not_set or
                                self.punt_reason_string.yfilter != YFilter.not_set or
                                self.sid.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accepted.get_name_leafdata())
                            if (self.burst_rate.is_set or self.burst_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst_rate.get_name_leafdata())
                            if (self.change_type.is_set or self.change_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.change_type.get_name_leafdata())
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.flow_rate.is_set or self.flow_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_rate.get_name_leafdata())
                            if (self.punt_reason.is_set or self.punt_reason.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.punt_reason.get_name_leafdata())
                            if (self.punt_reason_string.is_set or self.punt_reason_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.punt_reason_string.get_name_leafdata())
                            if (self.sid.is_set or self.sid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sid.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accepted" or name == "burst-rate" or name == "change-type" or name == "dropped" or name == "flow-rate" or name == "punt-reason" or name == "punt-reason-string" or name == "sid"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accepted"):
                                self.accepted = value
                                self.accepted.value_namespace = name_space
                                self.accepted.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst-rate"):
                                self.burst_rate = value
                                self.burst_rate.value_namespace = name_space
                                self.burst_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "change-type"):
                                self.change_type = value
                                self.change_type.value_namespace = name_space
                                self.change_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-rate"):
                                self.flow_rate = value
                                self.flow_rate.value_namespace = name_space
                                self.flow_rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "punt-reason"):
                                self.punt_reason = value
                                self.punt_reason.value_namespace = name_space
                                self.punt_reason.value_namespace_prefix = name_space_prefix
                            if(value_path == "punt-reason-string"):
                                self.punt_reason_string = value
                                self.punt_reason_string.value_namespace = name_space
                                self.punt_reason_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "sid"):
                                self.sid = value
                                self.sid.value_namespace = name_space
                                self.sid.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-police" + path_buffer

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

                        if (child_yang_name == "static-info"):
                            for c in self.static_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Bfd(Entity):
                    """
                    Bfd details
                    
                    .. attribute:: bfd_entry_info
                    
                    	Per bfd disc entry info
                    	**type**\: list of    :py:class:`BfdEntryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Bfd, self).__init__()

                        self.yang_name = "bfd"
                        self.yang_parent_name = "hardware"

                        self.bfd_entry_info = YList(self)

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
                                    super(LptsPifib_.Nodes.Node.Hardware.Bfd, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.Bfd, self).__setattr__(name, value)


                    class BfdEntryInfo(Entity):
                        """
                        Per bfd disc entry info
                        
                        .. attribute:: fgid_or_vqi
                        
                        	fgid or vqi
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: index
                        
                        	index
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_mcast
                        
                        	is mcast
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_valid
                        
                        	is valid
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policer_id
                        
                        	policer id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, self).__init__()

                            self.yang_name = "bfd-entry-info"
                            self.yang_parent_name = "bfd"

                            self.fgid_or_vqi = YLeaf(YType.uint32, "fgid-or-vqi")

                            self.index = YLeaf(YType.uint8, "index")

                            self.is_mcast = YLeaf(YType.uint8, "is-mcast")

                            self.is_valid = YLeaf(YType.uint8, "is-valid")

                            self.policer_id = YLeaf(YType.uint32, "policer-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("fgid_or_vqi",
                                            "index",
                                            "is_mcast",
                                            "is_valid",
                                            "policer_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.fgid_or_vqi.is_set or
                                self.index.is_set or
                                self.is_mcast.is_set or
                                self.is_valid.is_set or
                                self.policer_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.fgid_or_vqi.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.is_mcast.yfilter != YFilter.not_set or
                                self.is_valid.yfilter != YFilter.not_set or
                                self.policer_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bfd-entry-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.fgid_or_vqi.is_set or self.fgid_or_vqi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fgid_or_vqi.get_name_leafdata())
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.is_mcast.is_set or self.is_mcast.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_mcast.get_name_leafdata())
                            if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_valid.get_name_leafdata())
                            if (self.policer_id.is_set or self.policer_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policer_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fgid-or-vqi" or name == "index" or name == "is-mcast" or name == "is-valid" or name == "policer-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "fgid-or-vqi"):
                                self.fgid_or_vqi = value
                                self.fgid_or_vqi.value_namespace = name_space
                                self.fgid_or_vqi.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-mcast"):
                                self.is_mcast = value
                                self.is_mcast.value_namespace = name_space
                                self.is_mcast.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-valid"):
                                self.is_valid = value
                                self.is_valid.value_namespace = name_space
                                self.is_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "policer-id"):
                                self.policer_id = value
                                self.policer_id.value_namespace = name_space
                                self.policer_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.bfd_entry_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.bfd_entry_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd" + path_buffer

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

                        if (child_yang_name == "bfd-entry-info"):
                            for c in self.bfd_entry_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.bfd_entry_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bfd-entry-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Statistics(Entity):
                    """
                    Hardware Entry type
                    
                    .. attribute:: accepted
                    
                    	Deleted\-entry accepted packets counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_ts
                    
                    	Statistics clear timestamp
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dropped
                    
                    	Deleted\-entry dropped packets counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: no_stats_mem_err
                    
                    	No statistics memory error
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "hardware"

                        self.accepted = YLeaf(YType.uint64, "accepted")

                        self.clear_ts = YLeaf(YType.uint64, "clear-ts")

                        self.dropped = YLeaf(YType.uint64, "dropped")

                        self.no_stats_mem_err = YLeaf(YType.uint64, "no-stats-mem-err")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accepted",
                                        "clear_ts",
                                        "dropped",
                                        "no_stats_mem_err") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(LptsPifib_.Nodes.Node.Hardware.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accepted.is_set or
                            self.clear_ts.is_set or
                            self.dropped.is_set or
                            self.no_stats_mem_err.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accepted.yfilter != YFilter.not_set or
                            self.clear_ts.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.no_stats_mem_err.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accepted.get_name_leafdata())
                        if (self.clear_ts.is_set or self.clear_ts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_ts.get_name_leafdata())
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.no_stats_mem_err.is_set or self.no_stats_mem_err.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_stats_mem_err.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accepted" or name == "clear-ts" or name == "dropped" or name == "no-stats-mem-err"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accepted"):
                            self.accepted = value
                            self.accepted.value_namespace = name_space
                            self.accepted.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-ts"):
                            self.clear_ts = value
                            self.clear_ts.value_namespace = name_space
                            self.clear_ts.value_namespace_prefix = name_space_prefix
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-stats-mem-err"):
                            self.no_stats_mem_err = value
                            self.no_stats_mem_err.value_namespace = name_space
                            self.no_stats_mem_err.value_namespace_prefix = name_space_prefix


                class IndexEntries(Entity):
                    """
                    Hardware Entry options
                    
                    .. attribute:: index_entry
                    
                    	Entry options
                    	**type**\: list of    :py:class:`IndexEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.IndexEntries, self).__init__()

                        self.yang_name = "index-entries"
                        self.yang_parent_name = "hardware"

                        self.index_entry = YList(self)

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
                                    super(LptsPifib_.Nodes.Node.Hardware.IndexEntries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LptsPifib_.Nodes.Node.Hardware.IndexEntries, self).__setattr__(name, value)


                    class IndexEntry(Entity):
                        """
                        Entry options
                        
                        .. attribute:: index  <key>
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: acl_str
                        
                        	Acl name
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: action
                        
                        	Action
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: action_string
                        
                        	Action String
                        	**type**\:  str
                        
                        .. attribute:: cir
                        
                        	Committed Information Rate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: entry_ptr
                        
                        	ptr to ifib\_entry\_st
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: entry_shadow_ptr
                        
                        	ptr to ifib\_entry\_shadow\_st
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fgid_or_sfp
                        
                        	fabric group id or swith fabric port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hw_info
                        
                        	Per pipe type hardware info
                        	**type**\: list of    :py:class:`HwInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo>`
                        
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
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_optimized
                        
                        	Is optimized or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_uidb_opt_bit
                        
                        	Is uidb set for optimized entry or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_vrf
                        
                        	Is VRF or not
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
                        
                        .. attribute:: list_node_ptr
                        
                        	ptr to dlqueue list node
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_addr
                        
                        	Local IP Address
                        	**type**\:  str
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_prefix_len
                        
                        	Local Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lookup_priority
                        
                        	Lookup priority
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: no_stats
                        
                        	Stats not available
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: num_retries
                        
                        	retries count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: num_tm_entries
                        
                        	Number of TCAM entries used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: policer_avgrate
                        
                        	Policer avg. rate limit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policer_burst
                        
                        	Policer burst
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: priority
                        
                        	Flow priority or COS
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rack_id
                        
                        	Remote racknum if remote
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote IP Address
                        	**type**\:  str
                        
                        .. attribute:: remote_fgid
                        
                        	Remote FGID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_prefix_len
                        
                        	Remote Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_rack
                        
                        	Is entry remote or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: retry_fail_cause
                        
                        	failure cause
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rslot
                        
                        	Remote slotnum if remote
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid
                        
                        	Stream ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	state of pifib entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: storage_priority
                        
                        	Storage priority
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: u_len
                        
                        	Union Key Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: u_type
                        
                        	Union Key Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: u_value
                        
                        	Remote Port/ICMP Type/IGMP Type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: uidb_index
                        
                        	Interface uidb index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, self).__init__()

                            self.yang_name = "index-entry"
                            self.yang_parent_name = "index-entries"

                            self.index = YLeaf(YType.int32, "index")

                            self.acl_str = YLeaf(YType.str, "acl-str")

                            self.action = YLeaf(YType.uint8, "action")

                            self.action_string = YLeaf(YType.str, "action-string")

                            self.cir = YLeaf(YType.uint64, "cir")

                            self.entry_ptr = YLeaf(YType.uint32, "entry-ptr")

                            self.entry_shadow_ptr = YLeaf(YType.uint32, "entry-shadow-ptr")

                            self.fgid_or_sfp = YLeaf(YType.uint32, "fgid-or-sfp")

                            self.flow_type = YLeaf(YType.uint32, "flow-type")

                            self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                            self.intf_name = YLeaf(YType.str, "intf-name")

                            self.is_fgid = YLeaf(YType.uint8, "is-fgid")

                            self.is_frag = YLeaf(YType.uint8, "is-frag")

                            self.is_optimized = YLeaf(YType.uint8, "is-optimized")

                            self.is_syn = YLeaf(YType.uint8, "is-syn")

                            self.is_uidb_opt_bit = YLeaf(YType.uint8, "is-uidb-opt-bit")

                            self.is_vrf = YLeaf(YType.uint8, "is-vrf")

                            self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                            self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                            self.list_node_ptr = YLeaf(YType.uint32, "list-node-ptr")

                            self.listener_tag = YLeaf(YType.uint8, "listener-tag")

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.local_port = YLeaf(YType.uint32, "local-port")

                            self.local_prefix_len = YLeaf(YType.uint32, "local-prefix-len")

                            self.lookup_priority = YLeaf(YType.int32, "lookup-priority")

                            self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                            self.no_stats = YLeaf(YType.uint8, "no-stats")

                            self.num_retries = YLeaf(YType.uint8, "num-retries")

                            self.num_tm_entries = YLeaf(YType.int32, "num-tm-entries")

                            self.policer_avgrate = YLeaf(YType.uint32, "policer-avgrate")

                            self.policer_burst = YLeaf(YType.uint32, "policer-burst")

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.rack_id = YLeaf(YType.uint32, "rack-id")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.remote_fgid = YLeaf(YType.uint32, "remote-fgid")

                            self.remote_prefix_len = YLeaf(YType.uint32, "remote-prefix-len")

                            self.remote_rack = YLeaf(YType.uint8, "remote-rack")

                            self.retry_fail_cause = YLeaf(YType.uint8, "retry-fail-cause")

                            self.rslot = YLeaf(YType.uint32, "rslot")

                            self.sid = YLeaf(YType.uint32, "sid")

                            self.state = YLeaf(YType.uint8, "state")

                            self.storage_priority = YLeaf(YType.int32, "storage-priority")

                            self.u_len = YLeaf(YType.uint32, "u-len")

                            self.u_type = YLeaf(YType.uint8, "u-type")

                            self.u_value = YLeaf(YType.uint32, "u-value")

                            self.uidb_index = YLeaf(YType.uint32, "uidb-index")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.hw_info = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "acl_str",
                                            "action",
                                            "action_string",
                                            "cir",
                                            "entry_ptr",
                                            "entry_shadow_ptr",
                                            "fgid_or_sfp",
                                            "flow_type",
                                            "intf_handle",
                                            "intf_name",
                                            "is_fgid",
                                            "is_frag",
                                            "is_optimized",
                                            "is_syn",
                                            "is_uidb_opt_bit",
                                            "is_vrf",
                                            "l3protocol",
                                            "l4protocol",
                                            "list_node_ptr",
                                            "listener_tag",
                                            "local_addr",
                                            "local_port",
                                            "local_prefix_len",
                                            "lookup_priority",
                                            "min_ttl",
                                            "no_stats",
                                            "num_retries",
                                            "num_tm_entries",
                                            "policer_avgrate",
                                            "policer_burst",
                                            "priority",
                                            "rack_id",
                                            "remote_addr",
                                            "remote_fgid",
                                            "remote_prefix_len",
                                            "remote_rack",
                                            "retry_fail_cause",
                                            "rslot",
                                            "sid",
                                            "state",
                                            "storage_priority",
                                            "u_len",
                                            "u_type",
                                            "u_value",
                                            "uidb_index",
                                            "vrf_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, self).__setattr__(name, value)


                        class HwInfo(Entity):
                            """
                            Per pipe type hardware info
                            
                            .. attribute:: accepted
                            
                            	Accepted Packets Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped
                            
                            	Dropped Packets Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policer
                            
                            	Policer Pointer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sort_start_offset
                            
                            	Relative position in sorting order
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: stats_ptr
                            
                            	Stats Pointer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tm_start_offset
                            
                            	Relative position in TCAM
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, self).__init__()

                                self.yang_name = "hw-info"
                                self.yang_parent_name = "index-entry"

                                self.accepted = YLeaf(YType.uint64, "accepted")

                                self.dropped = YLeaf(YType.uint64, "dropped")

                                self.policer = YLeaf(YType.uint32, "policer")

                                self.sort_start_offset = YLeaf(YType.int32, "sort-start-offset")

                                self.stats_ptr = YLeaf(YType.uint32, "stats-ptr")

                                self.tm_start_offset = YLeaf(YType.int32, "tm-start-offset")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accepted",
                                                "dropped",
                                                "policer",
                                                "sort_start_offset",
                                                "stats_ptr",
                                                "tm_start_offset") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accepted.is_set or
                                    self.dropped.is_set or
                                    self.policer.is_set or
                                    self.sort_start_offset.is_set or
                                    self.stats_ptr.is_set or
                                    self.tm_start_offset.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accepted.yfilter != YFilter.not_set or
                                    self.dropped.yfilter != YFilter.not_set or
                                    self.policer.yfilter != YFilter.not_set or
                                    self.sort_start_offset.yfilter != YFilter.not_set or
                                    self.stats_ptr.yfilter != YFilter.not_set or
                                    self.tm_start_offset.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "hw-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.accepted.is_set or self.accepted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accepted.get_name_leafdata())
                                if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dropped.get_name_leafdata())
                                if (self.policer.is_set or self.policer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer.get_name_leafdata())
                                if (self.sort_start_offset.is_set or self.sort_start_offset.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sort_start_offset.get_name_leafdata())
                                if (self.stats_ptr.is_set or self.stats_ptr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stats_ptr.get_name_leafdata())
                                if (self.tm_start_offset.is_set or self.tm_start_offset.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tm_start_offset.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accepted" or name == "dropped" or name == "policer" or name == "sort-start-offset" or name == "stats-ptr" or name == "tm-start-offset"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accepted"):
                                    self.accepted = value
                                    self.accepted.value_namespace = name_space
                                    self.accepted.value_namespace_prefix = name_space_prefix
                                if(value_path == "dropped"):
                                    self.dropped = value
                                    self.dropped.value_namespace = name_space
                                    self.dropped.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer"):
                                    self.policer = value
                                    self.policer.value_namespace = name_space
                                    self.policer.value_namespace_prefix = name_space_prefix
                                if(value_path == "sort-start-offset"):
                                    self.sort_start_offset = value
                                    self.sort_start_offset.value_namespace = name_space
                                    self.sort_start_offset.value_namespace_prefix = name_space_prefix
                                if(value_path == "stats-ptr"):
                                    self.stats_ptr = value
                                    self.stats_ptr.value_namespace = name_space
                                    self.stats_ptr.value_namespace_prefix = name_space_prefix
                                if(value_path == "tm-start-offset"):
                                    self.tm_start_offset = value
                                    self.tm_start_offset.value_namespace = name_space
                                    self.tm_start_offset.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.hw_info:
                                if (c.has_data()):
                                    return True
                            return (
                                self.index.is_set or
                                self.acl_str.is_set or
                                self.action.is_set or
                                self.action_string.is_set or
                                self.cir.is_set or
                                self.entry_ptr.is_set or
                                self.entry_shadow_ptr.is_set or
                                self.fgid_or_sfp.is_set or
                                self.flow_type.is_set or
                                self.intf_handle.is_set or
                                self.intf_name.is_set or
                                self.is_fgid.is_set or
                                self.is_frag.is_set or
                                self.is_optimized.is_set or
                                self.is_syn.is_set or
                                self.is_uidb_opt_bit.is_set or
                                self.is_vrf.is_set or
                                self.l3protocol.is_set or
                                self.l4protocol.is_set or
                                self.list_node_ptr.is_set or
                                self.listener_tag.is_set or
                                self.local_addr.is_set or
                                self.local_port.is_set or
                                self.local_prefix_len.is_set or
                                self.lookup_priority.is_set or
                                self.min_ttl.is_set or
                                self.no_stats.is_set or
                                self.num_retries.is_set or
                                self.num_tm_entries.is_set or
                                self.policer_avgrate.is_set or
                                self.policer_burst.is_set or
                                self.priority.is_set or
                                self.rack_id.is_set or
                                self.remote_addr.is_set or
                                self.remote_fgid.is_set or
                                self.remote_prefix_len.is_set or
                                self.remote_rack.is_set or
                                self.retry_fail_cause.is_set or
                                self.rslot.is_set or
                                self.sid.is_set or
                                self.state.is_set or
                                self.storage_priority.is_set or
                                self.u_len.is_set or
                                self.u_type.is_set or
                                self.u_value.is_set or
                                self.uidb_index.is_set or
                                self.vrf_id.is_set)

                        def has_operation(self):
                            for c in self.hw_info:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.acl_str.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set or
                                self.action_string.yfilter != YFilter.not_set or
                                self.cir.yfilter != YFilter.not_set or
                                self.entry_ptr.yfilter != YFilter.not_set or
                                self.entry_shadow_ptr.yfilter != YFilter.not_set or
                                self.fgid_or_sfp.yfilter != YFilter.not_set or
                                self.flow_type.yfilter != YFilter.not_set or
                                self.intf_handle.yfilter != YFilter.not_set or
                                self.intf_name.yfilter != YFilter.not_set or
                                self.is_fgid.yfilter != YFilter.not_set or
                                self.is_frag.yfilter != YFilter.not_set or
                                self.is_optimized.yfilter != YFilter.not_set or
                                self.is_syn.yfilter != YFilter.not_set or
                                self.is_uidb_opt_bit.yfilter != YFilter.not_set or
                                self.is_vrf.yfilter != YFilter.not_set or
                                self.l3protocol.yfilter != YFilter.not_set or
                                self.l4protocol.yfilter != YFilter.not_set or
                                self.list_node_ptr.yfilter != YFilter.not_set or
                                self.listener_tag.yfilter != YFilter.not_set or
                                self.local_addr.yfilter != YFilter.not_set or
                                self.local_port.yfilter != YFilter.not_set or
                                self.local_prefix_len.yfilter != YFilter.not_set or
                                self.lookup_priority.yfilter != YFilter.not_set or
                                self.min_ttl.yfilter != YFilter.not_set or
                                self.no_stats.yfilter != YFilter.not_set or
                                self.num_retries.yfilter != YFilter.not_set or
                                self.num_tm_entries.yfilter != YFilter.not_set or
                                self.policer_avgrate.yfilter != YFilter.not_set or
                                self.policer_burst.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.rack_id.yfilter != YFilter.not_set or
                                self.remote_addr.yfilter != YFilter.not_set or
                                self.remote_fgid.yfilter != YFilter.not_set or
                                self.remote_prefix_len.yfilter != YFilter.not_set or
                                self.remote_rack.yfilter != YFilter.not_set or
                                self.retry_fail_cause.yfilter != YFilter.not_set or
                                self.rslot.yfilter != YFilter.not_set or
                                self.sid.yfilter != YFilter.not_set or
                                self.state.yfilter != YFilter.not_set or
                                self.storage_priority.yfilter != YFilter.not_set or
                                self.u_len.yfilter != YFilter.not_set or
                                self.u_type.yfilter != YFilter.not_set or
                                self.u_value.yfilter != YFilter.not_set or
                                self.uidb_index.yfilter != YFilter.not_set or
                                self.vrf_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "index-entry" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.acl_str.is_set or self.acl_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_str.get_name_leafdata())
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())
                            if (self.action_string.is_set or self.action_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action_string.get_name_leafdata())
                            if (self.cir.is_set or self.cir.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cir.get_name_leafdata())
                            if (self.entry_ptr.is_set or self.entry_ptr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entry_ptr.get_name_leafdata())
                            if (self.entry_shadow_ptr.is_set or self.entry_shadow_ptr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entry_shadow_ptr.get_name_leafdata())
                            if (self.fgid_or_sfp.is_set or self.fgid_or_sfp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fgid_or_sfp.get_name_leafdata())
                            if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_type.get_name_leafdata())
                            if (self.intf_handle.is_set or self.intf_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_handle.get_name_leafdata())
                            if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.intf_name.get_name_leafdata())
                            if (self.is_fgid.is_set or self.is_fgid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_fgid.get_name_leafdata())
                            if (self.is_frag.is_set or self.is_frag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_frag.get_name_leafdata())
                            if (self.is_optimized.is_set or self.is_optimized.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_optimized.get_name_leafdata())
                            if (self.is_syn.is_set or self.is_syn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_syn.get_name_leafdata())
                            if (self.is_uidb_opt_bit.is_set or self.is_uidb_opt_bit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_uidb_opt_bit.get_name_leafdata())
                            if (self.is_vrf.is_set or self.is_vrf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_vrf.get_name_leafdata())
                            if (self.l3protocol.is_set or self.l3protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.l3protocol.get_name_leafdata())
                            if (self.l4protocol.is_set or self.l4protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.l4protocol.get_name_leafdata())
                            if (self.list_node_ptr.is_set or self.list_node_ptr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.list_node_ptr.get_name_leafdata())
                            if (self.listener_tag.is_set or self.listener_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.listener_tag.get_name_leafdata())
                            if (self.local_addr.is_set or self.local_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_addr.get_name_leafdata())
                            if (self.local_port.is_set or self.local_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_port.get_name_leafdata())
                            if (self.local_prefix_len.is_set or self.local_prefix_len.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_prefix_len.get_name_leafdata())
                            if (self.lookup_priority.is_set or self.lookup_priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lookup_priority.get_name_leafdata())
                            if (self.min_ttl.is_set or self.min_ttl.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min_ttl.get_name_leafdata())
                            if (self.no_stats.is_set or self.no_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_stats.get_name_leafdata())
                            if (self.num_retries.is_set or self.num_retries.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_retries.get_name_leafdata())
                            if (self.num_tm_entries.is_set or self.num_tm_entries.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_tm_entries.get_name_leafdata())
                            if (self.policer_avgrate.is_set or self.policer_avgrate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policer_avgrate.get_name_leafdata())
                            if (self.policer_burst.is_set or self.policer_burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policer_burst.get_name_leafdata())
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.rack_id.is_set or self.rack_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rack_id.get_name_leafdata())
                            if (self.remote_addr.is_set or self.remote_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_addr.get_name_leafdata())
                            if (self.remote_fgid.is_set or self.remote_fgid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_fgid.get_name_leafdata())
                            if (self.remote_prefix_len.is_set or self.remote_prefix_len.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_prefix_len.get_name_leafdata())
                            if (self.remote_rack.is_set or self.remote_rack.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_rack.get_name_leafdata())
                            if (self.retry_fail_cause.is_set or self.retry_fail_cause.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.retry_fail_cause.get_name_leafdata())
                            if (self.rslot.is_set or self.rslot.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rslot.get_name_leafdata())
                            if (self.sid.is_set or self.sid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sid.get_name_leafdata())
                            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.state.get_name_leafdata())
                            if (self.storage_priority.is_set or self.storage_priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.storage_priority.get_name_leafdata())
                            if (self.u_len.is_set or self.u_len.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.u_len.get_name_leafdata())
                            if (self.u_type.is_set or self.u_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.u_type.get_name_leafdata())
                            if (self.u_value.is_set or self.u_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.u_value.get_name_leafdata())
                            if (self.uidb_index.is_set or self.uidb_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.uidb_index.get_name_leafdata())
                            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "hw-info"):
                                for c in self.hw_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.hw_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hw-info" or name == "index" or name == "acl-str" or name == "action" or name == "action-string" or name == "cir" or name == "entry-ptr" or name == "entry-shadow-ptr" or name == "fgid-or-sfp" or name == "flow-type" or name == "intf-handle" or name == "intf-name" or name == "is-fgid" or name == "is-frag" or name == "is-optimized" or name == "is-syn" or name == "is-uidb-opt-bit" or name == "is-vrf" or name == "l3protocol" or name == "l4protocol" or name == "list-node-ptr" or name == "listener-tag" or name == "local-addr" or name == "local-port" or name == "local-prefix-len" or name == "lookup-priority" or name == "min-ttl" or name == "no-stats" or name == "num-retries" or name == "num-tm-entries" or name == "policer-avgrate" or name == "policer-burst" or name == "priority" or name == "rack-id" or name == "remote-addr" or name == "remote-fgid" or name == "remote-prefix-len" or name == "remote-rack" or name == "retry-fail-cause" or name == "rslot" or name == "sid" or name == "state" or name == "storage-priority" or name == "u-len" or name == "u-type" or name == "u-value" or name == "uidb-index" or name == "vrf-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-str"):
                                self.acl_str = value
                                self.acl_str.value_namespace = name_space
                                self.acl_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix
                            if(value_path == "action-string"):
                                self.action_string = value
                                self.action_string.value_namespace = name_space
                                self.action_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "cir"):
                                self.cir = value
                                self.cir.value_namespace = name_space
                                self.cir.value_namespace_prefix = name_space_prefix
                            if(value_path == "entry-ptr"):
                                self.entry_ptr = value
                                self.entry_ptr.value_namespace = name_space
                                self.entry_ptr.value_namespace_prefix = name_space_prefix
                            if(value_path == "entry-shadow-ptr"):
                                self.entry_shadow_ptr = value
                                self.entry_shadow_ptr.value_namespace = name_space
                                self.entry_shadow_ptr.value_namespace_prefix = name_space_prefix
                            if(value_path == "fgid-or-sfp"):
                                self.fgid_or_sfp = value
                                self.fgid_or_sfp.value_namespace = name_space
                                self.fgid_or_sfp.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-type"):
                                self.flow_type = value
                                self.flow_type.value_namespace = name_space
                                self.flow_type.value_namespace_prefix = name_space_prefix
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
                            if(value_path == "is-frag"):
                                self.is_frag = value
                                self.is_frag.value_namespace = name_space
                                self.is_frag.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-optimized"):
                                self.is_optimized = value
                                self.is_optimized.value_namespace = name_space
                                self.is_optimized.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-syn"):
                                self.is_syn = value
                                self.is_syn.value_namespace = name_space
                                self.is_syn.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-uidb-opt-bit"):
                                self.is_uidb_opt_bit = value
                                self.is_uidb_opt_bit.value_namespace = name_space
                                self.is_uidb_opt_bit.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-vrf"):
                                self.is_vrf = value
                                self.is_vrf.value_namespace = name_space
                                self.is_vrf.value_namespace_prefix = name_space_prefix
                            if(value_path == "l3protocol"):
                                self.l3protocol = value
                                self.l3protocol.value_namespace = name_space
                                self.l3protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "l4protocol"):
                                self.l4protocol = value
                                self.l4protocol.value_namespace = name_space
                                self.l4protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "list-node-ptr"):
                                self.list_node_ptr = value
                                self.list_node_ptr.value_namespace = name_space
                                self.list_node_ptr.value_namespace_prefix = name_space_prefix
                            if(value_path == "listener-tag"):
                                self.listener_tag = value
                                self.listener_tag.value_namespace = name_space
                                self.listener_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "local-addr"):
                                self.local_addr = value
                                self.local_addr.value_namespace = name_space
                                self.local_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "local-port"):
                                self.local_port = value
                                self.local_port.value_namespace = name_space
                                self.local_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "local-prefix-len"):
                                self.local_prefix_len = value
                                self.local_prefix_len.value_namespace = name_space
                                self.local_prefix_len.value_namespace_prefix = name_space_prefix
                            if(value_path == "lookup-priority"):
                                self.lookup_priority = value
                                self.lookup_priority.value_namespace = name_space
                                self.lookup_priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "min-ttl"):
                                self.min_ttl = value
                                self.min_ttl.value_namespace = name_space
                                self.min_ttl.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-stats"):
                                self.no_stats = value
                                self.no_stats.value_namespace = name_space
                                self.no_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-retries"):
                                self.num_retries = value
                                self.num_retries.value_namespace = name_space
                                self.num_retries.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-tm-entries"):
                                self.num_tm_entries = value
                                self.num_tm_entries.value_namespace = name_space
                                self.num_tm_entries.value_namespace_prefix = name_space_prefix
                            if(value_path == "policer-avgrate"):
                                self.policer_avgrate = value
                                self.policer_avgrate.value_namespace = name_space
                                self.policer_avgrate.value_namespace_prefix = name_space_prefix
                            if(value_path == "policer-burst"):
                                self.policer_burst = value
                                self.policer_burst.value_namespace = name_space
                                self.policer_burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "rack-id"):
                                self.rack_id = value
                                self.rack_id.value_namespace = name_space
                                self.rack_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-addr"):
                                self.remote_addr = value
                                self.remote_addr.value_namespace = name_space
                                self.remote_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-fgid"):
                                self.remote_fgid = value
                                self.remote_fgid.value_namespace = name_space
                                self.remote_fgid.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-prefix-len"):
                                self.remote_prefix_len = value
                                self.remote_prefix_len.value_namespace = name_space
                                self.remote_prefix_len.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-rack"):
                                self.remote_rack = value
                                self.remote_rack.value_namespace = name_space
                                self.remote_rack.value_namespace_prefix = name_space_prefix
                            if(value_path == "retry-fail-cause"):
                                self.retry_fail_cause = value
                                self.retry_fail_cause.value_namespace = name_space
                                self.retry_fail_cause.value_namespace_prefix = name_space_prefix
                            if(value_path == "rslot"):
                                self.rslot = value
                                self.rslot.value_namespace = name_space
                                self.rslot.value_namespace_prefix = name_space_prefix
                            if(value_path == "sid"):
                                self.sid = value
                                self.sid.value_namespace = name_space
                                self.sid.value_namespace_prefix = name_space_prefix
                            if(value_path == "state"):
                                self.state = value
                                self.state.value_namespace = name_space
                                self.state.value_namespace_prefix = name_space_prefix
                            if(value_path == "storage-priority"):
                                self.storage_priority = value
                                self.storage_priority.value_namespace = name_space
                                self.storage_priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "u-len"):
                                self.u_len = value
                                self.u_len.value_namespace = name_space
                                self.u_len.value_namespace_prefix = name_space_prefix
                            if(value_path == "u-type"):
                                self.u_type = value
                                self.u_type.value_namespace = name_space
                                self.u_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "u-value"):
                                self.u_value = value
                                self.u_value.value_namespace = name_space
                                self.u_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "uidb-index"):
                                self.uidb_index = value
                                self.uidb_index.value_namespace = name_space
                                self.uidb_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-id"):
                                self.vrf_id = value
                                self.vrf_id.value_namespace = name_space
                                self.vrf_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.index_entry:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.index_entry:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "index-entries" + path_buffer

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

                        if (child_yang_name == "index-entry"):
                            for c in self.index_entry:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.index_entry.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "index-entry"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.bfd is not None and self.bfd.has_data()) or
                        (self.index_entries is not None and self.index_entries.has_data()) or
                        (self.police is not None and self.police.has_data()) or
                        (self.static_police is not None and self.static_police.has_data()) or
                        (self.statistics is not None and self.statistics.has_data()) or
                        (self.usage_entries is not None and self.usage_entries.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.bfd is not None and self.bfd.has_operation()) or
                        (self.index_entries is not None and self.index_entries.has_operation()) or
                        (self.police is not None and self.police.has_operation()) or
                        (self.static_police is not None and self.static_police.has_operation()) or
                        (self.statistics is not None and self.statistics.has_operation()) or
                        (self.usage_entries is not None and self.usage_entries.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-platform-pifib-oper:hardware" + path_buffer

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

                    if (child_yang_name == "bfd"):
                        if (self.bfd is None):
                            self.bfd = LptsPifib_.Nodes.Node.Hardware.Bfd()
                            self.bfd.parent = self
                            self._children_name_map["bfd"] = "bfd"
                        return self.bfd

                    if (child_yang_name == "index-entries"):
                        if (self.index_entries is None):
                            self.index_entries = LptsPifib_.Nodes.Node.Hardware.IndexEntries()
                            self.index_entries.parent = self
                            self._children_name_map["index_entries"] = "index-entries"
                        return self.index_entries

                    if (child_yang_name == "police"):
                        if (self.police is None):
                            self.police = LptsPifib_.Nodes.Node.Hardware.Police()
                            self.police.parent = self
                            self._children_name_map["police"] = "police"
                        return self.police

                    if (child_yang_name == "static-police"):
                        if (self.static_police is None):
                            self.static_police = LptsPifib_.Nodes.Node.Hardware.StaticPolice()
                            self.static_police.parent = self
                            self._children_name_map["static_police"] = "static-police"
                        return self.static_police

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = LptsPifib_.Nodes.Node.Hardware.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    if (child_yang_name == "usage-entries"):
                        if (self.usage_entries is None):
                            self.usage_entries = LptsPifib_.Nodes.Node.Hardware.UsageEntries()
                            self.usage_entries.parent = self
                            self._children_name_map["usage_entries"] = "usage-entries"
                        return self.usage_entries

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd" or name == "index-entries" or name == "police" or name == "static-police" or name == "statistics" or name == "usage-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.hardware is not None and self.hardware.has_data()) or
                    (self.type_values is not None and self.type_values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.hardware is not None and self.hardware.has_operation()) or
                    (self.type_values is not None and self.type_values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "hardware"):
                    if (self.hardware is None):
                        self.hardware = LptsPifib_.Nodes.Node.Hardware()
                        self.hardware.parent = self
                        self._children_name_map["hardware"] = "hardware"
                    return self.hardware

                if (child_yang_name == "type-values"):
                    if (self.type_values is None):
                        self.type_values = LptsPifib_.Nodes.Node.TypeValues()
                        self.type_values.parent = self
                        self._children_name_map["type_values"] = "type-values"
                    return self.type_values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hardware" or name == "type-values" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/%s" % self.get_segment_path()
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
                c = LptsPifib_.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib" + path_buffer

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
                self.nodes = LptsPifib_.Nodes()
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
        self._top_entity = LptsPifib_()
        return self._top_entity

