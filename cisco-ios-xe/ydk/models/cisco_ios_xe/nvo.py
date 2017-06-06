""" nvo 

This module contains a collection of YANG definitions
for Cisco VxLAN feature configuration.

Copyright (c) 2013\-2014 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class OverlayEncapTypeIdentity(object):
    """
    Base identity from which identities describing different
    encapsulationtypes are derived.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _nvo as meta
        return meta._meta_table['OverlayEncapTypeIdentity']['meta_info']


class NvoInstances(object):
    """
    vxlan instances
    
    .. attribute:: nvo_instance
    
    	List of instances
    	**type**\: list of    :py:class:`NvoInstance <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance>`
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        self.nvo_instance = YList()
        self.nvo_instance.parent = self
        self.nvo_instance.name = 'nvo_instance'


    class NvoInstance(object):
        """
        List of instances
        
        .. attribute:: nvo_id  <key>
        
        	Network Virtualization Overlay Instance  Identifier
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: overlay_encapsulation
        
        	Encapsulation type
        	**type**\:   :py:class:`OverlayEncapTypeIdentity <ydk.models.cisco_ios_xe.nvo.OverlayEncapTypeIdentity>`
        
        .. attribute:: source_interface
        
        	Source interface name
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        	**mandatory**\: True
        
        .. attribute:: virtual_network
        
        	VNI member attributes
        	**type**\: list of    :py:class:`VirtualNetwork <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork>`
        
        

        """

        _prefix = 'nvo'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.nvo_id = None
            self.overlay_encapsulation = None
            self.source_interface = None
            self.virtual_network = YList()
            self.virtual_network.parent = self
            self.virtual_network.name = 'virtual_network'


        class VirtualNetwork(object):
            """
            VNI member attributes
            
            .. attribute:: vni_start  <key>
            
            	Single Virtual Network Identifier  or start of range
            	**type**\:  int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: vni_end  <key>
            
            	End of Virtual Network Identifier range  (make equal to vni\-start for single vni
            	**type**\:  int
            
            	**range:** 1..16777214
            
            	**mandatory**\: True
            
            .. attribute:: bgp
            
            	Use control protocol BGP to discover  peers
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: end_host_discovery
            
            	How to peform endpoint discovery
            	**type**\:   :py:class:`EndHostDiscoveryEnum <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscoveryEnum>`
            
            	**default value**\: flood-and-learn
            
            .. attribute:: multicast
            
            	Mulitcast group range associated  with the VxLAN segment(s)
            	**type**\:   :py:class:`Multicast <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Multicast>`
            
            .. attribute:: peers
            
            	List of VTEP peers
            	**type**\: list of    :py:class:`Peers <ydk.models.cisco_ios_xe.nvo.NvoInstances.NvoInstance.VirtualNetwork.Peers>`
            
            .. attribute:: routing_instance
            
            	VRF Name
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
            
            .. attribute:: suppress_arp
            
            	Enable ARP request suppression for this VNI
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nvo'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.vni_start = None
                self.vni_end = None
                self.bgp = None
                self.end_host_discovery = None
                self.multicast = NvoInstances.NvoInstance.VirtualNetwork.Multicast()
                self.multicast.parent = self
                self.peers = YList()
                self.peers.parent = self
                self.peers.name = 'peers'
                self.routing_instance = None
                self.suppress_arp = None

            class EndHostDiscoveryEnum(Enum):
                """
                EndHostDiscoveryEnum

                How to peform endpoint discovery

                .. data:: flood_and_learn = 0

                	Discover end-hosts using data plane 

                	              flood and learn

                .. data:: bgp = 1

                	Discover end-hosts using bgp-evpn

                """

                flood_and_learn = 0

                bgp = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _nvo as meta
                    return meta._meta_table['NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscoveryEnum']



            class Multicast(object):
                """
                Mulitcast group range associated 
                with the VxLAN segment(s)
                
                .. attribute:: multicast_group_max
                
                	End of IPV4 Multicast group  address (leave unspecified for single value
                	**type**\:  str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: multicast_group_min
                
                	Single IPV4 Multicast group  address or start of range
                	**type**\:  str
                
                	**pattern:** (2((2[4\-9])\|(3[0\-9]))\\.)(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){2}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.multicast_group_max = None
                    self.multicast_group_min = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/nvo:multicast'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.multicast_group_max is not None:
                        return True

                    if self.multicast_group_min is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _nvo as meta
                    return meta._meta_table['NvoInstances.NvoInstance.VirtualNetwork.Multicast']['meta_info']


            class Peers(object):
                """
                List of VTEP peers
                
                .. attribute:: peer_ip  <key>
                
                	VTEP peer IP address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'nvo'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.peer_ip = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.peer_ip is None:
                        raise YPYModelError('Key property peer_ip is None')

                    return self.parent._common_path +'/nvo:peers[nvo:peer-ip = ' + str(self.peer_ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer_ip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _nvo as meta
                    return meta._meta_table['NvoInstances.NvoInstance.VirtualNetwork.Peers']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.vni_start is None:
                    raise YPYModelError('Key property vni_start is None')
                if self.vni_end is None:
                    raise YPYModelError('Key property vni_end is None')

                return self.parent._common_path +'/nvo:virtual-network[nvo:vni-start = ' + str(self.vni_start) + '][nvo:vni-end = ' + str(self.vni_end) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vni_start is not None:
                    return True

                if self.vni_end is not None:
                    return True

                if self.bgp is not None:
                    return True

                if self.end_host_discovery is not None:
                    return True

                if self.multicast is not None and self.multicast._has_data():
                    return True

                if self.peers is not None:
                    for child_ref in self.peers:
                        if child_ref._has_data():
                            return True

                if self.routing_instance is not None:
                    return True

                if self.suppress_arp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _nvo as meta
                return meta._meta_table['NvoInstances.NvoInstance.VirtualNetwork']['meta_info']

        @property
        def _common_path(self):
            if self.nvo_id is None:
                raise YPYModelError('Key property nvo_id is None')

            return '/nvo:nvo-instances/nvo:nvo-instance[nvo:nvo-id = ' + str(self.nvo_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.nvo_id is not None:
                return True

            if self.overlay_encapsulation is not None:
                return True

            if self.source_interface is not None:
                return True

            if self.virtual_network is not None:
                for child_ref in self.virtual_network:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _nvo as meta
            return meta._meta_table['NvoInstances.NvoInstance']['meta_info']

    @property
    def _common_path(self):

        return '/nvo:nvo-instances'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.nvo_instance is not None:
            for child_ref in self.nvo_instance:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _nvo as meta
        return meta._meta_table['NvoInstances']['meta_info']


class NvgreTypeIdentity(OverlayEncapTypeIdentity):
    """
    This identity represents nvgre encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        OverlayEncapTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _nvo as meta
        return meta._meta_table['NvgreTypeIdentity']['meta_info']


class VxlanTypeIdentity(OverlayEncapTypeIdentity):
    """
    This identity represents vxlan encapsulation.
    
    

    """

    _prefix = 'nvo'
    _revision = '2015-06-02'

    def __init__(self):
        OverlayEncapTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _nvo as meta
        return meta._meta_table['VxlanTypeIdentity']['meta_info']


