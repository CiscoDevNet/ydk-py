""" Cisco_IOS_XR_ipv6_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-network\: IPv6 network operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv6MaIfAddrStateEnum(Enum):
    """
    Ipv6MaIfAddrStateEnum

    Interface address states

    .. data:: active = 1

    	This is an active address that can appear as

    	the destination or source address of a packet

    .. data:: deprecated = 2

    	This is a valid but deprecated address that

    	should no longer be used as a source address in

    	new communications

    .. data:: duplicate = 3

    	This is a duplicate (invalid) address because

    	of conflict

    .. data:: inaccessible = 4

    	This is not accessible because the interface to

    	which this address is assigned is not

    	operational

    .. data:: tentative = 5

    	Status can not be determined for some reason

    """

    active = 1

    deprecated = 2

    duplicate = 3

    inaccessible = 4

    tentative = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaIfAddrStateEnum']


class Ipv6MaIfLineStateEnum(Enum):
    """
    Ipv6MaIfLineStateEnum

    Interface line states

    .. data:: down = 1

    	Interface state is down

    .. data:: up = 2

    	Interface state is up

    .. data:: unknown = 3

    	Interface state is unknown

    .. data:: error = 4

    	Interface state is incorrect

    """

    down = 1

    up = 2

    unknown = 3

    error = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaIfLineStateEnum']


class Ipv6MaOperStateEnum(Enum):
    """
    Ipv6MaOperStateEnum

    Interface oper states

    .. data:: oper_up = 1

    	Interface oper state is up

    .. data:: oper_down = 2

    	Interface oper state is down

    """

    oper_up = 1

    oper_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaOperStateEnum']



class Ipv6Network(object):
    """
    IPv6 network operational data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 network operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes>`
    
    

    """

    _prefix = 'ipv6-ma-oper'
    _revision = '2015-10-20'

    def __init__(self):
        self.nodes = Ipv6Network.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific IPv6 network operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-ma-oper'
        _revision = '2015-10-20'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv6 network operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_data
            
            	IPv6 network operational interface data
            	**type**\:   :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData>`
            
            

            """

            _prefix = 'ipv6-ma-oper'
            _revision = '2015-10-20'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interface_data = Ipv6Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self


            class InterfaceData(object):
                """
                IPv6 network operational interface data
                
                .. attribute:: summary
                
                	Summary of IPv6 network operational interface data on a node
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary>`
                
                .. attribute:: vrfs
                
                	VRF specific IPv6 network operational interface data
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs>`
                
                

                """

                _prefix = 'ipv6-ma-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    self.parent = None
                    self.summary = Ipv6Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self.vrfs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self


                class Vrfs(object):
                    """
                    VRF specific IPv6 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF ID of an interface belong to
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        VRF ID of an interface belong to
                        
                        .. attribute:: vrf_name  <key>
                        
                        	The VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv6 network operational data for a node
                        	**type**\:   :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        .. attribute:: global_briefs
                        
                        	Brief interface IPv6 network operational data from global data
                        	**type**\:   :py:class:`GlobalBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs>`
                        
                        .. attribute:: global_details
                        
                        	Detail interface IPv4 network operational data for global data
                        	**type**\:   :py:class:`GlobalDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self.details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self.global_briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs()
                            self.global_briefs.parent = self
                            self.global_details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails()
                            self.global_details.parent = self


                        class Briefs(object):
                            """
                            Brief interface IPv6 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.brief = YList()
                                self.brief.parent = self
                                self.brief.name = 'brief'


                            class Brief(object):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:   :py:class:`Ipv6MaIfLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineStateEnum>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.address = YList()
                                    self.address.parent = self
                                    self.address.name = 'address'
                                    self.line_state = None
                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress()
                                    self.link_local_address.parent = self


                                class LinkLocalAddress(object):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:link-local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress']['meta_info']


                                class Address(object):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:brief[Cisco-IOS-XR-ipv6-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.address is not None:
                                        for child_ref in self.address:
                                            if child_ref._has_data():
                                                return True

                                    if self.line_state is not None:
                                        return True

                                    if self.link_local_address is not None and self.link_local_address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:briefs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.brief is not None:
                                    for child_ref in self.brief:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info']


                        class GlobalDetails(object):
                            """
                            Detail interface IPv4 network operational
                            data for global data
                            
                            .. attribute:: global_detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of    :py:class:`GlobalDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.global_detail = YList()
                                self.global_detail.parent = self
                                self.global_detail.name = 'global_detail'


                            class GlobalDetail(object):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:   :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList>`
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime>`
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of    :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup>`
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\:  bool
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime>`
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\:  bool
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:   :py:class:`Ipv6MaIfLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineStateEnum>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress>`
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\:  bool
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:   :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList>`
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup>`
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:   :py:class:`Ipv6MaOperStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperStateEnum>`
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self.address = YList()
                                    self.address.parent = self
                                    self.address.name = 'address'
                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self.client_multicast_group = YList()
                                    self.client_multicast_group.parent = self
                                    self.client_multicast_group.name = 'client_multicast_group'
                                    self.flow_tag_dst = None
                                    self.flow_tag_src = None
                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self.is_icmp_unreach_enabled = None
                                    self.line_state = None
                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self.mlacp_active = None
                                    self.mtu = None
                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self.multicast_group = YList()
                                    self.multicast_group.parent = self
                                    self.multicast_group.name = 'multicast_group'
                                    self.operation_state = None
                                    self.rg_id_exists = None
                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf()
                                    self.rpf.parent = self
                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime()
                                    self.utime.parent = self


                                class LinkLocalAddress(object):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:link-local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress']['meta_info']


                                class AccessControlList(object):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self.in_bound = None
                                        self.out_bound = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:access-control-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.common_in_bound is not None:
                                            return True

                                        if self.common_out_bound is not None:
                                            return True

                                        if self.in_bound is not None:
                                            return True

                                        if self.out_bound is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList']['meta_info']


                                class MultiAccessControlList(object):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\:  list of str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.common = YLeafList()
                                        self.common.parent = self
                                        self.common.name = 'common'
                                        self.inbound = YLeafList()
                                        self.inbound.parent = self
                                        self.inbound.name = 'inbound'
                                        self.outbound = YLeafList()
                                        self.outbound.parent = self
                                        self.outbound.name = 'outbound'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:multi-access-control-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.common is not None:
                                            for child in self.common:
                                                if child is not None:
                                                    return True

                                        if self.inbound is not None:
                                            for child in self.inbound:
                                                if child is not None:
                                                    return True

                                        if self.outbound is not None:
                                            for child in self.outbound:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList']['meta_info']


                                class Rpf(object):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\:  bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\:  bool
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\:  bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.allow_default_route = None
                                        self.allow_self_ping = None
                                        self.enable = None
                                        self.mode = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:rpf'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.allow_default_route is not None:
                                            return True

                                        if self.allow_self_ping is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.mode is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf']['meta_info']


                                class BgpPa(object):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input()
                                        self.input.parent = self
                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output()
                                        self.output.parent = self


                                    class Input(object):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination = None
                                            self.enable = None
                                            self.source = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:input'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.destination is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.source is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input']['meta_info']


                                    class Output(object):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination = None
                                            self.enable = None
                                            self.source = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:output'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.destination is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.source is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:bgp-pa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.input is not None and self.input._has_data():
                                            return True

                                        if self.output is not None and self.output._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa']['meta_info']


                                class Utime(object):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime']['meta_info']


                                class IdbUtime(object):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:idb-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime']['meta_info']


                                class CapsUtime(object):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:caps-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime']['meta_info']


                                class FwdEnUtime(object):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:fwd-en-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime']['meta_info']


                                class FwdDisUtime(object):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:fwd-dis-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime']['meta_info']


                                class MulticastGroup(object):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:multicast-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup']['meta_info']


                                class Address(object):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address']['meta_info']


                                class ClientMulticastGroup(object):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:client-multicast-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:global-detail[Cisco-IOS-XR-ipv6-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.access_control_list is not None and self.access_control_list._has_data():
                                        return True

                                    if self.address is not None:
                                        for child_ref in self.address:
                                            if child_ref._has_data():
                                                return True

                                    if self.bgp_pa is not None and self.bgp_pa._has_data():
                                        return True

                                    if self.caps_utime is not None and self.caps_utime._has_data():
                                        return True

                                    if self.client_multicast_group is not None:
                                        for child_ref in self.client_multicast_group:
                                            if child_ref._has_data():
                                                return True

                                    if self.flow_tag_dst is not None:
                                        return True

                                    if self.flow_tag_src is not None:
                                        return True

                                    if self.fwd_dis_utime is not None and self.fwd_dis_utime._has_data():
                                        return True

                                    if self.fwd_en_utime is not None and self.fwd_en_utime._has_data():
                                        return True

                                    if self.idb_utime is not None and self.idb_utime._has_data():
                                        return True

                                    if self.is_icmp_unreach_enabled is not None:
                                        return True

                                    if self.line_state is not None:
                                        return True

                                    if self.link_local_address is not None and self.link_local_address._has_data():
                                        return True

                                    if self.mlacp_active is not None:
                                        return True

                                    if self.mtu is not None:
                                        return True

                                    if self.multi_access_control_list is not None and self.multi_access_control_list._has_data():
                                        return True

                                    if self.multicast_group is not None:
                                        for child_ref in self.multicast_group:
                                            if child_ref._has_data():
                                                return True

                                    if self.operation_state is not None:
                                        return True

                                    if self.rg_id_exists is not None:
                                        return True

                                    if self.rpf is not None and self.rpf._has_data():
                                        return True

                                    if self.utime is not None and self.utime._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:global-details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.global_detail is not None:
                                    for child_ref in self.global_detail:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails']['meta_info']


                        class GlobalBriefs(object):
                            """
                            Brief interface IPv6 network operational
                            data from global data
                            
                            .. attribute:: global_brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of    :py:class:`GlobalBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.global_brief = YList()
                                self.global_brief.parent = self
                                self.global_brief.name = 'global_brief'


                            class GlobalBrief(object):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:   :py:class:`Ipv6MaIfLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineStateEnum>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.address = YList()
                                    self.address.parent = self
                                    self.address.name = 'address'
                                    self.line_state = None
                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress()
                                    self.link_local_address.parent = self


                                class LinkLocalAddress(object):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:link-local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress']['meta_info']


                                class Address(object):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:global-brief[Cisco-IOS-XR-ipv6-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.address is not None:
                                        for child_ref in self.address:
                                            if child_ref._has_data():
                                                return True

                                    if self.line_state is not None:
                                        return True

                                    if self.link_local_address is not None and self.link_local_address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:global-briefs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.global_brief is not None:
                                    for child_ref in self.global_brief:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs']['meta_info']


                        class Details(object):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.detail = YList()
                                self.detail.parent = self
                                self.detail.name = 'detail'


                            class Detail(object):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:   :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList>`
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime>`
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of    :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup>`
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\:  bool
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime>`
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\:  bool
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:   :py:class:`Ipv6MaIfLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineStateEnum>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress>`
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\:  bool
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:   :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList>`
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:   :py:class:`Ipv6MaOperStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperStateEnum>`
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self.address = YList()
                                    self.address.parent = self
                                    self.address.name = 'address'
                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self.client_multicast_group = YList()
                                    self.client_multicast_group.parent = self
                                    self.client_multicast_group.name = 'client_multicast_group'
                                    self.flow_tag_dst = None
                                    self.flow_tag_src = None
                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self.is_icmp_unreach_enabled = None
                                    self.line_state = None
                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self.mlacp_active = None
                                    self.mtu = None
                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self.multicast_group = YList()
                                    self.multicast_group.parent = self
                                    self.multicast_group.name = 'multicast_group'
                                    self.operation_state = None
                                    self.rg_id_exists = None
                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime()
                                    self.utime.parent = self


                                class LinkLocalAddress(object):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:link-local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress']['meta_info']


                                class AccessControlList(object):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self.in_bound = None
                                        self.out_bound = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:access-control-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.common_in_bound is not None:
                                            return True

                                        if self.common_out_bound is not None:
                                            return True

                                        if self.in_bound is not None:
                                            return True

                                        if self.out_bound is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList']['meta_info']


                                class MultiAccessControlList(object):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\:  list of str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.common = YLeafList()
                                        self.common.parent = self
                                        self.common.name = 'common'
                                        self.inbound = YLeafList()
                                        self.inbound.parent = self
                                        self.inbound.name = 'inbound'
                                        self.outbound = YLeafList()
                                        self.outbound.parent = self
                                        self.outbound.name = 'outbound'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:multi-access-control-list'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.common is not None:
                                            for child in self.common:
                                                if child is not None:
                                                    return True

                                        if self.inbound is not None:
                                            for child in self.inbound:
                                                if child is not None:
                                                    return True

                                        if self.outbound is not None:
                                            for child in self.outbound:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList']['meta_info']


                                class Rpf(object):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\:  bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\:  bool
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\:  bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.allow_default_route = None
                                        self.allow_self_ping = None
                                        self.enable = None
                                        self.mode = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:rpf'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.allow_default_route is not None:
                                            return True

                                        if self.allow_self_ping is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.mode is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf']['meta_info']


                                class BgpPa(object):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self


                                    class Input(object):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination = None
                                            self.enable = None
                                            self.source = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:input'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.destination is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.source is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input']['meta_info']


                                    class Output(object):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination = None
                                            self.enable = None
                                            self.source = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:output'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.destination is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.source is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:bgp-pa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.input is not None and self.input._has_data():
                                            return True

                                        if self.output is not None and self.output._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']


                                class Utime(object):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime']['meta_info']


                                class IdbUtime(object):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:idb-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime']['meta_info']


                                class CapsUtime(object):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:caps-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime']['meta_info']


                                class FwdEnUtime(object):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:fwd-en-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime']['meta_info']


                                class FwdDisUtime(object):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:fwd-dis-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime']['meta_info']


                                class MulticastGroup(object):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:multicast-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup']['meta_info']


                                class Address(object):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrStateEnum>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\:  bool
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_state is not None:
                                            return True

                                        if self.is_anycast is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address']['meta_info']


                                class ClientMulticastGroup(object):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:client-multicast-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:detail[Cisco-IOS-XR-ipv6-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.access_control_list is not None and self.access_control_list._has_data():
                                        return True

                                    if self.address is not None:
                                        for child_ref in self.address:
                                            if child_ref._has_data():
                                                return True

                                    if self.bgp_pa is not None and self.bgp_pa._has_data():
                                        return True

                                    if self.caps_utime is not None and self.caps_utime._has_data():
                                        return True

                                    if self.client_multicast_group is not None:
                                        for child_ref in self.client_multicast_group:
                                            if child_ref._has_data():
                                                return True

                                    if self.flow_tag_dst is not None:
                                        return True

                                    if self.flow_tag_src is not None:
                                        return True

                                    if self.fwd_dis_utime is not None and self.fwd_dis_utime._has_data():
                                        return True

                                    if self.fwd_en_utime is not None and self.fwd_en_utime._has_data():
                                        return True

                                    if self.idb_utime is not None and self.idb_utime._has_data():
                                        return True

                                    if self.is_icmp_unreach_enabled is not None:
                                        return True

                                    if self.line_state is not None:
                                        return True

                                    if self.link_local_address is not None and self.link_local_address._has_data():
                                        return True

                                    if self.mlacp_active is not None:
                                        return True

                                    if self.mtu is not None:
                                        return True

                                    if self.multi_access_control_list is not None and self.multi_access_control_list._has_data():
                                        return True

                                    if self.multicast_group is not None:
                                        for child_ref in self.multicast_group:
                                            if child_ref._has_data():
                                                return True

                                    if self.operation_state is not None:
                                        return True

                                    if self.rg_id_exists is not None:
                                        return True

                                    if self.rpf is not None and self.rpf._has_data():
                                        return True

                                    if self.utime is not None and self.utime._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:details'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:vrf[Cisco-IOS-XR-ipv6-ma-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.briefs is not None and self.briefs._has_data():
                                return True

                            if self.details is not None and self.details._has_data():
                                return True

                            if self.global_briefs is not None and self.global_briefs._has_data():
                                return True

                            if self.global_details is not None and self.global_details._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs']['meta_info']


                class Summary(object):
                    """
                    Summary of IPv6 network operational interface
                    data on a node
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:   :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:   :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:   :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:   :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.if_down_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self.if_shutdown_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self.if_up_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self.if_up_down_basecaps_up = None
                        self.if_up_up = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self


                    class IfUpUp(object):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.ip_assigned = None
                            self.ip_unassigned = None
                            self.ip_unnumbered = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:if-up-up'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ip_assigned is not None:
                                return True

                            if self.ip_unassigned is not None:
                                return True

                            if self.ip_unnumbered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp']['meta_info']


                    class IfUpDown(object):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.ip_assigned = None
                            self.ip_unassigned = None
                            self.ip_unnumbered = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:if-up-down'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ip_assigned is not None:
                                return True

                            if self.ip_unassigned is not None:
                                return True

                            if self.ip_unnumbered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown']['meta_info']


                    class IfDownDown(object):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.ip_assigned = None
                            self.ip_unassigned = None
                            self.ip_unnumbered = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:if-down-down'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ip_assigned is not None:
                                return True

                            if self.ip_unassigned is not None:
                                return True

                            if self.ip_unnumbered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown']['meta_info']


                    class IfShutdownDown(object):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.ip_assigned = None
                            self.ip_unassigned = None
                            self.ip_unnumbered = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:if-shutdown-down'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ip_assigned is not None:
                                return True

                            if self.ip_unassigned is not None:
                                return True

                            if self.ip_unnumbered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.if_down_down is not None and self.if_down_down._has_data():
                            return True

                        if self.if_shutdown_down is not None and self.if_shutdown_down._has_data():
                            return True

                        if self.if_up_down is not None and self.if_up_down._has_data():
                            return True

                        if self.if_up_down_basecaps_up is not None:
                            return True

                        if self.if_up_up is not None and self.if_up_up._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-ma-oper:interface-data'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.summary is not None and self.summary._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/Cisco-IOS-XR-ipv6-ma-oper:nodes/Cisco-IOS-XR-ipv6-ma-oper:node[Cisco-IOS-XR-ipv6-ma-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.interface_data is not None and self.interface_data._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                return meta._meta_table['Ipv6Network.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/Cisco-IOS-XR-ipv6-ma-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
            return meta._meta_table['Ipv6Network.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ma-oper:ipv6-network'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6Network']['meta_info']


