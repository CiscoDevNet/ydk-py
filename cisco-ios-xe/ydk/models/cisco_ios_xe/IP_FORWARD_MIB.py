""" IP_FORWARD_MIB 

The MIB module for the display of CIDR multipath IP Routes.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IpForwardMib(object):
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
        self.ipcidrroutetable = IpForwardMib.Ipcidrroutetable()
        self.ipcidrroutetable.parent = self
        self.ipforward = IpForwardMib.Ipforward()
        self.ipforward.parent = self
        self.ipforwardtable = IpForwardMib.Ipforwardtable()
        self.ipforwardtable.parent = self


    class Ipforward(object):
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
            self.parent = None
            self.ipcidrroutenumber = None
            self.ipforwardnumber = None

        @property
        def _common_path(self):

            return '/IP-FORWARD-MIB:IP-FORWARD-MIB/IP-FORWARD-MIB:ipForward'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipcidrroutenumber is not None:
                return True

            if self.ipforwardnumber is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
            return meta._meta_table['IpForwardMib.Ipforward']['meta_info']


    class Ipforwardtable(object):
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
            self.parent = None
            self.ipforwardentry = YList()
            self.ipforwardentry.parent = self
            self.ipforwardentry.name = 'ipforwardentry'


        class Ipforwardentry(object):
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
            	**type**\:   :py:class:`IpforwardprotoEnum <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardprotoEnum>`
            
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
            	**type**\:   :py:class:`IpforwardtypeEnum <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardtypeEnum>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                self.parent = None
                self.ipforwarddest = None
                self.ipforwardproto = None
                self.ipforwardpolicy = None
                self.ipforwardnexthop = None
                self.ipforwardage = None
                self.ipforwardifindex = None
                self.ipforwardinfo = None
                self.ipforwardmask = None
                self.ipforwardmetric1 = None
                self.ipforwardmetric2 = None
                self.ipforwardmetric3 = None
                self.ipforwardmetric4 = None
                self.ipforwardmetric5 = None
                self.ipforwardnexthopas = None
                self.ipforwardtype = None

            class IpforwardprotoEnum(Enum):
                """
                IpforwardprotoEnum

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

                other = 1

                local = 2

                netmgmt = 3

                icmp = 4

                egp = 5

                ggp = 6

                hello = 7

                rip = 8

                is_is = 9

                es_is = 10

                ciscoIgrp = 11

                bbnSpfIgp = 12

                ospf = 13

                bgp = 14

                idpr = 15


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                    return meta._meta_table['IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardprotoEnum']


            class IpforwardtypeEnum(Enum):
                """
                IpforwardtypeEnum

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

                other = 1

                invalid = 2

                local = 3

                remote = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                    return meta._meta_table['IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardtypeEnum']


            @property
            def _common_path(self):
                if self.ipforwarddest is None:
                    raise YPYModelError('Key property ipforwarddest is None')
                if self.ipforwardproto is None:
                    raise YPYModelError('Key property ipforwardproto is None')
                if self.ipforwardpolicy is None:
                    raise YPYModelError('Key property ipforwardpolicy is None')
                if self.ipforwardnexthop is None:
                    raise YPYModelError('Key property ipforwardnexthop is None')

                return '/IP-FORWARD-MIB:IP-FORWARD-MIB/IP-FORWARD-MIB:ipForwardTable/IP-FORWARD-MIB:ipForwardEntry[IP-FORWARD-MIB:ipForwardDest = ' + str(self.ipforwarddest) + '][IP-FORWARD-MIB:ipForwardProto = ' + str(self.ipforwardproto) + '][IP-FORWARD-MIB:ipForwardPolicy = ' + str(self.ipforwardpolicy) + '][IP-FORWARD-MIB:ipForwardNextHop = ' + str(self.ipforwardnexthop) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipforwarddest is not None:
                    return True

                if self.ipforwardproto is not None:
                    return True

                if self.ipforwardpolicy is not None:
                    return True

                if self.ipforwardnexthop is not None:
                    return True

                if self.ipforwardage is not None:
                    return True

                if self.ipforwardifindex is not None:
                    return True

                if self.ipforwardinfo is not None:
                    return True

                if self.ipforwardmask is not None:
                    return True

                if self.ipforwardmetric1 is not None:
                    return True

                if self.ipforwardmetric2 is not None:
                    return True

                if self.ipforwardmetric3 is not None:
                    return True

                if self.ipforwardmetric4 is not None:
                    return True

                if self.ipforwardmetric5 is not None:
                    return True

                if self.ipforwardnexthopas is not None:
                    return True

                if self.ipforwardtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                return meta._meta_table['IpForwardMib.Ipforwardtable.Ipforwardentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-FORWARD-MIB:IP-FORWARD-MIB/IP-FORWARD-MIB:ipForwardTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipforwardentry is not None:
                for child_ref in self.ipforwardentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
            return meta._meta_table['IpForwardMib.Ipforwardtable']['meta_info']


    class Ipcidrroutetable(object):
        """
        This entity's IP Routing table.
        
        .. attribute:: ipcidrrouteentry
        
        	A particular route to  a  particular  destina\- tion, under a particular policy
        	**type**\: list of    :py:class:`Ipcidrrouteentry <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry>`
        
        

        """

        _prefix = 'IP-FORWARD-MIB'
        _revision = '1996-09-19'

        def __init__(self):
            self.parent = None
            self.ipcidrrouteentry = YList()
            self.ipcidrrouteentry.parent = self
            self.ipcidrrouteentry.name = 'ipcidrrouteentry'


        class Ipcidrrouteentry(object):
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
            	**type**\:   :py:class:`IpcidrrouteprotoEnum <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrrouteprotoEnum>`
            
            .. attribute:: ipcidrroutestatus
            
            	The row status variable, used according to row installation and removal conventions
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ipcidrroutetype
            
            	The type of route.  Note that local(3)  refers to  a route for which the next hop is the final destination; remote(4) refers to  a  route  for which  the  next  hop is not the final destina\- tion.  Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.   reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:   :py:class:`IpcidrroutetypeEnum <ydk.models.cisco_ios_xe.IP_FORWARD_MIB.IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrroutetypeEnum>`
            
            

            """

            _prefix = 'IP-FORWARD-MIB'
            _revision = '1996-09-19'

            def __init__(self):
                self.parent = None
                self.ipcidrroutedest = None
                self.ipcidrroutemask = None
                self.ipcidrroutetos = None
                self.ipcidrroutenexthop = None
                self.ipcidrrouteage = None
                self.ipcidrrouteifindex = None
                self.ipcidrrouteinfo = None
                self.ipcidrroutemetric1 = None
                self.ipcidrroutemetric2 = None
                self.ipcidrroutemetric3 = None
                self.ipcidrroutemetric4 = None
                self.ipcidrroutemetric5 = None
                self.ipcidrroutenexthopas = None
                self.ipcidrrouteproto = None
                self.ipcidrroutestatus = None
                self.ipcidrroutetype = None

            class IpcidrrouteprotoEnum(Enum):
                """
                IpcidrrouteprotoEnum

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

                other = 1

                local = 2

                netmgmt = 3

                icmp = 4

                egp = 5

                ggp = 6

                hello = 7

                rip = 8

                isIs = 9

                esIs = 10

                ciscoIgrp = 11

                bbnSpfIgp = 12

                ospf = 13

                bgp = 14

                idpr = 15

                ciscoEigrp = 16


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                    return meta._meta_table['IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrrouteprotoEnum']


            class IpcidrroutetypeEnum(Enum):
                """
                IpcidrroutetypeEnum

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

                other = 1

                reject = 2

                local = 3

                remote = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                    return meta._meta_table['IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrroutetypeEnum']


            @property
            def _common_path(self):
                if self.ipcidrroutedest is None:
                    raise YPYModelError('Key property ipcidrroutedest is None')
                if self.ipcidrroutemask is None:
                    raise YPYModelError('Key property ipcidrroutemask is None')
                if self.ipcidrroutetos is None:
                    raise YPYModelError('Key property ipcidrroutetos is None')
                if self.ipcidrroutenexthop is None:
                    raise YPYModelError('Key property ipcidrroutenexthop is None')

                return '/IP-FORWARD-MIB:IP-FORWARD-MIB/IP-FORWARD-MIB:ipCidrRouteTable/IP-FORWARD-MIB:ipCidrRouteEntry[IP-FORWARD-MIB:ipCidrRouteDest = ' + str(self.ipcidrroutedest) + '][IP-FORWARD-MIB:ipCidrRouteMask = ' + str(self.ipcidrroutemask) + '][IP-FORWARD-MIB:ipCidrRouteTos = ' + str(self.ipcidrroutetos) + '][IP-FORWARD-MIB:ipCidrRouteNextHop = ' + str(self.ipcidrroutenexthop) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipcidrroutedest is not None:
                    return True

                if self.ipcidrroutemask is not None:
                    return True

                if self.ipcidrroutetos is not None:
                    return True

                if self.ipcidrroutenexthop is not None:
                    return True

                if self.ipcidrrouteage is not None:
                    return True

                if self.ipcidrrouteifindex is not None:
                    return True

                if self.ipcidrrouteinfo is not None:
                    return True

                if self.ipcidrroutemetric1 is not None:
                    return True

                if self.ipcidrroutemetric2 is not None:
                    return True

                if self.ipcidrroutemetric3 is not None:
                    return True

                if self.ipcidrroutemetric4 is not None:
                    return True

                if self.ipcidrroutemetric5 is not None:
                    return True

                if self.ipcidrroutenexthopas is not None:
                    return True

                if self.ipcidrrouteproto is not None:
                    return True

                if self.ipcidrroutestatus is not None:
                    return True

                if self.ipcidrroutetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
                return meta._meta_table['IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-FORWARD-MIB:IP-FORWARD-MIB/IP-FORWARD-MIB:ipCidrRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipcidrrouteentry is not None:
                for child_ref in self.ipcidrrouteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
            return meta._meta_table['IpForwardMib.Ipcidrroutetable']['meta_info']

    @property
    def _common_path(self):

        return '/IP-FORWARD-MIB:IP-FORWARD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ipcidrroutetable is not None and self.ipcidrroutetable._has_data():
            return True

        if self.ipforward is not None and self.ipforward._has_data():
            return True

        if self.ipforwardtable is not None and self.ipforwardtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IP_FORWARD_MIB as meta
        return meta._meta_table['IpForwardMib']['meta_info']


