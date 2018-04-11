""" BGP4_MIB 

The MIB module for BGP\-4.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BGP4MIB(Entity):
    """
    
    
    .. attribute:: bgp
    
    	
    	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp>`
    
    .. attribute:: bgppeertable
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\:  :py:class:`Bgppeertable <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable>`
    
    .. attribute:: bgprcvdpathattrtable
    
    	The BGP Received Path Attribute Table contains information about paths to destination networks received from all peers running BGP version 3 or less
    	**type**\:  :py:class:`Bgprcvdpathattrtable <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgprcvdpathattrtable>`
    
    	**status**\: obsolete
    
    .. attribute:: bgp4pathattrtable
    
    	The BGP\-4 Received Path Attribute Table contains information about paths to destination networks received from all BGP4 peers
    	**type**\:  :py:class:`Bgp4Pathattrtable <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp4Pathattrtable>`
    
    

    """

    _prefix = 'BGP4-MIB'
    _revision = '1994-05-05'

    def __init__(self):
        super(BGP4MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "BGP4-MIB"
        self.yang_parent_name = "BGP4-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("bgp", ("bgp", BGP4MIB.Bgp)), ("bgpPeerTable", ("bgppeertable", BGP4MIB.Bgppeertable)), ("bgpRcvdPathAttrTable", ("bgprcvdpathattrtable", BGP4MIB.Bgprcvdpathattrtable)), ("bgp4PathAttrTable", ("bgp4pathattrtable", BGP4MIB.Bgp4Pathattrtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.bgp = BGP4MIB.Bgp()
        self.bgp.parent = self
        self._children_name_map["bgp"] = "bgp"
        self._children_yang_names.add("bgp")

        self.bgppeertable = BGP4MIB.Bgppeertable()
        self.bgppeertable.parent = self
        self._children_name_map["bgppeertable"] = "bgpPeerTable"
        self._children_yang_names.add("bgpPeerTable")

        self.bgprcvdpathattrtable = BGP4MIB.Bgprcvdpathattrtable()
        self.bgprcvdpathattrtable.parent = self
        self._children_name_map["bgprcvdpathattrtable"] = "bgpRcvdPathAttrTable"
        self._children_yang_names.add("bgpRcvdPathAttrTable")

        self.bgp4pathattrtable = BGP4MIB.Bgp4Pathattrtable()
        self.bgp4pathattrtable.parent = self
        self._children_name_map["bgp4pathattrtable"] = "bgp4PathAttrTable"
        self._children_yang_names.add("bgp4PathAttrTable")
        self._segment_path = lambda: "BGP4-MIB:BGP4-MIB"


    class Bgp(Entity):
        """
        
        
        .. attribute:: bgpversion
        
        	Vector of supported BGP protocol version numbers.  Each peer negotiates the version from this vector.  Versions are identified via the string of bits contained within this object.  The first octet contains bits 0 to 7, the second octet contains bits 8 to 15, and so on, with the most significant bit referring to the lowest bit number in the octet (e.g., the MSB of the first octet refers to bit 0).  If a bit, i, is present and set, then the version (i+1) of the BGP is supported
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: bgplocalas
        
        	The local autonomous system number
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: bgpidentifier
        
        	The BGP Identifier of local system
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            super(BGP4MIB.Bgp, self).__init__()

            self.yang_name = "bgp"
            self.yang_parent_name = "BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bgpversion', YLeaf(YType.str, 'bgpVersion')),
                ('bgplocalas', YLeaf(YType.int32, 'bgpLocalAs')),
                ('bgpidentifier', YLeaf(YType.str, 'bgpIdentifier')),
            ])
            self.bgpversion = None
            self.bgplocalas = None
            self.bgpidentifier = None
            self._segment_path = lambda: "bgp"
            self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BGP4MIB.Bgp, ['bgpversion', 'bgplocalas', 'bgpidentifier'], name, value)


    class Bgppeertable(Entity):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: bgppeerentry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of  		 :py:class:`Bgppeerentry <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry>`
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            super(BGP4MIB.Bgppeertable, self).__init__()

            self.yang_name = "bgpPeerTable"
            self.yang_parent_name = "BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bgpPeerEntry", ("bgppeerentry", BGP4MIB.Bgppeertable.Bgppeerentry))])
            self._leafs = OrderedDict()

            self.bgppeerentry = YList(self)
            self._segment_path = lambda: "bgpPeerTable"
            self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BGP4MIB.Bgppeertable, [], name, value)


        class Bgppeerentry(Entity):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	The remote IP address of this entry's BGP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeeridentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeerstate
            
            	The BGP peer connection state
            	**type**\:  :py:class:`Bgppeerstate <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry.Bgppeerstate>`
            
            .. attribute:: bgppeeradminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:  :py:class:`Bgppeeradminstatus <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry.Bgppeeradminstatus>`
            
            .. attribute:: bgppeernegotiatedversion
            
            	The negotiated version of BGP running between the two peers
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: bgppeerlocaladdr
            
            	The local IP address of this entry's BGP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeerlocalport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerremoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects bgpPeerLocalAddr, bgpPeerLocalPort, bgpPeerRemoteAddr and bgpPeerRemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerremoteas
            
            	The remote autonomous system number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerinupdates
            
            	The number of BGP UPDATE messages received on this connection.  This object should be initialized to zero (0) when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeeroutupdates
            
            	The number of BGP UPDATE messages transmitted on this connection.  This object should be initialized to zero (0) when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerintotalmessages
            
            	The total number of messages received from the remote peer on this connection. This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerouttotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerlasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\: str
            
            	**length:** 2
            
            .. attribute:: bgppeerfsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerfsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state.  It is set to zero when a new peer is configured or the router is booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerconnectretryinterval
            
            	Time interval in seconds for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeerholdtime
            
            	Time interval in seconds for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker by using the smaller of the value in bgpPeerHoldTimeConfigured and the Hold Time received in the OPEN message. This value must be at lease three seconds if it is not zero (0) in which case the Hold Timer has not been established with the peer, or, the value of bgpPeerHoldTimeConfigured is zero (0)
            	**type**\: int
            
            	**range:** 0..None \| 3..65535
            
            .. attribute:: bgppeerkeepalive
            
            	Time interval in seconds for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with bgpPeerHoldTime, it has the same proportion as what bgpPeerKeepAliveConfigured has when compared with bgpPeerHoldTimeConfigured. If the value of this object is zero (0), it indicates that the KeepAlive timer has not been established with the peer, or, the value of bgpPeerKeepAliveConfigured is zero (0)
            	**type**\: int
            
            	**range:** 0..21845
            
            .. attribute:: bgppeerholdtimeconfigured
            
            	Time interval in seconds for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (bgpPeerHoldTime) with the peer. This value must not be less than three seconds if it is not zero (0) in which case the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\: int
            
            	**range:** 0..None \| 3..65535
            
            .. attribute:: bgppeerkeepaliveconfigured
            
            	Time interval in seconds for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in bgpPeerHoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by bgpPeerKeepAlive.  A reasonable maximum value for this timer would be configured to be one third of that of bgpPeerHoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\: int
            
            	**range:** 0..21845
            
            .. attribute:: bgppeerminasoriginationinterval
            
            	Time interval in seconds for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeerminrouteadvertisementinterval
            
            	Time interval in seconds for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeerinupdateelapsedtime
            
            	Elapsed time in seconds since the last BGP UPDATE message was received from the peer. Each time bgpPeerInUpdates is incremented, the value of this object is set to zero (0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerprefixaccepted
            
            	Number of Route prefixes received on this connnection, which are accepted after applying filters. Possible filters are route maps, prefix lists, distributed lists, etc
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixdenied
            
            	Counter which gets incremented when a route prefix received on this connection is denied  or when a route prefix is denied during soft reset of this connection if 'soft\-reconfiguration' is on . This object is  initialized to zero when the peer is  configured or the router is rebooted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixlimit
            
            	Max number of route prefixes accepted on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixadvertised
            
            	Counter which gets incremented when a route prefix is advertised on this connection. This object is initialized to zero when the peer is configured or  the router is rebooted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixsuppressed
            
            	Counter which gets incremented when a route prefix is suppressed from being sent on this connection. This  object is initialized to zero when the peer is  configured or the router is rebooted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixwithdrawn
            
            	Counter which gets incremented when a route prefix is withdrawn on this connection. This object is initialized to zero when the peer is configured or the router is rebooted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerlasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\: str
            
            .. attribute:: cbgppeerprevstate
            
            	The BGP peer connection previous state
            	**type**\:  :py:class:`Cbgppeerprevstate <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry.Cbgppeerprevstate>`
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(BGP4MIB.Bgppeertable.Bgppeerentry, self).__init__()

                self.yang_name = "bgpPeerEntry"
                self.yang_parent_name = "bgpPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', YLeaf(YType.str, 'bgpPeerRemoteAddr')),
                    ('bgppeeridentifier', YLeaf(YType.str, 'bgpPeerIdentifier')),
                    ('bgppeerstate', YLeaf(YType.enumeration, 'bgpPeerState')),
                    ('bgppeeradminstatus', YLeaf(YType.enumeration, 'bgpPeerAdminStatus')),
                    ('bgppeernegotiatedversion', YLeaf(YType.int32, 'bgpPeerNegotiatedVersion')),
                    ('bgppeerlocaladdr', YLeaf(YType.str, 'bgpPeerLocalAddr')),
                    ('bgppeerlocalport', YLeaf(YType.int32, 'bgpPeerLocalPort')),
                    ('bgppeerremoteport', YLeaf(YType.int32, 'bgpPeerRemotePort')),
                    ('bgppeerremoteas', YLeaf(YType.int32, 'bgpPeerRemoteAs')),
                    ('bgppeerinupdates', YLeaf(YType.uint32, 'bgpPeerInUpdates')),
                    ('bgppeeroutupdates', YLeaf(YType.uint32, 'bgpPeerOutUpdates')),
                    ('bgppeerintotalmessages', YLeaf(YType.uint32, 'bgpPeerInTotalMessages')),
                    ('bgppeerouttotalmessages', YLeaf(YType.uint32, 'bgpPeerOutTotalMessages')),
                    ('bgppeerlasterror', YLeaf(YType.str, 'bgpPeerLastError')),
                    ('bgppeerfsmestablishedtransitions', YLeaf(YType.uint32, 'bgpPeerFsmEstablishedTransitions')),
                    ('bgppeerfsmestablishedtime', YLeaf(YType.uint32, 'bgpPeerFsmEstablishedTime')),
                    ('bgppeerconnectretryinterval', YLeaf(YType.int32, 'bgpPeerConnectRetryInterval')),
                    ('bgppeerholdtime', YLeaf(YType.int32, 'bgpPeerHoldTime')),
                    ('bgppeerkeepalive', YLeaf(YType.int32, 'bgpPeerKeepAlive')),
                    ('bgppeerholdtimeconfigured', YLeaf(YType.int32, 'bgpPeerHoldTimeConfigured')),
                    ('bgppeerkeepaliveconfigured', YLeaf(YType.int32, 'bgpPeerKeepAliveConfigured')),
                    ('bgppeerminasoriginationinterval', YLeaf(YType.int32, 'bgpPeerMinASOriginationInterval')),
                    ('bgppeerminrouteadvertisementinterval', YLeaf(YType.int32, 'bgpPeerMinRouteAdvertisementInterval')),
                    ('bgppeerinupdateelapsedtime', YLeaf(YType.uint32, 'bgpPeerInUpdateElapsedTime')),
                    ('cbgppeerprefixaccepted', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixAccepted')),
                    ('cbgppeerprefixdenied', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixDenied')),
                    ('cbgppeerprefixlimit', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixLimit')),
                    ('cbgppeerprefixadvertised', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixAdvertised')),
                    ('cbgppeerprefixsuppressed', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixSuppressed')),
                    ('cbgppeerprefixwithdrawn', YLeaf(YType.uint32, 'CISCO-BGP4-MIB:cbgpPeerPrefixWithdrawn')),
                    ('cbgppeerlasterrortxt', YLeaf(YType.str, 'CISCO-BGP4-MIB:cbgpPeerLastErrorTxt')),
                    ('cbgppeerprevstate', YLeaf(YType.enumeration, 'CISCO-BGP4-MIB:cbgpPeerPrevState')),
                ])
                self.bgppeerremoteaddr = None
                self.bgppeeridentifier = None
                self.bgppeerstate = None
                self.bgppeeradminstatus = None
                self.bgppeernegotiatedversion = None
                self.bgppeerlocaladdr = None
                self.bgppeerlocalport = None
                self.bgppeerremoteport = None
                self.bgppeerremoteas = None
                self.bgppeerinupdates = None
                self.bgppeeroutupdates = None
                self.bgppeerintotalmessages = None
                self.bgppeerouttotalmessages = None
                self.bgppeerlasterror = None
                self.bgppeerfsmestablishedtransitions = None
                self.bgppeerfsmestablishedtime = None
                self.bgppeerconnectretryinterval = None
                self.bgppeerholdtime = None
                self.bgppeerkeepalive = None
                self.bgppeerholdtimeconfigured = None
                self.bgppeerkeepaliveconfigured = None
                self.bgppeerminasoriginationinterval = None
                self.bgppeerminrouteadvertisementinterval = None
                self.bgppeerinupdateelapsedtime = None
                self.cbgppeerprefixaccepted = None
                self.cbgppeerprefixdenied = None
                self.cbgppeerprefixlimit = None
                self.cbgppeerprefixadvertised = None
                self.cbgppeerprefixsuppressed = None
                self.cbgppeerprefixwithdrawn = None
                self.cbgppeerlasterrortxt = None
                self.cbgppeerprevstate = None
                self._segment_path = lambda: "bgpPeerEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']"
                self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/bgpPeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BGP4MIB.Bgppeertable.Bgppeerentry, ['bgppeerremoteaddr', 'bgppeeridentifier', 'bgppeerstate', 'bgppeeradminstatus', 'bgppeernegotiatedversion', 'bgppeerlocaladdr', 'bgppeerlocalport', 'bgppeerremoteport', 'bgppeerremoteas', 'bgppeerinupdates', 'bgppeeroutupdates', 'bgppeerintotalmessages', 'bgppeerouttotalmessages', 'bgppeerlasterror', 'bgppeerfsmestablishedtransitions', 'bgppeerfsmestablishedtime', 'bgppeerconnectretryinterval', 'bgppeerholdtime', 'bgppeerkeepalive', 'bgppeerholdtimeconfigured', 'bgppeerkeepaliveconfigured', 'bgppeerminasoriginationinterval', 'bgppeerminrouteadvertisementinterval', 'bgppeerinupdateelapsedtime', 'cbgppeerprefixaccepted', 'cbgppeerprefixdenied', 'cbgppeerprefixlimit', 'cbgppeerprefixadvertised', 'cbgppeerprefixsuppressed', 'cbgppeerprefixwithdrawn', 'cbgppeerlasterrortxt', 'cbgppeerprevstate'], name, value)

            class Bgppeeradminstatus(Enum):
                """
                Bgppeeradminstatus (Enum Class)

                The desired state of the BGP connection.

                A transition from 'stop' to 'start' will

                cause the BGP Start Event to be generated.

                A transition from 'start' to 'stop' will

                cause the BGP Stop Event to be generated.

                This parameter can be used to restart BGP

                peer connections.  Care should be used in

                providing write access to this object

                without adequate authentication.

                .. data:: stop = 1

                .. data:: start = 2

                """

                stop = Enum.YLeaf(1, "stop")

                start = Enum.YLeaf(2, "start")


            class Bgppeerstate(Enum):
                """
                Bgppeerstate (Enum Class)

                The BGP peer connection state.

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                idle = Enum.YLeaf(1, "idle")

                connect = Enum.YLeaf(2, "connect")

                active = Enum.YLeaf(3, "active")

                opensent = Enum.YLeaf(4, "opensent")

                openconfirm = Enum.YLeaf(5, "openconfirm")

                established = Enum.YLeaf(6, "established")


            class Cbgppeerprevstate(Enum):
                """
                Cbgppeerprevstate (Enum Class)

                The BGP peer connection previous state.

                .. data:: none = 0

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                none = Enum.YLeaf(0, "none")

                idle = Enum.YLeaf(1, "idle")

                connect = Enum.YLeaf(2, "connect")

                active = Enum.YLeaf(3, "active")

                opensent = Enum.YLeaf(4, "opensent")

                openconfirm = Enum.YLeaf(5, "openconfirm")

                established = Enum.YLeaf(6, "established")



    class Bgprcvdpathattrtable(Entity):
        """
        The BGP Received Path Attribute Table
        contains information about paths to
        destination networks received from all
        peers running BGP version 3 or less.
        
        .. attribute:: bgppathattrentry
        
        	Information about a path to a network
        	**type**\: list of  		 :py:class:`Bgppathattrentry <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgprcvdpathattrtable.Bgppathattrentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            super(BGP4MIB.Bgprcvdpathattrtable, self).__init__()

            self.yang_name = "bgpRcvdPathAttrTable"
            self.yang_parent_name = "BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bgpPathAttrEntry", ("bgppathattrentry", BGP4MIB.Bgprcvdpathattrtable.Bgppathattrentry))])
            self._leafs = OrderedDict()

            self.bgppathattrentry = YList(self)
            self._segment_path = lambda: "bgpRcvdPathAttrTable"
            self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BGP4MIB.Bgprcvdpathattrtable, [], name, value)


        class Bgppathattrentry(Entity):
            """
            Information about a path to a network.
            
            .. attribute:: bgppathattrdestnetwork  (key)
            
            	The address of the destination network
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrpeer  (key)
            
            	The IP address of the peer where the path information was learned
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:  :py:class:`Bgppathattrorigin <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgprcvdpathattrtable.Bgppathattrentry.Bgppathattrorigin>`
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattraspath
            
            	The set of ASs that must be traversed to reach the network.  This object is probably best represented as SEQUENCE OF INTEGER.  For SMI compatibility, though, it is represented as OCTET STRING.  Each AS is represented as a pair of octets according to the following algorithm\:      first\-byte\-of\-pair = ASNumber / 256;     second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**length:** 2..255
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrinterasmetric
            
            	The optional inter\-AS metric.  If this attribute has not been provided for this route, the value for this object is 0
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(BGP4MIB.Bgprcvdpathattrtable.Bgppathattrentry, self).__init__()

                self.yang_name = "bgpPathAttrEntry"
                self.yang_parent_name = "bgpRcvdPathAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppathattrdestnetwork','bgppathattrpeer']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppathattrdestnetwork', YLeaf(YType.str, 'bgpPathAttrDestNetwork')),
                    ('bgppathattrpeer', YLeaf(YType.str, 'bgpPathAttrPeer')),
                    ('bgppathattrorigin', YLeaf(YType.enumeration, 'bgpPathAttrOrigin')),
                    ('bgppathattraspath', YLeaf(YType.str, 'bgpPathAttrASPath')),
                    ('bgppathattrnexthop', YLeaf(YType.str, 'bgpPathAttrNextHop')),
                    ('bgppathattrinterasmetric', YLeaf(YType.int32, 'bgpPathAttrInterASMetric')),
                ])
                self.bgppathattrdestnetwork = None
                self.bgppathattrpeer = None
                self.bgppathattrorigin = None
                self.bgppathattraspath = None
                self.bgppathattrnexthop = None
                self.bgppathattrinterasmetric = None
                self._segment_path = lambda: "bgpPathAttrEntry" + "[bgpPathAttrDestNetwork='" + str(self.bgppathattrdestnetwork) + "']" + "[bgpPathAttrPeer='" + str(self.bgppathattrpeer) + "']"
                self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/bgpRcvdPathAttrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BGP4MIB.Bgprcvdpathattrtable.Bgppathattrentry, ['bgppathattrdestnetwork', 'bgppathattrpeer', 'bgppathattrorigin', 'bgppathattraspath', 'bgppathattrnexthop', 'bgppathattrinterasmetric'], name, value)

            class Bgppathattrorigin(Enum):
                """
                Bgppathattrorigin (Enum Class)

                The ultimate origin of the path information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")



    class Bgp4Pathattrtable(Entity):
        """
        The BGP\-4 Received Path Attribute Table
        contains information about paths to
        destination networks received from all
        BGP4 peers.
        
        .. attribute:: bgp4pathattrentry
        
        	Information about a path to a network
        	**type**\: list of  		 :py:class:`Bgp4Pathattrentry <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry>`
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            super(BGP4MIB.Bgp4Pathattrtable, self).__init__()

            self.yang_name = "bgp4PathAttrTable"
            self.yang_parent_name = "BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bgp4PathAttrEntry", ("bgp4pathattrentry", BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry))])
            self._leafs = OrderedDict()

            self.bgp4pathattrentry = YList(self)
            self._segment_path = lambda: "bgp4PathAttrTable"
            self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BGP4MIB.Bgp4Pathattrtable, [], name, value)


        class Bgp4Pathattrentry(Entity):
            """
            Information about a path to a network.
            
            .. attribute:: bgp4pathattripaddrprefix  (key)
            
            	An IP address prefix in the Network Layer Reachability Information field.  This object is an IP address containing the prefix with length specified by bgp4PathAttrIpAddrPrefixLen. Any bits beyond the length specified by bgp4PathAttrIpAddrPrefixLen are zeroed
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattripaddrprefixlen  (key)
            
            	Length in bits of the IP address prefix in the Network Layer Reachability Information field
            	**type**\: int
            
            	**range:** 0..32
            
            .. attribute:: bgp4pathattrpeer  (key)
            
            	The IP address of the peer where the path information was learned
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:  :py:class:`Bgp4Pathattrorigin <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattrorigin>`
            
            .. attribute:: bgp4pathattraspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\:      1      AS\_SET\: unordered set of ASs a                  route in the UPDATE                  message has traversed      2      AS\_SEQUENCE\: ordered set of ASs                  a route in the UPDATE                  message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:      first\-byte\-of\-pair = ASNumber / 256;     second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**length:** 2..255
            
            .. attribute:: bgp4pathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattrmultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattrlocalpref
            
            	The originating BGP4 speaker's degree of preference for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattratomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:  :py:class:`Bgp4Pathattratomicaggregate <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattratomicaggregate>`
            
            .. attribute:: bgp4pathattraggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the absence of this attribute
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: bgp4pathattraggregatoraddr
            
            	The IP address of the last BGP4 speaker that performed route aggregation.  A value of 0.0.0.0 indicates the absence of this attribute
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattrcalclocalpref
            
            	The degree of preference calculated by the receiving BGP4 speaker for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:  :py:class:`Bgp4Pathattrbest <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattrbest>`
            
            .. attribute:: bgp4pathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry, self).__init__()

                self.yang_name = "bgp4PathAttrEntry"
                self.yang_parent_name = "bgp4PathAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgp4pathattripaddrprefix','bgp4pathattripaddrprefixlen','bgp4pathattrpeer']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgp4pathattripaddrprefix', YLeaf(YType.str, 'bgp4PathAttrIpAddrPrefix')),
                    ('bgp4pathattripaddrprefixlen', YLeaf(YType.int32, 'bgp4PathAttrIpAddrPrefixLen')),
                    ('bgp4pathattrpeer', YLeaf(YType.str, 'bgp4PathAttrPeer')),
                    ('bgp4pathattrorigin', YLeaf(YType.enumeration, 'bgp4PathAttrOrigin')),
                    ('bgp4pathattraspathsegment', YLeaf(YType.str, 'bgp4PathAttrASPathSegment')),
                    ('bgp4pathattrnexthop', YLeaf(YType.str, 'bgp4PathAttrNextHop')),
                    ('bgp4pathattrmultiexitdisc', YLeaf(YType.int32, 'bgp4PathAttrMultiExitDisc')),
                    ('bgp4pathattrlocalpref', YLeaf(YType.int32, 'bgp4PathAttrLocalPref')),
                    ('bgp4pathattratomicaggregate', YLeaf(YType.enumeration, 'bgp4PathAttrAtomicAggregate')),
                    ('bgp4pathattraggregatoras', YLeaf(YType.int32, 'bgp4PathAttrAggregatorAS')),
                    ('bgp4pathattraggregatoraddr', YLeaf(YType.str, 'bgp4PathAttrAggregatorAddr')),
                    ('bgp4pathattrcalclocalpref', YLeaf(YType.int32, 'bgp4PathAttrCalcLocalPref')),
                    ('bgp4pathattrbest', YLeaf(YType.enumeration, 'bgp4PathAttrBest')),
                    ('bgp4pathattrunknown', YLeaf(YType.str, 'bgp4PathAttrUnknown')),
                ])
                self.bgp4pathattripaddrprefix = None
                self.bgp4pathattripaddrprefixlen = None
                self.bgp4pathattrpeer = None
                self.bgp4pathattrorigin = None
                self.bgp4pathattraspathsegment = None
                self.bgp4pathattrnexthop = None
                self.bgp4pathattrmultiexitdisc = None
                self.bgp4pathattrlocalpref = None
                self.bgp4pathattratomicaggregate = None
                self.bgp4pathattraggregatoras = None
                self.bgp4pathattraggregatoraddr = None
                self.bgp4pathattrcalclocalpref = None
                self.bgp4pathattrbest = None
                self.bgp4pathattrunknown = None
                self._segment_path = lambda: "bgp4PathAttrEntry" + "[bgp4PathAttrIpAddrPrefix='" + str(self.bgp4pathattripaddrprefix) + "']" + "[bgp4PathAttrIpAddrPrefixLen='" + str(self.bgp4pathattripaddrprefixlen) + "']" + "[bgp4PathAttrPeer='" + str(self.bgp4pathattrpeer) + "']"
                self._absolute_path = lambda: "BGP4-MIB:BGP4-MIB/bgp4PathAttrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BGP4MIB.Bgp4Pathattrtable.Bgp4Pathattrentry, ['bgp4pathattripaddrprefix', 'bgp4pathattripaddrprefixlen', 'bgp4pathattrpeer', 'bgp4pathattrorigin', 'bgp4pathattraspathsegment', 'bgp4pathattrnexthop', 'bgp4pathattrmultiexitdisc', 'bgp4pathattrlocalpref', 'bgp4pathattratomicaggregate', 'bgp4pathattraggregatoras', 'bgp4pathattraggregatoraddr', 'bgp4pathattrcalclocalpref', 'bgp4pathattrbest', 'bgp4pathattrunknown'], name, value)

            class Bgp4Pathattratomicaggregate(Enum):
                """
                Bgp4Pathattratomicaggregate (Enum Class)

                Whether or not the local system has

                selected a less specific route without

                selecting a more specific route.

                .. data:: lessSpecificRrouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRrouteNotSelected = Enum.YLeaf(1, "lessSpecificRrouteNotSelected")

                lessSpecificRouteSelected = Enum.YLeaf(2, "lessSpecificRouteSelected")


            class Bgp4Pathattrbest(Enum):
                """
                Bgp4Pathattrbest (Enum Class)

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = Enum.YLeaf(1, "false")

                true = Enum.YLeaf(2, "true")


            class Bgp4Pathattrorigin(Enum):
                """
                Bgp4Pathattrorigin (Enum Class)

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")


    def clone_ptr(self):
        self._top_entity = BGP4MIB()
        return self._top_entity

