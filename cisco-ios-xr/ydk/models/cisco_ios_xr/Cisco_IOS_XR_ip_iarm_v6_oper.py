""" Cisco_IOS_XR_ip_iarm_v6_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iarm\-v6 package operational data.

This module contains definitions
for the following management objects\:
  ipv6arm\: IPv6 Address Repository Manager (IPv6 ARM)
    operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6Arm(Entity):
    """
    IPv6 Address Repository Manager (IPv6 ARM)
    operational data
    
    .. attribute:: addresses
    
    	IPv6 ARM address database information
    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses>`
    
    .. attribute:: multicast_host_interface
    
    	Default multicast host interface
    	**type**\:  str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    .. attribute:: summary
    
    	IPv6 ARM summary information
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Summary>`
    
    .. attribute:: vrf_summaries
    
    	IPv6 ARM VRFs summary information
    	**type**\:   :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.VrfSummaries>`
    
    

    """

    _prefix = 'ip-iarm-v6-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv6Arm, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6arm"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iarm-v6-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"addresses" : ("addresses", Ipv6Arm.Addresses), "summary" : ("summary", Ipv6Arm.Summary), "vrf-summaries" : ("vrf_summaries", Ipv6Arm.VrfSummaries)}
        self._child_list_classes = {}

        self.multicast_host_interface = YLeaf(YType.str, "multicast-host-interface")

        self.addresses = Ipv6Arm.Addresses()
        self.addresses.parent = self
        self._children_name_map["addresses"] = "addresses"
        self._children_yang_names.add("addresses")

        self.summary = Ipv6Arm.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrf_summaries = Ipv6Arm.VrfSummaries()
        self.vrf_summaries.parent = self
        self._children_name_map["vrf_summaries"] = "vrf-summaries"
        self._children_yang_names.add("vrf-summaries")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm"

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Arm, ['multicast_host_interface'], name, value)


    class Addresses(Entity):
        """
        IPv6 ARM address database information
        
        .. attribute:: vrfs
        
        	IPv6 ARM address database information per VRF
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs>`
        
        

        """

        _prefix = 'ip-iarm-v6-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6Arm.Addresses, self).__init__()

            self.yang_name = "addresses"
            self.yang_parent_name = "ipv6arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"vrfs" : ("vrfs", Ipv6Arm.Addresses.Vrfs)}
            self._child_list_classes = {}

            self.vrfs = Ipv6Arm.Addresses.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")
            self._segment_path = lambda: "addresses"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/%s" % self._segment_path()


        class Vrfs(Entity):
            """
            IPv6 ARM address database information per VRF
            
            .. attribute:: vrf
            
            	IPv6 ARM address database information in a VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf>`
            
            

            """

            _prefix = 'ip-iarm-v6-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6Arm.Addresses.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "addresses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"vrf" : ("vrf", Ipv6Arm.Addresses.Vrfs.Vrf)}

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/addresses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Arm.Addresses.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                IPv6 ARM address database information in a VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                .. attribute:: interfaces
                
                	IPv6 ARM address database information by interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces>`
                
                .. attribute:: networks
                
                	IPv6 ARM address database information by network
                	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Networks>`
                
                

                """

                _prefix = 'ip-iarm-v6-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6Arm.Addresses.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"interfaces" : ("interfaces", Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces), "networks" : ("networks", Ipv6Arm.Addresses.Vrfs.Vrf.Networks)}
                    self._child_list_classes = {}

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.interfaces = Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.networks = Ipv6Arm.Addresses.Vrfs.Vrf.Networks()
                    self.networks.parent = self
                    self._children_name_map["networks"] = "networks"
                    self._children_yang_names.add("networks")
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/addresses/vrfs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf, ['vrf_name'], name, value)


                class Interfaces(Entity):
                    """
                    IPv6 ARM address database information by
                    interface
                    
                    .. attribute:: interface
                    
                    	An IPv6 address in IPv6 ARM
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v6-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        An IPv6 address in IPv6 ARM
                        
                        .. attribute:: interface  <key>
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: address
                        
                        	Address info
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address>`
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v6-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"address" : ("address", Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address)}

                            self.interface = YLeaf(YType.str, "interface")

                            self.referenced_interface = YLeaf(YType.str, "referenced-interface")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address = YList(self)
                            self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, ['interface', 'referenced_interface', 'vrf_name'], name, value)


                        class Address(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address>`
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\:  str
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-iarm-v6-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"address" : ("address", Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address)}
                                self._child_list_classes = {}

                                self.is_prefix_sid = YLeaf(YType.boolean, "is-prefix-sid")

                                self.is_primary = YLeaf(YType.boolean, "is-primary")

                                self.is_tentative = YLeaf(YType.boolean, "is-tentative")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.producer = YLeaf(YType.str, "producer")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")

                                self.address = Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, ['is_prefix_sid', 'is_primary', 'is_tentative', 'prefix_length', 'producer', 'route_tag'], name, value)


                            class Address(Entity):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v6-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.afi = YLeaf(YType.int32, "afi")

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address, ['afi', 'ipv4_address', 'ipv6_address'], name, value)


                class Networks(Entity):
                    """
                    IPv6 ARM address database information by
                    network
                    
                    .. attribute:: network
                    
                    	An IPv6 Address in IPv6 ARM
                    	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v6-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv6Arm.Addresses.Vrfs.Vrf.Networks, self).__init__()

                        self.yang_name = "networks"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"network" : ("network", Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network)}

                        self.network = YList(self)
                        self._segment_path = lambda: "networks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Networks, [], name, value)


                    class Network(Entity):
                        """
                        An IPv6 Address in IPv6 ARM
                        
                        .. attribute:: address
                        
                        	Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_xr
                        
                        	Address info
                        	**type**\:   :py:class:`AddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr>`
                        
                        .. attribute:: handle
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v6-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network, self).__init__()

                            self.yang_name = "network"
                            self.yang_parent_name = "networks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-xr" : ("address_xr", Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr)}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.handle = YLeaf(YType.str, "handle")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.referenced_interface = YLeaf(YType.str, "referenced-interface")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address_xr = Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr()
                            self.address_xr.parent = self
                            self._children_name_map["address_xr"] = "address-xr"
                            self._children_yang_names.add("address-xr")
                            self._segment_path = lambda: "network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network, ['address', 'handle', 'interface_name', 'prefix_length', 'referenced_interface', 'vrf_name'], name, value)


                        class AddressXr(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address>`
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\:  str
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-iarm-v6-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, self).__init__()

                                self.yang_name = "address-xr"
                                self.yang_parent_name = "network"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"address" : ("address", Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address)}
                                self._child_list_classes = {}

                                self.is_prefix_sid = YLeaf(YType.boolean, "is-prefix-sid")

                                self.is_primary = YLeaf(YType.boolean, "is-primary")

                                self.is_tentative = YLeaf(YType.boolean, "is-tentative")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.producer = YLeaf(YType.str, "producer")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")

                                self.address = Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")
                                self._segment_path = lambda: "address-xr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, ['is_prefix_sid', 'is_primary', 'is_tentative', 'prefix_length', 'producer', 'route_tag'], name, value)


                            class Address(Entity):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v6-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.afi = YLeaf(YType.int32, "afi")

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                    self._segment_path = lambda: "address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, ['afi', 'ipv4_address', 'ipv6_address'], name, value)


    class Summary(Entity):
        """
        IPv6 ARM summary information
        
        .. attribute:: address_conflict_count
        
        	Number of address conflicts
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: db_master_version
        
        	IP\-ARM DB master version
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: producer_count
        
        	Number of producers
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: unnumbered_conflict_count
        
        	Number of unnumbered interface conflicts
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: vrf_count
        
        	Number of known VRFs
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'ip-iarm-v6-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6Arm.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "ipv6arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.address_conflict_count = YLeaf(YType.int32, "address-conflict-count")

            self.db_master_version = YLeaf(YType.uint32, "db-master-version")

            self.producer_count = YLeaf(YType.int32, "producer-count")

            self.unnumbered_conflict_count = YLeaf(YType.int32, "unnumbered-conflict-count")

            self.vrf_count = YLeaf(YType.int32, "vrf-count")
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Arm.Summary, ['address_conflict_count', 'db_master_version', 'producer_count', 'unnumbered_conflict_count', 'vrf_count'], name, value)


    class VrfSummaries(Entity):
        """
        IPv6 ARM VRFs summary information
        
        .. attribute:: vrf_summary
        
        	IPv6 ARM VRF summary information
        	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper.Ipv6Arm.VrfSummaries.VrfSummary>`
        
        

        """

        _prefix = 'ip-iarm-v6-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6Arm.VrfSummaries, self).__init__()

            self.yang_name = "vrf-summaries"
            self.yang_parent_name = "ipv6arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf-summary" : ("vrf_summary", Ipv6Arm.VrfSummaries.VrfSummary)}

            self.vrf_summary = YList(self)
            self._segment_path = lambda: "vrf-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Arm.VrfSummaries, [], name, value)


        class VrfSummary(Entity):
            """
            IPv6 ARM VRF summary information
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: vrf_id
            
            	VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'ip-iarm-v6-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6Arm.VrfSummaries.VrfSummary, self).__init__()

                self.yang_name = "vrf-summary"
                self.yang_parent_name = "vrf-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")
                self._segment_path = lambda: "vrf-summary" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v6-oper:ipv6arm/vrf-summaries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Arm.VrfSummaries.VrfSummary, ['vrf_name', 'vrf_id', 'vrf_name_xr'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Arm()
        return self._top_entity

