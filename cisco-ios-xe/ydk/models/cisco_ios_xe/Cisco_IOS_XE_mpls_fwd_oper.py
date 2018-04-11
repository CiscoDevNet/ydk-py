""" Cisco_IOS_XE_mpls_fwd_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsForwardingTable(Entity):
    """
    Data nodes for MPLS forwarding table entries.
    
    .. attribute:: local_label_entry
    
    	The list of MPLS forwarding table entries
    	**type**\: list of  		 :py:class:`LocalLabelEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry>`
    
    

    """

    _prefix = 'mpls-fwd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(MplsForwardingTable, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-forwarding-table"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-fwd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("local-label-entry", ("local_label_entry", MplsForwardingTable.LocalLabelEntry))])
        self._leafs = OrderedDict()

        self.local_label_entry = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table"

    def __setattr__(self, name, value):
        self._perform_setattr(MplsForwardingTable, [], name, value)


    class LocalLabelEntry(Entity):
        """
        The list of MPLS forwarding table entries.
        
        .. attribute:: local_label  (key)
        
        	Value of local\-label
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: forwarding_info
        
        	
        	**type**\: list of  		 :py:class:`ForwardingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo>`
        
        

        """

        _prefix = 'mpls-fwd-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MplsForwardingTable.LocalLabelEntry, self).__init__()

            self.yang_name = "local-label-entry"
            self.yang_parent_name = "mpls-forwarding-table"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['local_label']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("forwarding-info", ("forwarding_info", MplsForwardingTable.LocalLabelEntry.ForwardingInfo))])
            self._leafs = OrderedDict([
                ('local_label', YLeaf(YType.uint32, 'local-label')),
            ])
            self.local_label = None

            self.forwarding_info = YList(self)
            self._segment_path = lambda: "local-label-entry" + "[local-label='" + str(self.local_label) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsForwardingTable.LocalLabelEntry, ['local_label'], name, value)


        class ForwardingInfo(Entity):
            """
            
            
            .. attribute:: outgoing_interface  (key)
            
            	The name of the outgoing interface. Example possible values are 1.none, 2.drop, 3.<tunnel\-name>, 4.<interface\-name>, 5.aggregate/<vrf\-name> etc
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`OutgoingInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterface>`
            
            		**type**\: str
            
            .. attribute:: outgoing_label
            
            	Value of outgoing\-label if exists or the type of non\-present label
            	**type**\: union of the below types:
            
            		**type**\: int
            
            			**range:** 0..4294967295
            
            		**type**\:  :py:class:`OutgoingLabel <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabel>`
            
            .. attribute:: connection_info
            
            	The Prefix or tunnel\-id info corresponding to this label. Ex\: 1) for l2ckt, a number tunnel\-id value. 2) for ipv4, a prefix with [V] tag (113.113.113.113/32[V]). 3) for TE, a pefix with [T] tag (113.113.113.113/32[T])
            	**type**\:  :py:class:`ConnectionInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo>`
            
            .. attribute:: label_switched_bytes
            
            	The number of bytes switched using this label
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: next_hop
            
            	Next hop information. Example possible values are 1.point2point, 2.<ip\-address>
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHop>`
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'mpls-fwd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo, self).__init__()

                self.yang_name = "forwarding-info"
                self.yang_parent_name = "local-label-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['outgoing_interface']
                self._child_container_classes = OrderedDict([("connection-info", ("connection_info", MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('outgoing_interface', YLeaf(YType.str, 'outgoing-interface')),
                    ('outgoing_label', YLeaf(YType.str, 'outgoing-label')),
                    ('label_switched_bytes', YLeaf(YType.uint64, 'label-switched-bytes')),
                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                ])
                self.outgoing_interface = None
                self.outgoing_label = None
                self.label_switched_bytes = None
                self.next_hop = None

                self.connection_info = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo()
                self.connection_info.parent = self
                self._children_name_map["connection_info"] = "connection-info"
                self._children_yang_names.add("connection-info")
                self._segment_path = lambda: "forwarding-info" + "[outgoing-interface='" + str(self.outgoing_interface) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MplsForwardingTable.LocalLabelEntry.ForwardingInfo, ['outgoing_interface', 'outgoing_label', 'label_switched_bytes', 'next_hop'], name, value)

            class NextHop(Enum):
                """
                NextHop (Enum Class)

                Next hop information.

                Example possible values are

                1.point2point,

                2.<ip\-address>

                .. data:: point2point = 0

                """

                point2point = Enum.YLeaf(0, "point2point")


            class OutgoingInterface(Enum):
                """
                OutgoingInterface (Enum Class)

                The name of the outgoing interface.

                Example possible values are 1.none, 2.drop, 3.<tunnel\-name>,

                4.<interface\-name>, 5.aggregate/<vrf\-name> etc.

                .. data:: drop = 0

                .. data:: punt = 1

                .. data:: aggregate = 2

                .. data:: exception = 3

                .. data:: none = 4

                """

                drop = Enum.YLeaf(0, "drop")

                punt = Enum.YLeaf(1, "punt")

                aggregate = Enum.YLeaf(2, "aggregate")

                exception = Enum.YLeaf(3, "exception")

                none = Enum.YLeaf(4, "none")


            class OutgoingLabel(Enum):
                """
                OutgoingLabel (Enum Class)

                Value of outgoing\-label if exists or

                the type of non\-present label.

                .. data:: no_label = 0

                .. data:: pop_label = 1

                .. data:: aggregate = 2

                .. data:: explicit_null = 3

                .. data:: illegal = 4

                """

                no_label = Enum.YLeaf(0, "no-label")

                pop_label = Enum.YLeaf(1, "pop-label")

                aggregate = Enum.YLeaf(2, "aggregate")

                explicit_null = Enum.YLeaf(3, "explicit-null")

                illegal = Enum.YLeaf(4, "illegal")



            class ConnectionInfo(Entity):
                """
                The Prefix or tunnel\-id info corresponding to this label.
                Ex\: 1) for l2ckt, a number tunnel\-id value.
                2) for ipv4, a prefix with [V] tag (113.113.113.113/32[V]).
                3) for TE, a pefix with [T] tag (113.113.113.113/32[T])
                
                .. attribute:: type
                
                	The type of connection represented by this label
                	**type**\:  :py:class:`Type <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.Type>`
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mask
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: tunnel_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nh_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: l2ckt_id
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_tp
                
                	
                	**type**\:  :py:class:`TunnelTp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp>`
                
                

                """

                _prefix = 'mpls-fwd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo, self).__init__()

                    self.yang_name = "connection-info"
                    self.yang_parent_name = "forwarding-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("tunnel-tp", ("tunnel_tp", MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('mask', YLeaf(YType.uint16, 'mask')),
                        ('tunnel_id', YLeaf(YType.uint32, 'tunnel-id')),
                        ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                        ('nh_id', YLeaf(YType.uint32, 'nh-id')),
                        ('l2ckt_id', YLeaf(YType.uint32, 'l2ckt-id')),
                    ])
                    self.type = None
                    self.ip = None
                    self.mask = None
                    self.tunnel_id = None
                    self.vrf_id = None
                    self.nh_id = None
                    self.l2ckt_id = None

                    self.tunnel_tp = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp()
                    self.tunnel_tp.parent = self
                    self._children_name_map["tunnel_tp"] = "tunnel-tp"
                    self._children_yang_names.add("tunnel-tp")
                    self._segment_path = lambda: "connection-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo, ['type', 'ip', 'mask', 'tunnel_id', 'vrf_id', 'nh_id', 'l2ckt_id'], name, value)

                class Type(Enum):
                    """
                    Type (Enum Class)

                    The type of connection represented by this label

                    .. data:: ip = 0

                    .. data:: tunnel = 1

                    .. data:: nh_id = 2

                    .. data:: l2ckt = 3

                    .. data:: ip_vrf = 4

                    .. data:: none = 5

                    .. data:: tunnel_tp = 6

                    """

                    ip = Enum.YLeaf(0, "ip")

                    tunnel = Enum.YLeaf(1, "tunnel")

                    nh_id = Enum.YLeaf(2, "nh-id")

                    l2ckt = Enum.YLeaf(3, "l2ckt")

                    ip_vrf = Enum.YLeaf(4, "ip-vrf")

                    none = Enum.YLeaf(5, "none")

                    tunnel_tp = Enum.YLeaf(6, "tunnel-tp")



                class TunnelTp(Entity):
                    """
                    
                    
                    .. attribute:: tunnel
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src_id
                    
                    	
                    	**type**\:  :py:class:`SrcId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId>`
                    
                    .. attribute:: dst_id
                    
                    	
                    	**type**\:  :py:class:`DstId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId>`
                    
                    

                    """

                    _prefix = 'mpls-fwd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp, self).__init__()

                        self.yang_name = "tunnel-tp"
                        self.yang_parent_name = "connection-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("src-id", ("src_id", MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId)), ("dst-id", ("dst_id", MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tunnel', YLeaf(YType.uint32, 'tunnel')),
                        ])
                        self.tunnel = None

                        self.src_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId()
                        self.src_id.parent = self
                        self._children_name_map["src_id"] = "src-id"
                        self._children_yang_names.add("src-id")

                        self.dst_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId()
                        self.dst_id.parent = self
                        self._children_name_map["dst_id"] = "dst-id"
                        self._children_yang_names.add("dst-id")
                        self._segment_path = lambda: "tunnel-tp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp, ['tunnel'], name, value)


                    class SrcId(Entity):
                        """
                        
                        
                        .. attribute:: global_
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-fwd-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId, self).__init__()

                            self.yang_name = "src-id"
                            self.yang_parent_name = "tunnel-tp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('global_', YLeaf(YType.uint32, 'global')),
                                ('node', YLeaf(YType.str, 'node')),
                            ])
                            self.global_ = None
                            self.node = None
                            self._segment_path = lambda: "src-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId, ['global_', 'node'], name, value)


                    class DstId(Entity):
                        """
                        
                        
                        .. attribute:: global_
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node
                        
                        	
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-fwd-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId, self).__init__()

                            self.yang_name = "dst-id"
                            self.yang_parent_name = "tunnel-tp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('global_', YLeaf(YType.uint32, 'global')),
                                ('node', YLeaf(YType.str, 'node')),
                            ])
                            self.global_ = None
                            self.node = None
                            self._segment_path = lambda: "dst-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId, ['global_', 'node'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsForwardingTable()
        return self._top_entity

