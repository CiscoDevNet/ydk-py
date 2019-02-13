""" IP_FORWARD_MIB 

The MIB module for the display of CIDR multipath IP Routes.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IPFORWARDMIB(Entity):
    """
    
    
    .. attribute:: ipforward
    
    	
    	**type**\:  :py:class:`IpForward <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpForward>`
    
    	**config**\: False
    
    .. attribute:: ipforwardtable
    
    	This entity's IP Routing table
    	**type**\:  :py:class:`IpForwardTable <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpForwardTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: ipcidrroutetable
    
    	This entity's IP Routing table
    	**type**\:  :py:class:`IpCidrRouteTable <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpCidrRouteTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'IP-FORWARD-MIB'
    _revision = '1996-09-19'

    def __init__(self):
        super(IPFORWARDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IP-FORWARD-MIB"
        self.yang_parent_name = "IP-FORWARD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipForward", ("ipforward", IPFORWARDMIB.IpForward)), ("ipForwardTable", ("ipforwardtable", IPFORWARDMIB.IpForwardTable)), ("ipCidrRouteTable", ("ipcidrroutetable", IPFORWARDMIB.IpCidrRouteTable))])
        self._leafs = OrderedDict()

        self.ipforward = IPFORWARDMIB.IpForward()
        self.ipforward.parent = self
        self._children_name_map["ipforward"] = "ipForward"

        self.ipforwardtable = IPFORWARDMIB.IpForwardTable()
        self.ipforwardtable.parent = self
        self._children_name_map["ipforwardtable"] = "ipForwardTable"

        self.ipcidrroutetable = IPFORWARDMIB.IpCidrRouteTable()
        self.ipcidrroutetable.parent = self
        self._children_name_map["ipcidrroutetable"] = "ipCidrRouteTable"
        self._segment_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IPFORWARDMIB, [], name, value)


    class IpForward(Entity):
        """
        
        
        .. attribute:: ipforwardnumber
        
        	The number of current  ipForwardTable  entries that are not invalid
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**status**\: obsolete
        
        .. attribute:: ipcidrroutenumber
        
        	The number of current ipCidrRouteTable entries that are not invalid
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IPFORWARDMIB.IpForward, self).__init__()

            self.yang_name = "ipForward"
            self.yang_parent_name = "IP-FORWARD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipforwardnumber', (YLeaf(YType.uint32, 'ipForwardNumber'), ['int'])),
                ('ipcidrroutenumber', (YLeaf(YType.uint32, 'ipCidrRouteNumber'), ['int'])),
            ])
            self.ipforwardnumber = None
            self.ipcidrroutenumber = None
            self._segment_path = lambda: "ipForward"
            self._absolute_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IPFORWARDMIB.IpForward, ['ipforwardnumber', 'ipcidrroutenumber'], name, value)



    class IpForwardTable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: ipforwardentry
        
        	A particular route to  a  particular  destina\- tion, under a particular policy
        	**type**\: list of  		 :py:class:`IpForwardEntry <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpForwardTable.IpForwardEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IPFORWARDMIB.IpForwardTable, self).__init__()

            self.yang_name = "ipForwardTable"
            self.yang_parent_name = "IP-FORWARD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipForwardEntry", ("ipforwardentry", IPFORWARDMIB.IpForwardTable.IpForwardEntry))])
            self._leafs = OrderedDict()

            self.ipforwardentry = YList(self)
            self._segment_path = lambda: "ipForwardTable"
            self._absolute_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IPFORWARDMIB.IpForwardTable, [], name, value)


        class IpForwardEntry(Entity):
            """
            A particular route to  a  particular  destina\-
            tion, under a particular policy.
            
            .. attribute:: ipforwarddest  (key)
            
            	The destination IP address of this route.   An entry  with  a value of 0.0.0.0 is considered a default route.  This object may not take a Multicast (Class  D) address value.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipForwardMask object is not equal to x
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardproto  (key)
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:  :py:class:`IpForwardProto <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpForwardTable.IpForwardEntry.IpForwardProto>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardpolicy  (key)
            
            	The general set of conditions that would cause the  selection  of  one multipath route (set of next hops for a given destination) is  referred to as 'policy'.  Unless the mechanism indicated by ipForwardPro\- to specifies otherwise, the policy specifier is the IP TOS Field.  The encoding of IP TOS is as  specified  by  the  following convention.  Zero indicates the default path if no more  specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+           IP TOS                IP TOS     Field     Policy      Field     Policy     Contents    Code      Contents    Code     0 0 0 0  ==>   0      0 0 0 1  ==>   2     0 0 1 0  ==>   4      0 0 1 1  ==>   6     0 1 0 0  ==>   8      0 1 0 1  ==>  10     0 1 1 0  ==>  12      0 1 1 1  ==>  14     1 0 0 0  ==>  16      1 0 0 1  ==>  18     1 0 1 0  ==>  20      1 0 1 1  ==>  22     1 1 0 0  ==>  24      1 1 0 1  ==>  26     1 1 1 0  ==>  28      1 1 1 1  ==>  30  Protocols defining 'policy' otherwise must  ei\- ther define a set of values which are valid for this  object  or  must  implement  an  integer\- instanced  policy table for which this object's value acts as an index
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardnexthop  (key)
            
            	On remote routes, the address of the next sys\- tem en route; Otherwise, 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmask
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  ipForwardDest  field.   For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value  of the  ipForwardMask  by  reference to the IP Ad\- dress Class.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipForwardDest object is not equal to ipForward\- Dest
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardifindex
            
            	The ifIndex value which identifies  the  local interface  through  which  the next hop of this route should be reached
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardtype
            
            	The type of route.  Note that local(3)  refers to  a route for which the next hop is the final destination; remote(4) refers to  a  route  for which  the  next  hop is not the final destina\- tion.  Setting this object to the value invalid(2) has the  effect  of  invalidating the corresponding entry in the ipForwardTable object.   That  is, it  effectively  disassociates  the destination identified with said entry from the route iden\- tified    with    said   entry.    It   is   an implementation\-specific matter  as  to  whether the agent removes an invalidated entry from the table.  Accordingly, management  stations  must be prepared to receive tabular information from agents that corresponds to entries not current\- ly  in  use.  Proper interpretation of such en\- tries requires examination of the relevant  ip\- ForwardType object
            	**type**\:  :py:class:`IpForwardType <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpForwardTable.IpForwardEntry.IpForwardType>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardage
            
            	The number of seconds  since  this  route  was last  updated  or  otherwise  determined  to be correct.  Note that no semantics of  `too  old' can  be implied except through knowledge of the routing  protocol  by  which  the   route   was learned
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardinfo
            
            	A reference to MIB definitions specific to the particular  routing protocol which is responsi\- ble for this route, as determined by the  value specified  in the route's ipForwardProto value. If this information is not present,  its  value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object  identif\- ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must  be  able  to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardnexthopas
            
            	The Autonomous System Number of the Next  Hop. When  this  is  unknown  or not relevant to the protocol indicated by ipForwardProto, zero
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric1
            
            	The primary routing  metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric2
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric3
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric4
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric5
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                super(IPFORWARDMIB.IpForwardTable.IpForwardEntry, self).__init__()

                self.yang_name = "ipForwardEntry"
                self.yang_parent_name = "ipForwardTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipforwarddest','ipforwardproto','ipforwardpolicy','ipforwardnexthop']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipforwarddest', (YLeaf(YType.str, 'ipForwardDest'), ['str'])),
                    ('ipforwardproto', (YLeaf(YType.enumeration, 'ipForwardProto'), [('ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IPFORWARDMIB', 'IpForwardTable.IpForwardEntry.IpForwardProto')])),
                    ('ipforwardpolicy', (YLeaf(YType.int32, 'ipForwardPolicy'), ['int'])),
                    ('ipforwardnexthop', (YLeaf(YType.str, 'ipForwardNextHop'), ['str'])),
                    ('ipforwardmask', (YLeaf(YType.str, 'ipForwardMask'), ['str'])),
                    ('ipforwardifindex', (YLeaf(YType.int32, 'ipForwardIfIndex'), ['int'])),
                    ('ipforwardtype', (YLeaf(YType.enumeration, 'ipForwardType'), [('ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IPFORWARDMIB', 'IpForwardTable.IpForwardEntry.IpForwardType')])),
                    ('ipforwardage', (YLeaf(YType.int32, 'ipForwardAge'), ['int'])),
                    ('ipforwardinfo', (YLeaf(YType.str, 'ipForwardInfo'), ['str'])),
                    ('ipforwardnexthopas', (YLeaf(YType.int32, 'ipForwardNextHopAS'), ['int'])),
                    ('ipforwardmetric1', (YLeaf(YType.int32, 'ipForwardMetric1'), ['int'])),
                    ('ipforwardmetric2', (YLeaf(YType.int32, 'ipForwardMetric2'), ['int'])),
                    ('ipforwardmetric3', (YLeaf(YType.int32, 'ipForwardMetric3'), ['int'])),
                    ('ipforwardmetric4', (YLeaf(YType.int32, 'ipForwardMetric4'), ['int'])),
                    ('ipforwardmetric5', (YLeaf(YType.int32, 'ipForwardMetric5'), ['int'])),
                ])
                self.ipforwarddest = None
                self.ipforwardproto = None
                self.ipforwardpolicy = None
                self.ipforwardnexthop = None
                self.ipforwardmask = None
                self.ipforwardifindex = None
                self.ipforwardtype = None
                self.ipforwardage = None
                self.ipforwardinfo = None
                self.ipforwardnexthopas = None
                self.ipforwardmetric1 = None
                self.ipforwardmetric2 = None
                self.ipforwardmetric3 = None
                self.ipforwardmetric4 = None
                self.ipforwardmetric5 = None
                self._segment_path = lambda: "ipForwardEntry" + "[ipForwardDest='" + str(self.ipforwarddest) + "']" + "[ipForwardProto='" + str(self.ipforwardproto) + "']" + "[ipForwardPolicy='" + str(self.ipforwardpolicy) + "']" + "[ipForwardNextHop='" + str(self.ipforwardnexthop) + "']"
                self._absolute_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB/ipForwardTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IPFORWARDMIB.IpForwardTable.IpForwardEntry, ['ipforwarddest', 'ipforwardproto', 'ipforwardpolicy', 'ipforwardnexthop', 'ipforwardmask', 'ipforwardifindex', 'ipforwardtype', 'ipforwardage', 'ipforwardinfo', 'ipforwardnexthopas', 'ipforwardmetric1', 'ipforwardmetric2', 'ipforwardmetric3', 'ipforwardmetric4', 'ipforwardmetric5'], name, value)

            class IpForwardProto(Enum):
                """
                IpForwardProto (Enum Class)

                The routing mechanism via which this route was

                learned.  Inclusion of values for gateway rout\-

                ing protocols is not  intended  to  imply  that

                hosts should support those protocols.

                .. data:: other = 1

                .. data:: local = 2

                .. data:: netmgmt = 3

                .. data:: icmp = 4

                .. data:: egp = 5

                .. data:: ggp = 6

                .. data:: hello = 7

                .. data:: rip = 8

                .. data:: is_is = 9

                .. data:: es_is = 10

                .. data:: ciscoIgrp = 11

                .. data:: bbnSpfIgp = 12

                .. data:: ospf = 13

                .. data:: bgp = 14

                .. data:: idpr = 15

                """

                other = Enum.YLeaf(1, "other")

                local = Enum.YLeaf(2, "local")

                netmgmt = Enum.YLeaf(3, "netmgmt")

                icmp = Enum.YLeaf(4, "icmp")

                egp = Enum.YLeaf(5, "egp")

                ggp = Enum.YLeaf(6, "ggp")

                hello = Enum.YLeaf(7, "hello")

                rip = Enum.YLeaf(8, "rip")

                is_is = Enum.YLeaf(9, "is-is")

                es_is = Enum.YLeaf(10, "es-is")

                ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

                bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

                ospf = Enum.YLeaf(13, "ospf")

                bgp = Enum.YLeaf(14, "bgp")

                idpr = Enum.YLeaf(15, "idpr")


            class IpForwardType(Enum):
                """
                IpForwardType (Enum Class)

                The type of route.  Note that local(3)  refers

                to  a route for which the next hop is the final

                destination; remote(4) refers to  a  route  for

                which  the  next  hop is not the final destina\-

                tion.

                Setting this object to the value invalid(2) has

                the  effect  of  invalidating the corresponding

                entry in the ipForwardTable object.   That  is,

                it  effectively  disassociates  the destination

                identified with said entry from the route iden\-

                tified    with    said   entry.    It   is   an

                implementation\-specific matter  as  to  whether

                the agent removes an invalidated entry from the

                table.  Accordingly, management  stations  must

                be prepared to receive tabular information from

                agents that corresponds to entries not current\-

                ly  in  use.  Proper interpretation of such en\-

                tries requires examination of the relevant  ip\-

                ForwardType object.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: local = 3

                .. data:: remote = 4

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")





    class IpCidrRouteTable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: ipcidrrouteentry
        
        	A particular route to  a  particular  destina\- tion, under a particular policy
        	**type**\: list of  		 :py:class:`IpCidrRouteEntry <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IPFORWARDMIB.IpCidrRouteTable, self).__init__()

            self.yang_name = "ipCidrRouteTable"
            self.yang_parent_name = "IP-FORWARD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipCidrRouteEntry", ("ipcidrrouteentry", IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry))])
            self._leafs = OrderedDict()

            self.ipcidrrouteentry = YList(self)
            self._segment_path = lambda: "ipCidrRouteTable"
            self._absolute_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IPFORWARDMIB.IpCidrRouteTable, [], name, value)


        class IpCidrRouteEntry(Entity):
            """
            A particular route to  a  particular  destina\-
            tion, under a particular policy.
            
            .. attribute:: ipcidrroutedest  (key)
            
            	The destination IP address of this route.  This object may not take a Multicast (Class  D) address value.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipCidrRouteMask object is not equal to x
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemask  (key)
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  ipCidrRouteDest  field.   For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value  of the  ipCidrRouteMask  by  reference to the IP Ad\- dress Class.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipCidrRouteDest object is not equal to ipCidrRoute\- Dest
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ipcidrroutetos  (key)
            
            	The policy specifier is the IP TOS Field.  The encoding of IP TOS is as specified  by  the  following convention. Zero indicates the default path if no more  specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+           IP TOS                IP TOS     Field     Policy      Field     Policy     Contents    Code      Contents    Code     0 0 0 0  ==>   0      0 0 0 1  ==>   2     0 0 1 0  ==>   4      0 0 1 1  ==>   6     0 1 0 0  ==>   8      0 1 0 1  ==>  10     0 1 1 0  ==>  12      0 1 1 1  ==>  14     1 0 0 0  ==>  16      1 0 0 1  ==>  18     1 0 1 0  ==>  20      1 0 1 1  ==>  22     1 1 0 0  ==>  24      1 1 0 1  ==>  26     1 1 1 0  ==>  28      1 1 1 1  ==>  30
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutenexthop  (key)
            
            	On remote routes, the address of the next sys\- tem en route; Otherwise, 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ipcidrrouteifindex
            
            	The ifIndex value which identifies  the  local interface  through  which  the next hop of this route should be reached
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutetype
            
            	The type of route.  Note that local(3)  refers to  a route for which the next hop is the final destination; remote(4) refers to  a  route  for which  the  next  hop is not the final destina\- tion.  Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.   reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:  :py:class:`IpCidrRouteType <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry.IpCidrRouteType>`
            
            	**config**\: False
            
            .. attribute:: ipcidrrouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:  :py:class:`IpCidrRouteProto <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry.IpCidrRouteProto>`
            
            	**config**\: False
            
            .. attribute:: ipcidrrouteage
            
            	The number of seconds  since  this  route  was last  updated  or  otherwise  determined  to be correct.  Note that no semantics of  `too  old' can  be implied except through knowledge of the routing  protocol  by  which  the   route   was learned
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrrouteinfo
            
            	A reference to MIB definitions specific to the particular  routing protocol which is responsi\- ble for this route, as determined by the  value specified  in the route's ipCidrRouteProto value. If this information is not present,  its  value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object  identif\- ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must  be  able  to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: ipcidrroutenexthopas
            
            	The Autonomous System Number of the Next  Hop. The  semantics of this object are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value. When  this object is unknown or not relevant its value should be set to zero
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemetric1
            
            	The primary routing  metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemetric2
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemetric3
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemetric4
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutemetric5
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ipcidrroutestatus
            
            	The row status variable, used according to row installation and removal conventions
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                super(IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry, self).__init__()

                self.yang_name = "ipCidrRouteEntry"
                self.yang_parent_name = "ipCidrRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipcidrroutedest','ipcidrroutemask','ipcidrroutetos','ipcidrroutenexthop']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipcidrroutedest', (YLeaf(YType.str, 'ipCidrRouteDest'), ['str'])),
                    ('ipcidrroutemask', (YLeaf(YType.str, 'ipCidrRouteMask'), ['str'])),
                    ('ipcidrroutetos', (YLeaf(YType.int32, 'ipCidrRouteTos'), ['int'])),
                    ('ipcidrroutenexthop', (YLeaf(YType.str, 'ipCidrRouteNextHop'), ['str'])),
                    ('ipcidrrouteifindex', (YLeaf(YType.int32, 'ipCidrRouteIfIndex'), ['int'])),
                    ('ipcidrroutetype', (YLeaf(YType.enumeration, 'ipCidrRouteType'), [('ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IPFORWARDMIB', 'IpCidrRouteTable.IpCidrRouteEntry.IpCidrRouteType')])),
                    ('ipcidrrouteproto', (YLeaf(YType.enumeration, 'ipCidrRouteProto'), [('ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IPFORWARDMIB', 'IpCidrRouteTable.IpCidrRouteEntry.IpCidrRouteProto')])),
                    ('ipcidrrouteage', (YLeaf(YType.int32, 'ipCidrRouteAge'), ['int'])),
                    ('ipcidrrouteinfo', (YLeaf(YType.str, 'ipCidrRouteInfo'), ['str'])),
                    ('ipcidrroutenexthopas', (YLeaf(YType.int32, 'ipCidrRouteNextHopAS'), ['int'])),
                    ('ipcidrroutemetric1', (YLeaf(YType.int32, 'ipCidrRouteMetric1'), ['int'])),
                    ('ipcidrroutemetric2', (YLeaf(YType.int32, 'ipCidrRouteMetric2'), ['int'])),
                    ('ipcidrroutemetric3', (YLeaf(YType.int32, 'ipCidrRouteMetric3'), ['int'])),
                    ('ipcidrroutemetric4', (YLeaf(YType.int32, 'ipCidrRouteMetric4'), ['int'])),
                    ('ipcidrroutemetric5', (YLeaf(YType.int32, 'ipCidrRouteMetric5'), ['int'])),
                    ('ipcidrroutestatus', (YLeaf(YType.enumeration, 'ipCidrRouteStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ipcidrroutedest = None
                self.ipcidrroutemask = None
                self.ipcidrroutetos = None
                self.ipcidrroutenexthop = None
                self.ipcidrrouteifindex = None
                self.ipcidrroutetype = None
                self.ipcidrrouteproto = None
                self.ipcidrrouteage = None
                self.ipcidrrouteinfo = None
                self.ipcidrroutenexthopas = None
                self.ipcidrroutemetric1 = None
                self.ipcidrroutemetric2 = None
                self.ipcidrroutemetric3 = None
                self.ipcidrroutemetric4 = None
                self.ipcidrroutemetric5 = None
                self.ipcidrroutestatus = None
                self._segment_path = lambda: "ipCidrRouteEntry" + "[ipCidrRouteDest='" + str(self.ipcidrroutedest) + "']" + "[ipCidrRouteMask='" + str(self.ipcidrroutemask) + "']" + "[ipCidrRouteTos='" + str(self.ipcidrroutetos) + "']" + "[ipCidrRouteNextHop='" + str(self.ipcidrroutenexthop) + "']"
                self._absolute_path = lambda: "IP-FORWARD-MIB:IP-FORWARD-MIB/ipCidrRouteTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IPFORWARDMIB.IpCidrRouteTable.IpCidrRouteEntry, ['ipcidrroutedest', 'ipcidrroutemask', 'ipcidrroutetos', 'ipcidrroutenexthop', 'ipcidrrouteifindex', 'ipcidrroutetype', 'ipcidrrouteproto', 'ipcidrrouteage', 'ipcidrrouteinfo', 'ipcidrroutenexthopas', 'ipcidrroutemetric1', 'ipcidrroutemetric2', 'ipcidrroutemetric3', 'ipcidrroutemetric4', 'ipcidrroutemetric5', 'ipcidrroutestatus'], name, value)

            class IpCidrRouteProto(Enum):
                """
                IpCidrRouteProto (Enum Class)

                The routing mechanism via which this route was

                learned.  Inclusion of values for gateway rout\-

                ing protocols is not  intended  to  imply  that

                hosts should support those protocols.

                .. data:: other = 1

                .. data:: local = 2

                .. data:: netmgmt = 3

                .. data:: icmp = 4

                .. data:: egp = 5

                .. data:: ggp = 6

                .. data:: hello = 7

                .. data:: rip = 8

                .. data:: isIs = 9

                .. data:: esIs = 10

                .. data:: ciscoIgrp = 11

                .. data:: bbnSpfIgp = 12

                .. data:: ospf = 13

                .. data:: bgp = 14

                .. data:: idpr = 15

                .. data:: ciscoEigrp = 16

                """

                other = Enum.YLeaf(1, "other")

                local = Enum.YLeaf(2, "local")

                netmgmt = Enum.YLeaf(3, "netmgmt")

                icmp = Enum.YLeaf(4, "icmp")

                egp = Enum.YLeaf(5, "egp")

                ggp = Enum.YLeaf(6, "ggp")

                hello = Enum.YLeaf(7, "hello")

                rip = Enum.YLeaf(8, "rip")

                isIs = Enum.YLeaf(9, "isIs")

                esIs = Enum.YLeaf(10, "esIs")

                ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

                bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

                ospf = Enum.YLeaf(13, "ospf")

                bgp = Enum.YLeaf(14, "bgp")

                idpr = Enum.YLeaf(15, "idpr")

                ciscoEigrp = Enum.YLeaf(16, "ciscoEigrp")


            class IpCidrRouteType(Enum):
                """
                IpCidrRouteType (Enum Class)

                The type of route.  Note that local(3)  refers

                to  a route for which the next hop is the final

                destination; remote(4) refers to  a  route  for

                which  the  next  hop is not the final destina\-

                tion.

                Routes which do not result in traffic forwarding or

                rejection should not be displayed even if the

                implementation keeps them stored internally.

                reject (2) refers to a route which, if matched, discards

                the message as unreachable. This is used in some

                protocols as a means of correctly aggregating routes.

                .. data:: other = 1

                .. data:: reject = 2

                .. data:: local = 3

                .. data:: remote = 4

                """

                other = Enum.YLeaf(1, "other")

                reject = Enum.YLeaf(2, "reject")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")




    def clone_ptr(self):
        self._top_entity = IPFORWARDMIB()
        return self._top_entity



