""" Cisco_IOS_XR_subscriber_ipsub_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-ipsub package operational data.

This module contains definitions
for the following management objects\:
  ip\-subscriber\: IP subscriber operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IpsubMaIntfInitiatorDataEnum(Enum):
    """
    IpsubMaIntfInitiatorDataEnum

    Ipsub ma intf initiator data

    .. data:: dhcp = 0

    	Session creation via DHCP discover packet

    .. data:: packet_trigger = 1

    	Session creation via unclassified IPv4 packet

    .. data:: invalid_trigger = 2

    	Invalid Trigger

    """

    dhcp = 0

    packet_trigger = 1

    invalid_trigger = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
        return meta._meta_table['IpsubMaIntfInitiatorDataEnum']


class IpsubMaIntfStateDataEnum(Enum):
    """
    IpsubMaIntfStateDataEnum

    Interface states

    .. data:: invalid = 0

    	Invalid state

    .. data:: initialized = 1

    	Initial state

    .. data:: session_creation_started = 2

    	Interface creation started

    .. data:: control_policy_executing = 3

    	Interface created in IM, AAA session start

    	called

    .. data:: control_policy_executed = 4

    	AAA session created

    .. data:: session_features_applied = 5

    	Interface config activated

    .. data:: vrf_configured = 6

    	Interface address and VRF information received

    	from IPv4

    .. data:: adding_adjacency = 7

    	VRF configuration received and interface config

    	activated

    .. data:: adjacency_added = 8

    	Subscriber AIB adjacency added

    .. data:: up = 9

    	Session up

    .. data:: down = 10

    	Session down

    .. data:: address_family_down = 11

    	Session down in progress

    .. data:: address_family_down_complete = 12

    	Session down complete

    .. data:: disconnecting = 13

    	Session teardown in progress

    .. data:: disconnected = 14

    	Session disconnected

    .. data:: error = 15

    	Session in error state

    """

    invalid = 0

    initialized = 1

    session_creation_started = 2

    control_policy_executing = 3

    control_policy_executed = 4

    session_features_applied = 5

    vrf_configured = 6

    adding_adjacency = 7

    adjacency_added = 8

    up = 9

    down = 10

    address_family_down = 11

    address_family_down_complete = 12

    disconnecting = 13

    disconnected = 14

    error = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
        return meta._meta_table['IpsubMaIntfStateDataEnum']


class IpsubMaParentIntfStateDataEnum(Enum):
    """
    IpsubMaParentIntfStateDataEnum

    Parent interface state

    .. data:: deleted = 0

    	Interface being deleted

    .. data:: down = 1

    	Interface operationally down

    .. data:: up = 2

    	Interface up

    """

    deleted = 0

    down = 1

    up = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
        return meta._meta_table['IpsubMaParentIntfStateDataEnum']


class IpsubMaParentIntfVlanEnum(Enum):
    """
    IpsubMaParentIntfVlanEnum

    Access interface VLAN type

    .. data:: plain = 0

    	Plain

    .. data:: ambiguous = 1

    	Ambiguous

    """

    plain = 0

    ambiguous = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
        return meta._meta_table['IpsubMaParentIntfVlanEnum']



class IpSubscriber(object):
    """
    IP subscriber operational data
    
    .. attribute:: nodes
    
    	IP subscriber operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes>`
    
    

    """

    _prefix = 'subscriber-ipsub-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = IpSubscriber.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        IP subscriber operational data for a particular
        location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-ipsub-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: node_name  <key>
            
            	The node ID to filter on. For eg., 0/1/CPU0
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: access_interfaces
            
            	IP subscriber access interface table
            	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces>`
            
            .. attribute:: interfaces
            
            	IP subscriber interface table
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces>`
            
            .. attribute:: summary
            
            	IP subscriber interface summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'subscriber-ipsub-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.access_interfaces = IpSubscriber.Nodes.Node.AccessInterfaces()
                self.access_interfaces.parent = self
                self.interfaces = IpSubscriber.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.summary = IpSubscriber.Nodes.Node.Summary()
                self.summary.parent = self


            class Summary(object):
                """
                IP subscriber interface summary
                
                .. attribute:: access_interface_summary
                
                	Access interface summary statistics
                	**type**\:   :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary>`
                
                .. attribute:: interface_counts
                
                	Initiator interface counts
                	**type**\:   :py:class:`InterfaceCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts>`
                
                .. attribute:: vrf
                
                	Array of VRFs with IPSUB interfaces
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.Vrf>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_interface_summary = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary()
                    self.access_interface_summary.parent = self
                    self.interface_counts = IpSubscriber.Nodes.Node.Summary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class AccessInterfaceSummary(object):
                    """
                    Access interface summary statistics
                    
                    .. attribute:: initiators
                    
                    	Summary counts per initiator
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators>`
                    
                    .. attribute:: interfaces
                    
                    	Number of interfaces with subscriber configuration
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6_initiators
                    
                    	Summary counts per initiator for ipv6 session
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators()
                        self.initiators.parent = self
                        self.interfaces = None
                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators()
                        self.ipv6_initiators.parent = self


                    class Initiators(object):
                        """
                        Summary counts per initiator
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators']['meta_info']


                    class Ipv6Initiators(object):
                        """
                        Summary counts per initiator for ipv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP summary statistics
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger summary statistics
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            Packet trigger summary statistics
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:ipv6-initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:access-interface-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.initiators is not None and self.initiators._has_data():
                            return True

                        if self.interfaces is not None:
                            return True

                        if self.ipv6_initiators is not None and self.ipv6_initiators._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                        return meta._meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary']['meta_info']


                class InterfaceCounts(object):
                    """
                    Initiator interface counts
                    
                    .. attribute:: initiators
                    
                    	Initiators
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators>`
                    
                    .. attribute:: ipv6_initiators
                    
                    	IPv6 Initiators
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators()
                        self.initiators.parent = self
                        self.ipv6_initiators = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators()
                        self.ipv6_initiators.parent = self


                    class Initiators(object):
                        """
                        Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.control_policy_executed = None
                                self.control_policy_executing = None
                                self.disconnected = None
                                self.disconnecting = None
                                self.down = None
                                self.error = None
                                self.initialized = None
                                self.invalid = None
                                self.session_creation_started = None
                                self.session_features_applied = None
                                self.total_interfaces = None
                                self.up = None
                                self.vrf_configured = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.adding_adjacency is not None:
                                    return True

                                if self.adjacency_added is not None:
                                    return True

                                if self.control_policy_executed is not None:
                                    return True

                                if self.control_policy_executing is not None:
                                    return True

                                if self.disconnected is not None:
                                    return True

                                if self.disconnecting is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.error is not None:
                                    return True

                                if self.initialized is not None:
                                    return True

                                if self.invalid is not None:
                                    return True

                                if self.session_creation_started is not None:
                                    return True

                                if self.session_features_applied is not None:
                                    return True

                                if self.total_interfaces is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                if self.vrf_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            Packet trigger
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.control_policy_executed = None
                                self.control_policy_executing = None
                                self.disconnected = None
                                self.disconnecting = None
                                self.down = None
                                self.error = None
                                self.initialized = None
                                self.invalid = None
                                self.session_creation_started = None
                                self.session_features_applied = None
                                self.total_interfaces = None
                                self.up = None
                                self.vrf_configured = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.adding_adjacency is not None:
                                    return True

                                if self.adjacency_added is not None:
                                    return True

                                if self.control_policy_executed is not None:
                                    return True

                                if self.control_policy_executing is not None:
                                    return True

                                if self.disconnected is not None:
                                    return True

                                if self.disconnecting is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.error is not None:
                                    return True

                                if self.initialized is not None:
                                    return True

                                if self.invalid is not None:
                                    return True

                                if self.session_creation_started is not None:
                                    return True

                                if self.session_features_applied is not None:
                                    return True

                                if self.total_interfaces is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                if self.vrf_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators']['meta_info']


                    class Ipv6Initiators(object):
                        """
                        IPv6 Initiators
                        
                        .. attribute:: dhcp
                        
                        	DHCP
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	Packet trigger
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.control_policy_executed = None
                                self.control_policy_executing = None
                                self.disconnected = None
                                self.disconnecting = None
                                self.down = None
                                self.error = None
                                self.initialized = None
                                self.invalid = None
                                self.session_creation_started = None
                                self.session_features_applied = None
                                self.total_interfaces = None
                                self.up = None
                                self.vrf_configured = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.adding_adjacency is not None:
                                    return True

                                if self.adjacency_added is not None:
                                    return True

                                if self.control_policy_executed is not None:
                                    return True

                                if self.control_policy_executing is not None:
                                    return True

                                if self.disconnected is not None:
                                    return True

                                if self.disconnecting is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.error is not None:
                                    return True

                                if self.initialized is not None:
                                    return True

                                if self.invalid is not None:
                                    return True

                                if self.session_creation_started is not None:
                                    return True

                                if self.session_features_applied is not None:
                                    return True

                                if self.total_interfaces is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                if self.vrf_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            Packet trigger
                            
                            .. attribute:: adding_adjacency
                            
                            	Adding adjacency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjacency_added
                            
                            	Adjacency added
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executed
                            
                            	Control policy executed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_policy_executing
                            
                            	Control policy executing
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnected
                            
                            	Disconnected
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting
                            
                            	Disconnecting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error
                            
                            	Error
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized
                            
                            	Initialized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid
                            
                            	Invalid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_creation_started
                            
                            	Session creation started
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_features_applied
                            
                            	Session features applied
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_interfaces
                            
                            	Total number of interfaces in all states
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_configured
                            
                            	VRF configured
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.adding_adjacency = None
                                self.adjacency_added = None
                                self.control_policy_executed = None
                                self.control_policy_executing = None
                                self.disconnected = None
                                self.disconnecting = None
                                self.down = None
                                self.error = None
                                self.initialized = None
                                self.invalid = None
                                self.session_creation_started = None
                                self.session_features_applied = None
                                self.total_interfaces = None
                                self.up = None
                                self.vrf_configured = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.adding_adjacency is not None:
                                    return True

                                if self.adjacency_added is not None:
                                    return True

                                if self.control_policy_executed is not None:
                                    return True

                                if self.control_policy_executing is not None:
                                    return True

                                if self.disconnected is not None:
                                    return True

                                if self.disconnecting is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.error is not None:
                                    return True

                                if self.initialized is not None:
                                    return True

                                if self.invalid is not None:
                                    return True

                                if self.session_creation_started is not None:
                                    return True

                                if self.session_features_applied is not None:
                                    return True

                                if self.total_interfaces is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                if self.vrf_configured is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:ipv6-initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:interface-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.initiators is not None and self.initiators._has_data():
                            return True

                        if self.ipv6_initiators is not None and self.ipv6_initiators._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                        return meta._meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts']['meta_info']


                class Vrf(object):
                    """
                    Array of VRFs with IPSUB interfaces
                    
                    .. attribute:: interfaces
                    
                    	Number of IP subscriber interfaces in the VRF table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_interfaces
                    
                    	Number of IPv6 subscriber interfaces in the VRF table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6vrf_name
                    
                    	IPv6 VRF
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	IPv4 VRF
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interfaces = None
                        self.ipv6_interfaces = None
                        self.ipv6vrf_name = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:vrf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interfaces is not None:
                            return True

                        if self.ipv6_interfaces is not None:
                            return True

                        if self.ipv6vrf_name is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                        return meta._meta_table['IpSubscriber.Nodes.Node.Summary.Vrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_interface_summary is not None and self.access_interface_summary._has_data():
                        return True

                    if self.interface_counts is not None and self.interface_counts._has_data():
                        return True

                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                    return meta._meta_table['IpSubscriber.Nodes.Node.Summary']['meta_info']


            class Interfaces(object):
                """
                IP subscriber interface table
                
                .. attribute:: interface
                
                	IP subscriber interface entry
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    IP subscriber interface entry
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_interface
                    
                    	Access interface through which this subscriber is accessible
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: age
                    
                    	Age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: current_change_age
                    
                    	Current change age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: initiator
                    
                    	Protocol trigger for creation of this subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfInitiatorDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorDataEnum>`
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_current_change_age
                    
                    	IPV6 Current change age in hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_initiator
                    
                    	Protocol trigger for creation of this subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfInitiatorDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfInitiatorDataEnum>`
                    
                    .. attribute:: ipv6_last_state_change_time
                    
                    	Interface's IPV6 last state change time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: ipv6_old_state
                    
                    	Previous state of the subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateDataEnum>`
                    
                    .. attribute:: ipv6_state
                    
                    	State of the subscriber's IPv6 session
                    	**type**\:   :py:class:`IpsubMaIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateDataEnum>`
                    
                    .. attribute:: ipv6vrf
                    
                    	IPv6 VRF details
                    	**type**\:   :py:class:`Ipv6Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf>`
                    
                    .. attribute:: is_l2_connected
                    
                    	True if L2 connected
                    	**type**\:  bool
                    
                    .. attribute:: last_state_change_time
                    
                    	Interface's last state change time in month day hh\:mm\:ss format
                    	**type**\:  str
                    
                    .. attribute:: old_state
                    
                    	Previous state of the subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateDataEnum>`
                    
                    .. attribute:: session_type
                    
                    	Session Type
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	State of the subscriber session
                    	**type**\:   :py:class:`IpsubMaIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaIntfStateDataEnum>`
                    
                    .. attribute:: subscriber_ipv4_address
                    
                    	IPv4 Address of the subscriber
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: subscriber_ipv6_address
                    
                    	IPv6 Address of the subscriber
                    	**type**\:  str
                    
                    .. attribute:: subscriber_label
                    
                    	Subscriber label for this subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscriber_mac_addres
                    
                    	MAC address of the subscriber
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: vrf
                    
                    	IPv4 VRF details
                    	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.access_interface = None
                        self.age = None
                        self.current_change_age = None
                        self.initiator = None
                        self.interface_creation_time = None
                        self.ipv6_current_change_age = None
                        self.ipv6_initiator = None
                        self.ipv6_last_state_change_time = None
                        self.ipv6_old_state = None
                        self.ipv6_state = None
                        self.ipv6vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf()
                        self.ipv6vrf.parent = self
                        self.is_l2_connected = None
                        self.last_state_change_time = None
                        self.old_state = None
                        self.session_type = None
                        self.state = None
                        self.subscriber_ipv4_address = None
                        self.subscriber_ipv6_address = None
                        self.subscriber_label = None
                        self.subscriber_mac_addres = None
                        self.vrf = IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf()
                        self.vrf.parent = self


                    class Vrf(object):
                        """
                        IPv4 VRF details
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.table_name = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:vrf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.table_name is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf']['meta_info']


                    class Ipv6Vrf(object):
                        """
                        IPv6 VRF details
                        
                        .. attribute:: table_name
                        
                        	Table
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.table_name = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:ipv6vrf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.table_name is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:interface[Cisco-IOS-XR-subscriber-ipsub-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.access_interface is not None:
                            return True

                        if self.age is not None:
                            return True

                        if self.current_change_age is not None:
                            return True

                        if self.initiator is not None:
                            return True

                        if self.interface_creation_time is not None:
                            return True

                        if self.ipv6_current_change_age is not None:
                            return True

                        if self.ipv6_initiator is not None:
                            return True

                        if self.ipv6_last_state_change_time is not None:
                            return True

                        if self.ipv6_old_state is not None:
                            return True

                        if self.ipv6_state is not None:
                            return True

                        if self.ipv6vrf is not None and self.ipv6vrf._has_data():
                            return True

                        if self.is_l2_connected is not None:
                            return True

                        if self.last_state_change_time is not None:
                            return True

                        if self.old_state is not None:
                            return True

                        if self.session_type is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.subscriber_ipv4_address is not None:
                            return True

                        if self.subscriber_ipv6_address is not None:
                            return True

                        if self.subscriber_label is not None:
                            return True

                        if self.subscriber_mac_addres is not None:
                            return True

                        if self.vrf is not None and self.vrf._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                        return meta._meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                    return meta._meta_table['IpSubscriber.Nodes.Node.Interfaces']['meta_info']


            class AccessInterfaces(object):
                """
                IP subscriber access interface table
                
                .. attribute:: access_interface
                
                	IP subscriber access interface entry
                	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface>`
                
                

                """

                _prefix = 'subscriber-ipsub-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_interface = YList()
                    self.access_interface.parent = self
                    self.access_interface.name = 'access_interface'


                class AccessInterface(object):
                    """
                    IP subscriber access interface entry
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: age
                    
                    	Age in HH\:MM\:SS format
                    	**type**\:  str
                    
                    .. attribute:: initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface
                    	**type**\:   :py:class:`Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators>`
                    
                    .. attribute:: interface_creation_time
                    
                    	Interface creation time in Month Date HH\:MM\:SS format
                    	**type**\:  str
                    
                    .. attribute:: interface_type
                    
                    	Interface Type
                    	**type**\:  str
                    
                    .. attribute:: ipv6_initiators
                    
                    	Configurational state\-statistics for each initiating protocol enabled on this parent interface for IPv6 session
                    	**type**\:   :py:class:`Ipv6Initiators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators>`
                    
                    .. attribute:: ipv6_state
                    
                    	Operational ipv6 state of this interface
                    	**type**\:   :py:class:`IpsubMaParentIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateDataEnum>`
                    
                    .. attribute:: session_limit
                    
                    	Configuration session limits for each session limit source and type
                    	**type**\:   :py:class:`SessionLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit>`
                    
                    .. attribute:: state
                    
                    	Operational state of this interface
                    	**type**\:   :py:class:`IpsubMaParentIntfStateDataEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfStateDataEnum>`
                    
                    .. attribute:: vlan_type
                    
                    	The VLAN type on the access interface
                    	**type**\:   :py:class:`IpsubMaParentIntfVlanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpsubMaParentIntfVlanEnum>`
                    
                    

                    """

                    _prefix = 'subscriber-ipsub-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.age = None
                        self.initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators()
                        self.initiators.parent = self
                        self.interface_creation_time = None
                        self.interface_type = None
                        self.ipv6_initiators = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators()
                        self.ipv6_initiators.parent = self
                        self.ipv6_state = None
                        self.session_limit = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit()
                        self.session_limit.parent = self
                        self.state = None
                        self.vlan_type = None


                    class Initiators(object):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_packets_dup_addr = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_packets = None
                                self.is_configured = None
                                self.sessions = None
                                self.unique_ip_check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_dropped_bytes is not None:
                                    return True

                                if self.fsol_dropped_packets is not None:
                                    return True

                                if self.fsol_dropped_packets_dup_addr is not None:
                                    return True

                                if self.fsol_dropped_packets_flow is not None:
                                    return True

                                if self.fsol_dropped_packets_session_limit is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                if self.is_configured is not None:
                                    return True

                                if self.sessions is not None:
                                    return True

                                if self.unique_ip_check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            packet trigger information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_packets_dup_addr = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_packets = None
                                self.is_configured = None
                                self.sessions = None
                                self.unique_ip_check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_dropped_bytes is not None:
                                    return True

                                if self.fsol_dropped_packets is not None:
                                    return True

                                if self.fsol_dropped_packets_dup_addr is not None:
                                    return True

                                if self.fsol_dropped_packets_flow is not None:
                                    return True

                                if self.fsol_dropped_packets_session_limit is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                if self.is_configured is not None:
                                    return True

                                if self.sessions is not None:
                                    return True

                                if self.unique_ip_check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators']['meta_info']


                    class Ipv6Initiators(object):
                        """
                        Configurational state\-statistics for each
                        initiating protocol enabled on this parent
                        interface for IPv6 session
                        
                        .. attribute:: dhcp
                        
                        	DHCP information
                        	**type**\:   :py:class:`Dhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp>`
                        
                        .. attribute:: packet_trigger
                        
                        	packet trigger information
                        	**type**\:   :py:class:`PacketTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dhcp = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp()
                            self.dhcp.parent = self
                            self.packet_trigger = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger()
                            self.packet_trigger.parent = self


                        class Dhcp(object):
                            """
                            DHCP information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_packets_dup_addr = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_packets = None
                                self.is_configured = None
                                self.sessions = None
                                self.unique_ip_check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_dropped_bytes is not None:
                                    return True

                                if self.fsol_dropped_packets is not None:
                                    return True

                                if self.fsol_dropped_packets_dup_addr is not None:
                                    return True

                                if self.fsol_dropped_packets_flow is not None:
                                    return True

                                if self.fsol_dropped_packets_session_limit is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                if self.is_configured is not None:
                                    return True

                                if self.sessions is not None:
                                    return True

                                if self.unique_ip_check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp']['meta_info']


                        class PacketTrigger(object):
                            """
                            packet trigger information
                            
                            .. attribute:: fsol_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_bytes
                            
                            	Number of first sign of life bytes received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: fsol_dropped_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_dup_addr
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to duplicate source address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_flow
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding creation rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_dropped_packets_session_limit
                            
                            	Number of first sign of life packets received for initiating protocol on this interface that were dropped due to exceeding one or more of the configured session limits
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: fsol_packets
                            
                            	Number of first sign of life packets received for initiating protocol on this interface
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_configured
                            
                            	Ture if the initiator is configred
                            	**type**\:  bool
                            
                            .. attribute:: sessions
                            
                            	Number of sessions currently up for each initiator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unique_ip_check
                            
                            	True if check for subscriber address uniquenessduring first sign of life is enabled
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fsol_bytes = None
                                self.fsol_dropped_bytes = None
                                self.fsol_dropped_packets = None
                                self.fsol_dropped_packets_dup_addr = None
                                self.fsol_dropped_packets_flow = None
                                self.fsol_dropped_packets_session_limit = None
                                self.fsol_packets = None
                                self.is_configured = None
                                self.sessions = None
                                self.unique_ip_check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:packet-trigger'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fsol_bytes is not None:
                                    return True

                                if self.fsol_dropped_bytes is not None:
                                    return True

                                if self.fsol_dropped_packets is not None:
                                    return True

                                if self.fsol_dropped_packets_dup_addr is not None:
                                    return True

                                if self.fsol_dropped_packets_flow is not None:
                                    return True

                                if self.fsol_dropped_packets_session_limit is not None:
                                    return True

                                if self.fsol_packets is not None:
                                    return True

                                if self.is_configured is not None:
                                    return True

                                if self.sessions is not None:
                                    return True

                                if self.unique_ip_check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:ipv6-initiators'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dhcp is not None and self.dhcp._has_data():
                                return True

                            if self.packet_trigger is not None and self.packet_trigger._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators']['meta_info']


                    class SessionLimit(object):
                        """
                        Configuration session limits for each session
                        limit source and type
                        
                        .. attribute:: total
                        
                        	All sources session limits
                        	**type**\:   :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total>`
                        
                        .. attribute:: unclassified_source
                        
                        	Unclassified source session limits
                        	**type**\:   :py:class:`UnclassifiedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper.IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource>`
                        
                        

                        """

                        _prefix = 'subscriber-ipsub-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.total = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total()
                            self.total.parent = self
                            self.unclassified_source = IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource()
                            self.unclassified_source.parent = self


                        class UnclassifiedSource(object):
                            """
                            Unclassified source session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.per_vlan = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:unclassified-source'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.per_vlan is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource']['meta_info']


                        class Total(object):
                            """
                            All sources session limits
                            
                            .. attribute:: per_vlan
                            
                            	Per\-VLAN limit category
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-ipsub-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.per_vlan = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:total'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.per_vlan is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                                return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:session-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.total is not None and self.total._has_data():
                                return True

                            if self.unclassified_source is not None and self.unclassified_source._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                            return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:access-interface[Cisco-IOS-XR-subscriber-ipsub-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.age is not None:
                            return True

                        if self.initiators is not None and self.initiators._has_data():
                            return True

                        if self.interface_creation_time is not None:
                            return True

                        if self.interface_type is not None:
                            return True

                        if self.ipv6_initiators is not None and self.ipv6_initiators._has_data():
                            return True

                        if self.ipv6_state is not None:
                            return True

                        if self.session_limit is not None and self.session_limit._has_data():
                            return True

                        if self.state is not None:
                            return True

                        if self.vlan_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                        return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-ipsub-oper:access-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_interface is not None:
                        for child_ref in self.access_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                    return meta._meta_table['IpSubscriber.Nodes.Node.AccessInterfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/Cisco-IOS-XR-subscriber-ipsub-oper:nodes/Cisco-IOS-XR-subscriber-ipsub-oper:node[Cisco-IOS-XR-subscriber-ipsub-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.access_interfaces is not None and self.access_interfaces._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
                return meta._meta_table['IpSubscriber.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber/Cisco-IOS-XR-subscriber-ipsub-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
            return meta._meta_table['IpSubscriber.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-ipsub-oper:ip-subscriber'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_ipsub_oper as meta
        return meta._meta_table['IpSubscriber']['meta_info']


