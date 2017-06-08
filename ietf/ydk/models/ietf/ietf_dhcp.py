""" ietf_dhcp 

The module for implementing DHCP protocol

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AllocateTypeEnum(Enum):
    """
    AllocateTypeEnum

    Mechanisms for IP address allocation

    .. data:: automatic = 0

    	DHCP assigns a permanent IP address to a client

    .. data:: dynamic = 1

    	DHCP assigns an IP address to a client

    	for a limited period of time

    .. data:: manual = 2

    	a client's IP address is assigned by the

    	          network administrator, and DHCP is used

    	simply to convey the assigned address to the client

    """

    automatic = 0

    dynamic = 1

    manual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['AllocateTypeEnum']



class Dhcp(object):
    """
    DHCP configuration
    
    .. attribute:: client
    
    	DHCP client configuration
    	**type**\:   :py:class:`Client <ydk.models.ietf.ietf_dhcp.Dhcp.Client>`
    
    .. attribute:: relay
    
    	DHCP relay agent configuration
    	**type**\:   :py:class:`Relay <ydk.models.ietf.ietf_dhcp.Dhcp.Relay>`
    
    .. attribute:: server
    
    	DHCP server configuration
    	**type**\:   :py:class:`Server <ydk.models.ietf.ietf_dhcp.Dhcp.Server>`
    
    

    """

    _prefix = 'dhcp'
    _revision = '2017-03-02'

    def __init__(self):
        self.client = Dhcp.Client()
        self.client.parent = self
        self.relay = Dhcp.Relay()
        self.relay.parent = self
        self.server = Dhcp.Server()
        self.server.parent = self


    class Server(object):
        """
        DHCP server configuration
        
        .. attribute:: dhcp_ip_pool
        
        	Global IP pool configuration
        	**type**\: list of    :py:class:`DhcpIpPool <ydk.models.ietf.ietf_dhcp.Dhcp.Server.DhcpIpPool>`
        
        .. attribute:: lease_time
        
        	Default network address lease time assigned to DHCP clients
        	**type**\:  int
        
        	**range:** 180..31536000
        
        .. attribute:: option
        
        	Configuration option
        	**type**\:   :py:class:`Option <ydk.models.ietf.ietf_dhcp.Dhcp.Server.Option>`
        
        .. attribute:: ping_packet_number
        
        	Number of ping packets
        	**type**\:  int
        
        	**range:** 0..10
        
        	**default value**\: 0
        
        .. attribute:: ping_packet_timeout
        
        	Timeout of ping packet
        	**type**\:  int
        
        	**range:** 0..10000
        
        	**default value**\: 500
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.dhcp_ip_pool = YList()
            self.dhcp_ip_pool.parent = self
            self.dhcp_ip_pool.name = 'dhcp_ip_pool'
            self.lease_time = None
            self.option = Dhcp.Server.Option()
            self.option.parent = self
            self.ping_packet_number = None
            self.ping_packet_timeout = None


        class Option(object):
            """
            Configuration option
            
            .. attribute:: dhcp_server_identifier
            
            	DHCP server identifier
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: domain_name
            
            	Name of the domain
            	**type**\:  str
            
            .. attribute:: domain_name_server
            
            	IPv4 address of the domain
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: interface_mtu
            
            	Minimum Transmission Unit (MTU) of the interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: netbios_name_server
            
            	NETBIOS name server
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: netbios_node_type
            
            	NETBIOS node type
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: netbios_scope
            
            	NETBIOS scope
            	**type**\:  str
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.dhcp_server_identifier = None
                self.domain_name = None
                self.domain_name_server = None
                self.interface_mtu = None
                self.netbios_name_server = None
                self.netbios_node_type = None
                self.netbios_scope = None

            @property
            def _common_path(self):

                return '/ietf-dhcp:dhcp/ietf-dhcp:server/ietf-dhcp:option'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.dhcp_server_identifier is not None:
                    return True

                if self.domain_name is not None:
                    return True

                if self.domain_name_server is not None:
                    return True

                if self.interface_mtu is not None:
                    return True

                if self.netbios_name_server is not None:
                    return True

                if self.netbios_node_type is not None:
                    return True

                if self.netbios_scope is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['Dhcp.Server.Option']['meta_info']


        class DhcpIpPool(object):
            """
            Global IP pool configuration
            
            .. attribute:: ip_pool_name  <key>
            
            	Name of the IP pool
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: gateway_ip
            
            	IPv4 address of the gateway
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: gateway_mask
            
            	Network submask of the gateway
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            .. attribute:: lease_time
            
            	Default network address lease time assigned to DHCP clients
            	**type**\:  int
            
            	**range:** 180..31536000
            
            .. attribute:: manual_allocation
            
            	Mapping from MAC address to IP address
            	**type**\: list of    :py:class:`ManualAllocation <ydk.models.ietf.ietf_dhcp.Dhcp.Server.DhcpIpPool.ManualAllocation>`
            
            .. attribute:: option
            
            	Configuration option
            	**type**\:   :py:class:`Option <ydk.models.ietf.ietf_dhcp.Dhcp.Server.DhcpIpPool.Option>`
            
            .. attribute:: section
            
            	IPv4 address for the range
            	**type**\: list of    :py:class:`Section <ydk.models.ietf.ietf_dhcp.Dhcp.Server.DhcpIpPool.Section>`
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.ip_pool_name = None
                self.gateway_ip = None
                self.gateway_mask = None
                self.interface = None
                self.lease_time = None
                self.manual_allocation = YList()
                self.manual_allocation.parent = self
                self.manual_allocation.name = 'manual_allocation'
                self.option = Dhcp.Server.DhcpIpPool.Option()
                self.option.parent = self
                self.section = YList()
                self.section.parent = self
                self.section.name = 'section'


            class ManualAllocation(object):
                """
                Mapping from MAC address to IP address
                
                .. attribute:: ip_address  <key>
                
                	IPv4 address of the host
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: mac_address  <key>
                
                	MAC address of the host
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.ip_address = None
                    self.mac_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip_address is None:
                        raise YPYModelError('Key property ip_address is None')
                    if self.mac_address is None:
                        raise YPYModelError('Key property mac_address is None')

                    return self.parent._common_path +'/ietf-dhcp:manual-allocation[ietf-dhcp:ip-address = ' + str(self.ip_address) + '][ietf-dhcp:mac-address = ' + str(self.mac_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ip_address is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['Dhcp.Server.DhcpIpPool.ManualAllocation']['meta_info']


            class Section(object):
                """
                IPv4 address for the range
                
                .. attribute:: section_index  <key>
                
                	Index of IPv4 address range
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: section_end_ip
                
                	Last IPv4 Address of a section
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: section_start_ip
                
                	Starting IPv4 Address of a section
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.section_index = None
                    self.section_end_ip = None
                    self.section_start_ip = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.section_index is None:
                        raise YPYModelError('Key property section_index is None')

                    return self.parent._common_path +'/ietf-dhcp:section[ietf-dhcp:section-index = ' + str(self.section_index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.section_index is not None:
                        return True

                    if self.section_end_ip is not None:
                        return True

                    if self.section_start_ip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['Dhcp.Server.DhcpIpPool.Section']['meta_info']


            class Option(object):
                """
                Configuration option
                
                .. attribute:: dhcp_server_identifier
                
                	DHCP server identifier
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: domain_name
                
                	Name of the domain
                	**type**\:  str
                
                .. attribute:: domain_name_server
                
                	IPv4 address of the domain
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: interface_mtu
                
                	Minimum Transmission Unit (MTU) of the interface
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: netbios_name_server
                
                	NETBIOS name server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: netbios_node_type
                
                	NETBIOS node type
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: netbios_scope
                
                	NETBIOS scope
                	**type**\:  str
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.dhcp_server_identifier = None
                    self.domain_name = None
                    self.domain_name_server = None
                    self.interface_mtu = None
                    self.netbios_name_server = None
                    self.netbios_node_type = None
                    self.netbios_scope = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-dhcp:option'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.dhcp_server_identifier is not None:
                        return True

                    if self.domain_name is not None:
                        return True

                    if self.domain_name_server is not None:
                        return True

                    if self.interface_mtu is not None:
                        return True

                    if self.netbios_name_server is not None:
                        return True

                    if self.netbios_node_type is not None:
                        return True

                    if self.netbios_scope is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['Dhcp.Server.DhcpIpPool.Option']['meta_info']

            @property
            def _common_path(self):
                if self.ip_pool_name is None:
                    raise YPYModelError('Key property ip_pool_name is None')

                return '/ietf-dhcp:dhcp/ietf-dhcp:server/ietf-dhcp:dhcp-ip-pool[ietf-dhcp:ip-pool-name = ' + str(self.ip_pool_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ip_pool_name is not None:
                    return True

                if self.gateway_ip is not None:
                    return True

                if self.gateway_mask is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.lease_time is not None:
                    return True

                if self.manual_allocation is not None:
                    for child_ref in self.manual_allocation:
                        if child_ref._has_data():
                            return True

                if self.option is not None and self.option._has_data():
                    return True

                if self.section is not None:
                    for child_ref in self.section:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['Dhcp.Server.DhcpIpPool']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp/ietf-dhcp:server'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.dhcp_ip_pool is not None:
                for child_ref in self.dhcp_ip_pool:
                    if child_ref._has_data():
                        return True

            if self.lease_time is not None:
                return True

            if self.option is not None and self.option._has_data():
                return True

            if self.ping_packet_number is not None:
                return True

            if self.ping_packet_timeout is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['Dhcp.Server']['meta_info']


    class Relay(object):
        """
        DHCP relay agent configuration
        
        .. attribute:: server_group
        
        	DHCP server group configuration that DHCP relays to
        	**type**\: list of    :py:class:`ServerGroup <ydk.models.ietf.ietf_dhcp.Dhcp.Relay.ServerGroup>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.server_group = YList()
            self.server_group.parent = self
            self.server_group.name = 'server_group'


        class ServerGroup(object):
            """
            DHCP server group configuration that DHCP relays to
            
            .. attribute:: server_group_name  <key>
            
            	Name of a DHCP server group
            	**type**\:  str
            
            .. attribute:: gateway_address
            
            	IPv4 address of the gateway
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            .. attribute:: server_address
            
            	IPv4 address of the server
            	**type**\:  list of str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.server_group_name = None
                self.gateway_address = None
                self.interface = None
                self.server_address = YLeafList()
                self.server_address.parent = self
                self.server_address.name = 'server_address'

            @property
            def _common_path(self):
                if self.server_group_name is None:
                    raise YPYModelError('Key property server_group_name is None')

                return '/ietf-dhcp:dhcp/ietf-dhcp:relay/ietf-dhcp:server-group[ietf-dhcp:server-group-name = ' + str(self.server_group_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.server_group_name is not None:
                    return True

                if self.gateway_address is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.server_address is not None:
                    for child in self.server_address:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['Dhcp.Relay.ServerGroup']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp/ietf-dhcp:relay'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.server_group is not None:
                for child_ref in self.server_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['Dhcp.Relay']['meta_info']


    class Client(object):
        """
        DHCP client configuration
        
        .. attribute:: interfaces
        
        	Interface configuration
        	**type**\: list of    :py:class:`Interfaces <ydk.models.ietf.ietf_dhcp.Dhcp.Client.Interfaces>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.interfaces = YList()
            self.interfaces.parent = self
            self.interfaces.name = 'interfaces'


        class Interfaces(object):
            """
            Interface configuration
            
            .. attribute:: interface  <key>
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            .. attribute:: client_id
            
            	DHCP client identifier
            	**type**\:  str
            
            .. attribute:: lease
            
            	Default network address lease time assigned to DHCP clients
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.interface = None
                self.client_id = None
                self.lease = None

            @property
            def _common_path(self):
                if self.interface is None:
                    raise YPYModelError('Key property interface is None')

                return '/ietf-dhcp:dhcp/ietf-dhcp:client/ietf-dhcp:interfaces[ietf-dhcp:interface = ' + str(self.interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface is not None:
                    return True

                if self.client_id is not None:
                    return True

                if self.lease is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['Dhcp.Client.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp/ietf-dhcp:client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interfaces is not None:
                for child_ref in self.interfaces:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['Dhcp.Client']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dhcp:dhcp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.client is not None and self.client._has_data():
            return True

        if self.relay is not None and self.relay._has_data():
            return True

        if self.server is not None and self.server._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['Dhcp']['meta_info']


class DhcpState(object):
    """
    DHCP state data
    
    .. attribute:: client
    
    	DHCP client state data
    	**type**\:   :py:class:`Client <ydk.models.ietf.ietf_dhcp.DhcpState.Client>`
    
    .. attribute:: relay
    
    	DHCP reply agent state data
    	**type**\:   :py:class:`Relay <ydk.models.ietf.ietf_dhcp.DhcpState.Relay>`
    
    .. attribute:: server
    
    	DHCP server state data
    	**type**\:   :py:class:`Server <ydk.models.ietf.ietf_dhcp.DhcpState.Server>`
    
    

    """

    _prefix = 'dhcp'
    _revision = '2017-03-02'

    def __init__(self):
        self.client = DhcpState.Client()
        self.client.parent = self
        self.relay = DhcpState.Relay()
        self.relay.parent = self
        self.server = DhcpState.Server()
        self.server.parent = self


    class Server(object):
        """
        DHCP server state data
        
        .. attribute:: host
        
        	Host status information
        	**type**\:   :py:class:`Host <ydk.models.ietf.ietf_dhcp.DhcpState.Server.Host>`
        
        .. attribute:: ip_pool
        
        	Global IP pool configuration
        	**type**\: list of    :py:class:`IpPool <ydk.models.ietf.ietf_dhcp.DhcpState.Server.IpPool>`
        
        .. attribute:: packet_statistics
        
        	Packet statistics
        	**type**\:   :py:class:`PacketStatistics <ydk.models.ietf.ietf_dhcp.DhcpState.Server.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.host = DhcpState.Server.Host()
            self.host.parent = self
            self.ip_pool = YList()
            self.ip_pool.parent = self
            self.ip_pool.name = 'ip_pool'
            self.packet_statistics = DhcpState.Server.PacketStatistics()
            self.packet_statistics.parent = self


        class PacketStatistics(object):
            """
            Packet statistics
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
            
            .. attribute:: receive
            
            	Number of  received packets
            	**type**\:   :py:class:`Receive <ydk.models.ietf.ietf_dhcp.DhcpState.Server.PacketStatistics.Receive>`
            
            .. attribute:: send
            
            	Number of sent packets
            	**type**\:   :py:class:`Send <ydk.models.ietf.ietf_dhcp.DhcpState.Server.PacketStatistics.Send>`
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.interface = None
                self.receive = DhcpState.Server.PacketStatistics.Receive()
                self.receive.parent = self
                self.send = DhcpState.Server.PacketStatistics.Send()
                self.send.parent = self


            class Receive(object):
                """
                Number of  received packets
                
                .. attribute:: decline_packet
                
                	Total number of DHCPDECLINE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discover_packet
                
                	Total number of DHCPDISCOVER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inform_packet
                
                	Total number of DHCPINFORM packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: release_packet
                
                	Total number of DHCPRELEASE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_packet
                
                	Total number of DHCPREQUEST packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.decline_packet = None
                    self.discover_packet = None
                    self.inform_packet = None
                    self.release_packet = None
                    self.request_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:server/ietf-dhcp:packet-statistics/ietf-dhcp:receive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.decline_packet is not None:
                        return True

                    if self.discover_packet is not None:
                        return True

                    if self.inform_packet is not None:
                        return True

                    if self.release_packet is not None:
                        return True

                    if self.request_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Server.PacketStatistics.Receive']['meta_info']


            class Send(object):
                """
                Number of sent packets
                
                .. attribute:: ack_packet
                
                	Total number of DHCPACK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nack_packet
                
                	Total number of DHCPNAK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offer_packet
                
                	Total number of DHCPOFFER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.ack_packet = None
                    self.nack_packet = None
                    self.offer_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:server/ietf-dhcp:packet-statistics/ietf-dhcp:send'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ack_packet is not None:
                        return True

                    if self.nack_packet is not None:
                        return True

                    if self.offer_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Server.PacketStatistics.Send']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-dhcp:dhcp-state/ietf-dhcp:server/ietf-dhcp:packet-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface is not None:
                    return True

                if self.receive is not None and self.receive._has_data():
                    return True

                if self.send is not None and self.send._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['DhcpState.Server.PacketStatistics']['meta_info']


        class Host(object):
            """
            Host status information
            
            .. attribute:: host_hardware_address
            
            	MAC address of the host
            	**type**\:  str
            
            .. attribute:: host_ip
            
            	IPv4 address of the host
            	**type**\:  str
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            .. attribute:: lease
            
            	Default network address lease time assigned to DHCP clients
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Mechanisms for IP address allocation
            	**type**\:   :py:class:`AllocateTypeEnum <ydk.models.ietf.ietf_dhcp.AllocateTypeEnum>`
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.host_hardware_address = None
                self.host_ip = None
                self.interface = None
                self.lease = None
                self.type = None

            @property
            def _common_path(self):

                return '/ietf-dhcp:dhcp-state/ietf-dhcp:server/ietf-dhcp:host'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.host_hardware_address is not None:
                    return True

                if self.host_ip is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.lease is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['DhcpState.Server.Host']['meta_info']


        class IpPool(object):
            """
            Global IP pool configuration
            
            .. attribute:: ip_pool_name  <key>
            
            	Name of an IP pool
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: conflict_ip_count
            
            	Total number of conflict IPv4 addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: gateway_ip
            
            	IPv4 address of the gateway
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: gateway_mask
            
            	Network submask of the gateway
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: idle_ip_count
            
            	Total number of idle IPv4 addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_ip_count
            
            	Total number of IPv4 addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: used_ip_count
            
            	Total number of used IPv4 addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.ip_pool_name = None
                self.conflict_ip_count = None
                self.gateway_ip = None
                self.gateway_mask = None
                self.idle_ip_count = None
                self.total_ip_count = None
                self.used_ip_count = None

            @property
            def _common_path(self):
                if self.ip_pool_name is None:
                    raise YPYModelError('Key property ip_pool_name is None')

                return '/ietf-dhcp:dhcp-state/ietf-dhcp:server/ietf-dhcp:ip-pool[ietf-dhcp:ip-pool-name = ' + str(self.ip_pool_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ip_pool_name is not None:
                    return True

                if self.conflict_ip_count is not None:
                    return True

                if self.gateway_ip is not None:
                    return True

                if self.gateway_mask is not None:
                    return True

                if self.idle_ip_count is not None:
                    return True

                if self.total_ip_count is not None:
                    return True

                if self.used_ip_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['DhcpState.Server.IpPool']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp-state/ietf-dhcp:server'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.host is not None and self.host._has_data():
                return True

            if self.ip_pool is not None:
                for child_ref in self.ip_pool:
                    if child_ref._has_data():
                        return True

            if self.packet_statistics is not None and self.packet_statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['DhcpState.Server']['meta_info']


    class Relay(object):
        """
        DHCP reply agent state data
        
        .. attribute:: packet_statistics
        
        	Packet statistics
        	**type**\:   :py:class:`PacketStatistics <ydk.models.ietf.ietf_dhcp.DhcpState.Relay.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.packet_statistics = DhcpState.Relay.PacketStatistics()
            self.packet_statistics.parent = self


        class PacketStatistics(object):
            """
            Packet statistics
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
            
            .. attribute:: receive
            
            	Number of  received packets
            	**type**\:   :py:class:`Receive <ydk.models.ietf.ietf_dhcp.DhcpState.Relay.PacketStatistics.Receive>`
            
            .. attribute:: send
            
            	Number of sent packets
            	**type**\:   :py:class:`Send <ydk.models.ietf.ietf_dhcp.DhcpState.Relay.PacketStatistics.Send>`
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.interface = None
                self.receive = DhcpState.Relay.PacketStatistics.Receive()
                self.receive.parent = self
                self.send = DhcpState.Relay.PacketStatistics.Send()
                self.send.parent = self


            class Receive(object):
                """
                Number of  received packets
                
                .. attribute:: ack_packet
                
                	Total number of DHCPACK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: decline_packet
                
                	Total number of DHCPDECLINE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discover_packet
                
                	Total number of DHCPDISCOVER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inform_packet
                
                	Total number of DHCPINFORM packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nack_packet
                
                	Total number of DHCPNAK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offer_packet
                
                	Total number of DHCPOFFER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: release_packet
                
                	Total number of DHCPRELEASE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_packet
                
                	Total number of DHCPREQUEST packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.ack_packet = None
                    self.decline_packet = None
                    self.discover_packet = None
                    self.inform_packet = None
                    self.nack_packet = None
                    self.offer_packet = None
                    self.release_packet = None
                    self.request_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:relay/ietf-dhcp:packet-statistics/ietf-dhcp:receive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ack_packet is not None:
                        return True

                    if self.decline_packet is not None:
                        return True

                    if self.discover_packet is not None:
                        return True

                    if self.inform_packet is not None:
                        return True

                    if self.nack_packet is not None:
                        return True

                    if self.offer_packet is not None:
                        return True

                    if self.release_packet is not None:
                        return True

                    if self.request_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Relay.PacketStatistics.Receive']['meta_info']


            class Send(object):
                """
                Number of sent packets
                
                .. attribute:: ack_packet
                
                	Total number of DHCPACK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: decline_packet
                
                	Total number of DHCPDECLINE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discover_packet
                
                	Total number of DHCPDISCOVER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inform_packet
                
                	Total number of DHCPINFORM packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nack_packet
                
                	Total number of DHCPNAK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offer_packet
                
                	Total number of DHCPOFFER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: release_packet
                
                	Total number of DHCPRELEASE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_packet
                
                	Total number of DHCPREQUEST packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.ack_packet = None
                    self.decline_packet = None
                    self.discover_packet = None
                    self.inform_packet = None
                    self.nack_packet = None
                    self.offer_packet = None
                    self.release_packet = None
                    self.request_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:relay/ietf-dhcp:packet-statistics/ietf-dhcp:send'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ack_packet is not None:
                        return True

                    if self.decline_packet is not None:
                        return True

                    if self.discover_packet is not None:
                        return True

                    if self.inform_packet is not None:
                        return True

                    if self.nack_packet is not None:
                        return True

                    if self.offer_packet is not None:
                        return True

                    if self.release_packet is not None:
                        return True

                    if self.request_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Relay.PacketStatistics.Send']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-dhcp:dhcp-state/ietf-dhcp:relay/ietf-dhcp:packet-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface is not None:
                    return True

                if self.receive is not None and self.receive._has_data():
                    return True

                if self.send is not None and self.send._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['DhcpState.Relay.PacketStatistics']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp-state/ietf-dhcp:relay'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.packet_statistics is not None and self.packet_statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['DhcpState.Relay']['meta_info']


    class Client(object):
        """
        DHCP client state data
        
        .. attribute:: packet_statistics
        
        	Packet statistics
        	**type**\:   :py:class:`PacketStatistics <ydk.models.ietf.ietf_dhcp.DhcpState.Client.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.packet_statistics = DhcpState.Client.PacketStatistics()
            self.packet_statistics.parent = self


        class PacketStatistics(object):
            """
            Packet statistics
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
            
            .. attribute:: receive
            
            	Number of  received packets
            	**type**\:   :py:class:`Receive <ydk.models.ietf.ietf_dhcp.DhcpState.Client.PacketStatistics.Receive>`
            
            .. attribute:: send
            
            	Number of sent packets
            	**type**\:   :py:class:`Send <ydk.models.ietf.ietf_dhcp.DhcpState.Client.PacketStatistics.Send>`
            
            

            """

            _prefix = 'dhcp'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.interface = None
                self.receive = DhcpState.Client.PacketStatistics.Receive()
                self.receive.parent = self
                self.send = DhcpState.Client.PacketStatistics.Send()
                self.send.parent = self


            class Receive(object):
                """
                Number of  received packets
                
                .. attribute:: ack_packet
                
                	Total number of DHCPACK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nack_packet
                
                	Total number of DHCPNAK packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offer_packet
                
                	Total number of DHCPOFFER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.ack_packet = None
                    self.nack_packet = None
                    self.offer_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:client/ietf-dhcp:packet-statistics/ietf-dhcp:receive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ack_packet is not None:
                        return True

                    if self.nack_packet is not None:
                        return True

                    if self.offer_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Client.PacketStatistics.Receive']['meta_info']


            class Send(object):
                """
                Number of sent packets
                
                .. attribute:: decline_packet
                
                	Total number of DHCPDECLINE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discover_packet
                
                	Total number of DHCPDISCOVER packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inform_packet
                
                	Total number of DHCPINFORM packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: release_packet
                
                	Total number of DHCPRELEASE packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_packet
                
                	Total number of DHCPREQUEST packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dhcp'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.decline_packet = None
                    self.discover_packet = None
                    self.inform_packet = None
                    self.release_packet = None
                    self.request_packet = None

                @property
                def _common_path(self):

                    return '/ietf-dhcp:dhcp-state/ietf-dhcp:client/ietf-dhcp:packet-statistics/ietf-dhcp:send'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.decline_packet is not None:
                        return True

                    if self.discover_packet is not None:
                        return True

                    if self.inform_packet is not None:
                        return True

                    if self.release_packet is not None:
                        return True

                    if self.request_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_dhcp as meta
                    return meta._meta_table['DhcpState.Client.PacketStatistics.Send']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-dhcp:dhcp-state/ietf-dhcp:client/ietf-dhcp:packet-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface is not None:
                    return True

                if self.receive is not None and self.receive._has_data():
                    return True

                if self.send is not None and self.send._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dhcp as meta
                return meta._meta_table['DhcpState.Client.PacketStatistics']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-dhcp:dhcp-state/ietf-dhcp:client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.packet_statistics is not None and self.packet_statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['DhcpState.Client']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dhcp:dhcp-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.client is not None and self.client._has_data():
            return True

        if self.relay is not None and self.relay._has_data():
            return True

        if self.server is not None and self.server._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['DhcpState']['meta_info']


class CleanServerStatisticsRpc(object):
    """
    Clean server packet statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_dhcp.CleanServerStatisticsRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_dhcp.CleanServerStatisticsRpc.Output>`
    
    

    """

    _prefix = 'dhcp'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = CleanServerStatisticsRpc.Input()
        self.input.parent = self
        self.output = CleanServerStatisticsRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: clean_at
        
        	The start time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: interface
        
        	Name of the interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`interface <ydk.models.ietf.ietf_dhcp.DhcpState.Server.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_at = None
            self.interface = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-server-statistics/ietf-dhcp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_at is not None:
                return True

            if self.interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanServerStatisticsRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: clean_finished_at
        
        	The finish time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_finished_at = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-server-statistics/ietf-dhcp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_finished_at is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanServerStatisticsRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dhcp:clean-server-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['CleanServerStatisticsRpc']['meta_info']


class CleanRelayStatisticsRpc(object):
    """
    Clean relay packet statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_dhcp.CleanRelayStatisticsRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_dhcp.CleanRelayStatisticsRpc.Output>`
    
    

    """

    _prefix = 'dhcp'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = CleanRelayStatisticsRpc.Input()
        self.input.parent = self
        self.output = CleanRelayStatisticsRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: clean_at
        
        	The start time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: interface
        
        	Name of the interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`interface <ydk.models.ietf.ietf_dhcp.DhcpState.Relay.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_at = None
            self.interface = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-relay-statistics/ietf-dhcp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_at is not None:
                return True

            if self.interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanRelayStatisticsRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: clean_finished_at
        
        	The finish time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_finished_at = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-relay-statistics/ietf-dhcp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_finished_at is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanRelayStatisticsRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dhcp:clean-relay-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['CleanRelayStatisticsRpc']['meta_info']


class CleanClientStatisticsRpc(object):
    """
    Clean client packet statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_dhcp.CleanClientStatisticsRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_dhcp.CleanClientStatisticsRpc.Output>`
    
    

    """

    _prefix = 'dhcp'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = CleanClientStatisticsRpc.Input()
        self.input.parent = self
        self.output = CleanClientStatisticsRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: clean_at
        
        	The start time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: interface
        
        	Name of the interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`interface <ydk.models.ietf.ietf_dhcp.DhcpState.Client.PacketStatistics>`
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_at = None
            self.interface = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-client-statistics/ietf-dhcp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_at is not None:
                return True

            if self.interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanClientStatisticsRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: clean_finished_at
        
        	The finish time to clean packet statistics
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'dhcp'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.clean_finished_at = None

        @property
        def _common_path(self):

            return '/ietf-dhcp:clean-client-statistics/ietf-dhcp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clean_finished_at is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dhcp as meta
            return meta._meta_table['CleanClientStatisticsRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dhcp:clean-client-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dhcp as meta
        return meta._meta_table['CleanClientStatisticsRpc']['meta_info']


