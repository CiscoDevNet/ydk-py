""" Cisco_IOS_XE_mpls_fwd_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsForwardingTable(object):
    """
    Data nodes for MPLS forwarding table entries.
    
    .. attribute:: local_label_entry
    
    	The list of MPLS forwarding table entries
    	**type**\: list of    :py:class:`LocalLabelEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry>`
    
    

    """

    _prefix = 'mpls-fwd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.local_label_entry = YList()
        self.local_label_entry.parent = self
        self.local_label_entry.name = 'local_label_entry'


    class LocalLabelEntry(object):
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
            self.parent = None
            self.local_label = None
            self.forwarding_info = YList()
            self.forwarding_info.parent = self
            self.forwarding_info.name = 'forwarding_info'


        class ForwardingInfo(object):
            """
            
            
            .. attribute:: outgoing_interface  <key>
            
            	The name of the outgoing interface. Example possible values are 1.none, 2.drop, 3.<tunnel\-name>, 4.<interface\-name>, 5.aggregate/<vrf\-name> etc
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`OutgoingInterfaceEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterfaceEnum>`
            
            
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
            
            	**type**\:   :py:class:`NextHopEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHopEnum>`
            
            
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
            	**type**\:   :py:class:`OutgoingLabelEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabelEnum>`
            
            
            ----
            

            """

            _prefix = 'mpls-fwd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.outgoing_interface = None
                self.connection_info = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo()
                self.connection_info.parent = self
                self.label_switched_bytes = None
                self.next_hop = None
                self.outgoing_label = None

            class NextHopEnum(Enum):
                """
                NextHopEnum

                Next hop information.

                Example possible values are

                1.point2point,

                2.<ip\-address>

                .. data:: point2point = 0

                """

                point2point = 0


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                    return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHopEnum']


            class OutgoingInterfaceEnum(Enum):
                """
                OutgoingInterfaceEnum

                The name of the outgoing interface.

                Example possible values are 1.none, 2.drop, 3.<tunnel\-name>,

                4.<interface\-name>, 5.aggregate/<vrf\-name> etc.

                .. data:: drop = 0

                .. data:: punt = 1

                .. data:: aggregate = 2

                .. data:: exception = 3

                .. data:: none = 4

                """

                drop = 0

                punt = 1

                aggregate = 2

                exception = 3

                none = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                    return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterfaceEnum']


            class OutgoingLabelEnum(Enum):
                """
                OutgoingLabelEnum

                Value of outgoing\-label if exists or

                the type of non\-present label.

                .. data:: no_label = 0

                .. data:: pop_label = 1

                .. data:: aggregate = 2

                .. data:: explicit_null = 3

                .. data:: illegal = 4

                """

                no_label = 0

                pop_label = 1

                aggregate = 2

                explicit_null = 3

                illegal = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                    return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabelEnum']



            class ConnectionInfo(object):
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
                	**type**\:   :py:class:`TypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper.MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TypeEnum>`
                
                .. attribute:: vrf_id
                
                	
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-fwd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.l2ckt_id = None
                    self.mask = None
                    self.nh_id = None
                    self.tunnel_id = None
                    self.tunnel_tp = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp()
                    self.tunnel_tp.parent = self
                    self.type = None
                    self.vrf_id = None

                class TypeEnum(Enum):
                    """
                    TypeEnum

                    The type of connection represented by this label

                    .. data:: ip = 0

                    .. data:: tunnel = 1

                    .. data:: nh_id = 2

                    .. data:: l2ckt = 3

                    .. data:: ip_vrf = 4

                    .. data:: none = 5

                    .. data:: tunnel_tp = 6

                    """

                    ip = 0

                    tunnel = 1

                    nh_id = 2

                    l2ckt = 3

                    ip_vrf = 4

                    none = 5

                    tunnel_tp = 6


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                        return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TypeEnum']



                class TunnelTp(object):
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
                        self.parent = None
                        self.dst_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId()
                        self.dst_id.parent = self
                        self.src_id = MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId()
                        self.src_id.parent = self
                        self.tunnel = None


                    class SrcId(object):
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
                            self.parent = None
                            self.global_ = None
                            self.node = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-fwd-oper:src-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.global_ is not None:
                                return True

                            if self.node is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                            return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId']['meta_info']


                    class DstId(object):
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
                            self.parent = None
                            self.global_ = None
                            self.node = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-fwd-oper:dst-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.global_ is not None:
                                return True

                            if self.node is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                            return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-fwd-oper:tunnel-tp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dst_id is not None and self.dst_id._has_data():
                            return True

                        if self.src_id is not None and self.src_id._has_data():
                            return True

                        if self.tunnel is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                        return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-fwd-oper:connection-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.l2ckt_id is not None:
                        return True

                    if self.mask is not None:
                        return True

                    if self.nh_id is not None:
                        return True

                    if self.tunnel_id is not None:
                        return True

                    if self.tunnel_tp is not None and self.tunnel_tp._has_data():
                        return True

                    if self.type is not None:
                        return True

                    if self.vrf_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                    return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.outgoing_interface is None:
                    raise YPYModelError('Key property outgoing_interface is None')

                return self.parent._common_path +'/Cisco-IOS-XE-mpls-fwd-oper:forwarding-info[Cisco-IOS-XE-mpls-fwd-oper:outgoing-interface = ' + str(self.outgoing_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.outgoing_interface is not None:
                    return True

                if self.connection_info is not None and self.connection_info._has_data():
                    return True

                if self.label_switched_bytes is not None:
                    return True

                if self.next_hop is not None:
                    return True

                if self.outgoing_label is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
                return meta._meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo']['meta_info']

        @property
        def _common_path(self):
            if self.local_label is None:
                raise YPYModelError('Key property local_label is None')

            return '/Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table/Cisco-IOS-XE-mpls-fwd-oper:local-label-entry[Cisco-IOS-XE-mpls-fwd-oper:local-label = ' + str(self.local_label) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.local_label is not None:
                return True

            if self.forwarding_info is not None:
                for child_ref in self.forwarding_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
            return meta._meta_table['MplsForwardingTable.LocalLabelEntry']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-mpls-fwd-oper:mpls-forwarding-table'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.local_label_entry is not None:
            for child_ref in self.local_label_entry:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_fwd_oper as meta
        return meta._meta_table['MplsForwardingTable']['meta_info']


