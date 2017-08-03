""" Cisco_IOS_XR_ipv6_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-network\: IPv6 network operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv6MaIfAddrState(Enum):
    """
    Ipv6MaIfAddrState

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

    active = Enum.YLeaf(1, "active")

    deprecated = Enum.YLeaf(2, "deprecated")

    duplicate = Enum.YLeaf(3, "duplicate")

    inaccessible = Enum.YLeaf(4, "inaccessible")

    tentative = Enum.YLeaf(5, "tentative")


class Ipv6MaIfLineState(Enum):
    """
    Ipv6MaIfLineState

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

    down = Enum.YLeaf(1, "down")

    up = Enum.YLeaf(2, "up")

    unknown = Enum.YLeaf(3, "unknown")

    error = Enum.YLeaf(4, "error")


class Ipv6MaOperState(Enum):
    """
    Ipv6MaOperState

    Interface oper states

    .. data:: oper_up = 1

    	Interface oper state is up

    .. data:: oper_down = 2

    	Interface oper state is down

    """

    oper_up = Enum.YLeaf(1, "oper-up")

    oper_down = Enum.YLeaf(2, "oper-down")



class Ipv6Network(Entity):
    """
    IPv6 network operational data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 network operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes>`
    
    

    """

    _prefix = 'ipv6-ma-oper'
    _revision = '2015-10-20'

    def __init__(self):
        super(Ipv6Network, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-network"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ma-oper"

        self.nodes = Ipv6Network.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific IPv6 network operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-ma-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv6Network.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-network"

            self.node = YList(self)

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
                        super(Ipv6Network.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6Network.Nodes, self).__setattr__(name, value)


        class Node(Entity):
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
                super(Ipv6Network.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_data = Ipv6Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self._children_name_map["interface_data"] = "interface-data"
                self._children_yang_names.add("interface-data")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv6Network.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6Network.Nodes.Node, self).__setattr__(name, value)


            class InterfaceData(Entity):
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
                    super(Ipv6Network.Nodes.Node.InterfaceData, self).__init__()

                    self.yang_name = "interface-data"
                    self.yang_parent_name = "node"

                    self.summary = Ipv6Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.vrfs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")


                class Vrfs(Entity):
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
                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "interface-data"

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
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs, self).__setattr__(name, value)


                    class Vrf(Entity):
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
                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self._children_name_map["briefs"] = "briefs"
                            self._children_yang_names.add("briefs")

                            self.details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._children_yang_names.add("details")

                            self.global_briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs()
                            self.global_briefs.parent = self
                            self._children_name_map["global_briefs"] = "global-briefs"
                            self._children_yang_names.add("global-briefs")

                            self.global_details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails()
                            self.global_details.parent = self
                            self._children_name_map["global_details"] = "global-details"
                            self._children_yang_names.add("global-details")

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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__setattr__(name, value)


                        class Briefs(Entity):
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
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__init__()

                                self.yang_name = "briefs"
                                self.yang_parent_name = "vrf"

                                self.brief = YList(self)

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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__setattr__(name, value)


                            class Brief(Entity):
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
                                	**type**\:   :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**length:** 0..32
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__init__()

                                    self.yang_name = "brief"
                                    self.yang_parent_name = "briefs"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"
                                    self._children_yang_names.add("link-local-address")

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
                                        if name in ("interface_name",
                                                    "line_state",
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__setattr__(name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "brief"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "link-local-address" + path_buffer

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
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "brief"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

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
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.address:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.interface_name.is_set or
                                        self.line_state.is_set or
                                        self.vrf_name.is_set or
                                        (self.link_local_address is not None and self.link_local_address.has_data()))

                                def has_operation(self):
                                    for c in self.address:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.link_local_address is not None and self.link_local_address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "brief" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
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
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.address.append(c)
                                        return c

                                    if (child_yang_name == "link-local-address"):
                                        if (self.link_local_address is None):
                                            self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress()
                                            self.link_local_address.parent = self
                                            self._children_name_map["link_local_address"] = "link-local-address"
                                        return self.link_local_address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "link-local-address" or name == "interface-name" or name == "line-state" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.brief:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.brief:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "briefs" + path_buffer

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

                                if (child_yang_name == "brief"):
                                    for c in self.brief:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.brief.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "brief"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class GlobalDetails(Entity):
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
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails, self).__init__()

                                self.yang_name = "global-details"
                                self.yang_parent_name = "vrf"

                                self.global_detail = YList(self)

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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails, self).__setattr__(name, value)


                            class GlobalDetail(Entity):
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
                                	**type**\:   :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
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
                                	**type**\:   :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**length:** 0..32
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, self).__init__()

                                    self.yang_name = "global-detail"
                                    self.yang_parent_name = "global-details"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                                    self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                                    self.is_icmp_unreach_enabled = YLeaf(YType.boolean, "is-icmp-unreach-enabled")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                                    self.mtu = YLeaf(YType.uint32, "mtu")

                                    self.operation_state = YLeaf(YType.enumeration, "operation-state")

                                    self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self._children_name_map["access_control_list"] = "access-control-list"
                                    self._children_yang_names.add("access-control-list")

                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"
                                    self._children_yang_names.add("bgp-pa")

                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"
                                    self._children_yang_names.add("caps-utime")

                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                    self._children_yang_names.add("fwd-dis-utime")

                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                    self._children_yang_names.add("fwd-en-utime")

                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"
                                    self._children_yang_names.add("idb-utime")

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"
                                    self._children_yang_names.add("link-local-address")

                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self._children_name_map["multi_access_control_list"] = "multi-access-control-list"
                                    self._children_yang_names.add("multi-access-control-list")

                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"
                                    self._children_yang_names.add("rpf")

                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime()
                                    self.utime.parent = self
                                    self._children_name_map["utime"] = "utime"
                                    self._children_yang_names.add("utime")

                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self.multicast_group = YList(self)

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
                                                    "flow_tag_dst",
                                                    "flow_tag_src",
                                                    "is_icmp_unreach_enabled",
                                                    "line_state",
                                                    "mlacp_active",
                                                    "mtu",
                                                    "operation_state",
                                                    "rg_id_exists",
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, self).__setattr__(name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "global-detail"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "link-local-address" + path_buffer

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
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class AccessControlList(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, self).__init__()

                                        self.yang_name = "access-control-list"
                                        self.yang_parent_name = "global-detail"

                                        self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                        self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                        self.in_bound = YLeaf(YType.str, "in-bound")

                                        self.out_bound = YLeaf(YType.str, "out-bound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common_in_bound",
                                                        "common_out_bound",
                                                        "in_bound",
                                                        "out_bound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.common_in_bound.is_set or
                                            self.common_out_bound.is_set or
                                            self.in_bound.is_set or
                                            self.out_bound.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common_in_bound.yfilter != YFilter.not_set or
                                            self.common_out_bound.yfilter != YFilter.not_set or
                                            self.in_bound.yfilter != YFilter.not_set or
                                            self.out_bound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "access-control-list" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.common_in_bound.is_set or self.common_in_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_in_bound.get_name_leafdata())
                                        if (self.common_out_bound.is_set or self.common_out_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_out_bound.get_name_leafdata())
                                        if (self.in_bound.is_set or self.in_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.in_bound.get_name_leafdata())
                                        if (self.out_bound.is_set or self.out_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.out_bound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common-in-bound" or name == "common-out-bound" or name == "in-bound" or name == "out-bound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common-in-bound"):
                                            self.common_in_bound = value
                                            self.common_in_bound.value_namespace = name_space
                                            self.common_in_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "common-out-bound"):
                                            self.common_out_bound = value
                                            self.common_out_bound.value_namespace = name_space
                                            self.common_out_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "in-bound"):
                                            self.in_bound = value
                                            self.in_bound.value_namespace = name_space
                                            self.in_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "out-bound"):
                                            self.out_bound = value
                                            self.out_bound.value_namespace = name_space
                                            self.out_bound.value_namespace_prefix = name_space_prefix


                                class MultiAccessControlList(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList, self).__init__()

                                        self.yang_name = "multi-access-control-list"
                                        self.yang_parent_name = "global-detail"

                                        self.common = YLeafList(YType.str, "common")

                                        self.inbound = YLeafList(YType.str, "inbound")

                                        self.outbound = YLeafList(YType.str, "outbound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common",
                                                        "inbound",
                                                        "outbound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common.yfilter != YFilter.not_set or
                                            self.inbound.yfilter != YFilter.not_set or
                                            self.outbound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multi-access-control-list" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.common.get_name_leafdata())

                                        leaf_name_data.extend(self.inbound.get_name_leafdata())

                                        leaf_name_data.extend(self.outbound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common" or name == "inbound" or name == "outbound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common"):
                                            self.common.append(value)
                                        if(value_path == "inbound"):
                                            self.inbound.append(value)
                                        if(value_path == "outbound"):
                                            self.outbound.append(value)


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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "global-detail"

                                        self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                        self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.mode = YLeaf(YType.uint32, "mode")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("allow_default_route",
                                                        "allow_self_ping",
                                                        "enable",
                                                        "mode") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.allow_default_route.is_set or
                                            self.allow_self_ping.is_set or
                                            self.enable.is_set or
                                            self.mode.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.allow_default_route.yfilter != YFilter.not_set or
                                            self.allow_self_ping.yfilter != YFilter.not_set or
                                            self.enable.yfilter != YFilter.not_set or
                                            self.mode.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rpf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.allow_default_route.is_set or self.allow_default_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_default_route.get_name_leafdata())
                                        if (self.allow_self_ping.is_set or self.allow_self_ping.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_self_ping.get_name_leafdata())
                                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.enable.get_name_leafdata())
                                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mode.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "allow-default-route" or name == "allow-self-ping" or name == "enable" or name == "mode"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "allow-default-route"):
                                            self.allow_default_route = value
                                            self.allow_default_route.value_namespace = name_space
                                            self.allow_default_route.value_namespace_prefix = name_space_prefix
                                        if(value_path == "allow-self-ping"):
                                            self.allow_self_ping = value
                                            self.allow_self_ping.value_namespace = name_space
                                            self.allow_self_ping.value_namespace_prefix = name_space_prefix
                                        if(value_path == "enable"):
                                            self.enable = value
                                            self.enable.value_namespace = name_space
                                            self.enable.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mode"):
                                            self.mode = value
                                            self.mode.value_namespace = name_space
                                            self.mode.value_namespace_prefix = name_space_prefix


                                class BgpPa(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "global-detail"

                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                        self._children_yang_names.add("input")

                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._children_yang_names.add("output")


                                    class Input(Entity):
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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.uint32, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "input" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix


                                    class Output(Entity):
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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.uint32, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "output" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.input is not None and self.input.has_data()) or
                                            (self.output is not None and self.output.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.input is not None and self.input.has_operation()) or
                                            (self.output is not None and self.output.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "bgp-pa" + path_buffer

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

                                        if (child_yang_name == "input"):
                                            if (self.input is None):
                                                self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input()
                                                self.input.parent = self
                                                self._children_name_map["input"] = "input"
                                            return self.input

                                        if (child_yang_name == "output"):
                                            if (self.output is None):
                                                self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output()
                                                self.output.parent = self
                                                self._children_name_map["output"] = "output"
                                            return self.output

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "input" or name == "output"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Utime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime, self).__init__()

                                        self.yang_name = "utime"
                                        self.yang_parent_name = "global-detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "global-detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "idb-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "global-detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "caps-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "global-detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-en-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "global-detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-dis-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class MulticastGroup(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "global-detail"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multicast-group" + path_buffer

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

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "global-detail"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

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
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class ClientMulticastGroup(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, self).__init__()

                                        self.yang_name = "client-multicast-group"
                                        self.yang_parent_name = "global-detail"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "client-multicast-group" + path_buffer

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

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.address:
                                        if (c.has_data()):
                                            return True
                                    for c in self.client_multicast_group:
                                        if (c.has_data()):
                                            return True
                                    for c in self.multicast_group:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.interface_name.is_set or
                                        self.flow_tag_dst.is_set or
                                        self.flow_tag_src.is_set or
                                        self.is_icmp_unreach_enabled.is_set or
                                        self.line_state.is_set or
                                        self.mlacp_active.is_set or
                                        self.mtu.is_set or
                                        self.operation_state.is_set or
                                        self.rg_id_exists.is_set or
                                        self.vrf_name.is_set or
                                        (self.access_control_list is not None and self.access_control_list.has_data()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_data()) or
                                        (self.caps_utime is not None and self.caps_utime.has_data()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_data()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_data()) or
                                        (self.idb_utime is not None and self.idb_utime.has_data()) or
                                        (self.link_local_address is not None and self.link_local_address.has_data()) or
                                        (self.multi_access_control_list is not None and self.multi_access_control_list.has_data()) or
                                        (self.rpf is not None and self.rpf.has_data()) or
                                        (self.utime is not None and self.utime.has_data()))

                                def has_operation(self):
                                    for c in self.address:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.client_multicast_group:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.multicast_group:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.flow_tag_dst.yfilter != YFilter.not_set or
                                        self.flow_tag_src.yfilter != YFilter.not_set or
                                        self.is_icmp_unreach_enabled.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.mlacp_active.yfilter != YFilter.not_set or
                                        self.mtu.yfilter != YFilter.not_set or
                                        self.operation_state.yfilter != YFilter.not_set or
                                        self.rg_id_exists.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.access_control_list is not None and self.access_control_list.has_operation()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_operation()) or
                                        (self.caps_utime is not None and self.caps_utime.has_operation()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_operation()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_operation()) or
                                        (self.idb_utime is not None and self.idb_utime.has_operation()) or
                                        (self.link_local_address is not None and self.link_local_address.has_operation()) or
                                        (self.multi_access_control_list is not None and self.multi_access_control_list.has_operation()) or
                                        (self.rpf is not None and self.rpf.has_operation()) or
                                        (self.utime is not None and self.utime.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "global-detail" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.flow_tag_dst.is_set or self.flow_tag_dst.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_dst.get_name_leafdata())
                                    if (self.flow_tag_src.is_set or self.flow_tag_src.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_src.get_name_leafdata())
                                    if (self.is_icmp_unreach_enabled.is_set or self.is_icmp_unreach_enabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_icmp_unreach_enabled.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
                                    if (self.mlacp_active.is_set or self.mlacp_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mlacp_active.get_name_leafdata())
                                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mtu.get_name_leafdata())
                                    if (self.operation_state.is_set or self.operation_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.operation_state.get_name_leafdata())
                                    if (self.rg_id_exists.is_set or self.rg_id_exists.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rg_id_exists.get_name_leafdata())
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "access-control-list"):
                                        if (self.access_control_list is None):
                                            self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList()
                                            self.access_control_list.parent = self
                                            self._children_name_map["access_control_list"] = "access-control-list"
                                        return self.access_control_list

                                    if (child_yang_name == "address"):
                                        for c in self.address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.address.append(c)
                                        return c

                                    if (child_yang_name == "bgp-pa"):
                                        if (self.bgp_pa is None):
                                            self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa()
                                            self.bgp_pa.parent = self
                                            self._children_name_map["bgp_pa"] = "bgp-pa"
                                        return self.bgp_pa

                                    if (child_yang_name == "caps-utime"):
                                        if (self.caps_utime is None):
                                            self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime()
                                            self.caps_utime.parent = self
                                            self._children_name_map["caps_utime"] = "caps-utime"
                                        return self.caps_utime

                                    if (child_yang_name == "client-multicast-group"):
                                        for c in self.client_multicast_group:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.client_multicast_group.append(c)
                                        return c

                                    if (child_yang_name == "fwd-dis-utime"):
                                        if (self.fwd_dis_utime is None):
                                            self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime()
                                            self.fwd_dis_utime.parent = self
                                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                        return self.fwd_dis_utime

                                    if (child_yang_name == "fwd-en-utime"):
                                        if (self.fwd_en_utime is None):
                                            self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime()
                                            self.fwd_en_utime.parent = self
                                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                        return self.fwd_en_utime

                                    if (child_yang_name == "idb-utime"):
                                        if (self.idb_utime is None):
                                            self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime()
                                            self.idb_utime.parent = self
                                            self._children_name_map["idb_utime"] = "idb-utime"
                                        return self.idb_utime

                                    if (child_yang_name == "link-local-address"):
                                        if (self.link_local_address is None):
                                            self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress()
                                            self.link_local_address.parent = self
                                            self._children_name_map["link_local_address"] = "link-local-address"
                                        return self.link_local_address

                                    if (child_yang_name == "multi-access-control-list"):
                                        if (self.multi_access_control_list is None):
                                            self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList()
                                            self.multi_access_control_list.parent = self
                                            self._children_name_map["multi_access_control_list"] = "multi-access-control-list"
                                        return self.multi_access_control_list

                                    if (child_yang_name == "multicast-group"):
                                        for c in self.multicast_group:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.multicast_group.append(c)
                                        return c

                                    if (child_yang_name == "rpf"):
                                        if (self.rpf is None):
                                            self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf()
                                            self.rpf.parent = self
                                            self._children_name_map["rpf"] = "rpf"
                                        return self.rpf

                                    if (child_yang_name == "utime"):
                                        if (self.utime is None):
                                            self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime()
                                            self.utime.parent = self
                                            self._children_name_map["utime"] = "utime"
                                        return self.utime

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-control-list" or name == "address" or name == "bgp-pa" or name == "caps-utime" or name == "client-multicast-group" or name == "fwd-dis-utime" or name == "fwd-en-utime" or name == "idb-utime" or name == "link-local-address" or name == "multi-access-control-list" or name == "multicast-group" or name == "rpf" or name == "utime" or name == "interface-name" or name == "flow-tag-dst" or name == "flow-tag-src" or name == "is-icmp-unreach-enabled" or name == "line-state" or name == "mlacp-active" or name == "mtu" or name == "operation-state" or name == "rg-id-exists" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-dst"):
                                        self.flow_tag_dst = value
                                        self.flow_tag_dst.value_namespace = name_space
                                        self.flow_tag_dst.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-src"):
                                        self.flow_tag_src = value
                                        self.flow_tag_src.value_namespace = name_space
                                        self.flow_tag_src.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-icmp-unreach-enabled"):
                                        self.is_icmp_unreach_enabled = value
                                        self.is_icmp_unreach_enabled.value_namespace = name_space
                                        self.is_icmp_unreach_enabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mlacp-active"):
                                        self.mlacp_active = value
                                        self.mlacp_active.value_namespace = name_space
                                        self.mlacp_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mtu"):
                                        self.mtu = value
                                        self.mtu.value_namespace = name_space
                                        self.mtu.value_namespace_prefix = name_space_prefix
                                    if(value_path == "operation-state"):
                                        self.operation_state = value
                                        self.operation_state.value_namespace = name_space
                                        self.operation_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rg-id-exists"):
                                        self.rg_id_exists = value
                                        self.rg_id_exists.value_namespace = name_space
                                        self.rg_id_exists.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.global_detail:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.global_detail:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "global-details" + path_buffer

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

                                if (child_yang_name == "global-detail"):
                                    for c in self.global_detail:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.global_detail.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "global-detail"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class GlobalBriefs(Entity):
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
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs, self).__init__()

                                self.yang_name = "global-briefs"
                                self.yang_parent_name = "vrf"

                                self.global_brief = YList(self)

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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs, self).__setattr__(name, value)


                            class GlobalBrief(Entity):
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
                                	**type**\:   :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:   :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**length:** 0..32
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, self).__init__()

                                    self.yang_name = "global-brief"
                                    self.yang_parent_name = "global-briefs"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"
                                    self._children_yang_names.add("link-local-address")

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
                                        if name in ("interface_name",
                                                    "line_state",
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, self).__setattr__(name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "global-brief"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "link-local-address" + path_buffer

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
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "global-brief"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

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
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.address:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.interface_name.is_set or
                                        self.line_state.is_set or
                                        self.vrf_name.is_set or
                                        (self.link_local_address is not None and self.link_local_address.has_data()))

                                def has_operation(self):
                                    for c in self.address:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.link_local_address is not None and self.link_local_address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "global-brief" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
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
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.address.append(c)
                                        return c

                                    if (child_yang_name == "link-local-address"):
                                        if (self.link_local_address is None):
                                            self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress()
                                            self.link_local_address.parent = self
                                            self._children_name_map["link_local_address"] = "link-local-address"
                                        return self.link_local_address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "link-local-address" or name == "interface-name" or name == "line-state" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.global_brief:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.global_brief:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "global-briefs" + path_buffer

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

                                if (child_yang_name == "global-brief"):
                                    for c in self.global_brief:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.global_brief.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "global-brief"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Details(Entity):
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
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "vrf"

                                self.detail = YList(self)

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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__setattr__(name, value)


                            class Detail(Entity):
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
                                	**type**\:   :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
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
                                	**type**\:   :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**length:** 0..32
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                                    self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                                    self.is_icmp_unreach_enabled = YLeaf(YType.boolean, "is-icmp-unreach-enabled")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                                    self.mtu = YLeaf(YType.uint32, "mtu")

                                    self.operation_state = YLeaf(YType.enumeration, "operation-state")

                                    self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self._children_name_map["access_control_list"] = "access-control-list"
                                    self._children_yang_names.add("access-control-list")

                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"
                                    self._children_yang_names.add("bgp-pa")

                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"
                                    self._children_yang_names.add("caps-utime")

                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                    self._children_yang_names.add("fwd-dis-utime")

                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                    self._children_yang_names.add("fwd-en-utime")

                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"
                                    self._children_yang_names.add("idb-utime")

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"
                                    self._children_yang_names.add("link-local-address")

                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self._children_name_map["multi_access_control_list"] = "multi-access-control-list"
                                    self._children_yang_names.add("multi-access-control-list")

                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"
                                    self._children_yang_names.add("rpf")

                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime()
                                    self.utime.parent = self
                                    self._children_name_map["utime"] = "utime"
                                    self._children_yang_names.add("utime")

                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self.multicast_group = YList(self)

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
                                                    "flow_tag_dst",
                                                    "flow_tag_src",
                                                    "is_icmp_unreach_enabled",
                                                    "line_state",
                                                    "mlacp_active",
                                                    "mtu",
                                                    "operation_state",
                                                    "rg_id_exists",
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__setattr__(name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "detail"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "link-local-address" + path_buffer

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
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class AccessControlList(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, self).__init__()

                                        self.yang_name = "access-control-list"
                                        self.yang_parent_name = "detail"

                                        self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                        self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                        self.in_bound = YLeaf(YType.str, "in-bound")

                                        self.out_bound = YLeaf(YType.str, "out-bound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common_in_bound",
                                                        "common_out_bound",
                                                        "in_bound",
                                                        "out_bound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.common_in_bound.is_set or
                                            self.common_out_bound.is_set or
                                            self.in_bound.is_set or
                                            self.out_bound.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common_in_bound.yfilter != YFilter.not_set or
                                            self.common_out_bound.yfilter != YFilter.not_set or
                                            self.in_bound.yfilter != YFilter.not_set or
                                            self.out_bound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "access-control-list" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.common_in_bound.is_set or self.common_in_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_in_bound.get_name_leafdata())
                                        if (self.common_out_bound.is_set or self.common_out_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_out_bound.get_name_leafdata())
                                        if (self.in_bound.is_set or self.in_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.in_bound.get_name_leafdata())
                                        if (self.out_bound.is_set or self.out_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.out_bound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common-in-bound" or name == "common-out-bound" or name == "in-bound" or name == "out-bound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common-in-bound"):
                                            self.common_in_bound = value
                                            self.common_in_bound.value_namespace = name_space
                                            self.common_in_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "common-out-bound"):
                                            self.common_out_bound = value
                                            self.common_out_bound.value_namespace = name_space
                                            self.common_out_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "in-bound"):
                                            self.in_bound = value
                                            self.in_bound.value_namespace = name_space
                                            self.in_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "out-bound"):
                                            self.out_bound = value
                                            self.out_bound.value_namespace = name_space
                                            self.out_bound.value_namespace_prefix = name_space_prefix


                                class MultiAccessControlList(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList, self).__init__()

                                        self.yang_name = "multi-access-control-list"
                                        self.yang_parent_name = "detail"

                                        self.common = YLeafList(YType.str, "common")

                                        self.inbound = YLeafList(YType.str, "inbound")

                                        self.outbound = YLeafList(YType.str, "outbound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common",
                                                        "inbound",
                                                        "outbound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common.yfilter != YFilter.not_set or
                                            self.inbound.yfilter != YFilter.not_set or
                                            self.outbound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multi-access-control-list" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.common.get_name_leafdata())

                                        leaf_name_data.extend(self.inbound.get_name_leafdata())

                                        leaf_name_data.extend(self.outbound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common" or name == "inbound" or name == "outbound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common"):
                                            self.common.append(value)
                                        if(value_path == "inbound"):
                                            self.inbound.append(value)
                                        if(value_path == "outbound"):
                                            self.outbound.append(value)


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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "detail"

                                        self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                        self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.mode = YLeaf(YType.uint32, "mode")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("allow_default_route",
                                                        "allow_self_ping",
                                                        "enable",
                                                        "mode") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.allow_default_route.is_set or
                                            self.allow_self_ping.is_set or
                                            self.enable.is_set or
                                            self.mode.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.allow_default_route.yfilter != YFilter.not_set or
                                            self.allow_self_ping.yfilter != YFilter.not_set or
                                            self.enable.yfilter != YFilter.not_set or
                                            self.mode.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rpf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.allow_default_route.is_set or self.allow_default_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_default_route.get_name_leafdata())
                                        if (self.allow_self_ping.is_set or self.allow_self_ping.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_self_ping.get_name_leafdata())
                                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.enable.get_name_leafdata())
                                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mode.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "allow-default-route" or name == "allow-self-ping" or name == "enable" or name == "mode"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "allow-default-route"):
                                            self.allow_default_route = value
                                            self.allow_default_route.value_namespace = name_space
                                            self.allow_default_route.value_namespace_prefix = name_space_prefix
                                        if(value_path == "allow-self-ping"):
                                            self.allow_self_ping = value
                                            self.allow_self_ping.value_namespace = name_space
                                            self.allow_self_ping.value_namespace_prefix = name_space_prefix
                                        if(value_path == "enable"):
                                            self.enable = value
                                            self.enable.value_namespace = name_space
                                            self.enable.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mode"):
                                            self.mode = value
                                            self.mode.value_namespace = name_space
                                            self.mode.value_namespace_prefix = name_space_prefix


                                class BgpPa(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "detail"

                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                        self._children_yang_names.add("input")

                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._children_yang_names.add("output")


                                    class Input(Entity):
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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.uint32, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "input" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix


                                    class Output(Entity):
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
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.uint32, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "output" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.input is not None and self.input.has_data()) or
                                            (self.output is not None and self.output.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.input is not None and self.input.has_operation()) or
                                            (self.output is not None and self.output.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "bgp-pa" + path_buffer

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

                                        if (child_yang_name == "input"):
                                            if (self.input is None):
                                                self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                                self.input.parent = self
                                                self._children_name_map["input"] = "input"
                                            return self.input

                                        if (child_yang_name == "output"):
                                            if (self.output is None):
                                                self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                                self.output.parent = self
                                                self._children_name_map["output"] = "output"
                                            return self.output

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "input" or name == "output"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Utime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime, self).__init__()

                                        self.yang_name = "utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "idb-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "caps-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-en-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-dis-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class MulticastGroup(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "detail"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multicast-group" + path_buffer

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

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:   :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "detail"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_state = YLeaf(YType.enumeration, "address-state")

                                        self.is_anycast = YLeaf(YType.boolean, "is-anycast")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "address_state",
                                                        "is_anycast",
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_state.is_set or
                                            self.is_anycast.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_state.yfilter != YFilter.not_set or
                                            self.is_anycast.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

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
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_state.is_set or self.address_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_state.get_name_leafdata())
                                        if (self.is_anycast.is_set or self.is_anycast.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.is_anycast.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-state" or name == "is-anycast" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-state"):
                                            self.address_state = value
                                            self.address_state.value_namespace = name_space
                                            self.address_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "is-anycast"):
                                            self.is_anycast = value
                                            self.is_anycast.value_namespace = name_space
                                            self.is_anycast.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix


                                class ClientMulticastGroup(Entity):
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
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, self).__init__()

                                        self.yang_name = "client-multicast-group"
                                        self.yang_parent_name = "detail"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "client-multicast-group" + path_buffer

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

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.address:
                                        if (c.has_data()):
                                            return True
                                    for c in self.client_multicast_group:
                                        if (c.has_data()):
                                            return True
                                    for c in self.multicast_group:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.interface_name.is_set or
                                        self.flow_tag_dst.is_set or
                                        self.flow_tag_src.is_set or
                                        self.is_icmp_unreach_enabled.is_set or
                                        self.line_state.is_set or
                                        self.mlacp_active.is_set or
                                        self.mtu.is_set or
                                        self.operation_state.is_set or
                                        self.rg_id_exists.is_set or
                                        self.vrf_name.is_set or
                                        (self.access_control_list is not None and self.access_control_list.has_data()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_data()) or
                                        (self.caps_utime is not None and self.caps_utime.has_data()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_data()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_data()) or
                                        (self.idb_utime is not None and self.idb_utime.has_data()) or
                                        (self.link_local_address is not None and self.link_local_address.has_data()) or
                                        (self.multi_access_control_list is not None and self.multi_access_control_list.has_data()) or
                                        (self.rpf is not None and self.rpf.has_data()) or
                                        (self.utime is not None and self.utime.has_data()))

                                def has_operation(self):
                                    for c in self.address:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.client_multicast_group:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.multicast_group:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.flow_tag_dst.yfilter != YFilter.not_set or
                                        self.flow_tag_src.yfilter != YFilter.not_set or
                                        self.is_icmp_unreach_enabled.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.mlacp_active.yfilter != YFilter.not_set or
                                        self.mtu.yfilter != YFilter.not_set or
                                        self.operation_state.yfilter != YFilter.not_set or
                                        self.rg_id_exists.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.access_control_list is not None and self.access_control_list.has_operation()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_operation()) or
                                        (self.caps_utime is not None and self.caps_utime.has_operation()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_operation()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_operation()) or
                                        (self.idb_utime is not None and self.idb_utime.has_operation()) or
                                        (self.link_local_address is not None and self.link_local_address.has_operation()) or
                                        (self.multi_access_control_list is not None and self.multi_access_control_list.has_operation()) or
                                        (self.rpf is not None and self.rpf.has_operation()) or
                                        (self.utime is not None and self.utime.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.flow_tag_dst.is_set or self.flow_tag_dst.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_dst.get_name_leafdata())
                                    if (self.flow_tag_src.is_set or self.flow_tag_src.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_src.get_name_leafdata())
                                    if (self.is_icmp_unreach_enabled.is_set or self.is_icmp_unreach_enabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_icmp_unreach_enabled.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
                                    if (self.mlacp_active.is_set or self.mlacp_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mlacp_active.get_name_leafdata())
                                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mtu.get_name_leafdata())
                                    if (self.operation_state.is_set or self.operation_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.operation_state.get_name_leafdata())
                                    if (self.rg_id_exists.is_set or self.rg_id_exists.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rg_id_exists.get_name_leafdata())
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "access-control-list"):
                                        if (self.access_control_list is None):
                                            self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList()
                                            self.access_control_list.parent = self
                                            self._children_name_map["access_control_list"] = "access-control-list"
                                        return self.access_control_list

                                    if (child_yang_name == "address"):
                                        for c in self.address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.address.append(c)
                                        return c

                                    if (child_yang_name == "bgp-pa"):
                                        if (self.bgp_pa is None):
                                            self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                            self.bgp_pa.parent = self
                                            self._children_name_map["bgp_pa"] = "bgp-pa"
                                        return self.bgp_pa

                                    if (child_yang_name == "caps-utime"):
                                        if (self.caps_utime is None):
                                            self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                            self.caps_utime.parent = self
                                            self._children_name_map["caps_utime"] = "caps-utime"
                                        return self.caps_utime

                                    if (child_yang_name == "client-multicast-group"):
                                        for c in self.client_multicast_group:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.client_multicast_group.append(c)
                                        return c

                                    if (child_yang_name == "fwd-dis-utime"):
                                        if (self.fwd_dis_utime is None):
                                            self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                            self.fwd_dis_utime.parent = self
                                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                        return self.fwd_dis_utime

                                    if (child_yang_name == "fwd-en-utime"):
                                        if (self.fwd_en_utime is None):
                                            self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                            self.fwd_en_utime.parent = self
                                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                        return self.fwd_en_utime

                                    if (child_yang_name == "idb-utime"):
                                        if (self.idb_utime is None):
                                            self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                            self.idb_utime.parent = self
                                            self._children_name_map["idb_utime"] = "idb-utime"
                                        return self.idb_utime

                                    if (child_yang_name == "link-local-address"):
                                        if (self.link_local_address is None):
                                            self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress()
                                            self.link_local_address.parent = self
                                            self._children_name_map["link_local_address"] = "link-local-address"
                                        return self.link_local_address

                                    if (child_yang_name == "multi-access-control-list"):
                                        if (self.multi_access_control_list is None):
                                            self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList()
                                            self.multi_access_control_list.parent = self
                                            self._children_name_map["multi_access_control_list"] = "multi-access-control-list"
                                        return self.multi_access_control_list

                                    if (child_yang_name == "multicast-group"):
                                        for c in self.multicast_group:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.multicast_group.append(c)
                                        return c

                                    if (child_yang_name == "rpf"):
                                        if (self.rpf is None):
                                            self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                            self.rpf.parent = self
                                            self._children_name_map["rpf"] = "rpf"
                                        return self.rpf

                                    if (child_yang_name == "utime"):
                                        if (self.utime is None):
                                            self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime()
                                            self.utime.parent = self
                                            self._children_name_map["utime"] = "utime"
                                        return self.utime

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-control-list" or name == "address" or name == "bgp-pa" or name == "caps-utime" or name == "client-multicast-group" or name == "fwd-dis-utime" or name == "fwd-en-utime" or name == "idb-utime" or name == "link-local-address" or name == "multi-access-control-list" or name == "multicast-group" or name == "rpf" or name == "utime" or name == "interface-name" or name == "flow-tag-dst" or name == "flow-tag-src" or name == "is-icmp-unreach-enabled" or name == "line-state" or name == "mlacp-active" or name == "mtu" or name == "operation-state" or name == "rg-id-exists" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-dst"):
                                        self.flow_tag_dst = value
                                        self.flow_tag_dst.value_namespace = name_space
                                        self.flow_tag_dst.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-src"):
                                        self.flow_tag_src = value
                                        self.flow_tag_src.value_namespace = name_space
                                        self.flow_tag_src.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-icmp-unreach-enabled"):
                                        self.is_icmp_unreach_enabled = value
                                        self.is_icmp_unreach_enabled.value_namespace = name_space
                                        self.is_icmp_unreach_enabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mlacp-active"):
                                        self.mlacp_active = value
                                        self.mlacp_active.value_namespace = name_space
                                        self.mlacp_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mtu"):
                                        self.mtu = value
                                        self.mtu.value_namespace = name_space
                                        self.mtu.value_namespace_prefix = name_space_prefix
                                    if(value_path == "operation-state"):
                                        self.operation_state = value
                                        self.operation_state.value_namespace = name_space
                                        self.operation_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rg-id-exists"):
                                        self.rg_id_exists = value
                                        self.rg_id_exists.value_namespace = name_space
                                        self.rg_id_exists.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.detail:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.detail:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "details" + path_buffer

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

                                if (child_yang_name == "detail"):
                                    for c in self.detail:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.detail.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.vrf_name.is_set or
                                (self.briefs is not None and self.briefs.has_data()) or
                                (self.details is not None and self.details.has_data()) or
                                (self.global_briefs is not None and self.global_briefs.has_data()) or
                                (self.global_details is not None and self.global_details.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                (self.briefs is not None and self.briefs.has_operation()) or
                                (self.details is not None and self.details.has_operation()) or
                                (self.global_briefs is not None and self.global_briefs.has_operation()) or
                                (self.global_details is not None and self.global_details.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                            if (child_yang_name == "briefs"):
                                if (self.briefs is None):
                                    self.briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                                    self.briefs.parent = self
                                    self._children_name_map["briefs"] = "briefs"
                                return self.briefs

                            if (child_yang_name == "details"):
                                if (self.details is None):
                                    self.details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                                    self.details.parent = self
                                    self._children_name_map["details"] = "details"
                                return self.details

                            if (child_yang_name == "global-briefs"):
                                if (self.global_briefs is None):
                                    self.global_briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs()
                                    self.global_briefs.parent = self
                                    self._children_name_map["global_briefs"] = "global-briefs"
                                return self.global_briefs

                            if (child_yang_name == "global-details"):
                                if (self.global_details is None):
                                    self.global_details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails()
                                    self.global_details.parent = self
                                    self._children_name_map["global_details"] = "global-details"
                                return self.global_details

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "briefs" or name == "details" or name == "global-briefs" or name == "global-details" or name == "vrf-name"):
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

                        if (child_yang_name == "vrf"):
                            for c in self.vrf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf()
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


                class Summary(Entity):
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
                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "interface-data"

                        self.if_up_down_basecaps_up = YLeaf(YType.uint32, "if-up-down-basecaps-up")

                        self.if_down_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self._children_name_map["if_down_down"] = "if-down-down"
                        self._children_yang_names.add("if-down-down")

                        self.if_shutdown_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                        self._children_yang_names.add("if-shutdown-down")

                        self.if_up_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self._children_name_map["if_up_down"] = "if-up-down"
                        self._children_yang_names.add("if-up-down")

                        self.if_up_up = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self
                        self._children_name_map["if_up_up"] = "if-up-up"
                        self._children_yang_names.add("if-up-up")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_up_down_basecaps_up") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Summary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6Network.Nodes.Node.InterfaceData.Summary, self).__setattr__(name, value)


                    class IfUpUp(Entity):
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
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__init__()

                            self.yang_name = "if-up-up"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-up-up" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfUpDown(Entity):
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
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__init__()

                            self.yang_name = "if-up-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-up-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfDownDown(Entity):
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
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__init__()

                            self.yang_name = "if-down-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-down-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfShutdownDown(Entity):
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
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__init__()

                            self.yang_name = "if-shutdown-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-shutdown-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.if_up_down_basecaps_up.is_set or
                            (self.if_down_down is not None and self.if_down_down.has_data()) or
                            (self.if_shutdown_down is not None and self.if_shutdown_down.has_data()) or
                            (self.if_up_down is not None and self.if_up_down.has_data()) or
                            (self.if_up_up is not None and self.if_up_up.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_up_down_basecaps_up.yfilter != YFilter.not_set or
                            (self.if_down_down is not None and self.if_down_down.has_operation()) or
                            (self.if_shutdown_down is not None and self.if_shutdown_down.has_operation()) or
                            (self.if_up_down is not None and self.if_up_down.has_operation()) or
                            (self.if_up_up is not None and self.if_up_up.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_up_down_basecaps_up.is_set or self.if_up_down_basecaps_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_up_down_basecaps_up.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "if-down-down"):
                            if (self.if_down_down is None):
                                self.if_down_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                                self.if_down_down.parent = self
                                self._children_name_map["if_down_down"] = "if-down-down"
                            return self.if_down_down

                        if (child_yang_name == "if-shutdown-down"):
                            if (self.if_shutdown_down is None):
                                self.if_shutdown_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                                self.if_shutdown_down.parent = self
                                self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                            return self.if_shutdown_down

                        if (child_yang_name == "if-up-down"):
                            if (self.if_up_down is None):
                                self.if_up_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                                self.if_up_down.parent = self
                                self._children_name_map["if_up_down"] = "if-up-down"
                            return self.if_up_down

                        if (child_yang_name == "if-up-up"):
                            if (self.if_up_up is None):
                                self.if_up_up = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                                self.if_up_up.parent = self
                                self._children_name_map["if_up_up"] = "if-up-up"
                            return self.if_up_up

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-down-down" or name == "if-shutdown-down" or name == "if-up-down" or name == "if-up-up" or name == "if-up-down-basecaps-up"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-up-down-basecaps-up"):
                            self.if_up_down_basecaps_up = value
                            self.if_up_down_basecaps_up.value_namespace = name_space
                            self.if_up_down_basecaps_up.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.summary is not None and self.summary.has_data()) or
                        (self.vrfs is not None and self.vrfs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.summary is not None and self.summary.has_operation()) or
                        (self.vrfs is not None and self.vrfs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-data" + path_buffer

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

                    if (child_yang_name == "summary"):
                        if (self.summary is None):
                            self.summary = Ipv6Network.Nodes.Node.InterfaceData.Summary()
                            self.summary.parent = self
                            self._children_name_map["summary"] = "summary"
                        return self.summary

                    if (child_yang_name == "vrfs"):
                        if (self.vrfs is None):
                            self.vrfs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"
                        return self.vrfs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "summary" or name == "vrfs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.interface_data is not None and self.interface_data.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.interface_data is not None and self.interface_data.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-data"):
                    if (self.interface_data is None):
                        self.interface_data = Ipv6Network.Nodes.Node.InterfaceData()
                        self.interface_data.parent = self
                        self._children_name_map["interface_data"] = "interface-data"
                    return self.interface_data

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-data" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv6Network.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Ipv6Network.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ipv6Network()
        return self._top_entity

