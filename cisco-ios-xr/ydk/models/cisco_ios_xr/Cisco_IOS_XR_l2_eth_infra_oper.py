""" Cisco_IOS_XR_l2_eth_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package operational data.

This module contains definitions
for the following management objects\:
  mac\-accounting\: MAC accounting operational data
  vlan\: vlan
  ethernet\-encapsulation\: ethernet encapsulation

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EfpPayloadEtypeEnum(Enum):
    """
    EfpPayloadEtypeEnum

    Payload ethertype match

    .. data:: payload_ethertype_any = 0

    	Any

    .. data:: payload_ethertype_ip = 1

    	IP

    .. data:: payload_ethertype_pppoe = 2

    	PPPoE

    """

    payload_ethertype_any = 0

    payload_ethertype_ip = 1

    payload_ethertype_pppoe = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EfpPayloadEtypeEnum']


class EfpTagEtypeEnum(Enum):
    """
    EfpTagEtypeEnum

    Tag ethertype

    .. data:: untagged = 0

    	Untagged

    .. data:: dot1q = 33024

    	Dot1Q

    .. data:: dot1ad = 34984

    	Dot1ad

    """

    untagged = 0

    dot1q = 33024

    dot1ad = 34984


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EfpTagEtypeEnum']


class EfpTagPriorityEnum(Enum):
    """
    EfpTagPriorityEnum

    Priority

    .. data:: priority0 = 0

    	Priority 0

    .. data:: priority1 = 1

    	Priority 1

    .. data:: priority2 = 2

    	Priority 2

    .. data:: priority3 = 3

    	Priority 3

    .. data:: priority4 = 4

    	Priority 4

    .. data:: priority5 = 5

    	Priority 5

    .. data:: priority6 = 6

    	Priority 6

    .. data:: priority7 = 7

    	Priority 7

    .. data:: priority_any = 8

    	Any priority

    """

    priority0 = 0

    priority1 = 1

    priority2 = 2

    priority3 = 3

    priority4 = 4

    priority5 = 5

    priority6 = 6

    priority7 = 7

    priority_any = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EfpTagPriorityEnum']


class EthCapsUcastMacModeEnum(Enum):
    """
    EthCapsUcastMacModeEnum

    Eth caps ucast mac mode

    .. data:: reserved = 0

    	Reserved

    .. data:: permit = 1

    	Permit

    """

    reserved = 0

    permit = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EthCapsUcastMacModeEnum']


class EthFilteringEnum(Enum):
    """
    EthFilteringEnum

    Ethernet frame filtering

    .. data:: no_filtering = 0

    	No IEEE 802.1Q/802.1ad/MAC relay multicast MAC

    	address filtering

    .. data:: dot1q_filtering = 1

    	IEEE 802.1q C-VLAN filtering

    .. data:: dot1ad_filtering = 2

    	IEEE 802.1ad S-VLAN filtering

    .. data:: two_port_mac_relay_filtering = 3

    	IEEE 802.1aj 2-Port MAC relay filtering

    """

    no_filtering = 0

    dot1q_filtering = 1

    dot1ad_filtering = 2

    two_port_mac_relay_filtering = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EthFilteringEnum']


class ImStateEnumEnum(Enum):
    """
    ImStateEnumEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = 0

    im_state_admin_down = 1

    im_state_down = 2

    im_state_up = 3

    im_state_shutdown = 4

    im_state_err_disable = 5

    im_state_down_immediate = 6

    im_state_down_immediate_admin = 7

    im_state_down_graceful = 8

    im_state_begin_shutdown = 9

    im_state_end_shutdown = 10

    im_state_begin_error_disable = 11

    im_state_end_error_disable = 12

    im_state_begin_down_graceful = 13

    im_state_reset = 14

    im_state_operational = 15

    im_state_not_operational = 16

    im_state_unknown = 17

    im_state_last = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['ImStateEnumEnum']


