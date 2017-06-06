""" Cisco_IOS_XR_ipv6_nd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-node\-discovery\: IPv6 node discovery operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv6NdBndlStateEnum(Enum):
    """
    Ipv6NdBndlStateEnum

    IPv6 ND Bundle State

    .. data:: run = 0

    	Running state

    .. data:: error = 1

    	Error state

    .. data:: wait = 2

    	Wait state

    """

    run = 0

    error = 1

    wait = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdBndlStateEnum']


class Ipv6NdMediaEncapEnum(Enum):
    """
    Ipv6NdMediaEncapEnum

    IPv6 ND Media Encapsulation Type

    .. data:: none = 0

    	No encapsulation

    .. data:: arpa = 1

    	ARPA encapsulation

    .. data:: snap = 2

    	SNAP encapsulation

    .. data:: ieee802_1q = 3

    	802_1Q encapsulation

    .. data:: srp = 4

    	SRP encapsulation

    .. data:: srpa = 5

    	SRPA encapsulation

    .. data:: srpb = 6

    	SRPB encapsulation

    .. data:: ppp = 7

    	PPP encapsulation

    .. data:: hdlc = 8

    	HDLC encapsulation

    .. data:: chdlc = 9

    	CHDLC encapsulation

    .. data:: dot1q = 10

    	DOT1Q encapsulation

    .. data:: fr = 11

    	FR encapsulation

    .. data:: gre = 12

    	GRE encapsulation

    """

    none = 0

    arpa = 1

    snap = 2

    ieee802_1q = 3

    srp = 4

    srpa = 5

    srpb = 6

    ppp = 7

    hdlc = 8

    chdlc = 9

    dot1q = 10

    fr = 11

    gre = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdMediaEncapEnum']


class Ipv6NdNeighborOriginEnum(Enum):
    """
    Ipv6NdNeighborOriginEnum

    IPv6 ND Neighbor Origin Type

    .. data:: other = 0

    	Other Address

    .. data:: static = 1

    	Static Address

    .. data:: dynamic = 2

    	Dynamic Address

    """

    other = 0

    static = 1

    dynamic = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdNeighborOriginEnum']


class Ipv6NdShStateEnum(Enum):
    """
    Ipv6NdShStateEnum

    IPv6 ND Neighbor Reachability State

    .. data:: incomplete = 0

    	Incomplete

    .. data:: reachable = 1

    	Reachable

    .. data:: stale = 2

    	Stale

    .. data:: glean = 3

    	Glean

    .. data:: delay = 4

    	Delay

    .. data:: probe = 5

    	Probe

    .. data:: delete = 6

    	Delete

    """

    incomplete = 0

    reachable = 1

    stale = 2

    glean = 3

    delay = 4

    probe = 5

    delete = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShStateEnum']


class Ipv6NdShVrFlagsEnum(Enum):
    """
    Ipv6NdShVrFlagsEnum

    IPv6 ND VR Entry Flags Type 

    .. data:: no_flags = 0

    	None

    .. data:: final_ra = 1

    	Final RA

    """

    no_flags = 0

    final_ra = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShVrFlagsEnum']


class Ipv6NdShVrStateEnum(Enum):
    """
    Ipv6NdShVrStateEnum

    IPv6 ND VR Entry State Type 

    .. data:: deleted = 0

    	Delete

    .. data:: standby = 1

    	Standby

    .. data:: active = 2

    	Active

    """

    deleted = 0

    standby = 1

    active = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShVrStateEnum']



class Ipv6NodeDiscovery(object):
    """
    IPv6 node discovery operational data
    
    .. attribute:: nodes
    
    	IPv6 node discovery list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes>`
    
    

    """

    _prefix = 'ipv6-nd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Ipv6NodeDiscovery.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        IPv6 node discovery list of nodes
        
        .. attribute:: node
        
        	IPv6 node discovery operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-nd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv6 node discovery operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	IPv6 ND list of bundle interfaces for a specific node
            	**type**\:   :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: bundle_nodes
            
            	IPv6 ND list of bundle nodes for a specific node
            	**type**\:   :py:class:`BundleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes>`
            
            .. attribute:: interfaces
            
            	IPv6 node discovery list of interfaces for a specific node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces>`
            
            .. attribute:: nd_virtual_routers
            
            	IPv6 ND virtual router information for a specific interface
            	**type**\:   :py:class:`NdVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters>`
            
            .. attribute:: neighbor_interfaces
            
            	IPv6 node discovery list of neighbor interfaces
            	**type**\:   :py:class:`NeighborInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces>`
            
            .. attribute:: neighbor_summary
            
            	IPv6 Neighbor summary
            	**type**\:   :py:class:`NeighborSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary>`
            
            

            """

            _prefix = 'ipv6-nd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.bundle_interfaces = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self.bundle_nodes = Ipv6NodeDiscovery.Nodes.Node.BundleNodes()
                self.bundle_nodes.parent = self
                self.interfaces = Ipv6NodeDiscovery.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.nd_virtual_routers = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters()
                self.nd_virtual_routers.parent = self
                self.neighbor_interfaces = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces()
                self.neighbor_interfaces.parent = self
                self.neighbor_summary = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary()
                self.neighbor_summary.parent = self


            class NeighborInterfaces(object):
                """
                IPv6 node discovery list of neighbor
                interfaces
                
                .. attribute:: neighbor_interface
                
                	IPv6 node discovery neighbor interface
                	**type**\: list of    :py:class:`NeighborInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.neighbor_interface = YList()
                    self.neighbor_interface.parent = self
                    self.neighbor_interface.name = 'neighbor_interface'


                class NeighborInterface(object):
                    """
                    IPv6 node discovery neighbor interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: host_addresses
                    
                    	IPv6 node discovery list of neighbor host addresses
                    	**type**\:   :py:class:`HostAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.host_addresses = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses()
                        self.host_addresses.parent = self


                    class HostAddresses(object):
                        """
                        IPv6 node discovery list of neighbor host
                        addresses
                        
                        .. attribute:: host_address
                        
                        	IPv6 Neighbor detailed information
                        	**type**\: list of    :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress>`
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.host_address = YList()
                            self.host_address.parent = self
                            self.host_address.name = 'host_address'


                        class HostAddress(object):
                            """
                            IPv6 Neighbor detailed information
                            
                            .. attribute:: host_address  <key>
                            
                            	Host Address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: encapsulation
                            
                            	Preferred media encap type
                            	**type**\:   :py:class:`Ipv6NdMediaEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncapEnum>`
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            .. attribute:: is_router
                            
                            	IsRouter
                            	**type**\:  bool
                            
                            .. attribute:: last_reached_time
                            
                            	Last time of reachability
                            	**type**\:   :py:class:`LastReachedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime>`
                            
                            .. attribute:: link_layer_address
                            
                            	Link\-Layer Address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: location
                            
                            	Location where the neighbor entry exists
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: origin_encapsulation
                            
                            	Neighbor origin
                            	**type**\:   :py:class:`Ipv6NdNeighborOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdNeighborOriginEnum>`
                            
                            .. attribute:: reachability_state
                            
                            	Current state
                            	**type**\:   :py:class:`Ipv6NdShStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShStateEnum>`
                            
                            .. attribute:: selected_encapsulation
                            
                            	Selected media encap
                            	**type**\:   :py:class:`Ipv6NdMediaEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncapEnum>`
                            
                            .. attribute:: serg_flags
                            
                            	ND serg flags for this entry
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.host_address = None
                                self.encapsulation = None
                                self.interface_name = None
                                self.is_router = None
                                self.last_reached_time = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime()
                                self.last_reached_time.parent = self
                                self.link_layer_address = None
                                self.location = None
                                self.origin_encapsulation = None
                                self.reachability_state = None
                                self.selected_encapsulation = None
                                self.serg_flags = None


                            class LastReachedTime(object):
                                """
                                Last time of reachability
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.seconds = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:last-reached-time'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.seconds is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.host_address is None:
                                    raise YPYModelError('Key property host_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:host-address[Cisco-IOS-XR-ipv6-nd-oper:host-address = ' + str(self.host_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.host_address is not None:
                                    return True

                                if self.encapsulation is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.is_router is not None:
                                    return True

                                if self.last_reached_time is not None and self.last_reached_time._has_data():
                                    return True

                                if self.link_layer_address is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.origin_encapsulation is not None:
                                    return True

                                if self.reachability_state is not None:
                                    return True

                                if self.selected_encapsulation is not None:
                                    return True

                                if self.serg_flags is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:host-addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.host_address is not None:
                                for child_ref in self.host_address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:neighbor-interface[Cisco-IOS-XR-ipv6-nd-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.host_addresses is not None and self.host_addresses._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:neighbor-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.neighbor_interface is not None:
                        for child_ref in self.neighbor_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces']['meta_info']


            class NeighborSummary(object):
                """
                IPv6 Neighbor summary
                
                .. attribute:: dynamic
                
                	Dynamic neighbor summary
                	**type**\:   :py:class:`Dynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic>`
                
                .. attribute:: multicast
                
                	Multicast neighbor summary
                	**type**\:   :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast>`
                
                .. attribute:: static
                
                	Static neighbor summary
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static>`
                
                .. attribute:: total_neighbor_entries
                
                	Total number of entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dynamic = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic()
                    self.dynamic.parent = self
                    self.multicast = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast()
                    self.multicast.parent = self
                    self.static = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static()
                    self.static.parent = self
                    self.total_neighbor_entries = None


                class Multicast(object):
                    """
                    Multicast neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.delayed_entries = None
                        self.deleted_entries = None
                        self.incomplete_entries = None
                        self.probe_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.subtotal_neighbor_entries = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:multicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.delayed_entries is not None:
                            return True

                        if self.deleted_entries is not None:
                            return True

                        if self.incomplete_entries is not None:
                            return True

                        if self.probe_entries is not None:
                            return True

                        if self.reachable_entries is not None:
                            return True

                        if self.stale_entries is not None:
                            return True

                        if self.subtotal_neighbor_entries is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast']['meta_info']


                class Static(object):
                    """
                    Static neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.delayed_entries = None
                        self.deleted_entries = None
                        self.incomplete_entries = None
                        self.probe_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.subtotal_neighbor_entries = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:static'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.delayed_entries is not None:
                            return True

                        if self.deleted_entries is not None:
                            return True

                        if self.incomplete_entries is not None:
                            return True

                        if self.probe_entries is not None:
                            return True

                        if self.reachable_entries is not None:
                            return True

                        if self.stale_entries is not None:
                            return True

                        if self.subtotal_neighbor_entries is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static']['meta_info']


                class Dynamic(object):
                    """
                    Dynamic neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.delayed_entries = None
                        self.deleted_entries = None
                        self.incomplete_entries = None
                        self.probe_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.subtotal_neighbor_entries = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:dynamic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.delayed_entries is not None:
                            return True

                        if self.deleted_entries is not None:
                            return True

                        if self.incomplete_entries is not None:
                            return True

                        if self.probe_entries is not None:
                            return True

                        if self.reachable_entries is not None:
                            return True

                        if self.stale_entries is not None:
                            return True

                        if self.subtotal_neighbor_entries is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:neighbor-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.dynamic is not None and self.dynamic._has_data():
                        return True

                    if self.multicast is not None and self.multicast._has_data():
                        return True

                    if self.static is not None and self.static._has_data():
                        return True

                    if self.total_neighbor_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info']


            class BundleNodes(object):
                """
                IPv6 ND list of bundle nodes for a specific
                node
                
                .. attribute:: bundle_node
                
                	IPv6 ND operational data for a specific bundle node
                	**type**\: list of    :py:class:`BundleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bundle_node = YList()
                    self.bundle_node.parent = self
                    self.bundle_node.name = 'bundle_node'


                class BundleNode(object):
                    """
                    IPv6 ND operational data for a specific
                    bundle node
                    
                    .. attribute:: node_name  <key>
                    
                    	The bundle node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: age
                    
                    	Uptime of node (secs)
                    	**type**\:   :py:class:`Age <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age>`
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\:  str
                    
                    .. attribute:: received_packets
                    
                    	Total packet receives
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_sequence_number
                    
                    	Received sequence num
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_packets
                    
                    	Total packet sends
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_sequence_number
                    
                    	Sent sequence num
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:   :py:class:`Ipv6NdBndlStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdBndlStateEnum>`
                    
                    .. attribute:: state_changes
                    
                    	State changes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_name = None
                        self.age = Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age()
                        self.age.parent = self
                        self.group_id = None
                        self.process_name = None
                        self.received_packets = None
                        self.received_sequence_number = None
                        self.sent_packets = None
                        self.sent_sequence_number = None
                        self.state = None
                        self.state_changes = None


                    class Age(object):
                        """
                        Uptime of node (secs)
                        
                        .. attribute:: seconds
                        
                        	Number of seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:age'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.node_name is None:
                            raise YPYModelError('Key property node_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:bundle-node[Cisco-IOS-XR-ipv6-nd-oper:node-name = ' + str(self.node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_name is not None:
                            return True

                        if self.age is not None and self.age._has_data():
                            return True

                        if self.group_id is not None:
                            return True

                        if self.process_name is not None:
                            return True

                        if self.received_packets is not None:
                            return True

                        if self.received_sequence_number is not None:
                            return True

                        if self.sent_packets is not None:
                            return True

                        if self.sent_sequence_number is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.state_changes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:bundle-nodes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bundle_node is not None:
                        for child_ref in self.bundle_node:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes']['meta_info']


            class BundleInterfaces(object):
                """
                IPv6 ND list of bundle interfaces for a
                specific node
                
                .. attribute:: bundle_interface
                
                	IPv6 ND operational data for a specific bundler interface
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bundle_interface = YList()
                    self.bundle_interface.parent = self
                    self.bundle_interface.name = 'bundle_interface'


                class BundleInterface(object):
                    """
                    IPv6 ND operational data for a specific
                    bundler interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: etype
                    
                    	etype
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: global_address
                    
                    	List of ND global addresses
                    	**type**\: list of    :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress>`
                    
                    .. attribute:: iftype
                    
                    	Interface type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_interface_enabled
                    
                    	If true, interface is enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_ipv6_enabled
                    
                    	If true, IPv6 is enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_mpls_enabled
                    
                    	If true, MPLS is enabled
                    	**type**\:  bool
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress>`
                    
                    .. attribute:: mac_addr
                    
                    	mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_addr_size
                    
                    	mac address size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: member_link
                    
                    	List of member links
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: member_node
                    
                    	List of member nodes
                    	**type**\: list of    :py:class:`MemberNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode>`
                    
                    .. attribute:: mtu
                    
                    	MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_parameters
                    
                    	ND interface parameters
                    	**type**\:   :py:class:`NdParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters>`
                    
                    .. attribute:: parent_interface_name
                    
                    	Parent interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vlan_tag
                    
                    	vlan tag/id/ucv
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.etype = None
                        self.global_address = YList()
                        self.global_address.parent = self
                        self.global_address.name = 'global_address'
                        self.iftype = None
                        self.is_interface_enabled = None
                        self.is_ipv6_enabled = None
                        self.is_mpls_enabled = None
                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress()
                        self.local_address.parent = self
                        self.mac_addr = None
                        self.mac_addr_size = None
                        self.member_link = YLeafList()
                        self.member_link.parent = self
                        self.member_link.name = 'member_link'
                        self.member_node = YList()
                        self.member_node.parent = self
                        self.member_node.name = 'member_node'
                        self.mtu = None
                        self.nd_parameters = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters()
                        self.nd_parameters.parent = self
                        self.parent_interface_name = None
                        self.vlan_tag = None


                    class NdParameters(object):
                        """
                        ND interface parameters
                        
                        .. attribute:: complete_glean_count
                        
                        	Completed GLEAN entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: complete_protocol_count
                        
                        	Completed PROTO entry Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dad_attempts
                        
                        	DAD attempt count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_glean_req_count
                        
                        	Dropped GLEAN entry lequest count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_protocol_req_count
                        
                        	Dropped PROTO entry request count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_glean_count
                        
                        	Incomplete GLEAN entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_protocol_count
                        
                        	Incomplete PROTO entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_dad_enabled
                        
                        	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                        	**type**\:  bool
                        
                        .. attribute:: is_dhcp_managed
                        
                        	Flag used for utilising DHCP
                        	**type**\:  bool
                        
                        .. attribute:: is_icm_pv6_redirect
                        
                        	ICMP redirect flag
                        	**type**\:  bool
                        
                        .. attribute:: is_route_address_managed
                        
                        	Flag used to manage routable address
                        	**type**\:  bool
                        
                        .. attribute:: is_suppressed
                        
                        	Suppress flag
                        	**type**\:  bool
                        
                        .. attribute:: nd_advertisement_lifetime
                        
                        	ND router advertisement life time in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_cache_limit
                        
                        	Completed adjacency limit per interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_max_transmit_interval
                        
                        	ND router advertisement maximum transmit interval in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_min_transmit_interval
                        
                        	ND router advertisement minimum transmit interval in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_reachable_time
                        
                        	Time to reach ND in msec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_retransmit_interval
                        
                        	ND retransmit interval in msec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: send_unicast_ra
                        
                        	unicast RA send flag
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.complete_glean_count = None
                            self.complete_protocol_count = None
                            self.dad_attempts = None
                            self.dropped_glean_req_count = None
                            self.dropped_protocol_req_count = None
                            self.incomplete_glean_count = None
                            self.incomplete_protocol_count = None
                            self.is_dad_enabled = None
                            self.is_dhcp_managed = None
                            self.is_icm_pv6_redirect = None
                            self.is_route_address_managed = None
                            self.is_suppressed = None
                            self.nd_advertisement_lifetime = None
                            self.nd_cache_limit = None
                            self.nd_max_transmit_interval = None
                            self.nd_min_transmit_interval = None
                            self.nd_reachable_time = None
                            self.nd_retransmit_interval = None
                            self.send_unicast_ra = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:nd-parameters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.complete_glean_count is not None:
                                return True

                            if self.complete_protocol_count is not None:
                                return True

                            if self.dad_attempts is not None:
                                return True

                            if self.dropped_glean_req_count is not None:
                                return True

                            if self.dropped_protocol_req_count is not None:
                                return True

                            if self.incomplete_glean_count is not None:
                                return True

                            if self.incomplete_protocol_count is not None:
                                return True

                            if self.is_dad_enabled is not None:
                                return True

                            if self.is_dhcp_managed is not None:
                                return True

                            if self.is_icm_pv6_redirect is not None:
                                return True

                            if self.is_route_address_managed is not None:
                                return True

                            if self.is_suppressed is not None:
                                return True

                            if self.nd_advertisement_lifetime is not None:
                                return True

                            if self.nd_cache_limit is not None:
                                return True

                            if self.nd_max_transmit_interval is not None:
                                return True

                            if self.nd_min_transmit_interval is not None:
                                return True

                            if self.nd_reachable_time is not None:
                                return True

                            if self.nd_retransmit_interval is not None:
                                return True

                            if self.send_unicast_ra is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters']['meta_info']


                    class LocalAddress(object):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress']['meta_info']


                    class GlobalAddress(object):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:global-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress']['meta_info']


                    class MemberNode(object):
                        """
                        List of member nodes
                        
                        .. attribute:: node_name
                        
                        	Node Name
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: total_links
                        
                        	Number of links on the node
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_name = None
                            self.total_links = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:member-node'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.node_name is not None:
                                return True

                            if self.total_links is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:bundle-interface[Cisco-IOS-XR-ipv6-nd-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.etype is not None:
                            return True

                        if self.global_address is not None:
                            for child_ref in self.global_address:
                                if child_ref._has_data():
                                    return True

                        if self.iftype is not None:
                            return True

                        if self.is_interface_enabled is not None:
                            return True

                        if self.is_ipv6_enabled is not None:
                            return True

                        if self.is_mpls_enabled is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.mac_addr is not None:
                            return True

                        if self.mac_addr_size is not None:
                            return True

                        if self.member_link is not None:
                            for child in self.member_link:
                                if child is not None:
                                    return True

                        if self.member_node is not None:
                            for child_ref in self.member_node:
                                if child_ref._has_data():
                                    return True

                        if self.mtu is not None:
                            return True

                        if self.nd_parameters is not None and self.nd_parameters._has_data():
                            return True

                        if self.parent_interface_name is not None:
                            return True

                        if self.vlan_tag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:bundle-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bundle_interface is not None:
                        for child_ref in self.bundle_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(object):
                """
                IPv6 node discovery list of interfaces for a
                specific node
                
                .. attribute:: interface
                
                	IPv6  node discovery operational data for a specific node and interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    IPv6  node discovery operational data for a
                    specific node and interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: complete_glean_count
                    
                    	Completed GLEAN entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: complete_protocol_count
                    
                    	Completed PROTO entry Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dad_attempts
                    
                    	DAD attempt count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_glean_req_count
                    
                    	Dropped GLEAN entry lequest count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_protocol_req_count
                    
                    	Dropped PROTO entry request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_glean_count
                    
                    	Incomplete GLEAN entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_protocol_count
                    
                    	Incomplete PROTO entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_dad_enabled
                    
                    	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                    	**type**\:  bool
                    
                    .. attribute:: is_dhcp_managed
                    
                    	Flag used for utilising DHCP
                    	**type**\:  bool
                    
                    .. attribute:: is_icm_pv6_redirect
                    
                    	ICMP redirect flag
                    	**type**\:  bool
                    
                    .. attribute:: is_route_address_managed
                    
                    	Flag used to manage routable address
                    	**type**\:  bool
                    
                    .. attribute:: is_suppressed
                    
                    	Suppress flag
                    	**type**\:  bool
                    
                    .. attribute:: nd_advertisement_lifetime
                    
                    	ND router advertisement life time in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_cache_limit
                    
                    	Completed adjacency limit per interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_max_transmit_interval
                    
                    	ND router advertisement maximum transmit interval in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_min_transmit_interval
                    
                    	ND router advertisement minimum transmit interval in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_reachable_time
                    
                    	Time to reach ND in msec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_retransmit_interval
                    
                    	ND retransmit interval in msec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_unicast_ra
                    
                    	unicast RA send flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.complete_glean_count = None
                        self.complete_protocol_count = None
                        self.dad_attempts = None
                        self.dropped_glean_req_count = None
                        self.dropped_protocol_req_count = None
                        self.incomplete_glean_count = None
                        self.incomplete_protocol_count = None
                        self.is_dad_enabled = None
                        self.is_dhcp_managed = None
                        self.is_icm_pv6_redirect = None
                        self.is_route_address_managed = None
                        self.is_suppressed = None
                        self.nd_advertisement_lifetime = None
                        self.nd_cache_limit = None
                        self.nd_max_transmit_interval = None
                        self.nd_min_transmit_interval = None
                        self.nd_reachable_time = None
                        self.nd_retransmit_interval = None
                        self.send_unicast_ra = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:interface[Cisco-IOS-XR-ipv6-nd-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.complete_glean_count is not None:
                            return True

                        if self.complete_protocol_count is not None:
                            return True

                        if self.dad_attempts is not None:
                            return True

                        if self.dropped_glean_req_count is not None:
                            return True

                        if self.dropped_protocol_req_count is not None:
                            return True

                        if self.incomplete_glean_count is not None:
                            return True

                        if self.incomplete_protocol_count is not None:
                            return True

                        if self.is_dad_enabled is not None:
                            return True

                        if self.is_dhcp_managed is not None:
                            return True

                        if self.is_icm_pv6_redirect is not None:
                            return True

                        if self.is_route_address_managed is not None:
                            return True

                        if self.is_suppressed is not None:
                            return True

                        if self.nd_advertisement_lifetime is not None:
                            return True

                        if self.nd_cache_limit is not None:
                            return True

                        if self.nd_max_transmit_interval is not None:
                            return True

                        if self.nd_min_transmit_interval is not None:
                            return True

                        if self.nd_reachable_time is not None:
                            return True

                        if self.nd_retransmit_interval is not None:
                            return True

                        if self.send_unicast_ra is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces']['meta_info']


            class NdVirtualRouters(object):
                """
                IPv6 ND virtual router information for a
                specific interface
                
                .. attribute:: nd_virtual_router
                
                	IPv6 ND virtual  router operational data for a specific interface
                	**type**\: list of    :py:class:`NdVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nd_virtual_router = YList()
                    self.nd_virtual_router.parent = self
                    self.nd_virtual_router.name = 'nd_virtual_router'


                class NdVirtualRouter(object):
                    """
                    IPv6 ND virtual  router operational data for
                    a specific interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: context
                    
                    	Virtual Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flags
                    
                    	VR Flags
                    	**type**\:   :py:class:`Ipv6NdShVrFlagsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrFlagsEnum>`
                    
                    .. attribute:: link_layer_address
                    
                    	Link\-Layer Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress>`
                    
                    .. attribute:: state
                    
                    	VR state
                    	**type**\:   :py:class:`Ipv6NdShVrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrStateEnum>`
                    
                    .. attribute:: vr_gl_addr_ct
                    
                    	Virtual Global Address Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vr_global_address
                    
                    	List of ND global addresses
                    	**type**\: list of    :py:class:`VrGlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.context = None
                        self.flags = None
                        self.link_layer_address = None
                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress()
                        self.local_address.parent = self
                        self.state = None
                        self.vr_gl_addr_ct = None
                        self.vr_global_address = YList()
                        self.vr_global_address.parent = self
                        self.vr_global_address.name = 'vr_global_address'


                    class LocalAddress(object):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress']['meta_info']


                    class VrGlobalAddress(object):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:vr-global-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:nd-virtual-router[Cisco-IOS-XR-ipv6-nd-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.context is not None:
                            return True

                        if self.flags is not None:
                            return True

                        if self.link_layer_address is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.state is not None:
                            return True

                        if self.vr_gl_addr_ct is not None:
                            return True

                        if self.vr_global_address is not None:
                            for child_ref in self.vr_global_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-nd-oper:nd-virtual-routers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nd_virtual_router is not None:
                        for child_ref in self.nd_virtual_router:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/Cisco-IOS-XR-ipv6-nd-oper:nodes/Cisco-IOS-XR-ipv6-nd-oper:node[Cisco-IOS-XR-ipv6-nd-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.bundle_interfaces is not None and self.bundle_interfaces._has_data():
                    return True

                if self.bundle_nodes is not None and self.bundle_nodes._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.nd_virtual_routers is not None and self.nd_virtual_routers._has_data():
                    return True

                if self.neighbor_interfaces is not None and self.neighbor_interfaces._has_data():
                    return True

                if self.neighbor_summary is not None and self.neighbor_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/Cisco-IOS-XR-ipv6-nd-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
            return meta._meta_table['Ipv6NodeDiscovery.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NodeDiscovery']['meta_info']


