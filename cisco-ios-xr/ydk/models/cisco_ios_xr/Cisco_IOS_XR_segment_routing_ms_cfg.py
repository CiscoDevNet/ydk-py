""" Cisco_IOS_XR_segment_routing_ms_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['SidTypeList']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['SrmsAddressFamily']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['SrmsMiFlag']



class Sr(_Entity_):
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
    
    .. attribute:: traffic_engineering
    
    	Traffic Engineering configuration data
    	**type**\:  :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering>`
    
    

    """

    _prefix = 'segment-routing-ms-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Sr, self).__init__()
        self._top_entity = None

        self.yang_name = "sr"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("local-block", ("local_block", Sr.LocalBlock)), ("mappings", ("mappings", Sr.Mappings)), ("adjacency-sid", ("adjacency_sid", Sr.AdjacencySid)), ("global-block", ("global_block", Sr.GlobalBlock)), ("Cisco-IOS-XR-segment-routing-srv6-cfg:srv6", ("srv6", Sr.Srv6)), ("Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering", ("traffic_engineering", Sr.TrafficEngineering))])
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

        self.traffic_engineering = Sr.TrafficEngineering()
        self.traffic_engineering.parent = self
        self._children_name_map["traffic_engineering"] = "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sr, ['enable'], name, value)


    class LocalBlock(_Entity_):
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
            if sys.version_info > (3,):
                super().__init__()
            else:
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.LocalBlock']['meta_info']


    class Mappings(_Entity_):
        """
        Mapping Server
        
        .. attribute:: mapping
        
        	IP prefix to SID mapping
        	**type**\: list of  		 :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Mappings.Mapping>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Mapping(_Entity_):
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
            
            	**range:** 0..65535
            
            .. attribute:: flag_attached
            
            	Enable/Disable Attached flag
            	**type**\:  :py:class:`SrmsMiFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.SrmsMiFlag>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.Mappings.Mapping']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.Mappings']['meta_info']


    class AdjacencySid(_Entity_):
        """
        Segment Routing Adjacency SID
        
        .. attribute:: interfaces
        
        	Segment Routing Adjacency SID Interface Table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces>`
        
        

        """

        _prefix = 'segment-routing-ms-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Interfaces(_Entity_):
            """
            Segment Routing Adjacency SID Interface Table
            
            .. attribute:: interface
            
            	Segment Routing Adjacency SID Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.AdjacencySid.Interfaces.Interface>`
            
            

            """

            _prefix = 'segment-routing-ms-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Interface(_Entity_):
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
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class AddressFamilies(_Entity_):
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
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class AddressFamily(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class NextHops(_Entity_):
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class NextHop(_Entity_):
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
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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


                                class L2AdjacencySid(_Entity_):
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                        return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                    return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.AdjacencySid.Interfaces.Interface']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.AdjacencySid.Interfaces']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.AdjacencySid']['meta_info']


    class GlobalBlock(_Entity_):
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
            if sys.version_info > (3,):
                super().__init__()
            else:
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.GlobalBlock']['meta_info']


    class Srv6(_Entity_):
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
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Logging(_Entity_):
            """
            Enable logging
            
            .. attribute:: locator_status
            
            	Enable logging for locator status changes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'segment-routing-srv6-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.Srv6.Logging']['meta_info']


        class Locators(_Entity_):
            """
            Configure SRv6 locators parameters
            
            .. attribute:: locators
            
            	Configure SRv6 table of locators
            	**type**\:  :py:class:`Locators_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators.Locators_>`
            
            

            """

            _prefix = 'segment-routing-srv6-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Locators_(_Entity_):
                """
                Configure SRv6 table of locators
                
                .. attribute:: locator
                
                	Configure a SRv6 locator
                	**type**\: list of  		 :py:class:`Locator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.Srv6.Locators.Locators_.Locator>`
                
                

                """

                _prefix = 'segment-routing-srv6-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Locator(_Entity_):
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
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Prefix(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.Srv6.Locators.Locators_.Locator.Prefix']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.Srv6.Locators.Locators_.Locator']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.Srv6.Locators.Locators_']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.Srv6.Locators']['meta_info']


        class Encapsulation(_Entity_):
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
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class HopLimit(_Entity_):
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
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.Srv6.Encapsulation.HopLimit']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.Srv6.Encapsulation']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.Srv6']['meta_info']


    class TrafficEngineering(_Entity_):
        """
        Traffic Engineering configuration data
        
        .. attribute:: out_of_resources
        
        	SR\-TE out\-of\-resources handling configuration
        	**type**\:  :py:class:`OutOfResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OutOfResources>`
        
        .. attribute:: on_demand_colors
        
        	On\-demand color configuration
        	**type**\:  :py:class:`OnDemandColors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors>`
        
        .. attribute:: segments
        
        	Segment\-lists configuration
        	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments>`
        
        .. attribute:: logging
        
        	Logging configuration
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Logging>`
        
        .. attribute:: timers
        
        	SR\-TE timers configuration
        	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Timers>`
        
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
        
        .. attribute:: candidate_path_types
        
        	Configurations for candidate paths
        	**type**\:  :py:class:`CandidatePathTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.CandidatePathTypes>`
        
        .. attribute:: te_latency
        
        	Use TE\-latency algorithm
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: maximum_sid_depth
        
        	Maximum SID Depth Configuration
        	**type**\: int
        
        	**range:** 1..255
        
        .. attribute:: enable
        
        	True only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-agent-cfg'
        _revision = '2019-09-05'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Sr.TrafficEngineering, self).__init__()

            self.yang_name = "traffic-engineering"
            self.yang_parent_name = "sr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("out-of-resources", ("out_of_resources", Sr.TrafficEngineering.OutOfResources)), ("on-demand-colors", ("on_demand_colors", Sr.TrafficEngineering.OnDemandColors)), ("segments", ("segments", Sr.TrafficEngineering.Segments)), ("logging", ("logging", Sr.TrafficEngineering.Logging)), ("timers", ("timers", Sr.TrafficEngineering.Timers)), ("binding-sid-rules", ("binding_sid_rules", Sr.TrafficEngineering.BindingSidRules)), ("policies", ("policies", Sr.TrafficEngineering.Policies)), ("srte-interfaces", ("srte_interfaces", Sr.TrafficEngineering.SrteInterfaces)), ("pcc", ("pcc", Sr.TrafficEngineering.Pcc)), ("affinity-maps", ("affinity_maps", Sr.TrafficEngineering.AffinityMaps)), ("candidate-path-types", ("candidate_path_types", Sr.TrafficEngineering.CandidatePathTypes))])
            self._leafs = OrderedDict([
                ('te_latency', (YLeaf(YType.empty, 'te-latency'), ['Empty'])),
                ('maximum_sid_depth', (YLeaf(YType.uint32, 'maximum-sid-depth'), ['int'])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.te_latency = None
            self.maximum_sid_depth = None
            self.enable = None

            self.out_of_resources = Sr.TrafficEngineering.OutOfResources()
            self.out_of_resources.parent = self
            self._children_name_map["out_of_resources"] = "out-of-resources"

            self.on_demand_colors = Sr.TrafficEngineering.OnDemandColors()
            self.on_demand_colors.parent = self
            self._children_name_map["on_demand_colors"] = "on-demand-colors"

            self.segments = Sr.TrafficEngineering.Segments()
            self.segments.parent = self
            self._children_name_map["segments"] = "segments"

            self.logging = Sr.TrafficEngineering.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"

            self.timers = Sr.TrafficEngineering.Timers()
            self.timers.parent = self
            self._children_name_map["timers"] = "timers"

            self.binding_sid_rules = Sr.TrafficEngineering.BindingSidRules()
            self.binding_sid_rules.parent = self
            self._children_name_map["binding_sid_rules"] = "binding-sid-rules"

            self.policies = Sr.TrafficEngineering.Policies()
            self.policies.parent = self
            self._children_name_map["policies"] = "policies"

            self.srte_interfaces = Sr.TrafficEngineering.SrteInterfaces()
            self.srte_interfaces.parent = self
            self._children_name_map["srte_interfaces"] = "srte-interfaces"

            self.pcc = Sr.TrafficEngineering.Pcc()
            self.pcc.parent = self
            self._children_name_map["pcc"] = "pcc"

            self.affinity_maps = Sr.TrafficEngineering.AffinityMaps()
            self.affinity_maps.parent = self
            self._children_name_map["affinity_maps"] = "affinity-maps"

            self.candidate_path_types = Sr.TrafficEngineering.CandidatePathTypes()
            self.candidate_path_types.parent = self
            self._children_name_map["candidate_path_types"] = "candidate-path-types"
            self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sr.TrafficEngineering, ['te_latency', 'maximum_sid_depth', 'enable'], name, value)


        class OutOfResources(_Entity_):
            """
            SR\-TE out\-of\-resources handling configuration
            
            .. attribute:: maximum_paths_batch
            
            	Maximum total number of LSP path operations in a single batch
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            .. attribute:: maximum_paths
            
            	Maximum total number of LSP paths that can be created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.OutOfResources, self).__init__()

                self.yang_name = "out-of-resources"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('maximum_paths_batch', (YLeaf(YType.uint32, 'maximum-paths-batch'), ['int'])),
                    ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                ])
                self.maximum_paths_batch = None
                self.maximum_paths = None
                self._segment_path = lambda: "out-of-resources"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.OutOfResources, ['maximum_paths_batch', 'maximum_paths'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.OutOfResources']['meta_info']


        class OnDemandColors(_Entity_):
            """
            On\-demand color configuration
            
            .. attribute:: on_demand_color
            
            	On\-demand color configuration
            	**type**\: list of  		 :py:class:`OnDemandColor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.OnDemandColors, self).__init__()

                self.yang_name = "on-demand-colors"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("on-demand-color", ("on_demand_color", Sr.TrafficEngineering.OnDemandColors.OnDemandColor))])
                self._leafs = OrderedDict()

                self.on_demand_color = YList(self)
                self._segment_path = lambda: "on-demand-colors"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.OnDemandColors, [], name, value)


            class OnDemandColor(_Entity_):
                """
                On\-demand color configuration
                
                .. attribute:: color  (key)
                
                	Color
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: on_demand_color_dyn_mpls
                
                	Dynamic MPLS path properties
                	**type**\:  :py:class:`OnDemandColorDynMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls>`
                
                .. attribute:: bandwidth
                
                	The value of the bandwidth reserved by this policy in kbps
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: maximum_sid_depth
                
                	Maximum SID Depth Configuration
                	**type**\: int
                
                	**range:** 1..255
                
                .. attribute:: source_address
                
                	Source address of a candidate path. EndPointType , Source
                	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress>`
                
                	**presence node**\: True
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor, self).__init__()

                    self.yang_name = "on-demand-color"
                    self.yang_parent_name = "on-demand-colors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['color']
                    self._child_classes = OrderedDict([("on-demand-color-dyn-mpls", ("on_demand_color_dyn_mpls", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls)), ("source-address", ("source_address", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress))])
                    self._leafs = OrderedDict([
                        ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                        ('maximum_sid_depth', (YLeaf(YType.uint32, 'maximum-sid-depth'), ['int'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.color = None
                    self.bandwidth = None
                    self.maximum_sid_depth = None
                    self.enable = None

                    self.on_demand_color_dyn_mpls = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls()
                    self.on_demand_color_dyn_mpls.parent = self
                    self._children_name_map["on_demand_color_dyn_mpls"] = "on-demand-color-dyn-mpls"

                    self.source_address = None
                    self._children_name_map["source_address"] = "source-address"
                    self._segment_path = lambda: "on-demand-color" + "[color='" + str(self.color) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/on-demand-colors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor, ['color', 'bandwidth', 'maximum_sid_depth', 'enable'], name, value)


                class OnDemandColorDynMpls(_Entity_):
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
                    
                    .. attribute:: on_demand_color_dyn_mpls_flex_algorithm
                    
                    	Prefix\-SID algorithm
                    	**type**\: int
                    
                    	**range:** 128..255
                    
                    .. attribute:: enable
                    
                    	Dynamic MPLS path properties submode Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_rules
                    
                    	SR path computation and verification affinity rules
                    	**type**\:  :py:class:`AffinityRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls, self).__init__()

                        self.yang_name = "on-demand-color-dyn-mpls"
                        self.yang_parent_name = "on-demand-color"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("on-demand-color-dyn-mpls-metric", ("on_demand_color_dyn_mpls_metric", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric)), ("on-demand-color-dyn-mpls-pce", ("on_demand_color_dyn_mpls_pce", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce)), ("disjoint-path", ("disjoint_path", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath)), ("affinity-rules", ("affinity_rules", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules))])
                        self._leafs = OrderedDict([
                            ('on_demand_color_dyn_mpls_flex_algorithm', (YLeaf(YType.uint32, 'on-demand-color-dyn-mpls-flex-algorithm'), ['int'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.on_demand_color_dyn_mpls_flex_algorithm = None
                        self.enable = None

                        self.on_demand_color_dyn_mpls_metric = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric()
                        self.on_demand_color_dyn_mpls_metric.parent = self
                        self._children_name_map["on_demand_color_dyn_mpls_metric"] = "on-demand-color-dyn-mpls-metric"

                        self.on_demand_color_dyn_mpls_pce = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce()
                        self.on_demand_color_dyn_mpls_pce.parent = self
                        self._children_name_map["on_demand_color_dyn_mpls_pce"] = "on-demand-color-dyn-mpls-pce"

                        self.disjoint_path = None
                        self._children_name_map["disjoint_path"] = "disjoint-path"

                        self.affinity_rules = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules()
                        self.affinity_rules.parent = self
                        self._children_name_map["affinity_rules"] = "affinity-rules"
                        self._segment_path = lambda: "on-demand-color-dyn-mpls"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls, ['on_demand_color_dyn_mpls_flex_algorithm', 'enable'], name, value)


                    class OnDemandColorDynMplsMetric(_Entity_):
                        """
                        Metric type
                        
                        .. attribute:: metric_type
                        
                        	Metric Type
                        	**type**\:  :py:class:`XtcMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetric>`
                        
                        .. attribute:: enable
                        
                        	Metric submode Enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: metric_margin
                        
                        	Metric Margin
                        	**type**\:  :py:class:`MetricMargin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric, self).__init__()

                            self.yang_name = "on-demand-color-dyn-mpls-metric"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("metric-margin", ("metric_margin", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin))])
                            self._leafs = OrderedDict([
                                ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetric', '')])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.metric_type = None
                            self.enable = None

                            self.metric_margin = Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin()
                            self.metric_margin.parent = self
                            self._children_name_map["metric_margin"] = "metric-margin"
                            self._segment_path = lambda: "on-demand-color-dyn-mpls-metric"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric, ['metric_type', 'enable'], name, value)


                        class MetricMargin(_Entity_):
                            """
                            Metric Margin
                            
                            .. attribute:: value_type
                            
                            	Metric margin type
                            	**type**\:  :py:class:`XtcMetricValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetricValue>`
                            
                            .. attribute:: absolute_value
                            
                            	Absolute metric value
                            	**type**\: int
                            
                            	**range:** 0..2147483647
                            
                            .. attribute:: relative_value
                            
                            	Relative metric value
                            	**type**\: int
                            
                            	**range:** 0..2147483647
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-cfg'
                            _revision = '2019-09-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin, self).__init__()

                                self.yang_name = "metric-margin"
                                self.yang_parent_name = "on-demand-color-dyn-mpls-metric"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('value_type', (YLeaf(YType.enumeration, 'value-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetricValue', '')])),
                                    ('absolute_value', (YLeaf(YType.uint32, 'absolute-value'), ['int'])),
                                    ('relative_value', (YLeaf(YType.uint32, 'relative-value'), ['int'])),
                                ])
                                self.value_type = None
                                self.absolute_value = None
                                self.relative_value = None
                                self._segment_path = lambda: "metric-margin"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin, ['value_type', 'absolute_value', 'relative_value'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric']['meta_info']


                    class OnDemandColorDynMplsPce(_Entity_):
                        """
                        Use Path Computation Element
                        
                        .. attribute:: enable
                        
                        	PCE submode Enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce, self).__init__()

                            self.yang_name = "on-demand-color-dyn-mpls-pce"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "on-demand-color-dyn-mpls-pce"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce, ['enable'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce']['meta_info']


                    class DisjointPath(_Entity_):
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
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath, self).__init__()

                            self.yang_name = "disjoint-path"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                                ('disjointness_type', (YLeaf(YType.enumeration, 'disjointness-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcDisjointness', '')])),
                                ('sub_id', (YLeaf(YType.uint32, 'sub-id'), ['int'])),
                            ])
                            self.group_id = None
                            self.disjointness_type = None
                            self.sub_id = None
                            self._segment_path = lambda: "disjoint-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath, ['group_id', 'disjointness_type', 'sub_id'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath']['meta_info']


                    class AffinityRules(_Entity_):
                        """
                        SR path computation and verification affinity
                        rules
                        
                        .. attribute:: affinity_rule
                        
                        	SR path computation and verification affinity rule
                        	**type**\: list of  		 :py:class:`AffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules, self).__init__()

                            self.yang_name = "affinity-rules"
                            self.yang_parent_name = "on-demand-color-dyn-mpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("affinity-rule", ("affinity_rule", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule))])
                            self._leafs = OrderedDict()

                            self.affinity_rule = YList(self)
                            self._segment_path = lambda: "affinity-rules"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules, [], name, value)


                        class AffinityRule(_Entity_):
                            """
                            SR path computation and verification affinity
                            rule
                            
                            .. attribute:: rule  (key)
                            
                            	Affinity rule type
                            	**type**\:  :py:class:`XtcAffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcAffinityRule>`
                            
                            .. attribute:: affinity_name
                            
                            	Affinity rule name
                            	**type**\: list of  		 :py:class:`AffinityName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-cfg'
                            _revision = '2019-09-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule, self).__init__()

                                self.yang_name = "affinity-rule"
                                self.yang_parent_name = "affinity-rules"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rule']
                                self._child_classes = OrderedDict([("affinity-name", ("affinity_name", Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName))])
                                self._leafs = OrderedDict([
                                    ('rule', (YLeaf(YType.enumeration, 'rule'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAffinityRule', '')])),
                                ])
                                self.rule = None

                                self.affinity_name = YList(self)
                                self._segment_path = lambda: "affinity-rule" + "[rule='" + str(self.rule) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule, ['rule'], name, value)


                            class AffinityName(_Entity_):
                                """
                                Affinity rule name
                                
                                .. attribute:: affinity_name  (key)
                                
                                	Affinity name
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-cfg'
                                _revision = '2019-09-05'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName, self).__init__()

                                    self.yang_name = "affinity-name"
                                    self.yang_parent_name = "affinity-rule"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['affinity_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('affinity_name', (YLeaf(YType.str, 'affinity-name'), ['str'])),
                                    ])
                                    self.affinity_name = None
                                    self._segment_path = lambda: "affinity-name" + "[affinity-name='" + str(self.affinity_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName, ['affinity_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                    return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info']


                class SourceAddress(_Entity_):
                    """
                    Source address of a candidate path. EndPointType
                    , Source
                    
                    .. attribute:: ip_address_type
                    
                    	IP address type
                    	**type**\:  :py:class:`XtcEndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcEndPoint>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress, self).__init__()

                        self.yang_name = "source-address"
                        self.yang_parent_name = "on-demand-color"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('ip_address_type', (YLeaf(YType.enumeration, 'ip-address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint', '')])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                        ])
                        self.ip_address_type = None
                        self.source_address = None
                        self._segment_path = lambda: "source-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress, ['ip_address_type', 'source_address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.OnDemandColors']['meta_info']


        class Segments(_Entity_):
            """
            Segment\-lists configuration
            
            .. attribute:: segment
            
            	Segment\-list configuration
            	**type**\: list of  		 :py:class:`Segment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments.Segment>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.Segments, self).__init__()

                self.yang_name = "segments"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("segment", ("segment", Sr.TrafficEngineering.Segments.Segment))])
                self._leafs = OrderedDict()

                self.segment = YList(self)
                self._segment_path = lambda: "segments"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Segments, [], name, value)


            class Segment(_Entity_):
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
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.Segments.Segment, self).__init__()

                    self.yang_name = "segment"
                    self.yang_parent_name = "segments"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['path_name']
                    self._child_classes = OrderedDict([("segments", ("segments", Sr.TrafficEngineering.Segments.Segment.Segments_))])
                    self._leafs = OrderedDict([
                        ('path_name', (YLeaf(YType.str, 'path-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.path_name = None
                    self.enable = None

                    self.segments = Sr.TrafficEngineering.Segments.Segment.Segments_()
                    self.segments.parent = self
                    self._children_name_map["segments"] = "segments"
                    self._segment_path = lambda: "segment" + "[path-name='" + str(self.path_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/segments/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Segments.Segment, ['path_name', 'enable'], name, value)


                class Segments_(_Entity_):
                    """
                    Segments/hops configuration for given
                    Segment\-list
                    
                    .. attribute:: segment
                    
                    	Configure Segment/hop at the index
                    	**type**\: list of  		 :py:class:`Segment_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Segments.Segment.Segments_, self).__init__()

                        self.yang_name = "segments"
                        self.yang_parent_name = "segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("segment", ("segment", Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_))])
                        self._leafs = OrderedDict()

                        self.segment = YList(self)
                        self._segment_path = lambda: "segments"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Segments.Segment.Segments_, [], name, value)


                    class Segment_(_Entity_):
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
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_, self).__init__()

                            self.yang_name = "segment"
                            self.yang_parent_name = "segments"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['segment_index']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('segment_index', (YLeaf(YType.uint32, 'segment-index'), ['int'])),
                                ('segment_type', (YLeaf(YType.enumeration, 'segment-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSegment', '')])),
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.segment_index = None
                            self.segment_type = None
                            self.address = None
                            self.mpls_label = None
                            self._segment_path = lambda: "segment" + "[segment-index='" + str(self.segment_index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_, ['segment_index', 'segment_type', 'address', 'mpls_label'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Segments.Segment.Segments_']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.Segments.Segment']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.Segments']['meta_info']


        class Logging(_Entity_):
            """
            Logging configuration
            
            .. attribute:: pcep_peer_status
            
            	Enable logging for pcep peer status
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: policy_status
            
            	Enable logging for policy status
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pcep_peer_status', (YLeaf(YType.empty, 'pcep-peer-status'), ['Empty'])),
                    ('policy_status', (YLeaf(YType.empty, 'policy-status'), ['Empty'])),
                ])
                self.pcep_peer_status = None
                self.policy_status = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Logging, ['pcep_peer_status', 'policy_status'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.Logging']['meta_info']


        class Timers(_Entity_):
            """
            SR\-TE timers configuration
            
            .. attribute:: candidate_path_cleanup_delay
            
            	Delay before cleaning up candidate paths
            	**type**\: int
            
            	**range:** 0..86400
            
            	**default value**\: 120
            
            .. attribute:: initial_verify_restart
            
            	Timer to wait for topology convergence after topology starts populating for restart case
            	**type**\: int
            
            	**range:** 10..10000
            
            	**default value**\: 40
            
            .. attribute:: initial_verify_switchover
            
            	Timer to wait for topology convergence after topology starts populating for switchover case
            	**type**\: int
            
            	**range:** 10..10000
            
            	**default value**\: 60
            
            .. attribute:: initial_verify_startup
            
            	Timer to wait for topology convergence after topology starts populating for startup case
            	**type**\: int
            
            	**range:** 10..10000
            
            	**default value**\: 300
            
            .. attribute:: cleanup_delay
            
            	Delay before cleaning up previous path
            	**type**\: int
            
            	**range:** 0..300
            
            	**default value**\: 10
            
            .. attribute:: install_delay
            
            	Delay before switching to a reoptimized path
            	**type**\: int
            
            	**range:** 0..300
            
            	**default value**\: 10
            
            .. attribute:: periodic_reoptimization
            
            	How often to perform periodic reoptimization of policies
            	**type**\: int
            
            	**range:** 0..86400
            
            	**default value**\: 600
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.Timers, self).__init__()

                self.yang_name = "timers"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('candidate_path_cleanup_delay', (YLeaf(YType.uint32, 'candidate-path-cleanup-delay'), ['int'])),
                    ('initial_verify_restart', (YLeaf(YType.uint32, 'initial-verify-restart'), ['int'])),
                    ('initial_verify_switchover', (YLeaf(YType.uint32, 'initial-verify-switchover'), ['int'])),
                    ('initial_verify_startup', (YLeaf(YType.uint32, 'initial-verify-startup'), ['int'])),
                    ('cleanup_delay', (YLeaf(YType.uint32, 'cleanup-delay'), ['int'])),
                    ('install_delay', (YLeaf(YType.uint32, 'install-delay'), ['int'])),
                    ('periodic_reoptimization', (YLeaf(YType.uint32, 'periodic-reoptimization'), ['int'])),
                ])
                self.candidate_path_cleanup_delay = None
                self.initial_verify_restart = None
                self.initial_verify_switchover = None
                self.initial_verify_startup = None
                self.cleanup_delay = None
                self.install_delay = None
                self.periodic_reoptimization = None
                self._segment_path = lambda: "timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Timers, ['candidate_path_cleanup_delay', 'initial_verify_restart', 'initial_verify_switchover', 'initial_verify_startup', 'cleanup_delay', 'install_delay', 'periodic_reoptimization'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.Timers']['meta_info']


        class BindingSidRules(_Entity_):
            """
            Binding sid rules
            
            .. attribute:: explicit
            
            	Binding sid explicit options
            	**type**\:  :py:class:`Explicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.BindingSidRules.Explicit>`
            
            	**presence node**\: True
            
            .. attribute:: dynamic_binding_sid_rules
            
            	Dynamic binding SID options
            	**type**\:  :py:class:`DynamicBindingSidRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.BindingSidRules, self).__init__()

                self.yang_name = "binding-sid-rules"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("explicit", ("explicit", Sr.TrafficEngineering.BindingSidRules.Explicit)), ("dynamic-binding-sid-rules", ("dynamic_binding_sid_rules", Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules))])
                self._leafs = OrderedDict()

                self.explicit = None
                self._children_name_map["explicit"] = "explicit"

                self.dynamic_binding_sid_rules = None
                self._children_name_map["dynamic_binding_sid_rules"] = "dynamic-binding-sid-rules"
                self._segment_path = lambda: "binding-sid-rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.BindingSidRules, [], name, value)


            class Explicit(_Entity_):
                """
                Binding sid explicit options
                
                .. attribute:: rule
                
                	Binding sid explicit rule
                	**type**\:  :py:class:`XtcBindingSidexplicitRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcBindingSidexplicitRule>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.BindingSidRules.Explicit, self).__init__()

                    self.yang_name = "explicit"
                    self.yang_parent_name = "binding-sid-rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('rule', (YLeaf(YType.enumeration, 'rule'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidexplicitRule', '')])),
                    ])
                    self.rule = None
                    self._segment_path = lambda: "explicit"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/binding-sid-rules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.BindingSidRules.Explicit, ['rule'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.BindingSidRules.Explicit']['meta_info']


            class DynamicBindingSidRules(_Entity_):
                """
                Dynamic binding SID options
                
                .. attribute:: dynamic_binding_sid_rule
                
                	Binding SID dynamic rule
                	**type**\:  :py:class:`XtcBindingSidDynamicRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcBindingSidDynamicRule>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules, self).__init__()

                    self.yang_name = "dynamic-binding-sid-rules"
                    self.yang_parent_name = "binding-sid-rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('dynamic_binding_sid_rule', (YLeaf(YType.enumeration, 'dynamic-binding-sid-rule'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidDynamicRule', '')])),
                    ])
                    self.dynamic_binding_sid_rule = None
                    self._segment_path = lambda: "dynamic-binding-sid-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/binding-sid-rules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules, ['dynamic_binding_sid_rule'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.BindingSidRules']['meta_info']


        class Policies(_Entity_):
            """
            Policy configuration
            
            .. attribute:: policy
            
            	Policy configuration
            	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.Policies, self).__init__()

                self.yang_name = "policies"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy", ("policy", Sr.TrafficEngineering.Policies.Policy))])
                self._leafs = OrderedDict()

                self.policy = YList(self)
                self._segment_path = lambda: "policies"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Policies, [], name, value)


            class Policy(_Entity_):
                """
                Policy configuration
                
                .. attribute:: policy_name  (key)
                
                	Policy name
                	**type**\: str
                
                	**length:** 1..59
                
                .. attribute:: steering
                
                	Steering options for the policy
                	**type**\:  :py:class:`Steering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.Steering>`
                
                .. attribute:: binding_sid
                
                	Binding Segment ID
                	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.BindingSid>`
                
                .. attribute:: policy_color_endpoint
                
                	Color and endpoint of a policyColor, EndPointType, Endpoint
                	**type**\:  :py:class:`PolicyColorEndpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint>`
                
                	**presence node**\: True
                
                .. attribute:: auto_route
                
                	Autoroute configuration
                	**type**\:  :py:class:`AutoRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.AutoRoute>`
                
                .. attribute:: candidate_paths
                
                	Policy candidate\-paths configuration
                	**type**\:  :py:class:`CandidatePaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths>`
                
                .. attribute:: ipv6_disable
                
                	IPv6 disable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: shutdown
                
                	Administratively shutdown policy
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bandwidth
                
                	The value of the bandwidth reserved by this policy in kbps
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: source_address
                
                	Source address of a candidate path. EndPointType , Source
                	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.SourceAddress>`
                
                	**presence node**\: True
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.Policies.Policy, self).__init__()

                    self.yang_name = "policy"
                    self.yang_parent_name = "policies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['policy_name']
                    self._child_classes = OrderedDict([("steering", ("steering", Sr.TrafficEngineering.Policies.Policy.Steering)), ("binding-sid", ("binding_sid", Sr.TrafficEngineering.Policies.Policy.BindingSid)), ("policy-color-endpoint", ("policy_color_endpoint", Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint)), ("auto-route", ("auto_route", Sr.TrafficEngineering.Policies.Policy.AutoRoute)), ("candidate-paths", ("candidate_paths", Sr.TrafficEngineering.Policies.Policy.CandidatePaths)), ("source-address", ("source_address", Sr.TrafficEngineering.Policies.Policy.SourceAddress))])
                    self._leafs = OrderedDict([
                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                        ('ipv6_disable', (YLeaf(YType.empty, 'ipv6-disable'), ['Empty'])),
                        ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.policy_name = None
                    self.ipv6_disable = None
                    self.shutdown = None
                    self.bandwidth = None
                    self.enable = None

                    self.steering = Sr.TrafficEngineering.Policies.Policy.Steering()
                    self.steering.parent = self
                    self._children_name_map["steering"] = "steering"

                    self.binding_sid = Sr.TrafficEngineering.Policies.Policy.BindingSid()
                    self.binding_sid.parent = self
                    self._children_name_map["binding_sid"] = "binding-sid"

                    self.policy_color_endpoint = None
                    self._children_name_map["policy_color_endpoint"] = "policy-color-endpoint"

                    self.auto_route = Sr.TrafficEngineering.Policies.Policy.AutoRoute()
                    self.auto_route.parent = self
                    self._children_name_map["auto_route"] = "auto-route"

                    self.candidate_paths = Sr.TrafficEngineering.Policies.Policy.CandidatePaths()
                    self.candidate_paths.parent = self
                    self._children_name_map["candidate_paths"] = "candidate-paths"

                    self.source_address = None
                    self._children_name_map["source_address"] = "source-address"
                    self._segment_path = lambda: "policy" + "[policy-name='" + str(self.policy_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/policies/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy, ['policy_name', 'ipv6_disable', 'shutdown', 'bandwidth', 'enable'], name, value)


                class Steering(_Entity_):
                    """
                    Steering options for the policy
                    
                    .. attribute:: applications
                    
                    	Application table that steering options need to be applied
                    	**type**\:  :py:class:`Applications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.Steering.Applications>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.Steering, self).__init__()

                        self.yang_name = "steering"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("applications", ("applications", Sr.TrafficEngineering.Policies.Policy.Steering.Applications))])
                        self._leafs = OrderedDict()

                        self.applications = Sr.TrafficEngineering.Policies.Policy.Steering.Applications()
                        self.applications.parent = self
                        self._children_name_map["applications"] = "applications"
                        self._segment_path = lambda: "steering"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.Steering, [], name, value)


                    class Applications(_Entity_):
                        """
                        Application table that steering options need
                        to be applied
                        
                        .. attribute:: application
                        
                        	Application that steering options need to be applied
                        	**type**\: list of  		 :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Policies.Policy.Steering.Applications, self).__init__()

                            self.yang_name = "applications"
                            self.yang_parent_name = "steering"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("application", ("application", Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application))])
                            self._leafs = OrderedDict()

                            self.application = YList(self)
                            self._segment_path = lambda: "applications"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.Steering.Applications, [], name, value)


                        class Application(_Entity_):
                            """
                            Application that steering options need to
                            be applied
                            
                            .. attribute:: application  (key)
                            
                            	Steering application
                            	**type**\:  :py:class:`XtcSteeringApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcSteeringApplication>`
                            
                            .. attribute:: disable
                            
                            	Disable all steering services
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-cfg'
                            _revision = '2019-09-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application, self).__init__()

                                self.yang_name = "application"
                                self.yang_parent_name = "applications"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['application']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('application', (YLeaf(YType.enumeration, 'application'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSteeringApplication', '')])),
                                    ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                                ])
                                self.application = None
                                self.disable = None
                                self._segment_path = lambda: "application" + "[application='" + str(self.application) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application, ['application', 'disable'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.Steering.Applications']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.Steering']['meta_info']


                class BindingSid(_Entity_):
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
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.BindingSid, self).__init__()

                        self.yang_name = "binding-sid"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('binding_sid_type', (YLeaf(YType.enumeration, 'binding-sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                        ])
                        self.binding_sid_type = None
                        self.mpls_label = None
                        self._segment_path = lambda: "binding-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.BindingSid, ['binding_sid_type', 'mpls_label'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.BindingSid']['meta_info']


                class PolicyColorEndpoint(_Entity_):
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
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint, self).__init__()

                        self.yang_name = "policy-color-endpoint"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                            ('end_point_type', (YLeaf(YType.enumeration, 'end-point-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint', '')])),
                            ('end_point_address', (YLeaf(YType.str, 'end-point-address'), ['str','str'])),
                        ])
                        self.color = None
                        self.end_point_type = None
                        self.end_point_address = None
                        self._segment_path = lambda: "policy-color-endpoint"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint, ['color', 'end_point_type', 'end_point_address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint']['meta_info']


                class AutoRoute(_Entity_):
                    """
                    Autoroute configuration
                    
                    .. attribute:: auto_route_metric
                    
                    	Autoroute metric
                    	**type**\:  :py:class:`AutoRouteMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric>`
                    
                    .. attribute:: include_prefixes
                    
                    	Autoroute include prefix table configuration
                    	**type**\:  :py:class:`IncludePrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes>`
                    
                    .. attribute:: force_sr_include
                    
                    	Force autoroute policy to be safe for carrying SR labelled traffic
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: forward_class
                    
                    	Forward class associated with the policy
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.AutoRoute, self).__init__()

                        self.yang_name = "auto-route"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auto-route-metric", ("auto_route_metric", Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric)), ("include-prefixes", ("include_prefixes", Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes))])
                        self._leafs = OrderedDict([
                            ('force_sr_include', (YLeaf(YType.empty, 'force-sr-include'), ['Empty'])),
                            ('forward_class', (YLeaf(YType.uint32, 'forward-class'), ['int'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.force_sr_include = None
                        self.forward_class = None
                        self.enable = None

                        self.auto_route_metric = Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric()
                        self.auto_route_metric.parent = self
                        self._children_name_map["auto_route_metric"] = "auto-route-metric"

                        self.include_prefixes = Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes()
                        self.include_prefixes.parent = self
                        self._children_name_map["include_prefixes"] = "include-prefixes"
                        self._segment_path = lambda: "auto-route"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.AutoRoute, ['force_sr_include', 'forward_class', 'enable'], name, value)


                    class AutoRouteMetric(_Entity_):
                        """
                        Autoroute metric
                        
                        .. attribute:: autoroute_metric_type
                        
                        	Metric type
                        	**type**\:  :py:class:`XtcAutoRouteMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcAutoRouteMetric>`
                        
                        .. attribute:: metric_relative_value
                        
                        	Autoroute relative metric
                        	**type**\: int
                        
                        	**range:** \-10..10
                        
                        .. attribute:: metric_constant_value
                        
                        	Autoroute constant metric
                        	**type**\: int
                        
                        	**range:** 1..2147483647
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric, self).__init__()

                            self.yang_name = "auto-route-metric"
                            self.yang_parent_name = "auto-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('autoroute_metric_type', (YLeaf(YType.enumeration, 'autoroute-metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAutoRouteMetric', '')])),
                                ('metric_relative_value', (YLeaf(YType.int32, 'metric-relative-value'), ['int'])),
                                ('metric_constant_value', (YLeaf(YType.uint32, 'metric-constant-value'), ['int'])),
                            ])
                            self.autoroute_metric_type = None
                            self.metric_relative_value = None
                            self.metric_constant_value = None
                            self._segment_path = lambda: "auto-route-metric"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric, ['autoroute_metric_type', 'metric_relative_value', 'metric_constant_value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric']['meta_info']


                    class IncludePrefixes(_Entity_):
                        """
                        Autoroute include prefix table configuration
                        
                        .. attribute:: include_prefix
                        
                        	Autoroute IP prefix to include
                        	**type**\: list of  		 :py:class:`IncludePrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes, self).__init__()

                            self.yang_name = "include-prefixes"
                            self.yang_parent_name = "auto-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("include-prefix", ("include_prefix", Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix))])
                            self._leafs = OrderedDict()

                            self.include_prefix = YList(self)
                            self._segment_path = lambda: "include-prefixes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes, [], name, value)


                        class IncludePrefix(_Entity_):
                            """
                            Autoroute IP prefix to include
                            
                            .. attribute:: af_type  (key)
                            
                            	Address family type
                            	**type**\:  :py:class:`XtcAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcAddressFamily>`
                            
                            .. attribute:: prefix_address  (key)
                            
                            	Autoroute prefix IP address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Autoroute IP prefix length
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-cfg'
                            _revision = '2019-09-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix, self).__init__()

                                self.yang_name = "include-prefix"
                                self.yang_parent_name = "include-prefixes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['af_type','prefix_address','prefix_length']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_type', (YLeaf(YType.enumeration, 'af-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAddressFamily', '')])),
                                    ('prefix_address', (YLeaf(YType.str, 'prefix-address'), ['str','str'])),
                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ])
                                self.af_type = None
                                self.prefix_address = None
                                self.prefix_length = None
                                self._segment_path = lambda: "include-prefix" + "[af-type='" + str(self.af_type) + "']" + "[prefix-address='" + str(self.prefix_address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix, ['af_type', 'prefix_address', 'prefix_length'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute']['meta_info']


                class CandidatePaths(_Entity_):
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
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths, self).__init__()

                        self.yang_name = "candidate-paths"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("preferences", ("preferences", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences))])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.enable = None

                        self.preferences = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences()
                        self.preferences.parent = self
                        self._children_name_map["preferences"] = "preferences"
                        self._segment_path = lambda: "candidate-paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths, ['enable'], name, value)


                    class Preferences(_Entity_):
                        """
                        Policy path\-option preference table
                        
                        .. attribute:: preference
                        
                        	Policy path\-option preference entry
                        	**type**\: list of  		 :py:class:`Preference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences, self).__init__()

                            self.yang_name = "preferences"
                            self.yang_parent_name = "candidate-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("preference", ("preference", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference))])
                            self._leafs = OrderedDict()

                            self.preference = YList(self)
                            self._segment_path = lambda: "preferences"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences, [], name, value)


                        class Preference(_Entity_):
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
                            _revision = '2019-09-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference, self).__init__()

                                self.yang_name = "preference"
                                self.yang_parent_name = "preferences"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['path_index']
                                self._child_classes = OrderedDict([("constraints", ("constraints", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints)), ("path-infos", ("path_infos", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos))])
                                self._leafs = OrderedDict([
                                    ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ])
                                self.path_index = None
                                self.enable = None

                                self.constraints = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints()
                                self.constraints.parent = self
                                self._children_name_map["constraints"] = "constraints"

                                self.path_infos = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos()
                                self.path_infos.parent = self
                                self._children_name_map["path_infos"] = "path-infos"
                                self._segment_path = lambda: "preference" + "[path-index='" + str(self.path_index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference, ['path_index', 'enable'], name, value)


                            class Constraints(_Entity_):
                                """
                                SR path computation and verification
                                constraints
                                
                                .. attribute:: disjoint_path
                                
                                	Disjoint path
                                	**type**\:  :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: segment_rules
                                
                                	SR path computation segment specific rules
                                	**type**\:  :py:class:`SegmentRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: affinity_rules
                                
                                	SR path computation and verification affinity rules
                                	**type**\:  :py:class:`AffinityRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules>`
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-cfg'
                                _revision = '2019-09-05'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints, self).__init__()

                                    self.yang_name = "constraints"
                                    self.yang_parent_name = "preference"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("disjoint-path", ("disjoint_path", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath)), ("segment-rules", ("segment_rules", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules)), ("affinity-rules", ("affinity_rules", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules))])
                                    self._leafs = OrderedDict()

                                    self.disjoint_path = None
                                    self._children_name_map["disjoint_path"] = "disjoint-path"

                                    self.segment_rules = None
                                    self._children_name_map["segment_rules"] = "segment-rules"

                                    self.affinity_rules = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules()
                                    self.affinity_rules.parent = self
                                    self._children_name_map["affinity_rules"] = "affinity-rules"
                                    self._segment_path = lambda: "constraints"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints, [], name, value)


                                class DisjointPath(_Entity_):
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
                                    _revision = '2019-09-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath, self).__init__()

                                        self.yang_name = "disjoint-path"
                                        self.yang_parent_name = "constraints"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                                            ('disjointness_type', (YLeaf(YType.enumeration, 'disjointness-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcDisjointness', '')])),
                                            ('sub_id', (YLeaf(YType.uint32, 'sub-id'), ['int'])),
                                        ])
                                        self.group_id = None
                                        self.disjointness_type = None
                                        self.sub_id = None
                                        self._segment_path = lambda: "disjoint-path"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath, ['group_id', 'disjointness_type', 'sub_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath']['meta_info']


                                class SegmentRules(_Entity_):
                                    """
                                    SR path computation segment specific
                                    rules
                                    
                                    .. attribute:: sid_algorithm
                                    
                                    	Prefix\-SID algorithm
                                    	**type**\: int
                                    
                                    	**range:** 128..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'infra-xtc-agent-cfg'
                                    _revision = '2019-09-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules, self).__init__()

                                        self.yang_name = "segment-rules"
                                        self.yang_parent_name = "constraints"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('sid_algorithm', (YLeaf(YType.uint32, 'sid-algorithm'), ['int'])),
                                        ])
                                        self.sid_algorithm = None
                                        self._segment_path = lambda: "segment-rules"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules, ['sid_algorithm'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules']['meta_info']


                                class AffinityRules(_Entity_):
                                    """
                                    SR path computation and verification affinity
                                    rules
                                    
                                    .. attribute:: affinity_rule
                                    
                                    	SR path computation and verification affinity rule
                                    	**type**\: list of  		 :py:class:`AffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-agent-cfg'
                                    _revision = '2019-09-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules, self).__init__()

                                        self.yang_name = "affinity-rules"
                                        self.yang_parent_name = "constraints"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("affinity-rule", ("affinity_rule", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule))])
                                        self._leafs = OrderedDict()

                                        self.affinity_rule = YList(self)
                                        self._segment_path = lambda: "affinity-rules"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules, [], name, value)


                                    class AffinityRule(_Entity_):
                                        """
                                        SR path computation and verification affinity
                                        rule
                                        
                                        .. attribute:: rule  (key)
                                        
                                        	Affinity rule type
                                        	**type**\:  :py:class:`XtcAffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcAffinityRule>`
                                        
                                        .. attribute:: affinity_name
                                        
                                        	Affinity rule name
                                        	**type**\: list of  		 :py:class:`AffinityName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2019-09-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule, self).__init__()

                                            self.yang_name = "affinity-rule"
                                            self.yang_parent_name = "affinity-rules"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['rule']
                                            self._child_classes = OrderedDict([("affinity-name", ("affinity_name", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName))])
                                            self._leafs = OrderedDict([
                                                ('rule', (YLeaf(YType.enumeration, 'rule'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAffinityRule', '')])),
                                            ])
                                            self.rule = None

                                            self.affinity_name = YList(self)
                                            self._segment_path = lambda: "affinity-rule" + "[rule='" + str(self.rule) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule, ['rule'], name, value)


                                        class AffinityName(_Entity_):
                                            """
                                            Affinity rule name
                                            
                                            .. attribute:: affinity_name  (key)
                                            
                                            	Affinity name
                                            	**type**\: str
                                            
                                            	**length:** 1..32
                                            
                                            

                                            """

                                            _prefix = 'infra-xtc-agent-cfg'
                                            _revision = '2019-09-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName, self).__init__()

                                                self.yang_name = "affinity-name"
                                                self.yang_parent_name = "affinity-rule"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['affinity_name']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('affinity_name', (YLeaf(YType.str, 'affinity-name'), ['str'])),
                                                ])
                                                self.affinity_name = None
                                                self._segment_path = lambda: "affinity-name" + "[affinity-name='" + str(self.affinity_name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName, ['affinity_name'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                                return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                    return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints']['meta_info']


                            class PathInfos(_Entity_):
                                """
                                Policy path\-option preference
                                configuration
                                
                                .. attribute:: path_info
                                
                                	Policy configuration
                                	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo>`
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-cfg'
                                _revision = '2019-09-05'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, self).__init__()

                                    self.yang_name = "path-infos"
                                    self.yang_parent_name = "preference"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path-info", ("path_info", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo))])
                                    self._leafs = OrderedDict()

                                    self.path_info = YList(self)
                                    self._segment_path = lambda: "path-infos"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, [], name, value)


                                class PathInfo(_Entity_):
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
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration, valid only for dynamic path\-options
                                    	**type**\:  :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric>`
                                    
                                    .. attribute:: pcep
                                    
                                    	Path Computation Element Protocol
                                    	**type**\:  :py:class:`Pcep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep>`
                                    
                                    .. attribute:: weight
                                    
                                    	Path\-option weight
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: enable
                                    
                                    	True only
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-agent-cfg'
                                    _revision = '2019-09-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, self).__init__()

                                        self.yang_name = "path-info"
                                        self.yang_parent_name = "path-infos"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['type','hop_type','segment_list_name']
                                        self._child_classes = OrderedDict([("metric", ("metric", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric)), ("pcep", ("pcep", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPath', '')])),
                                            ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPathHop', '')])),
                                            ('segment_list_name', (YLeaf(YType.str, 'segment-list-name'), ['str'])),
                                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                        ])
                                        self.type = None
                                        self.hop_type = None
                                        self.segment_list_name = None
                                        self.weight = None
                                        self.enable = None

                                        self.metric = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric()
                                        self.metric.parent = self
                                        self._children_name_map["metric"] = "metric"

                                        self.pcep = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep()
                                        self.pcep.parent = self
                                        self._children_name_map["pcep"] = "pcep"
                                        self._segment_path = lambda: "path-info" + "[type='" + str(self.type) + "']" + "[hop-type='" + str(self.hop_type) + "']" + "[segment-list-name='" + str(self.segment_list_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, ['type', 'hop_type', 'segment_list_name', 'weight', 'enable'], name, value)


                                    class Metric(_Entity_):
                                        """
                                        Metric configuration, valid only for
                                        dynamic path\-options
                                        
                                        .. attribute:: sid_limit
                                        
                                        	Maximum number of SIDs
                                        	**type**\: int
                                        
                                        	**range:** 1..255
                                        
                                        .. attribute:: metric_type
                                        
                                        	Metric type
                                        	**type**\:  :py:class:`XtcMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetric>`
                                        
                                        .. attribute:: enable
                                        
                                        	True only
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: metric_margin
                                        
                                        	Metric Margin
                                        	**type**\:  :py:class:`MetricMargin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2019-09-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "path-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("metric-margin", ("metric_margin", Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin))])
                                            self._leafs = OrderedDict([
                                                ('sid_limit', (YLeaf(YType.uint32, 'sid-limit'), ['int'])),
                                                ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetric', '')])),
                                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                            ])
                                            self.sid_limit = None
                                            self.metric_type = None
                                            self.enable = None

                                            self.metric_margin = Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin()
                                            self.metric_margin.parent = self
                                            self._children_name_map["metric_margin"] = "metric-margin"
                                            self._segment_path = lambda: "metric"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, ['sid_limit', 'metric_type', 'enable'], name, value)


                                        class MetricMargin(_Entity_):
                                            """
                                            Metric Margin
                                            
                                            .. attribute:: value_type
                                            
                                            	Metric margin type
                                            	**type**\:  :py:class:`XtcMetricValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcMetricValue>`
                                            
                                            .. attribute:: absolute_value
                                            
                                            	Absolute metric value
                                            	**type**\: int
                                            
                                            	**range:** 0..2147483647
                                            
                                            .. attribute:: relative_value
                                            
                                            	Relative metric value
                                            	**type**\: int
                                            
                                            	**range:** 0..2147483647
                                            
                                            

                                            """

                                            _prefix = 'infra-xtc-agent-cfg'
                                            _revision = '2019-09-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin, self).__init__()

                                                self.yang_name = "metric-margin"
                                                self.yang_parent_name = "metric"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value_type', (YLeaf(YType.enumeration, 'value-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetricValue', '')])),
                                                    ('absolute_value', (YLeaf(YType.uint32, 'absolute-value'), ['int'])),
                                                    ('relative_value', (YLeaf(YType.uint32, 'relative-value'), ['int'])),
                                                ])
                                                self.value_type = None
                                                self.absolute_value = None
                                                self.relative_value = None
                                                self._segment_path = lambda: "metric-margin"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin, ['value_type', 'absolute_value', 'relative_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                                return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric']['meta_info']


                                    class Pcep(_Entity_):
                                        """
                                        Path Computation Element Protocol
                                        
                                        .. attribute:: enable
                                        
                                        	True only
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-agent-cfg'
                                        _revision = '2019-09-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep, self).__init__()

                                            self.yang_name = "pcep"
                                            self.yang_parent_name = "path-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                            ])
                                            self.enable = None
                                            self._segment_path = lambda: "pcep"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep, ['enable'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                    return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                                return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths']['meta_info']


                class SourceAddress(_Entity_):
                    """
                    Source address of a candidate path. EndPointType
                    , Source
                    
                    .. attribute:: ip_address_type
                    
                    	IP address type
                    	**type**\:  :py:class:`XtcEndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcEndPoint>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Policies.Policy.SourceAddress, self).__init__()

                        self.yang_name = "source-address"
                        self.yang_parent_name = "policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('ip_address_type', (YLeaf(YType.enumeration, 'ip-address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint', '')])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                        ])
                        self.ip_address_type = None
                        self.source_address = None
                        self._segment_path = lambda: "source-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Policies.Policy.SourceAddress, ['ip_address_type', 'source_address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Policies.Policy.SourceAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.Policies']['meta_info']


        class SrteInterfaces(_Entity_):
            """
            SR\-TE interfaces
            
            .. attribute:: srte_interface
            
            	SR\-TE interface
            	**type**\: list of  		 :py:class:`SrteInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.SrteInterfaces, self).__init__()

                self.yang_name = "srte-interfaces"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("srte-interface", ("srte_interface", Sr.TrafficEngineering.SrteInterfaces.SrteInterface))])
                self._leafs = OrderedDict()

                self.srte_interface = YList(self)
                self._segment_path = lambda: "srte-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces, [], name, value)


            class SrteInterface(_Entity_):
                """
                SR\-TE interface
                
                .. attribute:: srte_interface_name  (key)
                
                	SR\-TE Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_affinities
                
                	Set user defined interface attribute flags
                	**type**\:  :py:class:`InterfaceAffinities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities>`
                
                .. attribute:: interface_metric
                
                	Interface TE metric configuration
                	**type**\: int
                
                	**range:** 0..2147483647
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface, self).__init__()

                    self.yang_name = "srte-interface"
                    self.yang_parent_name = "srte-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['srte_interface_name']
                    self._child_classes = OrderedDict([("interface-affinities", ("interface_affinities", Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities))])
                    self._leafs = OrderedDict([
                        ('srte_interface_name', (YLeaf(YType.str, 'srte-interface-name'), ['str'])),
                        ('interface_metric', (YLeaf(YType.uint32, 'interface-metric'), ['int'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.srte_interface_name = None
                    self.interface_metric = None
                    self.enable = None

                    self.interface_affinities = Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities()
                    self.interface_affinities.parent = self
                    self._children_name_map["interface_affinities"] = "interface-affinities"
                    self._segment_path = lambda: "srte-interface" + "[srte-interface-name='" + str(self.srte_interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/srte-interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface, ['srte_interface_name', 'interface_metric', 'enable'], name, value)


                class InterfaceAffinities(_Entity_):
                    """
                    Set user defined interface attribute flags
                    
                    .. attribute:: interface_affinity
                    
                    	Set user defined interface attribute flags
                    	**type**\: list of  		 :py:class:`InterfaceAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities, self).__init__()

                        self.yang_name = "interface-affinities"
                        self.yang_parent_name = "srte-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-affinity", ("interface_affinity", Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity))])
                        self._leafs = OrderedDict()

                        self.interface_affinity = YList(self)
                        self._segment_path = lambda: "interface-affinities"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities, [], name, value)


                    class InterfaceAffinity(_Entity_):
                        """
                        Set user defined interface attribute flags
                        
                        .. attribute:: affinity_name  (key)
                        
                        	Interface affinity names
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity, self).__init__()

                            self.yang_name = "interface-affinity"
                            self.yang_parent_name = "interface-affinities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['affinity_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('affinity_name', (YLeaf(YType.str, 'affinity-name'), ['str'])),
                            ])
                            self.affinity_name = None
                            self._segment_path = lambda: "interface-affinity" + "[affinity-name='" + str(self.affinity_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity, ['affinity_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.SrteInterfaces']['meta_info']


        class Pcc(_Entity_):
            """
            Path Computation Client
            
            .. attribute:: pce_peers
            
            	PCE peer configuration
            	**type**\:  :py:class:`PcePeers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PcePeers>`
            
            .. attribute:: profiles
            
            	Path profiles configuration
            	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.Profiles>`
            
            .. attribute:: dead_timer_interval
            
            	Amount of time after which the peer can declare this session down, if no PCEP message has been received
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: pcc_centric
            
            	Enable PCC centric model, where PCC only allows the lowest precedence PCE to initiate policies
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: report_all
            
            	Report all local SR policies to connected PCEP peers
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: keepalive_timer_interval
            
            	Maximum time between two consecutive PCEP messages sent by this node
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: initiated_state_interval
            
            	Amount of time a PCE Initiated policy can remain orphan
            	**type**\: int
            
            	**range:** 15..14400
            
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
            
            .. attribute:: initiated_orphan_interval
            
            	Amount of time that a policy will be owned by a PCE after that PCE has gone down
            	**type**\: int
            
            	**range:** 10..180
            
            .. attribute:: delegation_timeout
            
            	The maximum time delegated SR\-TE policies can remain up without an active connection to a PCE
            	**type**\: int
            
            	**range:** 0..3600
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.Pcc, self).__init__()

                self.yang_name = "pcc"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("pce-peers", ("pce_peers", Sr.TrafficEngineering.Pcc.PcePeers)), ("profiles", ("profiles", Sr.TrafficEngineering.Pcc.Profiles))])
                self._leafs = OrderedDict([
                    ('dead_timer_interval', (YLeaf(YType.uint32, 'dead-timer-interval'), ['int'])),
                    ('pcc_centric', (YLeaf(YType.empty, 'pcc-centric'), ['Empty'])),
                    ('report_all', (YLeaf(YType.empty, 'report-all'), ['Empty'])),
                    ('keepalive_timer_interval', (YLeaf(YType.uint32, 'keepalive-timer-interval'), ['int'])),
                    ('initiated_state_interval', (YLeaf(YType.uint32, 'initiated-state-interval'), ['int'])),
                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('initiated_orphan_interval', (YLeaf(YType.uint32, 'initiated-orphan-interval'), ['int'])),
                    ('delegation_timeout', (YLeaf(YType.uint32, 'delegation-timeout'), ['int'])),
                ])
                self.dead_timer_interval = None
                self.pcc_centric = None
                self.report_all = None
                self.keepalive_timer_interval = None
                self.initiated_state_interval = None
                self.source_address = None
                self.enable = None
                self.initiated_orphan_interval = None
                self.delegation_timeout = None

                self.pce_peers = Sr.TrafficEngineering.Pcc.PcePeers()
                self.pce_peers.parent = self
                self._children_name_map["pce_peers"] = "pce-peers"

                self.profiles = Sr.TrafficEngineering.Pcc.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
                self._segment_path = lambda: "pcc"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.Pcc, ['dead_timer_interval', 'pcc_centric', 'report_all', 'keepalive_timer_interval', 'initiated_state_interval', 'source_address', 'enable', 'initiated_orphan_interval', 'delegation_timeout'], name, value)


            class PcePeers(_Entity_):
                """
                PCE peer configuration
                
                .. attribute:: pce_peer
                
                	PCE peer
                	**type**\: list of  		 :py:class:`PcePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.PcePeers.PcePeer>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.Pcc.PcePeers, self).__init__()

                    self.yang_name = "pce-peers"
                    self.yang_parent_name = "pcc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pce-peer", ("pce_peer", Sr.TrafficEngineering.Pcc.PcePeers.PcePeer))])
                    self._leafs = OrderedDict()

                    self.pce_peer = YList(self)
                    self._segment_path = lambda: "pce-peers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Pcc.PcePeers, [], name, value)


                class PcePeer(_Entity_):
                    """
                    PCE peer
                    
                    .. attribute:: pce_address  (key)
                    
                    	Remote PCE address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: password
                    
                    	PCC Peer MD5 Password
                    	**type**\: str
                    
                    	**length:** 1..25
                    
                    .. attribute:: keychain
                    
                    	PCC Peer Keychain
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: enable
                    
                    	PCC Peer Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value of this PCE
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Pcc.PcePeers.PcePeer, self).__init__()

                        self.yang_name = "pce-peer"
                        self.yang_parent_name = "pce-peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['pce_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pce_address', (YLeaf(YType.str, 'pce-address'), ['str','str'])),
                            ('password', (YLeaf(YType.str, 'password'), ['str'])),
                            ('keychain', (YLeaf(YType.str, 'keychain'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('precedence', (YLeaf(YType.uint32, 'precedence'), ['int'])),
                        ])
                        self.pce_address = None
                        self.password = None
                        self.keychain = None
                        self.enable = None
                        self.precedence = None
                        self._segment_path = lambda: "pce-peer" + "[pce-address='" + str(self.pce_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/pce-peers/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Pcc.PcePeers.PcePeer, ['pce_address', 'password', 'keychain', 'enable', 'precedence'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Pcc.PcePeers.PcePeer']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.Pcc.PcePeers']['meta_info']


            class Profiles(_Entity_):
                """
                Path profiles configuration
                
                .. attribute:: profile
                
                	Path profile configuration
                	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.Profiles.Profile>`
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.Pcc.Profiles, self).__init__()

                    self.yang_name = "profiles"
                    self.yang_parent_name = "pcc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("profile", ("profile", Sr.TrafficEngineering.Pcc.Profiles.Profile))])
                    self._leafs = OrderedDict()

                    self.profile = YList(self)
                    self._segment_path = lambda: "profiles"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.Pcc.Profiles, [], name, value)


                class Profile(_Entity_):
                    """
                    Path profile configuration
                    
                    .. attribute:: profile_id  (key)
                    
                    	Profile unique identifier
                    	**type**\: int
                    
                    	**range:** 1..65534
                    
                    .. attribute:: profile_auto_route
                    
                    	Autoroute configuration
                    	**type**\:  :py:class:`ProfileAutoRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute>`
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.Pcc.Profiles.Profile, self).__init__()

                        self.yang_name = "profile"
                        self.yang_parent_name = "profiles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['profile_id']
                        self._child_classes = OrderedDict([("profile-auto-route", ("profile_auto_route", Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute))])
                        self._leafs = OrderedDict([
                            ('profile_id', (YLeaf(YType.uint32, 'profile-id'), ['int'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.profile_id = None
                        self.enable = None

                        self.profile_auto_route = Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute()
                        self.profile_auto_route.parent = self
                        self._children_name_map["profile_auto_route"] = "profile-auto-route"
                        self._segment_path = lambda: "profile" + "[profile-id='" + str(self.profile_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/pcc/profiles/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.Pcc.Profiles.Profile, ['profile_id', 'enable'], name, value)


                    class ProfileAutoRoute(_Entity_):
                        """
                        Autoroute configuration
                        
                        .. attribute:: include_all
                        
                        	Include all prefixes to autoroute
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: forward_class
                        
                        	Forward class associated with the policy
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute, self).__init__()

                            self.yang_name = "profile-auto-route"
                            self.yang_parent_name = "profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('include_all', (YLeaf(YType.empty, 'include-all'), ['Empty'])),
                                ('forward_class', (YLeaf(YType.uint32, 'forward-class'), ['int'])),
                            ])
                            self.include_all = None
                            self.forward_class = None
                            self._segment_path = lambda: "profile-auto-route"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute, ['include_all', 'forward_class'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.Pcc.Profiles.Profile']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.Pcc.Profiles']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.Pcc']['meta_info']


        class AffinityMaps(_Entity_):
            """
            Affinity\-map configuration
            
            .. attribute:: affinity_map
            
            	Affinity\-map entry
            	**type**\: list of  		 :py:class:`AffinityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.AffinityMaps.AffinityMap>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.AffinityMaps, self).__init__()

                self.yang_name = "affinity-maps"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("affinity-map", ("affinity_map", Sr.TrafficEngineering.AffinityMaps.AffinityMap))])
                self._leafs = OrderedDict()

                self.affinity_map = YList(self)
                self._segment_path = lambda: "affinity-maps"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.AffinityMaps, [], name, value)


            class AffinityMap(_Entity_):
                """
                Affinity\-map entry
                
                .. attribute:: affinity_name  (key)
                
                	Affinity\-map bit\-position
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: bit_position
                
                	Affinity\-map bit\-position
                	**type**\: int
                
                	**range:** 0..255
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.AffinityMaps.AffinityMap, self).__init__()

                    self.yang_name = "affinity-map"
                    self.yang_parent_name = "affinity-maps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['affinity_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('affinity_name', (YLeaf(YType.str, 'affinity-name'), ['str'])),
                        ('bit_position', (YLeaf(YType.uint32, 'bit-position'), ['int'])),
                    ])
                    self.affinity_name = None
                    self.bit_position = None
                    self._segment_path = lambda: "affinity-map" + "[affinity-name='" + str(self.affinity_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/affinity-maps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.AffinityMaps.AffinityMap, ['affinity_name', 'bit_position'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.AffinityMaps.AffinityMap']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.AffinityMaps']['meta_info']


        class CandidatePathTypes(_Entity_):
            """
            Configurations for candidate paths.
            
            .. attribute:: candidate_path_type
            
            	Configurations for candidate paths of specific type
            	**type**\: list of  		 :py:class:`CandidatePathType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType>`
            
            

            """

            _prefix = 'infra-xtc-agent-cfg'
            _revision = '2019-09-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Sr.TrafficEngineering.CandidatePathTypes, self).__init__()

                self.yang_name = "candidate-path-types"
                self.yang_parent_name = "traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("candidate-path-type", ("candidate_path_type", Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType))])
                self._leafs = OrderedDict()

                self.candidate_path_type = YList(self)
                self._segment_path = lambda: "candidate-path-types"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sr.TrafficEngineering.CandidatePathTypes, [], name, value)


            class CandidatePathType(_Entity_):
                """
                Configurations for candidate paths of specific
                type.
                
                .. attribute:: candidate_path_type  (key)
                
                	Candidate\-path type
                	**type**\:  :py:class:`XtcCpath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcCpath>`
                
                .. attribute:: candidate_path_type_all_or_candidate_path_type_local_or_candidate_path_type_bgp_odn_or_candidate_path_type_bgp_srte_or_candidate_path_type_pcep
                
                	candidate path type all or candidate path type local or candidate path type bgp odn or candidate path type bgp srte or candidate path type pcep
                	**type**\:  :py:class:`CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'infra-xtc-agent-cfg'
                _revision = '2019-09-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType, self).__init__()

                    self.yang_name = "candidate-path-type"
                    self.yang_parent_name = "candidate-path-types"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['candidate_path_type']
                    self._child_classes = OrderedDict([("candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep", ("candidate_path_type_all_or_candidate_path_type_local_or_candidate_path_type_bgp_odn_or_candidate_path_type_bgp_srte_or_candidate_path_type_pcep", Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep))])
                    self._leafs = OrderedDict([
                        ('candidate_path_type', (YLeaf(YType.enumeration, 'candidate-path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcCpath', '')])),
                    ])
                    self.candidate_path_type = None

                    self.candidate_path_type_all_or_candidate_path_type_local_or_candidate_path_type_bgp_odn_or_candidate_path_type_bgp_srte_or_candidate_path_type_pcep = None
                    self._children_name_map["candidate_path_type_all_or_candidate_path_type_local_or_candidate_path_type_bgp_odn_or_candidate_path_type_bgp_srte_or_candidate_path_type_pcep"] = "candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep"
                    self._segment_path = lambda: "candidate-path-type" + "[candidate-path-type='" + str(self.candidate_path_type) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-ms-cfg:sr/Cisco-IOS-XR-infra-xtc-agent-cfg:traffic-engineering/candidate-path-types/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType, ['candidate_path_type'], name, value)


                class CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep(_Entity_):
                    """
                    candidate path type all or candidate path
                    type local or candidate path type bgp odn or
                    candidate path type bgp srte or candidate
                    path type pcep
                    
                    .. attribute:: source_address
                    
                    	Source address of a candidate path. EndPointType , Source
                    	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg.Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-xtc-agent-cfg'
                    _revision = '2019-09-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep, self).__init__()

                        self.yang_name = "candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep"
                        self.yang_parent_name = "candidate-path-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source-address", ("source_address", Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress))])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.enable = None

                        self.source_address = None
                        self._children_name_map["source_address"] = "source-address"
                        self._segment_path = lambda: "candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep, ['enable'], name, value)


                    class SourceAddress(_Entity_):
                        """
                        Source address of a candidate path. EndPointType
                        , Source
                        
                        .. attribute:: ip_address_type
                        
                        	IP address type
                        	**type**\:  :py:class:`XtcEndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg.XtcEndPoint>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'infra-xtc-agent-cfg'
                        _revision = '2019-09-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress, self).__init__()

                            self.yang_name = "source-address"
                            self.yang_parent_name = "candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('ip_address_type', (YLeaf(YType.enumeration, 'ip-address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint', '')])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                            ])
                            self.ip_address_type = None
                            self.source_address = None
                            self._segment_path = lambda: "source-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress, ['ip_address_type', 'source_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                            return meta._meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                        return meta._meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                    return meta._meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
                return meta._meta_table['Sr.TrafficEngineering.CandidatePathTypes']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
            return meta._meta_table['Sr.TrafficEngineering']['meta_info']

    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_ms_cfg as meta
        return meta._meta_table['Sr']['meta_info']


