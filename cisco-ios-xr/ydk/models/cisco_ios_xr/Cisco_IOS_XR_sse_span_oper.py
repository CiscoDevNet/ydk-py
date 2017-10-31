""" Cisco_IOS_XR_sse_span_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sse\-span package operational data.

This module contains definitions
for the following management objects\:
  ssespan\: SSE SPAN operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ssespan(Entity):
    """
    SSE SPAN operational data
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes>`
    
    

    """

    _prefix = 'sse-span-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ssespan, self).__init__()
        self._top_entity = None

        self.yang_name = "ssespan"
        self.yang_parent_name = "Cisco-IOS-XR-sse-span-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", Ssespan.Nodes)}
        self._child_list_classes = {}

        self.nodes = Ssespan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan"


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node>`
        
        

        """

        _prefix = 'sse-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ssespan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ssespan"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Ssespan.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ssespan.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\:  str
            
            .. attribute:: span_mirr_infos
            
            	SPAN SFT entry
            	**type**\:   :py:class:`SpanMirrInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanMirrInfos>`
            
            .. attribute:: spanudf
            
            	udf info
            	**type**\:   :py:class:`Spanudf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.Spanudf>`
            
            .. attribute:: span_sess_infos
            
            	SPAN SDT entry
            	**type**\:   :py:class:`SpanSessInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanSessInfos>`
            
            

            """

            _prefix = 'sse-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ssespan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"span-mirr-infos" : ("span_mirr_infos", Ssespan.Nodes.Node.SpanMirrInfos), "spanudf" : ("spanudf", Ssespan.Nodes.Node.Spanudf), "span-sess-infos" : ("span_sess_infos", Ssespan.Nodes.Node.SpanSessInfos)}
                self._child_list_classes = {}

                self.node = YLeaf(YType.str, "node")

                self.span_mirr_infos = Ssespan.Nodes.Node.SpanMirrInfos()
                self.span_mirr_infos.parent = self
                self._children_name_map["span_mirr_infos"] = "span-mirr-infos"
                self._children_yang_names.add("span-mirr-infos")

                self.spanudf = Ssespan.Nodes.Node.Spanudf()
                self.spanudf.parent = self
                self._children_name_map["spanudf"] = "spanudf"
                self._children_yang_names.add("spanudf")

                self.span_sess_infos = Ssespan.Nodes.Node.SpanSessInfos()
                self.span_sess_infos.parent = self
                self._children_name_map["span_sess_infos"] = "span-sess-infos"
                self._children_yang_names.add("span-sess-infos")
                self._segment_path = lambda: "node" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ssespan.Nodes.Node, ['node'], name, value)


            class SpanMirrInfos(Entity):
                """
                SPAN SFT entry
                
                .. attribute:: span_mirr_info
                
                	Mirror info 
                	**type**\: list of    :py:class:`SpanMirrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo>`
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ssespan.Nodes.Node.SpanMirrInfos, self).__init__()

                    self.yang_name = "span-mirr-infos"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"span-mirr-info" : ("span_mirr_info", Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo)}

                    self.span_mirr_info = YList(self)
                    self._segment_path = lambda: "span-mirr-infos"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.SpanMirrInfos, [], name, value)


                class SpanMirrInfo(Entity):
                    """
                    Mirror info 
                    
                    .. attribute:: intf_name  <key>
                    
                    	interface name
                    	**type**\:  str
                    
                    .. attribute:: src_ifh
                    
                    	source IFH
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_name_xr
                    
                    	interface name
                    	**type**\:  str
                    
                    .. attribute:: v4_acl_flag
                    
                    	ipv4 acl flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v6_acl_flag
                    
                    	ipv6 acl flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gre_acl_flag
                    
                    	gre acl flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v4state
                    
                    	ipv4 state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v6state
                    
                    	ipv6 state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gre_state
                    
                    	gre state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v4sessid
                    
                    	ipv4 session Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v6sessid
                    
                    	ipv6 session Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gre_sessid
                    
                    	gre session Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v4dst_type
                    
                    	ipv4 dst type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v6dst_type
                    
                    	ipv6 dst type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gredst_type
                    
                    	gre dst type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v4statsptr
                    
                    	v4 stats ptr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: v6statsptr
                    
                    	v6 stats ptr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: grev4statsptr
                    
                    	mpls ipv4 stats ptr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: grev6statsptr
                    
                    	mpls ipv6 stats ptr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mplsv4stats
                    
                    	mpls ipv4 pkts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mplsv6pkts
                    
                    	mpls ipv6 pkts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: np_umask
                    
                    	npu mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: uidb
                    
                    	uidb array 
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sft_hw_data
                    
                    	16x5npu=80 bytes of hw sft entry
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'sse-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo, self).__init__()

                        self.yang_name = "span-mirr-info"
                        self.yang_parent_name = "span-mirr-infos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.intf_name = YLeaf(YType.str, "intf-name")

                        self.src_ifh = YLeaf(YType.uint32, "src-ifh")

                        self.intf_name_xr = YLeaf(YType.str, "intf-name-xr")

                        self.v4_acl_flag = YLeaf(YType.uint32, "v4-acl-flag")

                        self.v6_acl_flag = YLeaf(YType.uint32, "v6-acl-flag")

                        self.gre_acl_flag = YLeaf(YType.uint32, "gre-acl-flag")

                        self.v4state = YLeaf(YType.uint32, "v4state")

                        self.v6state = YLeaf(YType.uint32, "v6state")

                        self.gre_state = YLeaf(YType.uint32, "gre-state")

                        self.v4sessid = YLeaf(YType.uint32, "v4sessid")

                        self.v6sessid = YLeaf(YType.uint32, "v6sessid")

                        self.gre_sessid = YLeaf(YType.uint32, "gre-sessid")

                        self.v4dst_type = YLeaf(YType.uint32, "v4dst-type")

                        self.v6dst_type = YLeaf(YType.uint32, "v6dst-type")

                        self.gredst_type = YLeaf(YType.uint32, "gredst-type")

                        self.v4statsptr = YLeaf(YType.uint32, "v4statsptr")

                        self.v6statsptr = YLeaf(YType.uint32, "v6statsptr")

                        self.grev4statsptr = YLeaf(YType.uint32, "grev4statsptr")

                        self.grev6statsptr = YLeaf(YType.uint32, "grev6statsptr")

                        self.mplsv4stats = YLeaf(YType.uint32, "mplsv4stats")

                        self.mplsv6pkts = YLeaf(YType.uint32, "mplsv6pkts")

                        self.np_umask = YLeaf(YType.uint32, "np-umask")

                        self.uidb = YLeafList(YType.uint32, "uidb")

                        self.sft_hw_data = YLeafList(YType.uint32, "sft-hw-data")
                        self._segment_path = lambda: "span-mirr-info" + "[intf-name='" + self.intf_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo, ['intf_name', 'src_ifh', 'intf_name_xr', 'v4_acl_flag', 'v6_acl_flag', 'gre_acl_flag', 'v4state', 'v6state', 'gre_state', 'v4sessid', 'v6sessid', 'gre_sessid', 'v4dst_type', 'v6dst_type', 'gredst_type', 'v4statsptr', 'v6statsptr', 'grev4statsptr', 'grev6statsptr', 'mplsv4stats', 'mplsv6pkts', 'np_umask', 'uidb', 'sft_hw_data'], name, value)


            class Spanudf(Entity):
                """
                udf info
                
                .. attribute:: udf_hdr
                
                	udf header
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: udf_type
                
                	udf type
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: udf_len
                
                	udf len
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: udf_value
                
                	udf value
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: udf_hw_data
                
                	16x5npu=80 bytes of hw udf entry
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ssespan.Nodes.Node.Spanudf, self).__init__()

                    self.yang_name = "spanudf"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.udf_hdr = YLeafList(YType.uint32, "udf-hdr")

                    self.udf_type = YLeafList(YType.uint32, "udf-type")

                    self.udf_len = YLeafList(YType.uint32, "udf-len")

                    self.udf_value = YLeafList(YType.uint32, "udf-value")

                    self.udf_hw_data = YLeafList(YType.uint32, "udf-hw-data")
                    self._segment_path = lambda: "spanudf"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.Spanudf, ['udf_hdr', 'udf_type', 'udf_len', 'udf_value', 'udf_hw_data'], name, value)


            class SpanSessInfos(Entity):
                """
                SPAN SDT entry
                
                .. attribute:: span_sess_info
                
                	Session info 
                	**type**\: list of    :py:class:`SpanSessInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo>`
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ssespan.Nodes.Node.SpanSessInfos, self).__init__()

                    self.yang_name = "span-sess-infos"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"span-sess-info" : ("span_sess_info", Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo)}

                    self.span_sess_info = YList(self)
                    self._segment_path = lambda: "span-sess-infos"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.SpanSessInfos, [], name, value)


                class SpanSessInfo(Entity):
                    """
                    Session info 
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: session_class  <key>
                    
                    	Session class
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: valid
                    
                    	marks validity of entry
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	session state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: class_
                    
                    	session Class gre,ipv4,ipv6
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ifhandle
                    
                    	ifhandle of interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mode
                    
                    	Tunnel mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_type
                    
                    	IP type v4 or v6 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	Vrf Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tos_bit
                    
                    	type of service
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tos_bit_copied
                    
                    	type of service copied
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dfbit
                    
                    	DF bit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src_ip
                    
                    	src ip v4 or v6
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dst_ip
                    
                    	dst ip v4 or v6
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sdt_hw_data
                    
                    	16x5npu=80 bytes of hw sdt entry
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'sse-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo, self).__init__()

                        self.yang_name = "span-sess-info"
                        self.yang_parent_name = "span-sess-infos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.session_class = YLeaf(YType.int32, "session-class")

                        self.valid = YLeaf(YType.uint8, "valid")

                        self.id = YLeaf(YType.uint32, "id")

                        self.state = YLeaf(YType.uint32, "state")

                        self.class_ = YLeaf(YType.uint32, "class")

                        self.ifhandle = YLeaf(YType.uint32, "ifhandle")

                        self.mode = YLeaf(YType.uint32, "mode")

                        self.ip_type = YLeaf(YType.uint32, "ip-type")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                        self.tos_bit = YLeaf(YType.uint32, "tos-bit")

                        self.tos_bit_copied = YLeaf(YType.uint32, "tos-bit-copied")

                        self.ttl = YLeaf(YType.uint32, "ttl")

                        self.dfbit = YLeaf(YType.uint32, "dfbit")

                        self.src_ip = YLeafList(YType.uint32, "src-ip")

                        self.dst_ip = YLeafList(YType.uint32, "dst-ip")

                        self.sdt_hw_data = YLeafList(YType.uint32, "sdt-hw-data")
                        self._segment_path = lambda: "span-sess-info" + "[session-id='" + self.session_id.get() + "']" + "[session-class='" + self.session_class.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo, ['session_id', 'session_class', 'valid', 'id', 'state', 'class_', 'ifhandle', 'mode', 'ip_type', 'vrf_id', 'tos_bit', 'tos_bit_copied', 'ttl', 'dfbit', 'src_ip', 'dst_ip', 'sdt_hw_data'], name, value)

    def clone_ptr(self):
        self._top_entity = Ssespan()
        return self._top_entity

