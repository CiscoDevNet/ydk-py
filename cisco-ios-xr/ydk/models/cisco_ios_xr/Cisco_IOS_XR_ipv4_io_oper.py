""" Cisco_IOS_XR_ipv4_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-network\: IPv4 network operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv4MaOperLineState(Enum):
    """
    Ipv4MaOperLineState

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

    unknown = Enum.YLeaf(0, "unknown")

    shutdown = Enum.YLeaf(1, "shutdown")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")


class RpfMode(Enum):
    """
    RpfMode

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")



class Ipv4Network(Entity):
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
        super(Ipv4Network, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-network"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-io-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"interfaces" : ("interfaces", Ipv4Network.Interfaces), "nodes" : ("nodes", Ipv4Network.Nodes)}
        self._child_list_classes = {}

        self.interfaces = Ipv4Network.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.nodes = Ipv4Network.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network"


    class Interfaces(Entity):
        """
        IPv4 network operational interface data
        
        .. attribute:: interface
        
        	Interface names with VRF
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-ma-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv4Network.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-network"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Ipv4Network.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-oper:interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Network.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface names with VRF
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: vrfs
            
            	List of VRF on the interface
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs>`
            
            

            """

            _prefix = 'ipv4-ma-oper'
            _revision = '2015-10-20'

            def __init__(self):
                super(Ipv4Network.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"vrfs" : ("vrfs", Ipv4Network.Interfaces.Interface.Vrfs)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.vrfs = Ipv4Network.Interfaces.Interface.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-ma-oper:interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Network.Interfaces.Interface, ['interface_name'], name, value)


            class Vrfs(Entity):
                """
                List of VRF on the interface
                
                .. attribute:: vrf
                
                	VRF information on the interface
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ipv4-ma-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Interfaces.Interface.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"vrf" : ("vrf", Ipv4Network.Interfaces.Interface.Vrfs.Vrf)}

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs, [], name, value)


                class Vrf(Entity):
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
                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"brief" : ("brief", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief), "detail" : ("detail", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail)}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.brief = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                        self._children_yang_names.add("brief")

                        self.detail = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, ['vrf_name'], name, value)


                    class Brief(Entity):
                        """
                        Brief IPv4 network operational data for an
                        interface
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF name of the interface
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.line_state = YLeaf(YType.enumeration, "line-state")

                            self.primary_address = YLeaf(YType.str, "primary-address")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "brief"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, ['line_state', 'primary_address', 'vrf_id', 'vrf_name'], name, value)


                    class Detail(Entity):
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
                        	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
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
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"acl" : ("acl", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl), "bgp-pa" : ("bgp_pa", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa), "caps-utime" : ("caps_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime), "fwd-dis-utime" : ("fwd_dis_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime), "fwd-en-utime" : ("fwd_en_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime), "helper-address" : ("helper_address", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress), "idb-utime" : ("idb_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime), "multi-acl" : ("multi_acl", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl), "pub-utime" : ("pub_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime), "rpf" : ("rpf", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf)}
                            self._child_list_classes = {"multicast-group" : ("multicast_group", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup), "secondary-address" : ("secondary_address", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress)}

                            self.direct_broadcast = YLeaf(YType.boolean, "direct-broadcast")

                            self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                            self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                            self.line_state = YLeaf(YType.enumeration, "line-state")

                            self.mask_reply = YLeaf(YType.boolean, "mask-reply")

                            self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                            self.mtu = YLeaf(YType.uint32, "mtu")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.primary_address = YLeaf(YType.str, "primary-address")

                            self.proxy_arp_disabled = YLeaf(YType.boolean, "proxy-arp-disabled")

                            self.redirect = YLeaf(YType.boolean, "redirect")

                            self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                            self.route_tag = YLeaf(YType.uint32, "route-tag")

                            self.unnumbered_interface_name = YLeaf(YType.str, "unnumbered-interface-name")

                            self.unreachable = YLeaf(YType.boolean, "unreachable")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl()
                            self.acl.parent = self
                            self._children_name_map["acl"] = "acl"
                            self._children_yang_names.add("acl")

                            self.bgp_pa = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa()
                            self.bgp_pa.parent = self
                            self._children_name_map["bgp_pa"] = "bgp-pa"
                            self._children_yang_names.add("bgp-pa")

                            self.caps_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime()
                            self.caps_utime.parent = self
                            self._children_name_map["caps_utime"] = "caps-utime"
                            self._children_yang_names.add("caps-utime")

                            self.fwd_dis_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime()
                            self.fwd_dis_utime.parent = self
                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                            self._children_yang_names.add("fwd-dis-utime")

                            self.fwd_en_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime()
                            self.fwd_en_utime.parent = self
                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                            self._children_yang_names.add("fwd-en-utime")

                            self.helper_address = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress()
                            self.helper_address.parent = self
                            self._children_name_map["helper_address"] = "helper-address"
                            self._children_yang_names.add("helper-address")

                            self.idb_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime()
                            self.idb_utime.parent = self
                            self._children_name_map["idb_utime"] = "idb-utime"
                            self._children_yang_names.add("idb-utime")

                            self.multi_acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl()
                            self.multi_acl.parent = self
                            self._children_name_map["multi_acl"] = "multi-acl"
                            self._children_yang_names.add("multi-acl")

                            self.pub_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime()
                            self.pub_utime.parent = self
                            self._children_name_map["pub_utime"] = "pub-utime"
                            self._children_yang_names.add("pub-utime")

                            self.rpf = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf()
                            self.rpf.parent = self
                            self._children_name_map["rpf"] = "rpf"
                            self._children_yang_names.add("rpf")

                            self.multicast_group = YList(self)
                            self.secondary_address = YList(self)
                            self._segment_path = lambda: "detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, ['direct_broadcast', 'flow_tag_dst', 'flow_tag_src', 'line_state', 'mask_reply', 'mlacp_active', 'mtu', 'prefix_length', 'primary_address', 'proxy_arp_disabled', 'redirect', 'rg_id_exists', 'route_tag', 'unnumbered_interface_name', 'unreachable', 'vrf_id'], name, value)


                        class Acl(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, self).__init__()

                                self.yang_name = "acl"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                self.inbound = YLeaf(YType.str, "inbound")

                                self.outbound = YLeaf(YType.str, "outbound")
                                self._segment_path = lambda: "acl"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, ['common_in_bound', 'common_out_bound', 'inbound', 'outbound'], name, value)


                        class BgpPa(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa, self).__init__()

                                self.yang_name = "bgp-pa"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"input" : ("input", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input), "output" : ("output", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output)}
                                self._child_list_classes = {}

                                self.input = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                                self._children_yang_names.add("input")

                                self.output = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                                self._children_yang_names.add("output")
                                self._segment_path = lambda: "bgp-pa"


                            class Input(Entity):
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
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, self).__init__()

                                    self.yang_name = "input"
                                    self.yang_parent_name = "bgp-pa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.destination = YLeaf(YType.boolean, "destination")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.source = YLeaf(YType.boolean, "source")
                                    self._segment_path = lambda: "input"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, ['destination', 'enable', 'source'], name, value)


                            class Output(Entity):
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
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, self).__init__()

                                    self.yang_name = "output"
                                    self.yang_parent_name = "bgp-pa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.destination = YLeaf(YType.boolean, "destination")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.source = YLeaf(YType.boolean, "source")
                                    self._segment_path = lambda: "output"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, ['destination', 'enable', 'source'], name, value)


                        class CapsUtime(Entity):
                            """
                            CAPS Add Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime, self).__init__()

                                self.yang_name = "caps-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "caps-utime"


                        class FwdDisUtime(Entity):
                            """
                            FWD DISABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime, self).__init__()

                                self.yang_name = "fwd-dis-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "fwd-dis-utime"


                        class FwdEnUtime(Entity):
                            """
                            FWD ENABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime, self).__init__()

                                self.yang_name = "fwd-en-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "fwd-en-utime"


                        class HelperAddress(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, self).__init__()

                                self.yang_name = "helper-address"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.address_array = YLeafList(YType.str, "address-array")
                                self._segment_path = lambda: "helper-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, ['address_array'], name, value)


                        class IdbUtime(Entity):
                            """
                            IDB Create Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime, self).__init__()

                                self.yang_name = "idb-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "idb-utime"


                        class MultiAcl(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, self).__init__()

                                self.yang_name = "multi-acl"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.common = YLeafList(YType.str, "common")

                                self.inbound = YLeafList(YType.str, "inbound")

                                self.outbound = YLeafList(YType.str, "outbound")
                                self._segment_path = lambda: "multi-acl"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, ['common', 'inbound', 'outbound'], name, value)


                        class MulticastGroup(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, self).__init__()

                                self.yang_name = "multicast-group"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")
                                self._segment_path = lambda: "multicast-group"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, ['group_address'], name, value)


                        class PubUtime(Entity):
                            """
                            Address Publish Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime, self).__init__()

                                self.yang_name = "pub-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "pub-utime"


                        class Rpf(Entity):
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
                            	**type**\:   :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.RpfMode>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, self).__init__()

                                self.yang_name = "rpf"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                self.enable = YLeaf(YType.boolean, "enable")

                                self.mode = YLeaf(YType.enumeration, "mode")
                                self._segment_path = lambda: "rpf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, ['allow_default_route', 'allow_self_ping', 'enable', 'mode'], name, value)


                        class SecondaryAddress(Entity):
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
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, self).__init__()

                                self.yang_name = "secondary-address"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.address = YLeaf(YType.str, "address")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")
                                self._segment_path = lambda: "secondary-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, ['address', 'prefix_length', 'route_tag'], name, value)


    class Nodes(Entity):
        """
        Node\-specific IPv4 network operational data
        
        .. attribute:: node
        
        	IPv4 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-io-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv4Network.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv4-network"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Ipv4Network.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Network.Nodes, [], name, value)


        class Node(Entity):
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
                super(Ipv4Network.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-data" : ("interface_data", Ipv4Network.Nodes.Node.InterfaceData), "statistics" : ("statistics", Ipv4Network.Nodes.Node.Statistics)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_data = Ipv4Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self._children_name_map["interface_data"] = "interface-data"
                self._children_yang_names.add("interface-data")

                self.statistics = Ipv4Network.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Network.Nodes.Node, ['node_name'], name, value)


            class InterfaceData(Entity):
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
                    super(Ipv4Network.Nodes.Node.InterfaceData, self).__init__()

                    self.yang_name = "interface-data"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"summary" : ("summary", Ipv4Network.Nodes.Node.InterfaceData.Summary), "vrfs" : ("vrfs", Ipv4Network.Nodes.Node.InterfaceData.Vrfs)}
                    self._child_list_classes = {}

                    self.summary = Ipv4Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.vrfs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")
                    self._segment_path = lambda: "interface-data"


                class Summary(Entity):
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
                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"if-down-down" : ("if_down_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown), "if-shutdown-down" : ("if_shutdown_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown), "if-up-down" : ("if_up_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown), "if-up-up" : ("if_up_up", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp)}
                        self._child_list_classes = {}

                        self.if_up_down_basecaps_up = YLeaf(YType.uint32, "if-up-down-basecaps-up")

                        self.if_down_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self._children_name_map["if_down_down"] = "if-down-down"
                        self._children_yang_names.add("if-down-down")

                        self.if_shutdown_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                        self._children_yang_names.add("if-shutdown-down")

                        self.if_up_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self._children_name_map["if_up_down"] = "if-up-down"
                        self._children_yang_names.add("if-up-down")

                        self.if_up_up = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self
                        self._children_name_map["if_up_up"] = "if-up-up"
                        self._children_yang_names.add("if-up-up")
                        self._segment_path = lambda: "summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary, ['if_up_down_basecaps_up'], name, value)


                    class IfDownDown(Entity):
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
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__init__()

                            self.yang_name = "if-down-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")
                            self._segment_path = lambda: "if-down-down"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, ['ip_assigned', 'ip_unassigned', 'ip_unnumbered'], name, value)


                    class IfShutdownDown(Entity):
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
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__init__()

                            self.yang_name = "if-shutdown-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")
                            self._segment_path = lambda: "if-shutdown-down"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, ['ip_assigned', 'ip_unassigned', 'ip_unnumbered'], name, value)


                    class IfUpDown(Entity):
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
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__init__()

                            self.yang_name = "if-up-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")
                            self._segment_path = lambda: "if-up-down"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, ['ip_assigned', 'ip_unassigned', 'ip_unnumbered'], name, value)


                    class IfUpUp(Entity):
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
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__init__()

                            self.yang_name = "if-up-up"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")
                            self._segment_path = lambda: "if-up-up"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, ['ip_assigned', 'ip_unassigned', 'ip_unnumbered'], name, value)


                class Vrfs(Entity):
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
                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"vrf" : ("vrf", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf)}

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, [], name, value)


                    class Vrf(Entity):
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
                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"briefs" : ("briefs", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs), "details" : ("details", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details)}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.briefs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self._children_name_map["briefs"] = "briefs"
                            self._children_yang_names.add("briefs")

                            self.details = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._children_yang_names.add("details")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Briefs(Entity):
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
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__init__()

                                self.yang_name = "briefs"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"brief" : ("brief", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief)}

                                self.brief = YList(self)
                                self._segment_path = lambda: "briefs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, [], name, value)


                            class Brief(Entity):
                                """
                                Brief interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: vrf_name
                                
                                	VRF name of the interface
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__init__()

                                    self.yang_name = "brief"
                                    self.yang_parent_name = "briefs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.primary_address = YLeaf(YType.str, "primary-address")

                                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                                    self._segment_path = lambda: "brief" + "[interface-name='" + self.interface_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, ['interface_name', 'line_state', 'primary_address', 'vrf_id', 'vrf_name'], name, value)


                        class Details(Entity):
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
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"detail" : ("detail", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail)}

                                self.detail = YList(self)
                                self._segment_path = lambda: "details"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, [], name, value)


                            class Detail(Entity):
                                """
                                Detail interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
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
                                	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
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
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"acl" : ("acl", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl), "bgp-pa" : ("bgp_pa", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa), "caps-utime" : ("caps_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime), "fwd-dis-utime" : ("fwd_dis_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime), "fwd-en-utime" : ("fwd_en_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime), "helper-address" : ("helper_address", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress), "idb-utime" : ("idb_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime), "multi-acl" : ("multi_acl", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl), "pub-utime" : ("pub_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime), "rpf" : ("rpf", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf)}
                                    self._child_list_classes = {"multicast-group" : ("multicast_group", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup), "secondary-address" : ("secondary_address", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress)}

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.direct_broadcast = YLeaf(YType.boolean, "direct-broadcast")

                                    self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                                    self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.mask_reply = YLeaf(YType.boolean, "mask-reply")

                                    self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                                    self.mtu = YLeaf(YType.uint32, "mtu")

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.primary_address = YLeaf(YType.str, "primary-address")

                                    self.proxy_arp_disabled = YLeaf(YType.boolean, "proxy-arp-disabled")

                                    self.redirect = YLeaf(YType.boolean, "redirect")

                                    self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                                    self.route_tag = YLeaf(YType.uint32, "route-tag")

                                    self.unnumbered_interface_name = YLeaf(YType.str, "unnumbered-interface-name")

                                    self.unreachable = YLeaf(YType.boolean, "unreachable")

                                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                                    self.acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl()
                                    self.acl.parent = self
                                    self._children_name_map["acl"] = "acl"
                                    self._children_yang_names.add("acl")

                                    self.bgp_pa = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"
                                    self._children_yang_names.add("bgp-pa")

                                    self.caps_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"
                                    self._children_yang_names.add("caps-utime")

                                    self.fwd_dis_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                    self._children_yang_names.add("fwd-dis-utime")

                                    self.fwd_en_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                    self._children_yang_names.add("fwd-en-utime")

                                    self.helper_address = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress()
                                    self.helper_address.parent = self
                                    self._children_name_map["helper_address"] = "helper-address"
                                    self._children_yang_names.add("helper-address")

                                    self.idb_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"
                                    self._children_yang_names.add("idb-utime")

                                    self.multi_acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl()
                                    self.multi_acl.parent = self
                                    self._children_name_map["multi_acl"] = "multi-acl"
                                    self._children_yang_names.add("multi-acl")

                                    self.pub_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime()
                                    self.pub_utime.parent = self
                                    self._children_name_map["pub_utime"] = "pub-utime"
                                    self._children_yang_names.add("pub-utime")

                                    self.rpf = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"
                                    self._children_yang_names.add("rpf")

                                    self.multicast_group = YList(self)
                                    self.secondary_address = YList(self)
                                    self._segment_path = lambda: "detail" + "[interface-name='" + self.interface_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, ['interface_name', 'direct_broadcast', 'flow_tag_dst', 'flow_tag_src', 'line_state', 'mask_reply', 'mlacp_active', 'mtu', 'prefix_length', 'primary_address', 'proxy_arp_disabled', 'redirect', 'rg_id_exists', 'route_tag', 'unnumbered_interface_name', 'unreachable', 'vrf_id'], name, value)


                                class Acl(Entity):
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
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, self).__init__()

                                        self.yang_name = "acl"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                        self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                        self.inbound = YLeaf(YType.str, "inbound")

                                        self.outbound = YLeaf(YType.str, "outbound")
                                        self._segment_path = lambda: "acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, ['common_in_bound', 'common_out_bound', 'inbound', 'outbound'], name, value)


                                class BgpPa(Entity):
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
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"input" : ("input", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input), "output" : ("output", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output)}
                                        self._child_list_classes = {}

                                        self.input = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                        self._children_yang_names.add("input")

                                        self.output = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._children_yang_names.add("output")
                                        self._segment_path = lambda: "bgp-pa"


                                    class Input(Entity):
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
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.boolean, "enable")

                                            self.source = YLeaf(YType.boolean, "source")
                                            self._segment_path = lambda: "input"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, ['destination', 'enable', 'source'], name, value)


                                    class Output(Entity):
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
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.boolean, "enable")

                                            self.source = YLeaf(YType.boolean, "source")
                                            self._segment_path = lambda: "output"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, ['destination', 'enable', 'source'], name, value)


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "caps-utime"


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "fwd-dis-utime"


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "fwd-en-utime"


                                class HelperAddress(Entity):
                                    """
                                    Helper Addresses configured on the interface
                                    
                                    .. attribute:: address_array
                                    
                                    	Helper address
                                    	**type**\: list of    :py:class:`AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, self).__init__()

                                        self.yang_name = "helper-address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"address-array" : ("address_array", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray)}

                                        self.address_array = YList(self)
                                        self._segment_path = lambda: "helper-address"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, [], name, value)


                                    class AddressArray(Entity):
                                        """
                                        Helper address
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray, self).__init__()

                                            self.yang_name = "address-array"
                                            self.yang_parent_name = "helper-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.entry = YLeaf(YType.str, "entry")
                                            self._segment_path = lambda: "address-array"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray, ['entry'], name, value)


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "idb-utime"


                                class MultiAcl(Entity):
                                    """
                                    Multi ACLs configured on the interface
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of    :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common>`
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of    :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound>`
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of    :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, self).__init__()

                                        self.yang_name = "multi-acl"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"common" : ("common", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common), "inbound" : ("inbound", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound), "outbound" : ("outbound", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound)}

                                        self.common = YList(self)
                                        self.inbound = YList(self)
                                        self.outbound = YList(self)
                                        self._segment_path = lambda: "multi-acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, [], name, value)


                                    class Common(Entity):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common, self).__init__()

                                            self.yang_name = "common"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.entry = YLeaf(YType.str, "entry")
                                            self._segment_path = lambda: "common"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common, ['entry'], name, value)


                                    class Inbound(Entity):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound, self).__init__()

                                            self.yang_name = "inbound"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.entry = YLeaf(YType.str, "entry")
                                            self._segment_path = lambda: "inbound"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound, ['entry'], name, value)


                                    class Outbound(Entity):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound, self).__init__()

                                            self.yang_name = "outbound"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.entry = YLeaf(YType.str, "entry")
                                            self._segment_path = lambda: "outbound"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound, ['entry'], name, value)


                                class MulticastGroup(Entity):
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
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.group_address = YLeaf(YType.str, "group-address")
                                        self._segment_path = lambda: "multicast-group"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, ['group_address'], name, value)


                                class PubUtime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime, self).__init__()

                                        self.yang_name = "pub-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "pub-utime"


                                class Rpf(Entity):
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
                                    	**type**\:   :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.RpfMode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                        self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.mode = YLeaf(YType.enumeration, "mode")
                                        self._segment_path = lambda: "rpf"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, ['allow_default_route', 'allow_self_ping', 'enable', 'mode'], name, value)


                                class SecondaryAddress(Entity):
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
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, self).__init__()

                                        self.yang_name = "secondary-address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")
                                        self._segment_path = lambda: "secondary-address"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, ['address', 'prefix_length', 'route_tag'], name, value)


            class Statistics(Entity):
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
                    super(Ipv4Network.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"traffic" : ("traffic", Ipv4Network.Nodes.Node.Statistics.Traffic)}
                    self._child_list_classes = {}

                    self.traffic = Ipv4Network.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                    self._children_yang_names.add("traffic")
                    self._segment_path = lambda: "statistics"


                class Traffic(Entity):
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
                        super(Ipv4Network.Nodes.Node.Statistics.Traffic, self).__init__()

                        self.yang_name = "traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"icmp-stats" : ("icmp_stats", Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats), "ipv4-stats" : ("ipv4_stats", Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats)}
                        self._child_list_classes = {}

                        self.icmp_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats()
                        self.icmp_stats.parent = self
                        self._children_name_map["icmp_stats"] = "icmp-stats"
                        self._children_yang_names.add("icmp-stats")

                        self.ipv4_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats()
                        self.ipv4_stats.parent = self
                        self._children_name_map["ipv4_stats"] = "ipv4-stats"
                        self._children_yang_names.add("ipv4-stats")
                        self._segment_path = lambda: "traffic"


                    class IcmpStats(Entity):
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
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, self).__init__()

                            self.yang_name = "icmp-stats"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.admin_unreachable_received = YLeaf(YType.uint32, "admin-unreachable-received")

                            self.admin_unreachable_sent = YLeaf(YType.uint32, "admin-unreachable-sent")

                            self.checksum_error = YLeaf(YType.uint32, "checksum-error")

                            self.echo_reply_received = YLeaf(YType.uint32, "echo-reply-received")

                            self.echo_reply_sent = YLeaf(YType.uint32, "echo-reply-sent")

                            self.echo_request_received = YLeaf(YType.uint32, "echo-request-received")

                            self.echo_request_sent = YLeaf(YType.uint32, "echo-request-sent")

                            self.fragment_unreachable_received = YLeaf(YType.uint32, "fragment-unreachable-received")

                            self.fragment_unreachable_sent = YLeaf(YType.uint32, "fragment-unreachable-sent")

                            self.hopcount_received = YLeaf(YType.uint32, "hopcount-received")

                            self.hopcount_sent = YLeaf(YType.uint32, "hopcount-sent")

                            self.host_unreachable_received = YLeaf(YType.uint32, "host-unreachable-received")

                            self.host_unreachable_sent = YLeaf(YType.uint32, "host-unreachable-sent")

                            self.mask_reply_received = YLeaf(YType.uint32, "mask-reply-received")

                            self.mask_reply_sent = YLeaf(YType.uint32, "mask-reply-sent")

                            self.mask_request_received = YLeaf(YType.uint32, "mask-request-received")

                            self.mask_request_sent = YLeaf(YType.uint32, "mask-request-sent")

                            self.network_unreachable_received = YLeaf(YType.uint32, "network-unreachable-received")

                            self.network_unreachable_sent = YLeaf(YType.uint32, "network-unreachable-sent")

                            self.output = YLeaf(YType.uint32, "output")

                            self.param_error_received = YLeaf(YType.uint32, "param-error-received")

                            self.param_error_send = YLeaf(YType.uint32, "param-error-send")

                            self.port_unreachable_received = YLeaf(YType.uint32, "port-unreachable-received")

                            self.port_unreachable_sent = YLeaf(YType.uint32, "port-unreachable-sent")

                            self.protocol_unreachable_received = YLeaf(YType.uint32, "protocol-unreachable-received")

                            self.protocol_unreachable_sent = YLeaf(YType.uint32, "protocol-unreachable-sent")

                            self.reassebly_received = YLeaf(YType.uint32, "reassebly-received")

                            self.reassembly_sent = YLeaf(YType.uint32, "reassembly-sent")

                            self.received = YLeaf(YType.uint32, "received")

                            self.redirect_received = YLeaf(YType.uint32, "redirect-received")

                            self.redirect_send = YLeaf(YType.uint32, "redirect-send")

                            self.router_advert_received = YLeaf(YType.uint32, "router-advert-received")

                            self.router_solicit_received = YLeaf(YType.uint32, "router-solicit-received")

                            self.source_quench_received = YLeaf(YType.uint32, "source-quench-received")

                            self.timestamp_received = YLeaf(YType.uint32, "timestamp-received")

                            self.timestamp_reply_received = YLeaf(YType.uint32, "timestamp-reply-received")

                            self.unknown = YLeaf(YType.uint32, "unknown")
                            self._segment_path = lambda: "icmp-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, ['admin_unreachable_received', 'admin_unreachable_sent', 'checksum_error', 'echo_reply_received', 'echo_reply_sent', 'echo_request_received', 'echo_request_sent', 'fragment_unreachable_received', 'fragment_unreachable_sent', 'hopcount_received', 'hopcount_sent', 'host_unreachable_received', 'host_unreachable_sent', 'mask_reply_received', 'mask_reply_sent', 'mask_request_received', 'mask_request_sent', 'network_unreachable_received', 'network_unreachable_sent', 'output', 'param_error_received', 'param_error_send', 'port_unreachable_received', 'port_unreachable_sent', 'protocol_unreachable_received', 'protocol_unreachable_sent', 'reassebly_received', 'reassembly_sent', 'received', 'redirect_received', 'redirect_send', 'router_advert_received', 'router_solicit_received', 'source_quench_received', 'timestamp_received', 'timestamp_reply_received', 'unknown'], name, value)


                    class Ipv4Stats(Entity):
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
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, self).__init__()

                            self.yang_name = "ipv4-stats"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_header = YLeaf(YType.uint32, "bad-header")

                            self.bad_hop_count = YLeaf(YType.uint32, "bad-hop-count")

                            self.bad_option = YLeaf(YType.uint32, "bad-option")

                            self.bad_security_option = YLeaf(YType.uint32, "bad-security-option")

                            self.bad_source_address = YLeaf(YType.uint32, "bad-source-address")

                            self.basic_security_option = YLeaf(YType.uint32, "basic-security-option")

                            self.broadcast_in = YLeaf(YType.uint32, "broadcast-in")

                            self.broadcast_out = YLeaf(YType.uint32, "broadcast-out")

                            self.cipso_option = YLeaf(YType.uint32, "cipso-option")

                            self.encapsulation_failed = YLeaf(YType.uint32, "encapsulation-failed")

                            self.end_option = YLeaf(YType.uint32, "end-option")

                            self.extended_security_option = YLeaf(YType.uint32, "extended-security-option")

                            self.format_errors = YLeaf(YType.uint32, "format-errors")

                            self.fragment_count = YLeaf(YType.uint32, "fragment-count")

                            self.input_packets = YLeaf(YType.uint32, "input-packets")

                            self.lisp_decap_error = YLeaf(YType.uint32, "lisp-decap-error")

                            self.lisp_encap_error = YLeaf(YType.uint32, "lisp-encap-error")

                            self.lisp_v4_decap = YLeaf(YType.uint32, "lisp-v4-decap")

                            self.lisp_v4_encap = YLeaf(YType.uint32, "lisp-v4-encap")

                            self.lisp_v6_decap = YLeaf(YType.uint32, "lisp-v6-decap")

                            self.lisp_v6_encap = YLeaf(YType.uint32, "lisp-v6-encap")

                            self.loose_source_route_option = YLeaf(YType.uint32, "loose-source-route-option")

                            self.multicast_in = YLeaf(YType.uint32, "multicast-in")

                            self.multicast_out = YLeaf(YType.uint32, "multicast-out")

                            self.no_gateway = YLeaf(YType.uint32, "no-gateway")

                            self.no_protocol = YLeaf(YType.uint32, "no-protocol")

                            self.no_router = YLeaf(YType.uint32, "no-router")

                            self.noop_option = YLeaf(YType.uint32, "noop-option")

                            self.options_present = YLeaf(YType.uint32, "options-present")

                            self.packet_too_big = YLeaf(YType.uint32, "packet-too-big")

                            self.packets_forwarded = YLeaf(YType.uint32, "packets-forwarded")

                            self.packets_fragmented = YLeaf(YType.uint32, "packets-fragmented")

                            self.packets_output = YLeaf(YType.uint32, "packets-output")

                            self.reassemble_failed = YLeaf(YType.uint32, "reassemble-failed")

                            self.reassemble_input = YLeaf(YType.uint32, "reassemble-input")

                            self.reassemble_max_drop = YLeaf(YType.uint32, "reassemble-max-drop")

                            self.reassemble_timeout = YLeaf(YType.uint32, "reassemble-timeout")

                            self.reassembled = YLeaf(YType.uint32, "reassembled")

                            self.received_packets = YLeaf(YType.uint32, "received-packets")

                            self.record_route_option = YLeaf(YType.uint32, "record-route-option")

                            self.router_alert_option = YLeaf(YType.uint32, "router-alert-option")

                            self.sid_option = YLeaf(YType.uint32, "sid-option")

                            self.strict_source_route_option = YLeaf(YType.uint32, "strict-source-route-option")

                            self.timestamp_option = YLeaf(YType.uint32, "timestamp-option")

                            self.unknown_option = YLeaf(YType.uint32, "unknown-option")
                            self._segment_path = lambda: "ipv4-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, ['bad_header', 'bad_hop_count', 'bad_option', 'bad_security_option', 'bad_source_address', 'basic_security_option', 'broadcast_in', 'broadcast_out', 'cipso_option', 'encapsulation_failed', 'end_option', 'extended_security_option', 'format_errors', 'fragment_count', 'input_packets', 'lisp_decap_error', 'lisp_encap_error', 'lisp_v4_decap', 'lisp_v4_encap', 'lisp_v6_decap', 'lisp_v6_encap', 'loose_source_route_option', 'multicast_in', 'multicast_out', 'no_gateway', 'no_protocol', 'no_router', 'noop_option', 'options_present', 'packet_too_big', 'packets_forwarded', 'packets_fragmented', 'packets_output', 'reassemble_failed', 'reassemble_input', 'reassemble_max_drop', 'reassemble_timeout', 'reassembled', 'received_packets', 'record_route_option', 'router_alert_option', 'sid_option', 'strict_source_route_option', 'timestamp_option', 'unknown_option'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Network()
        return self._top_entity

