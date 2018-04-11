""" Cisco_IOS_XE_fib_oper 

This module contains a collection of YANG definitions
for IOS\-XE FIB operational data.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EncapsulationHeaderType(Enum):
    """
    EncapsulationHeaderType (Enum Class)

    Types of header for packet encapsulation

    .. data:: encap_hdr_type_unknown = 0

    	Unknown encapsulation header type

    .. data:: encap_hdr_type_gre = 1

    	GRE encapsulation header type

    .. data:: encap_hdr_type_ipv4 = 2

    	IPv4 encapsulation header type

    .. data:: encap_hdr_type_ipv6 = 3

    	IPv6 encapsulation header type

    .. data:: encap_hdr_type_mpls = 4

    	MPLS encapsulation header type

    """

    encap_hdr_type_unknown = Enum.YLeaf(0, "encap-hdr-type-unknown")

    encap_hdr_type_gre = Enum.YLeaf(1, "encap-hdr-type-gre")

    encap_hdr_type_ipv4 = Enum.YLeaf(2, "encap-hdr-type-ipv4")

    encap_hdr_type_ipv6 = Enum.YLeaf(3, "encap-hdr-type-ipv6")

    encap_hdr_type_mpls = Enum.YLeaf(4, "encap-hdr-type-mpls")


class FibAddressFamily(Enum):
    """
    FibAddressFamily (Enum Class)

    FIB Address Family Types

    .. data:: fib_addr_fam_unknown = 0

    	Unknown Address Family

    .. data:: fib_addr_fam_ipv4 = 1

    	IPv4 Address Family

    .. data:: fib_addr_fam_ipv6 = 2

    	IPv6 Address Family

    """

    fib_addr_fam_unknown = Enum.YLeaf(0, "fib-addr-fam-unknown")

    fib_addr_fam_ipv4 = Enum.YLeaf(1, "fib-addr-fam-ipv4")

    fib_addr_fam_ipv6 = Enum.YLeaf(2, "fib-addr-fam-ipv6")


class FibPathType(Enum):
    """
    FibPathType (Enum Class)

    Type of FIB path used

    .. data:: fib_path_type_unknown = 0

    	Unknown FIB path type

    .. data:: fib_path_type_receive = 1

    	Receive FIB path type

    .. data:: fib_path_type_connected = 2

    	Connected FIB path type

    .. data:: fib_path_type_attached_prefix = 3

    	Attached Prefix FIB path type

    .. data:: fib_path_type_attached_host = 4

    	Attached Host FIB path type

    .. data:: fib_path_type_attached_nexthop = 5

    	Attached Nexthop FIB path type

    .. data:: fib_path_type_recursive = 6

    	Recursive FIB path type

    .. data:: fib_path_type_adjacency_prefix = 7

    	Adjacency Prefix FIB path type

    .. data:: fib_path_type_special_prefix = 8

    	Special Prefix FIB path type

    """

    fib_path_type_unknown = Enum.YLeaf(0, "fib-path-type-unknown")

    fib_path_type_receive = Enum.YLeaf(1, "fib-path-type-receive")

    fib_path_type_connected = Enum.YLeaf(2, "fib-path-type-connected")

    fib_path_type_attached_prefix = Enum.YLeaf(3, "fib-path-type-attached-prefix")

    fib_path_type_attached_host = Enum.YLeaf(4, "fib-path-type-attached-host")

    fib_path_type_attached_nexthop = Enum.YLeaf(5, "fib-path-type-attached-nexthop")

    fib_path_type_recursive = Enum.YLeaf(6, "fib-path-type-recursive")

    fib_path_type_adjacency_prefix = Enum.YLeaf(7, "fib-path-type-adjacency-prefix")

    fib_path_type_special_prefix = Enum.YLeaf(8, "fib-path-type-special-prefix")



class FibOperData(Entity):
    """
    This module contains a collection of YANG definitions for
    monitoring the operation of IOS\-XE CEF.
    Copyright (c) 2016\-2017 by Cisco Systems, Inc.
    All rights reserved.
    
    .. attribute:: fib_ni_entry
    
    	FIB Network Instances
    	**type**\: list of  		 :py:class:`FibNiEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibOperData.FibNiEntry>`
    
    

    """

    _prefix = 'fib-ios-xe-oper'
    _revision = '2017-07-04'

    def __init__(self):
        super(FibOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "fib-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-fib-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("fib-ni-entry", ("fib_ni_entry", FibOperData.FibNiEntry))])
        self._leafs = OrderedDict()

        self.fib_ni_entry = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-fib-oper:fib-oper-data"

    def __setattr__(self, name, value):
        self._perform_setattr(FibOperData, [], name, value)


    class FibNiEntry(Entity):
        """
        FIB Network Instances
        
        .. attribute:: instance_name  (key)
        
        	Instance Name
        	**type**\: str
        
        .. attribute:: af
        
        	Address Family
        	**type**\:  :py:class:`FibAddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibAddressFamily>`
        
        .. attribute:: num_pfx
        
        	Number of prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_pfx_fwd
        
        	Number of forwarding prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_pfx_non_fwd
        
        	Number of non\-forwarding prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: fib_entries
        
        	List of FIB entries
        	**type**\: list of  		 :py:class:`FibEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibOperData.FibNiEntry.FibEntries>`
        
        

        """

        _prefix = 'fib-ios-xe-oper'
        _revision = '2017-07-04'

        def __init__(self):
            super(FibOperData.FibNiEntry, self).__init__()

            self.yang_name = "fib-ni-entry"
            self.yang_parent_name = "fib-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['instance_name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("fib-entries", ("fib_entries", FibOperData.FibNiEntry.FibEntries))])
            self._leafs = OrderedDict([
                ('instance_name', YLeaf(YType.str, 'instance-name')),
                ('af', YLeaf(YType.enumeration, 'af')),
                ('num_pfx', YLeaf(YType.uint32, 'num-pfx')),
                ('num_pfx_fwd', YLeaf(YType.uint32, 'num-pfx-fwd')),
                ('num_pfx_non_fwd', YLeaf(YType.uint32, 'num-pfx-non-fwd')),
            ])
            self.instance_name = None
            self.af = None
            self.num_pfx = None
            self.num_pfx_fwd = None
            self.num_pfx_non_fwd = None

            self.fib_entries = YList(self)
            self._segment_path = lambda: "fib-ni-entry" + "[instance-name='" + str(self.instance_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-fib-oper:fib-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FibOperData.FibNiEntry, ['instance_name', 'af', 'num_pfx', 'num_pfx_fwd', 'num_pfx_non_fwd'], name, value)


        class FibEntries(Entity):
            """
            List of FIB entries
            
            .. attribute:: ip_addr  (key)
            
            	IP address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            .. attribute:: instance_name
            
            	Instance Name
            	**type**\: str
            
            .. attribute:: af
            
            	Address Family
            	**type**\:  :py:class:`FibAddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibAddressFamily>`
            
            .. attribute:: num_paths
            
            	Number of Paths available
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: packets_forwarded
            
            	Packets forwarded through this entry
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: octets_forwarded
            
            	Octets forwarded through this entry
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: fib_nexthop_entries
            
            	List of FIB next\-hop entries
            	**type**\: list of  		 :py:class:`FibNexthopEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibOperData.FibNiEntry.FibEntries.FibNexthopEntries>`
            
            

            """

            _prefix = 'fib-ios-xe-oper'
            _revision = '2017-07-04'

            def __init__(self):
                super(FibOperData.FibNiEntry.FibEntries, self).__init__()

                self.yang_name = "fib-entries"
                self.yang_parent_name = "fib-ni-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['ip_addr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("fib-nexthop-entries", ("fib_nexthop_entries", FibOperData.FibNiEntry.FibEntries.FibNexthopEntries))])
                self._leafs = OrderedDict([
                    ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                    ('instance_name', YLeaf(YType.str, 'instance-name')),
                    ('af', YLeaf(YType.enumeration, 'af')),
                    ('num_paths', YLeaf(YType.uint8, 'num-paths')),
                    ('packets_forwarded', YLeaf(YType.uint64, 'packets-forwarded')),
                    ('octets_forwarded', YLeaf(YType.uint64, 'octets-forwarded')),
                ])
                self.ip_addr = None
                self.instance_name = None
                self.af = None
                self.num_paths = None
                self.packets_forwarded = None
                self.octets_forwarded = None

                self.fib_nexthop_entries = YList(self)
                self._segment_path = lambda: "fib-entries" + "[ip-addr='" + str(self.ip_addr) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(FibOperData.FibNiEntry.FibEntries, ['ip_addr', 'instance_name', 'af', 'num_paths', 'packets_forwarded', 'octets_forwarded'], name, value)


            class FibNexthopEntries(Entity):
                """
                List of FIB next\-hop entries
                
                .. attribute:: nh_addr  (key)
                
                	IP Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: index
                
                	Unique Next\-hop Path Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: af
                
                	Address Family
                	**type**\:  :py:class:`FibAddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibAddressFamily>`
                
                .. attribute:: ifname
                
                	Output Interface Name
                	**type**\: str
                
                .. attribute:: path_type
                
                	FIB path type
                	**type**\:  :py:class:`FibPathType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.FibPathType>`
                
                .. attribute:: path_id
                
                	Unique Next\-hop Path Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: weight
                
                	Next\-hop weight
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: encap
                
                	Encap Header Type
                	**type**\:  :py:class:`EncapsulationHeaderType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.EncapsulationHeaderType>`
                
                .. attribute:: decap
                
                	Decap Header Type
                	**type**\:  :py:class:`EncapsulationHeaderType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_fib_oper.EncapsulationHeaderType>`
                
                

                """

                _prefix = 'fib-ios-xe-oper'
                _revision = '2017-07-04'

                def __init__(self):
                    super(FibOperData.FibNiEntry.FibEntries.FibNexthopEntries, self).__init__()

                    self.yang_name = "fib-nexthop-entries"
                    self.yang_parent_name = "fib-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['nh_addr']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nh_addr', YLeaf(YType.str, 'nh-addr')),
                        ('index', YLeaf(YType.uint32, 'index')),
                        ('af', YLeaf(YType.enumeration, 'af')),
                        ('ifname', YLeaf(YType.str, 'ifname')),
                        ('path_type', YLeaf(YType.enumeration, 'path-type')),
                        ('path_id', YLeaf(YType.uint32, 'path-id')),
                        ('weight', YLeaf(YType.uint8, 'weight')),
                        ('encap', YLeaf(YType.enumeration, 'encap')),
                        ('decap', YLeaf(YType.enumeration, 'decap')),
                    ])
                    self.nh_addr = None
                    self.index = None
                    self.af = None
                    self.ifname = None
                    self.path_type = None
                    self.path_id = None
                    self.weight = None
                    self.encap = None
                    self.decap = None
                    self._segment_path = lambda: "fib-nexthop-entries" + "[nh-addr='" + str(self.nh_addr) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(FibOperData.FibNiEntry.FibEntries.FibNexthopEntries, ['nh_addr', 'index', 'af', 'ifname', 'path_type', 'path_id', 'weight', 'encap', 'decap'], name, value)

    def clone_ptr(self):
        self._top_entity = FibOperData()
        return self._top_entity