class VlanEncapsEnum(Enum):
    """
    VlanEncapsEnum

    VLAN encapsulation

    .. data:: no_encapsulation = 0

    	No encapsulation

    .. data:: dot1q = 1

    	IEEE 802.1Q encapsulation

    .. data:: qinq = 2

    	Double 802.1Q encapsulation

    .. data:: qin_any = 3

    	Double 802.1Q wildcarded encapsulation

    .. data:: dot1q_native = 4

    	IEEE 802.1Q native VLAN encapsulation

    .. data:: dot1ad = 5

    	IEEE 802.1ad encapsulation

    .. data:: dot1ad_native = 6

    	IEEE 802.1ad native VLAN encapsulation

    .. data:: service_instance = 7

    	Ethernet Service Instance

    .. data:: dot1ad_dot1q = 8

    	IEEE 802.1ad 802.1Q encapsulation

    .. data:: dot1ad_any = 9

    	IEEE 802.1ad wildcard 802.1Q encapsulation

    """

    no_encapsulation = 0

    dot1q = 1

    qinq = 2

    qin_any = 3

    dot1q_native = 4

    dot1ad = 5

    dot1ad_native = 6

    service_instance = 7

    dot1ad_dot1q = 8

    dot1ad_any = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['VlanEncapsEnum']


class VlanQinqOuterEtypeEnum(Enum):
    """
    VlanQinqOuterEtypeEnum

    QinQ Outer Tag Ethertype

    .. data:: ether_type8100 = 33024

    	Dot1Q (0x8100)

    .. data:: ether_type9100 = 37120

    	0x9100

    .. data:: ether_type9200 = 37376

    	0x9200

    """

    ether_type8100 = 33024

    ether_type9100 = 37120

    ether_type9200 = 37376


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['VlanQinqOuterEtypeEnum']


class VlanServiceEnum(Enum):
    """
    VlanServiceEnum

    Layer 2 vs. Layer 3 Terminated Service

    .. data:: vlan_service_l2 = 1

    	Layer 2 Transport Service

    .. data:: vlan_service_l3 = 2

    	Layer 3 Terminated Service

    """

    vlan_service_l2 = 1

    vlan_service_l3 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['VlanServiceEnum']



