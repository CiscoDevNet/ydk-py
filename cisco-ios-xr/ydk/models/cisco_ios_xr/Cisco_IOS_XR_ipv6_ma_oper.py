""" Cisco_IOS_XR_ipv6_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-ma package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-network\: IPv6 network operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaIfAddrState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaIfLineState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6MaOperState']



class Ipv6Network(_Entity_):
    """
    IPv6 network operational data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 network operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv6-ma-oper'
    _revision = '2018-08-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Nodes(_Entity_):
        """
        Node\-specific IPv6 network operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv6-ma-oper'
        _revision = '2018-08-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Node(_Entity_):
            """
            IPv6 network operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: interface_data
            
            	IPv6 network operational interface data
            	**type**\:  :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv6-ma-oper'
            _revision = '2018-08-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class InterfaceData(_Entity_):
                """
                IPv6 network operational interface data
                
                .. attribute:: vrfs
                
                	VRF specific IPv6 network operational interface data
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs>`
                
                	**config**\: False
                
                .. attribute:: summary
                
                	Summary of IPv6 network operational interface data on a node
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-ma-oper'
                _revision = '2018-08-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Vrfs(_Entity_):
                    """
                    VRF specific IPv6 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF ID of an interface belong to
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2018-08-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Vrf(_Entity_):
                        """
                        VRF ID of an interface belong to
                        
                        .. attribute:: vrf_name  (key)
                        
                        	The VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv6 network operational data for a node
                        	**type**\:  :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        	**config**\: False
                        
                        .. attribute:: global_details
                        
                        	Detail interface IPv4 network operational data for global data
                        	**type**\:  :py:class:`GlobalDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails>`
                        
                        	**config**\: False
                        
                        .. attribute:: global_briefs
                        
                        	Brief interface IPv6 network operational data from global data
                        	**type**\:  :py:class:`GlobalBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs>`
                        
                        	**config**\: False
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2018-08-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Briefs(_Entity_):
                            """
                            Brief interface IPv6 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2018-08-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Brief(_Entity_):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                	**config**\: False
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2018-08-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, ['interface_name', 'line_state', 'vrf_name'], name, value)


                                class LinkLocalAddress(_Entity_):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress']['meta_info']


                                class Address(_Entity_):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info']


                        class GlobalDetails(_Entity_):
                            """
                            Detail interface IPv4 network operational
                            data for global data
                            
                            .. attribute:: global_detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`GlobalDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2018-08-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class GlobalDetail(_Entity_):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:  :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList>`
                                
                                	**config**\: False
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:  :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList>`
                                
                                	**config**\: False
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf>`
                                
                                	**config**\: False
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa>`
                                
                                	**config**\: False
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                	**config**\: False
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:  :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6_config_flag
                                
                                	Interface Configured Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6_oper_flag
                                
                                	Interface Operational Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                	**config**\: False
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: idb_pointer
                                
                                	idb pointer value
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup>`
                                
                                	**config**\: False
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address>`
                                
                                	**config**\: False
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of  		 :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2018-08-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, self).__init__()

                                    self.yang_name = "global-detail"
                                    self.yang_parent_name = "global-details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress)), ("access-control-list", ("access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList)), ("multi-access-control-list", ("multi_access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList)), ("rpf", ("rpf", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa)), ("multicast-group", ("multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address)), ("client-multicast-group", ("client_multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                        ('operation_state', (YLeaf(YType.enumeration, 'operation-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperState', '')])),
                                        ('ipv6_config_flag', (YLeaf(YType.uint32, 'ipv6-config-flag'), ['int'])),
                                        ('ipv6_oper_flag', (YLeaf(YType.uint32, 'ipv6-oper-flag'), ['int'])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('is_icmp_unreach_enabled', (YLeaf(YType.boolean, 'is-icmp-unreach-enabled'), ['bool'])),
                                        ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                        ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                        ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                        ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                        ('idb_pointer', (YLeaf(YType.uint64, 'idb-pointer'), ['int'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.mtu = None
                                    self.operation_state = None
                                    self.ipv6_config_flag = None
                                    self.ipv6_oper_flag = None
                                    self.vrf_name = None
                                    self.is_icmp_unreach_enabled = None
                                    self.rg_id_exists = None
                                    self.mlacp_active = None
                                    self.flow_tag_src = None
                                    self.flow_tag_dst = None
                                    self.idb_pointer = None

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

                                    self.multicast_group = YList(self)
                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self._segment_path = lambda: "global-detail" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail, ['interface_name', 'line_state', 'mtu', 'operation_state', 'ipv6_config_flag', 'ipv6_oper_flag', 'vrf_name', 'is_icmp_unreach_enabled', 'rg_id_exists', 'mlacp_active', 'flow_tag_src', 'flow_tag_dst', 'idb_pointer'], name, value)


                                class LinkLocalAddress(_Entity_):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress']['meta_info']


                                class AccessControlList(_Entity_):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList, ['in_bound', 'out_bound', 'common_in_bound', 'common_out_bound'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList']['meta_info']


                                class MultiAccessControlList(_Entity_):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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


                                    class Inbound(_Entity_):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Inbound ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Inbound']['meta_info']


                                    class Outbound(_Entity_):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Outbound ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Outbound']['meta_info']


                                    class Common(_Entity_):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Common ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList.Common']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList']['meta_info']


                                class Rpf(_Entity_):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf, ['enable', 'allow_default_route', 'allow_self_ping', 'mode'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf']['meta_info']


                                class BgpPa(_Entity_):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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


                                    class Input(_Entity_):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input, ['enable', 'source', 'destination'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input']['meta_info']


                                    class Output(_Entity_):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output, ['enable', 'source', 'destination'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa']['meta_info']


                                class MulticastGroup(_Entity_):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup, ['address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup']['meta_info']


                                class Address(_Entity_):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address']['meta_info']


                                class ClientMulticastGroup(_Entity_):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup, ['address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails']['meta_info']


                        class GlobalBriefs(_Entity_):
                            """
                            Brief interface IPv6 network operational
                            data from global data
                            
                            .. attribute:: global_brief
                            
                            	Brief interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`GlobalBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2018-08-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class GlobalBrief(_Entity_):
                                """
                                Brief interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                	**config**\: False
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2018-08-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief, ['interface_name', 'line_state', 'vrf_name'], name, value)


                                class LinkLocalAddress(_Entity_):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress']['meta_info']


                                class Address(_Entity_):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs']['meta_info']


                        class Details(_Entity_):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv6 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-ma-oper'
                            _revision = '2018-08-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Detail(_Entity_):
                                """
                                Detail interface IPv6 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: link_local_address
                                
                                	Link Local Address
                                	**type**\:  :py:class:`LinkLocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress>`
                                
                                	**config**\: False
                                
                                .. attribute:: access_control_list
                                
                                	IPv6 Access Control List
                                	**type**\:  :py:class:`AccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList>`
                                
                                	**config**\: False
                                
                                .. attribute:: multi_access_control_list
                                
                                	Multi IPv6 Access Control List
                                	**type**\:  :py:class:`MultiAccessControlList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList>`
                                
                                	**config**\: False
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                	**config**\: False
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                	**config**\: False
                                
                                .. attribute:: line_state
                                
                                	State of Interface Line
                                	**type**\:  :py:class:`Ipv6MaIfLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfLineState>`
                                
                                	**config**\: False
                                
                                .. attribute:: mtu
                                
                                	IPv6 MTU
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: operation_state
                                
                                	IPv6 Operation State
                                	**type**\:  :py:class:`Ipv6MaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaOperState>`
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6_config_flag
                                
                                	Interface Configured Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6_oper_flag
                                
                                	Interface Operational Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_name
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**length:** 0..32
                                
                                	**config**\: False
                                
                                .. attribute:: is_icmp_unreach_enabled
                                
                                	ICMP unreach Enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: idb_pointer
                                
                                	idb pointer value
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: multicast_group
                                
                                	IPv6 Multicast Group
                                	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                	**config**\: False
                                
                                .. attribute:: address
                                
                                	Address List
                                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address>`
                                
                                	**config**\: False
                                
                                .. attribute:: client_multicast_group
                                
                                	IPv6 Client Multicast Group
                                	**type**\: list of  		 :py:class:`ClientMulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv6-ma-oper'
                                _revision = '2018-08-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("link-local-address", ("link_local_address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress)), ("access-control-list", ("access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList)), ("multi-access-control-list", ("multi_access_control_list", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList)), ("rpf", ("rpf", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa)), ("multicast-group", ("multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup)), ("address", ("address", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address)), ("client-multicast-group", ("client_multicast_group", Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineState', '')])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                        ('operation_state', (YLeaf(YType.enumeration, 'operation-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperState', '')])),
                                        ('ipv6_config_flag', (YLeaf(YType.uint32, 'ipv6-config-flag'), ['int'])),
                                        ('ipv6_oper_flag', (YLeaf(YType.uint32, 'ipv6-oper-flag'), ['int'])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('is_icmp_unreach_enabled', (YLeaf(YType.boolean, 'is-icmp-unreach-enabled'), ['bool'])),
                                        ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                        ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                        ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                        ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                        ('idb_pointer', (YLeaf(YType.uint64, 'idb-pointer'), ['int'])),
                                    ])
                                    self.interface_name = None
                                    self.line_state = None
                                    self.mtu = None
                                    self.operation_state = None
                                    self.ipv6_config_flag = None
                                    self.ipv6_oper_flag = None
                                    self.vrf_name = None
                                    self.is_icmp_unreach_enabled = None
                                    self.rg_id_exists = None
                                    self.mlacp_active = None
                                    self.flow_tag_src = None
                                    self.flow_tag_dst = None
                                    self.idb_pointer = None

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

                                    self.multicast_group = YList(self)
                                    self.address = YList(self)
                                    self.client_multicast_group = YList(self)
                                    self._segment_path = lambda: "detail" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, ['interface_name', 'line_state', 'mtu', 'operation_state', 'ipv6_config_flag', 'ipv6_oper_flag', 'vrf_name', 'is_icmp_unreach_enabled', 'rg_id_exists', 'mlacp_active', 'flow_tag_src', 'flow_tag_dst', 'idb_pointer'], name, value)


                                class LinkLocalAddress(_Entity_):
                                    """
                                    Link Local Address
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "link-local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress']['meta_info']


                                class AccessControlList(_Entity_):
                                    """
                                    IPv6 Access Control List
                                    
                                    .. attribute:: in_bound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: out_bound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList, ['in_bound', 'out_bound', 'common_in_bound', 'common_out_bound'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList']['meta_info']


                                class MultiAccessControlList(_Entity_):
                                    """
                                    Multi IPv6 Access Control List
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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


                                    class Inbound(_Entity_):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Inbound ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Inbound']['meta_info']


                                    class Outbound(_Entity_):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Outbound ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Outbound']['meta_info']


                                    class Common(_Entity_):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	Common ACLs
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common, ['entry'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList.Common']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList']['meta_info']


                                class Rpf(_Entity_):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, ['enable', 'allow_default_route', 'allow_self_ping', 'mode'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf']['meta_info']


                                class BgpPa(_Entity_):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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


                                    class Input(_Entity_):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, ['enable', 'source', 'destination'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input']['meta_info']


                                    class Output(_Entity_):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv6-ma-oper'
                                        _revision = '2018-08-01'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
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
                                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, ['enable', 'source', 'destination'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']


                                class MulticastGroup(_Entity_):
                                    """
                                    IPv6 Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, ['address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup']['meta_info']


                                class Address(_Entity_):
                                    """
                                    Address List
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix Length of IPv6 Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address_state
                                    
                                    	State of Address
                                    	**type**\:  :py:class:`Ipv6MaIfAddrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6MaIfAddrState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_anycast
                                    
                                    	Anycast address
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route\-tag of the Address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: arm_flags
                                    
                                    	Bitmap for ARM flags
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                            ('arm_flags', (YLeaf(YType.uint32, 'arm-flags'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.address_state = None
                                        self.is_anycast = None
                                        self.route_tag = None
                                        self.arm_flags = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address, ['address', 'prefix_length', 'address_state', 'is_anycast', 'route_tag', 'arm_flags'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address']['meta_info']


                                class ClientMulticastGroup(_Entity_):
                                    """
                                    IPv6 Client Multicast Group
                                    
                                    .. attribute:: address
                                    
                                    	IPv6 Address of Multicast Group
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv6-ma-oper'
                                    _revision = '2018-08-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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
                                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup, ['address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                                return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs']['meta_info']


                class Summary(_Entity_):
                    """
                    Summary of IPv6 network operational interface
                    data on a node
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:  :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    	**config**\: False
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:  :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    	**config**\: False
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:  :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    	**config**\: False
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:  :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper.Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    	**config**\: False
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-ma-oper'
                    _revision = '2018-08-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary, ['if_up_down_basecaps_up'], name, value)


                    class IfUpUp(_Entity_):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2018-08-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp, ['ip_assigned', 'ip_unnumbered', 'ip_unassigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp']['meta_info']


                    class IfUpDown(_Entity_):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2018-08-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown, ['ip_assigned', 'ip_unnumbered', 'ip_unassigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown']['meta_info']


                    class IfDownDown(_Entity_):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2018-08-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown, ['ip_assigned', 'ip_unnumbered', 'ip_unassigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown']['meta_info']


                    class IfShutdownDown(_Entity_):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces without explicit address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-ma-oper'
                        _revision = '2018-08-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, ['ip_assigned', 'ip_unnumbered', 'ip_unassigned'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                            return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                        return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                    return meta._meta_table['Ipv6Network.Nodes.Node.InterfaceData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
                return meta._meta_table['Ipv6Network.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
            return meta._meta_table['Ipv6Network.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ipv6Network()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ma_oper as meta
        return meta._meta_table['Ipv6Network']['meta_info']


