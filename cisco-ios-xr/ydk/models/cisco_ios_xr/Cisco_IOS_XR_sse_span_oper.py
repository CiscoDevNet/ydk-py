""" Cisco_IOS_XR_sse_span_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sse\-span package operational data.

This module contains definitions
for the following management objects\:
  ssespan\: SSE SPAN operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ssespan(_Entity_):
    """
    SSE SPAN operational data
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'sse-span-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ssespan, self).__init__()
        self._top_entity = None

        self.yang_name = "ssespan"
        self.yang_parent_name = "Cisco-IOS-XR-sse-span-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ssespan.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Ssespan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssespan, [], name, value)


    class Nodes(_Entity_):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'sse-span-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ssespan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ssespan"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ssespan.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssespan.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: span_mirr_infos
            
            	SPAN SFT entry
            	**type**\:  :py:class:`SpanMirrInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanMirrInfos>`
            
            	**config**\: False
            
            .. attribute:: spanudf
            
            	udf info
            	**type**\:  :py:class:`Spanudf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.Spanudf>`
            
            	**config**\: False
            
            .. attribute:: span_sess_infos
            
            	SPAN SDT entry
            	**type**\:  :py:class:`SpanSessInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanSessInfos>`
            
            	**config**\: False
            
            

            """

            _prefix = 'sse-span-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ssespan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("span-mirr-infos", ("span_mirr_infos", Ssespan.Nodes.Node.SpanMirrInfos)), ("spanudf", ("spanudf", Ssespan.Nodes.Node.Spanudf)), ("span-sess-infos", ("span_sess_infos", Ssespan.Nodes.Node.SpanSessInfos))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.span_mirr_infos = Ssespan.Nodes.Node.SpanMirrInfos()
                self.span_mirr_infos.parent = self
                self._children_name_map["span_mirr_infos"] = "span-mirr-infos"

                self.spanudf = Ssespan.Nodes.Node.Spanudf()
                self.spanudf.parent = self
                self._children_name_map["spanudf"] = "spanudf"

                self.span_sess_infos = Ssespan.Nodes.Node.SpanSessInfos()
                self.span_sess_infos.parent = self
                self._children_name_map["span_sess_infos"] = "span-sess-infos"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sse-span-oper:ssespan/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssespan.Nodes.Node, ['node'], name, value)


            class SpanMirrInfos(_Entity_):
                """
                SPAN SFT entry
                
                .. attribute:: span_mirr_info
                
                	Mirror info 
                	**type**\: list of  		 :py:class:`SpanMirrInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssespan.Nodes.Node.SpanMirrInfos, self).__init__()

                    self.yang_name = "span-mirr-infos"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("span-mirr-info", ("span_mirr_info", Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo))])
                    self._leafs = OrderedDict()

                    self.span_mirr_info = YList(self)
                    self._segment_path = lambda: "span-mirr-infos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.SpanMirrInfos, [], name, value)


                class SpanMirrInfo(_Entity_):
                    """
                    Mirror info 
                    
                    .. attribute:: intf_name  (key)
                    
                    	interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: src_ifh
                    
                    	source IFH
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: intf_name_xr
                    
                    	interface name
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    .. attribute:: v4_acl_flag
                    
                    	ipv4 acl flag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v6_acl_flag
                    
                    	ipv6 acl flag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gre_acl_flag
                    
                    	gre acl flag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v4state
                    
                    	ipv4 state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v6state
                    
                    	ipv6 state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gre_state
                    
                    	gre state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v4sessid
                    
                    	ipv4 session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v6sessid
                    
                    	ipv6 session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gre_sessid
                    
                    	gre session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v4dst_type
                    
                    	ipv4 dst type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v6dst_type
                    
                    	ipv6 dst type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gredst_type
                    
                    	gre dst type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v4statsptr
                    
                    	v4 stats ptr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: v6statsptr
                    
                    	v6 stats ptr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: grev4statsptr
                    
                    	mpls ipv4 stats ptr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: grev6statsptr
                    
                    	mpls ipv6 stats ptr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mplsv4stats
                    
                    	mpls ipv4 pkts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mplsv6pkts
                    
                    	mpls ipv6 pkts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: np_umask
                    
                    	npu mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: uidb
                    
                    	uidb array 
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sft_hw_data
                    
                    	16x5npu=80 bytes of hw sft entry
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sse-span-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo, self).__init__()

                        self.yang_name = "span-mirr-info"
                        self.yang_parent_name = "span-mirr-infos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['intf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                            ('src_ifh', (YLeaf(YType.uint32, 'src-ifh'), ['int'])),
                            ('intf_name_xr', (YLeaf(YType.str, 'intf-name-xr'), ['str'])),
                            ('v4_acl_flag', (YLeaf(YType.uint32, 'v4-acl-flag'), ['int'])),
                            ('v6_acl_flag', (YLeaf(YType.uint32, 'v6-acl-flag'), ['int'])),
                            ('gre_acl_flag', (YLeaf(YType.uint32, 'gre-acl-flag'), ['int'])),
                            ('v4state', (YLeaf(YType.uint32, 'v4state'), ['int'])),
                            ('v6state', (YLeaf(YType.uint32, 'v6state'), ['int'])),
                            ('gre_state', (YLeaf(YType.uint32, 'gre-state'), ['int'])),
                            ('v4sessid', (YLeaf(YType.uint32, 'v4sessid'), ['int'])),
                            ('v6sessid', (YLeaf(YType.uint32, 'v6sessid'), ['int'])),
                            ('gre_sessid', (YLeaf(YType.uint32, 'gre-sessid'), ['int'])),
                            ('v4dst_type', (YLeaf(YType.uint32, 'v4dst-type'), ['int'])),
                            ('v6dst_type', (YLeaf(YType.uint32, 'v6dst-type'), ['int'])),
                            ('gredst_type', (YLeaf(YType.uint32, 'gredst-type'), ['int'])),
                            ('v4statsptr', (YLeaf(YType.uint32, 'v4statsptr'), ['int'])),
                            ('v6statsptr', (YLeaf(YType.uint32, 'v6statsptr'), ['int'])),
                            ('grev4statsptr', (YLeaf(YType.uint32, 'grev4statsptr'), ['int'])),
                            ('grev6statsptr', (YLeaf(YType.uint32, 'grev6statsptr'), ['int'])),
                            ('mplsv4stats', (YLeaf(YType.uint32, 'mplsv4stats'), ['int'])),
                            ('mplsv6pkts', (YLeaf(YType.uint32, 'mplsv6pkts'), ['int'])),
                            ('np_umask', (YLeaf(YType.uint32, 'np-umask'), ['int'])),
                            ('uidb', (YLeafList(YType.uint32, 'uidb'), ['int'])),
                            ('sft_hw_data', (YLeafList(YType.uint32, 'sft-hw-data'), ['int'])),
                        ])
                        self.intf_name = None
                        self.src_ifh = None
                        self.intf_name_xr = None
                        self.v4_acl_flag = None
                        self.v6_acl_flag = None
                        self.gre_acl_flag = None
                        self.v4state = None
                        self.v6state = None
                        self.gre_state = None
                        self.v4sessid = None
                        self.v6sessid = None
                        self.gre_sessid = None
                        self.v4dst_type = None
                        self.v6dst_type = None
                        self.gredst_type = None
                        self.v4statsptr = None
                        self.v6statsptr = None
                        self.grev4statsptr = None
                        self.grev6statsptr = None
                        self.mplsv4stats = None
                        self.mplsv6pkts = None
                        self.np_umask = None
                        self.uidb = []
                        self.sft_hw_data = []
                        self._segment_path = lambda: "span-mirr-info" + "[intf-name='" + str(self.intf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo, ['intf_name', 'src_ifh', 'intf_name_xr', 'v4_acl_flag', 'v6_acl_flag', 'gre_acl_flag', 'v4state', 'v6state', 'gre_state', 'v4sessid', 'v6sessid', 'gre_sessid', 'v4dst_type', 'v6dst_type', 'gredst_type', 'v4statsptr', 'v6statsptr', 'grev4statsptr', 'grev6statsptr', 'mplsv4stats', 'mplsv6pkts', 'np_umask', 'uidb', 'sft_hw_data'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                        return meta._meta_table['Ssespan.Nodes.Node.SpanMirrInfos.SpanMirrInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                    return meta._meta_table['Ssespan.Nodes.Node.SpanMirrInfos']['meta_info']


            class Spanudf(_Entity_):
                """
                udf info
                
                .. attribute:: udf_hdr
                
                	udf header
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: udf_type
                
                	udf type
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: udf_len
                
                	udf len
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: udf_value
                
                	udf value
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: udf_hw_data
                
                	16x5npu=80 bytes of hw udf entry
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssespan.Nodes.Node.Spanudf, self).__init__()

                    self.yang_name = "spanudf"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('udf_hdr', (YLeafList(YType.uint32, 'udf-hdr'), ['int'])),
                        ('udf_type', (YLeafList(YType.uint32, 'udf-type'), ['int'])),
                        ('udf_len', (YLeafList(YType.uint32, 'udf-len'), ['int'])),
                        ('udf_value', (YLeafList(YType.uint32, 'udf-value'), ['int'])),
                        ('udf_hw_data', (YLeafList(YType.uint32, 'udf-hw-data'), ['int'])),
                    ])
                    self.udf_hdr = []
                    self.udf_type = []
                    self.udf_len = []
                    self.udf_value = []
                    self.udf_hw_data = []
                    self._segment_path = lambda: "spanudf"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.Spanudf, ['udf_hdr', 'udf_type', 'udf_len', 'udf_value', 'udf_hw_data'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                    return meta._meta_table['Ssespan.Nodes.Node.Spanudf']['meta_info']


            class SpanSessInfos(_Entity_):
                """
                SPAN SDT entry
                
                .. attribute:: span_sess_info
                
                	Session info 
                	**type**\: list of  		 :py:class:`SpanSessInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sse_span_oper.Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sse-span-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ssespan.Nodes.Node.SpanSessInfos, self).__init__()

                    self.yang_name = "span-sess-infos"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("span-sess-info", ("span_sess_info", Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo))])
                    self._leafs = OrderedDict()

                    self.span_sess_info = YList(self)
                    self._segment_path = lambda: "span-sess-infos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ssespan.Nodes.Node.SpanSessInfos, [], name, value)


                class SpanSessInfo(_Entity_):
                    """
                    Session info 
                    
                    .. attribute:: session_id  (key)
                    
                    	Session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_class  (key)
                    
                    	Session class
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: valid
                    
                    	marks validity of entry
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	session state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: class_
                    
                    	session Class gre,ipv4,ipv6
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ifhandle
                    
                    	ifhandle of interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mode
                    
                    	Tunnel mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ip_type
                    
                    	IP type v4 or v6 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_id
                    
                    	Vrf Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: tos_bit
                    
                    	type of service
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: tos_bit_copied
                    
                    	type of service copied
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dfbit
                    
                    	DF bit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: src_ip
                    
                    	src ip v4 or v6
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dst_ip
                    
                    	dst ip v4 or v6
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sdt_hw_data
                    
                    	16x5npu=80 bytes of hw sdt entry
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sse-span-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo, self).__init__()

                        self.yang_name = "span-sess-info"
                        self.yang_parent_name = "span-sess-infos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session_id','session_class']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('session_class', (YLeaf(YType.uint32, 'session-class'), ['int'])),
                            ('valid', (YLeaf(YType.uint8, 'valid'), ['int'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('state', (YLeaf(YType.uint32, 'state'), ['int'])),
                            ('class_', (YLeaf(YType.uint32, 'class'), ['int'])),
                            ('ifhandle', (YLeaf(YType.uint32, 'ifhandle'), ['int'])),
                            ('mode', (YLeaf(YType.uint32, 'mode'), ['int'])),
                            ('ip_type', (YLeaf(YType.uint32, 'ip-type'), ['int'])),
                            ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                            ('tos_bit', (YLeaf(YType.uint32, 'tos-bit'), ['int'])),
                            ('tos_bit_copied', (YLeaf(YType.uint32, 'tos-bit-copied'), ['int'])),
                            ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                            ('dfbit', (YLeaf(YType.uint32, 'dfbit'), ['int'])),
                            ('src_ip', (YLeafList(YType.uint32, 'src-ip'), ['int'])),
                            ('dst_ip', (YLeafList(YType.uint32, 'dst-ip'), ['int'])),
                            ('sdt_hw_data', (YLeafList(YType.uint32, 'sdt-hw-data'), ['int'])),
                        ])
                        self.session_id = None
                        self.session_class = None
                        self.valid = None
                        self.id = None
                        self.state = None
                        self.class_ = None
                        self.ifhandle = None
                        self.mode = None
                        self.ip_type = None
                        self.vrf_id = None
                        self.tos_bit = None
                        self.tos_bit_copied = None
                        self.ttl = None
                        self.dfbit = None
                        self.src_ip = []
                        self.dst_ip = []
                        self.sdt_hw_data = []
                        self._segment_path = lambda: "span-sess-info" + "[session-id='" + str(self.session_id) + "']" + "[session-class='" + str(self.session_class) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo, ['session_id', 'session_class', 'valid', 'id', 'state', 'class_', 'ifhandle', 'mode', 'ip_type', 'vrf_id', 'tos_bit', 'tos_bit_copied', 'ttl', 'dfbit', 'src_ip', 'dst_ip', 'sdt_hw_data'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                        return meta._meta_table['Ssespan.Nodes.Node.SpanSessInfos.SpanSessInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                    return meta._meta_table['Ssespan.Nodes.Node.SpanSessInfos']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
                return meta._meta_table['Ssespan.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
            return meta._meta_table['Ssespan.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ssespan()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sse_span_oper as meta
        return meta._meta_table['Ssespan']['meta_info']


