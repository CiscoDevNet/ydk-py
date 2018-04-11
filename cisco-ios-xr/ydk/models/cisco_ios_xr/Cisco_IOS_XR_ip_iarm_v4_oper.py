""" Cisco_IOS_XR_ip_iarm_v4_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iarm\-v4 package operational data.

This module contains definitions
for the following management objects\:
  ipv4arm\: IPv4 Address Repository Manager (IPv4 ARM)
    operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4Arm(Entity):
    """
    IPv4 Address Repository Manager (IPv4 ARM)
    operational data
    
    .. attribute:: addresses
    
    	IPv4 ARM address database information
    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses>`
    
    .. attribute:: summary
    
    	IPv4 ARM summary information
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Summary>`
    
    .. attribute:: vrf_summaries
    
    	IPv4 ARM VRFs summary information
    	**type**\:  :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries>`
    
    .. attribute:: router_id
    
    	IPv4 ARM Router ID information
    	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.RouterId>`
    
    .. attribute:: multicast_host_interface
    
    	Default multicast host interface
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    

    """

    _prefix = 'ip-iarm-v4-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv4Arm, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4arm"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iarm-v4-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("addresses", ("addresses", Ipv4Arm.Addresses)), ("summary", ("summary", Ipv4Arm.Summary)), ("vrf-summaries", ("vrf_summaries", Ipv4Arm.VrfSummaries)), ("router-id", ("router_id", Ipv4Arm.RouterId))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('multicast_host_interface', YLeaf(YType.str, 'multicast-host-interface')),
        ])
        self.multicast_host_interface = None

        self.addresses = Ipv4Arm.Addresses()
        self.addresses.parent = self
        self._children_name_map["addresses"] = "addresses"
        self._children_yang_names.add("addresses")

        self.summary = Ipv4Arm.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrf_summaries = Ipv4Arm.VrfSummaries()
        self.vrf_summaries.parent = self
        self._children_name_map["vrf_summaries"] = "vrf-summaries"
        self._children_yang_names.add("vrf-summaries")

        self.router_id = Ipv4Arm.RouterId()
        self.router_id.parent = self
        self._children_name_map["router_id"] = "router-id"
        self._children_yang_names.add("router-id")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm"

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Arm, ['multicast_host_interface'], name, value)


    class Addresses(Entity):
        """
        IPv4 ARM address database information
        
        .. attribute:: vrfs
        
        	IPv4 ARM address database information per VRF
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Arm.Addresses, self).__init__()

            self.yang_name = "addresses"
            self.yang_parent_name = "ipv4arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("vrfs", ("vrfs", Ipv4Arm.Addresses.Vrfs))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.vrfs = Ipv4Arm.Addresses.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")
            self._segment_path = lambda: "addresses"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self._segment_path()


        class Vrfs(Entity):
            """
            IPv4 ARM address database information per VRF
            
            .. attribute:: vrf
            
            	IPv4 ARM address database information in a VRF
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf>`
            
            

            """

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4Arm.Addresses.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "addresses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("vrf", ("vrf", Ipv4Arm.Addresses.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/addresses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Arm.Addresses.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                IPv4 ARM address database information in a VRF
                
                .. attribute:: vrf_name  (key)
                
                	VRF name
                	**type**\: str
                
                .. attribute:: networks
                
                	IPv4 ARM address database information by network
                	**type**\:  :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks>`
                
                .. attribute:: interfaces
                
                	IPv4 ARM address database information by interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces>`
                
                

                """

                _prefix = 'ip-iarm-v4-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Arm.Addresses.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_container_classes = OrderedDict([("networks", ("networks", Ipv4Arm.Addresses.Vrfs.Vrf.Networks)), ("interfaces", ("interfaces", Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ])
                    self.vrf_name = None

                    self.networks = Ipv4Arm.Addresses.Vrfs.Vrf.Networks()
                    self.networks.parent = self
                    self._children_name_map["networks"] = "networks"
                    self._children_yang_names.add("networks")

                    self.interfaces = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/addresses/vrfs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf, ['vrf_name'], name, value)


                class Networks(Entity):
                    """
                    IPv4 ARM address database information by
                    network
                    
                    .. attribute:: network
                    
                    	An IPv4 Address in IPv4 ARM
                    	**type**\: list of  		 :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks, self).__init__()

                        self.yang_name = "networks"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("network", ("network", Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network))])
                        self._leafs = OrderedDict()

                        self.network = YList(self)
                        self._segment_path = lambda: "networks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Networks, [], name, value)


                    class Network(Entity):
                        """
                        An IPv4 Address in IPv4 ARM
                        
                        .. attribute:: address
                        
                        	Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        .. attribute:: handle
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: address_xr
                        
                        	Address info
                        	**type**\:  :py:class:`AddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr>`
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: str
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\: str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network, self).__init__()

                            self.yang_name = "network"
                            self.yang_parent_name = "networks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("address-xr", ("address_xr", Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', YLeaf(YType.str, 'address')),
                                ('prefix_length', YLeaf(YType.uint32, 'prefix-length')),
                                ('handle', YLeaf(YType.str, 'handle')),
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('referenced_interface', YLeaf(YType.str, 'referenced-interface')),
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.address = None
                            self.prefix_length = None
                            self.handle = None
                            self.interface_name = None
                            self.referenced_interface = None
                            self.vrf_name = None

                            self.address_xr = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr()
                            self.address_xr.parent = self
                            self._children_name_map["address_xr"] = "address-xr"
                            self._children_yang_names.add("address-xr")
                            self._segment_path = lambda: "network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network, ['address', 'prefix_length', 'handle', 'interface_name', 'referenced_interface', 'vrf_name'], name, value)


                        class AddressXr(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address>`
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\: bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\: bool
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\: bool
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, self).__init__()

                                self.yang_name = "address-xr"
                                self.yang_parent_name = "network"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("address", ("address", Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix_length', YLeaf(YType.uint32, 'prefix-length')),
                                    ('route_tag', YLeaf(YType.uint32, 'route-tag')),
                                    ('is_primary', YLeaf(YType.boolean, 'is-primary')),
                                    ('is_tentative', YLeaf(YType.boolean, 'is-tentative')),
                                    ('is_prefix_sid', YLeaf(YType.boolean, 'is-prefix-sid')),
                                    ('producer', YLeaf(YType.str, 'producer')),
                                ])
                                self.prefix_length = None
                                self.route_tag = None
                                self.is_primary = None
                                self.is_tentative = None
                                self.is_prefix_sid = None
                                self.producer = None

                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")
                                self._segment_path = lambda: "address-xr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, ['prefix_length', 'route_tag', 'is_primary', 'is_tentative', 'is_prefix_sid', 'producer'], name, value)


                            class Address(Entity):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('afi', YLeaf(YType.int32, 'afi')),
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                    ])
                                    self.afi = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, ['afi', 'ipv4_address', 'ipv6_address'], name, value)


                class Interfaces(Entity):
                    """
                    IPv4 ARM address database information by
                    interface
                    
                    .. attribute:: interface
                    
                    	An IPv4 address in IPv4 ARM
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface", ("interface", Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        An IPv4 address in IPv4 ARM
                        
                        .. attribute:: interface  (key)
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\: str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\: str
                        
                        .. attribute:: address
                        
                        	Address info
                        	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address>`
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("address", ("address", Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address))])
                            self._leafs = OrderedDict([
                                ('interface', YLeaf(YType.str, 'interface')),
                                ('referenced_interface', YLeaf(YType.str, 'referenced-interface')),
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.interface = None
                            self.referenced_interface = None
                            self.vrf_name = None

                            self.address = YList(self)
                            self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, ['interface', 'referenced_interface', 'vrf_name'], name, value)


                        class Address(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:  :py:class:`Address_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_>`
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\: bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\: bool
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\: bool
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("address", ("address", Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix_length', YLeaf(YType.uint32, 'prefix-length')),
                                    ('route_tag', YLeaf(YType.uint32, 'route-tag')),
                                    ('is_primary', YLeaf(YType.boolean, 'is-primary')),
                                    ('is_tentative', YLeaf(YType.boolean, 'is-tentative')),
                                    ('is_prefix_sid', YLeaf(YType.boolean, 'is-prefix-sid')),
                                    ('producer', YLeaf(YType.str, 'producer')),
                                ])
                                self.prefix_length = None
                                self.route_tag = None
                                self.is_primary = None
                                self.is_tentative = None
                                self.is_prefix_sid = None
                                self.producer = None

                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")
                                self._segment_path = lambda: "address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, ['prefix_length', 'route_tag', 'is_primary', 'is_tentative', 'is_prefix_sid', 'producer'], name, value)


                            class Address_(Entity):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('afi', YLeaf(YType.int32, 'afi')),
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                    ])
                                    self.afi = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_, ['afi', 'ipv4_address', 'ipv6_address'], name, value)


    class Summary(Entity):
        """
        IPv4 ARM summary information
        
        .. attribute:: producer_count
        
        	Number of producers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: address_conflict_count
        
        	Number of address conflicts
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: unnumbered_conflict_count
        
        	Number of unnumbered interface conflicts
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: db_master_version
        
        	IP\-ARM DB master version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_count
        
        	Number of known VRFs
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Arm.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "ipv4arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('producer_count', YLeaf(YType.int32, 'producer-count')),
                ('address_conflict_count', YLeaf(YType.int32, 'address-conflict-count')),
                ('unnumbered_conflict_count', YLeaf(YType.int32, 'unnumbered-conflict-count')),
                ('db_master_version', YLeaf(YType.uint32, 'db-master-version')),
                ('vrf_count', YLeaf(YType.int32, 'vrf-count')),
            ])
            self.producer_count = None
            self.address_conflict_count = None
            self.unnumbered_conflict_count = None
            self.db_master_version = None
            self.vrf_count = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Arm.Summary, ['producer_count', 'address_conflict_count', 'unnumbered_conflict_count', 'db_master_version', 'vrf_count'], name, value)


    class VrfSummaries(Entity):
        """
        IPv4 ARM VRFs summary information
        
        .. attribute:: vrf_summary
        
        	IPv4 ARM VRF summary information
        	**type**\: list of  		 :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries.VrfSummary>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Arm.VrfSummaries, self).__init__()

            self.yang_name = "vrf-summaries"
            self.yang_parent_name = "ipv4arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vrf-summary", ("vrf_summary", Ipv4Arm.VrfSummaries.VrfSummary))])
            self._leafs = OrderedDict()

            self.vrf_summary = YList(self)
            self._segment_path = lambda: "vrf-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Arm.VrfSummaries, [], name, value)


        class VrfSummary(Entity):
            """
            IPv4 ARM VRF summary information
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            .. attribute:: vrf_id
            
            	VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\: str
            
            

            """

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4Arm.VrfSummaries.VrfSummary, self).__init__()

                self.yang_name = "vrf-summary"
                self.yang_parent_name = "vrf-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                    ('vrf_name_xr', YLeaf(YType.str, 'vrf-name-xr')),
                ])
                self.vrf_name = None
                self.vrf_id = None
                self.vrf_name_xr = None
                self._segment_path = lambda: "vrf-summary" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/vrf-summaries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Arm.VrfSummaries.VrfSummary, ['vrf_name', 'vrf_id', 'vrf_name_xr'], name, value)


    class RouterId(Entity):
        """
        IPv4 ARM Router ID information
        
        .. attribute:: vrf_id
        
        	VRF ID
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\: str
        
        .. attribute:: interface_name
        
        	Interface name
        	**type**\: str
        
        .. attribute:: router_id
        
        	Router ID
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Arm.RouterId, self).__init__()

            self.yang_name = "router-id"
            self.yang_parent_name = "ipv4arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('interface_name', YLeaf(YType.str, 'interface-name')),
                ('router_id', YLeaf(YType.str, 'router-id')),
            ])
            self.vrf_id = None
            self.vrf_name = None
            self.interface_name = None
            self.router_id = None
            self._segment_path = lambda: "router-id"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Arm.RouterId, ['vrf_id', 'vrf_name', 'interface_name', 'router_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Arm()
        return self._top_entity

