""" Cisco_IOS_XE_ipv6_oper 

This module contains a collection of YANG definitions
for IPv6 operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv6NdTdlState(Enum):
    """
    Ipv6NdTdlState (Enum Class)

    Indicate the current state of 

    the Neighbor\-Discovery entry.

    .. data:: ipv6_nd_incomplete = 0

    	Address resolution is in progress and the 

    	link-layer address of the neighbor has not

    	yet been determined.

    .. data:: ipv6_nd_reachable = 1

    	The neighbor is known to have been reachable

    	recently (within tens of seconds ago).

    .. data:: ipv6_nd_stale = 2

    	The neighbor is no longer known to be reachable

    	but until traffic is sent to the neighbor, no 

    	attempt should be made to verify its reachability

    .. data:: ipv6_nd_glean = 3

    	Received updated link-layer information. 

    	Behaviour like STALE.

    .. data:: ipv6_nd_delay = 4

    	The neighbor is no longer known to be reachable, and traffic

    	has recently been sent to the neighbor. Rather than probe the

    	neighbor immediately, however, delay sending probes for a short

    	while in order to give upper layer protocols a chance to provide

    	reachability confirmation.

    .. data:: ipv6_nd_probe = 5

    	The neighbor is no longer known to be reachable, and unicast

    	Neighbor Solicitation probes are being sent to verify 

    	reachability.

    .. data:: ipv6_nd_delete = 6

    	Entry is deleted.

    """

    ipv6_nd_incomplete = Enum.YLeaf(0, "ipv6-nd-incomplete")

    ipv6_nd_reachable = Enum.YLeaf(1, "ipv6-nd-reachable")

    ipv6_nd_stale = Enum.YLeaf(2, "ipv6-nd-stale")

    ipv6_nd_glean = Enum.YLeaf(3, "ipv6-nd-glean")

    ipv6_nd_delay = Enum.YLeaf(4, "ipv6-nd-delay")

    ipv6_nd_probe = Enum.YLeaf(5, "ipv6-nd-probe")

    ipv6_nd_delete = Enum.YLeaf(6, "ipv6-nd-delete")



class Ipv6Data(Entity):
    """
    Operational state of IPv6
    
    .. attribute:: nd6_info
    
    	List of IPv6 neighbors
    	**type**\: list of  		 :py:class:`Nd6Info <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ipv6_oper.Ipv6Data.Nd6Info>`
    
    

    """

    _prefix = 'ipv6-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(Ipv6Data, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-data"
        self.yang_parent_name = "Cisco-IOS-XE-ipv6-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("nd6-info", ("nd6_info", Ipv6Data.Nd6Info))])
        self._leafs = OrderedDict()

        self.nd6_info = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-ipv6-oper:ipv6-data"

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Data, [], name, value)


    class Nd6Info(Entity):
        """
        List of IPv6 neighbors
        
        .. attribute:: vrf_name  (key)
        
        	The Virtual Router and Forwarding instance that  this neighbor information is associated with
        	**type**\: str
        
        .. attribute:: if_name  (key)
        
        	The Interface name
        	**type**\: str
        
        .. attribute:: ip  (key)
        
        	IPv6 address of this neighbor entry
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: mac_address
        
        	MAC address
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: state
        
        	State of the entry
        	**type**\:  :py:class:`Ipv6NdTdlState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ipv6_oper.Ipv6NdTdlState>`
        
        .. attribute:: idle_timer
        
        	Time before expiration, in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: uptime
        
        	Indicates how long this neighbor entry has  been active, in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv6-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(Ipv6Data.Nd6Info, self).__init__()

            self.yang_name = "nd6-info"
            self.yang_parent_name = "ipv6-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf_name','if_name','ip']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('if_name', YLeaf(YType.str, 'if-name')),
                ('ip', YLeaf(YType.str, 'ip')),
                ('mac_address', YLeaf(YType.str, 'mac-address')),
                ('state', YLeaf(YType.enumeration, 'state')),
                ('idle_timer', YLeaf(YType.uint32, 'idle-timer')),
                ('uptime', YLeaf(YType.uint32, 'uptime')),
            ])
            self.vrf_name = None
            self.if_name = None
            self.ip = None
            self.mac_address = None
            self.state = None
            self.idle_timer = None
            self.uptime = None
            self._segment_path = lambda: "nd6-info" + "[vrf-name='" + str(self.vrf_name) + "']" + "[if-name='" + str(self.if_name) + "']" + "[ip='" + str(self.ip) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-ipv6-oper:ipv6-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Data.Nd6Info, ['vrf_name', 'if_name', 'ip', 'mac_address', 'state', 'idle_timer', 'uptime'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Data()
        return self._top_entity

