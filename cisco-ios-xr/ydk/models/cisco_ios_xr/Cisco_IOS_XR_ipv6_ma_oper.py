""" Cisco_IOS_XR_ipv6_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-network\: IPv6 network operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6MaIfAddrState(Enum):
    """
    Ipv6MaIfAddrState (Enum Class)

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
    Ipv6MaIfLineState (Enum Class)

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
    Ipv6MaOperState (Enum Class)

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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes>`
    
    

    """

    _prefix = 'ipv6-ma-oper'
    _revision = '2017-08-09'

    def __init__(self):
        super(Ipv6Network, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-network"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ma-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ipv6Network.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Ipv6Network.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Network, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific IPv6 network operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-ma-oper'
        _revision = '2017-08-09'

        def __init__(self):
            super(Ipv6Network.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-network"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ipv6Network.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Network.Nodes, [], name, value)


        class Node(Entity):
            """
            IPv6 network operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_data
            
            	IPv6 network operational interface data
            	**type**\:  :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData>`
            
            

            """

            _prefix = 'ipv6-ma-oper'
            _revision = '2017-08-09'

            def __init__(self):
                super(Ipv6Network.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("interface-data", ("interface_data", Ipv6Network.Nodes.Node.InterfaceData))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.interface_data = Ipv6Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self._children_name_map["interface_data"] = "interface-data"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ma-oper:ipv6-network/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Network.Nodes.Node, ['node_name'], name, value)


            class InterfaceData(Entity):
                """
                IPv6 network operational interface data
                
                .. attribute:: vrfs
                
                	VRF specific IPv6 network operational interface data
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs>`
                
                .. attribute:: summary
                
                	Summary of IPv6 network operational interface data on a node
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary>`
                
                

                """

                _prefix = 'ipv6-ma-oper'
                _revision = '2017-08-09'

                def __init__(self):
                    super(Ipv6Network.Nodes.Node.InterfaceData, self).__init__()

                    self.yang_name = "interface-data"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv6Network.Nodes.Node.InterfaceData.Vrfs)), ("summary", ("summary", Ipv6Network.Nodes.Node.InterfaceData.Summary))])
                    self._leafs = OrderedDict()

                    self.vrfs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"

                    self.summary = Ipv6Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._segment_path = lambda: "interface-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData, [], name, value)


                class Vrfs(Entity):
                    """
                    VRF specific IPv6 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF ID of an interface belong to
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2017-08-09'

                    def __init__(self):
                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        VRF ID of an interface belong to
                        
                        .. attribute:: vrf_name  (key)
                        
                        	The VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv6 network operational data for a node
                        	**type**\:  :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        .. attribute:: global_details
                        
                        	Detail interface IPv4 network operational data for global data
                        	**type**\:  :py:class:`GlobalDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails>`
                        
                        .. attribute:: global_briefs
                        
                        	Brief interface IPv6 network operational data from global data
                        	**type**\:  :py:class:`GlobalBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs>`
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2017-08-09'

                        def __init__(self):
                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("briefs", ("briefs", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs)), ("global-details", ("global_details", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails)), ("global-briefs", ("global_briefs", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs)), ("details", ("details", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self._children_name_map["briefs"] = "briefs"

                            self.global_details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails()
                            self.global_details.parent = self
                            self._children_name_map["global_details"] = "global-details"

                            self.global_briefs = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs()
                            self.global_briefs.parent = self
                            self._children_name_map["global_briefs"] = "global-briefs"

                            self.details = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Briefs(Entity):
                            """
                            Brief interface IPv6 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2017-08-09'

                            def __init__(self):
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__init__()

                                self.yang_name = "briefs"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("brief", ("brief", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief))])
                                self._leafs = OrderedDict()

                                self.brief = YList(self)
                                self._segment_path = lambda: "briefs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, [], name, value)


                            class Brief(Entity):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2017-08-09'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__init__()

                                    self.yang_name = "brief"
                                    self.yang_parent_name = "briefs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.vrf_name = None

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"

                                    self.address = YList(self)
                                    self._segment_path = lambda: "brief" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, ['interface_name', u'line_state', u'vrf_name'], name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "brief"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "brief"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                        class GlobalDetails(Entity):
                            """
                            Detail interface IPv4 network operational
                            data for global data
                            
                            .. attribute:: global_detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`GlobalDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2017-08-09'

                            def __init__(self):
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails, self).__init__()

                                self.yang_name = "global-details"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("global-detail", ("global_detail", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail))])
                                self._leafs = OrderedDict()

                                self.global_detail = YList(self)
                                self._segment_path = lambda: "global-details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails, [], name, value)


                            class GlobalDetail(Entity):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress>`
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:  :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList>`
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:  :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList>`
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:  :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:  :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:  :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:  :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime>`
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:  :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:  :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\: bool
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\: bool
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\: bool
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup>`
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address>`
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of  		 :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2017-08-09'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, self).__init__()

                                    self.yang_name = "global-detail"
                                    self.yang_parent_name = "global-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress)), ("access-control-list", ("access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList)), ("multi-access-control-list", ("multi_access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList)), ("rpf", ("rpf", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa)), ("utime", ("utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime)), ("idb-utime", ("idb_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime)), ("caps-utime", ("caps_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime)), ("fwd-en-utime", ("fwd_en_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime)), ("fwd-dis-utime", ("fwd_dis_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime)), ("multicast-group", ("multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address)), ("client-multicast-group", ("client_multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                        ('operation_state', (YLeaf(YType.enumeration, 'operation-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperState', '')])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('is_icmp_unreach_enabled', (YLeaf(YType.boolean, 'is-icmp-unreach-enabled'), ['bool'])),
                                        ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                        ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                        ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                        ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.mtu = None
                                    self.operation_state = None
                                    self.vrf_name = None
                                    self.is_icmp_unreach_enabled = None
                                    self.rg_id_exists = None
                                    self.mlacp_active = None
                                    self.flow_tag_src = None
                                    self.flow_tag_dst = None

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"

                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self._children_name_map["access_control_list"] = "access-control-list"

                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self._children_name_map["multi_access_control_list"] = "multi-access-control-list"

                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"

                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"

                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime()
                                    self.utime.parent = self
                                    self._children_name_map["utime"] = "utime"

                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"

                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"

                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"

                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"

                                    self.multicast_group = YList(self)
                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self._segment_path = lambda: "global-detail" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, ['interface_name', u'line_state', u'mtu', u'operation_state', u'vrf_name', u'is_icmp_unreach_enabled', u'rg_id_exists', u'mlacp_active', u'flow_tag_src', u'flow_tag_dst'], name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class AccessControlList(Entity):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, self).__init__()

                                        self.yang_name = "access-control-list"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_bound', (YLeaf(YType.str, 'in-bound'), ['str'])),
                                            ('out_bound', (YLeaf(YType.str, 'out-bound'), ['str'])),
                                            ('common_in_bound', (YLeaf(YType.str, 'common-in-bound'), ['str'])),
                                            ('common_out_bound', (YLeaf(YType.str, 'common-out-bound'), ['str'])),
                                        ])
                                        self.in_bound = None
                                        self.out_bound = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self._segment_path = lambda: "access-control-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, [u'in_bound', u'out_bound', u'common_in_bound', u'common_out_bound'], name, value)


                                class MultiAccessControlList(Entity):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound>`
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound>`
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList, self).__init__()

                                        self.yang_name = "multi-access-control-list"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("inbound", ("inbound", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound)), ("outbound", ("outbound", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound)), ("common", ("common", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common))])
                                        self._leafs = OrderedDict()

                                        self.inbound = YList(self)
                                        self.outbound = YList(self)
                                        self.common = YList(self)
                                        self._segment_path = lambda: "multi-access-control-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList, [], name, value)


                                    class Inbound(Entity):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound, self).__init__()

                                            self.yang_name = "inbound"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "inbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound, [u'entry'], name, value)


                                    class Outbound(Entity):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound, self).__init__()

                                            self.yang_name = "outbound"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "outbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound, [u'entry'], name, value)


                                    class Common(Entity):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common, self).__init__()

                                            self.yang_name = "common"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "common"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common, [u'entry'], name, value)


                                class Rpf(Entity):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\: bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('allow_default_route', (YLeaf(YType.boolean, 'allow-default-route'), ['bool'])),
                                            ('allow_self_ping', (YLeaf(YType.boolean, 'allow-self-ping'), ['bool'])),
                                            ('mode', (YLeaf(YType.uint32, 'mode'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.allow_default_route = None
                                        self.allow_self_ping = None
                                        self.mode = None
                                        self._segment_path = lambda: "rpf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, [u'enable', u'allow_default_route', u'allow_self_ping', u'mode'], name, value)


                                class BgpPa(Entity):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("input", ("input", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input)), ("output", ("output", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output))])
                                        self._leafs = OrderedDict()

                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"

                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._segment_path = lambda: "bgp-pa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa, [], name, value)


                                    class Input(Entity):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.uint32, 'enable'), ['int'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "input"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, [u'enable', u'source', u'destination'], name, value)


                                    class Output(Entity):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.uint32, 'enable'), ['int'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "output"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, [u'enable', u'source', u'destination'], name, value)


                                class Utime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime, self).__init__()

                                        self.yang_name = "utime"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "utime"
                                        self._is_frozen = True


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "idb-utime"
                                        self._is_frozen = True


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "caps-utime"
                                        self._is_frozen = True


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-en-utime"
                                        self._is_frozen = True


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-dis-utime"
                                        self._is_frozen = True


                                class MulticastGroup(Entity):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "multicast-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, [u'address'], name, value)


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class ClientMulticastGroup(Entity):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, self).__init__()

                                        self.yang_name = "client-multicast-group"
                                        self.yang_parent_name = "global-detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "client-multicast-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, [u'address'], name, value)


                        class GlobalBriefs(Entity):
                            """
                            Brief interface IPv6 network operational
                            data from global data
                            
                            .. attribute:: global_brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`GlobalBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2017-08-09'

                            def __init__(self):
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs, self).__init__()

                                self.yang_name = "global-briefs"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("global-brief", ("global_brief", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief))])
                                self._leafs = OrderedDict()

                                self.global_brief = YList(self)
                                self._segment_path = lambda: "global-briefs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs, [], name, value)


                            class GlobalBrief(Entity):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2017-08-09'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, self).__init__()

                                    self.yang_name = "global-brief"
                                    self.yang_parent_name = "global-briefs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.vrf_name = None

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"

                                    self.address = YList(self)
                                    self._segment_path = lambda: "global-brief" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, ['interface_name', u'line_state', u'vrf_name'], name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "global-brief"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "global-brief"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                        class Details(Entity):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2017-08-09'

                            def __init__(self):
                                super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail))])
                                self._leafs = OrderedDict()

                                self.detail = YList(self)
                                self._segment_path = lambda: "details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, [], name, value)


                            class Detail(Entity):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress>`
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:  :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList>`
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:  :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList>`
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                .. attribute:: utime
                                
                                	Address Publish Time
                                	**type**\:  :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:  :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:  :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:  :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime>`
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:  :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime>`
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:  :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\: bool
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\: bool
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\: bool
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address>`
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of  		 :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup>`
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2017-08-09'

                                def __init__(self):
                                    super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress)), ("access-control-list", ("access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList)), ("multi-access-control-list", ("multi_access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList)), ("rpf", ("rpf", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa)), ("utime", ("utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime)), ("idb-utime", ("idb_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime)), ("caps-utime", ("caps_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime)), ("fwd-en-utime", ("fwd_en_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime)), ("fwd-dis-utime", ("fwd_dis_utime", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime)), ("multicast-group", ("multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address)), ("client-multicast-group", ("client_multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                        ('operation_state', (YLeaf(YType.enumeration, 'operation-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperState', '')])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('is_icmp_unreach_enabled', (YLeaf(YType.boolean, 'is-icmp-unreach-enabled'), ['bool'])),
                                        ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                        ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                        ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                        ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.mtu = None
                                    self.operation_state = None
                                    self.vrf_name = None
                                    self.is_icmp_unreach_enabled = None
                                    self.rg_id_exists = None
                                    self.mlacp_active = None
                                    self.flow_tag_src = None
                                    self.flow_tag_dst = None

                                    self.link_local_address = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress()
                                    self.link_local_address.parent = self
                                    self._children_name_map["link_local_address"] = "link-local-address"

                                    self.access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList()
                                    self.access_control_list.parent = self
                                    self._children_name_map["access_control_list"] = "access-control-list"

                                    self.multi_access_control_list = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList()
                                    self.multi_access_control_list.parent = self
                                    self._children_name_map["multi_access_control_list"] = "multi-access-control-list"

                                    self.rpf = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"

                                    self.bgp_pa = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"

                                    self.utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime()
                                    self.utime.parent = self
                                    self._children_name_map["utime"] = "utime"

                                    self.idb_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"

                                    self.caps_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"

                                    self.fwd_en_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"

                                    self.fwd_dis_utime = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"

                                    self.multicast_group = YList(self)
                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self._segment_path = lambda: "detail" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, ['interface_name', u'line_state', u'mtu', u'operation_state', u'vrf_name', u'is_icmp_unreach_enabled', u'rg_id_exists', u'mlacp_active', u'flow_tag_src', u'flow_tag_dst'], name, value)


                                class LinkLocalAddress(Entity):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, self).__init__()

                                        self.yang_name = "link-local-address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class AccessControlList(Entity):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, self).__init__()

                                        self.yang_name = "access-control-list"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_bound', (YLeaf(YType.str, 'in-bound'), ['str'])),
                                            ('out_bound', (YLeaf(YType.str, 'out-bound'), ['str'])),
                                            ('common_in_bound', (YLeaf(YType.str, 'common-in-bound'), ['str'])),
                                            ('common_out_bound', (YLeaf(YType.str, 'common-out-bound'), ['str'])),
                                        ])
                                        self.in_bound = None
                                        self.out_bound = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self._segment_path = lambda: "access-control-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, [u'in_bound', u'out_bound', u'common_in_bound', u'common_out_bound'], name, value)


                                class MultiAccessControlList(Entity):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound>`
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound>`
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList, self).__init__()

                                        self.yang_name = "multi-access-control-list"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("inbound", ("inbound", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound)), ("outbound", ("outbound", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound)), ("common", ("common", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common))])
                                        self._leafs = OrderedDict()

                                        self.inbound = YList(self)
                                        self.outbound = YList(self)
                                        self.common = YList(self)
                                        self._segment_path = lambda: "multi-access-control-list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList, [], name, value)


                                    class Inbound(Entity):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound, self).__init__()

                                            self.yang_name = "inbound"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "inbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound, [u'entry'], name, value)


                                    class Outbound(Entity):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound, self).__init__()

                                            self.yang_name = "outbound"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "outbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound, [u'entry'], name, value)


                                    class Common(Entity):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common, self).__init__()

                                            self.yang_name = "common"
                                            self.yang_parent_name = "multi-access-control-list"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "common"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common, [u'entry'], name, value)


                                class Rpf(Entity):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\: bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('allow_default_route', (YLeaf(YType.boolean, 'allow-default-route'), ['bool'])),
                                            ('allow_self_ping', (YLeaf(YType.boolean, 'allow-self-ping'), ['bool'])),
                                            ('mode', (YLeaf(YType.uint32, 'mode'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.allow_default_route = None
                                        self.allow_self_ping = None
                                        self.mode = None
                                        self._segment_path = lambda: "rpf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, [u'enable', u'allow_default_route', u'allow_self_ping', u'mode'], name, value)


                                class BgpPa(Entity):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("input", ("input", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input)), ("output", ("output", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output))])
                                        self._leafs = OrderedDict()

                                        self.input = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"

                                        self.output = Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._segment_path = lambda: "bgp-pa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, [], name, value)


                                    class Input(Entity):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.uint32, 'enable'), ['int'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "input"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, [u'enable', u'source', u'destination'], name, value)


                                    class Output(Entity):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2017-08-09'

                                        def __init__(self):
                                            super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.uint32, 'enable'), ['int'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "output"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, [u'enable', u'source', u'destination'], name, value)


                                class Utime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime, self).__init__()

                                        self.yang_name = "utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "utime"
                                        self._is_frozen = True


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "idb-utime"
                                        self._is_frozen = True


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "caps-utime"
                                        self._is_frozen = True


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-en-utime"
                                        self._is_frozen = True


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-dis-utime"
                                        self._is_frozen = True


                                class MulticastGroup(Entity):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "multicast-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, [u'address'], name, value)


                                class Address(Entity):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('address_state', (YLeaf(YType.enumeration, 'address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrState', '')])),
                                            ('is_anycast', (YLeaf(YType.boolean, 'is-anycast'), ['bool'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, [u'address', u'prefix_length', u'address_state', u'is_anycast', u'route_tag'], name, value)


                                class ClientMulticastGroup(Entity):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2017-08-09'

                                    def __init__(self):
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, self).__init__()

                                        self.yang_name = "client-multicast-group"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "client-multicast-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, [u'address'], name, value)


                class Summary(Entity):
                    """
                    Summary of IPv6 network operational interface
                    data on a node
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:  :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:  :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:  :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:  :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2017-08-09'

                    def __init__(self):
                        super(Ipv6Network.Nodes.Node.InterfaceData.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("if-up-up", ("if_up_up", Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp)), ("if-up-down", ("if_up_down", Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown)), ("if-down-down", ("if_down_down", Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown)), ("if-shutdown-down", ("if_shutdown_down", Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown))])
                        self._leafs = OrderedDict([
                            ('if_up_down_basecaps_up', (YLeaf(YType.uint32, 'if-up-down-basecaps-up'), ['int'])),
                        ])
                        self.if_up_down_basecaps_up = None

                        self.if_up_up = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self
                        self._children_name_map["if_up_up"] = "if-up-up"

                        self.if_up_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self._children_name_map["if_up_down"] = "if-up-down"

                        self.if_down_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self._children_name_map["if_down_down"] = "if-down-down"

                        self.if_shutdown_down = Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary, [u'if_up_down_basecaps_up'], name, value)


                    class IfUpUp(Entity):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2017-08-09'

                        def __init__(self):
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__init__()

                            self.yang_name = "if-up-up"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-up-up"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfUpDown(Entity):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2017-08-09'

                        def __init__(self):
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__init__()

                            self.yang_name = "if-up-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-up-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfDownDown(Entity):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2017-08-09'

                        def __init__(self):
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__init__()

                            self.yang_name = "if-down-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-down-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfShutdownDown(Entity):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2017-08-09'

                        def __init__(self):
                            super(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__init__()

                            self.yang_name = "if-shutdown-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-shutdown-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Network()
        return self._top_entity

