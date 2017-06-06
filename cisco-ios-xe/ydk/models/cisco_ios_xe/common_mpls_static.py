""" common_mpls_static 

YANG module describing configuration and
operational data relating to MPLS Static.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class HoptypeEnum(Enum):
    """
    HoptypeEnum

    The Nexthop type

    .. data:: PRIMARY = 0

    	Primary next hop

    .. data:: BACKUP = 1

    	Backup next hop

    """

    PRIMARY = 0

    BACKUP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['HoptypeEnum']



class NexthopResolutionTypeIdentity(object):
    """
    The Routing Protocol from which the nexthop is resolved
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['NexthopResolutionTypeIdentity']['meta_info']


class LspTypeIdentity(object):
    """
    The type of Label Switched Path
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['LspTypeIdentity']['meta_info']


class MplsStatic(object):
    """
    MPLS Static module
    
    .. attribute:: mpls_static_cfg
    
    	MPLS Static configuration commands
    	**type**\:   :py:class:`MplsStaticCfg <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg>`
    
    .. attribute:: mpls_static_state
    
    	MPLS static operational data
    	**type**\:   :py:class:`MplsStaticState <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState>`
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        self.mpls_static_cfg = MplsStatic.MplsStaticCfg()
        self.mpls_static_cfg.parent = self
        self.mpls_static_state = MplsStatic.MplsStaticState()
        self.mpls_static_state.parent = self


    class MplsStaticCfg(object):
        """
        MPLS Static configuration commands
        
        .. attribute:: in_label_lsps
        
        	The LSPs indexed by in\-label
        	**type**\:   :py:class:`InLabelLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps>`
        
        .. attribute:: interfaces
        
        	The list of interfaces configured with mpls
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces>`
        
        .. attribute:: ipv4_ingress_lsps
        
        	The LSPs indexed by ipv4 prefix
        	**type**\:   :py:class:`Ipv4IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps>`
        
        .. attribute:: ipv6_ingress_lsps
        
        	The LSPs indexed by ipv6 prefix
        	**type**\:   :py:class:`Ipv6IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps>`
        
        .. attribute:: named_lsps
        
        	The LSPs indexed by name
        	**type**\:   :py:class:`NamedLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps>`
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            self.parent = None
            self.in_label_lsps = MplsStatic.MplsStaticCfg.InLabelLsps()
            self.in_label_lsps.parent = self
            self.interfaces = MplsStatic.MplsStaticCfg.Interfaces()
            self.interfaces.parent = self
            self.ipv4_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv4IngressLsps()
            self.ipv4_ingress_lsps.parent = self
            self.ipv6_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv6IngressLsps()
            self.ipv6_ingress_lsps.parent = self
            self.named_lsps = MplsStatic.MplsStaticCfg.NamedLsps()
            self.named_lsps.parent = self


        class InLabelLsps(object):
            """
            The LSPs indexed by in\-label
            
            .. attribute:: in_label_lsp
            
            	Non\-ingress MPLS Static LSPs, keyed on the incoming label
            	**type**\: list of    :py:class:`InLabelLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.in_label_lsp = YList()
                self.in_label_lsp.parent = self
                self.in_label_lsp.name = 'in_label_lsp'


            class InLabelLsp(object):
                """
                Non\-ingress MPLS Static LSPs,
                keyed on the incoming label
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: in_label  <key>
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                
                
                ----
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.in_label = None
                    self.path = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path()
                    self.path.parent = self


                class Path(object):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.auto_protect = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations()
                        self.operations.parent = self


                    class Operations(object):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.pop_and_forward = None
                            self.preserve = None
                            self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push()
                            self.push.parent = self
                            self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap()
                            self.swap.parent = self


                        class Swap(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:swap'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap']['meta_info']


                        class Push(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:push'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:operations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.pop_and_forward is not None:
                                return True

                            if self.preserve is not None:
                                return True

                            if self.push is not None and self.push._has_data():
                                return True

                            if self.swap is not None and self.swap._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations']['meta_info']


                    class NextHop(object):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`HoptypeEnum <ydk.models.cisco_ios_xe.common_mpls_static.HoptypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.next_hop_type = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self.protected_by = None
                            self.type = None


                        class NextHopType(object):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:next-hop-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.if_index is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.out_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType']['meta_info']


                        class Operations(object):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.pop_and_forward = None
                                self.preserve = None
                                self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self


                            class Swap(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:swap'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap']['meta_info']


                            class Push(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:push'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:operations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pop_and_forward is not None:
                                    return True

                                if self.preserve is not None:
                                    return True

                                if self.push is not None and self.push._has_data():
                                    return True

                                if self.swap is not None and self.swap._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/common-mpls-static:next-hop[common-mpls-static:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.next_hop_type is not None and self.next_hop_type._has_data():
                                return True

                            if self.operations is not None and self.operations._has_data():
                                return True

                            if self.protected_by is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.auto_protect is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.operations is not None and self.operations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.in_label is None:
                        raise YPYModelError('Key property in_label is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:in-label-lsps/common-mpls-static:in-label-lsp[common-mpls-static:vrf-name = ' + str(self.vrf_name) + '][common-mpls-static:in-label = ' + str(self.in_label) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.in_label is not None:
                        return True

                    if self.path is not None and self.path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:in-label-lsps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.in_label_lsp is not None:
                    for child_ref in self.in_label_lsp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticCfg.InLabelLsps']['meta_info']


        class Ipv6IngressLsps(object):
            """
            The LSPs indexed by ipv6 prefix
            
            .. attribute:: ipv6_ingress_lsp
            
            	MPLS Static IPv6 Label Switched Path Configuration at Ingress
            	**type**\: list of    :py:class:`Ipv6IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.ipv6_ingress_lsp = YList()
                self.ipv6_ingress_lsp.parent = self
                self.ipv6_ingress_lsp.name = 'ipv6_ingress_lsp'


            class Ipv6IngressLsp(object):
                """
                MPLS Static IPv6 Label Switched Path
                Configuration at Ingress
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IPv6 prefix of packets that will ingress on this LSP
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                
                
                ----
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.prefix = None
                    self.in_label = None
                    self.name = None
                    self.path = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path()
                    self.path.parent = self


                class Path(object):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.auto_protect = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations()
                        self.operations.parent = self


                    class Operations(object):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.pop_and_forward = None
                            self.preserve = None
                            self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self


                        class Swap(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:swap'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap']['meta_info']


                        class Push(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:push'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:operations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.pop_and_forward is not None:
                                return True

                            if self.preserve is not None:
                                return True

                            if self.push is not None and self.push._has_data():
                                return True

                            if self.swap is not None and self.swap._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations']['meta_info']


                    class NextHop(object):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`HoptypeEnum <ydk.models.cisco_ios_xe.common_mpls_static.HoptypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self.protected_by = None
                            self.type = None


                        class NextHopType(object):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:next-hop-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.if_index is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.out_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType']['meta_info']


                        class Operations(object):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.pop_and_forward = None
                                self.preserve = None
                                self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self


                            class Swap(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:swap'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap']['meta_info']


                            class Push(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:push'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:operations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pop_and_forward is not None:
                                    return True

                                if self.preserve is not None:
                                    return True

                                if self.push is not None and self.push._has_data():
                                    return True

                                if self.swap is not None and self.swap._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/common-mpls-static:next-hop[common-mpls-static:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.next_hop_type is not None and self.next_hop_type._has_data():
                                return True

                            if self.operations is not None and self.operations._has_data():
                                return True

                            if self.protected_by is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.auto_protect is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.operations is not None and self.operations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.prefix is None:
                        raise YPYModelError('Key property prefix is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:ipv6-ingress-lsps/common-mpls-static:ipv6-ingress-lsp[common-mpls-static:vrf-name = ' + str(self.vrf_name) + '][common-mpls-static:prefix = ' + str(self.prefix) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.in_label is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.path is not None and self.path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:ipv6-ingress-lsps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv6_ingress_lsp is not None:
                    for child_ref in self.ipv6_ingress_lsp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps']['meta_info']


        class NamedLsps(object):
            """
            The LSPs indexed by name
            
            .. attribute:: named_lsp
            
            	MPLS Static Label Switched Path Configuration. The LSPs in this list are referenced by a string name. The LSPs may be ingress/egress/crossconnect, may have v4/v6 prefixes and may be associated with any VRF. The other specialized lists above are for implemetations that are keyed on prefixes or in\-labels instead of the LSP name
            	**type**\: list of    :py:class:`NamedLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.named_lsp = YList()
                self.named_lsp.parent = self
                self.named_lsp.name = 'named_lsp'


            class NamedLsp(object):
                """
                MPLS Static Label Switched Path Configuration.
                The LSPs in this list are referenced by a string name.
                The LSPs may be ingress/egress/crossconnect,
                may have v4/v6 prefixes and may be associated with any
                VRF. The other specialized lists above are for
                implemetations that are keyed on prefixes or in\-labels
                instead of the LSP name.
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: name  <key>
                
                	Name of the LSP
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: in_label
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                
                
                ----
                .. attribute:: ipv4_prefix
                
                	ipv4 prefix
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: ipv6_prefix
                
                	ipv6 prefix
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: lsp_type
                
                	lsp type
                	**type**\:   :py:class:`LspTypeIdentity <ydk.models.cisco_ios_xe.common_mpls_static.LspTypeIdentity>`
                
                	**mandatory**\: True
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.name = None
                    self.in_label = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None
                    self.lsp_type = None
                    self.path = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path()
                    self.path.parent = self


                class Path(object):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.auto_protect = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations()
                        self.operations.parent = self


                    class Operations(object):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.pop_and_forward = None
                            self.preserve = None
                            self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push()
                            self.push.parent = self
                            self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap()
                            self.swap.parent = self


                        class Swap(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:swap'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap']['meta_info']


                        class Push(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:push'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:operations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.pop_and_forward is not None:
                                return True

                            if self.preserve is not None:
                                return True

                            if self.push is not None and self.push._has_data():
                                return True

                            if self.swap is not None and self.swap._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations']['meta_info']


                    class NextHop(object):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`HoptypeEnum <ydk.models.cisco_ios_xe.common_mpls_static.HoptypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.next_hop_type = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self.protected_by = None
                            self.type = None


                        class NextHopType(object):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:next-hop-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.if_index is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.out_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType']['meta_info']


                        class Operations(object):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.pop_and_forward = None
                                self.preserve = None
                                self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self


                            class Swap(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:swap'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap']['meta_info']


                            class Push(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:push'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:operations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pop_and_forward is not None:
                                    return True

                                if self.preserve is not None:
                                    return True

                                if self.push is not None and self.push._has_data():
                                    return True

                                if self.swap is not None and self.swap._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/common-mpls-static:next-hop[common-mpls-static:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.next_hop_type is not None and self.next_hop_type._has_data():
                                return True

                            if self.operations is not None and self.operations._has_data():
                                return True

                            if self.protected_by is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.auto_protect is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.operations is not None and self.operations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:named-lsps/common-mpls-static:named-lsp[common-mpls-static:vrf-name = ' + str(self.vrf_name) + '][common-mpls-static:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.in_label is not None:
                        return True

                    if self.ipv4_prefix is not None:
                        return True

                    if self.ipv6_prefix is not None:
                        return True

                    if self.lsp_type is not None:
                        return True

                    if self.path is not None and self.path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:named-lsps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.named_lsp is not None:
                    for child_ref in self.named_lsp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticCfg.NamedLsps']['meta_info']


        class Interfaces(object):
            """
            The list of interfaces configured with mpls
            
            .. attribute:: interface
            
            	List of interfaces that can be enabled under mpls static
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces.Interface>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                List of interfaces that can be enabled under
                mpls static
                
                .. attribute:: name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                	**mandatory**\: True
                
                .. attribute:: enabled
                
                	Interface Enabled boolean
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.enabled = None

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:interfaces/common-mpls-static:interface[common-mpls-static:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.enabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticCfg.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticCfg.Interfaces']['meta_info']


        class Ipv4IngressLsps(object):
            """
            The LSPs indexed by ipv4 prefix
            
            .. attribute:: ipv4_ingress_lsp
            
            	MPLS Static IPv4 Label Switched Path Configuration at Ingress
            	**type**\: list of    :py:class:`Ipv4IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.ipv4_ingress_lsp = YList()
                self.ipv4_ingress_lsp.parent = self
                self.ipv4_ingress_lsp.name = 'ipv4_ingress_lsp'


            class Ipv4IngressLsp(object):
                """
                MPLS Static IPv4 Label Switched
                Path Configuration at Ingress
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IPv4 prefix of packets that will ingress on this LSP
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                
                
                ----
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.prefix = None
                    self.in_label = None
                    self.name = None
                    self.path = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path()
                    self.path.parent = self


                class Path(object):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.auto_protect = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations()
                        self.operations.parent = self


                    class Operations(object):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.pop_and_forward = None
                            self.preserve = None
                            self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self


                        class Swap(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:swap'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap']['meta_info']


                        class Push(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:push'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:operations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.pop_and_forward is not None:
                                return True

                            if self.preserve is not None:
                                return True

                            if self.push is not None and self.push._has_data():
                                return True

                            if self.swap is not None and self.swap._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations']['meta_info']


                    class NextHop(object):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`HoptypeEnum <ydk.models.cisco_ios_xe.common_mpls_static.HoptypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self.protected_by = None
                            self.type = None


                        class NextHopType(object):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:next-hop-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.if_index is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.out_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType']['meta_info']


                        class Operations(object):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.pop_and_forward = None
                                self.preserve = None
                                self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self


                            class Swap(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:swap'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap']['meta_info']


                            class Push(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:push'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:operations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pop_and_forward is not None:
                                    return True

                                if self.preserve is not None:
                                    return True

                                if self.push is not None and self.push._has_data():
                                    return True

                                if self.swap is not None and self.swap._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/common-mpls-static:next-hop[common-mpls-static:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.next_hop_type is not None and self.next_hop_type._has_data():
                                return True

                            if self.operations is not None and self.operations._has_data():
                                return True

                            if self.protected_by is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.auto_protect is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.operations is not None and self.operations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.prefix is None:
                        raise YPYModelError('Key property prefix is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:ipv4-ingress-lsps/common-mpls-static:ipv4-ingress-lsp[common-mpls-static:vrf-name = ' + str(self.vrf_name) + '][common-mpls-static:prefix = ' + str(self.prefix) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.in_label is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.path is not None and self.path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg/common-mpls-static:ipv4-ingress-lsps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4_ingress_lsp is not None:
                    for child_ref in self.ipv4_ingress_lsp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps']['meta_info']

        @property
        def _common_path(self):

            return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-cfg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.in_label_lsps is not None and self.in_label_lsps._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.ipv4_ingress_lsps is not None and self.ipv4_ingress_lsps._has_data():
                return True

            if self.ipv6_ingress_lsps is not None and self.ipv6_ingress_lsps._has_data():
                return True

            if self.named_lsps is not None and self.named_lsps._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
            return meta._meta_table['MplsStatic.MplsStaticCfg']['meta_info']


    class MplsStaticState(object):
        """
        MPLS static operational data
        
        .. attribute:: label_switched_paths
        
        	MPLS Static Label Switched Paths
        	**type**\:   :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths>`
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            self.parent = None
            self.label_switched_paths = MplsStatic.MplsStaticState.LabelSwitchedPaths()
            self.label_switched_paths.parent = self


        class LabelSwitchedPaths(object):
            """
            MPLS Static Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	MPLS LSPs list
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                self.parent = None
                self.label_switched_path = YList()
                self.label_switched_path.parent = self
                self.label_switched_path.name = 'label_switched_path'


            class LabelSwitchedPath(object):
                """
                MPLS LSPs list
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IP v4/v6 prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: egress_stats
                
                	egress stats
                	**type**\:   :py:class:`EgressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats>`
                
                .. attribute:: in_label_value
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                
                
                ----
                .. attribute:: ingress_stats
                
                	ingress stats
                	**type**\:   :py:class:`IngressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats>`
                
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.prefix = None
                    self.egress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats()
                    self.egress_stats.parent = self
                    self.in_label_value = None
                    self.ingress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats()
                    self.ingress_stats.parent = self
                    self.name = None
                    self.path = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path()
                    self.path.parent = self


                class IngressStats(object):
                    """
                    ingress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats()
                        self.stats.parent = self


                    class Stats(object):
                        """
                        Statistics
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.bytes = None
                            self.dropped_bytes = None
                            self.dropped_packets = None
                            self.packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bytes is not None:
                                return True

                            if self.dropped_bytes is not None:
                                return True

                            if self.dropped_packets is not None:
                                return True

                            if self.packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:ingress-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.stats is not None and self.stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats']['meta_info']


                class EgressStats(object):
                    """
                    egress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats()
                        self.stats.parent = self


                    class Stats(object):
                        """
                        Statistics
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.bytes = None
                            self.dropped_bytes = None
                            self.dropped_packets = None
                            self.packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bytes is not None:
                                return True

                            if self.dropped_bytes is not None:
                                return True

                            if self.dropped_packets is not None:
                                return True

                            if self.packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:egress-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.stats is not None and self.stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats']['meta_info']


                class Path(object):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        self.parent = None
                        self.auto_protect = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations()
                        self.operations.parent = self


                    class Operations(object):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.pop_and_forward = None
                            self.preserve = None
                            self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push()
                            self.push.parent = self
                            self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap()
                            self.swap.parent = self


                        class Swap(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:swap'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap']['meta_info']


                        class Push(object):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack()
                                self.stack.parent = self


                            class Stack(object):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.label_stack = YLeafList()
                                    self.label_stack.parent = self
                                    self.label_stack.name = 'label_stack'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.label_stack is not None:
                                        for child in self.label_stack:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:push'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.stack is not None and self.stack._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/common-mpls-static:operations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.pop_and_forward is not None:
                                return True

                            if self.preserve is not None:
                                return True

                            if self.push is not None and self.push._has_data():
                                return True

                            if self.swap is not None and self.swap._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations']['meta_info']


                    class NextHop(object):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType>`
                        
                        .. attribute:: nexthop_stats
                        
                        	lsp stats
                        	**type**\:   :py:class:`NexthopStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations>`
                        
                        .. attribute:: origin
                        
                        	The origin of this nexthop
                        	**type**\:   :py:class:`NexthopResolutionTypeIdentity <ydk.models.cisco_ios_xe.common_mpls_static.NexthopResolutionTypeIdentity>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`HoptypeEnum <ydk.models.cisco_ios_xe.common_mpls_static.HoptypeEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.next_hop_type = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self.nexthop_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats()
                            self.nexthop_stats.parent = self
                            self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations()
                            self.operations.parent = self
                            self.origin = None
                            self.protected_by = None
                            self.type = None


                        class NextHopType(object):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:next-hop-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.if_index is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.out_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType']['meta_info']


                        class Operations(object):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.pop_and_forward = None
                                self.preserve = None
                                self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap()
                                self.swap.parent = self


                            class Swap(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:swap'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap']['meta_info']


                            class Push(object):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self


                                class Stack(object):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabelEnum <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabelEnum>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_stack = YLeafList()
                                        self.label_stack.parent = self
                                        self.label_stack.name = 'label_stack'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/common-mpls-static:stack'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.label_stack is not None:
                                            for child in self.label_stack:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                        return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:push'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.stack is not None and self.stack._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:operations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.pop_and_forward is not None:
                                    return True

                                if self.preserve is not None:
                                    return True

                                if self.push is not None and self.push._has_data():
                                    return True

                                if self.swap is not None and self.swap._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations']['meta_info']


                        class NexthopStats(object):
                            """
                            lsp stats
                            
                            .. attribute:: stats
                            
                            	Statistics
                            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                self.parent = None
                                self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats()
                                self.stats.parent = self


                            class Stats(object):
                                """
                                Statistics
                                
                                .. attribute:: bytes
                                
                                	stats for byte count
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_bytes
                                
                                	stats for dropped\-bytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	stats for dropped\-packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: packets
                                
                                	stats for packet count
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    self.parent = None
                                    self.bytes = None
                                    self.dropped_bytes = None
                                    self.dropped_packets = None
                                    self.packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/common-mpls-static:stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bytes is not None:
                                        return True

                                    if self.dropped_bytes is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    if self.packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/common-mpls-static:nexthop-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.stats is not None and self.stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/common-mpls-static:next-hop[common-mpls-static:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.next_hop_type is not None and self.next_hop_type._has_data():
                                return True

                            if self.nexthop_stats is not None and self.nexthop_stats._has_data():
                                return True

                            if self.operations is not None and self.operations._has_data():
                                return True

                            if self.origin is not None:
                                return True

                            if self.protected_by is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                            return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/common-mpls-static:path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.auto_protect is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.operations is not None and self.operations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                        return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.prefix is None:
                        raise YPYModelError('Key property prefix is None')

                    return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-state/common-mpls-static:label-switched-paths/common-mpls-static:label-switched-path[common-mpls-static:vrf-name = ' + str(self.vrf_name) + '][common-mpls-static:prefix = ' + str(self.prefix) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.egress_stats is not None and self.egress_stats._has_data():
                        return True

                    if self.in_label_value is not None:
                        return True

                    if self.ingress_stats is not None and self.ingress_stats._has_data():
                        return True

                    if self.name is not None:
                        return True

                    if self.path is not None and self.path._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                    return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']

            @property
            def _common_path(self):

                return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-state/common-mpls-static:label-switched-paths'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.label_switched_path is not None:
                    for child_ref in self.label_switched_path:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
                return meta._meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths']['meta_info']

        @property
        def _common_path(self):

            return '/common-mpls-static:mpls-static/common-mpls-static:mpls-static-state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.label_switched_paths is not None and self.label_switched_paths._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
            return meta._meta_table['MplsStatic.MplsStaticState']['meta_info']

    @property
    def _common_path(self):

        return '/common-mpls-static:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.mpls_static_cfg is not None and self.mpls_static_cfg._has_data():
            return True

        if self.mpls_static_state is not None and self.mpls_static_state._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['MplsStatic']['meta_info']


class BgpRouteNexthopIdentity(NexthopResolutionTypeIdentity):
    """
    The nexthop resolved from a BGP route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        NexthopResolutionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['BgpRouteNexthopIdentity']['meta_info']


class LspVrfIdentity(LspTypeIdentity):
    """
    The LSP is per VRF
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        LspTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['LspVrfIdentity']['meta_info']


class LspIpv4Identity(LspTypeIdentity):
    """
    The LSP is for an IPv4 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        LspTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['LspIpv4Identity']['meta_info']


class StaticNexthopIdentity(NexthopResolutionTypeIdentity):
    """
    The nexthop resolved from statically configured route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        NexthopResolutionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['StaticNexthopIdentity']['meta_info']


class IsisRouteNexthopIdentity(NexthopResolutionTypeIdentity):
    """
    The nexthop resolved from an ISIS route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        NexthopResolutionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['IsisRouteNexthopIdentity']['meta_info']


class LspIdentity(LspTypeIdentity):
    """
    The LSP is cross\-connect
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        LspTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['LspIdentity']['meta_info']


class OspfRouteNexthopIdentity(NexthopResolutionTypeIdentity):
    """
    The nexthop resolved from an OSPF route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        NexthopResolutionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['OspfRouteNexthopIdentity']['meta_info']


class LspIpv6Identity(LspTypeIdentity):
    """
    The LSP is for an IPv6 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        LspTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_static as meta
        return meta._meta_table['LspIpv6Identity']['meta_info']


