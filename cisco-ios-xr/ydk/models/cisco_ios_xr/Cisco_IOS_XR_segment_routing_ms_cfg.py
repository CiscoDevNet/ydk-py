""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SidTypeList(Enum):
    """
    SidTypeList (Enum Class)

    Sid type list

    .. data:: absolute = 1

    	Absolute SID

    .. data:: index = 2

    	Index SID

    """

    absolute = Enum.YLeaf(1, "absolute")

    index = Enum.YLeaf(2, "index")


class SrmsAddressFamily(Enum):
    """
    SrmsAddressFamily (Enum Class)

    Srms address family

    .. data:: ipv4 = 1

    	IP version 4

    .. data:: ipv6 = 2

    	IP version 6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class SrmsMiFlag(Enum):
    """
    SrmsMiFlag (Enum Class)

    Srms mi flag

    .. data:: disable = 0

    	Disable flag

    .. data:: enable = 1

    	Enable flag

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Sr(Entity):
    """
    Segment Routing
    
    .. attribute:: local_block
    
    	Segment Routing Local Block of Labels
    	**type**\:  :py:class:`LocalBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.LocalBlock>`
    
    	**presence node**\: True
    
    .. attribute:: mappings
    
    	Mapping Server
    	**type**\:  :py:class:`Mappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings>`
    
    .. attribute:: adjacency_sid
    
    	Segment Routing Adjacency SID
    	**type**\:  :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid>`
    
    .. attribute:: global_block
    
    	Global Block Segment Routing
    	**type**\:  :py:class:`GlobalBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.GlobalBlock>`
    
    	**presence node**\: True
    
    .. attribute:: enable
    
    	enable SR
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: traffic_engineering
    
    	Traffic Engineering configuration data
    	**type**\:  :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering>`
    
    

    """

    _prefix = 'segment-routing-ms-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sr, self).__init__()
        self._top_entity = None

        self.yang_name = "sr"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("local-block", ("local_block", Sr.LocalBlock)), ("mappings", ("mappings", Sr.Mappings)), ("adjacency-sid", ("adjacency_sid", Sr.AdjacencySid)), ("global-block", ("global_block", Sr.GlobalBlock)), ("Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering", ("traffic_engineering", Sr.TrafficEngineering))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('enable', YLeaf(YType.empty, 'enable')),
        ])
        self.enable = None

        self.local_block = None
        self._children_name_map["local_block"] = "local-block"
        self._children_yang_names.add("local-block")

        self.mappings = Sr.Mappings()
        self.mappings.parent = self
        self._children_name_map["mappings"] = "mappings"
        self._children_yang_names.add("mappings")

        self.adjacency_sid = Sr.AdjacencySid()
        self.adjacency_sid.parent = self
        self._children_name_map["adjacency_sid"] = "adjacency-sid"
        self._children_yang_names.add("adjacency-sid")

        self.global_block = None
        self._children_name_map["global_block"] = "global-block"
        self._children_yang_names.add("global-block")

        self.traffic_engineering = Sr.TrafficEngineering()
        self.traffic_engineering.parent = self
        self._children_name_map["traffic_engineering"] = "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering"
        self._children_yang_names.add("Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering")
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr"

    def __setattr__(self, name, value):
        self._perform_setattr(Sr, ['enable'], name, value)


    class LocalBlock(Entity):
        """
        Segment Routing Local Block of Labels
        
        .. attribute:: lower_bound
        
        	SRLB Lower Bound
        	**type**\: int
        
        	**range:** 15000..1048574
        
        	**mandatory**\: True
        
        .. attribute:: upper_bound
        
        	SRLB Upper Bound
        	**type**\: int
        
        	**range:** 15001..1048575
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.LocalBlock, self).__init__()

            self.yang_name = "local-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('lower_bound', YLeaf(YType.uint32, 'lower-bound')),
                ('upper_bound', YLeaf(YType.uint32, 'upper-bound')),
            ])
            self.lower_bound = None
            self.upper_bound = None
            self._segment_path = lambda: "local-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.LocalBlock, ['lower_bound', 'upper_bound'], name, value)


    class Mappings(Entity):
        """
        Mapping Server
        
        .. attribute:: mapping
        
        	IP prefix to SID mapping
        	**type**\: list of  		 :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings.Mapping>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.Mappings, self).__init__()

            self.yang_name = "mappings"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mapping", ("mapping", Sr.Mappings.Mapping))])
            self._leafs = OrderedDict()

            self.mapping = YList(self)
            self._segment_path = lambda: "mappings"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.Mappings, [], name, value)


        class Mapping(Entity):
            """
            IP prefix to SID mapping
            
            .. attribute:: af  (key)
            
            	Address Family
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ip  (key)
            
            	IP prefix
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: mask  (key)
            
            	Mask
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sid_start
            
            	Start of SID index range
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: sid_range
            
            	Range (number of SIDs)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: flag_attached
            
            	Enable/Disable Attached flag
            	**type**\:  :py:class:`SrmsMiFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsMiFlag>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.Mappings.Mapping, self).__init__()

                self.yang_name = "mapping"
                self.yang_parent_name = "mappings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af','ip','mask']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('af', YLeaf(YType.str, 'af')),
                    ('ip', YLeaf(YType.str, 'ip')),
                    ('mask', YLeaf(YType.int32, 'mask')),
                    ('sid_start', YLeaf(YType.uint32, 'sid-start')),
                    ('sid_range', YLeaf(YType.int32, 'sid-range')),
                    ('flag_attached', YLeaf(YType.enumeration, 'flag-attached')),
                ])
                self.af = None
                self.ip = None
                self.mask = None
                self.sid_start = None
                self.sid_range = None
                self.flag_attached = None
                self._segment_path = lambda: "mapping" + "[af='" + str(self.af) + "']" + "[ip='" + str(self.ip) + "']" + "[mask='" + str(self.mask) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/mappings/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.Mappings.Mapping, ['af', 'ip', 'mask', 'sid_start', 'sid_range', 'flag_attached'], name, value)


    class AdjacencySid(Entity):
        """
        Segment Routing Adjacency SID
        
        .. attribute:: interfaces
        
        	Segment Routing Adjacency SID Interface Table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.AdjacencySid, self).__init__()

            self.yang_name = "adjacency-sid"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("interfaces", ("interfaces", Sr.AdjacencySid.Interfaces))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.interfaces = Sr.AdjacencySid.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "adjacency-sid"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()


        class Interfaces(Entity):
            """
            Segment Routing Adjacency SID Interface Table
            
            .. attribute:: interface
            
            	Segment Routing Adjacency SID Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.AdjacencySid.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "adjacency-sid"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", Sr.AdjacencySid.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/adjacency-sid/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.AdjacencySid.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Segment Routing Adjacency SID Interface
                
                .. attribute:: interface  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: address_families
                
                	Segment Routing Adjacency SID Interface Address Family Table
                	**type**\:  :py:class:`AddressFamilies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies>`
                
                

                """

                _prefix = 'segment-routing-ms-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sr.AdjacencySid.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface']
                    self._child_container_classes = OrderedDict([("address-families", ("address_families", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', YLeaf(YType.str, 'interface')),
                    ])
                    self.interface = None

                    self.address_families = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies()
                    self.address_families.parent = self
                    self._children_name_map["address_families"] = "address-families"
                    self._children_yang_names.add("address-families")
                    self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/adjacency-sid/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface, ['interface'], name, value)


                class AddressFamilies(Entity):
                    """
                    Segment Routing Adjacency SID Interface
                    Address Family Table
                    
                    .. attribute:: address_family
                    
                    	Segment Routing Adjacency SID Interface Address Family
                    	**type**\: list of  		 :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies, self).__init__()

                        self.yang_name = "address-families"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("address-family", ("address_family", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily))])
                        self._leafs = OrderedDict()

                        self.address_family = YList(self)
                        self._segment_path = lambda: "address-families"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies, [], name, value)


                    class AddressFamily(Entity):
                        """
                        Segment Routing Adjacency SID Interface
                        Address Family
                        
                        .. attribute:: address_family  (key)
                        
                        	Address Family
                        	**type**\:  :py:class:`SrmsAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsAddressFamily>`
                        
                        .. attribute:: next_hops
                        
                        	Segment Routing Adjacency SID Interface Address Family NextHop Table
                        	**type**\:  :py:class:`NextHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops>`
                        
                        

                        """

                        _prefix = 'segment-routing-ms-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily, self).__init__()

                            self.yang_name = "address-family"
                            self.yang_parent_name = "address-families"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address_family']
                            self._child_container_classes = OrderedDict([("next-hops", ("next_hops", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_family', YLeaf(YType.enumeration, 'address-family')),
                            ])
                            self.address_family = None

                            self.next_hops = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops()
                            self.next_hops.parent = self
                            self._children_name_map["next_hops"] = "next-hops"
                            self._children_yang_names.add("next-hops")
                            self._segment_path = lambda: "address-family" + "[address-family='" + str(self.address_family) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily, ['address_family'], name, value)


                        class NextHops(Entity):
                            """
                            Segment Routing Adjacency SID Interface
                            Address Family NextHop Table
                            
                            .. attribute:: next_hop
                            
                            	Segment Routing Adjacency SID Interface Address Family NextHop, use a single ANYADDR (0.0.0.0 or \:\:) NextHop for point to point links
                            	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop>`
                            
                            

                            """

                            _prefix = 'segment-routing-ms-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops, self).__init__()

                                self.yang_name = "next-hops"
                                self.yang_parent_name = "address-family"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("next-hop", ("next_hop", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop))])
                                self._leafs = OrderedDict()

                                self.next_hop = YList(self)
                                self._segment_path = lambda: "next-hops"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops, [], name, value)


                            class NextHop(Entity):
                                """
                                Segment Routing Adjacency SID Interface
                                Address Family NextHop, use a single
                                ANYADDR (0.0.0.0 or \:\:) NextHop for point
                                to point links
                                
                                .. attribute:: ip_addr  (key)
                                
                                	NextHop IP address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: l2_adjacency_sid
                                
                                	L2 Adjacency SID type and value
                                	**type**\:  :py:class:`L2AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid>`
                                
                                

                                """

                                _prefix = 'segment-routing-ms-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "next-hops"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['ip_addr']
                                    self._child_container_classes = OrderedDict([("l2-adjacency-sid", ("l2_adjacency_sid", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                                    ])
                                    self.ip_addr = None

                                    self.l2_adjacency_sid = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid()
                                    self.l2_adjacency_sid.parent = self
                                    self._children_name_map["l2_adjacency_sid"] = "l2-adjacency-sid"
                                    self._children_yang_names.add("l2-adjacency-sid")
                                    self._segment_path = lambda: "next-hop" + "[ip-addr='" + str(self.ip_addr) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop, ['ip_addr'], name, value)


                                class L2AdjacencySid(Entity):
                                    """
                                    L2 Adjacency SID type and value
                                    
                                    .. attribute:: sid_type
                                    
                                    	SID type
                                    	**type**\:  :py:class:`SidTypeList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SidTypeList>`
                                    
                                    .. attribute:: absolute_sid
                                    
                                    	SID value
                                    	**type**\: int
                                    
                                    	**range:** 15000..1048575
                                    
                                    .. attribute:: index_sid
                                    
                                    	SID value
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    .. attribute:: srlb
                                    
                                    	SRLB block name
                                    	**type**\: str
                                    
                                    	**pattern:** (srlb\_default)
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-ms-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid, self).__init__()

                                        self.yang_name = "l2-adjacency-sid"
                                        self.yang_parent_name = "next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sid_type', YLeaf(YType.enumeration, 'sid-type')),
                                            ('absolute_sid', YLeaf(YType.uint32, 'absolute-sid')),
                                            ('index_sid', YLeaf(YType.uint32, 'index-sid')),
                                            ('srlb', YLeaf(YType.str, 'srlb')),
                                        ])
                                        self.sid_type = None
                                        self.absolute_sid = None
                                        self.index_sid = None
                                        self.srlb = None
                                        self._segment_path = lambda: "l2-adjacency-sid"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid, ['sid_type', 'absolute_sid', 'index_sid', 'srlb'], name, value)


    class GlobalBlock(Entity):
        """
        Global Block Segment Routing
        
        .. attribute:: lower_bound
        
        	SRGB Lower Bound
        	**type**\: int
        
        	**range:** 16000..1048574
        
        	**mandatory**\: True
        
        .. attribute:: upper_bound
        
        	SRGB Upper Bound
        	**type**\: int
        
        	**range:** 16001..1048575
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.GlobalBlock, self).__init__()

            self.yang_name = "global-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('lower_bound', YLeaf(YType.uint32, 'lower-bound')),
                ('upper_bound', YLeaf(YType.uint32, 'upper-bound')),
            ])
            self.lower_bound = None
            self.upper_bound = None
            self._segment_path = lambda: "global-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.GlobalBlock, ['lower_bound', 'upper_bound'], name, value)


    class TrafficEngineering(Entity):
        """
        Traffic Engineering configuration data
        
        .. attribute:: on_demand_colors
        
        	On\-demand color configuration
        	**type**\:  :py:class:`OnDemandColors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors>`
        
        .. attribute:: segments
        
        	Segment\-lists configuration
        	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments>`
        
        .. attribute:: logging
        
        	Logging configuration
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Logging>`
        
        .. attribute:: binding_sid_rules
        
        	Binding sid rules
        	**type**\:  :py:class:`BindingSidRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.BindingSidRules>`
        
        .. attribute:: policies
        
        	Policy configuration
        	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies>`
        
        .. attribute:: srte_interfaces
        
        	SR\-TE interfaces
        	**type**\:  :py:class:`SrteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces>`
        
        .. attribute:: pcc
        
        	Path Computation Client
        	**type**\:  :py:class:`Pcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc>`
        
        .. attribute:: affinity_maps
        
        	Affinity\-map configuration
        	**type**\:  :py:class:`AffinityMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.AffinityMaps>`
        
        .. attribute:: enable
        
        	True only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-agent-cfg'
        _revision = '2017-09-11'

        def __init__(self):
            super(Sr.TrafficEngineering, self).__init__()

            self.yang_name = "traffic-engineering"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("on-demand-colors", ("on_demand_colors", Sr.TrafficEngineering.OnDemandColors)), ("segments", ("segments", Sr.TrafficEngineering.Segments)), ("logging", ("logging", Sr.TrafficEngineering.Logging)), ("binding-sid-rules", ("binding_sid_rules", Sr.TrafficEngineering.BindingSidRules)), ("policies", ("policies", Sr.TrafficEngineering.Policies)), ("srte-interfaces", ("srte_interfaces", Sr.TrafficEngineering.SrteInterfaces)), ("pcc", ("pcc", Sr.TrafficEngineering.Pcc)), ("affinity-maps", ("affinity_maps", Sr.TrafficEngineering.AffinityMaps))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', YLeaf(YType.empty, 'enable')),
            ])
            self.enable = None

            self.on_demand_colors = Sr.TrafficEngineering.OnDemandColors()
            self.on_demand_colors.parent = self
            self._children_name_map["on_demand_colors"] = "on-demand-colors"
            self._children_yang_names.add("on-demand-colors")

            self.segments = Sr.TrafficEngineering.Segments()
            self.segments.parent = self
            self._children_name_map["segments"] = "segments"
            self._children_yang_names.add("segments")

            self.logging = Sr.TrafficEngineering.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"
            self._children_yang_names.add("logging")

            self.binding_sid_rules = Sr.TrafficEngineering.BindingSidRules()
            self.binding_sid_rules.parent = self
            self._children_name_map["binding_sid_rules"] = "binding-sid-rules"
            self._children_yang_names.add("binding-sid-rules")

            self.policies = Sr.TrafficEngineering.Policies()
            self.policies.parent = self
            self._children_name_map["policies"] = "policies"
            self._children_yang_names.add("policies")

            self.srte_interfaces = Sr.TrafficEngineering.SrteInterfaces()
            self.srte_interfaces.parent = self
            self._children_name_map["srte_interfaces"] = "srte-interfaces"
            self._children_yang_names.add("srte-interfaces")

            self.pcc = Sr.TrafficEngineering.Pcc()
            self.pcc.parent = self
            self._children_name_map["pcc"] = "pcc"
            self._children_yang_names.add("pcc")

            self.affinity_maps = Sr.TrafficEngineering.AffinityMaps()
            self.affinity_maps.parent = self
            self._children_name_map["affinity_maps"] = "affinity-maps"
            self._children_yang_names.add("affinity-maps")
            self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.TrafficEngineering, ['enable'], name, value)


        class OnDemandColors(Entity):
            """
            On\-demand color configuration
            
            .. attribute:: on_demand_color
            
            	On\-demand color configuration
            	**type**\: list of  		 :py:class:`OnDemandColor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.OnDemandColors, self).__init__()

                self.yang_name = "on-demand-colors"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("on-demand-color", ("on_demand_color", Sr.TrafficEngineering.OnDemandColors.OnDemandColor))])
                self._leafs = OrderedDict()

                self.on_demand_color = YList(self)
                self._segment_path = lambda: "on-demand-colors"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.OnDemandColors, [], name, value)


            class OnDemandColor(Entity):
                """
                On\-demand color configuration
                
                .. attribute:: color  (key)
                
                	Color
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: on_demand_color_dyn_mpls
                
                	Dynamic MPLS path properties
                	**type**\:  :py:class:`OnDemandColorDynMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls>`
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor, self).__init__()

                    self.yang_name = "on-demand-color"
                    self.yang_parent_name = "on-demand-colors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['color']
                    self._child_container_classes = OrderedDict([("on-demand-color-dyn-mpls", ("on_demand_color_dyn_mpls", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('color', YLeaf(YType.uint32, 'color')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.color = None
                    self.enable = None

                    self.on_demand_color_dyn_mpls = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls()
                    self.on_demand_color_dyn_mpls.parent = self
                    self._children_name_map["on_demand_color_dyn_mpls"] = "on-demand-color-dyn-mpls"
                    self._children_yang_names.add("on-demand-color-dyn-mpls")
                    self._segment_path = lambda: "on-demand-color" + "[color='" + str(self.color) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/on-demand-colors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor, ['color', 'enable'], name, value)


                class OnDemandColorDynMpls(Entity):
                    """
                    Dynamic MPLS path properties
                    
                    .. attribute:: on_demand_color_dyn_mpls_metric
                    
                    	Metric type
                    	**type**\:  :py:class:`OnDemandColorDynMplsMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric>`
                    
                    .. attribute:: on_demand_color_dyn_mpls_pce
                    
                    	Use Path Computation Element
                    	**type**\:  :py:class:`OnDemandColorDynMplsPce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce>`
                    
                    .. attribute:: disjoint_path
                    
                    	Disjoint path
                    	**type**\:  :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	Dynamic MPLS path properties submode Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls, self).__init__()

                        self.yang_name = "on-demand-color-dyn-mpls"
                        self.yang_parent_name = "on-demand-color"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("on-demand-color-dyn-mpls-metric", ("on_demand_color_dyn_mpls_metric", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric)), ("on-demand-color-dyn-mpls-pce", ("on_demand_color_dyn_mpls_pce", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce)), ("disjoint-path", ("disjoint_path", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                        ])
                        self.enable = None

                        self.on_demand_color_dyn_mpls_metric = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric()
                        self.on_demand_color_dyn_mpls_metric.parent = self
                        self._children_name_map["on_demand_color_dyn_mpls_metric"] = "on-demand-color-dyn-mpls-metric"
                        self._children_yang_names.add("on-demand-color-dyn-mpls-metric")

                        self.on_demand_color_dyn_mpls_pce = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce()
                        self.on_demand_color_dyn_mpls_pce.parent = self
                        self._children_name_map["on_demand_color_dyn_mpls_pce"] = "on-demand-color-dyn-mpls-pce"
                        self._children_yang_names.add("on-demand-color-dyn-mpls-pce")

                        self.disjoint_path = None
                        self._children_name_map["disjoint_path"] = "disjoint-path"
                        self._children_yang_names.add("disjoint-path")
                        self._segment_path = lambda: "on-demand-color-dyn-mpls"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls, ['enable'], name, value)


                    class OnDemandColorDynMplsMetric(Entity):
                        """
                        Metric type
                        
                        .. attribute:: metric_type
                        
                        	Metric Type
                        	**type**\:  :py:class:`XtcMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetric>`
                        
                        .. attribute:: enable
                        
                        	Metric submode Enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric, self).__init__()

                            self.yang_name = "on-demand-color-dyn-mpls-metric"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('metric_type', YLeaf(YType.enumeration, 'metric-type')),
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.metric_type = None
                            self.enable = None
                            self._segment_path = lambda: "on-demand-color-dyn-mpls-metric"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric, ['metric_type', 'enable'], name, value)


                    class OnDemandColorDynMplsPce(Entity):
                        """
                        Use Path Computation Element
                        
                        .. attribute:: enable
                        
                        	PCE submode Enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce, self).__init__()

                            self.yang_name = "on-demand-color-dyn-mpls-pce"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "on-demand-color-dyn-mpls-pce"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce, ['enable'], name, value)


                    class DisjointPath(Entity):
                        """
                        Disjoint path
                        
                        .. attribute:: group_id
                        
                        	Group ID
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        .. attribute:: disjointness_type
                        
                        	Disjointness Type
                        	**type**\:  :py:class:`XtcDisjointness <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcDisjointness>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: sub_id
                        
                        	Sub ID
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath, self).__init__()

                            self.yang_name = "disjoint-path"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('group_id', YLeaf(YType.uint32, 'group-id')),
                                ('disjointness_type', YLeaf(YType.enumeration, 'disjointness-type')),
                                ('sub_id', YLeaf(YType.uint32, 'sub-id')),
                            ])
                            self.group_id = None
                            self.disjointness_type = None
                            self.sub_id = None
                            self._segment_path = lambda: "disjoint-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath, ['group_id', 'disjointness_type', 'sub_id'], name, value)


        class Segments(Entity):
            """
            Segment\-lists configuration
            
            .. attribute:: segment
            
            	Segment\-list configuration
            	**type**\: list of  		 :py:class:`Segment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments.Segment>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.Segments, self).__init__()

                self.yang_name = "segments"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("segment", ("segment", Sr.TrafficEngineering.Segments.Segment))])
                self._leafs = OrderedDict()

                self.segment = YList(self)
                self._segment_path = lambda: "segments"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Segments, [], name, value)


            class Segment(Entity):
                """
                Segment\-list configuration
                
                .. attribute:: path_name  (key)
                
                	Segment\-list name
                	**type**\: str
                
                	**length:** 1..128
                
                .. attribute:: segments
                
                	Segments/hops configuration for given Segment\-list
                	**type**\:  :py:class:`Segments_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments.Segment.Segments_>`
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.Segments.Segment, self).__init__()

                    self.yang_name = "segment"
                    self.yang_parent_name = "segments"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['path_name']
                    self._child_container_classes = OrderedDict([("segments", ("segments", Sr.TrafficEngineering.Segments.Segment.Segments_))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('path_name', YLeaf(YType.str, 'path-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.path_name = None
                    self.enable = None

                    self.segments = Sr.TrafficEngineering.Segments.Segment.Segments_()
                    self.segments.parent = self
                    self._children_name_map["segments"] = "segments"
                    self._children_yang_names.add("segments")
                    self._segment_path = lambda: "segment" + "[path-name='" + str(self.path_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/segments/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Segments.Segment, ['path_name', 'enable'], name, value)


                class Segments_(Entity):
                    """
                    Segments/hops configuration for given
                    Segment\-list
                    
                    .. attribute:: segment
                    
                    	Configure Segment/hop at the index
                    	**type**\: list of  		 :py:class:`Segment_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Segments.Segment.Segments_, self).__init__()

                        self.yang_name = "segments"
                        self.yang_parent_name = "segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("segment", ("segment", Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_))])
                        self._leafs = OrderedDict()

                        self.segment = YList(self)
                        self._segment_path = lambda: "segments"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Segments.Segment.Segments_, [], name, value)


                    class Segment_(Entity):
                        """
                        Configure Segment/hop at the index
                        
                        .. attribute:: segment_index  (key)
                        
                        	Segment index
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: segment_type
                        
                        	Segment/hop type
                        	**type**\:  :py:class:`XtcSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcSegment>`
                        
                        .. attribute:: address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\: int
                        
                        	**range:** 0..1048575
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_, self).__init__()

                            self.yang_name = "segment"
                            self.yang_parent_name = "segments"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['segment_index']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('segment_index', YLeaf(YType.uint32, 'segment-index')),
                                ('segment_type', YLeaf(YType.enumeration, 'segment-type')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('mpls_label', YLeaf(YType.uint32, 'mpls-label')),
                            ])
                            self.segment_index = None
                            self.segment_type = None
                            self.address = None
                            self.mpls_label = None
                            self._segment_path = lambda: "segment" + "[segment-index='" + str(self.segment_index) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_, ['segment_index', 'segment_type', 'address', 'mpls_label'], name, value)


        class Logging(Entity):
            """
            Logging configuration
            
            .. attribute:: policy_status
            
            	Enable logging for policy status
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('policy_status', YLeaf(YType.empty, 'policy-status')),
                ])
                self.policy_status = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Logging, ['policy_status'], name, value)


        class BindingSidRules(Entity):
            """
            Binding sid rules
            
            .. attribute:: explicit
            
            	Binding sid explicit options
            	**type**\:  :py:class:`Explicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.BindingSidRules.Explicit>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.BindingSidRules, self).__init__()

                self.yang_name = "binding-sid-rules"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("explicit", ("explicit", Sr.TrafficEngineering.BindingSidRules.Explicit))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.explicit = Sr.TrafficEngineering.BindingSidRules.Explicit()
                self.explicit.parent = self
                self._children_name_map["explicit"] = "explicit"
                self._children_yang_names.add("explicit")
                self._segment_path = lambda: "binding-sid-rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()


            class Explicit(Entity):
                """
                Binding sid explicit options
                
                .. attribute:: rule
                
                	Binding sid explicit rule
                	**type**\:  :py:class:`XtcBindingSidexplicitRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcBindingSidexplicitRule>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.BindingSidRules.Explicit, self).__init__()

                    self.yang_name = "explicit"
                    self.yang_parent_name = "binding-sid-rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rule', YLeaf(YType.enumeration, 'rule')),
                    ])
                    self.rule = None
                    self._segment_path = lambda: "explicit"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/binding-sid-rules/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.BindingSidRules.Explicit, ['rule'], name, value)


        class Policies(Entity):
            """
            Policy configuration
            
            .. attribute:: policy
            
            	Policy configuration
            	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.Policies, self).__init__()

                self.yang_name = "policies"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("policy", ("policy", Sr.TrafficEngineering.Policies.Policy))])
                self._leafs = OrderedDict()

                self.policy = YList(self)
                self._segment_path = lambda: "policies"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Policies, [], name, value)


            class Policy(Entity):
                """
                Policy configuration
                
                .. attribute:: policy_name  (key)
                
                	Policy name
                	**type**\: str
                
                	**length:** 1..128
                
                .. attribute:: binding_sid
                
                	Binding Segment ID
                	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.BindingSid>`
                
                .. attribute:: policy_color_endpoint
                
                	Color and endpoint of a policyColor, EndPointType, Endpoint
                	**type**\:  :py:class:`PolicyColorEndpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint>`
                
                	**presence node**\: True
                
                .. attribute:: candidate_paths
                
                	Policy candidate\-paths configuration
                	**type**\:  :py:class:`CandidatePaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths>`
                
                .. attribute:: shutdown
                
                	Administratively shutdown policy
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.Policies.Policy, self).__init__()

                    self.yang_name = "policy"
                    self.yang_parent_name = "policies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['policy_name']
                    self._child_container_classes = OrderedDict([("binding-sid", ("binding_sid", Sr.TrafficEngineering.Policies.Policy.BindingSid)), ("policy-color-endpoint", ("policy_color_endpoint", Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint)), ("candidate-paths", ("candidate_paths", Sr.TrafficEngineering.Policies.Policy.CandidatePaths))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('policy_name', YLeaf(YType.str, 'policy-name')),
                        ('shutdown', YLeaf(YType.empty, 'shutdown')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.policy_name = None
                    self.shutdown = None
                    self.enable = None

                    self.binding_sid = Sr.TrafficEngineering.Policies.Policy.BindingSid()
                    self.binding_sid.parent = self
                    self._children_name_map["binding_sid"] = "binding-sid"
                    self._children_yang_names.add("binding-sid")

                    self.policy_color_endpoint = None
                    self._children_name_map["policy_color_endpoint"] = "policy-color-endpoint"
                    self._children_yang_names.add("policy-color-endpoint")

                    self.candidate_paths = Sr.TrafficEngineering.Policies.Policy.CandidatePaths()
                    self.candidate_paths.parent = self
                    self._children_name_map["candidate_paths"] = "candidate-paths"
                    self._children_yang_names.add("candidate-paths")
                    self._segment_path = lambda: "policy" + "[policy-name='" + str(self.policy_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/policies/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy, ['policy_name', 'shutdown', 'enable'], name, value)


                class BindingSid(Entity):
                    """
                    Binding Segment ID
                    
                    .. attribute:: binding_sid_type
                    
                    	Binding SID type
                    	**type**\:  :py:class:`XtcBindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcBindingSid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 16..1048575
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Policies.Policy.BindingSid, self).__init__()

                        self.yang_name = "binding-sid"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('binding_sid_type', YLeaf(YType.enumeration, 'binding-sid-type')),
                            ('mpls_label', YLeaf(YType.uint32, 'mpls-label')),
                        ])
                        self.binding_sid_type = None
                        self.mpls_label = None
                        self._segment_path = lambda: "binding-sid"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.BindingSid, ['binding_sid_type', 'mpls_label'], name, value)


                class PolicyColorEndpoint(Entity):
                    """
                    Color and endpoint of a policyColor,
                    EndPointType, Endpoint
                    
                    .. attribute:: color
                    
                    	Color
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: end_point_type
                    
                    	End point type
                    	**type**\:  :py:class:`XtcEndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcEndPoint>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: end_point_address
                    
                    	End point address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint, self).__init__()

                        self.yang_name = "policy-color-endpoint"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('color', YLeaf(YType.uint32, 'color')),
                            ('end_point_type', YLeaf(YType.enumeration, 'end-point-type')),
                            ('end_point_address', YLeaf(YType.str, 'end-point-address')),
                        ])
                        self.color = None
                        self.end_point_type = None
                        self.end_point_address = None
                        self._segment_path = lambda: "policy-color-endpoint"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint, ['color', 'end_point_type', 'end_point_address'], name, value)


                class CandidatePaths(Entity):
                    """
                    Policy candidate\-paths configuration
                    
                    .. attribute:: preferences
                    
                    	Policy path\-option preference table
                    	**type**\:  :py:class:`Preferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences>`
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths, self).__init__()

                        self.yang_name = "candidate-paths"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("preferences", ("preferences", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.empty, 'enable')),
                        ])
                        self.enable = None

                        self.preferences = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences()
                        self.preferences.parent = self
                        self._children_name_map["preferences"] = "preferences"
                        self._children_yang_names.add("preferences")
                        self._segment_path = lambda: "candidate-paths"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths, ['enable'], name, value)


                    class Preferences(Entity):
                        """
                        Policy path\-option preference table
                        
                        .. attribute:: preference
                        
                        	Policy path\-option preference entry
                        	**type**\: list of  		 :py:class:`Preference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences, self).__init__()

                            self.yang_name = "preferences"
                            self.yang_parent_name = "candidate-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("preference", ("preference", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference))])
                            self._leafs = OrderedDict()

                            self.preference = YList(self)
                            self._segment_path = lambda: "preferences"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences, [], name, value)


                        class Preference(Entity):
                            """
                            Policy path\-option preference entry
                            
                            .. attribute:: path_index  (key)
                            
                            	Path\-option preference
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: constraints
                            
                            	SR path computation and verification constraints
                            	**type**\:  :py:class:`Constraints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints>`
                            
                            .. attribute:: path_infos
                            
                            	Policy path\-option preference configuration
                            	**type**\:  :py:class:`PathInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos>`
                            
                            .. attribute:: enable
                            
                            	True only
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-cfg'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference, self).__init__()

                                self.yang_name = "preference"
                                self.yang_parent_name = "preferences"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['path_index']
                                self._child_container_classes = OrderedDict([("constraints", ("constraints", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints)), ("path-infos", ("path_infos", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path_index', YLeaf(YType.uint32, 'path-index')),
                                    ('enable', YLeaf(YType.empty, 'enable')),
                                ])
                                self.path_index = None
                                self.enable = None

                                self.constraints = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints()
                                self.constraints.parent = self
                                self._children_name_map["constraints"] = "constraints"
                                self._children_yang_names.add("constraints")

                                self.path_infos = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos()
                                self.path_infos.parent = self
                                self._children_name_map["path_infos"] = "path-infos"
                                self._children_yang_names.add("path-infos")
                                self._segment_path = lambda: "preference" + "[path-index='" + str(self.path_index) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference, ['path_index', 'enable'], name, value)


                            class Constraints(Entity):
                                """
                                SR path computation and verification
                                constraints
                                
                                .. attribute:: affinity_rules
                                
                                	SR path computation and verification affinity rules
                                	**type**\:  :py:class:`AffinityRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules>`
                                
                                .. attribute:: enable
                                
                                	True only
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-cfg'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints, self).__init__()

                                    self.yang_name = "constraints"
                                    self.yang_parent_name = "preference"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("affinity-rules", ("affinity_rules", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('enable', YLeaf(YType.empty, 'enable')),
                                    ])
                                    self.enable = None

                                    self.affinity_rules = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules()
                                    self.affinity_rules.parent = self
                                    self._children_name_map["affinity_rules"] = "affinity-rules"
                                    self._children_yang_names.add("affinity-rules")
                                    self._segment_path = lambda: "constraints"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints, ['enable'], name, value)


                                class AffinityRules(Entity):
                                    """
                                    SR path computation and verification
                                    affinity rules
                                    
                                    .. attribute:: affinity_rule
                                    
                                    	SR path computation and verification affinity rule
                                    	**type**\: list of  		 :py:class:`AffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-agent-cfg'
                                    _revision = '2017-09-11'

                                    def __init__(self):
                                        super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules, self).__init__()

                                        self.yang_name = "affinity-rules"
                                        self.yang_parent_name = "constraints"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("affinity-rule", ("affinity_rule", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule))])
                                        self._leafs = OrderedDict()

                                        self.affinity_rule = YList(self)
                                        self._segment_path = lambda: "affinity-rules"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules, [], name, value)


                                    class AffinityRule(Entity):
                                        """
                                        SR path computation and verification
                                        affinity rule
                                        
                                        .. attribute:: rule  (key)
                                        
                                        	Path\-option preference
                                        	**type**\:  :py:class:`XtcAffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcAffinityRule>`
                                        
                                        .. attribute:: color  (key)
                                        
                                        	The color
                                        	**type**\: str
                                        
                                        	**length:** 1..128
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2017-09-11'

                                        def __init__(self):
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule, self).__init__()

                                            self.yang_name = "affinity-rule"
                                            self.yang_parent_name = "affinity-rules"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['rule','color']
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rule', YLeaf(YType.enumeration, 'rule')),
                                                ('color', YLeaf(YType.str, 'color')),
                                            ])
                                            self.rule = None
                                            self.color = None
                                            self._segment_path = lambda: "affinity-rule" + "[rule='" + str(self.rule) + "']" + "[color='" + str(self.color) + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule, ['rule', 'color'], name, value)


                            class PathInfos(Entity):
                                """
                                Policy path\-option preference
                                configuration
                                
                                .. attribute:: path_info
                                
                                	Policy configuration
                                	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo>`
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-cfg'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, self).__init__()

                                    self.yang_name = "path-infos"
                                    self.yang_parent_name = "preference"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("path-info", ("path_info", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo))])
                                    self._leafs = OrderedDict()

                                    self.path_info = YList(self)
                                    self._segment_path = lambda: "path-infos"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, [], name, value)


                                class PathInfo(Entity):
                                    """
                                    Policy configuration
                                    
                                    .. attribute:: type  (key)
                                    
                                    	Path\-option type
                                    	**type**\:  :py:class:`XtcPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcPath>`
                                    
                                    .. attribute:: hop_type  (key)
                                    
                                    	Type of dynamic path to be computed
                                    	**type**\:  :py:class:`XtcPathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcPathHop>`
                                    
                                    .. attribute:: segment_list_name  (key)
                                    
                                    	Segment\-list name
                                    	**type**\: str
                                    
                                    	**length:** 1..128
                                    
                                    .. attribute:: pce
                                    
                                    	PCE configuration for the candidate\-path . Valid only for dynamic candidate\-paths 
                                    	**type**\:  :py:class:`Pce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pce>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration, valid only for dynamic path\-options
                                    	**type**\:  :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric>`
                                    
                                    .. attribute:: weight
                                    
                                    	Path\-option weight
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: enable
                                    
                                    	True only
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-agent-cfg'
                                    _revision = '2017-09-11'

                                    def __init__(self):
                                        super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, self).__init__()

                                        self.yang_name = "path-info"
                                        self.yang_parent_name = "path-infos"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['type','hop_type','segment_list_name']
                                        self._child_container_classes = OrderedDict([("pce", ("pce", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pce)), ("metric", ("metric", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('type', YLeaf(YType.enumeration, 'type')),
                                            ('hop_type', YLeaf(YType.enumeration, 'hop-type')),
                                            ('segment_list_name', YLeaf(YType.str, 'segment-list-name')),
                                            ('weight', YLeaf(YType.int32, 'weight')),
                                            ('enable', YLeaf(YType.empty, 'enable')),
                                        ])
                                        self.type = None
                                        self.hop_type = None
                                        self.segment_list_name = None
                                        self.weight = None
                                        self.enable = None

                                        self.pce = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pce()
                                        self.pce.parent = self
                                        self._children_name_map["pce"] = "pce"
                                        self._children_yang_names.add("pce")

                                        self.metric = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric()
                                        self.metric.parent = self
                                        self._children_name_map["metric"] = "metric"
                                        self._children_yang_names.add("metric")
                                        self._segment_path = lambda: "path-info" + "[type='" + str(self.type) + "']" + "[hop-type='" + str(self.hop_type) + "']" + "[segment-list-name='" + str(self.segment_list_name) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, ['type', 'hop_type', 'segment_list_name', 'weight', 'enable'], name, value)


                                    class Pce(Entity):
                                        """
                                        PCE configuration for the candidate\-path
                                        . Valid only for dynamic candidate\-paths
                                        .
                                        
                                        .. attribute:: enable
                                        
                                        	True only
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2017-09-11'

                                        def __init__(self):
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pce, self).__init__()

                                            self.yang_name = "pce"
                                            self.yang_parent_name = "path-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "pce"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pce, ['enable'], name, value)


                                    class Metric(Entity):
                                        """
                                        Metric configuration, valid only for
                                        dynamic path\-options
                                        
                                        .. attribute:: margin
                                        
                                        	Metric type
                                        	**type**\:  :py:class:`Margin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.Margin>`
                                        
                                        .. attribute:: sid_limit
                                        
                                        	Maximum number of SIDs
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: metric_type
                                        
                                        	Metric type
                                        	**type**\:  :py:class:`XtcMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetric>`
                                        
                                        .. attribute:: enable
                                        
                                        	True only
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2017-09-11'

                                        def __init__(self):
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "path-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("margin", ("margin", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.Margin))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sid_limit', YLeaf(YType.uint32, 'sid-limit')),
                                                ('metric_type', YLeaf(YType.enumeration, 'metric-type')),
                                                ('enable', YLeaf(YType.empty, 'enable')),
                                            ])
                                            self.sid_limit = None
                                            self.metric_type = None
                                            self.enable = None

                                            self.margin = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.Margin()
                                            self.margin.parent = self
                                            self._children_name_map["margin"] = "margin"
                                            self._children_yang_names.add("margin")
                                            self._segment_path = lambda: "metric"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, ['sid_limit', 'metric_type', 'enable'], name, value)


                                        class Margin(Entity):
                                            """
                                            Metric type
                                            
                                            .. attribute:: value_type
                                            
                                            	Metric value type
                                            	**type**\:  :py:class:`XtcMetricValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetricValue>`
                                            
                                            .. attribute:: absolute_value
                                            
                                            	Absolute metric value
                                            	**type**\: int
                                            
                                            	**range:** 0..2147483647
                                            
                                            .. attribute:: relative_value
                                            
                                            	Relative metric value
                                            	**type**\: int
                                            
                                            	**range:** 0..100
                                            
                                            

                                            """

                                            _prefix = 'infra-xtc-agent-cfg'
                                            _revision = '2017-09-11'

                                            def __init__(self):
                                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.Margin, self).__init__()

                                                self.yang_name = "margin"
                                                self.yang_parent_name = "metric"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value_type', YLeaf(YType.enumeration, 'value-type')),
                                                    ('absolute_value', YLeaf(YType.uint32, 'absolute-value')),
                                                    ('relative_value', YLeaf(YType.uint32, 'relative-value')),
                                                ])
                                                self.value_type = None
                                                self.absolute_value = None
                                                self.relative_value = None
                                                self._segment_path = lambda: "margin"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.Margin, ['value_type', 'absolute_value', 'relative_value'], name, value)


        class SrteInterfaces(Entity):
            """
            SR\-TE interfaces
            
            .. attribute:: srte_interface
            
            	SR\-TE interface
            	**type**\: list of  		 :py:class:`SrteInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.SrteInterfaces, self).__init__()

                self.yang_name = "srte-interfaces"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("srte-interface", ("srte_interface", Sr.TrafficEngineering.SrteInterfaces.SrteInterface))])
                self._leafs = OrderedDict()

                self.srte_interface = YList(self)
                self._segment_path = lambda: "srte-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces, [], name, value)


            class SrteInterface(Entity):
                """
                SR\-TE interface
                
                .. attribute:: srte_interface_name  (key)
                
                	SR\-TE Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: interface_affinities
                
                	Set user defined interface attribute flags
                	**type**\:  :py:class:`InterfaceAffinities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities>`
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface, self).__init__()

                    self.yang_name = "srte-interface"
                    self.yang_parent_name = "srte-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['srte_interface_name']
                    self._child_container_classes = OrderedDict([("interface-affinities", ("interface_affinities", Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srte_interface_name', YLeaf(YType.str, 'srte-interface-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.srte_interface_name = None
                    self.enable = None

                    self.interface_affinities = Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities()
                    self.interface_affinities.parent = self
                    self._children_name_map["interface_affinities"] = "interface-affinities"
                    self._children_yang_names.add("interface-affinities")
                    self._segment_path = lambda: "srte-interface" + "[srte-interface-name='" + str(self.srte_interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/srte-interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface, ['srte_interface_name', 'enable'], name, value)


                class InterfaceAffinities(Entity):
                    """
                    Set user defined interface attribute flags
                    
                    .. attribute:: interface_affinity
                    
                    	Set user defined interface attribute flags
                    	**type**\: list of  		 :py:class:`InterfaceAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities, self).__init__()

                        self.yang_name = "interface-affinities"
                        self.yang_parent_name = "srte-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface-affinity", ("interface_affinity", Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity))])
                        self._leafs = OrderedDict()

                        self.interface_affinity = YList(self)
                        self._segment_path = lambda: "interface-affinities"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities, [], name, value)


                    class InterfaceAffinity(Entity):
                        """
                        Set user defined interface attribute flags
                        
                        .. attribute:: color  (key)
                        
                        	Interface affinity colors
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity, self).__init__()

                            self.yang_name = "interface-affinity"
                            self.yang_parent_name = "interface-affinities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['color']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('color', YLeaf(YType.str, 'color')),
                            ])
                            self.color = None
                            self._segment_path = lambda: "interface-affinity" + "[color='" + str(self.color) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity, ['color'], name, value)


        class Pcc(Entity):
            """
            Path Computation Client
            
            .. attribute:: pce_peers
            
            	PCE peer configuration
            	**type**\:  :py:class:`PcePeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PcePeers>`
            
            .. attribute:: pce_addresses
            
            	PCE peer configuration
            	**type**\:  :py:class:`PceAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PceAddresses>`
            
            .. attribute:: dead_timer_interval
            
            	Amount of time after which the peer can declare this session down, if no PCEP message has been received
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: report_all
            
            	Report all local SR policies to connected PCEP peers
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: keepalive_timer_interval
            
            	Maximum time between two consecutive PCEP messages sent by this node
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: source_address
            
            	Local source IP address to use on PCEP sessions
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: enable
            
            	PCC Enable
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: delegation_timeout
            
            	The maximum time delegated SR\-TE policies can remain up without an active connection to a PCE
            	**type**\: int
            
            	**range:** 0..3600
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.Pcc, self).__init__()

                self.yang_name = "pcc"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("pce-peers", ("pce_peers", Sr.TrafficEngineering.Pcc.PcePeers)), ("pce-addresses", ("pce_addresses", Sr.TrafficEngineering.Pcc.PceAddresses))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dead_timer_interval', YLeaf(YType.uint32, 'dead-timer-interval')),
                    ('report_all', YLeaf(YType.empty, 'report-all')),
                    ('keepalive_timer_interval', YLeaf(YType.uint32, 'keepalive-timer-interval')),
                    ('source_address', YLeaf(YType.str, 'source-address')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                    ('delegation_timeout', YLeaf(YType.uint32, 'delegation-timeout')),
                ])
                self.dead_timer_interval = None
                self.report_all = None
                self.keepalive_timer_interval = None
                self.source_address = None
                self.enable = None
                self.delegation_timeout = None

                self.pce_peers = Sr.TrafficEngineering.Pcc.PcePeers()
                self.pce_peers.parent = self
                self._children_name_map["pce_peers"] = "pce-peers"
                self._children_yang_names.add("pce-peers")

                self.pce_addresses = Sr.TrafficEngineering.Pcc.PceAddresses()
                self.pce_addresses.parent = self
                self._children_name_map["pce_addresses"] = "pce-addresses"
                self._children_yang_names.add("pce-addresses")
                self._segment_path = lambda: "pcc"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Pcc, ['dead_timer_interval', 'report_all', 'keepalive_timer_interval', 'source_address', 'enable', 'delegation_timeout'], name, value)


            class PcePeers(Entity):
                """
                PCE peer configuration
                
                .. attribute:: pce_peer
                
                	PCE peer
                	**type**\: list of  		 :py:class:`PcePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PcePeers.PcePeer>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.Pcc.PcePeers, self).__init__()

                    self.yang_name = "pce-peers"
                    self.yang_parent_name = "pcc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("pce-peer", ("pce_peer", Sr.TrafficEngineering.Pcc.PcePeers.PcePeer))])
                    self._leafs = OrderedDict()

                    self.pce_peer = YList(self)
                    self._segment_path = lambda: "pce-peers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Pcc.PcePeers, [], name, value)


                class PcePeer(Entity):
                    """
                    PCE peer
                    
                    .. attribute:: pce_address  (key)
                    
                    	Remote PCE address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enable
                    
                    	PCC Peer Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value of this PCE
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Pcc.PcePeers.PcePeer, self).__init__()

                        self.yang_name = "pce-peer"
                        self.yang_parent_name = "pce-peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['pce_address']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pce_address', YLeaf(YType.str, 'pce-address')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                            ('precedence', YLeaf(YType.uint32, 'precedence')),
                        ])
                        self.pce_address = None
                        self.enable = None
                        self.precedence = None
                        self._segment_path = lambda: "pce-peer" + "[pce-address='" + str(self.pce_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/pce-peers/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Pcc.PcePeers.PcePeer, ['pce_address', 'enable', 'precedence'], name, value)


            class PceAddresses(Entity):
                """
                PCE peer configuration
                
                .. attribute:: pce_address
                
                	PCE peer address
                	**type**\: list of  		 :py:class:`PceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PceAddresses.PceAddress>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.Pcc.PceAddresses, self).__init__()

                    self.yang_name = "pce-addresses"
                    self.yang_parent_name = "pcc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("pce-address", ("pce_address", Sr.TrafficEngineering.Pcc.PceAddresses.PceAddress))])
                    self._leafs = OrderedDict()

                    self.pce_address = YList(self)
                    self._segment_path = lambda: "pce-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Pcc.PceAddresses, [], name, value)


                class PceAddress(Entity):
                    """
                    PCE peer address
                    
                    .. attribute:: pce_address  (key)
                    
                    	Remote PCE address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: precedence
                    
                    	Precedence value of this PCE
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Sr.TrafficEngineering.Pcc.PceAddresses.PceAddress, self).__init__()

                        self.yang_name = "pce-address"
                        self.yang_parent_name = "pce-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['pce_address']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pce_address', YLeaf(YType.str, 'pce-address')),
                            ('precedence', YLeaf(YType.uint32, 'precedence')),
                        ])
                        self.pce_address = None
                        self.precedence = None
                        self._segment_path = lambda: "pce-address" + "[pce-address='" + str(self.pce_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/pce-addresses/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Pcc.PceAddresses.PceAddress, ['pce_address', 'precedence'], name, value)


        class AffinityMaps(Entity):
            """
            Affinity\-map configuration
            
            .. attribute:: affinity_map
            
            	Affinity\-map entry
            	**type**\: list of  		 :py:class:`AffinityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.AffinityMaps.AffinityMap>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2017-09-11'

            def __init__(self):
                super(Sr.TrafficEngineering.AffinityMaps, self).__init__()

                self.yang_name = "affinity-maps"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("affinity-map", ("affinity_map", Sr.TrafficEngineering.AffinityMaps.AffinityMap))])
                self._leafs = OrderedDict()

                self.affinity_map = YList(self)
                self._segment_path = lambda: "affinity-maps"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.AffinityMaps, [], name, value)


            class AffinityMap(Entity):
                """
                Affinity\-map entry
                
                .. attribute:: color  (key)
                
                	Affinity\-map bit\-position
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: bit_position
                
                	Affinity\-map bit\-position
                	**type**\: int
                
                	**range:** 0..31
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Sr.TrafficEngineering.AffinityMaps.AffinityMap, self).__init__()

                    self.yang_name = "affinity-map"
                    self.yang_parent_name = "affinity-maps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['color']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('color', YLeaf(YType.str, 'color')),
                        ('bit_position', YLeaf(YType.uint32, 'bit-position')),
                    ])
                    self.color = None
                    self.bit_position = None
                    self._segment_path = lambda: "affinity-map" + "[color='" + str(self.color) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/affinity-maps/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.AffinityMaps.AffinityMap, ['color', 'bit_position'], name, value)

    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity

