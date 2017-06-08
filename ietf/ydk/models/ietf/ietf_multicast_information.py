""" ietf_multicast_information 

This module contains a collection of YANG definitions for
managing multicast information.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class VirtualTypeEnum(Enum):
    """
    VirtualTypeEnum

    The collection of virtual network type.

    .. data:: vxlan = 0

    	The vxlan type.

    .. data:: virtual_subnet = 1

    	The nvgre type

    .. data:: vni = 2

    	The geneve type

    """

    vxlan = 0

    virtual_subnet = 1

    vni = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_multicast_information as meta
        return meta._meta_table['VirtualTypeEnum']



class MulticastInformation(object):
    """
    The model of multicast service. Include overlay, transport and underlay.
    
    .. attribute:: multicast_info
    
    	The detail multicast information
    	**type**\: list of    :py:class:`MulticastInfo <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo>`
    
    

    """

    _prefix = 'multicast-info'
    _revision = '2016-12-08'

    def __init__(self):
        self.multicast_info = YList()
        self.multicast_info.parent = self
        self.multicast_info.name = 'multicast_info'


    class MulticastInfo(object):
        """
        The detail multicast information.
        
        .. attribute:: group_address  <key>
        
        	The address of multicast group
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: group_wildcard  <key>
        
        	The wildcard information of group
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: source_address  <key>
        
        	The address of multicast source. The value set to zero means that the receiver interests in all source that relevant to one group
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: source_wildcard  <key>
        
        	The wildcard information of source
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: vni_type  <key>
        
        	The type of virtual network identifier. Include the Vxlan NVGRE and Geneve
        	**type**\:   :py:class:`VirtualTypeEnum <ydk.models.ietf.ietf_multicast_information.VirtualTypeEnum>`
        
        .. attribute:: vni_value  <key>
        
        	The value of Vxlan network identifier, virtual subnet ID or virtual net identifier
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vpn_id  <key>
        
        	The vpn\-id of the multicast flow. If there is global instance, the vpnid value should be zero
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: multicast_overlay
        
        	The overlay information of multicast service
        	**type**\:   :py:class:`MulticastOverlay <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay>`
        
        .. attribute:: multicast_transport
        
        	The transportion of multicast service
        	**type**\:   :py:class:`MulticastTransport <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastTransport>`
        
        .. attribute:: multicast_underlay
        
        	The underlay of multicast service
        	**type**\:   :py:class:`MulticastUnderlay <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay>`
        
        

        """

        _prefix = 'multicast-info'
        _revision = '2016-12-08'

        def __init__(self):
            self.parent = None
            self.group_address = None
            self.group_wildcard = None
            self.source_address = None
            self.source_wildcard = None
            self.vni_type = None
            self.vni_value = None
            self.vpn_id = None
            self.multicast_overlay = MulticastInformation.MulticastInfo.MulticastOverlay()
            self.multicast_overlay.parent = self
            self.multicast_transport = MulticastInformation.MulticastInfo.MulticastTransport()
            self.multicast_transport.parent = self
            self.multicast_underlay = MulticastInformation.MulticastInfo.MulticastUnderlay()
            self.multicast_underlay.parent = self


        class MulticastOverlay(object):
            """
            The overlay information of multicast service.
            
            .. attribute:: bier_information
            
            	The ingress and egress BIER nodes information
            	**type**\:   :py:class:`BierInformation <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation>`
            
            .. attribute:: nodes_information
            
            	The ingress and egress nodes information
            	**type**\:   :py:class:`NodesInformation <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation>`
            
            .. attribute:: overlay_technology
            
            	The possible overlay technologies for multicast service
            	**type**\:   :py:class:`OverlayTechnology <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology>`
            
            

            """

            _prefix = 'multicast-info'
            _revision = '2016-12-08'

            def __init__(self):
                self.parent = None
                self.bier_information = MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation()
                self.bier_information.parent = self
                self.nodes_information = MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation()
                self.nodes_information.parent = self
                self.overlay_technology = MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology()
                self.overlay_technology.parent = self


            class NodesInformation(object):
                """
                The ingress and egress nodes information.
                
                .. attribute:: egress_nodes
                
                	This ID information of one adjacency
                	**type**\: list of    :py:class:`EgressNodes <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes>`
                
                .. attribute:: ingress_node
                
                	The ingress node of multicast flow. Or the ingress node of MVPN and BIER. In MVPN, this is the address of ingress PE; in BIER, this is the BFR\-prefix of ingress nodes
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.egress_nodes = YList()
                    self.egress_nodes.parent = self
                    self.egress_nodes.name = 'egress_nodes'
                    self.ingress_node = None


                class EgressNodes(object):
                    """
                    This ID information of one adjacency.
                    
                    .. attribute:: number  <key>
                    
                    	The number of egress nodes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: egress_node
                    
                    	The egress multicast nodes of multicast flow. Or the egress node of MVPN and BIER. In MVPN, this is the address of egress PE; in BIER, this is the BFR\-prefix of ingress nodes
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'multicast-info'
                    _revision = '2016-12-08'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.egress_node = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/ietf-multicast-information:egress-nodes[ietf-multicast-information:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.number is not None:
                            return True

                        if self.egress_node is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_multicast_information as meta
                        return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:nodes-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.egress_nodes is not None:
                        for child_ref in self.egress_nodes:
                            if child_ref._has_data():
                                return True

                    if self.ingress_node is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation']['meta_info']


            class BierInformation(object):
                """
                The ingress and egress BIER nodes information.
                
                .. attribute:: egress_nodes
                
                	This ID information of one adjacency
                	**type**\: list of    :py:class:`EgressNodes <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes>`
                
                .. attribute:: ingress_node
                
                	The ingress node of multicast flow. This is the BFR\-id of ingress nodes
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: sub_domain
                
                	The sub\-domain that this multicast flow belongs to
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.egress_nodes = YList()
                    self.egress_nodes.parent = self
                    self.egress_nodes.name = 'egress_nodes'
                    self.ingress_node = None
                    self.sub_domain = None


                class EgressNodes(object):
                    """
                    This ID information of one adjacency.
                    
                    .. attribute:: number  <key>
                    
                    	The number of egress nodes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: egress_node
                    
                    	The egress multicast nodes of multicast flow. This is the BFR\-id of egress nodes
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'multicast-info'
                    _revision = '2016-12-08'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.egress_node = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/ietf-multicast-information:egress-nodes[ietf-multicast-information:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.number is not None:
                            return True

                        if self.egress_node is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_multicast_information as meta
                        return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:bier-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.egress_nodes is not None:
                        for child_ref in self.egress_nodes:
                            if child_ref._has_data():
                                return True

                    if self.ingress_node is not None:
                        return True

                    if self.sub_domain is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation']['meta_info']


            class OverlayTechnology(object):
                """
                The possible overlay technologies for multicast service.
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:overlay-technology'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-multicast-information:multicast-overlay'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bier_information is not None and self.bier_information._has_data():
                    return True

                if self.nodes_information is not None and self.nodes_information._has_data():
                    return True

                if self.overlay_technology is not None and self.overlay_technology._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_multicast_information as meta
                return meta._meta_table['MulticastInformation.MulticastInfo.MulticastOverlay']['meta_info']


        class MulticastTransport(object):
            """
            The transportion of multicast service.
            
            .. attribute:: bier
            
            	The transport technology is BIER
            	**type**\:   :py:class:`Bier <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastTransport.Bier>`
            
            .. attribute:: cisco_mode
            
            	The transport technology is cisco\-mode
            	**type**\:   :py:class:`CiscoMode <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode>`
            
            .. attribute:: mpls
            
            	The transport technology is mpls
            	**type**\:   :py:class:`Mpls <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastTransport.Mpls>`
            
            .. attribute:: pim
            
            	The transport technology is PIM
            	**type**\:   :py:class:`Pim <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastTransport.Pim>`
            
            

            """

            _prefix = 'multicast-info'
            _revision = '2016-12-08'

            def __init__(self):
                self.parent = None
                self.bier = MulticastInformation.MulticastInfo.MulticastTransport.Bier()
                self.bier.parent = self
                self.cisco_mode = MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode()
                self.cisco_mode.parent = self
                self.mpls = MulticastInformation.MulticastInfo.MulticastTransport.Mpls()
                self.mpls.parent = self
                self.pim = MulticastInformation.MulticastInfo.MulticastTransport.Pim()
                self.pim.parent = self


            class Bier(object):
                """
                The transport technology is BIER.
                
                .. attribute:: bitstringlength
                
                	The bitstringlength used by BIER forwarding
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: ecmp
                
                	The capability of ECMP
                	**type**\:  bool
                
                .. attribute:: frr
                
                	The capability of fast re\-route
                	**type**\:  bool
                
                .. attribute:: set_identifier
                
                	The set identifier used by this multicast flow, especially in BIER TE
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: sub_domain
                
                	The subdomain id that this multicast flow belongs to
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.bitstringlength = None
                    self.ecmp = None
                    self.frr = None
                    self.set_identifier = None
                    self.sub_domain = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:bier'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.bitstringlength is not None:
                        return True

                    if self.ecmp is not None:
                        return True

                    if self.frr is not None:
                        return True

                    if self.set_identifier is not None:
                        return True

                    if self.sub_domain is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Bier']['meta_info']


            class CiscoMode(object):
                """
                The transport technology is cisco\-mode.
                
                .. attribute:: bfd
                
                	If the bfd function should be supported
                	**type**\:  bool
                
                .. attribute:: graceful_restart
                
                	If the graceful restart function should be supported
                	**type**\:  bool
                
                .. attribute:: p_group
                
                	The address of p\-group
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.bfd = None
                    self.graceful_restart = None
                    self.p_group = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:cisco-mode'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.bfd is not None:
                        return True

                    if self.graceful_restart is not None:
                        return True

                    if self.p_group is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode']['meta_info']


            class Mpls(object):
                """
                The transport technology is mpls.
                
                .. attribute:: mldp_backup_tunnel
                
                	If the backup tunnel function should be supported
                	**type**\:  bool
                
                .. attribute:: mldp_frr
                
                	If the fast re\-route function should be supported
                	**type**\:  bool
                
                .. attribute:: mldp_tunnel_id
                
                	The tunnel id that correspond this flow
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_backup_tunnel
                
                	If the backup tunnel function should be supported
                	**type**\:  bool
                
                .. attribute:: te_frr
                
                	If the fast re\-route function should be supported
                	**type**\:  bool
                
                .. attribute:: te_tunnel_id
                
                	The tunnel id that correspond this flow
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.mldp_backup_tunnel = None
                    self.mldp_frr = None
                    self.mldp_tunnel_id = None
                    self.te_backup_tunnel = None
                    self.te_frr = None
                    self.te_tunnel_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:mpls'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mldp_backup_tunnel is not None:
                        return True

                    if self.mldp_frr is not None:
                        return True

                    if self.mldp_tunnel_id is not None:
                        return True

                    if self.te_backup_tunnel is not None:
                        return True

                    if self.te_frr is not None:
                        return True

                    if self.te_tunnel_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Mpls']['meta_info']


            class Pim(object):
                """
                The transport technology is PIM.
                
                .. attribute:: bfd
                
                	If the bfd function should be supported
                	**type**\:  bool
                
                .. attribute:: graceful_restart
                
                	If the graceful restart function should be supported
                	**type**\:  bool
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.bfd = None
                    self.graceful_restart = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:pim'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.bfd is not None:
                        return True

                    if self.graceful_restart is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Pim']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-multicast-information:multicast-transport'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bier is not None and self.bier._has_data():
                    return True

                if self.cisco_mode is not None and self.cisco_mode._has_data():
                    return True

                if self.mpls is not None and self.mpls._has_data():
                    return True

                if self.pim is not None and self.pim._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_multicast_information as meta
                return meta._meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info']


        class MulticastUnderlay(object):
            """
            The underlay of multicast service.
            
            .. attribute:: babel
            
            	The underlay technology is Babel
            	**type**\:   :py:class:`Babel <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay.Babel>`
            
            .. attribute:: bgp
            
            	The underlay technology is BGP
            	**type**\:   :py:class:`Bgp <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp>`
            
            .. attribute:: isis
            
            	The underlay technology is ISIS
            	**type**\:   :py:class:`Isis <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay.Isis>`
            
            .. attribute:: ospf
            
            	The underlay technology is OSPF
            	**type**\:   :py:class:`Ospf <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf>`
            
            .. attribute:: pim
            
            	The underlay technology is PIM
            	**type**\:   :py:class:`Pim <ydk.models.ietf.ietf_multicast_information.MulticastInformation.MulticastInfo.MulticastUnderlay.Pim>`
            
            .. attribute:: underlay_requirement
            
            	If the underlay technology should be required
            	**type**\:  bool
            
            

            """

            _prefix = 'multicast-info'
            _revision = '2016-12-08'

            def __init__(self):
                self.parent = None
                self.babel = MulticastInformation.MulticastInfo.MulticastUnderlay.Babel()
                self.babel.parent = self
                self.bgp = MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp()
                self.bgp.parent = self
                self.isis = MulticastInformation.MulticastInfo.MulticastUnderlay.Isis()
                self.isis.parent = self
                self.ospf = MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf()
                self.ospf.parent = self
                self.pim = MulticastInformation.MulticastInfo.MulticastUnderlay.Pim()
                self.pim.parent = self
                self.underlay_requirement = None


            class Bgp(object):
                """
                The underlay technology is BGP.
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:bgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp']['meta_info']


            class Ospf(object):
                """
                The underlay technology is OSPF.
                
                .. attribute:: topology_id
                
                	The topology id of ospf instance
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.topology_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:ospf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.topology_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf']['meta_info']


            class Isis(object):
                """
                The underlay technology is ISIS.
                
                .. attribute:: topology_id
                
                	The topology id of isis instance
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None
                    self.topology_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:isis'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.topology_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Isis']['meta_info']


            class Babel(object):
                """
                The underlay technology is Babel.
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:babel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Babel']['meta_info']


            class Pim(object):
                """
                The underlay technology is PIM.
                
                

                """

                _prefix = 'multicast-info'
                _revision = '2016-12-08'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-multicast-information:pim'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_multicast_information as meta
                    return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Pim']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-multicast-information:multicast-underlay'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.babel is not None and self.babel._has_data():
                    return True

                if self.bgp is not None and self.bgp._has_data():
                    return True

                if self.isis is not None and self.isis._has_data():
                    return True

                if self.ospf is not None and self.ospf._has_data():
                    return True

                if self.pim is not None and self.pim._has_data():
                    return True

                if self.underlay_requirement is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_multicast_information as meta
                return meta._meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']

        @property
        def _common_path(self):
            if self.group_address is None:
                raise YPYModelError('Key property group_address is None')
            if self.group_wildcard is None:
                raise YPYModelError('Key property group_wildcard is None')
            if self.source_address is None:
                raise YPYModelError('Key property source_address is None')
            if self.source_wildcard is None:
                raise YPYModelError('Key property source_wildcard is None')
            if self.vni_type is None:
                raise YPYModelError('Key property vni_type is None')
            if self.vni_value is None:
                raise YPYModelError('Key property vni_value is None')
            if self.vpn_id is None:
                raise YPYModelError('Key property vpn_id is None')

            return '/ietf-multicast-information:multicast-information/ietf-multicast-information:multicast-info[ietf-multicast-information:group-address = ' + str(self.group_address) + '][ietf-multicast-information:group-wildcard = ' + str(self.group_wildcard) + '][ietf-multicast-information:source-address = ' + str(self.source_address) + '][ietf-multicast-information:source-wildcard = ' + str(self.source_wildcard) + '][ietf-multicast-information:vni-type = ' + str(self.vni_type) + '][ietf-multicast-information:vni-value = ' + str(self.vni_value) + '][ietf-multicast-information:vpn-id = ' + str(self.vpn_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.group_address is not None:
                return True

            if self.group_wildcard is not None:
                return True

            if self.source_address is not None:
                return True

            if self.source_wildcard is not None:
                return True

            if self.vni_type is not None:
                return True

            if self.vni_value is not None:
                return True

            if self.vpn_id is not None:
                return True

            if self.multicast_overlay is not None and self.multicast_overlay._has_data():
                return True

            if self.multicast_transport is not None and self.multicast_transport._has_data():
                return True

            if self.multicast_underlay is not None and self.multicast_underlay._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_multicast_information as meta
            return meta._meta_table['MulticastInformation.MulticastInfo']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-multicast-information:multicast-information'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.multicast_info is not None:
            for child_ref in self.multicast_info:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_multicast_information as meta
        return meta._meta_table['MulticastInformation']['meta_info']