class MacAccounting(object):
    """
    MAC accounting operational data
    
    .. attribute:: interfaces
    
    	MAC accounting interface table in MIB lexicographic order
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.interfaces = MacAccounting.Interfaces()
        self.interfaces.parent = self


    class Interfaces(object):
        """
        MAC accounting interface table in MIB
        lexicographic order
        
        .. attribute:: interface
        
        	Operational data and statistics for an interface configured with MAC accounting enabled
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Operational data and statistics for an
            interface configured with MAC accounting
            enabled
            
            .. attribute:: interface_name  <key>
            
            	The interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: egress_statistic
            
            	Egress MAC accounting statistics
            	**type**\: list of    :py:class:`EgressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.EgressStatistic>`
            
            .. attribute:: ingress_statistic
            
            	Ingress MAC accounting statistics
            	**type**\: list of    :py:class:`IngressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.IngressStatistic>`
            
            .. attribute:: state
            
            	MAC accounting state for the interface
            	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.State>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.egress_statistic = YList()
                self.egress_statistic.parent = self
                self.egress_statistic.name = 'egress_statistic'
                self.ingress_statistic = YList()
                self.ingress_statistic.parent = self
                self.ingress_statistic.name = 'ingress_statistic'
                self.state = MacAccounting.Interfaces.Interface.State()
                self.state.parent = self


            class State(object):
                """
                MAC accounting state for the interface
                
                .. attribute:: is_egress_enabled
                
                	MAC accounting on on egress
                	**type**\:  bool
                
                .. attribute:: is_ingress_enabled
                
                	MAC accounting on on ingress
                	**type**\:  bool
                
                .. attribute:: number_available_egress
                
                	MAC accounting entries available on egress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_ingress
                
                	MAC accounting entries available on ingress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_on_node
                
                	MAC accountng entries available across the node
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.is_egress_enabled = None
                    self.is_ingress_enabled = None
                    self.number_available_egress = None
                    self.number_available_ingress = None
                    self.number_available_on_node = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.is_egress_enabled is not None:
                        return True

                    if self.is_ingress_enabled is not None:
                        return True

                    if self.number_available_egress is not None:
                        return True

                    if self.number_available_ingress is not None:
                        return True

                    if self.number_available_on_node is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['MacAccounting.Interfaces.Interface.State']['meta_info']


            class IngressStatistic(object):
                """
                Ingress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.mac_address = None
                    self.packets = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:ingress-statistic'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['MacAccounting.Interfaces.Interface.IngressStatistic']['meta_info']


            class EgressStatistic(object):
                """
                Egress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bytes = None
                    self.mac_address = None
                    self.packets = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:egress-statistic'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bytes is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['MacAccounting.Interfaces.Interface.EgressStatistic']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/Cisco-IOS-XR-l2-eth-infra-oper:interfaces/Cisco-IOS-XR-l2-eth-infra-oper:interface[Cisco-IOS-XR-l2-eth-infra-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.egress_statistic is not None:
                    for child_ref in self.egress_statistic:
                        if child_ref._has_data():
                            return True

                if self.ingress_statistic is not None:
                    for child_ref in self.ingress_statistic:
                        if child_ref._has_data():
                            return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                return meta._meta_table['MacAccounting.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/Cisco-IOS-XR-l2-eth-infra-oper:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
            return meta._meta_table['MacAccounting.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['MacAccounting']['meta_info']


class Vlan(object):
    """
    vlan
    
    .. attribute:: nodes
    
    	Per node VLAN operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Vlan.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Per node VLAN operational data
        
        .. attribute:: node
        
        	The VLAN operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The VLAN operational data for a particular node
            
            .. attribute:: node_id  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	VLAN interface table (specific to this node)
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces>`
            
            .. attribute:: tag_allocations
            
            	VLAN tag allocation table (specific to this node)
            	**type**\:   :py:class:`TagAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations>`
            
            .. attribute:: trunks
            
            	VLAN trunk table (specific to this node)
            	**type**\:   :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_id = None
                self.interfaces = Vlan.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.tag_allocations = Vlan.Nodes.Node.TagAllocations()
                self.tag_allocations.parent = self
                self.trunks = Vlan.Nodes.Node.Trunks()
                self.trunks.parent = self


            class Trunks(object):
                """
                VLAN trunk table (specific to this node)
                
                .. attribute:: trunk
                
                	Operational data for trunk interfaces configured with VLANs
                	**type**\: list of    :py:class:`Trunk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.trunk = YList()
                    self.trunk.parent = self
                    self.trunk.name = 'trunk'


                class Trunk(object):
                    """
                    Operational data for trunk interfaces
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: dot1ad_count
                    
                    	Number of subinterfaces with 802.1ad outer tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: layer2_sub_interfaces
                    
                    	Layer 2 Transport Subinterfaces
                    	**type**\:   :py:class:`Layer2SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces>`
                    
                    .. attribute:: layer3_sub_interfaces
                    
                    	Layer 3 Terminated Subinterfaces
                    	**type**\:   :py:class:`Layer3SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces>`
                    
                    .. attribute:: mac_filtering
                    
                    	IEEE 802.1Q/802.1ad multicast MAC address filtering
                    	**type**\:   :py:class:`EthFilteringEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthFilteringEnum>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: qinq_outer_ether_type
                    
                    	QinQ Outer Tag Ether Type
                    	**type**\:   :py:class:`VlanQinqOuterEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanQinqOuterEtypeEnum>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnumEnum>`
                    
                    .. attribute:: untagged_interface
                    
                    	Interface/Sub\-interface handling untagged frames
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.dot1ad_count = None
                        self.interface_xr = None
                        self.layer2_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces()
                        self.layer2_sub_interfaces.parent = self
                        self.layer3_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces()
                        self.layer3_sub_interfaces.parent = self
                        self.mac_filtering = None
                        self.mtu = None
                        self.qinq_outer_ether_type = None
                        self.state = None
                        self.untagged_interface = None


                    class Layer2SubInterfaces(object):
                        """
                        Layer 2 Transport Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_any_count
                        
                        	Number of double tagged subinterfaces with wildcarded inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces with explicit inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 2 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dot1q_count = None
                            self.qin_any_count = None
                            self.qin_q_count = None
                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self.total_count = None
                            self.untagged_count = None


                        class StateCounters(object):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_down = None
                                self.down = None
                                self.up = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:state-counters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_down is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:layer2-sub-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dot1q_count is not None:
                                return True

                            if self.qin_any_count is not None:
                                return True

                            if self.qin_q_count is not None:
                                return True

                            if self.state_counters is not None and self.state_counters._has_data():
                                return True

                            if self.total_count is not None:
                                return True

                            if self.untagged_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                            return meta._meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces']['meta_info']


                    class Layer3SubInterfaces(object):
                        """
                        Layer 3 Terminated Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: native_vlan
                        
                        	Native VLAN ID configured on trunk
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 3 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dot1q_count = None
                            self.native_vlan = None
                            self.qin_q_count = None
                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self.total_count = None
                            self.untagged_count = None


                        class StateCounters(object):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_down = None
                                self.down = None
                                self.up = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:state-counters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.admin_down is not None:
                                    return True

                                if self.down is not None:
                                    return True

                                if self.up is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:layer3-sub-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dot1q_count is not None:
                                return True

                            if self.native_vlan is not None:
                                return True

                            if self.qin_q_count is not None:
                                return True

                            if self.state_counters is not None and self.state_counters._has_data():
                                return True

                            if self.total_count is not None:
                                return True

                            if self.untagged_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                            return meta._meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:trunk[Cisco-IOS-XR-l2-eth-infra-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.dot1ad_count is not None:
                            return True

                        if self.interface_xr is not None:
                            return True

                        if self.layer2_sub_interfaces is not None and self.layer2_sub_interfaces._has_data():
                            return True

                        if self.layer3_sub_interfaces is not None and self.layer3_sub_interfaces._has_data():
                            return True

                        if self.mac_filtering is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        if self.qinq_outer_ether_type is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.untagged_interface is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                        return meta._meta_table['Vlan.Nodes.Node.Trunks.Trunk']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:trunks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.trunk is not None:
                        for child_ref in self.trunk:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['Vlan.Nodes.Node.Trunks']['meta_info']


            class Interfaces(object):
                """
                VLAN interface table (specific to this node)
                
                .. attribute:: interface
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanServiceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanServiceEnum>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnumEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.encapsulation_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self.interface_xr = None
                        self.mtu = None
                        self.parent_interface = None
                        self.service = None
                        self.state = None
                        self.switched_mtu = None


                    class EncapsulationDetails(object):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncapsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncapsEnum>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None
                            self.dot1ad_tag = None
                            self.native_tag = None
                            self.outer_tag = None
                            self.service_instance_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self.stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self.tag = None
                            self.vlan_encapsulation = None


                        class Stack(object):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack']['meta_info']


                        class ServiceInstanceDetails(object):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtypeEnum>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.destination_mac_match = None
                                self.is_exact_match = None
                                self.is_native_preserving = None
                                self.is_native_vlan = None
                                self.local_traffic_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self.payload_ethertype = None
                                self.pushe = YList()
                                self.pushe.parent = self
                                self.pushe.name = 'pushe'
                                self.source_mac_match = None
                                self.tags_popped = None
                                self.tags_to_match = YList()
                                self.tags_to_match.parent = self
                                self.tags_to_match.name = 'tags_to_match'


                            class LocalTrafficStack(object):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.local_traffic_tag = YList()
                                    self.local_traffic_tag.parent = self
                                    self.local_traffic_tag.name = 'local_traffic_tag'


                                class LocalTrafficTag(object):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ethertype = None
                                        self.vlan_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:local-traffic-tag'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.ethertype is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                        return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:local-traffic-stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.local_traffic_tag is not None:
                                        for child_ref in self.local_traffic_tag:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']


                            class TagsToMatch(object):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriorityEnum>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.priority = None
                                    self.vlan_range = YList()
                                    self.vlan_range.parent = self
                                    self.vlan_range.name = 'vlan_range'


                                class VlanRange(object):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vlan_id_high = None
                                        self.vlan_id_low = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:vlan-range'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.vlan_id_high is not None:
                                            return True

                                        if self.vlan_id_low is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                        return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:tags-to-match'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.vlan_range is not None:
                                        for child_ref in self.vlan_range:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']


                            class Pushe(object):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.vlan_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:pushe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:service-instance-details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.destination_mac_match is not None:
                                    return True

                                if self.is_exact_match is not None:
                                    return True

                                if self.is_native_preserving is not None:
                                    return True

                                if self.is_native_vlan is not None:
                                    return True

                                if self.local_traffic_stack is not None and self.local_traffic_stack._has_data():
                                    return True

                                if self.payload_ethertype is not None:
                                    return True

                                if self.pushe is not None:
                                    for child_ref in self.pushe:
                                        if child_ref._has_data():
                                            return True

                                if self.source_mac_match is not None:
                                    return True

                                if self.tags_popped is not None:
                                    return True

                                if self.tags_to_match is not None:
                                    for child_ref in self.tags_to_match:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails']['meta_info']


                        class Dot1AdDot1QStack(object):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:dot1ad-dot1q-stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:encapsulation-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack._has_data():
                                return True

                            if self.dot1ad_native_tag is not None:
                                return True

                            if self.dot1ad_outer_tag is not None:
                                return True

                            if self.dot1ad_tag is not None:
                                return True

                            if self.native_tag is not None:
                                return True

                            if self.outer_tag is not None:
                                return True

                            if self.service_instance_details is not None and self.service_instance_details._has_data():
                                return True

                            if self.stack is not None and self.stack._has_data():
                                return True

                            if self.tag is not None:
                                return True

                            if self.vlan_encapsulation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                            return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:interface[Cisco-IOS-XR-l2-eth-infra-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.encapsulation_details is not None and self.encapsulation_details._has_data():
                            return True

                        if self.interface_xr is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        if self.parent_interface is not None:
                            return True

                        if self.service is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.switched_mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                        return meta._meta_table['Vlan.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['Vlan.Nodes.Node.Interfaces']['meta_info']


            class TagAllocations(object):
                """
                VLAN tag allocation table (specific to this
                node)
                
                .. attribute:: tag_allocation
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`TagAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tag_allocation = YList()
                    self.tag_allocation.parent = self
                    self.tag_allocation.name = 'tag_allocation'


                class TagAllocation(object):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails>`
                    
                    .. attribute:: first_tag
                    
                    	The first (outermost) tag
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: interface
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: second_tag
                    
                    	The second tag
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`VlanTagOrAnyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes.VlanTagOrAnyEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 1..4096
                    
                    
                    ----
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanServiceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanServiceEnum>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnumEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.encapsulation_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self.first_tag = None
                        self.interface = None
                        self.interface_xr = None
                        self.mtu = None
                        self.parent_interface = None
                        self.second_tag = None
                        self.service = None
                        self.state = None
                        self.switched_mtu = None


                    class EncapsulationDetails(object):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncapsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncapsEnum>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None
                            self.dot1ad_tag = None
                            self.native_tag = None
                            self.outer_tag = None
                            self.service_instance_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self.stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self.tag = None
                            self.vlan_encapsulation = None


                        class Stack(object):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack']['meta_info']


                        class ServiceInstanceDetails(object):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtypeEnum>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.destination_mac_match = None
                                self.is_exact_match = None
                                self.is_native_preserving = None
                                self.is_native_vlan = None
                                self.local_traffic_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self.payload_ethertype = None
                                self.pushe = YList()
                                self.pushe.parent = self
                                self.pushe.name = 'pushe'
                                self.source_mac_match = None
                                self.tags_popped = None
                                self.tags_to_match = YList()
                                self.tags_to_match.parent = self
                                self.tags_to_match.name = 'tags_to_match'


                            class LocalTrafficStack(object):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.local_traffic_tag = YList()
                                    self.local_traffic_tag.parent = self
                                    self.local_traffic_tag.name = 'local_traffic_tag'


                                class LocalTrafficTag(object):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ethertype = None
                                        self.vlan_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:local-traffic-tag'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.ethertype is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                        return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:local-traffic-stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.local_traffic_tag is not None:
                                        for child_ref in self.local_traffic_tag:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']


                            class TagsToMatch(object):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriorityEnum>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.priority = None
                                    self.vlan_range = YList()
                                    self.vlan_range.parent = self
                                    self.vlan_range.name = 'vlan_range'


                                class VlanRange(object):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vlan_id_high = None
                                        self.vlan_id_low = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:vlan-range'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.vlan_id_high is not None:
                                            return True

                                        if self.vlan_id_low is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                        return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:tags-to-match'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.vlan_range is not None:
                                        for child_ref in self.vlan_range:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']


                            class Pushe(object):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtypeEnum>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.vlan_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:pushe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ethertype is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                    return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:service-instance-details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.destination_mac_match is not None:
                                    return True

                                if self.is_exact_match is not None:
                                    return True

                                if self.is_native_preserving is not None:
                                    return True

                                if self.is_native_vlan is not None:
                                    return True

                                if self.local_traffic_stack is not None and self.local_traffic_stack._has_data():
                                    return True

                                if self.payload_ethertype is not None:
                                    return True

                                if self.pushe is not None:
                                    for child_ref in self.pushe:
                                        if child_ref._has_data():
                                            return True

                                if self.source_mac_match is not None:
                                    return True

                                if self.tags_popped is not None:
                                    return True

                                if self.tags_to_match is not None:
                                    for child_ref in self.tags_to_match:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']


                        class Dot1AdDot1QStack(object):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:dot1ad-dot1q-stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                                return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:encapsulation-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack._has_data():
                                return True

                            if self.dot1ad_native_tag is not None:
                                return True

                            if self.dot1ad_outer_tag is not None:
                                return True

                            if self.dot1ad_tag is not None:
                                return True

                            if self.native_tag is not None:
                                return True

                            if self.outer_tag is not None:
                                return True

                            if self.service_instance_details is not None and self.service_instance_details._has_data():
                                return True

                            if self.stack is not None and self.stack._has_data():
                                return True

                            if self.tag is not None:
                                return True

                            if self.vlan_encapsulation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                            return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:tag-allocation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.encapsulation_details is not None and self.encapsulation_details._has_data():
                            return True

                        if self.first_tag is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.interface_xr is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        if self.parent_interface is not None:
                            return True

                        if self.second_tag is not None:
                            return True

                        if self.service is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.switched_mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                        return meta._meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:tag-allocations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.tag_allocation is not None:
                        for child_ref in self.tag_allocation:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['Vlan.Nodes.Node.TagAllocations']['meta_info']

            @property
            def _common_path(self):
                if self.node_id is None:
                    raise YPYModelError('Key property node_id is None')

                return '/Cisco-IOS-XR-l2-eth-infra-oper:vlan/Cisco-IOS-XR-l2-eth-infra-oper:nodes/Cisco-IOS-XR-l2-eth-infra-oper:node[Cisco-IOS-XR-l2-eth-infra-oper:node-id = ' + str(self.node_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_id is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.tag_allocations is not None and self.tag_allocations._has_data():
                    return True

                if self.trunks is not None and self.trunks._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                return meta._meta_table['Vlan.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-oper:vlan/Cisco-IOS-XR-l2-eth-infra-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
            return meta._meta_table['Vlan.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2-eth-infra-oper:vlan'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['Vlan']['meta_info']


class EthernetEncapsulation(object):
    """
    ethernet encapsulation
    
    .. attribute:: nodes
    
    	Per node Ethernet encapsulation operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = EthernetEncapsulation.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Per node Ethernet encapsulation operational data
        
        .. attribute:: node
        
        	The Ethernet encaps operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The Ethernet encaps operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: unicast_mac_filters
            
            	Unicast MAC filter table (specific to this node)
            	**type**\:   :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.unicast_mac_filters = EthernetEncapsulation.Nodes.Node.UnicastMacFilters()
                self.unicast_mac_filters.parent = self


            class UnicastMacFilters(object):
                """
                Unicast MAC filter table (specific to this
                node)
                
                .. attribute:: unicast_mac_filter
                
                	Operational data for interface with MAC filters configured
                	**type**\: list of    :py:class:`UnicastMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.unicast_mac_filter = YList()
                    self.unicast_mac_filter.parent = self
                    self.unicast_mac_filter.name = 'unicast_mac_filter'


                class UnicastMacFilter(object):
                    """
                    Operational data for interface with MAC
                    filters configured
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: unicast_filter
                    
                    	Unicast MAC filter information
                    	**type**\: list of    :py:class:`UnicastFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter>`
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.unicast_filter = YList()
                        self.unicast_filter.parent = self
                        self.unicast_filter.name = 'unicast_filter'


                    class UnicastFilter(object):
                        """
                        Unicast MAC filter information
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mode
                        
                        	Unicast MAC mode
                        	**type**\:   :py:class:`EthCapsUcastMacModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthCapsUcastMacModeEnum>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mac_address = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:unicast-filter'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mac_address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                            return meta._meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:unicast-mac-filter[Cisco-IOS-XR-l2-eth-infra-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.unicast_filter is not None:
                            for child_ref in self.unicast_filter:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                        return meta._meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2-eth-infra-oper:unicast-mac-filters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.unicast_mac_filter is not None:
                        for child_ref in self.unicast_mac_filter:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                    return meta._meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/Cisco-IOS-XR-l2-eth-infra-oper:nodes/Cisco-IOS-XR-l2-eth-infra-oper:node[Cisco-IOS-XR-l2-eth-infra-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.unicast_mac_filters is not None and self.unicast_mac_filters._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
                return meta._meta_table['EthernetEncapsulation.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/Cisco-IOS-XR-l2-eth-infra-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
            return meta._meta_table['EthernetEncapsulation.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2_eth_infra_oper as meta
        return meta._meta_table['EthernetEncapsulation']['meta_info']


