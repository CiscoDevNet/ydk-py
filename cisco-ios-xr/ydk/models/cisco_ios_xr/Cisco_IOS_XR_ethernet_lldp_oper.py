""" Cisco_IOS_XR_ethernet_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\: Link Layer Discovery Protocol operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LldpL3AddrProtocolEnum(Enum):
    """
    LldpL3AddrProtocolEnum

    Lldp l3 addr protocol

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
        return meta._meta_table['LldpL3AddrProtocolEnum']



class Lldp(object):
    """
    Link Layer Discovery Protocol operational data
    
    .. attribute:: global_lldp
    
    	Global LLDP data
    	**type**\:   :py:class:`GlobalLldp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp>`
    
    .. attribute:: nodes
    
    	Per node LLDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes>`
    
    

    """

    _prefix = 'ethernet-lldp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_lldp = Lldp.GlobalLldp()
        self.global_lldp.parent = self
        self.nodes = Lldp.Nodes()
        self.nodes.parent = self


    class GlobalLldp(object):
        """
        Global LLDP data
        
        .. attribute:: lldp_info
        
        	The LLDP Global Information of this box
        	**type**\:   :py:class:`LldpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.GlobalLldp.LldpInfo>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.lldp_info = Lldp.GlobalLldp.LldpInfo()
            self.lldp_info.parent = self


        class LldpInfo(object):
            """
            The LLDP Global Information of this box
            
            .. attribute:: hold_time
            
            	Length  of time  (in sec)                        that receiver must keep this                     packet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: re_init
            
            	Delay (in sec) for LLDP                          initialization on any                            interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: timer
            
            	Rate at which LLDP packets                       are sent (in sec)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.hold_time = None
                self.re_init = None
                self.timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-lldp-oper:lldp/Cisco-IOS-XR-ethernet-lldp-oper:global-lldp/Cisco-IOS-XR-ethernet-lldp-oper:lldp-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.hold_time is not None:
                    return True

                if self.re_init is not None:
                    return True

                if self.timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                return meta._meta_table['Lldp.GlobalLldp.LldpInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-lldp-oper:lldp/Cisco-IOS-XR-ethernet-lldp-oper:global-lldp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.lldp_info is not None and self.lldp_info._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
            return meta._meta_table['Lldp.GlobalLldp']['meta_info']


    class Nodes(object):
        """
        Per node LLDP operational data
        
        .. attribute:: node
        
        	The LLDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-lldp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            The LLDP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	The table of interfaces on which LLDP is running on this node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces>`
            
            .. attribute:: neighbors
            
            	The LLDP neighbor tables on this node
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors>`
            
            .. attribute:: statistics
            
            	The LLDP traffic statistics for this node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ethernet-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interfaces = Lldp.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.neighbors = Lldp.Nodes.Node.Neighbors()
                self.neighbors.parent = self
                self.statistics = Lldp.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Neighbors(object):
                """
                The LLDP neighbor tables on this node
                
                .. attribute:: details
                
                	The detailed LLDP neighbor table
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details>`
                
                .. attribute:: devices
                
                	The detailed LLDP neighbor table on this device
                	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices>`
                
                .. attribute:: summaries
                
                	The LLDP neighbor summary table
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.details = Lldp.Nodes.Node.Neighbors.Details()
                    self.details.parent = self
                    self.devices = Lldp.Nodes.Node.Neighbors.Devices()
                    self.devices.parent = self
                    self.summaries = Lldp.Nodes.Node.Neighbors.Summaries()
                    self.summaries.parent = self


                class Devices(object):
                    """
                    The detailed LLDP neighbor table on this
                    device
                    
                    .. attribute:: device
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.device = YList()
                        self.device.parent = self
                        self.device.name = 'device'


                    class Device(object):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.device_id = None
                            self.interface_name = None
                            self.lldp_neighbor = YList()
                            self.lldp_neighbor.parent = self
                            self.lldp_neighbor.name = 'lldp_neighbor'


                        class LldpNeighbor(object):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.detail = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self.device_id = None
                                self.enabled_capabilities = None
                                self.header_version = None
                                self.hold_time = None
                                self.mib = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self.platform = None
                                self.port_id_detail = None
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None


                            class Detail(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_negotiation = None
                                    self.enabled_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.physical_media_capabilities = None
                                    self.port_description = None
                                    self.port_vlan_id = None
                                    self.system_capabilities = None
                                    self.system_description = None
                                    self.system_name = None
                                    self.time_remaining = None


                                class NetworkAddresses(object):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_addr_entry = YList()
                                        self.lldp_addr_entry.parent = self
                                        self.lldp_addr_entry.name = 'lldp_addr_entry'


                                    class LldpAddrEntry(object):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self.if_num = None
                                            self.ma_subtype = None


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:address'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            if self.if_num is not None:
                                                return True

                                            if self.ma_subtype is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_addr_entry is not None:
                                            for child_ref in self.lldp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.auto_negotiation is not None:
                                        return True

                                    if self.enabled_capabilities is not None:
                                        return True

                                    if self.media_attachment_unit_type is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.physical_media_capabilities is not None:
                                        return True

                                    if self.port_description is not None:
                                        return True

                                    if self.port_vlan_id is not None:
                                        return True

                                    if self.system_capabilities is not None:
                                        return True

                                    if self.system_description is not None:
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.time_remaining is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail']['meta_info']


                            class Mib(object):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id_len = None
                                    self.chassis_id_sub_type = None
                                    self.combined_capabilities = None
                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self.port_id_len = None
                                    self.port_id_sub_type = None
                                    self.rem_index = None
                                    self.rem_local_port_num = None
                                    self.rem_time_mark = None
                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self


                                class UnknownTlvList(object):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_unknown_tlv_entry = YList()
                                        self.lldp_unknown_tlv_entry.parent = self
                                        self.lldp_unknown_tlv_entry.name = 'lldp_unknown_tlv_entry'


                                    class LldpUnknownTlvEntry(object):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.tlv_type = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-unknown-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.tlv_type is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:unknown-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_unknown_tlv_entry is not None:
                                            for child_ref in self.lldp_unknown_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList']['meta_info']


                                class OrgDefTlvList(object):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_org_def_tlv_entry = YList()
                                        self.lldp_org_def_tlv_entry.parent = self
                                        self.lldp_org_def_tlv_entry.name = 'lldp_org_def_tlv_entry'


                                    class LldpOrgDefTlvEntry(object):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.oui = None
                                            self.tlv_info_indes = None
                                            self.tlv_subtype = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-org-def-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.oui is not None:
                                                return True

                                            if self.tlv_info_indes is not None:
                                                return True

                                            if self.tlv_subtype is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:org-def-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_org_def_tlv_entry is not None:
                                            for child_ref in self.lldp_org_def_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:mib'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id_len is not None:
                                        return True

                                    if self.chassis_id_sub_type is not None:
                                        return True

                                    if self.combined_capabilities is not None:
                                        return True

                                    if self.org_def_tlv_list is not None and self.org_def_tlv_list._has_data():
                                        return True

                                    if self.port_id_len is not None:
                                        return True

                                    if self.port_id_sub_type is not None:
                                        return True

                                    if self.rem_index is not None:
                                        return True

                                    if self.rem_local_port_num is not None:
                                        return True

                                    if self.rem_time_mark is not None:
                                        return True

                                    if self.unknown_tlv_list is not None and self.unknown_tlv_list._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.enabled_capabilities is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.mib is not None and self.mib._has_data():
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id_detail is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                if self.receiving_parent_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:device'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.device_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.lldp_neighbor is not None:
                                for child_ref in self.lldp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:devices'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Devices']['meta_info']


                class Details(object):
                    """
                    The detailed LLDP neighbor table
                    
                    .. attribute:: detail
                    
                    	Detailed information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.detail = YList()
                        self.detail.parent = self
                        self.detail.name = 'detail'


                    class Detail(object):
                        """
                        Detailed information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.device_id = None
                            self.interface_name = None
                            self.lldp_neighbor = YList()
                            self.lldp_neighbor.parent = self
                            self.lldp_neighbor.name = 'lldp_neighbor'


                        class LldpNeighbor(object):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.detail = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_()
                                self.detail.parent = self
                                self.device_id = None
                                self.enabled_capabilities = None
                                self.header_version = None
                                self.hold_time = None
                                self.mib = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self.platform = None
                                self.port_id_detail = None
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None


                            class Detail_(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_negotiation = None
                                    self.enabled_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.physical_media_capabilities = None
                                    self.port_description = None
                                    self.port_vlan_id = None
                                    self.system_capabilities = None
                                    self.system_description = None
                                    self.system_name = None
                                    self.time_remaining = None


                                class NetworkAddresses(object):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_addr_entry = YList()
                                        self.lldp_addr_entry.parent = self
                                        self.lldp_addr_entry.name = 'lldp_addr_entry'


                                    class LldpAddrEntry(object):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self.if_num = None
                                            self.ma_subtype = None


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:address'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            if self.if_num is not None:
                                                return True

                                            if self.ma_subtype is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_addr_entry is not None:
                                            for child_ref in self.lldp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.auto_negotiation is not None:
                                        return True

                                    if self.enabled_capabilities is not None:
                                        return True

                                    if self.media_attachment_unit_type is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.physical_media_capabilities is not None:
                                        return True

                                    if self.port_description is not None:
                                        return True

                                    if self.port_vlan_id is not None:
                                        return True

                                    if self.system_capabilities is not None:
                                        return True

                                    if self.system_description is not None:
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.time_remaining is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_']['meta_info']


                            class Mib(object):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id_len = None
                                    self.chassis_id_sub_type = None
                                    self.combined_capabilities = None
                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self.port_id_len = None
                                    self.port_id_sub_type = None
                                    self.rem_index = None
                                    self.rem_local_port_num = None
                                    self.rem_time_mark = None
                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self


                                class UnknownTlvList(object):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_unknown_tlv_entry = YList()
                                        self.lldp_unknown_tlv_entry.parent = self
                                        self.lldp_unknown_tlv_entry.name = 'lldp_unknown_tlv_entry'


                                    class LldpUnknownTlvEntry(object):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.tlv_type = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-unknown-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.tlv_type is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:unknown-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_unknown_tlv_entry is not None:
                                            for child_ref in self.lldp_unknown_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList']['meta_info']


                                class OrgDefTlvList(object):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_org_def_tlv_entry = YList()
                                        self.lldp_org_def_tlv_entry.parent = self
                                        self.lldp_org_def_tlv_entry.name = 'lldp_org_def_tlv_entry'


                                    class LldpOrgDefTlvEntry(object):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.oui = None
                                            self.tlv_info_indes = None
                                            self.tlv_subtype = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-org-def-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.oui is not None:
                                                return True

                                            if self.tlv_info_indes is not None:
                                                return True

                                            if self.tlv_subtype is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:org-def-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_org_def_tlv_entry is not None:
                                            for child_ref in self.lldp_org_def_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:mib'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id_len is not None:
                                        return True

                                    if self.chassis_id_sub_type is not None:
                                        return True

                                    if self.combined_capabilities is not None:
                                        return True

                                    if self.org_def_tlv_list is not None and self.org_def_tlv_list._has_data():
                                        return True

                                    if self.port_id_len is not None:
                                        return True

                                    if self.port_id_sub_type is not None:
                                        return True

                                    if self.rem_index is not None:
                                        return True

                                    if self.rem_local_port_num is not None:
                                        return True

                                    if self.rem_time_mark is not None:
                                        return True

                                    if self.unknown_tlv_list is not None and self.unknown_tlv_list._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.enabled_capabilities is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.mib is not None and self.mib._has_data():
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id_detail is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                if self.receiving_parent_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:detail'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.device_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.lldp_neighbor is not None:
                                for child_ref in self.lldp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:details'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Details']['meta_info']


                class Summaries(object):
                    """
                    The LLDP neighbor summary table
                    
                    .. attribute:: summary
                    
                    	Brief information about a LLDP neighbor entry
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.summary = YList()
                        self.summary.parent = self
                        self.summary.name = 'summary'


                    class Summary(object):
                        """
                        Brief information about a LLDP neighbor
                        entry
                        
                        .. attribute:: device_id
                        
                        	The neighboring device identifier
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	The interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: lldp_neighbor
                        
                        	lldp neighbor
                        	**type**\: list of    :py:class:`LldpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.device_id = None
                            self.interface_name = None
                            self.lldp_neighbor = YList()
                            self.lldp_neighbor.parent = self
                            self.lldp_neighbor.name = 'lldp_neighbor'


                        class LldpNeighbor(object):
                            """
                            lldp neighbor
                            
                            .. attribute:: chassis_id
                            
                            	Chassis id
                            	**type**\:  str
                            
                            .. attribute:: detail
                            
                            	Detailed neighbor info
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail>`
                            
                            .. attribute:: device_id
                            
                            	Device identifier
                            	**type**\:  str
                            
                            .. attribute:: enabled_capabilities
                            
                            	Enabled Capabilities
                            	**type**\:  str
                            
                            .. attribute:: header_version
                            
                            	Version number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: hold_time
                            
                            	Remaining hold time
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mib
                            
                            	MIB nieghbor info
                            	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib>`
                            
                            .. attribute:: platform
                            
                            	Platform type
                            	**type**\:  str
                            
                            .. attribute:: port_id_detail
                            
                            	Outgoing port identifier
                            	**type**\:  str
                            
                            .. attribute:: receiving_interface_name
                            
                            	Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: receiving_parent_interface_name
                            
                            	Parent Interface the neighbor entry was received on 
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.detail = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail()
                                self.detail.parent = self
                                self.device_id = None
                                self.enabled_capabilities = None
                                self.header_version = None
                                self.hold_time = None
                                self.mib = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib()
                                self.mib.parent = self
                                self.platform = None
                                self.port_id_detail = None
                                self.receiving_interface_name = None
                                self.receiving_parent_interface_name = None


                            class Detail(object):
                                """
                                Detailed neighbor info
                                
                                .. attribute:: auto_negotiation
                                
                                	Auto Negotiation
                                	**type**\:  str
                                
                                .. attribute:: enabled_capabilities
                                
                                	Enabled Capabilities
                                	**type**\:  str
                                
                                .. attribute:: media_attachment_unit_type
                                
                                	Media Attachment Unit type
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_addresses
                                
                                	Management Addresses
                                	**type**\:   :py:class:`NetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses>`
                                
                                .. attribute:: physical_media_capabilities
                                
                                	Physical media capabilities
                                	**type**\:  str
                                
                                .. attribute:: port_description
                                
                                	Port Description
                                	**type**\:  str
                                
                                .. attribute:: port_vlan_id
                                
                                	Vlan ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_capabilities
                                
                                	System Capabilities
                                	**type**\:  str
                                
                                .. attribute:: system_description
                                
                                	System Description
                                	**type**\:  str
                                
                                .. attribute:: system_name
                                
                                	System Name
                                	**type**\:  str
                                
                                .. attribute:: time_remaining
                                
                                	Time remaining
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_negotiation = None
                                    self.enabled_capabilities = None
                                    self.media_attachment_unit_type = None
                                    self.network_addresses = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses()
                                    self.network_addresses.parent = self
                                    self.physical_media_capabilities = None
                                    self.port_description = None
                                    self.port_vlan_id = None
                                    self.system_capabilities = None
                                    self.system_description = None
                                    self.system_name = None
                                    self.time_remaining = None


                                class NetworkAddresses(object):
                                    """
                                    Management Addresses
                                    
                                    .. attribute:: lldp_addr_entry
                                    
                                    	lldp addr entry
                                    	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_addr_entry = YList()
                                        self.lldp_addr_entry.parent = self
                                        self.lldp_addr_entry.name = 'lldp_addr_entry'


                                    class LldpAddrEntry(object):
                                        """
                                        lldp addr entry
                                        
                                        .. attribute:: address
                                        
                                        	Network layer address
                                        	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address>`
                                        
                                        .. attribute:: if_num
                                        
                                        	Interface num
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ma_subtype
                                        
                                        	MA sub type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address()
                                            self.address.parent = self
                                            self.if_num = None
                                            self.ma_subtype = None


                                        class Address(object):
                                            """
                                            Network layer address
                                            
                                            .. attribute:: address_type
                                            
                                            	AddressType
                                            	**type**\:   :py:class:`LldpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocolEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ethernet-lldp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address_type = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:address'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-addr-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None and self.address._has_data():
                                                return True

                                            if self.if_num is not None:
                                                return True

                                            if self.ma_subtype is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:network-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_addr_entry is not None:
                                            for child_ref in self.lldp_addr_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.auto_negotiation is not None:
                                        return True

                                    if self.enabled_capabilities is not None:
                                        return True

                                    if self.media_attachment_unit_type is not None:
                                        return True

                                    if self.network_addresses is not None and self.network_addresses._has_data():
                                        return True

                                    if self.physical_media_capabilities is not None:
                                        return True

                                    if self.port_description is not None:
                                        return True

                                    if self.port_vlan_id is not None:
                                        return True

                                    if self.system_capabilities is not None:
                                        return True

                                    if self.system_description is not None:
                                        return True

                                    if self.system_name is not None:
                                        return True

                                    if self.time_remaining is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail']['meta_info']


                            class Mib(object):
                                """
                                MIB nieghbor info
                                
                                .. attribute:: chassis_id_len
                                
                                	Chassis ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: chassis_id_sub_type
                                
                                	Chassis ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: combined_capabilities
                                
                                	Supported and combined cpabilities
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: org_def_tlv_list
                                
                                	Org Def TLV list
                                	**type**\:   :py:class:`OrgDefTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList>`
                                
                                .. attribute:: port_id_len
                                
                                	Port ID length
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: port_id_sub_type
                                
                                	Port ID sub type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rem_index
                                
                                	lldpRemIndex
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_local_port_num
                                
                                	LldpPortNumber
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rem_time_mark
                                
                                	TimeFilter
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_tlv_list
                                
                                	Unknown TLV list
                                	**type**\:   :py:class:`UnknownTlvList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList>`
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id_len = None
                                    self.chassis_id_sub_type = None
                                    self.combined_capabilities = None
                                    self.org_def_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList()
                                    self.org_def_tlv_list.parent = self
                                    self.port_id_len = None
                                    self.port_id_sub_type = None
                                    self.rem_index = None
                                    self.rem_local_port_num = None
                                    self.rem_time_mark = None
                                    self.unknown_tlv_list = Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList()
                                    self.unknown_tlv_list.parent = self


                                class UnknownTlvList(object):
                                    """
                                    Unknown TLV list
                                    
                                    .. attribute:: lldp_unknown_tlv_entry
                                    
                                    	lldp unknown tlv entry
                                    	**type**\: list of    :py:class:`LldpUnknownTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_unknown_tlv_entry = YList()
                                        self.lldp_unknown_tlv_entry.parent = self
                                        self.lldp_unknown_tlv_entry.name = 'lldp_unknown_tlv_entry'


                                    class LldpUnknownTlvEntry(object):
                                        """
                                        lldp unknown tlv entry
                                        
                                        .. attribute:: tlv_type
                                        
                                        	Unknown TLV type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Unknown TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.tlv_type = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-unknown-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.tlv_type is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:unknown-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_unknown_tlv_entry is not None:
                                            for child_ref in self.lldp_unknown_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList']['meta_info']


                                class OrgDefTlvList(object):
                                    """
                                    Org Def TLV list
                                    
                                    .. attribute:: lldp_org_def_tlv_entry
                                    
                                    	lldp org def tlv entry
                                    	**type**\: list of    :py:class:`LldpOrgDefTlvEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry>`
                                    
                                    

                                    """

                                    _prefix = 'ethernet-lldp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lldp_org_def_tlv_entry = YList()
                                        self.lldp_org_def_tlv_entry.parent = self
                                        self.lldp_org_def_tlv_entry.name = 'lldp_org_def_tlv_entry'


                                    class LldpOrgDefTlvEntry(object):
                                        """
                                        lldp org def tlv entry
                                        
                                        .. attribute:: oui
                                        
                                        	Organizationally Unique Identifier
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_info_indes
                                        
                                        	lldpRemOrgDefInfoIndex
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: tlv_subtype
                                        
                                        	Org Def TLV subtype
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tlv_value
                                        
                                        	Org Def TLV payload
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ethernet-lldp-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.oui = None
                                            self.tlv_info_indes = None
                                            self.tlv_subtype = None
                                            self.tlv_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-org-def-tlv-entry'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.oui is not None:
                                                return True

                                            if self.tlv_info_indes is not None:
                                                return True

                                            if self.tlv_subtype is not None:
                                                return True

                                            if self.tlv_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:org-def-tlv-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lldp_org_def_tlv_entry is not None:
                                            for child_ref in self.lldp_org_def_tlv_entry:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:mib'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id_len is not None:
                                        return True

                                    if self.chassis_id_sub_type is not None:
                                        return True

                                    if self.combined_capabilities is not None:
                                        return True

                                    if self.org_def_tlv_list is not None and self.org_def_tlv_list._has_data():
                                        return True

                                    if self.port_id_len is not None:
                                        return True

                                    if self.port_id_sub_type is not None:
                                        return True

                                    if self.rem_index is not None:
                                        return True

                                    if self.rem_local_port_num is not None:
                                        return True

                                    if self.rem_time_mark is not None:
                                        return True

                                    if self.unknown_tlv_list is not None and self.unknown_tlv_list._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                if self.device_id is not None:
                                    return True

                                if self.enabled_capabilities is not None:
                                    return True

                                if self.header_version is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.mib is not None and self.mib._has_data():
                                    return True

                                if self.platform is not None:
                                    return True

                                if self.port_id_detail is not None:
                                    return True

                                if self.receiving_interface_name is not None:
                                    return True

                                if self.receiving_parent_interface_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.device_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.lldp_neighbor is not None:
                                for child_ref in self.lldp_neighbor:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                            return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:summaries'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                        return meta._meta_table['Lldp.Nodes.Node.Neighbors.Summaries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:neighbors'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                    return meta._meta_table['Lldp.Nodes.Node.Neighbors']['meta_info']


            class Interfaces(object):
                """
                The table of interfaces on which LLDP is
                running on this node
                
                .. attribute:: interface
                
                	Operational data for an interface on which LLDP is running
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Operational data for an interface on which
                    LLDP is running
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: if_index
                    
                    	ifIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: local_network_addresses
                    
                    	Local Management Addresses
                    	**type**\:   :py:class:`LocalNetworkAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses>`
                    
                    .. attribute:: port_description
                    
                    	Port Description
                    	**type**\:  str
                    
                    .. attribute:: port_id
                    
                    	Outgoing port identifier
                    	**type**\:  str
                    
                    .. attribute:: port_id_sub_type
                    
                    	Port ID sub type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_enabled
                    
                    	RX Enabled
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rx_state
                    
                    	RX State
                    	**type**\:  str
                    
                    .. attribute:: tx_enabled
                    
                    	TX Enabled
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: tx_state
                    
                    	TX State
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ethernet-lldp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.if_index = None
                        self.interface_name_xr = None
                        self.local_network_addresses = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses()
                        self.local_network_addresses.parent = self
                        self.port_description = None
                        self.port_id = None
                        self.port_id_sub_type = None
                        self.rx_enabled = None
                        self.rx_state = None
                        self.tx_enabled = None
                        self.tx_state = None


                    class LocalNetworkAddresses(object):
                        """
                        Local Management Addresses
                        
                        .. attribute:: lldp_addr_entry
                        
                        	lldp addr entry
                        	**type**\: list of    :py:class:`LldpAddrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry>`
                        
                        

                        """

                        _prefix = 'ethernet-lldp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lldp_addr_entry = YList()
                            self.lldp_addr_entry.parent = self
                            self.lldp_addr_entry.name = 'lldp_addr_entry'


                        class LldpAddrEntry(object):
                            """
                            lldp addr entry
                            
                            .. attribute:: address
                            
                            	Network layer address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address>`
                            
                            .. attribute:: if_num
                            
                            	Interface num
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ma_subtype
                            
                            	MA sub type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-lldp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address()
                                self.address.parent = self
                                self.if_num = None
                                self.ma_subtype = None


                            class Address(object):
                                """
                                Network layer address
                                
                                .. attribute:: address_type
                                
                                	AddressType
                                	**type**\:   :py:class:`LldpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper.LldpL3AddrProtocolEnum>`
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ethernet-lldp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_type = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:address'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                    return meta._meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:lldp-addr-entry'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.if_num is not None:
                                    return True

                                if self.ma_subtype is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                                return meta._meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:local-network-addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.lldp_addr_entry is not None:
                                for child_ref in self.lldp_addr_entry:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                            return meta._meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:interface[Cisco-IOS-XR-ethernet-lldp-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.if_index is not None:
                            return True

                        if self.interface_name_xr is not None:
                            return True

                        if self.local_network_addresses is not None and self.local_network_addresses._has_data():
                            return True

                        if self.port_description is not None:
                            return True

                        if self.port_id is not None:
                            return True

                        if self.port_id_sub_type is not None:
                            return True

                        if self.rx_enabled is not None:
                            return True

                        if self.rx_state is not None:
                            return True

                        if self.tx_enabled is not None:
                            return True

                        if self.tx_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                        return meta._meta_table['Lldp.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                    return meta._meta_table['Lldp.Nodes.Node.Interfaces']['meta_info']


            class Statistics(object):
                """
                The LLDP traffic statistics for this node
                
                .. attribute:: aged_out_entries
                
                	Aged out entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_packets
                
                	Bad packet received and dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_packets
                
                	Discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_tl_vs
                
                	Discarded TLVs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: encapsulation_errors
                
                	Transmission errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Out\-of\-memory conditions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: queue_overflow_errors
                
                	Queue overflows
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Received packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: table_overflow_errors
                
                	Table overflows
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: transmitted_packets
                
                	Transmitted packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unrecognized_tl_vs
                
                	Unrecognized TLVs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-lldp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aged_out_entries = None
                    self.bad_packets = None
                    self.discarded_packets = None
                    self.discarded_tl_vs = None
                    self.encapsulation_errors = None
                    self.out_of_memory_errors = None
                    self.queue_overflow_errors = None
                    self.received_packets = None
                    self.table_overflow_errors = None
                    self.transmitted_packets = None
                    self.unrecognized_tl_vs = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-lldp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aged_out_entries is not None:
                        return True

                    if self.bad_packets is not None:
                        return True

                    if self.discarded_packets is not None:
                        return True

                    if self.discarded_tl_vs is not None:
                        return True

                    if self.encapsulation_errors is not None:
                        return True

                    if self.out_of_memory_errors is not None:
                        return True

                    if self.queue_overflow_errors is not None:
                        return True

                    if self.received_packets is not None:
                        return True

                    if self.table_overflow_errors is not None:
                        return True

                    if self.transmitted_packets is not None:
                        return True

                    if self.unrecognized_tl_vs is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                    return meta._meta_table['Lldp.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ethernet-lldp-oper:lldp/Cisco-IOS-XR-ethernet-lldp-oper:nodes/Cisco-IOS-XR-ethernet-lldp-oper:node[Cisco-IOS-XR-ethernet-lldp-oper:node-name = ' + str(self.node_name) + ']'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
                return meta._meta_table['Lldp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-lldp-oper:lldp/Cisco-IOS-XR-ethernet-lldp-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
            return meta._meta_table['Lldp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ethernet-lldp-oper:lldp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.global_lldp is not None and self.global_lldp._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_lldp_oper as meta
        return meta._meta_table['Lldp']['meta_info']


