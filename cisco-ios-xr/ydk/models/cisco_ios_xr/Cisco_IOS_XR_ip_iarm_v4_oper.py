""" Cisco_IOS_XR_ip_iarm_v4_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iarm\-v4 package operational data.

This module contains definitions
for the following management objects\:
  ipv4arm\: IPv4 Address Repository Manager (IPv4 ARM)
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4Arm(Entity):
    """
    IPv4 Address Repository Manager (IPv4 ARM)
    operational data
    
    .. attribute:: addresses
    
    	IPv4 ARM address database information
    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses>`
    
    .. attribute:: multicast_host_interface
    
    	Default multicast host interface
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: router_id
    
    	IPv4 ARM Router ID information
    	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.RouterId>`
    
    .. attribute:: summary
    
    	IPv4 ARM summary information
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Summary>`
    
    .. attribute:: vrf_summaries
    
    	IPv4 ARM VRFs summary information
    	**type**\:   :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries>`
    
    

    """

    _prefix = 'ip-iarm-v4-oper'
    _revision = '2016-12-19'

    def __init__(self):
        super(Ipv4Arm, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4arm"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iarm-v4-oper"

        self.multicast_host_interface = YLeaf(YType.str, "multicast-host-interface")

        self.addresses = Ipv4Arm.Addresses()
        self.addresses.parent = self
        self._children_name_map["addresses"] = "addresses"
        self._children_yang_names.add("addresses")

        self.router_id = Ipv4Arm.RouterId()
        self.router_id.parent = self
        self._children_name_map["router_id"] = "router-id"
        self._children_yang_names.add("router-id")

        self.summary = Ipv4Arm.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrf_summaries = Ipv4Arm.VrfSummaries()
        self.vrf_summaries.parent = self
        self._children_name_map["vrf_summaries"] = "vrf-summaries"
        self._children_yang_names.add("vrf-summaries")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("multicast_host_interface") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv4Arm, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv4Arm, self).__setattr__(name, value)


    class Addresses(Entity):
        """
        IPv4 ARM address database information
        
        .. attribute:: vrfs
        
        	IPv4 ARM address database information per VRF
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(Ipv4Arm.Addresses, self).__init__()

            self.yang_name = "addresses"
            self.yang_parent_name = "ipv4arm"

            self.vrfs = Ipv4Arm.Addresses.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")


        class Vrfs(Entity):
            """
            IPv4 ARM address database information per VRF
            
            .. attribute:: vrf
            
            	IPv4 ARM address database information in a VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf>`
            
            

            """

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2016-12-19'

            def __init__(self):
                super(Ipv4Arm.Addresses.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "addresses"

                self.vrf = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Arm.Addresses.Vrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Arm.Addresses.Vrfs, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                IPv4 ARM address database information in a VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                .. attribute:: interfaces
                
                	IPv4 ARM address database information by interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces>`
                
                .. attribute:: networks
                
                	IPv4 ARM address database information by network
                	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks>`
                
                

                """

                _prefix = 'ip-iarm-v4-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Ipv4Arm.Addresses.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.interfaces = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.networks = Ipv4Arm.Addresses.Vrfs.Vrf.Networks()
                    self.networks.parent = self
                    self._children_name_map["networks"] = "networks"
                    self._children_yang_names.add("networks")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Arm.Addresses.Vrfs.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Arm.Addresses.Vrfs.Vrf, self).__setattr__(name, value)


                class Networks(Entity):
                    """
                    IPv4 ARM address database information by
                    network
                    
                    .. attribute:: network
                    
                    	An IPv4 Address in IPv4 ARM
                    	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks, self).__init__()

                        self.yang_name = "networks"
                        self.yang_parent_name = "vrf"

                        self.network = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks, self).__setattr__(name, value)


                    class Network(Entity):
                        """
                        An IPv4 Address in IPv4 ARM
                        
                        .. attribute:: address
                        
                        	Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_xr
                        
                        	Address info
                        	**type**\:   :py:class:`AddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr>`
                        
                        .. attribute:: handle
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2016-12-19'

                        def __init__(self):
                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network, self).__init__()

                            self.yang_name = "network"
                            self.yang_parent_name = "networks"

                            self.address = YLeaf(YType.str, "address")

                            self.handle = YLeaf(YType.str, "handle")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.referenced_interface = YLeaf(YType.str, "referenced-interface")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address_xr = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr()
                            self.address_xr.parent = self
                            self._children_name_map["address_xr"] = "address-xr"
                            self._children_yang_names.add("address-xr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address",
                                            "handle",
                                            "interface_name",
                                            "prefix_length",
                                            "referenced_interface",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network, self).__setattr__(name, value)


                        class AddressXr(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address>`
                            
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

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2016-12-19'

                            def __init__(self):
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, self).__init__()

                                self.yang_name = "address-xr"
                                self.yang_parent_name = "network"

                                self.is_prefix_sid = YLeaf(YType.boolean, "is-prefix-sid")

                                self.is_primary = YLeaf(YType.boolean, "is-primary")

                                self.is_tentative = YLeaf(YType.boolean, "is-tentative")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.producer = YLeaf(YType.str, "producer")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")

                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_prefix_sid",
                                                "is_primary",
                                                "is_tentative",
                                                "prefix_length",
                                                "producer",
                                                "route_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr, self).__setattr__(name, value)


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

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2016-12-19'

                                def __init__(self):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address-xr"

                                    self.afi = YLeaf(YType.int32, "afi")

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi",
                                                    "ipv4_address",
                                                    "ipv6_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.afi.is_set or
                                        self.ipv4_address.is_set or
                                        self.ipv6_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi.yfilter != YFilter.not_set or
                                        self.ipv4_address.yfilter != YFilter.not_set or
                                        self.ipv6_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.afi.get_name_leafdata())
                                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "afi" or name == "ipv4-address" or name == "ipv6-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi"):
                                        self.afi = value
                                        self.afi.value_namespace = name_space
                                        self.afi.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-address"):
                                        self.ipv4_address = value
                                        self.ipv4_address.value_namespace = name_space
                                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-address"):
                                        self.ipv6_address = value
                                        self.ipv6_address.value_namespace = name_space
                                        self.ipv6_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.is_prefix_sid.is_set or
                                    self.is_primary.is_set or
                                    self.is_tentative.is_set or
                                    self.prefix_length.is_set or
                                    self.producer.is_set or
                                    self.route_tag.is_set or
                                    (self.address is not None and self.address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_prefix_sid.yfilter != YFilter.not_set or
                                    self.is_primary.yfilter != YFilter.not_set or
                                    self.is_tentative.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.producer.yfilter != YFilter.not_set or
                                    self.route_tag.yfilter != YFilter.not_set or
                                    (self.address is not None and self.address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-xr" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_prefix_sid.is_set or self.is_prefix_sid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_prefix_sid.get_name_leafdata())
                                if (self.is_primary.is_set or self.is_primary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_primary.get_name_leafdata())
                                if (self.is_tentative.is_set or self.is_tentative.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_tentative.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.producer.is_set or self.producer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.producer.get_name_leafdata())
                                if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.route_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "address"):
                                    if (self.address is None):
                                        self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address()
                                        self.address.parent = self
                                        self._children_name_map["address"] = "address"
                                    return self.address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "is-prefix-sid" or name == "is-primary" or name == "is-tentative" or name == "prefix-length" or name == "producer" or name == "route-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-prefix-sid"):
                                    self.is_prefix_sid = value
                                    self.is_prefix_sid.value_namespace = name_space
                                    self.is_prefix_sid.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-primary"):
                                    self.is_primary = value
                                    self.is_primary.value_namespace = name_space
                                    self.is_primary.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-tentative"):
                                    self.is_tentative = value
                                    self.is_tentative.value_namespace = name_space
                                    self.is_tentative.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "producer"):
                                    self.producer = value
                                    self.producer.value_namespace = name_space
                                    self.producer.value_namespace_prefix = name_space_prefix
                                if(value_path == "route-tag"):
                                    self.route_tag = value
                                    self.route_tag.value_namespace = name_space
                                    self.route_tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.handle.is_set or
                                self.interface_name.is_set or
                                self.prefix_length.is_set or
                                self.referenced_interface.is_set or
                                self.vrf_name.is_set or
                                (self.address_xr is not None and self.address_xr.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.handle.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.referenced_interface.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                (self.address_xr is not None and self.address_xr.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "network" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.handle.is_set or self.handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.handle.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.referenced_interface.is_set or self.referenced_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.referenced_interface.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address-xr"):
                                if (self.address_xr is None):
                                    self.address_xr = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr()
                                    self.address_xr.parent = self
                                    self._children_name_map["address_xr"] = "address-xr"
                                return self.address_xr

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-xr" or name == "address" or name == "handle" or name == "interface-name" or name == "prefix-length" or name == "referenced-interface" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "handle"):
                                self.handle = value
                                self.handle.value_namespace = name_space
                                self.handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "referenced-interface"):
                                self.referenced_interface = value
                                self.referenced_interface.value_namespace = name_space
                                self.referenced_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.network:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.network:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "networks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "network"):
                            for c in self.network:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.network.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "network"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Interfaces(Entity):
                    """
                    IPv4 ARM address database information by
                    interface
                    
                    .. attribute:: interface
                    
                    	An IPv4 address in IPv4 ARM
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "vrf"

                        self.interface = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        An IPv4 address in IPv4 ARM
                        
                        .. attribute:: interface  <key>
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: address
                        
                        	Address info
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address>`
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2016-12-19'

                        def __init__(self):
                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"

                            self.interface = YLeaf(YType.str, "interface")

                            self.referenced_interface = YLeaf(YType.str, "referenced-interface")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface",
                                            "referenced_interface",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                        class Address(Entity):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address>`
                            
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

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2016-12-19'

                            def __init__(self):
                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "interface"

                                self.is_prefix_sid = YLeaf(YType.boolean, "is-prefix-sid")

                                self.is_primary = YLeaf(YType.boolean, "is-primary")

                                self.is_tentative = YLeaf(YType.boolean, "is-tentative")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.producer = YLeaf(YType.str, "producer")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")

                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_prefix_sid",
                                                "is_primary",
                                                "is_tentative",
                                                "prefix_length",
                                                "producer",
                                                "route_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address, self).__setattr__(name, value)


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

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2016-12-19'

                                def __init__(self):
                                    super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "address"

                                    self.afi = YLeaf(YType.int32, "afi")

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi",
                                                    "ipv4_address",
                                                    "ipv6_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.afi.is_set or
                                        self.ipv4_address.is_set or
                                        self.ipv6_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi.yfilter != YFilter.not_set or
                                        self.ipv4_address.yfilter != YFilter.not_set or
                                        self.ipv6_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.afi.get_name_leafdata())
                                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "afi" or name == "ipv4-address" or name == "ipv6-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi"):
                                        self.afi = value
                                        self.afi.value_namespace = name_space
                                        self.afi.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-address"):
                                        self.ipv4_address = value
                                        self.ipv4_address.value_namespace = name_space
                                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-address"):
                                        self.ipv6_address = value
                                        self.ipv6_address.value_namespace = name_space
                                        self.ipv6_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.is_prefix_sid.is_set or
                                    self.is_primary.is_set or
                                    self.is_tentative.is_set or
                                    self.prefix_length.is_set or
                                    self.producer.is_set or
                                    self.route_tag.is_set or
                                    (self.address is not None and self.address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_prefix_sid.yfilter != YFilter.not_set or
                                    self.is_primary.yfilter != YFilter.not_set or
                                    self.is_tentative.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.producer.yfilter != YFilter.not_set or
                                    self.route_tag.yfilter != YFilter.not_set or
                                    (self.address is not None and self.address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_prefix_sid.is_set or self.is_prefix_sid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_prefix_sid.get_name_leafdata())
                                if (self.is_primary.is_set or self.is_primary.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_primary.get_name_leafdata())
                                if (self.is_tentative.is_set or self.is_tentative.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_tentative.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.producer.is_set or self.producer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.producer.get_name_leafdata())
                                if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.route_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "address"):
                                    if (self.address is None):
                                        self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address()
                                        self.address.parent = self
                                        self._children_name_map["address"] = "address"
                                    return self.address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "is-prefix-sid" or name == "is-primary" or name == "is-tentative" or name == "prefix-length" or name == "producer" or name == "route-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-prefix-sid"):
                                    self.is_prefix_sid = value
                                    self.is_prefix_sid.value_namespace = name_space
                                    self.is_prefix_sid.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-primary"):
                                    self.is_primary = value
                                    self.is_primary.value_namespace = name_space
                                    self.is_primary.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-tentative"):
                                    self.is_tentative = value
                                    self.is_tentative.value_namespace = name_space
                                    self.is_tentative.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "producer"):
                                    self.producer = value
                                    self.producer.value_namespace = name_space
                                    self.producer.value_namespace_prefix = name_space_prefix
                                if(value_path == "route-tag"):
                                    self.route_tag = value
                                    self.route_tag.value_namespace = name_space
                                    self.route_tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address:
                                if (c.has_data()):
                                    return True
                            return (
                                self.interface.is_set or
                                self.referenced_interface.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            for c in self.address:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.referenced_interface.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.referenced_interface.is_set or self.referenced_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.referenced_interface.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address"):
                                for c in self.address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "interface" or name == "referenced-interface" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "referenced-interface"):
                                self.referenced_interface = value
                                self.referenced_interface.value_namespace = name_space
                                self.referenced_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.interface:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interfaces" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface"):
                            for c in self.interface:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        (self.interfaces is not None and self.interfaces.has_data()) or
                        (self.networks is not None and self.networks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        (self.interfaces is not None and self.interfaces.has_operation()) or
                        (self.networks is not None and self.networks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/addresses/vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    if (child_yang_name == "networks"):
                        if (self.networks is None):
                            self.networks = Ipv4Arm.Addresses.Vrfs.Vrf.Networks()
                            self.networks.parent = self
                            self._children_name_map["networks"] = "networks"
                        return self.networks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interfaces" or name == "networks" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/addresses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrf"):
                    for c in self.vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ipv4Arm.Addresses.Vrfs.Vrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.vrfs is not None and self.vrfs.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.vrfs is not None and self.vrfs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "addresses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrfs"):
                if (self.vrfs is None):
                    self.vrfs = Ipv4Arm.Addresses.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                return self.vrfs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrfs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Summary(Entity):
        """
        IPv4 ARM summary information
        
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

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(Ipv4Arm.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "ipv4arm"

            self.address_conflict_count = YLeaf(YType.int32, "address-conflict-count")

            self.db_master_version = YLeaf(YType.uint32, "db-master-version")

            self.producer_count = YLeaf(YType.int32, "producer-count")

            self.unnumbered_conflict_count = YLeaf(YType.int32, "unnumbered-conflict-count")

            self.vrf_count = YLeaf(YType.int32, "vrf-count")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address_conflict_count",
                            "db_master_version",
                            "producer_count",
                            "unnumbered_conflict_count",
                            "vrf_count") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Arm.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Arm.Summary, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address_conflict_count.is_set or
                self.db_master_version.is_set or
                self.producer_count.is_set or
                self.unnumbered_conflict_count.is_set or
                self.vrf_count.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address_conflict_count.yfilter != YFilter.not_set or
                self.db_master_version.yfilter != YFilter.not_set or
                self.producer_count.yfilter != YFilter.not_set or
                self.unnumbered_conflict_count.yfilter != YFilter.not_set or
                self.vrf_count.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address_conflict_count.is_set or self.address_conflict_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address_conflict_count.get_name_leafdata())
            if (self.db_master_version.is_set or self.db_master_version.yfilter != YFilter.not_set):
                leaf_name_data.append(self.db_master_version.get_name_leafdata())
            if (self.producer_count.is_set or self.producer_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.producer_count.get_name_leafdata())
            if (self.unnumbered_conflict_count.is_set or self.unnumbered_conflict_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.unnumbered_conflict_count.get_name_leafdata())
            if (self.vrf_count.is_set or self.vrf_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_count.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address-conflict-count" or name == "db-master-version" or name == "producer-count" or name == "unnumbered-conflict-count" or name == "vrf-count"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address-conflict-count"):
                self.address_conflict_count = value
                self.address_conflict_count.value_namespace = name_space
                self.address_conflict_count.value_namespace_prefix = name_space_prefix
            if(value_path == "db-master-version"):
                self.db_master_version = value
                self.db_master_version.value_namespace = name_space
                self.db_master_version.value_namespace_prefix = name_space_prefix
            if(value_path == "producer-count"):
                self.producer_count = value
                self.producer_count.value_namespace = name_space
                self.producer_count.value_namespace_prefix = name_space_prefix
            if(value_path == "unnumbered-conflict-count"):
                self.unnumbered_conflict_count = value
                self.unnumbered_conflict_count.value_namespace = name_space
                self.unnumbered_conflict_count.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf-count"):
                self.vrf_count = value
                self.vrf_count.value_namespace = name_space
                self.vrf_count.value_namespace_prefix = name_space_prefix


    class VrfSummaries(Entity):
        """
        IPv4 ARM VRFs summary information
        
        .. attribute:: vrf_summary
        
        	IPv4 ARM VRF summary information
        	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries.VrfSummary>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(Ipv4Arm.VrfSummaries, self).__init__()

            self.yang_name = "vrf-summaries"
            self.yang_parent_name = "ipv4arm"

            self.vrf_summary = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Arm.VrfSummaries, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Arm.VrfSummaries, self).__setattr__(name, value)


        class VrfSummary(Entity):
            """
            IPv4 ARM VRF summary information
            
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

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2016-12-19'

            def __init__(self):
                super(Ipv4Arm.VrfSummaries.VrfSummary, self).__init__()

                self.yang_name = "vrf-summary"
                self.yang_parent_name = "vrf-summaries"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "vrf_id",
                                "vrf_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Arm.VrfSummaries.VrfSummary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Arm.VrfSummaries.VrfSummary, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.vrf_id.is_set or
                    self.vrf_name_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.vrf_id.yfilter != YFilter.not_set or
                    self.vrf_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf-summary" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/vrf-summaries/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_id.get_name_leafdata())
                if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf-name" or name == "vrf-id" or name == "vrf-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-id"):
                    self.vrf_id = value
                    self.vrf_id.value_namespace = name_space
                    self.vrf_id.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name-xr"):
                    self.vrf_name_xr = value
                    self.vrf_name_xr.value_namespace = name_space
                    self.vrf_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf_summary:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf_summary:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf-summaries" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf-summary"):
                for c in self.vrf_summary:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv4Arm.VrfSummaries.VrfSummary()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf_summary.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf-summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RouterId(Entity):
        """
        IPv4 ARM Router ID information
        
        .. attribute:: interface_name
        
        	Interface name
        	**type**\:  str
        
        .. attribute:: router_id
        
        	Router ID
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vrf_id
        
        	VRF ID
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\:  str
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(Ipv4Arm.RouterId, self).__init__()

            self.yang_name = "router-id"
            self.yang_parent_name = "ipv4arm"

            self.interface_name = YLeaf(YType.str, "interface-name")

            self.router_id = YLeaf(YType.str, "router-id")

            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

            self.vrf_name = YLeaf(YType.str, "vrf-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("interface_name",
                            "router_id",
                            "vrf_id",
                            "vrf_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Arm.RouterId, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Arm.RouterId, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.interface_name.is_set or
                self.router_id.is_set or
                self.vrf_id.is_set or
                self.vrf_name.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.interface_name.yfilter != YFilter.not_set or
                self.router_id.yfilter != YFilter.not_set or
                self.vrf_id.yfilter != YFilter.not_set or
                self.vrf_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "router-id" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_name.get_name_leafdata())
            if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.router_id.get_name_leafdata())
            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_id.get_name_leafdata())
            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-name" or name == "router-id" or name == "vrf-id" or name == "vrf-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "interface-name"):
                self.interface_name = value
                self.interface_name.value_namespace = name_space
                self.interface_name.value_namespace_prefix = name_space_prefix
            if(value_path == "router-id"):
                self.router_id = value
                self.router_id.value_namespace = name_space
                self.router_id.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf-id"):
                self.vrf_id = value
                self.vrf_id.value_namespace = name_space
                self.vrf_id.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf-name"):
                self.vrf_name = value
                self.vrf_name.value_namespace = name_space
                self.vrf_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.multicast_host_interface.is_set or
            (self.addresses is not None and self.addresses.has_data()) or
            (self.router_id is not None and self.router_id.has_data()) or
            (self.summary is not None and self.summary.has_data()) or
            (self.vrf_summaries is not None and self.vrf_summaries.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.multicast_host_interface.yfilter != YFilter.not_set or
            (self.addresses is not None and self.addresses.has_operation()) or
            (self.router_id is not None and self.router_id.has_operation()) or
            (self.summary is not None and self.summary.has_operation()) or
            (self.vrf_summaries is not None and self.vrf_summaries.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.multicast_host_interface.is_set or self.multicast_host_interface.yfilter != YFilter.not_set):
            leaf_name_data.append(self.multicast_host_interface.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "addresses"):
            if (self.addresses is None):
                self.addresses = Ipv4Arm.Addresses()
                self.addresses.parent = self
                self._children_name_map["addresses"] = "addresses"
            return self.addresses

        if (child_yang_name == "router-id"):
            if (self.router_id is None):
                self.router_id = Ipv4Arm.RouterId()
                self.router_id.parent = self
                self._children_name_map["router_id"] = "router-id"
            return self.router_id

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = Ipv4Arm.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        if (child_yang_name == "vrf-summaries"):
            if (self.vrf_summaries is None):
                self.vrf_summaries = Ipv4Arm.VrfSummaries()
                self.vrf_summaries.parent = self
                self._children_name_map["vrf_summaries"] = "vrf-summaries"
            return self.vrf_summaries

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "addresses" or name == "router-id" or name == "summary" or name == "vrf-summaries" or name == "multicast-host-interface"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "multicast-host-interface"):
            self.multicast_host_interface = value
            self.multicast_host_interface.value_namespace = name_space
            self.multicast_host_interface.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv4Arm()
        return self._top_entity

