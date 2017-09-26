""" Cisco_IOS_XR_lpts_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-ifib\: lpts ifib database

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", LptsIfib.Nodes)}
        self._child_list_classes = {}

        self.nodes = LptsIfib.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", LptsIfib.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LptsIfib.Nodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"slice-ids" : ("slice_ids", LptsIfib.Nodes.Node.SliceIds)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.slice_ids = LptsIfib.Nodes.Node.SliceIds()
                self.slice_ids.parent = self
                self._children_name_map["slice_ids"] = "slice-ids"
                self._children_yang_names.add("slice-ids")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LptsIfib.Nodes.Node, ['node_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"slice-id" : ("slice_id", LptsIfib.Nodes.Node.SliceIds.SliceId)}

                    self.slice_id = YList(self)
                    self._segment_path = lambda: "slice-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsIfib.Nodes.Node.SliceIds, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"entry" : ("entry", LptsIfib.Nodes.Node.SliceIds.SliceId.Entry)}

                        self.slice_name = YLeaf(YType.str, "slice-name")

                        self.entry = YList(self)
                        self._segment_path = lambda: "slice-id" + "[slice-name='" + self.slice_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsIfib.Nodes.Node.SliceIds.SliceId, ['slice_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "entry" + "[entry='" + self.entry.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsIfib.Nodes.Node.SliceIds.SliceId.Entry, ['entry', 'accepts', 'deliver_list_long', 'deliver_list_short', 'destination_addr', 'destination_type', 'destination_value', 'drops', 'flow_type', 'ifib_program_time', 'intf_handle', 'intf_name', 'is_fgid', 'is_syn', 'l3protocol', 'l4protocol', 'listener_tag', 'local_flag', 'min_ttl', 'opcode', 'pending_ifibq_delay', 'sl_ifibq_delay', 'source_addr', 'source_port', 'vid', 'vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = LptsIfib()
        return self._top_entity

