""" Cisco_IOS_XR_ppp_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppea\: PPPEA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PppEaAdjStateEnum(Enum):
    """
    PppEaAdjStateEnum

    Ppp ea adj state

    .. data:: ppp_ea_adj_state_not_installed = 0

    	Ajacency not installed in AIB

    .. data:: ppp_ea_adj_state_installed = 1

    	Adjacency installed in AIB

    """

    ppp_ea_adj_state_not_installed = 0

    ppp_ea_adj_state_installed = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
        return meta._meta_table['PppEaAdjStateEnum']



class Pppea(object):
    """
    PPPEA operational data
    
    .. attribute:: nodes
    
    	Per node PPPEA operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes>`
    
    

    """

    _prefix = 'ppp-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Pppea.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Per node PPPEA operational data
        
        .. attribute:: node
        
        	The PPPEA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node>`
        
        

        """

        _prefix = 'ppp-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The PPPEA operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ea_interface_names
            
            	Show interface related information from the PPP EA
            	**type**\:   :py:class:`EaInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames>`
            
            

            """

            _prefix = 'ppp-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.ea_interface_names = Pppea.Nodes.Node.EaInterfaceNames()
                self.ea_interface_names.parent = self


            class EaInterfaceNames(object):
                """
                Show interface related information from the
                PPP EA
                
                .. attribute:: ea_interface_name
                
                	Interface name
                	**type**\: list of    :py:class:`EaInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName>`
                
                

                """

                _prefix = 'ppp-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ea_interface_name = YList()
                    self.ea_interface_name.parent = self
                    self.ea_interface_name.name = 'ea_interface_name'


                class EaInterfaceName(object):
                    """
                    Interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface running PPPEA
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: echo_request_interval
                    
                    	Echo\-Request interval
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: echo_request_retry_count
                    
                    	Echo\-Request retry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forwarding_enabled
                    
                    	Forwarding State
                    	**type**\:  bool
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_adjacency_state
                    
                    	Interface adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: ipv4_adjacency_state
                    
                    	Ipv4 adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: ipv6_adjacency_state
                    
                    	IPv6 adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: ipv6vrf_table_id
                    
                    	IPv6CP VRF Table ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_ipcp_running
                    
                    	TRUE if IPCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_ipv6cp_running
                    
                    	TRUE if IPV6CP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_lcp_running
                    
                    	TRUE if LCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_mplscp_running
                    
                    	TRUE if MPLSCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_multilink_bundle
                    
                    	TRUE if this is a Multilink bundle interface
                    	**type**\:  bool
                    
                    .. attribute:: is_vpdn_tunneled
                    
                    	Is VPDN tunneled
                    	**type**\:  bool
                    
                    .. attribute:: l2_adjacency_state
                    
                    	L2 adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: l2_provisioned
                    
                    	L2 Provisioned State
                    	**type**\:  bool
                    
                    .. attribute:: l2_tunnel_enabled
                    
                    	L2 Tunnel State
                    	**type**\:  bool
                    
                    .. attribute:: l2ip_interworking_adjacency_state
                    
                    	L2 IP Interworking adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: l2ip_interworking_enabled
                    
                    	L2 IP Interworking State
                    	**type**\:  bool
                    
                    .. attribute:: lac_adjacency_state
                    
                    	LAC adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: local_magic
                    
                    	Local magic number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_mcmp_classes
                    
                    	Local number of MCMP Suspension classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_mrru
                    
                    	Local MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_mtu
                    
                    	Local interface MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mpls_adjacency_state
                    
                    	MPLS adjacency state
                    	**type**\:   :py:class:`PppEaAdjStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjStateEnum>`
                    
                    .. attribute:: multilink_interface
                    
                    	Multilink interface that this interface is a member of, if any
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: parent_interface_handle
                    
                    	Parent Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: peer_magic
                    
                    	Peer magic number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_mcmp_classes
                    
                    	Peer number of MCMP Suspension classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: peer_mrru
                    
                    	Peer MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: synchronized
                    
                    	MA synchronization
                    	**type**\:  bool
                    
                    .. attribute:: vrf_table_id
                    
                    	IPCP VRF Table ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: xconnect_id
                    
                    	XConnect ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ppp-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.echo_request_interval = None
                        self.echo_request_retry_count = None
                        self.forwarding_enabled = None
                        self.interface = None
                        self.interface_adjacency_state = None
                        self.ipv4_adjacency_state = None
                        self.ipv6_adjacency_state = None
                        self.ipv6vrf_table_id = None
                        self.is_ipcp_running = None
                        self.is_ipv6cp_running = None
                        self.is_lcp_running = None
                        self.is_mplscp_running = None
                        self.is_multilink_bundle = None
                        self.is_vpdn_tunneled = None
                        self.l2_adjacency_state = None
                        self.l2_provisioned = None
                        self.l2_tunnel_enabled = None
                        self.l2ip_interworking_adjacency_state = None
                        self.l2ip_interworking_enabled = None
                        self.lac_adjacency_state = None
                        self.local_magic = None
                        self.local_mcmp_classes = None
                        self.local_mrru = None
                        self.local_mtu = None
                        self.mpls_adjacency_state = None
                        self.multilink_interface = None
                        self.parent_interface_handle = None
                        self.peer_magic = None
                        self.peer_mcmp_classes = None
                        self.peer_mrru = None
                        self.synchronized = None
                        self.vrf_table_id = None
                        self.xconnect_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ea-oper:ea-interface-name[Cisco-IOS-XR-ppp-ea-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.echo_request_interval is not None:
                            return True

                        if self.echo_request_retry_count is not None:
                            return True

                        if self.forwarding_enabled is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.interface_adjacency_state is not None:
                            return True

                        if self.ipv4_adjacency_state is not None:
                            return True

                        if self.ipv6_adjacency_state is not None:
                            return True

                        if self.ipv6vrf_table_id is not None:
                            return True

                        if self.is_ipcp_running is not None:
                            return True

                        if self.is_ipv6cp_running is not None:
                            return True

                        if self.is_lcp_running is not None:
                            return True

                        if self.is_mplscp_running is not None:
                            return True

                        if self.is_multilink_bundle is not None:
                            return True

                        if self.is_vpdn_tunneled is not None:
                            return True

                        if self.l2_adjacency_state is not None:
                            return True

                        if self.l2_provisioned is not None:
                            return True

                        if self.l2_tunnel_enabled is not None:
                            return True

                        if self.l2ip_interworking_adjacency_state is not None:
                            return True

                        if self.l2ip_interworking_enabled is not None:
                            return True

                        if self.lac_adjacency_state is not None:
                            return True

                        if self.local_magic is not None:
                            return True

                        if self.local_mcmp_classes is not None:
                            return True

                        if self.local_mrru is not None:
                            return True

                        if self.local_mtu is not None:
                            return True

                        if self.mpls_adjacency_state is not None:
                            return True

                        if self.multilink_interface is not None:
                            return True

                        if self.parent_interface_handle is not None:
                            return True

                        if self.peer_magic is not None:
                            return True

                        if self.peer_mcmp_classes is not None:
                            return True

                        if self.peer_mrru is not None:
                            return True

                        if self.synchronized is not None:
                            return True

                        if self.vrf_table_id is not None:
                            return True

                        if self.xconnect_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
                        return meta._meta_table['Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ea-oper:ea-interface-names'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ea_interface_name is not None:
                        for child_ref in self.ea_interface_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
                    return meta._meta_table['Pppea.Nodes.Node.EaInterfaceNames']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ppp-ea-oper:pppea/Cisco-IOS-XR-ppp-ea-oper:nodes/Cisco-IOS-XR-ppp-ea-oper:node[Cisco-IOS-XR-ppp-ea-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.ea_interface_names is not None and self.ea_interface_names._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
                return meta._meta_table['Pppea.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ppp-ea-oper:pppea/Cisco-IOS-XR-ppp-ea-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
            return meta._meta_table['Pppea.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ppp-ea-oper:pppea'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ea_oper as meta
        return meta._meta_table['Pppea']['meta_info']


