""" Cisco_IOS_XR_cdp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package operational data.

This module contains definitions
for the following management objects\:
  cdp\: CDP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CdpDuplexEnum(Enum):
    """
    CdpDuplexEnum

    Cdp duplex

    .. data:: cdp_dplx_none = 0

    	cdp dplx none

    .. data:: cdp_dplx_half = 1

    	cdp dplx half

    .. data:: cdp_dplx_full = 2

    	cdp dplx full

    """

    cdp_dplx_none = 0

    cdp_dplx_half = 1

    cdp_dplx_full = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
        return meta._meta_table['CdpDuplexEnum']


class CdpL3AddrProtocolEnum(Enum):
    """
    CdpL3AddrProtocolEnum

    Cdp l3 addr protocol

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
        return meta._meta_table['CdpL3AddrProtocolEnum']



class Cdp(object):
    """
    CDP operational data
    
    .. attribute:: nodes
    
    	Per node CDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes>`
    
    

    """

    _prefix = 'cdp-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.nodes = Cdp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Per node CDP operational data
        
        .. attribute:: node
        
        	The CDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node>`
        
        

        """

        _prefix = 'cdp-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The CDP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	The table of interfaces on which CDP is running on this node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces>`
            
            .. attribute:: neighbors
            
            	The CDP neighbor tables on this node
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors>`
            
            .. attribute:: statistics
            
            	The CDP traffic statistics for this node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'cdp-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interfaces = Cdp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.neighbors = Cdp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self.statistics = Cdp.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Neighbors(object):
                """
                The CDP neighbor tables on this node
                
                .. attribute:: details
                
                	The detailed CDP neighbor table
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: devices
                
                	The detailed CDP neighbor table
                	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: summaries
                
                	The CDP neighbor summary table
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.details = Cdp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self.devices = Cdp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self.summaries = Cdp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self


                class Details(object):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.detail = YList()
                        self.detail.parent = self
                        self.detail.name = 'detail'


                    class Detail(object):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor>`
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.cdp_neighbor = YList()
                            self.cdp_neighbor.parent = self
                            self.cdp_neighbor.name = 'cdp_neighbor'
                            self.device_id = None
                            self.interface_name = None


                        class CdpNeighbor(object):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.capabilities = None
                                self.detail = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_()
                                self.detail.parent = self
                                self.device_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.platform = None
                                self.port_id = None
                                self.receiving_interface_name = None


                            class Detail_(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplexEnum>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.duplex = None
                                    self.native_vlan = None
                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self.system_name = None
                                    self.version = None
                                    self.vtp_domain = None


                                class NetworkAddresses(object):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_addr_entry = YList()
                                        self.cdp_addr_entry.parent = self
                                        self.cdp_addr_entry.name = 'cdp_addr_entry'


                                    class CdpAddrEntry(object):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:address'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address_type is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_addr_entry is not None:
                                            for child_ref in self.cdp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses']['meta_info']


                                class ProtocolHelloList(object):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_prot_hello_entry = YList()
                                        self.cdp_prot_hello_entry.parent = self
                                        self.cdp_prot_hello_entry.name = 'cdp_prot_hello_entry'


                                    class CdpProtHelloEntry(object):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.hello_message = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-prot-hello-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.hello_message is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:protocol-hello-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_prot_hello_entry is not None:
                                            for child_ref in self.cdp_prot_hello_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.duplex is not None:
                                        return True

                                    if self.native_vlan is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.protocol_hello_list is not None and self.protocol_hello_list._has_data():
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.version is not None:
                                        return True

                                    if self.vtp_domain is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                    return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.capabilities is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:detail'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cdp_neighbor is not None:
                                for child_ref in self.cdp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            if self.device_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:details'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.detail is not None:
                            for child_ref in self.detail:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Details']['meta_info']


                class Devices(object):
                    """
                    The detailed CDP neighbor table
                    
                    .. attribute:: device
                    
                    	Detailed information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.device = YList()
                        self.device.parent = self
                        self.device.name = 'device'


                    class Device(object):
                        """
                        Detailed information about a CDP neighbor
                        entry
                        
                        .. attribute:: device_id  <key>
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor>`
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.device_id = None
                            self.cdp_neighbor = YList()
                            self.cdp_neighbor.parent = self
                            self.cdp_neighbor.name = 'cdp_neighbor'


                        class CdpNeighbor(object):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.capabilities = None
                                self.detail = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self.device_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.platform = None
                                self.port_id = None
                                self.receiving_interface_name = None


                            class Detail(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplexEnum>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.duplex = None
                                    self.native_vlan = None
                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self.system_name = None
                                    self.version = None
                                    self.vtp_domain = None


                                class NetworkAddresses(object):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_addr_entry = YList()
                                        self.cdp_addr_entry.parent = self
                                        self.cdp_addr_entry.name = 'cdp_addr_entry'


                                    class CdpAddrEntry(object):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:address'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address_type is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_addr_entry is not None:
                                            for child_ref in self.cdp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses']['meta_info']


                                class ProtocolHelloList(object):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_prot_hello_entry = YList()
                                        self.cdp_prot_hello_entry.parent = self
                                        self.cdp_prot_hello_entry.name = 'cdp_prot_hello_entry'


                                    class CdpProtHelloEntry(object):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.hello_message = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-prot-hello-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.hello_message is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:protocol-hello-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_prot_hello_entry is not None:
                                            for child_ref in self.cdp_prot_hello_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.duplex is not None:
                                        return True

                                    if self.native_vlan is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.protocol_hello_list is not None and self.protocol_hello_list._has_data():
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.version is not None:
                                        return True

                                    if self.vtp_domain is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                    return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.capabilities is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.device_id is None:
                                raise YPYModelError('Key property device_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:device[Cisco-IOS-XR-cdp-oper:device-id = ' + str(self.device_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.device_id is not None:
                                return True

                            if self.cdp_neighbor is not None:
                                for child_ref in self.cdp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:devices'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.device is not None:
                            for child_ref in self.device:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Devices']['meta_info']


                class Summaries(object):
                    """
                    The CDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a CDP neighbor entry
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.summary = YList()
                        self.summary.parent = self
                        self.summary.name = 'summary'


                    class Summary(object):
                        """
                        Brief information about a CDP neighbor entry
                        
                        .. attribute:: cdp_neighbor
                        
                        	cdp neighbor
                        	**type**\: list of    :py:class:`CdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor>`
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'cdp-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.cdp_neighbor = YList()
                            self.cdp_neighbor.parent = self
                            self.cdp_neighbor.name = 'cdp_neighbor'
                            self.device_id = None
                            self.interface_name = None


                        class CdpNeighbor(object):
                            """
                            cdp neighbor
                            
                            .. attribute:: capabilities
                            
                            	Capabilities
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'cdp-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.capabilities = None
                                self.detail = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail()
                                self.detail.parent = self
                                self.device_id = None
                                self.header_version = None
                                self.hold_time = None
                                self.platform = None
                                self.port_id = None
                                self.receiving_interface_name = None


                            class Detail(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: duplex
                                
                                	Duplex setting
                                	**type**\:   :py:class:`CdpDuplexEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpDuplexEnum>`
                                
                                .. attribute:: native_vlan
                                
                                	Native VLAN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	List of network addresses 
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: protocol_hello_list
                                
                                	List of protocol hello entries
                                	**type**\:   :py:class:`ProtocolHelloList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList>`
                                
                                .. attribute:: system_name
                                
                                	SysName
                                	**type**\:  str
                                
                                .. attribute:: version
                                
                                	Version TLV
                                	**type**\:  str
                                
                                .. attribute:: vtp_domain
                                
                                	VTP domain
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'cdp-oper'
                                _revision = '2015-07-30'

                                def __init__(self):
                                    self.parent = None
                                    self.duplex = None
                                    self.native_vlan = None
                                    self.network_addresses = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.protocol_hello_list = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList()
                                    self.protocol_hello_list.parent = self
                                    self.system_name = None
                                    self.version = None
                                    self.vtp_domain = None


                                class NetworkAddresses(object):
                                    """
                                    List of network addresses 
                                    
                                    .. attribute:: cdp_addr_entry
                                    
                                    	cdp addr entry
                                    	**type**\: list of    :py:class:`CdpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_addr_entry = YList()
                                        self.cdp_addr_entry.parent = self
                                        self.cdp_addr_entry.name = 'cdp_addr_entry'


                                    class CdpAddrEntry(object):
                                        """
                                        cdp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address>`
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address()
                                            self.address.parent = self


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`CdpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.CdpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'cdp-oper'
                                            _revision = '2015-07-30'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:address'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address_type is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_addr_entry is not None:
                                            for child_ref in self.cdp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses']['meta_info']


                                class ProtocolHelloList(object):
                                    """
                                    List of protocol hello entries
                                    
                                    .. attribute:: cdp_prot_hello_entry
                                    
                                    	cdp prot hello entry
                                    	**type**\: list of    :py:class:`CdpProtHelloEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry>`
                                    
                                    

                                    """

                                    _prefix = 'cdp-oper'
                                    _revision = '2015-07-30'

                                    def __init__(self):
                                        self.parent = None
                                        self.cdp_prot_hello_entry = YList()
                                        self.cdp_prot_hello_entry.parent = self
                                        self.cdp_prot_hello_entry.name = 'cdp_prot_hello_entry'


                                    class CdpProtHelloEntry(object):
                                        """
                                        cdp prot hello entry
                                        
                                        .. attribute:: hello_message
                                        
                                        	Protocol Hello msg
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'cdp-oper'
                                        _revision = '2015-07-30'

                                        def __init__(self):
                                            self.parent = None
                                            self.hello_message = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-prot-hello-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.hello_message is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:protocol-hello-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cdp_prot_hello_entry is not None:
                                            for child_ref in self.cdp_prot_hello_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.duplex is not None:
                                        return True

                                    if self.native_vlan is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.protocol_hello_list is not None and self.protocol_hello_list._has_data():
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.version is not None:
                                        return True

                                    if self.vtp_domain is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                    return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:cdp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.capabilities is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                                return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cdp_neighbor is not None:
                                for child_ref in self.cdp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            if self.device_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                            return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.summary is not None:
                            for child_ref in self.summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                        return meta._meta_table['Cdp.Nodes.Node.Neighbors.Summaries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.details is not None and self.details._has_data():
                        return True

                    if self.devices is not None and self.devices._has_data():
                        return True

                    if self.summaries is not None and self.summaries._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                    return meta._meta_table['Cdp.Nodes.Node.Neighbors']['meta_info']


            class Statistics(object):
                """
                The CDP traffic statistics for this node
                
                .. attribute:: bad_packet_errors
                
                	Bad packet received and dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: checksum_errors
                
                	Checksum errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_errors
                
                	Header syntax errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: header_version_errors
                
                	Can't handle receive version
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: open_file_errors
                
                	Cannot open file
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v1
                
                	Received v1 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets_v2
                
                	Received v2 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v1
                
                	Transmitted v1 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets_v2
                
                	Transmitted v2 packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: truncated_packet_errors
                
                	Truncated messages
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.bad_packet_errors = None
                    self.checksum_errors = None
                    self.encapsulation_errors = None
                    self.header_errors = None
                    self.header_version_errors = None
                    self.open_file_errors = None
                    self.out_of_memory_errors = None
                    self.received_packets = None
                    self.received_packets_v1 = None
                    self.received_packets_v2 = None
                    self.transmitted_packets = None
                    self.transmitted_packets_v1 = None
                    self.transmitted_packets_v2 = None
                    self.truncated_packet_errors = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bad_packet_errors is not None:
                        return True

                    if self.checksum_errors is not None:
                        return True

                    if self.encapsulation_errors is not None:
                        return True

                    if self.header_errors is not None:
                        return True

                    if self.header_version_errors is not None:
                        return True

                    if self.open_file_errors is not None:
                        return True

                    if self.out_of_memory_errors is not None:
                        return True

                    if self.received_packets is not None:
                        return True

                    if self.received_packets_v1 is not None:
                        return True

                    if self.received_packets_v2 is not None:
                        return True

                    if self.transmitted_packets is not None:
                        return True

                    if self.transmitted_packets_v1 is not None:
                        return True

                    if self.transmitted_packets_v2 is not None:
                        return True

                    if self.truncated_packet_errors is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                    return meta._meta_table['Cdp.Nodes.Node.Statistics']['meta_info']


            class Interfaces(object):
                """
                The table of interfaces on which CDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which CDP is running
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper.Cdp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'cdp-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Operational data for an interface on which
                    CDP is running
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: basecaps_state
                    
                    	Interface basecaps state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cdp_protocol_state
                    
                    	CDP protocol state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_encaps
                    
                    	Interface encapsulation
                    	**type**\:  str
                    
                    .. attribute:: interface_handle
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'cdp-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.basecaps_state = None
                        self.cdp_protocol_state = None
                        self.interface_encaps = None
                        self.interface_handle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:interface[Cisco-IOS-XR-cdp-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.basecaps_state is not None:
                            return True

                        if self.cdp_protocol_state is not None:
                            return True

                        if self.interface_encaps is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                        return meta._meta_table['Cdp.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-cdp-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                    return meta._meta_table['Cdp.Nodes.Node.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-cdp-oper:cdp/Cisco-IOS-XR-cdp-oper:nodes/Cisco-IOS-XR-cdp-oper:node[Cisco-IOS-XR-cdp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.neighbors is not None and self.neighbors._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
                return meta._meta_table['Cdp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cdp-oper:cdp/Cisco-IOS-XR-cdp-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
            return meta._meta_table['Cdp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cdp-oper:cdp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_oper as meta
        return meta._meta_table['Cdp']['meta_info']


