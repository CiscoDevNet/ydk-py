""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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
    
    .. attribute:: srv6
    
    	Segment Routing with IPv6 dataplane
    	**type**\:  :py:class:`Srv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6>`
    
    

    """

    _prefix = 'segment-routing-ms-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(Sr, self).__init__()
        self._top_entity = None

        self.yang_name = "sr"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("local-block", ("local_block", Sr.LocalBlock)), ("mappings", ("mappings", Sr.Mappings)), ("adjacency-sid", ("adjacency_sid", Sr.AdjacencySid)), ("global-block", ("global_block", Sr.GlobalBlock)), ("Cisco-IOS-XR-segment-routing-srv6-cfg:srv6", ("srv6", Sr.Srv6))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.local_block = None
        self._children_name_map["local_block"] = "local-block"

        self.mappings = Sr.Mappings()
        self.mappings.parent = self
        self._children_name_map["mappings"] = "mappings"

        self.adjacency_sid = Sr.AdjacencySid()
        self.adjacency_sid.parent = self
        self._children_name_map["adjacency_sid"] = "adjacency-sid"

        self.global_block = None
        self._children_name_map["global_block"] = "global-block"

        self.srv6 = Sr.Srv6()
        self.srv6.parent = self
        self._children_name_map["srv6"] = "Cisco-IOS-XR-segment-routing-srv6-cfg:srv6"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr"
        self._is_frozen = True

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
        _revision = '2017-09-07'

        def __init__(self):
            super(Sr.LocalBlock, self).__init__()

            self.yang_name = "local-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('lower_bound', (YLeaf(YType.uint32, 'lower-bound'), ['int'])),
                ('upper_bound', (YLeaf(YType.uint32, 'upper-bound'), ['int'])),
            ])
            self.lower_bound = None
            self.upper_bound = None
            self._segment_path = lambda: "local-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

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
        _revision = '2017-09-07'

        def __init__(self):
            super(Sr.Mappings, self).__init__()

            self.yang_name = "mappings"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mapping", ("mapping", Sr.Mappings.Mapping))])
            self._leafs = OrderedDict()

            self.mapping = YList(self)
            self._segment_path = lambda: "mappings"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.Mappings, [], name, value)


        class Mapping(Entity):
            """
            IP prefix to SID mapping
            
            .. attribute:: af  (key)
            
            	Address Family
            	**type**\:  :py:class:`SrmsAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsAddressFamily>`
            
            .. attribute:: ip  (key)
            
            	IP prefix
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: mask  (key)
            
            	Mask
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: sid_start
            
            	Start of SID index range
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: sid_range
            
            	Range (number of SIDs)
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: flag_attached
            
            	Enable/Disable Attached flag
            	**type**\:  :py:class:`SrmsMiFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsMiFlag>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sr.Mappings.Mapping, self).__init__()

                self.yang_name = "mapping"
                self.yang_parent_name = "mappings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af','ip','mask']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsAddressFamily', '')])),
                    ('ip', (YLeaf(YType.str, 'ip'), ['str','str'])),
                    ('mask', (YLeaf(YType.uint32, 'mask'), ['int'])),
                    ('sid_start', (YLeaf(YType.uint32, 'sid-start'), ['int'])),
                    ('sid_range', (YLeaf(YType.uint32, 'sid-range'), ['int'])),
                    ('flag_attached', (YLeaf(YType.enumeration, 'flag-attached'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsMiFlag', '')])),
                ])
                self.af = None
                self.ip = None
                self.mask = None
                self.sid_start = None
                self.sid_range = None
                self.flag_attached = None
                self._segment_path = lambda: "mapping" + "[af='" + str(self.af) + "']" + "[ip='" + str(self.ip) + "']" + "[mask='" + str(self.mask) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/mappings/%s" % self._segment_path()
                self._is_frozen = True

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
        _revision = '2017-09-07'

        def __init__(self):
            super(Sr.AdjacencySid, self).__init__()

            self.yang_name = "adjacency-sid"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Sr.AdjacencySid.Interfaces))])
            self._leafs = OrderedDict()

            self.interfaces = Sr.AdjacencySid.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "adjacency-sid"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.AdjacencySid, [], name, value)


        class Interfaces(Entity):
            """
            Segment Routing Adjacency SID Interface Table
            
            .. attribute:: interface
            
            	Segment Routing Adjacency SID Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sr.AdjacencySid.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "adjacency-sid"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Sr.AdjacencySid.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/adjacency-sid/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.AdjacencySid.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Segment Routing Adjacency SID Interface
                
                .. attribute:: interface  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: address_families
                
                	Segment Routing Adjacency SID Interface Address Family Table
                	**type**\:  :py:class:`AddressFamilies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface.AddressFamilies>`
                
                

                """

                _prefix = 'segment-routing-ms-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sr.AdjacencySid.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface']
                    self._child_classes = OrderedDict([("address-families", ("address_families", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies))])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = None

                    self.address_families = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies()
                    self.address_families.parent = self
                    self._children_name_map["address_families"] = "address-families"
                    self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/adjacency-sid/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies, self).__init__()

                        self.yang_name = "address-families"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address-family", ("address_family", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily))])
                        self._leafs = OrderedDict()

                        self.address_family = YList(self)
                        self._segment_path = lambda: "address-families"
                        self._is_frozen = True

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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily, self).__init__()

                            self.yang_name = "address-family"
                            self.yang_parent_name = "address-families"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address_family']
                            self._child_classes = OrderedDict([("next-hops", ("next_hops", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops))])
                            self._leafs = OrderedDict([
                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsAddressFamily', '')])),
                            ])
                            self.address_family = None

                            self.next_hops = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops()
                            self.next_hops.parent = self
                            self._children_name_map["next_hops"] = "next-hops"
                            self._segment_path = lambda: "address-family" + "[address-family='" + str(self.address_family) + "']"
                            self._is_frozen = True

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
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops, self).__init__()

                                self.yang_name = "next-hops"
                                self.yang_parent_name = "address-family"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop))])
                                self._leafs = OrderedDict()

                                self.next_hop = YList(self)
                                self._segment_path = lambda: "next-hops"
                                self._is_frozen = True

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
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "next-hops"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['ip_addr']
                                    self._child_classes = OrderedDict([("l2-adjacency-sid", ("l2_adjacency_sid", Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid))])
                                    self._leafs = OrderedDict([
                                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                                    ])
                                    self.ip_addr = None

                                    self.l2_adjacency_sid = Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid()
                                    self.l2_adjacency_sid.parent = self
                                    self._children_name_map["l2_adjacency_sid"] = "l2-adjacency-sid"
                                    self._segment_path = lambda: "next-hop" + "[ip-addr='" + str(self.ip_addr) + "']"
                                    self._is_frozen = True

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
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid, self).__init__()

                                        self.yang_name = "l2-adjacency-sid"
                                        self.yang_parent_name = "next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SidTypeList', '')])),
                                            ('absolute_sid', (YLeaf(YType.uint32, 'absolute-sid'), ['int'])),
                                            ('index_sid', (YLeaf(YType.uint32, 'index-sid'), ['int'])),
                                            ('srlb', (YLeaf(YType.str, 'srlb'), ['str'])),
                                        ])
                                        self.sid_type = None
                                        self.absolute_sid = None
                                        self.index_sid = None
                                        self.srlb = None
                                        self._segment_path = lambda: "l2-adjacency-sid"
                                        self._is_frozen = True

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
        _revision = '2017-09-07'

        def __init__(self):
            super(Sr.GlobalBlock, self).__init__()

            self.yang_name = "global-block"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('lower_bound', (YLeaf(YType.uint32, 'lower-bound'), ['int'])),
                ('upper_bound', (YLeaf(YType.uint32, 'upper-bound'), ['int'])),
            ])
            self.lower_bound = None
            self.upper_bound = None
            self._segment_path = lambda: "global-block"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.GlobalBlock, ['lower_bound', 'upper_bound'], name, value)



    class Srv6(Entity):
        """
        Segment Routing with IPv6 dataplane
        
        .. attribute:: logging
        
        	Enable logging
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Logging>`
        
        .. attribute:: locators
        
        	Configure SRv6 locators parameters
        	**type**\:  :py:class:`Locators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators>`
        
        .. attribute:: encapsulation
        
        	Configure encapsulation related parameters
        	**type**\:  :py:class:`Encapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Encapsulation>`
        
        .. attribute:: enable
        
        	Enable SRv6
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: sid_holdtime
        
        	Configure SID holdtime for a stale/freed SID
        	**type**\: int
        
        	**range:** 0..60
        
        

        """

        _prefix = 'segment-routing-srv6-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sr.Srv6, self).__init__()

            self.yang_name = "srv6"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("logging", ("logging", Sr.Srv6.Logging)), ("locators", ("locators", Sr.Srv6.Locators)), ("encapsulation", ("encapsulation", Sr.Srv6.Encapsulation))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ('sid_holdtime', (YLeaf(YType.uint32, 'sid-holdtime'), ['int'])),
            ])
            self.enable = None
            self.sid_holdtime = None

            self.logging = Sr.Srv6.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"

            self.locators = Sr.Srv6.Locators()
            self.locators.parent = self
            self._children_name_map["locators"] = "locators"

            self.encapsulation = Sr.Srv6.Encapsulation()
            self.encapsulation.parent = self
            self._children_name_map["encapsulation"] = "encapsulation"
            self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-cfg:srv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.Srv6, ['enable', 'sid_holdtime'], name, value)


        class Logging(Entity):
            """
            Enable logging
            
            .. attribute:: locator_status
            
            	Enable logging for locator status changes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'segment-routing-srv6-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.Srv6.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "srv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('locator_status', (YLeaf(YType.empty, 'locator-status'), ['Empty'])),
                ])
                self.locator_status = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.Srv6.Logging, ['locator_status'], name, value)



        class Locators(Entity):
            """
            Configure SRv6 locators parameters
            
            .. attribute:: locators
            
            	Configure SRv6 table of locators
            	**type**\:  :py:class:`Locators_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators.Locators_>`
            
            

            """

            _prefix = 'segment-routing-srv6-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.Srv6.Locators, self).__init__()

                self.yang_name = "locators"
                self.yang_parent_name = "srv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locators", ("locators", Sr.Srv6.Locators.Locators_))])
                self._leafs = OrderedDict()

                self.locators = Sr.Srv6.Locators.Locators_()
                self.locators.parent = self
                self._children_name_map["locators"] = "locators"
                self._segment_path = lambda: "locators"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.Srv6.Locators, [], name, value)


            class Locators_(Entity):
                """
                Configure SRv6 table of locators
                
                .. attribute:: locator
                
                	Configure a SRv6 locator
                	**type**\: list of  		 :py:class:`Locator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators.Locators_.Locator>`
                
                

                """

                _prefix = 'segment-routing-srv6-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sr.Srv6.Locators.Locators_, self).__init__()

                    self.yang_name = "locators"
                    self.yang_parent_name = "locators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("locator", ("locator", Sr.Srv6.Locators.Locators_.Locator))])
                    self._leafs = OrderedDict()

                    self.locator = YList(self)
                    self._segment_path = lambda: "locators"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/locators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.Srv6.Locators.Locators_, [], name, value)


                class Locator(Entity):
                    """
                    Configure a SRv6 locator
                    
                    .. attribute:: name  (key)
                    
                    	Locator name
                    	**type**\: str
                    
                    	**length:** 1..58
                    
                    .. attribute:: prefix
                    
                    	Specify locator prefix value
                    	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators.Locators_.Locator.Prefix>`
                    
                    .. attribute:: locator_enable
                    
                    	Enable a SRv6 locator
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sr.Srv6.Locators.Locators_.Locator, self).__init__()

                        self.yang_name = "locator"
                        self.yang_parent_name = "locators"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("prefix", ("prefix", Sr.Srv6.Locators.Locators_.Locator.Prefix))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('locator_enable', (YLeaf(YType.empty, 'locator-enable'), ['Empty'])),
                        ])
                        self.name = None
                        self.locator_enable = None

                        self.prefix = Sr.Srv6.Locators.Locators_.Locator.Prefix()
                        self.prefix.parent = self
                        self._children_name_map["prefix"] = "prefix"
                        self._segment_path = lambda: "locator" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/locators/locators/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.Srv6.Locators.Locators_.Locator, ['name', 'locator_enable'], name, value)


                    class Prefix(Entity):
                        """
                        Specify locator prefix value
                        
                        .. attribute:: prefix
                        
                        	IPv6 Prefix
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 32..112
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sr.Srv6.Locators.Locators_.Locator.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "locator"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self._segment_path = lambda: "prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.Srv6.Locators.Locators_.Locator.Prefix, ['prefix', 'prefix_length'], name, value)






        class Encapsulation(Entity):
            """
            Configure encapsulation related parameters
            
            .. attribute:: hop_limit
            
            	Configure IPv6 Hop\-Limit options
            	**type**\:  :py:class:`HopLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Encapsulation.HopLimit>`
            
            .. attribute:: source_address
            
            	Configure a source address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'segment-routing-srv6-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sr.Srv6.Encapsulation, self).__init__()

                self.yang_name = "encapsulation"
                self.yang_parent_name = "srv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("hop-limit", ("hop_limit", Sr.Srv6.Encapsulation.HopLimit))])
                self._leafs = OrderedDict([
                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                ])
                self.source_address = None

                self.hop_limit = Sr.Srv6.Encapsulation.HopLimit()
                self.hop_limit.parent = self
                self._children_name_map["hop_limit"] = "hop-limit"
                self._segment_path = lambda: "encapsulation"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.Srv6.Encapsulation, ['source_address'], name, value)


            class HopLimit(Entity):
                """
                Configure IPv6 Hop\-Limit options
                
                .. attribute:: option
                
                	Hop\-Limit config option
                	**type**\:  :py:class:`Srv6EncapsulationHopLimitOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_datatypes.Srv6EncapsulationHopLimitOption>`
                
                .. attribute:: value
                
                	Count for Hop\-limit
                	**type**\: int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'segment-routing-srv6-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sr.Srv6.Encapsulation.HopLimit, self).__init__()

                    self.yang_name = "hop-limit"
                    self.yang_parent_name = "encapsulation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('option', (YLeaf(YType.enumeration, 'option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_datatypes', 'Srv6EncapsulationHopLimitOption', '')])),
                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                    ])
                    self.option = None
                    self.value = None
                    self._segment_path = lambda: "hop-limit"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-segment-routing-srv6-cfg:srv6/encapsulation/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.Srv6.Encapsulation.HopLimit, ['option', 'value'], name, value)




    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity



