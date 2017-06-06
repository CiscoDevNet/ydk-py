""" Cisco_IOS_XR_ipv4_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-network\: IPv4 network operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv4MaOperLineStateEnum(Enum):
    """
    Ipv4MaOperLineStateEnum

    Interface line states

    .. data:: unknown = 0

    	Interface state is unknown

    .. data:: shutdown = 1

    	Interface has been shutdown

    .. data:: down = 2

    	Interface state is down

    .. data:: up = 3

    	Interface state is up

    """

    unknown = 0

    shutdown = 1

    down = 2

    up = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
        return meta._meta_table['Ipv4MaOperLineStateEnum']


class RpfModeEnum(Enum):
    """
    RpfModeEnum

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = 0

    loose = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
        return meta._meta_table['RpfModeEnum']



class Ipv4Network(object):
    """
    IPv4 network operational data
    
    .. attribute:: interfaces
    
    	IPv4 network operational interface data
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces>`
    
    .. attribute:: nodes
    
    	Node\-specific IPv4 network operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes>`
    
    

    """

    _prefix = 'ipv4-io-oper'
    _revision = '2015-10-20'

    def __init__(self):
        self.interfaces = Ipv4Network.Interfaces()
        self.interfaces.parent = self
        self.nodes = Ipv4Network.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific IPv4 network operational data
        
        .. attribute:: node
        
        	IPv4 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-io-oper'
        _revision = '2015-10-20'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv4 network operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_data
            
            	IPv4 network operational interface data
            	**type**\:   :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData>`
            
            .. attribute:: statistics
            
            	Statistical IPv4 network operational data for a node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ipv4-io-oper'
            _revision = '2015-10-20'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interface_data = Ipv4Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self.statistics = Ipv4Network.Nodes.Node.Statistics()
                self.statistics.parent = self


            class InterfaceData(object):
                """
                IPv4 network operational interface data
                
                .. attribute:: summary
                
                	Summary of IPv4 network operational interface data on a node
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary>`
                
                .. attribute:: vrfs
                
                	VRF specific IPv4 network operational interface data
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    self.parent = None
                    self.summary = Ipv4Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self.vrfs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self


                class Vrfs(object):
                    """
                    VRF specific IPv4 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF name of an interface belong to
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        VRF name of an interface belong to
                        
                        .. attribute:: vrf_name  <key>
                        
                        	The VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv4 network operational data for a node
                        	**type**\:   :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.briefs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self.details = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self


                        class Briefs(object):
                            """
                            Brief interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv4 network operational data for an interface
                            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.brief = YList()
                                self.brief.parent = self
                                self.brief.name = 'brief'


                            class Brief(object):
                                """
                                Brief interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:   :py:class:`Ipv4MaOperLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineStateEnum>`
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.line_state = None
                                    self.primary_address = None
                                    self.vrf_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:brief[Cisco-IOS-XR-ipv4-io-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.line_state is not None:
                                        return True

                                    if self.primary_address is not None:
                                        return True

                                    if self.vrf_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                    return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:briefs'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info']


                        class Details(object):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv4 network operational data for an interface
                            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.detail = YList()
                                self.detail.parent = self
                                self.detail.name = 'detail'


                            class Detail(object):
                                """
                                Detail interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl
                                
                                	ACLs configured on the interface
                                	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime>`
                                
                                .. attribute:: direct_broadcast
                                
                                	Are direct broadcasts sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\:  bool
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime>`
                                
                                .. attribute:: helper_address
                                
                                	Helper Addresses configured on the interface
                                	**type**\:   :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime>`
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:   :py:class:`Ipv4MaOperLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineStateEnum>`
                                
                                .. attribute:: mask_reply
                                
                                	Are mask replies sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\:  bool
                                
                                .. attribute:: mtu
                                
                                	IP MTU of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: multi_acl
                                
                                	Multi ACLs configured on the interface
                                	**type**\:   :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl>`
                                
                                .. attribute:: multicast_group
                                
                                	Multicast groups joined on the interface
                                	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length of primary address
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: proxy_arp_disabled
                                
                                	Is Proxy ARP disabled on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: pub_utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime>`
                                
                                .. attribute:: redirect
                                
                                	Are ICMP redirects sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: route_tag
                                
                                	Route tag associated with the primary address (0 = no tag)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: secondary_address
                                
                                	Secondary addresses on the interface
                                	**type**\: list of    :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress>`
                                
                                .. attribute:: unnumbered_interface_name
                                
                                	Name of referenced interface (valid if unnumbered)
                                	**type**\:  str
                                
                                .. attribute:: unreachable
                                
                                	Are ICMP unreachables sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl()
                                    self.acl.parent = self
                                    self.bgp_pa = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self.caps_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self.direct_broadcast = None
                                    self.flow_tag_dst = None
                                    self.flow_tag_src = None
                                    self.fwd_dis_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self.fwd_en_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self.helper_address = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress()
                                    self.helper_address.parent = self
                                    self.idb_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self.line_state = None
                                    self.mask_reply = None
                                    self.mlacp_active = None
                                    self.mtu = None
                                    self.multi_acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl()
                                    self.multi_acl.parent = self
                                    self.multicast_group = YList()
                                    self.multicast_group.parent = self
                                    self.multicast_group.name = 'multicast_group'
                                    self.prefix_length = None
                                    self.primary_address = None
                                    self.proxy_arp_disabled = None
                                    self.pub_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime()
                                    self.pub_utime.parent = self
                                    self.redirect = None
                                    self.rg_id_exists = None
                                    self.route_tag = None
                                    self.rpf = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self.secondary_address = YList()
                                    self.secondary_address.parent = self
                                    self.secondary_address.name = 'secondary_address'
                                    self.unnumbered_interface_name = None
                                    self.unreachable = None
                                    self.vrf_id = None


                                class Acl(object):
                                    """
                                    ACLs configured on the interface
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    .. attribute:: inbound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: outbound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self.inbound = None
                                        self.outbound = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:acl'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.common_in_bound is not None:
                                            return True

                                        if self.common_out_bound is not None:
                                            return True

                                        if self.inbound is not None:
                                            return True

                                        if self.outbound is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl']['meta_info']


                                class MultiAcl(object):
                                    """
                                    Multi ACLs configured on the interface
                                    
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

                                    _prefix = 'ipv4-io-oper'
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

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:multi-acl'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl']['meta_info']


                                class HelperAddress(object):
                                    """
                                    Helper Addresses configured on the interface
                                    
                                    .. attribute:: address_array
                                    
                                    	Helper address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address_array = YLeafList()
                                        self.address_array.parent = self
                                        self.address_array.name = 'address_array'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:helper-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_array is not None:
                                            for child in self.address_array:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress']['meta_info']


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
                                    	**type**\:   :py:class:`RpfModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.RpfModeEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
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

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:rpf'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf']['meta_info']


                                class BgpPa(object):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.input = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self.output = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self


                                    class Input(object):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
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

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:input'

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
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input']['meta_info']


                                    class Output(object):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
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

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:output'

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
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:bgp-pa'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']


                                class PubUtime(object):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:pub-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime']['meta_info']


                                class IdbUtime(object):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:idb-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime']['meta_info']


                                class CapsUtime(object):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:caps-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime']['meta_info']


                                class FwdEnUtime(object):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:fwd-en-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime']['meta_info']


                                class FwdDisUtime(object):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:fwd-dis-utime'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime']['meta_info']


                                class MulticastGroup(object):
                                    """
                                    Multicast groups joined on the interface
                                    
                                    .. attribute:: group_address
                                    
                                    	Address of multicast group
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.group_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:multicast-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.group_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup']['meta_info']


                                class SecondaryAddress(object):
                                    """
                                    Secondary addresses on the interface
                                    
                                    .. attribute:: address
                                    
                                    	Address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length of address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route Tag associated with this address (0 = no tag)
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.prefix_length = None
                                        self.route_tag = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:secondary-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        if self.route_tag is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:detail[Cisco-IOS-XR-ipv4-io-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.acl is not None and self.acl._has_data():
                                        return True

                                    if self.bgp_pa is not None and self.bgp_pa._has_data():
                                        return True

                                    if self.caps_utime is not None and self.caps_utime._has_data():
                                        return True

                                    if self.direct_broadcast is not None:
                                        return True

                                    if self.flow_tag_dst is not None:
                                        return True

                                    if self.flow_tag_src is not None:
                                        return True

                                    if self.fwd_dis_utime is not None and self.fwd_dis_utime._has_data():
                                        return True

                                    if self.fwd_en_utime is not None and self.fwd_en_utime._has_data():
                                        return True

                                    if self.helper_address is not None and self.helper_address._has_data():
                                        return True

                                    if self.idb_utime is not None and self.idb_utime._has_data():
                                        return True

                                    if self.line_state is not None:
                                        return True

                                    if self.mask_reply is not None:
                                        return True

                                    if self.mlacp_active is not None:
                                        return True

                                    if self.mtu is not None:
                                        return True

                                    if self.multi_acl is not None and self.multi_acl._has_data():
                                        return True

                                    if self.multicast_group is not None:
                                        for child_ref in self.multicast_group:
                                            if child_ref._has_data():
                                                return True

                                    if self.prefix_length is not None:
                                        return True

                                    if self.primary_address is not None:
                                        return True

                                    if self.proxy_arp_disabled is not None:
                                        return True

                                    if self.pub_utime is not None and self.pub_utime._has_data():
                                        return True

                                    if self.redirect is not None:
                                        return True

                                    if self.rg_id_exists is not None:
                                        return True

                                    if self.route_tag is not None:
                                        return True

                                    if self.rpf is not None and self.rpf._has_data():
                                        return True

                                    if self.secondary_address is not None:
                                        for child_ref in self.secondary_address:
                                            if child_ref._has_data():
                                                return True

                                    if self.unnumbered_interface_name is not None:
                                        return True

                                    if self.unreachable is not None:
                                        return True

                                    if self.vrf_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                    return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:details'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:vrf[Cisco-IOS-XR-ipv4-io-oper:vrf-name = ' + str(self.vrf_name) + ']'

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

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:vrfs'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs']['meta_info']


                class Summary(object):
                    """
                    Summary of IPv4 network operational interface
                    data on a node
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:   :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:   :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:   :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:   :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.if_down_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self.if_shutdown_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self.if_up_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self.if_up_down_basecaps_up = None
                        self.if_up_up = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self


                    class IfUpUp(object):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:if-up-up'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp']['meta_info']


                    class IfUpDown(object):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:if-up-down'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown']['meta_info']


                    class IfDownDown(object):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:if-down-down'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown']['meta_info']


                    class IfShutdownDown(object):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:if-shutdown-down'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:summary'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                        return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:interface-data'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                    return meta._meta_table['Ipv4Network.Nodes.Node.InterfaceData']['meta_info']


            class Statistics(object):
                """
                Statistical IPv4 network operational data for
                a node
                
                .. attribute:: traffic
                
                	Traffic statistics for a node
                	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    self.parent = None
                    self.traffic = Ipv4Network.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self


                class Traffic(object):
                    """
                    Traffic statistics for a node
                    
                    .. attribute:: icmp_stats
                    
                    	ICMP Stats
                    	**type**\:   :py:class:`IcmpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats>`
                    
                    .. attribute:: ipv4_stats
                    
                    	IPv4 Network Stats
                    	**type**\:   :py:class:`Ipv4Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.icmp_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats()
                        self.icmp_stats.parent = self
                        self.ipv4_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats()
                        self.ipv4_stats.parent = self


                    class Ipv4Stats(object):
                        """
                        IPv4 Network Stats
                        
                        .. attribute:: bad_header
                        
                        	Bad Header
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hop_count
                        
                        	Bad Hop Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_option
                        
                        	Bad Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_security_option
                        
                        	Bad Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_source_address
                        
                        	Bad Source Address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: basic_security_option
                        
                        	Basic Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_in
                        
                        	Broadcast In
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_out
                        
                        	Broadcast Out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipso_option
                        
                        	Cipso Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encapsulation_failed
                        
                        	Encapsulation Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_option
                        
                        	End Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: extended_security_option
                        
                        	Extended Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format_errors
                        
                        	Format Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_count
                        
                        	Fragment Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: input_packets
                        
                        	Input Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_decap_error
                        
                        	Lisp decap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_encap_error
                        
                        	Lisp encap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_decap
                        
                        	Lisp IPv4 decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_encap
                        
                        	Lisp IPv4 encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_decap
                        
                        	Lisp IPv6 decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_encap
                        
                        	Lisp IPv6 encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: loose_source_route_option
                        
                        	Loose Source Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_in
                        
                        	Multicast In
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_out
                        
                        	Multicast Out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_gateway
                        
                        	No Gateway
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_protocol
                        
                        	No Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_router
                        
                        	No Router
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: noop_option
                        
                        	Noop Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: options_present
                        
                        	IP Options Present
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packet_too_big
                        
                        	Packet Too Big
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_forwarded
                        
                        	Packets Forwarded
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_fragmented
                        
                        	Packets Fragmented
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_output
                        
                        	Packets Output
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_failed
                        
                        	Reassembly Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_input
                        
                        	RaInput
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_max_drop
                        
                        	Reassembly Max Drop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_timeout
                        
                        	Reassembly Timeout
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembled
                        
                        	Reassembled
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_packets
                        
                        	Received Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: record_route_option
                        
                        	Record Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_alert_option
                        
                        	Router Alert Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid_option
                        
                        	SID Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: strict_source_route_option
                        
                        	Strict Source Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_option
                        
                        	Timestamp Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_option
                        
                        	Unknown Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.bad_header = None
                            self.bad_hop_count = None
                            self.bad_option = None
                            self.bad_security_option = None
                            self.bad_source_address = None
                            self.basic_security_option = None
                            self.broadcast_in = None
                            self.broadcast_out = None
                            self.cipso_option = None
                            self.encapsulation_failed = None
                            self.end_option = None
                            self.extended_security_option = None
                            self.format_errors = None
                            self.fragment_count = None
                            self.input_packets = None
                            self.lisp_decap_error = None
                            self.lisp_encap_error = None
                            self.lisp_v4_decap = None
                            self.lisp_v4_encap = None
                            self.lisp_v6_decap = None
                            self.lisp_v6_encap = None
                            self.loose_source_route_option = None
                            self.multicast_in = None
                            self.multicast_out = None
                            self.no_gateway = None
                            self.no_protocol = None
                            self.no_router = None
                            self.noop_option = None
                            self.options_present = None
                            self.packet_too_big = None
                            self.packets_forwarded = None
                            self.packets_fragmented = None
                            self.packets_output = None
                            self.reassemble_failed = None
                            self.reassemble_input = None
                            self.reassemble_max_drop = None
                            self.reassemble_timeout = None
                            self.reassembled = None
                            self.received_packets = None
                            self.record_route_option = None
                            self.router_alert_option = None
                            self.sid_option = None
                            self.strict_source_route_option = None
                            self.timestamp_option = None
                            self.unknown_option = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:ipv4-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_header is not None:
                                return True

                            if self.bad_hop_count is not None:
                                return True

                            if self.bad_option is not None:
                                return True

                            if self.bad_security_option is not None:
                                return True

                            if self.bad_source_address is not None:
                                return True

                            if self.basic_security_option is not None:
                                return True

                            if self.broadcast_in is not None:
                                return True

                            if self.broadcast_out is not None:
                                return True

                            if self.cipso_option is not None:
                                return True

                            if self.encapsulation_failed is not None:
                                return True

                            if self.end_option is not None:
                                return True

                            if self.extended_security_option is not None:
                                return True

                            if self.format_errors is not None:
                                return True

                            if self.fragment_count is not None:
                                return True

                            if self.input_packets is not None:
                                return True

                            if self.lisp_decap_error is not None:
                                return True

                            if self.lisp_encap_error is not None:
                                return True

                            if self.lisp_v4_decap is not None:
                                return True

                            if self.lisp_v4_encap is not None:
                                return True

                            if self.lisp_v6_decap is not None:
                                return True

                            if self.lisp_v6_encap is not None:
                                return True

                            if self.loose_source_route_option is not None:
                                return True

                            if self.multicast_in is not None:
                                return True

                            if self.multicast_out is not None:
                                return True

                            if self.no_gateway is not None:
                                return True

                            if self.no_protocol is not None:
                                return True

                            if self.no_router is not None:
                                return True

                            if self.noop_option is not None:
                                return True

                            if self.options_present is not None:
                                return True

                            if self.packet_too_big is not None:
                                return True

                            if self.packets_forwarded is not None:
                                return True

                            if self.packets_fragmented is not None:
                                return True

                            if self.packets_output is not None:
                                return True

                            if self.reassemble_failed is not None:
                                return True

                            if self.reassemble_input is not None:
                                return True

                            if self.reassemble_max_drop is not None:
                                return True

                            if self.reassemble_timeout is not None:
                                return True

                            if self.reassembled is not None:
                                return True

                            if self.received_packets is not None:
                                return True

                            if self.record_route_option is not None:
                                return True

                            if self.router_alert_option is not None:
                                return True

                            if self.sid_option is not None:
                                return True

                            if self.strict_source_route_option is not None:
                                return True

                            if self.timestamp_option is not None:
                                return True

                            if self.unknown_option is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats']['meta_info']


                    class IcmpStats(object):
                        """
                        ICMP Stats
                        
                        .. attribute:: admin_unreachable_received
                        
                        	ICMP Admin Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_unreachable_sent
                        
                        	ICMP Admin Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: checksum_error
                        
                        	ICMP Checksum Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_received
                        
                        	ICMP Echo Reply Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_sent
                        
                        	ICMP Echo Reply Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_received
                        
                        	ICMP Echo Request Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_sent
                        
                        	ICMP Echo Request Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_received
                        
                        	ICMP Fragment Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_sent
                        
                        	ICMP Fragment Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_received
                        
                        	ICMP Hopcount Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_sent
                        
                        	ICMP Hopcount Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_received
                        
                        	ICMP Host Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_sent
                        
                        	ICMP Host Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_received
                        
                        	ICMP Mask Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_sent
                        
                        	ICMP Mask Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_received
                        
                        	ICMP Mask Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_sent
                        
                        	ICMP Mask Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_received
                        
                        	ICMP Network Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_sent
                        
                        	ICMP Network Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: output
                        
                        	ICMP Transmitted
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_received
                        
                        	ICMP Parameter Error Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_send
                        
                        	ICMP Parameter Error Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_received
                        
                        	ICMP Port Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_sent
                        
                        	ICMP Port Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_received
                        
                        	ICMP Protocol Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_sent
                        
                        	ICMP Protocol Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassebly_received
                        
                        	ICMP Reassembly Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_sent
                        
                        	ICMP Reassembly Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	ICMP Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_received
                        
                        	ICMP Redirect Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_send
                        
                        	ICMP Redirect Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_advert_received
                        
                        	ICMP Router Advertisement Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_solicit_received
                        
                        	ICMP Router Solicited Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_quench_received
                        
                        	ICMP Source Quench
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_received
                        
                        	ICMP Timestamp Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_reply_received
                        
                        	ICMP Timestamp Reply Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown
                        
                        	ICMP Unknown
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.admin_unreachable_received = None
                            self.admin_unreachable_sent = None
                            self.checksum_error = None
                            self.echo_reply_received = None
                            self.echo_reply_sent = None
                            self.echo_request_received = None
                            self.echo_request_sent = None
                            self.fragment_unreachable_received = None
                            self.fragment_unreachable_sent = None
                            self.hopcount_received = None
                            self.hopcount_sent = None
                            self.host_unreachable_received = None
                            self.host_unreachable_sent = None
                            self.mask_reply_received = None
                            self.mask_reply_sent = None
                            self.mask_request_received = None
                            self.mask_request_sent = None
                            self.network_unreachable_received = None
                            self.network_unreachable_sent = None
                            self.output = None
                            self.param_error_received = None
                            self.param_error_send = None
                            self.port_unreachable_received = None
                            self.port_unreachable_sent = None
                            self.protocol_unreachable_received = None
                            self.protocol_unreachable_sent = None
                            self.reassebly_received = None
                            self.reassembly_sent = None
                            self.received = None
                            self.redirect_received = None
                            self.redirect_send = None
                            self.router_advert_received = None
                            self.router_solicit_received = None
                            self.source_quench_received = None
                            self.timestamp_received = None
                            self.timestamp_reply_received = None
                            self.unknown = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:icmp-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.admin_unreachable_received is not None:
                                return True

                            if self.admin_unreachable_sent is not None:
                                return True

                            if self.checksum_error is not None:
                                return True

                            if self.echo_reply_received is not None:
                                return True

                            if self.echo_reply_sent is not None:
                                return True

                            if self.echo_request_received is not None:
                                return True

                            if self.echo_request_sent is not None:
                                return True

                            if self.fragment_unreachable_received is not None:
                                return True

                            if self.fragment_unreachable_sent is not None:
                                return True

                            if self.hopcount_received is not None:
                                return True

                            if self.hopcount_sent is not None:
                                return True

                            if self.host_unreachable_received is not None:
                                return True

                            if self.host_unreachable_sent is not None:
                                return True

                            if self.mask_reply_received is not None:
                                return True

                            if self.mask_reply_sent is not None:
                                return True

                            if self.mask_request_received is not None:
                                return True

                            if self.mask_request_sent is not None:
                                return True

                            if self.network_unreachable_received is not None:
                                return True

                            if self.network_unreachable_sent is not None:
                                return True

                            if self.output is not None:
                                return True

                            if self.param_error_received is not None:
                                return True

                            if self.param_error_send is not None:
                                return True

                            if self.port_unreachable_received is not None:
                                return True

                            if self.port_unreachable_sent is not None:
                                return True

                            if self.protocol_unreachable_received is not None:
                                return True

                            if self.protocol_unreachable_sent is not None:
                                return True

                            if self.reassebly_received is not None:
                                return True

                            if self.reassembly_sent is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.redirect_received is not None:
                                return True

                            if self.redirect_send is not None:
                                return True

                            if self.router_advert_received is not None:
                                return True

                            if self.router_solicit_received is not None:
                                return True

                            if self.source_quench_received is not None:
                                return True

                            if self.timestamp_received is not None:
                                return True

                            if self.timestamp_reply_received is not None:
                                return True

                            if self.unknown is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.icmp_stats is not None and self.icmp_stats._has_data():
                            return True

                        if self.ipv4_stats is not None and self.ipv4_stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                        return meta._meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-io-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.traffic is not None and self.traffic._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                    return meta._meta_table['Ipv4Network.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-io-oper:nodes/Cisco-IOS-XR-ipv4-io-oper:node[Cisco-IOS-XR-ipv4-io-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.interface_data is not None and self.interface_data._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                return meta._meta_table['Ipv4Network.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-io-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
            return meta._meta_table['Ipv4Network.Nodes']['meta_info']


    class Interfaces(object):
        """
        IPv4 network operational interface data
        
        .. attribute:: interface
        
        	Interface names with VRF
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-ma-oper'
        _revision = '2015-10-20'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Interface names with VRF
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: vrfs
            
            	List of VRF on the interface
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs>`
            
            

            """

            _prefix = 'ipv4-ma-oper'
            _revision = '2015-10-20'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.vrfs = Ipv4Network.Interfaces.Interface.Vrfs()
                self.vrfs.parent = self


            class Vrfs(object):
                """
                List of VRF on the interface
                
                .. attribute:: vrf
                
                	VRF information on the interface
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ipv4-ma-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    VRF information on the interface
                    
                    .. attribute:: vrf_name  <key>
                    
                    	The VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: brief
                    
                    	Brief IPv4 network operational data for an interface
                    	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief>`
                    
                    .. attribute:: detail
                    
                    	Detail IPv4 network operational data for an interface
                    	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail>`
                    
                    

                    """

                    _prefix = 'ipv4-ma-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.brief = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief()
                        self.brief.parent = self
                        self.detail = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail()
                        self.detail.parent = self


                    class Detail(object):
                        """
                        Detail IPv4 network operational data for an
                        interface
                        
                        .. attribute:: acl
                        
                        	ACLs configured on the interface
                        	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl>`
                        
                        .. attribute:: bgp_pa
                        
                        	BGP PA config on the interface
                        	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa>`
                        
                        .. attribute:: caps_utime
                        
                        	CAPS Add Time
                        	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime>`
                        
                        .. attribute:: direct_broadcast
                        
                        	Are direct broadcasts sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: flow_tag_dst
                        
                        	Is BGP Flow Tag Destination is enable
                        	**type**\:  bool
                        
                        .. attribute:: flow_tag_src
                        
                        	Is BGP Flow Tag Source is enable
                        	**type**\:  bool
                        
                        .. attribute:: fwd_dis_utime
                        
                        	FWD DISABLE Time
                        	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime>`
                        
                        .. attribute:: fwd_en_utime
                        
                        	FWD ENABLE Time
                        	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime>`
                        
                        .. attribute:: helper_address
                        
                        	Helper Addresses configured on the interface
                        	**type**\:   :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress>`
                        
                        .. attribute:: idb_utime
                        
                        	IDB Create Time
                        	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime>`
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:   :py:class:`Ipv4MaOperLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineStateEnum>`
                        
                        .. attribute:: mask_reply
                        
                        	Are mask replies sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: mlacp_active
                        
                        	Is mLACP state Active (valid if RG ID exists)
                        	**type**\:  bool
                        
                        .. attribute:: mtu
                        
                        	IP MTU of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multi_acl
                        
                        	Multi ACLs configured on the interface
                        	**type**\:   :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl>`
                        
                        .. attribute:: multicast_group
                        
                        	Multicast groups joined on the interface
                        	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of primary address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: proxy_arp_disabled
                        
                        	Is Proxy ARP disabled on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: pub_utime
                        
                        	Address Publish Time
                        	**type**\:   :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime>`
                        
                        .. attribute:: redirect
                        
                        	Are ICMP redirects sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: rg_id_exists
                        
                        	Does ICCP RG ID exist on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: route_tag
                        
                        	Route tag associated with the primary address (0 = no tag)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rpf
                        
                        	RPF config on the interface
                        	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf>`
                        
                        .. attribute:: secondary_address
                        
                        	Secondary addresses on the interface
                        	**type**\: list of    :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress>`
                        
                        .. attribute:: unnumbered_interface_name
                        
                        	Name of referenced interface (valid if unnumbered)
                        	**type**\:  str
                        
                        .. attribute:: unreachable
                        
                        	Are ICMP unreachables sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl()
                            self.acl.parent = self
                            self.bgp_pa = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa()
                            self.bgp_pa.parent = self
                            self.caps_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime()
                            self.caps_utime.parent = self
                            self.direct_broadcast = None
                            self.flow_tag_dst = None
                            self.flow_tag_src = None
                            self.fwd_dis_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime()
                            self.fwd_dis_utime.parent = self
                            self.fwd_en_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime()
                            self.fwd_en_utime.parent = self
                            self.helper_address = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress()
                            self.helper_address.parent = self
                            self.idb_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime()
                            self.idb_utime.parent = self
                            self.line_state = None
                            self.mask_reply = None
                            self.mlacp_active = None
                            self.mtu = None
                            self.multi_acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl()
                            self.multi_acl.parent = self
                            self.multicast_group = YList()
                            self.multicast_group.parent = self
                            self.multicast_group.name = 'multicast_group'
                            self.prefix_length = None
                            self.primary_address = None
                            self.proxy_arp_disabled = None
                            self.pub_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime()
                            self.pub_utime.parent = self
                            self.redirect = None
                            self.rg_id_exists = None
                            self.route_tag = None
                            self.rpf = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf()
                            self.rpf.parent = self
                            self.secondary_address = YList()
                            self.secondary_address.parent = self
                            self.secondary_address.name = 'secondary_address'
                            self.unnumbered_interface_name = None
                            self.unreachable = None
                            self.vrf_id = None


                        class Acl(object):
                            """
                            ACLs configured on the interface
                            
                            .. attribute:: common_in_bound
                            
                            	Common ACL applied to incoming packets
                            	**type**\:  str
                            
                            .. attribute:: common_out_bound
                            
                            	Common ACL applied to outgoing packets
                            	**type**\:  str
                            
                            .. attribute:: inbound
                            
                            	ACL applied to incoming packets
                            	**type**\:  str
                            
                            .. attribute:: outbound
                            
                            	ACL applied to outgoing packets
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.common_in_bound = None
                                self.common_out_bound = None
                                self.inbound = None
                                self.outbound = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:acl'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.common_in_bound is not None:
                                    return True

                                if self.common_out_bound is not None:
                                    return True

                                if self.inbound is not None:
                                    return True

                                if self.outbound is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl']['meta_info']


                        class MultiAcl(object):
                            """
                            Multi ACLs configured on the interface
                            
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

                            _prefix = 'ipv4-ma-oper'
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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:multi-acl'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl']['meta_info']


                        class HelperAddress(object):
                            """
                            Helper Addresses configured on the interface
                            
                            .. attribute:: address_array
                            
                            	Helper address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.address_array = YLeafList()
                                self.address_array.parent = self
                                self.address_array.name = 'address_array'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:helper-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address_array is not None:
                                    for child in self.address_array:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress']['meta_info']


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
                            	**type**\:   :py:class:`RpfModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.RpfModeEnum>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:rpf'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf']['meta_info']


                        class BgpPa(object):
                            """
                            BGP PA config on the interface
                            
                            .. attribute:: input
                            
                            	BGP PA input config
                            	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input>`
                            
                            .. attribute:: output
                            
                            	BGP PA output config
                            	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.input = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input()
                                self.input.parent = self
                                self.output = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output()
                                self.output.parent = self


                            class Input(object):
                                """
                                BGP PA input config
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\:  bool
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\:  bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:input'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                    return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input']['meta_info']


                            class Output(object):
                                """
                                BGP PA output config
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\:  bool
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\:  bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:output'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                    return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:bgp-pa'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa']['meta_info']


                        class PubUtime(object):
                            """
                            Address Publish Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:pub-utime'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime']['meta_info']


                        class IdbUtime(object):
                            """
                            IDB Create Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:idb-utime'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime']['meta_info']


                        class CapsUtime(object):
                            """
                            CAPS Add Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:caps-utime'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime']['meta_info']


                        class FwdEnUtime(object):
                            """
                            FWD ENABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:fwd-en-utime'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime']['meta_info']


                        class FwdDisUtime(object):
                            """
                            FWD DISABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:fwd-dis-utime'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime']['meta_info']


                        class MulticastGroup(object):
                            """
                            Multicast groups joined on the interface
                            
                            .. attribute:: group_address
                            
                            	Address of multicast group
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.group_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:multicast-group'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup']['meta_info']


                        class SecondaryAddress(object):
                            """
                            Secondary addresses on the interface
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length of address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_tag
                            
                            	Route Tag associated with this address (0 = no tag)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.prefix_length = None
                                self.route_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:secondary-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.route_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                                return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:detail'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acl is not None and self.acl._has_data():
                                return True

                            if self.bgp_pa is not None and self.bgp_pa._has_data():
                                return True

                            if self.caps_utime is not None and self.caps_utime._has_data():
                                return True

                            if self.direct_broadcast is not None:
                                return True

                            if self.flow_tag_dst is not None:
                                return True

                            if self.flow_tag_src is not None:
                                return True

                            if self.fwd_dis_utime is not None and self.fwd_dis_utime._has_data():
                                return True

                            if self.fwd_en_utime is not None and self.fwd_en_utime._has_data():
                                return True

                            if self.helper_address is not None and self.helper_address._has_data():
                                return True

                            if self.idb_utime is not None and self.idb_utime._has_data():
                                return True

                            if self.line_state is not None:
                                return True

                            if self.mask_reply is not None:
                                return True

                            if self.mlacp_active is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            if self.multi_acl is not None and self.multi_acl._has_data():
                                return True

                            if self.multicast_group is not None:
                                for child_ref in self.multicast_group:
                                    if child_ref._has_data():
                                        return True

                            if self.prefix_length is not None:
                                return True

                            if self.primary_address is not None:
                                return True

                            if self.proxy_arp_disabled is not None:
                                return True

                            if self.pub_utime is not None and self.pub_utime._has_data():
                                return True

                            if self.redirect is not None:
                                return True

                            if self.rg_id_exists is not None:
                                return True

                            if self.route_tag is not None:
                                return True

                            if self.rpf is not None and self.rpf._has_data():
                                return True

                            if self.secondary_address is not None:
                                for child_ref in self.secondary_address:
                                    if child_ref._has_data():
                                        return True

                            if self.unnumbered_interface_name is not None:
                                return True

                            if self.unreachable is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']


                    class Brief(object):
                        """
                        Brief IPv4 network operational data for an
                        interface
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:   :py:class:`Ipv4MaOperLineStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineStateEnum>`
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            self.parent = None
                            self.line_state = None
                            self.primary_address = None
                            self.vrf_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:brief'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.line_state is not None:
                                return True

                            if self.primary_address is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                            return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:vrf[Cisco-IOS-XR-ipv4-ma-oper:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.brief is not None and self.brief._has_data():
                            return True

                        if self.detail is not None and self.detail._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                        return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-ma-oper:vrfs'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                    return meta._meta_table['Ipv4Network.Interfaces.Interface.Vrfs']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-ma-oper:interfaces/Cisco-IOS-XR-ipv4-ma-oper:interface[Cisco-IOS-XR-ipv4-ma-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
                return meta._meta_table['Ipv4Network.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-ma-oper:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
            return meta._meta_table['Ipv4Network.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-io-oper:ipv4-network'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_io_oper as meta
        return meta._meta_table['Ipv4Network']['meta_info']


