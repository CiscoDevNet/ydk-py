""" IP_FORWARD_MIB 

The MIB module for the display of CIDR multipath IP Routes.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpForwardMib(Entity):
    """
    
    
    .. attribute:: ipcidrroutetable
    
    	This entity's IP Routing table
    	**type**\:   :py:class:`Ipcidrroutetable <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable>`
    
    .. attribute:: ipforward
    
    	
    	**type**\:   :py:class:`Ipforward <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforward>`
    
    .. attribute:: ipforwardtable
    
    	This entity's IP Routing table
    	**type**\:   :py:class:`Ipforwardtable <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable>`
    
    	**status**\: obsolete
    
    

    """

    _prefix = 'IP-FORWARD-MIB'
    _revision = '1996-09-19'

    def __init__(self):
        super(IpForwardMib, self).__init__()
        self._top_entity = None

        self.yang_name = "IP-FORWARD-MIB"
        self.yang_parent_name = "IP-FORWARD-MIB"

        self.ipcidrroutetable = IpForwardMib.Ipcidrroutetable()
        self.ipcidrroutetable.parent = self
        self._children_name_map["ipcidrroutetable"] = "ipCidrRouteTable"
        self._children_yang_names.add("ipCidrRouteTable")

        self.ipforward = IpForwardMib.Ipforward()
        self.ipforward.parent = self
        self._children_name_map["ipforward"] = "ipForward"
        self._children_yang_names.add("ipForward")

        self.ipforwardtable = IpForwardMib.Ipforwardtable()
        self.ipforwardtable.parent = self
        self._children_name_map["ipforwardtable"] = "ipForwardTable"
        self._children_yang_names.add("ipForwardTable")


    class Ipforward(Entity):
        """
        
        
        .. attribute:: ipcidrroutenumber
        
        	The number of current ipCidrRouteTable entries that are not invalid
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipforwardnumber
        
        	The number of current  ipForwardTable  entries that are not invalid
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IpForwardMib.Ipforward, self).__init__()

            self.yang_name = "ipForward"
            self.yang_parent_name = "IP-FORWARD-MIB"

            self.ipcidrroutenumber = YLeaf(YType.uint32, "ipCidrRouteNumber")

            self.ipforwardnumber = YLeaf(YType.uint32, "ipForwardNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ipcidrroutenumber",
                            "ipforwardnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpForwardMib.Ipforward, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpForwardMib.Ipforward, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ipcidrroutenumber.is_set or
                self.ipforwardnumber.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ipcidrroutenumber.yfilter != YFilter.not_set or
                self.ipforwardnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipForward" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ipcidrroutenumber.is_set or self.ipcidrroutenumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipcidrroutenumber.get_name_leafdata())
            if (self.ipforwardnumber.is_set or self.ipforwardnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipforwardnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipCidrRouteNumber" or name == "ipForwardNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ipCidrRouteNumber"):
                self.ipcidrroutenumber = value
                self.ipcidrroutenumber.value_namespace = name_space
                self.ipcidrroutenumber.value_namespace_prefix = name_space_prefix
            if(value_path == "ipForwardNumber"):
                self.ipforwardnumber = value
                self.ipforwardnumber.value_namespace = name_space
                self.ipforwardnumber.value_namespace_prefix = name_space_prefix


    class Ipforwardtable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: ipforwardentry
        
        	A particular route to  a  particular  destina\- tion, under a particular policy
        	**type**\: list of    :py:class:`Ipforwardentry <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable.Ipforwardentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IpForwardMib.Ipforwardtable, self).__init__()

            self.yang_name = "ipForwardTable"
            self.yang_parent_name = "IP-FORWARD-MIB"

            self.ipforwardentry = YList(self)

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
                        super(IpForwardMib.Ipforwardtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpForwardMib.Ipforwardtable, self).__setattr__(name, value)


        class Ipforwardentry(Entity):
            """
            A particular route to  a  particular  destina\-
            tion, under a particular policy.
            
            .. attribute:: ipforwarddest  <key>
            
            	The destination IP address of this route.   An entry  with  a value of 0.0.0.0 is considered a default route.  This object may not take a Multicast (Class  D) address value.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipForwardMask object is not equal to x
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardproto  <key>
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:   :py:class:`Ipforwardproto <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable.Ipforwardentry.Ipforwardproto>`
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardpolicy  <key>
            
            	The general set of conditions that would cause the  selection  of  one multipath route (set of next hops for a given destination) is  referred to as 'policy'.  Unless the mechanism indicated by ipForwardPro\- to specifies otherwise, the policy specifier is the IP TOS Field.  The encoding of IP TOS is as  specified  by  the  following convention.  Zero indicates the default path if no more  specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+           IP TOS                IP TOS     Field     Policy      Field     Policy     Contents    Code      Contents    Code     0 0 0 0  ==>   0      0 0 0 1  ==>   2     0 0 1 0  ==>   4      0 0 1 1  ==>   6     0 1 0 0  ==>   8      0 1 0 1  ==>  10     0 1 1 0  ==>  12      0 1 1 1  ==>  14     1 0 0 0  ==>  16      1 0 0 1  ==>  18     1 0 1 0  ==>  20      1 0 1 1  ==>  22     1 1 0 0  ==>  24      1 1 0 1  ==>  26     1 1 1 0  ==>  28      1 1 1 1  ==>  30  Protocols defining 'policy' otherwise must  ei\- ther define a set of values which are valid for this  object  or  must  implement  an  integer\- instanced  policy table for which this object's value acts as an index
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardnexthop  <key>
            
            	On remote routes, the address of the next sys\- tem en route; Otherwise, 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardage
            
            	The number of seconds  since  this  route  was last  updated  or  otherwise  determined  to be correct.  Note that no semantics of  `too  old' can  be implied except through knowledge of the routing  protocol  by  which  the   route   was learned
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardifindex
            
            	The ifIndex value which identifies  the  local interface  through  which  the next hop of this route should be reached
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardinfo
            
            	A reference to MIB definitions specific to the particular  routing protocol which is responsi\- ble for this route, as determined by the  value specified  in the route's ipForwardProto value. If this information is not present,  its  value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object  identif\- ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must  be  able  to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmask
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  ipForwardDest  field.   For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value  of the  ipForwardMask  by  reference to the IP Ad\- dress Class.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipForwardDest object is not equal to ipForward\- Dest
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric1
            
            	The primary routing  metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric2
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric3
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric4
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardmetric5
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipForwardProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardnexthopas
            
            	The Autonomous System Number of the Next  Hop. When  this  is  unknown  or not relevant to the protocol indicated by ipForwardProto, zero
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: ipforwardtype
            
            	The type of route.  Note that local(3)  refers to  a route for which the next hop is the final destination; remote(4) refers to  a  route  for which  the  next  hop is not the final destina\- tion.  Setting this object to the value invalid(2) has the  effect  of  invalidating the corresponding entry in the ipForwardTable object.   That  is, it  effectively  disassociates  the destination identified with said entry from the route iden\- tified    with    said   entry.    It   is   an implementation\-specific matter  as  to  whether the agent removes an invalidated entry from the table.  Accordingly, management  stations  must be prepared to receive tabular information from agents that corresponds to entries not current\- ly  in  use.  Proper interpretation of such en\- tries requires examination of the relevant  ip\- ForwardType object
            	**type**\:   :py:class:`Ipforwardtype <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable.Ipforwardentry.Ipforwardtype>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                super(IpForwardMib.Ipforwardtable.Ipforwardentry, self).__init__()

                self.yang_name = "ipForwardEntry"
                self.yang_parent_name = "ipForwardTable"

                self.ipforwarddest = YLeaf(YType.str, "ipForwardDest")

                self.ipforwardproto = YLeaf(YType.enumeration, "ipForwardProto")

                self.ipforwardpolicy = YLeaf(YType.int32, "ipForwardPolicy")

                self.ipforwardnexthop = YLeaf(YType.str, "ipForwardNextHop")

                self.ipforwardage = YLeaf(YType.int32, "ipForwardAge")

                self.ipforwardifindex = YLeaf(YType.int32, "ipForwardIfIndex")

                self.ipforwardinfo = YLeaf(YType.str, "ipForwardInfo")

                self.ipforwardmask = YLeaf(YType.str, "ipForwardMask")

                self.ipforwardmetric1 = YLeaf(YType.int32, "ipForwardMetric1")

                self.ipforwardmetric2 = YLeaf(YType.int32, "ipForwardMetric2")

                self.ipforwardmetric3 = YLeaf(YType.int32, "ipForwardMetric3")

                self.ipforwardmetric4 = YLeaf(YType.int32, "ipForwardMetric4")

                self.ipforwardmetric5 = YLeaf(YType.int32, "ipForwardMetric5")

                self.ipforwardnexthopas = YLeaf(YType.int32, "ipForwardNextHopAS")

                self.ipforwardtype = YLeaf(YType.enumeration, "ipForwardType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipforwarddest",
                                "ipforwardproto",
                                "ipforwardpolicy",
                                "ipforwardnexthop",
                                "ipforwardage",
                                "ipforwardifindex",
                                "ipforwardinfo",
                                "ipforwardmask",
                                "ipforwardmetric1",
                                "ipforwardmetric2",
                                "ipforwardmetric3",
                                "ipforwardmetric4",
                                "ipforwardmetric5",
                                "ipforwardnexthopas",
                                "ipforwardtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpForwardMib.Ipforwardtable.Ipforwardentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpForwardMib.Ipforwardtable.Ipforwardentry, self).__setattr__(name, value)

            class Ipforwardproto(Enum):
                """
                Ipforwardproto

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


            class Ipforwardtype(Enum):
                """
                Ipforwardtype

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


            def has_data(self):
                return (
                    self.ipforwarddest.is_set or
                    self.ipforwardproto.is_set or
                    self.ipforwardpolicy.is_set or
                    self.ipforwardnexthop.is_set or
                    self.ipforwardage.is_set or
                    self.ipforwardifindex.is_set or
                    self.ipforwardinfo.is_set or
                    self.ipforwardmask.is_set or
                    self.ipforwardmetric1.is_set or
                    self.ipforwardmetric2.is_set or
                    self.ipforwardmetric3.is_set or
                    self.ipforwardmetric4.is_set or
                    self.ipforwardmetric5.is_set or
                    self.ipforwardnexthopas.is_set or
                    self.ipforwardtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipforwarddest.yfilter != YFilter.not_set or
                    self.ipforwardproto.yfilter != YFilter.not_set or
                    self.ipforwardpolicy.yfilter != YFilter.not_set or
                    self.ipforwardnexthop.yfilter != YFilter.not_set or
                    self.ipforwardage.yfilter != YFilter.not_set or
                    self.ipforwardifindex.yfilter != YFilter.not_set or
                    self.ipforwardinfo.yfilter != YFilter.not_set or
                    self.ipforwardmask.yfilter != YFilter.not_set or
                    self.ipforwardmetric1.yfilter != YFilter.not_set or
                    self.ipforwardmetric2.yfilter != YFilter.not_set or
                    self.ipforwardmetric3.yfilter != YFilter.not_set or
                    self.ipforwardmetric4.yfilter != YFilter.not_set or
                    self.ipforwardmetric5.yfilter != YFilter.not_set or
                    self.ipforwardnexthopas.yfilter != YFilter.not_set or
                    self.ipforwardtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipForwardEntry" + "[ipForwardDest='" + self.ipforwarddest.get() + "']" + "[ipForwardProto='" + self.ipforwardproto.get() + "']" + "[ipForwardPolicy='" + self.ipforwardpolicy.get() + "']" + "[ipForwardNextHop='" + self.ipforwardnexthop.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB/ipForwardTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipforwarddest.is_set or self.ipforwarddest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwarddest.get_name_leafdata())
                if (self.ipforwardproto.is_set or self.ipforwardproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardproto.get_name_leafdata())
                if (self.ipforwardpolicy.is_set or self.ipforwardpolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardpolicy.get_name_leafdata())
                if (self.ipforwardnexthop.is_set or self.ipforwardnexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardnexthop.get_name_leafdata())
                if (self.ipforwardage.is_set or self.ipforwardage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardage.get_name_leafdata())
                if (self.ipforwardifindex.is_set or self.ipforwardifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardifindex.get_name_leafdata())
                if (self.ipforwardinfo.is_set or self.ipforwardinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardinfo.get_name_leafdata())
                if (self.ipforwardmask.is_set or self.ipforwardmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmask.get_name_leafdata())
                if (self.ipforwardmetric1.is_set or self.ipforwardmetric1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmetric1.get_name_leafdata())
                if (self.ipforwardmetric2.is_set or self.ipforwardmetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmetric2.get_name_leafdata())
                if (self.ipforwardmetric3.is_set or self.ipforwardmetric3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmetric3.get_name_leafdata())
                if (self.ipforwardmetric4.is_set or self.ipforwardmetric4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmetric4.get_name_leafdata())
                if (self.ipforwardmetric5.is_set or self.ipforwardmetric5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardmetric5.get_name_leafdata())
                if (self.ipforwardnexthopas.is_set or self.ipforwardnexthopas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardnexthopas.get_name_leafdata())
                if (self.ipforwardtype.is_set or self.ipforwardtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipforwardtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipForwardDest" or name == "ipForwardProto" or name == "ipForwardPolicy" or name == "ipForwardNextHop" or name == "ipForwardAge" or name == "ipForwardIfIndex" or name == "ipForwardInfo" or name == "ipForwardMask" or name == "ipForwardMetric1" or name == "ipForwardMetric2" or name == "ipForwardMetric3" or name == "ipForwardMetric4" or name == "ipForwardMetric5" or name == "ipForwardNextHopAS" or name == "ipForwardType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipForwardDest"):
                    self.ipforwarddest = value
                    self.ipforwarddest.value_namespace = name_space
                    self.ipforwarddest.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardProto"):
                    self.ipforwardproto = value
                    self.ipforwardproto.value_namespace = name_space
                    self.ipforwardproto.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardPolicy"):
                    self.ipforwardpolicy = value
                    self.ipforwardpolicy.value_namespace = name_space
                    self.ipforwardpolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardNextHop"):
                    self.ipforwardnexthop = value
                    self.ipforwardnexthop.value_namespace = name_space
                    self.ipforwardnexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardAge"):
                    self.ipforwardage = value
                    self.ipforwardage.value_namespace = name_space
                    self.ipforwardage.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardIfIndex"):
                    self.ipforwardifindex = value
                    self.ipforwardifindex.value_namespace = name_space
                    self.ipforwardifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardInfo"):
                    self.ipforwardinfo = value
                    self.ipforwardinfo.value_namespace = name_space
                    self.ipforwardinfo.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMask"):
                    self.ipforwardmask = value
                    self.ipforwardmask.value_namespace = name_space
                    self.ipforwardmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMetric1"):
                    self.ipforwardmetric1 = value
                    self.ipforwardmetric1.value_namespace = name_space
                    self.ipforwardmetric1.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMetric2"):
                    self.ipforwardmetric2 = value
                    self.ipforwardmetric2.value_namespace = name_space
                    self.ipforwardmetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMetric3"):
                    self.ipforwardmetric3 = value
                    self.ipforwardmetric3.value_namespace = name_space
                    self.ipforwardmetric3.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMetric4"):
                    self.ipforwardmetric4 = value
                    self.ipforwardmetric4.value_namespace = name_space
                    self.ipforwardmetric4.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardMetric5"):
                    self.ipforwardmetric5 = value
                    self.ipforwardmetric5.value_namespace = name_space
                    self.ipforwardmetric5.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardNextHopAS"):
                    self.ipforwardnexthopas = value
                    self.ipforwardnexthopas.value_namespace = name_space
                    self.ipforwardnexthopas.value_namespace_prefix = name_space_prefix
                if(value_path == "ipForwardType"):
                    self.ipforwardtype = value
                    self.ipforwardtype.value_namespace = name_space
                    self.ipforwardtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipforwardentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipforwardentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipForwardTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipForwardEntry"):
                for c in self.ipforwardentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpForwardMib.Ipforwardtable.Ipforwardentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipforwardentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipForwardEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipcidrroutetable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: ipcidrrouteentry
        
        	A particular route to  a  particular  destina\- tion, under a particular policy
        	**type**\: list of    :py:class:`Ipcidrrouteentry <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry>`
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            super(IpForwardMib.Ipcidrroutetable, self).__init__()

            self.yang_name = "ipCidrRouteTable"
            self.yang_parent_name = "IP-FORWARD-MIB"

            self.ipcidrrouteentry = YList(self)

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
                        super(IpForwardMib.Ipcidrroutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpForwardMib.Ipcidrroutetable, self).__setattr__(name, value)


        class Ipcidrrouteentry(Entity):
            """
            A particular route to  a  particular  destina\-
            tion, under a particular policy.
            
            .. attribute:: ipcidrroutedest  <key>
            
            	The destination IP address of this route.  This object may not take a Multicast (Class  D) address value.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipCidrRouteMask object is not equal to x
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipcidrroutemask  <key>
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  ipCidrRouteDest  field.   For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value  of the  ipCidrRouteMask  by  reference to the IP Ad\- dress Class.  Any assignment (implicit or  otherwise)  of  an instance  of  this  object to a value x must be rejected if the bitwise logical\-AND of  x  with the  value of the corresponding instance of the ipCidrRouteDest object is not equal to ipCidrRoute\- Dest
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipcidrroutetos  <key>
            
            	The policy specifier is the IP TOS Field.  The encoding of IP TOS is as specified  by  the  following convention. Zero indicates the default path if no more  specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+           IP TOS                IP TOS     Field     Policy      Field     Policy     Contents    Code      Contents    Code     0 0 0 0  ==>   0      0 0 0 1  ==>   2     0 0 1 0  ==>   4      0 0 1 1  ==>   6     0 1 0 0  ==>   8      0 1 0 1  ==>  10     0 1 1 0  ==>  12      0 1 1 1  ==>  14     1 0 0 0  ==>  16      1 0 0 1  ==>  18     1 0 1 0  ==>  20      1 0 1 1  ==>  22     1 1 0 0  ==>  24      1 1 0 1  ==>  26     1 1 1 0  ==>  28      1 1 1 1  ==>  30
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutenexthop  <key>
            
            	On remote routes, the address of the next sys\- tem en route; Otherwise, 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipcidrrouteage
            
            	The number of seconds  since  this  route  was last  updated  or  otherwise  determined  to be correct.  Note that no semantics of  `too  old' can  be implied except through knowledge of the routing  protocol  by  which  the   route   was learned
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrrouteifindex
            
            	The ifIndex value which identifies  the  local interface  through  which  the next hop of this route should be reached
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrrouteinfo
            
            	A reference to MIB definitions specific to the particular  routing protocol which is responsi\- ble for this route, as determined by the  value specified  in the route's ipCidrRouteProto value. If this information is not present,  its  value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object  identif\- ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must  be  able  to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ipcidrroutemetric1
            
            	The primary routing  metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutemetric2
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutemetric3
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutemetric4
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutemetric5
            
            	An alternate routing metric  for  this  route. The  semantics of this metric are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value.   If  this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrroutenexthopas
            
            	The Autonomous System Number of the Next  Hop. The  semantics of this object are determined by the routing\-protocol specified in  the  route's ipCidrRouteProto  value. When  this object is unknown or not relevant its value should be set to zero
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipcidrrouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:   :py:class:`Ipcidrrouteproto <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.Ipcidrrouteproto>`
            
            .. attribute:: ipcidrroutestatus
            
            	The row status variable, used according to row installation and removal conventions
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ipcidrroutetype
            
            	The type of route.  Note that local(3)  refers to  a route for which the next hop is the final destination; remote(4) refers to  a  route  for which  the  next  hop is not the final destina\- tion.  Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.   reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:   :py:class:`Ipcidrroutetype <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.Ipcidrroutetype>`
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                super(IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry, self).__init__()

                self.yang_name = "ipCidrRouteEntry"
                self.yang_parent_name = "ipCidrRouteTable"

                self.ipcidrroutedest = YLeaf(YType.str, "ipCidrRouteDest")

                self.ipcidrroutemask = YLeaf(YType.str, "ipCidrRouteMask")

                self.ipcidrroutetos = YLeaf(YType.int32, "ipCidrRouteTos")

                self.ipcidrroutenexthop = YLeaf(YType.str, "ipCidrRouteNextHop")

                self.ipcidrrouteage = YLeaf(YType.int32, "ipCidrRouteAge")

                self.ipcidrrouteifindex = YLeaf(YType.int32, "ipCidrRouteIfIndex")

                self.ipcidrrouteinfo = YLeaf(YType.str, "ipCidrRouteInfo")

                self.ipcidrroutemetric1 = YLeaf(YType.int32, "ipCidrRouteMetric1")

                self.ipcidrroutemetric2 = YLeaf(YType.int32, "ipCidrRouteMetric2")

                self.ipcidrroutemetric3 = YLeaf(YType.int32, "ipCidrRouteMetric3")

                self.ipcidrroutemetric4 = YLeaf(YType.int32, "ipCidrRouteMetric4")

                self.ipcidrroutemetric5 = YLeaf(YType.int32, "ipCidrRouteMetric5")

                self.ipcidrroutenexthopas = YLeaf(YType.int32, "ipCidrRouteNextHopAS")

                self.ipcidrrouteproto = YLeaf(YType.enumeration, "ipCidrRouteProto")

                self.ipcidrroutestatus = YLeaf(YType.enumeration, "ipCidrRouteStatus")

                self.ipcidrroutetype = YLeaf(YType.enumeration, "ipCidrRouteType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipcidrroutedest",
                                "ipcidrroutemask",
                                "ipcidrroutetos",
                                "ipcidrroutenexthop",
                                "ipcidrrouteage",
                                "ipcidrrouteifindex",
                                "ipcidrrouteinfo",
                                "ipcidrroutemetric1",
                                "ipcidrroutemetric2",
                                "ipcidrroutemetric3",
                                "ipcidrroutemetric4",
                                "ipcidrroutemetric5",
                                "ipcidrroutenexthopas",
                                "ipcidrrouteproto",
                                "ipcidrroutestatus",
                                "ipcidrroutetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry, self).__setattr__(name, value)

            class Ipcidrrouteproto(Enum):
                """
                Ipcidrrouteproto

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


            class Ipcidrroutetype(Enum):
                """
                Ipcidrroutetype

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


            def has_data(self):
                return (
                    self.ipcidrroutedest.is_set or
                    self.ipcidrroutemask.is_set or
                    self.ipcidrroutetos.is_set or
                    self.ipcidrroutenexthop.is_set or
                    self.ipcidrrouteage.is_set or
                    self.ipcidrrouteifindex.is_set or
                    self.ipcidrrouteinfo.is_set or
                    self.ipcidrroutemetric1.is_set or
                    self.ipcidrroutemetric2.is_set or
                    self.ipcidrroutemetric3.is_set or
                    self.ipcidrroutemetric4.is_set or
                    self.ipcidrroutemetric5.is_set or
                    self.ipcidrroutenexthopas.is_set or
                    self.ipcidrrouteproto.is_set or
                    self.ipcidrroutestatus.is_set or
                    self.ipcidrroutetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipcidrroutedest.yfilter != YFilter.not_set or
                    self.ipcidrroutemask.yfilter != YFilter.not_set or
                    self.ipcidrroutetos.yfilter != YFilter.not_set or
                    self.ipcidrroutenexthop.yfilter != YFilter.not_set or
                    self.ipcidrrouteage.yfilter != YFilter.not_set or
                    self.ipcidrrouteifindex.yfilter != YFilter.not_set or
                    self.ipcidrrouteinfo.yfilter != YFilter.not_set or
                    self.ipcidrroutemetric1.yfilter != YFilter.not_set or
                    self.ipcidrroutemetric2.yfilter != YFilter.not_set or
                    self.ipcidrroutemetric3.yfilter != YFilter.not_set or
                    self.ipcidrroutemetric4.yfilter != YFilter.not_set or
                    self.ipcidrroutemetric5.yfilter != YFilter.not_set or
                    self.ipcidrroutenexthopas.yfilter != YFilter.not_set or
                    self.ipcidrrouteproto.yfilter != YFilter.not_set or
                    self.ipcidrroutestatus.yfilter != YFilter.not_set or
                    self.ipcidrroutetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipCidrRouteEntry" + "[ipCidrRouteDest='" + self.ipcidrroutedest.get() + "']" + "[ipCidrRouteMask='" + self.ipcidrroutemask.get() + "']" + "[ipCidrRouteTos='" + self.ipcidrroutetos.get() + "']" + "[ipCidrRouteNextHop='" + self.ipcidrroutenexthop.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB/ipCidrRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipcidrroutedest.is_set or self.ipcidrroutedest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutedest.get_name_leafdata())
                if (self.ipcidrroutemask.is_set or self.ipcidrroutemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemask.get_name_leafdata())
                if (self.ipcidrroutetos.is_set or self.ipcidrroutetos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutetos.get_name_leafdata())
                if (self.ipcidrroutenexthop.is_set or self.ipcidrroutenexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutenexthop.get_name_leafdata())
                if (self.ipcidrrouteage.is_set or self.ipcidrrouteage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrrouteage.get_name_leafdata())
                if (self.ipcidrrouteifindex.is_set or self.ipcidrrouteifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrrouteifindex.get_name_leafdata())
                if (self.ipcidrrouteinfo.is_set or self.ipcidrrouteinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrrouteinfo.get_name_leafdata())
                if (self.ipcidrroutemetric1.is_set or self.ipcidrroutemetric1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemetric1.get_name_leafdata())
                if (self.ipcidrroutemetric2.is_set or self.ipcidrroutemetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemetric2.get_name_leafdata())
                if (self.ipcidrroutemetric3.is_set or self.ipcidrroutemetric3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemetric3.get_name_leafdata())
                if (self.ipcidrroutemetric4.is_set or self.ipcidrroutemetric4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemetric4.get_name_leafdata())
                if (self.ipcidrroutemetric5.is_set or self.ipcidrroutemetric5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutemetric5.get_name_leafdata())
                if (self.ipcidrroutenexthopas.is_set or self.ipcidrroutenexthopas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutenexthopas.get_name_leafdata())
                if (self.ipcidrrouteproto.is_set or self.ipcidrrouteproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrrouteproto.get_name_leafdata())
                if (self.ipcidrroutestatus.is_set or self.ipcidrroutestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutestatus.get_name_leafdata())
                if (self.ipcidrroutetype.is_set or self.ipcidrroutetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipcidrroutetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipCidrRouteDest" or name == "ipCidrRouteMask" or name == "ipCidrRouteTos" or name == "ipCidrRouteNextHop" or name == "ipCidrRouteAge" or name == "ipCidrRouteIfIndex" or name == "ipCidrRouteInfo" or name == "ipCidrRouteMetric1" or name == "ipCidrRouteMetric2" or name == "ipCidrRouteMetric3" or name == "ipCidrRouteMetric4" or name == "ipCidrRouteMetric5" or name == "ipCidrRouteNextHopAS" or name == "ipCidrRouteProto" or name == "ipCidrRouteStatus" or name == "ipCidrRouteType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipCidrRouteDest"):
                    self.ipcidrroutedest = value
                    self.ipcidrroutedest.value_namespace = name_space
                    self.ipcidrroutedest.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMask"):
                    self.ipcidrroutemask = value
                    self.ipcidrroutemask.value_namespace = name_space
                    self.ipcidrroutemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteTos"):
                    self.ipcidrroutetos = value
                    self.ipcidrroutetos.value_namespace = name_space
                    self.ipcidrroutetos.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteNextHop"):
                    self.ipcidrroutenexthop = value
                    self.ipcidrroutenexthop.value_namespace = name_space
                    self.ipcidrroutenexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteAge"):
                    self.ipcidrrouteage = value
                    self.ipcidrrouteage.value_namespace = name_space
                    self.ipcidrrouteage.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteIfIndex"):
                    self.ipcidrrouteifindex = value
                    self.ipcidrrouteifindex.value_namespace = name_space
                    self.ipcidrrouteifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteInfo"):
                    self.ipcidrrouteinfo = value
                    self.ipcidrrouteinfo.value_namespace = name_space
                    self.ipcidrrouteinfo.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMetric1"):
                    self.ipcidrroutemetric1 = value
                    self.ipcidrroutemetric1.value_namespace = name_space
                    self.ipcidrroutemetric1.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMetric2"):
                    self.ipcidrroutemetric2 = value
                    self.ipcidrroutemetric2.value_namespace = name_space
                    self.ipcidrroutemetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMetric3"):
                    self.ipcidrroutemetric3 = value
                    self.ipcidrroutemetric3.value_namespace = name_space
                    self.ipcidrroutemetric3.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMetric4"):
                    self.ipcidrroutemetric4 = value
                    self.ipcidrroutemetric4.value_namespace = name_space
                    self.ipcidrroutemetric4.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteMetric5"):
                    self.ipcidrroutemetric5 = value
                    self.ipcidrroutemetric5.value_namespace = name_space
                    self.ipcidrroutemetric5.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteNextHopAS"):
                    self.ipcidrroutenexthopas = value
                    self.ipcidrroutenexthopas.value_namespace = name_space
                    self.ipcidrroutenexthopas.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteProto"):
                    self.ipcidrrouteproto = value
                    self.ipcidrrouteproto.value_namespace = name_space
                    self.ipcidrrouteproto.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteStatus"):
                    self.ipcidrroutestatus = value
                    self.ipcidrroutestatus.value_namespace = name_space
                    self.ipcidrroutestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipCidrRouteType"):
                    self.ipcidrroutetype = value
                    self.ipcidrroutetype.value_namespace = name_space
                    self.ipcidrroutetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipcidrrouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipcidrrouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipCidrRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipCidrRouteEntry"):
                for c in self.ipcidrrouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipcidrrouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipCidrRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ipcidrroutetable is not None and self.ipcidrroutetable.has_data()) or
            (self.ipforward is not None and self.ipforward.has_data()) or
            (self.ipforwardtable is not None and self.ipforwardtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ipcidrroutetable is not None and self.ipcidrroutetable.has_operation()) or
            (self.ipforward is not None and self.ipforward.has_operation()) or
            (self.ipforwardtable is not None and self.ipforwardtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "IP-FORWARD-MIB:IP-FORWARD-MIB" + path_buffer

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

        if (child_yang_name == "ipCidrRouteTable"):
            if (self.ipcidrroutetable is None):
                self.ipcidrroutetable = IpForwardMib.Ipcidrroutetable()
                self.ipcidrroutetable.parent = self
                self._children_name_map["ipcidrroutetable"] = "ipCidrRouteTable"
            return self.ipcidrroutetable

        if (child_yang_name == "ipForward"):
            if (self.ipforward is None):
                self.ipforward = IpForwardMib.Ipforward()
                self.ipforward.parent = self
                self._children_name_map["ipforward"] = "ipForward"
            return self.ipforward

        if (child_yang_name == "ipForwardTable"):
            if (self.ipforwardtable is None):
                self.ipforwardtable = IpForwardMib.Ipforwardtable()
                self.ipforwardtable.parent = self
                self._children_name_map["ipforwardtable"] = "ipForwardTable"
            return self.ipforwardtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipCidrRouteTable" or name == "ipForward" or name == "ipForwardTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpForwardMib()
        return self._top_entity

