""" BGP4_MIB 

The MIB module for BGP\-4.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Bgp4Mib(object):
    """
    
    
    .. attribute:: bgp
    
    	
    	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp>`
    
    .. attribute:: bgp4pathattrtable
    
    	The BGP\-4 Received Path Attribute Table contains information about paths to destination networks received from all BGP4 peers
    	**type**\:   :py:class:`Bgp4Pathattrtable <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable>`
    
    .. attribute:: bgppeertable
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\:   :py:class:`Bgppeertable <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable>`
    
    .. attribute:: bgprcvdpathattrtable
    
    	The BGP Received Path Attribute Table contains information about paths to destination networks received from all peers running BGP version 3 or less
    	**type**\:   :py:class:`Bgprcvdpathattrtable <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgprcvdpathattrtable>`
    
    	**status**\: obsolete
    
    

    """

    _prefix = 'BGP4-MIB'
    _revision = '1994-05-05'

    def __init__(self):
        self.bgp = Bgp4Mib.Bgp()
        self.bgp.parent = self
        self.bgp4pathattrtable = Bgp4Mib.Bgp4Pathattrtable()
        self.bgp4pathattrtable.parent = self
        self.bgppeertable = Bgp4Mib.Bgppeertable()
        self.bgppeertable.parent = self
        self.bgprcvdpathattrtable = Bgp4Mib.Bgprcvdpathattrtable()
        self.bgprcvdpathattrtable.parent = self


    class Bgp(object):
        """
        
        
        .. attribute:: bgpidentifier
        
        	The BGP Identifier of local system
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: bgplocalas
        
        	The local autonomous system number
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: bgpversion
        
        	Vector of supported BGP protocol version numbers.  Each peer negotiates the version from this vector.  Versions are identified via the string of bits contained within this object.  The first octet contains bits 0 to 7, the second octet contains bits 8 to 15, and so on, with the most significant bit referring to the lowest bit number in the octet (e.g., the MSB of the first octet refers to bit 0).  If a bit, i, is present and set, then the version (i+1) of the BGP is supported
        	**type**\:  str
        
        	**length:** 1..255
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            self.parent = None
            self.bgpidentifier = None
            self.bgplocalas = None
            self.bgpversion = None

        @property
        def _common_path(self):

            return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgpidentifier is not None:
                return True

            if self.bgplocalas is not None:
                return True

            if self.bgpversion is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
            return meta._meta_table['Bgp4Mib.Bgp']['meta_info']


    class Bgppeertable(object):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: bgppeerentry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of    :py:class:`Bgppeerentry <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry>`
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            self.parent = None
            self.bgppeerentry = YList()
            self.bgppeerentry.parent = self
            self.bgppeerentry.name = 'bgppeerentry'


        class Bgppeerentry(object):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	The remote IP address of this entry's BGP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeeradminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`BgppeeradminstatusEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeeradminstatusEnum>`
            
            .. attribute:: bgppeerconnectretryinterval
            
            	Time interval in seconds for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeerfsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state.  It is set to zero when a new peer is configured or the router is booted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerfsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerholdtime
            
            	Time interval in seconds for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker by using the smaller of the value in bgpPeerHoldTimeConfigured and the Hold Time received in the OPEN message. This value must be at lease three seconds if it is not zero (0) in which case the Hold Timer has not been established with the peer, or, the value of bgpPeerHoldTimeConfigured is zero (0)
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            .. attribute:: bgppeerholdtimeconfigured
            
            	Time interval in seconds for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (bgpPeerHoldTime) with the peer. This value must not be less than three seconds if it is not zero (0) in which case the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            .. attribute:: bgppeeridentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeerintotalmessages
            
            	The total number of messages received from the remote peer on this connection. This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerinupdateelapsedtime
            
            	Elapsed time in seconds since the last BGP UPDATE message was received from the peer. Each time bgpPeerInUpdates is incremented, the value of this object is set to zero (0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerinupdates
            
            	The number of BGP UPDATE messages received on this connection.  This object should be initialized to zero (0) when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerkeepalive
            
            	Time interval in seconds for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with bgpPeerHoldTime, it has the same proportion as what bgpPeerKeepAliveConfigured has when compared with bgpPeerHoldTimeConfigured. If the value of this object is zero (0), it indicates that the KeepAlive timer has not been established with the peer, or, the value of bgpPeerKeepAliveConfigured is zero (0)
            	**type**\:  int
            
            	**range:** 0..21845
            
            .. attribute:: bgppeerkeepaliveconfigured
            
            	Time interval in seconds for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in bgpPeerHoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by bgpPeerKeepAlive.  A reasonable maximum value for this timer would be configured to be one third of that of bgpPeerHoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\:  int
            
            	**range:** 0..21845
            
            .. attribute:: bgppeerlasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: bgppeerlocaladdr
            
            	The local IP address of this entry's BGP connection
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeerlocalport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerminasoriginationinterval
            
            	Time interval in seconds for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeerminrouteadvertisementinterval
            
            	Time interval in seconds for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: bgppeernegotiatedversion
            
            	The negotiated version of BGP running between the two peers
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: bgppeerouttotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeeroutupdates
            
            	The number of BGP UPDATE messages transmitted on this connection.  This object should be initialized to zero (0) when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bgppeerremoteas
            
            	The remote autonomous system number
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerremoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects bgpPeerLocalAddr, bgpPeerLocalPort, bgpPeerRemoteAddr and bgpPeerRemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: bgppeerstate
            
            	The BGP peer connection state
            	**type**\:   :py:class:`BgppeerstateEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeerstateEnum>`
            
            .. attribute:: cbgppeerlasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\:  str
            
            .. attribute:: cbgppeerprefixaccepted
            
            	Number of Route prefixes received on this connnection, which are accepted after applying filters. Possible filters are route maps, prefix lists, distributed lists, etc
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixadvertised
            
            	Counter which gets incremented when a route prefix is advertised on this connection. This object is initialized to zero when the peer is configured or  the router is rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixdenied
            
            	Counter which gets incremented when a route prefix received on this connection is denied  or when a route prefix is denied during soft reset of this connection if 'soft\-reconfiguration' is on . This object is  initialized to zero when the peer is  configured or the router is rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixlimit
            
            	Max number of route prefixes accepted on this connection
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixsuppressed
            
            	Counter which gets incremented when a route prefix is suppressed from being sent on this connection. This  object is initialized to zero when the peer is  configured or the router is rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprefixwithdrawn
            
            	Counter which gets incremented when a route prefix is withdrawn on this connection. This object is initialized to zero when the peer is configured or the router is rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cbgppeerprevstate
            
            	The BGP peer connection previous state
            	**type**\:   :py:class:`CbgppeerprevstateEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.CbgppeerprevstateEnum>`
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                self.parent = None
                self.bgppeerremoteaddr = None
                self.bgppeeradminstatus = None
                self.bgppeerconnectretryinterval = None
                self.bgppeerfsmestablishedtime = None
                self.bgppeerfsmestablishedtransitions = None
                self.bgppeerholdtime = None
                self.bgppeerholdtimeconfigured = None
                self.bgppeeridentifier = None
                self.bgppeerintotalmessages = None
                self.bgppeerinupdateelapsedtime = None
                self.bgppeerinupdates = None
                self.bgppeerkeepalive = None
                self.bgppeerkeepaliveconfigured = None
                self.bgppeerlasterror = None
                self.bgppeerlocaladdr = None
                self.bgppeerlocalport = None
                self.bgppeerminasoriginationinterval = None
                self.bgppeerminrouteadvertisementinterval = None
                self.bgppeernegotiatedversion = None
                self.bgppeerouttotalmessages = None
                self.bgppeeroutupdates = None
                self.bgppeerremoteas = None
                self.bgppeerremoteport = None
                self.bgppeerstate = None
                self.cbgppeerlasterrortxt = None
                self.cbgppeerprefixaccepted = None
                self.cbgppeerprefixadvertised = None
                self.cbgppeerprefixdenied = None
                self.cbgppeerprefixlimit = None
                self.cbgppeerprefixsuppressed = None
                self.cbgppeerprefixwithdrawn = None
                self.cbgppeerprevstate = None

            class BgppeeradminstatusEnum(Enum):
                """
                BgppeeradminstatusEnum

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

                stop = 1

                start = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeeradminstatusEnum']


            class BgppeerstateEnum(Enum):
                """
                BgppeerstateEnum

                The BGP peer connection state.

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                idle = 1

                connect = 2

                active = 3

                opensent = 4

                openconfirm = 5

                established = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeerstateEnum']


            class CbgppeerprevstateEnum(Enum):
                """
                CbgppeerprevstateEnum

                The BGP peer connection previous state.

                .. data:: none = 0

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                none = 0

                idle = 1

                connect = 2

                active = 3

                opensent = 4

                openconfirm = 5

                established = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgppeertable.Bgppeerentry.CbgppeerprevstateEnum']


            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYModelError('Key property bgppeerremoteaddr is None')

                return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgpPeerTable/BGP4-MIB:bgpPeerEntry[BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.bgppeeradminstatus is not None:
                    return True

                if self.bgppeerconnectretryinterval is not None:
                    return True

                if self.bgppeerfsmestablishedtime is not None:
                    return True

                if self.bgppeerfsmestablishedtransitions is not None:
                    return True

                if self.bgppeerholdtime is not None:
                    return True

                if self.bgppeerholdtimeconfigured is not None:
                    return True

                if self.bgppeeridentifier is not None:
                    return True

                if self.bgppeerintotalmessages is not None:
                    return True

                if self.bgppeerinupdateelapsedtime is not None:
                    return True

                if self.bgppeerinupdates is not None:
                    return True

                if self.bgppeerkeepalive is not None:
                    return True

                if self.bgppeerkeepaliveconfigured is not None:
                    return True

                if self.bgppeerlasterror is not None:
                    return True

                if self.bgppeerlocaladdr is not None:
                    return True

                if self.bgppeerlocalport is not None:
                    return True

                if self.bgppeerminasoriginationinterval is not None:
                    return True

                if self.bgppeerminrouteadvertisementinterval is not None:
                    return True

                if self.bgppeernegotiatedversion is not None:
                    return True

                if self.bgppeerouttotalmessages is not None:
                    return True

                if self.bgppeeroutupdates is not None:
                    return True

                if self.bgppeerremoteas is not None:
                    return True

                if self.bgppeerremoteport is not None:
                    return True

                if self.bgppeerstate is not None:
                    return True

                if self.cbgppeerlasterrortxt is not None:
                    return True

                if self.cbgppeerprefixaccepted is not None:
                    return True

                if self.cbgppeerprefixadvertised is not None:
                    return True

                if self.cbgppeerprefixdenied is not None:
                    return True

                if self.cbgppeerprefixlimit is not None:
                    return True

                if self.cbgppeerprefixsuppressed is not None:
                    return True

                if self.cbgppeerprefixwithdrawn is not None:
                    return True

                if self.cbgppeerprevstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                return meta._meta_table['Bgp4Mib.Bgppeertable.Bgppeerentry']['meta_info']

        @property
        def _common_path(self):

            return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgpPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgppeerentry is not None:
                for child_ref in self.bgppeerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
            return meta._meta_table['Bgp4Mib.Bgppeertable']['meta_info']


    class Bgprcvdpathattrtable(object):
        """
        The BGP Received Path Attribute Table
        contains information about paths to
        destination networks received from all
        peers running BGP version 3 or less.
        
        .. attribute:: bgppathattrentry
        
        	Information about a path to a network
        	**type**\: list of    :py:class:`Bgppathattrentry <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            self.parent = None
            self.bgppathattrentry = YList()
            self.bgppathattrentry.parent = self
            self.bgppathattrentry.name = 'bgppathattrentry'


        class Bgppathattrentry(object):
            """
            Information about a path to a network.
            
            .. attribute:: bgppathattrdestnetwork  <key>
            
            	The address of the destination network
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrpeer  <key>
            
            	The IP address of the peer where the path information was learned
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattraspath
            
            	The set of ASs that must be traversed to reach the network.  This object is probably best represented as SEQUENCE OF INTEGER.  For SMI compatibility, though, it is represented as OCTET STRING.  Each AS is represented as a pair of octets according to the following algorithm\:      first\-byte\-of\-pair = ASNumber / 256;     second\-byte\-of\-pair = ASNumber & 255;
            	**type**\:  str
            
            	**length:** 2..255
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrinterasmetric
            
            	The optional inter\-AS metric.  If this attribute has not been provided for this route, the value for this object is 0
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: bgppathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:   :py:class:`BgppathattroriginEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry.BgppathattroriginEnum>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                self.parent = None
                self.bgppathattrdestnetwork = None
                self.bgppathattrpeer = None
                self.bgppathattraspath = None
                self.bgppathattrinterasmetric = None
                self.bgppathattrnexthop = None
                self.bgppathattrorigin = None

            class BgppathattroriginEnum(Enum):
                """
                BgppathattroriginEnum

                The ultimate origin of the path information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = 1

                egp = 2

                incomplete = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry.BgppathattroriginEnum']


            @property
            def _common_path(self):
                if self.bgppathattrdestnetwork is None:
                    raise YPYModelError('Key property bgppathattrdestnetwork is None')
                if self.bgppathattrpeer is None:
                    raise YPYModelError('Key property bgppathattrpeer is None')

                return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgpRcvdPathAttrTable/BGP4-MIB:bgpPathAttrEntry[BGP4-MIB:bgpPathAttrDestNetwork = ' + str(self.bgppathattrdestnetwork) + '][BGP4-MIB:bgpPathAttrPeer = ' + str(self.bgppathattrpeer) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgppathattrdestnetwork is not None:
                    return True

                if self.bgppathattrpeer is not None:
                    return True

                if self.bgppathattraspath is not None:
                    return True

                if self.bgppathattrinterasmetric is not None:
                    return True

                if self.bgppathattrnexthop is not None:
                    return True

                if self.bgppathattrorigin is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                return meta._meta_table['Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry']['meta_info']

        @property
        def _common_path(self):

            return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgpRcvdPathAttrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgppathattrentry is not None:
                for child_ref in self.bgppathattrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
            return meta._meta_table['Bgp4Mib.Bgprcvdpathattrtable']['meta_info']


    class Bgp4Pathattrtable(object):
        """
        The BGP\-4 Received Path Attribute Table
        contains information about paths to
        destination networks received from all
        BGP4 peers.
        
        .. attribute:: bgp4pathattrentry
        
        	Information about a path to a network
        	**type**\: list of    :py:class:`Bgp4Pathattrentry <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry>`
        
        

        """

        _prefix = 'BGP4-MIB'
        _revision = '1994-05-05'

        def __init__(self):
            self.parent = None
            self.bgp4pathattrentry = YList()
            self.bgp4pathattrentry.parent = self
            self.bgp4pathattrentry.name = 'bgp4pathattrentry'


        class Bgp4Pathattrentry(object):
            """
            Information about a path to a network.
            
            .. attribute:: bgp4pathattripaddrprefix  <key>
            
            	An IP address prefix in the Network Layer Reachability Information field.  This object is an IP address containing the prefix with length specified by bgp4PathAttrIpAddrPrefixLen. Any bits beyond the length specified by bgp4PathAttrIpAddrPrefixLen are zeroed
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattripaddrprefixlen  <key>
            
            	Length in bits of the IP address prefix in the Network Layer Reachability Information field
            	**type**\:  int
            
            	**range:** 0..32
            
            .. attribute:: bgp4pathattrpeer  <key>
            
            	The IP address of the peer where the path information was learned
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattraggregatoraddr
            
            	The IP address of the last BGP4 speaker that performed route aggregation.  A value of 0.0.0.0 indicates the absence of this attribute
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattraggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: bgp4pathattraspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\:      1      AS\_SET\: unordered set of ASs a                  route in the UPDATE                  message has traversed      2      AS\_SEQUENCE\: ordered set of ASs                  a route in the UPDATE                  message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:      first\-byte\-of\-pair = ASNumber / 256;     second\-byte\-of\-pair = ASNumber & 255;
            	**type**\:  str
            
            	**length:** 2..255
            
            .. attribute:: bgp4pathattratomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:   :py:class:`Bgp4PathattratomicaggregateEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattratomicaggregateEnum>`
            
            .. attribute:: bgp4pathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:   :py:class:`Bgp4PathattrbestEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattrbestEnum>`
            
            .. attribute:: bgp4pathattrcalclocalpref
            
            	The degree of preference calculated by the receiving BGP4 speaker for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattrlocalpref
            
            	The originating BGP4 speaker's degree of preference for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattrmultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: bgp4pathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp4pathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:   :py:class:`Bgp4PathattroriginEnum <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattroriginEnum>`
            
            .. attribute:: bgp4pathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                self.parent = None
                self.bgp4pathattripaddrprefix = None
                self.bgp4pathattripaddrprefixlen = None
                self.bgp4pathattrpeer = None
                self.bgp4pathattraggregatoraddr = None
                self.bgp4pathattraggregatoras = None
                self.bgp4pathattraspathsegment = None
                self.bgp4pathattratomicaggregate = None
                self.bgp4pathattrbest = None
                self.bgp4pathattrcalclocalpref = None
                self.bgp4pathattrlocalpref = None
                self.bgp4pathattrmultiexitdisc = None
                self.bgp4pathattrnexthop = None
                self.bgp4pathattrorigin = None
                self.bgp4pathattrunknown = None

            class Bgp4PathattratomicaggregateEnum(Enum):
                """
                Bgp4PathattratomicaggregateEnum

                Whether or not the local system has

                selected a less specific route without

                selecting a more specific route.

                .. data:: lessSpecificRrouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRrouteNotSelected = 1

                lessSpecificRouteSelected = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattratomicaggregateEnum']


            class Bgp4PathattrbestEnum(Enum):
                """
                Bgp4PathattrbestEnum

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = 1

                true = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattrbestEnum']


            class Bgp4PathattroriginEnum(Enum):
                """
                Bgp4PathattroriginEnum

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = 1

                egp = 2

                incomplete = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                    return meta._meta_table['Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattroriginEnum']


            @property
            def _common_path(self):
                if self.bgp4pathattripaddrprefix is None:
                    raise YPYModelError('Key property bgp4pathattripaddrprefix is None')
                if self.bgp4pathattripaddrprefixlen is None:
                    raise YPYModelError('Key property bgp4pathattripaddrprefixlen is None')
                if self.bgp4pathattrpeer is None:
                    raise YPYModelError('Key property bgp4pathattrpeer is None')

                return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgp4PathAttrTable/BGP4-MIB:bgp4PathAttrEntry[BGP4-MIB:bgp4PathAttrIpAddrPrefix = ' + str(self.bgp4pathattripaddrprefix) + '][BGP4-MIB:bgp4PathAttrIpAddrPrefixLen = ' + str(self.bgp4pathattripaddrprefixlen) + '][BGP4-MIB:bgp4PathAttrPeer = ' + str(self.bgp4pathattrpeer) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgp4pathattripaddrprefix is not None:
                    return True

                if self.bgp4pathattripaddrprefixlen is not None:
                    return True

                if self.bgp4pathattrpeer is not None:
                    return True

                if self.bgp4pathattraggregatoraddr is not None:
                    return True

                if self.bgp4pathattraggregatoras is not None:
                    return True

                if self.bgp4pathattraspathsegment is not None:
                    return True

                if self.bgp4pathattratomicaggregate is not None:
                    return True

                if self.bgp4pathattrbest is not None:
                    return True

                if self.bgp4pathattrcalclocalpref is not None:
                    return True

                if self.bgp4pathattrlocalpref is not None:
                    return True

                if self.bgp4pathattrmultiexitdisc is not None:
                    return True

                if self.bgp4pathattrnexthop is not None:
                    return True

                if self.bgp4pathattrorigin is not None:
                    return True

                if self.bgp4pathattrunknown is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
                return meta._meta_table['Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry']['meta_info']

        @property
        def _common_path(self):

            return '/BGP4-MIB:BGP4-MIB/BGP4-MIB:bgp4PathAttrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgp4pathattrentry is not None:
                for child_ref in self.bgp4pathattrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
            return meta._meta_table['Bgp4Mib.Bgp4Pathattrtable']['meta_info']

    @property
    def _common_path(self):

        return '/BGP4-MIB:BGP4-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.bgp is not None and self.bgp._has_data():
            return True

        if self.bgp4pathattrtable is not None and self.bgp4pathattrtable._has_data():
            return True

        if self.bgppeertable is not None and self.bgppeertable._has_data():
            return True

        if self.bgprcvdpathattrtable is not None and self.bgprcvdpathattrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _BGP4_MIB as meta
        return meta._meta_table['Bgp4Mib']['meta_info']


