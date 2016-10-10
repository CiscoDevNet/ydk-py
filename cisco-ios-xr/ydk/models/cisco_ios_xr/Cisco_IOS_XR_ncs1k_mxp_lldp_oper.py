""" Cisco_IOS_XR_ncs1k_mxp_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\-snoop\-data\: Information related to LLDP Snoop

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

    .. data:: IPV4 = 0

    	IPv4

    .. data:: IPV6 = 1

    	IPv6

    """

    IPV4 = 0

    IPV6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
        return meta._meta_table['LldpL3AddrProtocolEnum']



class LldpSnoopData(object):
    """
    Information related to LLDP Snoop
    
    .. attribute:: ethernet_controller_names
    
    	Ethernet controller snoop data
    	**type**\:  :py:class:`EthernetControllerNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames>`
    
    

    """

    _prefix = 'ncs1k-mxp-lldp-oper'
    _revision = '2016-04-05'

    def __init__(self):
        self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
        self.ethernet_controller_names.parent = self


    class EthernetControllerNames(object):
        """
        Ethernet controller snoop data
        
        .. attribute:: ethernet_controller_name
        
        	port Name
        	**type**\: list of  :py:class:`EthernetControllerName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName>`
        
        

        """

        _prefix = 'ncs1k-mxp-lldp-oper'
        _revision = '2016-04-05'

        def __init__(self):
            self.parent = None
            self.ethernet_controller_name = YList()
            self.ethernet_controller_name.parent = self
            self.ethernet_controller_name.name = 'ethernet_controller_name'


        class EthernetControllerName(object):
            """
            port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: chassis_id
            
            	Chassis id
            	**type**\:  str
            
            .. attribute:: enabled_capabilities
            
            	Enabled Capabilities
            	**type**\:  str
            
            .. attribute:: hold_time
            
            	Remaining hold time
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: lldp_neighbor
            
            	LldpNeighbor
            	**type**\:  str
            
            	**range:** 0..40
            
            .. attribute:: network_address
            
            	Management Address
            	**type**\:  :py:class:`NetworkAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress>`
            
            .. attribute:: port_description
            
            	Port Description
            	**type**\:  str
            
            .. attribute:: port_id_ckt
            
            	Outgoing port identifier circuit id
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: port_id_detail
            
            	Outgoing port identifier
            	**type**\:  str
            
            .. attribute:: source_mac
            
            	Mac address of the neighbor
            	**type**\:  str
            
            .. attribute:: system_capabilities
            
            	System Capabilities
            	**type**\:  str
            
            .. attribute:: system_description
            
            	System Description
            	**type**\:  str
            
            .. attribute:: system_name
            
            	System Name
            	**type**\:  str
            
            

            """

            _prefix = 'ncs1k-mxp-lldp-oper'
            _revision = '2016-04-05'

            def __init__(self):
                self.parent = None
                self.name = None
                self.chassis_id = None
                self.enabled_capabilities = None
                self.hold_time = None
                self.lldp_neighbor = None
                self.network_address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress()
                self.network_address.parent = self
                self.port_description = None
                self.port_id_ckt = None
                self.port_id_detail = None
                self.source_mac = None
                self.system_capabilities = None
                self.system_description = None
                self.system_name = None


            class NetworkAddress(object):
                """
                Management Address
                
                .. attribute:: address
                
                	Network layer address
                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress.Address>`
                
                .. attribute:: if_num
                
                	Interface num
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ma_subtype
                
                	MA sub type
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ncs1k-mxp-lldp-oper'
                _revision = '2016-04-05'

                def __init__(self):
                    self.parent = None
                    self.address = LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress.Address()
                    self.address.parent = self
                    self.if_num = None
                    self.ma_subtype = None


                class Address(object):
                    """
                    Network layer address
                    
                    .. attribute:: address_type
                    
                    	AddressType
                    	**type**\:  :py:class:`LldpL3AddrProtocolEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpL3AddrProtocolEnum>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-lldp-oper'
                    _revision = '2016-04-05'

                    def __init__(self):
                        self.parent = None
                        self.address_type = None
                        self.ipv4_address = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address_type is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
                        return meta._meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress.Address']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:network-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None and self.address._has_data():
                        return True

                    if self.if_num is not None:
                        return True

                    if self.ma_subtype is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
                    return meta._meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddress']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-names/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-name[Cisco-IOS-XR-ncs1k-mxp-lldp-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.chassis_id is not None:
                    return True

                if self.enabled_capabilities is not None:
                    return True

                if self.hold_time is not None:
                    return True

                if self.lldp_neighbor is not None:
                    return True

                if self.network_address is not None and self.network_address._has_data():
                    return True

                if self.port_description is not None:
                    return True

                if self.port_id_ckt is not None:
                    return True

                if self.port_id_detail is not None:
                    return True

                if self.source_mac is not None:
                    return True

                if self.system_capabilities is not None:
                    return True

                if self.system_description is not None:
                    return True

                if self.system_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
                return meta._meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ethernet_controller_name is not None:
                for child_ref in self.ethernet_controller_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
            return meta._meta_table['LldpSnoopData.EthernetControllerNames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ethernet_controller_names is not None and self.ethernet_controller_names._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
        return meta._meta_table['LldpSnoopData']['meta_info']


