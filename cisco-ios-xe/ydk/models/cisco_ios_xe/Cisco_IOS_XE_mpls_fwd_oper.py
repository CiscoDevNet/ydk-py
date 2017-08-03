""" Cisco_IOS_XE_mpls_fwd_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsForwardingTable(Entity):
    """
    Data nodes for MPLS forwarding table entries.
    
    .. attribute:: local_label_entry
    
    	The list of MPLS forwarding table entries
    	**type**\: list of    :py:class:`LocalLabelEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry>`
    
    

    """

    _prefix = 'mpls-fwd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(MplsForwardingTable, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-forwarding-table"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-fwd-oper"

        self.local_label_entry = YList(self)

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
                    super(MplsForwardingTable, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MplsForwardingTable, self).__setattr__(name, value)


    class LocalLabelEntry(Entity):
        """
        The list of MPLS forwarding table entries.
        
        .. attribute:: local_label  <key>
        
        	Value of local\-label
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: forwarding_info
        
        	
        	**type**\: list of    :py:class:`ForwardingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo>`
        
        

        """

        _prefix = 'mpls-fwd-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MplsForwardingTable.LocalLabelEntry, self).__init__()

            self.yang_name = "local-label-entry"
            self.yang_parent_name = "mpls-forwarding-table"

            self.local_label = YLeaf(YType.uint32, "local-label")

            self.forwarding_info = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("local_label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsForwardingTable.LocalLabelEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsForwardingTable.LocalLabelEntry, self).__setattr__(name, value)


        class ForwardingInfo(Entity):
            """
            
            
            .. attribute:: outgoing_interface  <key>
            
            	The name of the outgoing interface. Example possible values are 1.none, 2.drop, 3.<tunnel\-name>, 4.<interface\-name>, 5.aggregate/<vrf\-name> etc
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`OutgoingInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterface>`
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: connection_info
            
            	The Prefix or tunnel\-id info corresponding to this label. Ex\: 1) for l2ckt, a number tunnel\-id value. 2) for ipv4, a prefix with [V] tag (113.113.113.113/32[V]). 3) for TE, a pefix with [T] tag (113.113.113.113/32[T])
            	**type**\:   :py:class:`ConnectionInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo>`
            
            .. attribute:: label_switched_bytes
            
            	The number of bytes switched using this label
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: next_hop
            
            	Next hop information. Example possible values are 1.point2point, 2.<ip\-address>
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHop>`
            
            
            ----
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            
            ----
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            
            ----
            .. attribute:: outgoing_label
            
            	Value of outgoing\-label if exists or the type of non\-present label
            	**type**\: one of the below types:
            
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            
            ----
            	**type**\:   :py:class:`OutgoingLabel <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabel>`
            
            
            ----
            

            """

            _prefix = 'mpls-fwd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo, self).__init__()

                self.yang_name = "forwarding-info"
                self.yang_parent_name = "local-label-entry"

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.label_switched_bytes = YLeaf(YType.uint64, "label-switched-bytes")

                self.next_hop = YLeaf(YType.str, "next-hop")

                self.outgoing_label = YLeaf(YType.str, "outgoing-label")

                self.connection_info = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo()
                self.connection_info.parent = self
                self._children_name_map["connection_info"] = "connection-info"
                self._children_yang_names.add("connection-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("outgoing_interface",
                                "label_switched_bytes",
                                "next_hop",
                                "outgoing_label") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo, self).__setattr__(name, value)

            class NextHop(Enum):
                """
                NextHop

                Next hop information.

                Example possible values are

                1.point2point,

                2.<ip\-address>

                .. data:: point2point = 0

                """

                point2point = Enum.YLeaf(0, "point2point")


            class OutgoingInterface(Enum):
                """
                OutgoingInterface

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
                OutgoingLabel

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
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: l2ckt_id
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mask
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: nh_id
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_id
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_tp
                
                	
                	**type**\:   :py:class:`TunnelTp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp>`
                
                .. attribute:: type
                
                	The type of connection represented by this label
                	**type**\:   :py:class:`Type <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.Type>`
                
                .. attribute:: vrf_id
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-fwd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo, self).__init__()

                    self.yang_name = "connection-info"
                    self.yang_parent_name = "forwarding-info"

                    self.ip = YLeaf(YType.str, "ip")

                    self.l2ckt_id = YLeaf(YType.uint32, "l2ckt-id")

                    self.mask = YLeaf(YType.uint16, "mask")

                    self.nh_id = YLeaf(YType.uint32, "nh-id")

                    self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                    self.tunnel_tp = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp()
                    self.tunnel_tp.parent = self
                    self._children_name_map["tunnel_tp"] = "tunnel-tp"
                    self._children_yang_names.add("tunnel-tp")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "l2ckt_id",
                                    "mask",
                                    "nh_id",
                                    "tunnel_id",
                                    "type",
                                    "vrf_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo, self).__setattr__(name, value)

                class Type(Enum):
                    """
                    Type

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
                    
                    
                    .. attribute:: dst_id
                    
                    	
                    	**type**\:   :py:class:`DstId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId>`
                    
                    .. attribute:: src_id
                    
                    	
                    	**type**\:   :py:class:`SrcId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId>`
                    
                    .. attribute:: tunnel
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-fwd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp, self).__init__()

                        self.yang_name = "tunnel-tp"
                        self.yang_parent_name = "connection-info"

                        self.tunnel = YLeaf(YType.uint32, "tunnel")

                        self.dst_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId()
                        self.dst_id.parent = self
                        self._children_name_map["dst_id"] = "dst-id"
                        self._children_yang_names.add("dst-id")

                        self.src_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId()
                        self.src_id.parent = self
                        self._children_name_map["src_id"] = "src-id"
                        self._children_yang_names.add("src-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tunnel") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp, self).__setattr__(name, value)


                    class SrcId(Entity):
                        """
                        
                        
                        .. attribute:: global_
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node
                        
                        	
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls-fwd-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId, self).__init__()

                            self.yang_name = "src-id"
                            self.yang_parent_name = "tunnel-tp"

                            self.global_ = YLeaf(YType.uint32, "global")

                            self.node = YLeaf(YType.str, "node")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("global_",
                                            "node") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.global_.is_set or
                                self.node.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.global_.yfilter != YFilter.not_set or
                                self.node.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "src-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.global_.is_set or self.global_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.global_.get_name_leafdata())
                            if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.node.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "global" or name == "node"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "global"):
                                self.global_ = value
                                self.global_.value_namespace = name_space
                                self.global_.value_namespace_prefix = name_space_prefix
                            if(value_path == "node"):
                                self.node = value
                                self.node.value_namespace = name_space
                                self.node.value_namespace_prefix = name_space_prefix


                    class DstId(Entity):
                        """
                        
                        
                        .. attribute:: global_
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: node
                        
                        	
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls-fwd-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId, self).__init__()

                            self.yang_name = "dst-id"
                            self.yang_parent_name = "tunnel-tp"

                            self.global_ = YLeaf(YType.uint32, "global")

                            self.node = YLeaf(YType.str, "node")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("global_",
                                            "node") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.global_.is_set or
                                self.node.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.global_.yfilter != YFilter.not_set or
                                self.node.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dst-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.global_.is_set or self.global_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.global_.get_name_leafdata())
                            if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.node.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "global" or name == "node"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "global"):
                                self.global_ = value
                                self.global_.value_namespace = name_space
                                self.global_.value_namespace_prefix = name_space_prefix
                            if(value_path == "node"):
                                self.node = value
                                self.node.value_namespace = name_space
                                self.node.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.tunnel.is_set or
                            (self.dst_id is not None and self.dst_id.has_data()) or
                            (self.src_id is not None and self.src_id.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tunnel.yfilter != YFilter.not_set or
                            (self.dst_id is not None and self.dst_id.has_operation()) or
                            (self.src_id is not None and self.src_id.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tunnel-tp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.tunnel.is_set or self.tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tunnel.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dst-id"):
                            if (self.dst_id is None):
                                self.dst_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId()
                                self.dst_id.parent = self
                                self._children_name_map["dst_id"] = "dst-id"
                            return self.dst_id

                        if (child_yang_name == "src-id"):
                            if (self.src_id is None):
                                self.src_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId()
                                self.src_id.parent = self
                                self._children_name_map["src_id"] = "src-id"
                            return self.src_id

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dst-id" or name == "src-id" or name == "tunnel"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tunnel"):
                            self.tunnel = value
                            self.tunnel.value_namespace = name_space
                            self.tunnel.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.l2ckt_id.is_set or
                        self.mask.is_set or
                        self.nh_id.is_set or
                        self.tunnel_id.is_set or
                        self.type.is_set or
                        self.vrf_id.is_set or
                        (self.tunnel_tp is not None and self.tunnel_tp.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.l2ckt_id.yfilter != YFilter.not_set or
                        self.mask.yfilter != YFilter.not_set or
                        self.nh_id.yfilter != YFilter.not_set or
                        self.tunnel_id.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        self.vrf_id.yfilter != YFilter.not_set or
                        (self.tunnel_tp is not None and self.tunnel_tp.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "connection-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.l2ckt_id.is_set or self.l2ckt_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.l2ckt_id.get_name_leafdata())
                    if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mask.get_name_leafdata())
                    if (self.nh_id.is_set or self.nh_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nh_id.get_name_leafdata())
                    if (self.tunnel_id.is_set or self.tunnel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tunnel_id.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())
                    if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "tunnel-tp"):
                        if (self.tunnel_tp is None):
                            self.tunnel_tp = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp()
                            self.tunnel_tp.parent = self
                            self._children_name_map["tunnel_tp"] = "tunnel-tp"
                        return self.tunnel_tp

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tunnel-tp" or name == "ip" or name == "l2ckt-id" or name == "mask" or name == "nh-id" or name == "tunnel-id" or name == "type" or name == "vrf-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "l2ckt-id"):
                        self.l2ckt_id = value
                        self.l2ckt_id.value_namespace = name_space
                        self.l2ckt_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "mask"):
                        self.mask = value
                        self.mask.value_namespace = name_space
                        self.mask.value_namespace_prefix = name_space_prefix
                    if(value_path == "nh-id"):
                        self.nh_id = value
                        self.nh_id.value_namespace = name_space
                        self.nh_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tunnel-id"):
                        self.tunnel_id = value
                        self.tunnel_id.value_namespace = name_space
                        self.tunnel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-id"):
                        self.vrf_id = value
                        self.vrf_id.value_namespace = name_space
                        self.vrf_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.outgoing_interface.is_set or
                    self.label_switched_bytes.is_set or
                    self.next_hop.is_set or
                    self.outgoing_label.is_set or
                    (self.connection_info is not None and self.connection_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.outgoing_interface.yfilter != YFilter.not_set or
                    self.label_switched_bytes.yfilter != YFilter.not_set or
                    self.next_hop.yfilter != YFilter.not_set or
                    self.outgoing_label.yfilter != YFilter.not_set or
                    (self.connection_info is not None and self.connection_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "forwarding-info" + "[outgoing-interface='" + self.outgoing_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.outgoing_interface.is_set or self.outgoing_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_interface.get_name_leafdata())
                if (self.label_switched_bytes.is_set or self.label_switched_bytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label_switched_bytes.get_name_leafdata())
                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                if (self.outgoing_label.is_set or self.outgoing_label.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_label.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "connection-info"):
                    if (self.connection_info is None):
                        self.connection_info = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo()
                        self.connection_info.parent = self
                        self._children_name_map["connection_info"] = "connection-info"
                    return self.connection_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "connection-info" or name == "outgoing-interface" or name == "label-switched-bytes" or name == "next-hop" or name == "outgoing-label"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "outgoing-interface"):
                    self.outgoing_interface = value
                    self.outgoing_interface.value_namespace = name_space
                    self.outgoing_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "label-switched-bytes"):
                    self.label_switched_bytes = value
                    self.label_switched_bytes.value_namespace = name_space
                    self.label_switched_bytes.value_namespace_prefix = name_space_prefix
                if(value_path == "next-hop"):
                    self.next_hop = value
                    self.next_hop.value_namespace = name_space
                    self.next_hop.value_namespace_prefix = name_space_prefix
                if(value_path == "outgoing-label"):
                    self.outgoing_label = value
                    self.outgoing_label.value_namespace = name_space
                    self.outgoing_label.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.forwarding_info:
                if (c.has_data()):
                    return True
            return self.local_label.is_set

        def has_operation(self):
            for c in self.forwarding_info:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.local_label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "local-label-entry" + "[local-label='" + self.local_label.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.local_label.is_set or self.local_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.local_label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "forwarding-info"):
                for c in self.forwarding_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsForwardingTable.LocalLabelEntry.ForwardingInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.forwarding_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "forwarding-info" or name == "local-label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "local-label"):
                self.local_label = value
                self.local_label.value_namespace = name_space
                self.local_label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.local_label_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.local_label_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table" + path_buffer

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

        if (child_yang_name == "local-label-entry"):
            for c in self.local_label_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MplsForwardingTable.LocalLabelEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.local_label_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "local-label-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsForwardingTable()
        return self._top_entity

