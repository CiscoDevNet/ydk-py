


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpForwardMib.Ipforward' : {
        'meta_info' : _MetaInfoClass('IpForwardMib.Ipforward',
            False, 
            [
            _MetaInfoClassMember('ipCidrRouteNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of current ipCidrRouteTable entries
                that are not invalid.
                ''',
                'ipcidrroutenumber',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of current  ipForwardTable  entries
                that are not invalid.
                ''',
                'ipforwardnumber',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'ipForward',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
    'IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardprotoEnum' : _MetaInfoEnum('IpforwardprotoEnum', 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'icmp':'icmp',
            'egp':'egp',
            'ggp':'ggp',
            'hello':'hello',
            'rip':'rip',
            'is-is':'is_is',
            'es-is':'es_is',
            'ciscoIgrp':'ciscoIgrp',
            'bbnSpfIgp':'bbnSpfIgp',
            'ospf':'ospf',
            'bgp':'bgp',
            'idpr':'idpr',
        }, 'IP-FORWARD-MIB', _yang_ns._namespaces['IP-FORWARD-MIB']),
    'IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardtypeEnum' : _MetaInfoEnum('IpforwardtypeEnum', 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB',
        {
            'other':'other',
            'invalid':'invalid',
            'local':'local',
            'remote':'remote',
        }, 'IP-FORWARD-MIB', _yang_ns._namespaces['IP-FORWARD-MIB']),
    'IpForwardMib.Ipforwardtable.Ipforwardentry' : {
        'meta_info' : _MetaInfoClass('IpForwardMib.Ipforwardtable.Ipforwardentry',
            False, 
            [
            _MetaInfoClassMember('ipForwardDest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of this route.   An
                entry  with  a value of 0.0.0.0 is considered a
                default route.
                
                This object may not take a Multicast (Class  D)
                address value.
                
                Any assignment (implicit or  otherwise)  of  an
                instance  of  this  object to a value x must be
                rejected if the bitwise logical-AND of  x  with
                the  value of the corresponding instance of the
                ipForwardMask object is not equal to x.
                ''',
                'ipforwarddest',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipForwardProto', REFERENCE_ENUM_CLASS, 'IpforwardprotoEnum' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardprotoEnum', 
                [], [], 
                '''                The routing mechanism via which this route was
                learned.  Inclusion of values for gateway rout-
                ing protocols is not  intended  to  imply  that
                hosts should support those protocols.
                ''',
                'ipforwardproto',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipForwardPolicy', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The general set of conditions that would cause
                the  selection  of  one multipath route (set of
                next hops for a given destination) is  referred
                to as 'policy'.
                
                Unless the mechanism indicated by ipForwardPro-
                to specifies otherwise, the policy specifier is
                the IP TOS Field.  The encoding of IP TOS is as
                 specified  by  the  following convention.  Zero
                indicates the default path if no more  specific
                policy applies.
                
                +-----+-----+-----+-----+-----+-----+-----+-----+
                |                 |                       |     |
                |   PRECEDENCE    |    TYPE OF SERVICE    |  0  |
                |                 |                       |     |
                +-----+-----+-----+-----+-----+-----+-----+-----+
                
                         IP TOS                IP TOS
                    Field     Policy      Field     Policy
                    Contents    Code      Contents    Code
                    0 0 0 0  ==>   0      0 0 0 1  ==>   2
                    0 0 1 0  ==>   4      0 0 1 1  ==>   6
                    0 1 0 0  ==>   8      0 1 0 1  ==>  10
                    0 1 1 0  ==>  12      0 1 1 1  ==>  14
                    1 0 0 0  ==>  16      1 0 0 1  ==>  18
                    1 0 1 0  ==>  20      1 0 1 1  ==>  22
                    1 1 0 0  ==>  24      1 1 0 1  ==>  26
                    1 1 1 0  ==>  28      1 1 1 1  ==>  30
                
                Protocols defining 'policy' otherwise must  ei-
                ther define a set of values which are valid for
                this  object  or  must  implement  an  integer-
                instanced  policy table for which this object's
                value acts as an index.
                ''',
                'ipforwardpolicy',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipForwardNextHop', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                On remote routes, the address of the next sys-
                tem en route; Otherwise, 0.0.0.0.
                ''',
                'ipforwardnexthop',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipForwardAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of seconds  since  this  route  was
                last  updated  or  otherwise  determined  to be
                correct.  Note that no semantics of  `too  old'
                can  be implied except through knowledge of the
                routing  protocol  by  which  the   route   was
                learned.
                ''',
                'ipforwardage',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ifIndex value which identifies  the  local
                interface  through  which  the next hop of this
                route should be reached.
                ''',
                'ipforwardifindex',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardInfo', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the
                particular  routing protocol which is responsi-
                ble for this route, as determined by the  value
                specified  in the route's ipForwardProto value.
                If this information is not present,  its  value
                should be set to the OBJECT IDENTIFIER { 0 0 },
                which is a syntactically valid object  identif-
                ier, and any implementation conforming to ASN.1
                and the Basic Encoding Rules must  be  able  to
                generate and recognize this value.
                ''',
                'ipforwardinfo',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Indicate the mask to be logical-ANDed with the
                destination  address  before  being compared to
                the value  in  the  ipForwardDest  field.   For
                those  systems  that  do  not support arbitrary
                subnet masks, an agent constructs the value  of
                the  ipForwardMask  by  reference to the IP Ad-
                dress Class.
                
                Any assignment (implicit or  otherwise)  of  an
                instance  of  this  object to a value x must be
                rejected if the bitwise logical-AND of  x  with
                the  value of the corresponding instance of the
                ipForwardDest object is not equal to ipForward-
                Dest.
                ''',
                'ipforwardmask',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMetric1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The primary routing  metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipForwardProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipforwardmetric1',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMetric2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipForwardProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipforwardmetric2',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMetric3', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipForwardProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipforwardmetric3',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMetric4', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipForwardProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipforwardmetric4',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardMetric5', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipForwardProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipforwardmetric5',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardNextHopAS', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Autonomous System Number of the Next  Hop.
                When  this  is  unknown  or not relevant to the
                protocol indicated by ipForwardProto, zero.
                ''',
                'ipforwardnexthopas',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardType', REFERENCE_ENUM_CLASS, 'IpforwardtypeEnum' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipforwardtable.Ipforwardentry.IpforwardtypeEnum', 
                [], [], 
                '''                The type of route.  Note that local(3)  refers
                to  a route for which the next hop is the final
                destination; remote(4) refers to  a  route  for
                which  the  next  hop is not the final destina-
                tion.
                
                Setting this object to the value invalid(2) has
                the  effect  of  invalidating the corresponding
                entry in the ipForwardTable object.   That  is,
                it  effectively  disassociates  the destination
                identified with said entry from the route iden-
                tified    with    said   entry.    It   is   an
                implementation-specific matter  as  to  whether
                the agent removes an invalidated entry from the
                table.  Accordingly, management  stations  must
                be prepared to receive tabular information from
                agents that corresponds to entries not current-
                ly  in  use.  Proper interpretation of such en-
                tries requires examination of the relevant  ip-
                ForwardType object.
                ''',
                'ipforwardtype',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'ipForwardEntry',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
    'IpForwardMib.Ipforwardtable' : {
        'meta_info' : _MetaInfoClass('IpForwardMib.Ipforwardtable',
            False, 
            [
            _MetaInfoClassMember('ipForwardEntry', REFERENCE_LIST, 'Ipforwardentry' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipforwardtable.Ipforwardentry', 
                [], [], 
                '''                A particular route to  a  particular  destina-
                tion, under a particular policy.
                ''',
                'ipforwardentry',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'ipForwardTable',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
    'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrrouteprotoEnum' : _MetaInfoEnum('IpcidrrouteprotoEnum', 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'icmp':'icmp',
            'egp':'egp',
            'ggp':'ggp',
            'hello':'hello',
            'rip':'rip',
            'isIs':'isIs',
            'esIs':'esIs',
            'ciscoIgrp':'ciscoIgrp',
            'bbnSpfIgp':'bbnSpfIgp',
            'ospf':'ospf',
            'bgp':'bgp',
            'idpr':'idpr',
            'ciscoEigrp':'ciscoEigrp',
        }, 'IP-FORWARD-MIB', _yang_ns._namespaces['IP-FORWARD-MIB']),
    'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrroutetypeEnum' : _MetaInfoEnum('IpcidrroutetypeEnum', 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB',
        {
            'other':'other',
            'reject':'reject',
            'local':'local',
            'remote':'remote',
        }, 'IP-FORWARD-MIB', _yang_ns._namespaces['IP-FORWARD-MIB']),
    'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry' : {
        'meta_info' : _MetaInfoClass('IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry',
            False, 
            [
            _MetaInfoClassMember('ipCidrRouteDest', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of this route.
                
                This object may not take a Multicast (Class  D)
                address value.
                
                Any assignment (implicit or  otherwise)  of  an
                instance  of  this  object to a value x must be
                rejected if the bitwise logical-AND of  x  with
                the  value of the corresponding instance of the
                ipCidrRouteMask object is not equal to x.
                ''',
                'ipcidrroutedest',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipCidrRouteMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Indicate the mask to be logical-ANDed with the
                destination  address  before  being compared to
                the value  in  the  ipCidrRouteDest  field.   For
                those  systems  that  do  not support arbitrary
                subnet masks, an agent constructs the value  of
                the  ipCidrRouteMask  by  reference to the IP Ad-
                dress Class.
                
                Any assignment (implicit or  otherwise)  of  an
                instance  of  this  object to a value x must be
                rejected if the bitwise logical-AND of  x  with
                the  value of the corresponding instance of the
                ipCidrRouteDest object is not equal to ipCidrRoute-
                Dest.
                ''',
                'ipcidrroutemask',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipCidrRouteTos', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The policy specifier is the IP TOS Field.  The encoding
                of IP TOS is as specified  by  the  following convention.
                Zero indicates the default path if no more  specific
                policy applies.
                
                +-----+-----+-----+-----+-----+-----+-----+-----+
                |                 |                       |     |
                |   PRECEDENCE    |    TYPE OF SERVICE    |  0  |
                |                 |                       |     |
                +-----+-----+-----+-----+-----+-----+-----+-----+
                
                         IP TOS                IP TOS
                    Field     Policy      Field     Policy
                    Contents    Code      Contents    Code
                    0 0 0 0  ==>   0      0 0 0 1  ==>   2
                    0 0 1 0  ==>   4      0 0 1 1  ==>   6
                    0 1 0 0  ==>   8      0 1 0 1  ==>  10
                    0 1 1 0  ==>  12      0 1 1 1  ==>  14
                    1 0 0 0  ==>  16      1 0 0 1  ==>  18
                    1 0 1 0  ==>  20      1 0 1 1  ==>  22
                    1 1 0 0  ==>  24      1 1 0 1  ==>  26
                    1 1 1 0  ==>  28      1 1 1 1  ==>  30
                ''',
                'ipcidrroutetos',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipCidrRouteNextHop', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                On remote routes, the address of the next sys-
                tem en route; Otherwise, 0.0.0.0.
                ''',
                'ipcidrroutenexthop',
                'IP-FORWARD-MIB', True),
            _MetaInfoClassMember('ipCidrRouteAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of seconds  since  this  route  was
                last  updated  or  otherwise  determined  to be
                correct.  Note that no semantics of  `too  old'
                can  be implied except through knowledge of the
                routing  protocol  by  which  the   route   was
                learned.
                ''',
                'ipcidrrouteage',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ifIndex value which identifies  the  local
                interface  through  which  the next hop of this
                route should be reached.
                ''',
                'ipcidrrouteifindex',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteInfo', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the
                particular  routing protocol which is responsi-
                ble for this route, as determined by the  value
                specified  in the route's ipCidrRouteProto value.
                If this information is not present,  its  value
                should be set to the OBJECT IDENTIFIER { 0 0 },
                which is a syntactically valid object  identif-
                ier, and any implementation conforming to ASN.1
                and the Basic Encoding Rules must  be  able  to
                generate and recognize this value.
                ''',
                'ipcidrrouteinfo',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteMetric1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The primary routing  metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipcidrroutemetric1',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteMetric2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipcidrroutemetric2',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteMetric3', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipcidrroutemetric3',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteMetric4', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipcidrroutemetric4',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteMetric5', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric  for  this  route.
                The  semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value.   If  this metric is not
                used, its value should be set to -1.
                ''',
                'ipcidrroutemetric5',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteNextHopAS', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Autonomous System Number of the Next  Hop.
                The  semantics of this object are determined by
                the routing-protocol specified in  the  route's
                ipCidrRouteProto  value. When  this object is
                unknown or not relevant its value should be set
                to zero.
                ''',
                'ipcidrroutenexthopas',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteProto', REFERENCE_ENUM_CLASS, 'IpcidrrouteprotoEnum' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrrouteprotoEnum', 
                [], [], 
                '''                The routing mechanism via which this route was
                learned.  Inclusion of values for gateway rout-
                ing protocols is not  intended  to  imply  that
                hosts should support those protocols.
                ''',
                'ipcidrrouteproto',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The row status variable, used according to
                row installation and removal conventions.
                ''',
                'ipcidrroutestatus',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipCidrRouteType', REFERENCE_ENUM_CLASS, 'IpcidrroutetypeEnum' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry.IpcidrroutetypeEnum', 
                [], [], 
                '''                The type of route.  Note that local(3)  refers
                to  a route for which the next hop is the final
                destination; remote(4) refers to  a  route  for
                which  the  next  hop is not the final destina-
                tion.
                
                Routes which do not result in traffic forwarding or
                rejection should not be displayed even if the
                implementation keeps them stored internally.
                
                
                reject (2) refers to a route which, if matched, discards
                the message as unreachable. This is used in some
                protocols as a means of correctly aggregating routes.
                ''',
                'ipcidrroutetype',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'ipCidrRouteEntry',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
    'IpForwardMib.Ipcidrroutetable' : {
        'meta_info' : _MetaInfoClass('IpForwardMib.Ipcidrroutetable',
            False, 
            [
            _MetaInfoClassMember('ipCidrRouteEntry', REFERENCE_LIST, 'Ipcidrrouteentry' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry', 
                [], [], 
                '''                A particular route to  a  particular  destina-
                tion, under a particular policy.
                ''',
                'ipcidrrouteentry',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'ipCidrRouteTable',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
    'IpForwardMib' : {
        'meta_info' : _MetaInfoClass('IpForwardMib',
            False, 
            [
            _MetaInfoClassMember('ipCidrRouteTable', REFERENCE_CLASS, 'Ipcidrroutetable' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipcidrroutetable', 
                [], [], 
                '''                This entity's IP Routing table.
                ''',
                'ipcidrroutetable',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForward', REFERENCE_CLASS, 'Ipforward' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipforward', 
                [], [], 
                '''                ''',
                'ipforward',
                'IP-FORWARD-MIB', False),
            _MetaInfoClassMember('ipForwardTable', REFERENCE_CLASS, 'Ipforwardtable' , 'ydk.models.cisco_ios_xe.IP_FORWARD_MIB', 'IpForwardMib.Ipforwardtable', 
                [], [], 
                '''                This entity's IP Routing table.
                ''',
                'ipforwardtable',
                'IP-FORWARD-MIB', False),
            ],
            'IP-FORWARD-MIB',
            'IP-FORWARD-MIB',
            _yang_ns._namespaces['IP-FORWARD-MIB'],
        'ydk.models.cisco_ios_xe.IP_FORWARD_MIB'
        ),
    },
}
_meta_table['IpForwardMib.Ipforwardtable.Ipforwardentry']['meta_info'].parent =_meta_table['IpForwardMib.Ipforwardtable']['meta_info']
_meta_table['IpForwardMib.Ipcidrroutetable.Ipcidrrouteentry']['meta_info'].parent =_meta_table['IpForwardMib.Ipcidrroutetable']['meta_info']
_meta_table['IpForwardMib.Ipforward']['meta_info'].parent =_meta_table['IpForwardMib']['meta_info']
_meta_table['IpForwardMib.Ipforwardtable']['meta_info'].parent =_meta_table['IpForwardMib']['meta_info']
_meta_table['IpForwardMib.Ipcidrroutetable']['meta_info'].parent =_meta_table['IpForwardMib']['meta_info']
