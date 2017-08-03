""" BGP4_MIB 

The MIB module for BGP\-4.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Bgp4Mib(Entity):
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
        super(Bgp4Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "BGP4-MIB"
        self.yang_parent_name = "BGP4-MIB"

        self.bgp = Bgp4Mib.Bgp()
        self.bgp.parent = self
        self._children_name_map["bgp"] = "bgp"
        self._children_yang_names.add("bgp")

        self.bgp4pathattrtable = Bgp4Mib.Bgp4Pathattrtable()
        self.bgp4pathattrtable.parent = self
        self._children_name_map["bgp4pathattrtable"] = "bgp4PathAttrTable"
        self._children_yang_names.add("bgp4PathAttrTable")

        self.bgppeertable = Bgp4Mib.Bgppeertable()
        self.bgppeertable.parent = self
        self._children_name_map["bgppeertable"] = "bgpPeerTable"
        self._children_yang_names.add("bgpPeerTable")

        self.bgprcvdpathattrtable = Bgp4Mib.Bgprcvdpathattrtable()
        self.bgprcvdpathattrtable.parent = self
        self._children_name_map["bgprcvdpathattrtable"] = "bgpRcvdPathAttrTable"
        self._children_yang_names.add("bgpRcvdPathAttrTable")


    class Bgp(Entity):
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
            super(Bgp4Mib.Bgp, self).__init__()

            self.yang_name = "bgp"
            self.yang_parent_name = "BGP4-MIB"

            self.bgpidentifier = YLeaf(YType.str, "bgpIdentifier")

            self.bgplocalas = YLeaf(YType.int32, "bgpLocalAs")

            self.bgpversion = YLeaf(YType.str, "bgpVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bgpidentifier",
                            "bgplocalas",
                            "bgpversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Bgp4Mib.Bgp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bgp4Mib.Bgp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.bgpidentifier.is_set or
                self.bgplocalas.is_set or
                self.bgpversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bgpidentifier.yfilter != YFilter.not_set or
                self.bgplocalas.yfilter != YFilter.not_set or
                self.bgpversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bgp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BGP4-MIB:BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bgpidentifier.is_set or self.bgpidentifier.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bgpidentifier.get_name_leafdata())
            if (self.bgplocalas.is_set or self.bgplocalas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bgplocalas.get_name_leafdata())
            if (self.bgpversion.is_set or self.bgpversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bgpversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgpIdentifier" or name == "bgpLocalAs" or name == "bgpVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bgpIdentifier"):
                self.bgpidentifier = value
                self.bgpidentifier.value_namespace = name_space
                self.bgpidentifier.value_namespace_prefix = name_space_prefix
            if(value_path == "bgpLocalAs"):
                self.bgplocalas = value
                self.bgplocalas.value_namespace = name_space
                self.bgplocalas.value_namespace_prefix = name_space_prefix
            if(value_path == "bgpVersion"):
                self.bgpversion = value
                self.bgpversion.value_namespace = name_space
                self.bgpversion.value_namespace_prefix = name_space_prefix


    class Bgppeertable(Entity):
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
            super(Bgp4Mib.Bgppeertable, self).__init__()

            self.yang_name = "bgpPeerTable"
            self.yang_parent_name = "BGP4-MIB"

            self.bgppeerentry = YList(self)

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
                        super(Bgp4Mib.Bgppeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bgp4Mib.Bgppeertable, self).__setattr__(name, value)


        class Bgppeerentry(Entity):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	The remote IP address of this entry's BGP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgppeeradminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`Bgppeeradminstatus <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.Bgppeeradminstatus>`
            
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
            	**type**\:   :py:class:`Bgppeerstate <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.Bgppeerstate>`
            
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
            	**type**\:   :py:class:`Cbgppeerprevstate <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry.Cbgppeerprevstate>`
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(Bgp4Mib.Bgppeertable.Bgppeerentry, self).__init__()

                self.yang_name = "bgpPeerEntry"
                self.yang_parent_name = "bgpPeerTable"

                self.bgppeerremoteaddr = YLeaf(YType.str, "bgpPeerRemoteAddr")

                self.bgppeeradminstatus = YLeaf(YType.enumeration, "bgpPeerAdminStatus")

                self.bgppeerconnectretryinterval = YLeaf(YType.int32, "bgpPeerConnectRetryInterval")

                self.bgppeerfsmestablishedtime = YLeaf(YType.uint32, "bgpPeerFsmEstablishedTime")

                self.bgppeerfsmestablishedtransitions = YLeaf(YType.uint32, "bgpPeerFsmEstablishedTransitions")

                self.bgppeerholdtime = YLeaf(YType.int32, "bgpPeerHoldTime")

                self.bgppeerholdtimeconfigured = YLeaf(YType.int32, "bgpPeerHoldTimeConfigured")

                self.bgppeeridentifier = YLeaf(YType.str, "bgpPeerIdentifier")

                self.bgppeerintotalmessages = YLeaf(YType.uint32, "bgpPeerInTotalMessages")

                self.bgppeerinupdateelapsedtime = YLeaf(YType.uint32, "bgpPeerInUpdateElapsedTime")

                self.bgppeerinupdates = YLeaf(YType.uint32, "bgpPeerInUpdates")

                self.bgppeerkeepalive = YLeaf(YType.int32, "bgpPeerKeepAlive")

                self.bgppeerkeepaliveconfigured = YLeaf(YType.int32, "bgpPeerKeepAliveConfigured")

                self.bgppeerlasterror = YLeaf(YType.str, "bgpPeerLastError")

                self.bgppeerlocaladdr = YLeaf(YType.str, "bgpPeerLocalAddr")

                self.bgppeerlocalport = YLeaf(YType.int32, "bgpPeerLocalPort")

                self.bgppeerminasoriginationinterval = YLeaf(YType.int32, "bgpPeerMinASOriginationInterval")

                self.bgppeerminrouteadvertisementinterval = YLeaf(YType.int32, "bgpPeerMinRouteAdvertisementInterval")

                self.bgppeernegotiatedversion = YLeaf(YType.int32, "bgpPeerNegotiatedVersion")

                self.bgppeerouttotalmessages = YLeaf(YType.uint32, "bgpPeerOutTotalMessages")

                self.bgppeeroutupdates = YLeaf(YType.uint32, "bgpPeerOutUpdates")

                self.bgppeerremoteas = YLeaf(YType.int32, "bgpPeerRemoteAs")

                self.bgppeerremoteport = YLeaf(YType.int32, "bgpPeerRemotePort")

                self.bgppeerstate = YLeaf(YType.enumeration, "bgpPeerState")

                self.cbgppeerlasterrortxt = YLeaf(YType.str, "CISCO-BGP4-MIB:cbgpPeerLastErrorTxt")

                self.cbgppeerprefixaccepted = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixAccepted")

                self.cbgppeerprefixadvertised = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixAdvertised")

                self.cbgppeerprefixdenied = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixDenied")

                self.cbgppeerprefixlimit = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixLimit")

                self.cbgppeerprefixsuppressed = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixSuppressed")

                self.cbgppeerprefixwithdrawn = YLeaf(YType.uint32, "CISCO-BGP4-MIB:cbgpPeerPrefixWithdrawn")

                self.cbgppeerprevstate = YLeaf(YType.enumeration, "CISCO-BGP4-MIB:cbgpPeerPrevState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgppeerremoteaddr",
                                "bgppeeradminstatus",
                                "bgppeerconnectretryinterval",
                                "bgppeerfsmestablishedtime",
                                "bgppeerfsmestablishedtransitions",
                                "bgppeerholdtime",
                                "bgppeerholdtimeconfigured",
                                "bgppeeridentifier",
                                "bgppeerintotalmessages",
                                "bgppeerinupdateelapsedtime",
                                "bgppeerinupdates",
                                "bgppeerkeepalive",
                                "bgppeerkeepaliveconfigured",
                                "bgppeerlasterror",
                                "bgppeerlocaladdr",
                                "bgppeerlocalport",
                                "bgppeerminasoriginationinterval",
                                "bgppeerminrouteadvertisementinterval",
                                "bgppeernegotiatedversion",
                                "bgppeerouttotalmessages",
                                "bgppeeroutupdates",
                                "bgppeerremoteas",
                                "bgppeerremoteport",
                                "bgppeerstate",
                                "cbgppeerlasterrortxt",
                                "cbgppeerprefixaccepted",
                                "cbgppeerprefixadvertised",
                                "cbgppeerprefixdenied",
                                "cbgppeerprefixlimit",
                                "cbgppeerprefixsuppressed",
                                "cbgppeerprefixwithdrawn",
                                "cbgppeerprevstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bgp4Mib.Bgppeertable.Bgppeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bgp4Mib.Bgppeertable.Bgppeerentry, self).__setattr__(name, value)

            class Bgppeeradminstatus(Enum):
                """
                Bgppeeradminstatus

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
                Bgppeerstate

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
                Cbgppeerprevstate

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


            def has_data(self):
                return (
                    self.bgppeerremoteaddr.is_set or
                    self.bgppeeradminstatus.is_set or
                    self.bgppeerconnectretryinterval.is_set or
                    self.bgppeerfsmestablishedtime.is_set or
                    self.bgppeerfsmestablishedtransitions.is_set or
                    self.bgppeerholdtime.is_set or
                    self.bgppeerholdtimeconfigured.is_set or
                    self.bgppeeridentifier.is_set or
                    self.bgppeerintotalmessages.is_set or
                    self.bgppeerinupdateelapsedtime.is_set or
                    self.bgppeerinupdates.is_set or
                    self.bgppeerkeepalive.is_set or
                    self.bgppeerkeepaliveconfigured.is_set or
                    self.bgppeerlasterror.is_set or
                    self.bgppeerlocaladdr.is_set or
                    self.bgppeerlocalport.is_set or
                    self.bgppeerminasoriginationinterval.is_set or
                    self.bgppeerminrouteadvertisementinterval.is_set or
                    self.bgppeernegotiatedversion.is_set or
                    self.bgppeerouttotalmessages.is_set or
                    self.bgppeeroutupdates.is_set or
                    self.bgppeerremoteas.is_set or
                    self.bgppeerremoteport.is_set or
                    self.bgppeerstate.is_set or
                    self.cbgppeerlasterrortxt.is_set or
                    self.cbgppeerprefixaccepted.is_set or
                    self.cbgppeerprefixadvertised.is_set or
                    self.cbgppeerprefixdenied.is_set or
                    self.cbgppeerprefixlimit.is_set or
                    self.cbgppeerprefixsuppressed.is_set or
                    self.cbgppeerprefixwithdrawn.is_set or
                    self.cbgppeerprevstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgppeerremoteaddr.yfilter != YFilter.not_set or
                    self.bgppeeradminstatus.yfilter != YFilter.not_set or
                    self.bgppeerconnectretryinterval.yfilter != YFilter.not_set or
                    self.bgppeerfsmestablishedtime.yfilter != YFilter.not_set or
                    self.bgppeerfsmestablishedtransitions.yfilter != YFilter.not_set or
                    self.bgppeerholdtime.yfilter != YFilter.not_set or
                    self.bgppeerholdtimeconfigured.yfilter != YFilter.not_set or
                    self.bgppeeridentifier.yfilter != YFilter.not_set or
                    self.bgppeerintotalmessages.yfilter != YFilter.not_set or
                    self.bgppeerinupdateelapsedtime.yfilter != YFilter.not_set or
                    self.bgppeerinupdates.yfilter != YFilter.not_set or
                    self.bgppeerkeepalive.yfilter != YFilter.not_set or
                    self.bgppeerkeepaliveconfigured.yfilter != YFilter.not_set or
                    self.bgppeerlasterror.yfilter != YFilter.not_set or
                    self.bgppeerlocaladdr.yfilter != YFilter.not_set or
                    self.bgppeerlocalport.yfilter != YFilter.not_set or
                    self.bgppeerminasoriginationinterval.yfilter != YFilter.not_set or
                    self.bgppeerminrouteadvertisementinterval.yfilter != YFilter.not_set or
                    self.bgppeernegotiatedversion.yfilter != YFilter.not_set or
                    self.bgppeerouttotalmessages.yfilter != YFilter.not_set or
                    self.bgppeeroutupdates.yfilter != YFilter.not_set or
                    self.bgppeerremoteas.yfilter != YFilter.not_set or
                    self.bgppeerremoteport.yfilter != YFilter.not_set or
                    self.bgppeerstate.yfilter != YFilter.not_set or
                    self.cbgppeerlasterrortxt.yfilter != YFilter.not_set or
                    self.cbgppeerprefixaccepted.yfilter != YFilter.not_set or
                    self.cbgppeerprefixadvertised.yfilter != YFilter.not_set or
                    self.cbgppeerprefixdenied.yfilter != YFilter.not_set or
                    self.cbgppeerprefixlimit.yfilter != YFilter.not_set or
                    self.cbgppeerprefixsuppressed.yfilter != YFilter.not_set or
                    self.cbgppeerprefixwithdrawn.yfilter != YFilter.not_set or
                    self.cbgppeerprevstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgpPeerEntry" + "[bgpPeerRemoteAddr='" + self.bgppeerremoteaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BGP4-MIB:BGP4-MIB/bgpPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgppeerremoteaddr.is_set or self.bgppeerremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteaddr.get_name_leafdata())
                if (self.bgppeeradminstatus.is_set or self.bgppeeradminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeeradminstatus.get_name_leafdata())
                if (self.bgppeerconnectretryinterval.is_set or self.bgppeerconnectretryinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerconnectretryinterval.get_name_leafdata())
                if (self.bgppeerfsmestablishedtime.is_set or self.bgppeerfsmestablishedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerfsmestablishedtime.get_name_leafdata())
                if (self.bgppeerfsmestablishedtransitions.is_set or self.bgppeerfsmestablishedtransitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerfsmestablishedtransitions.get_name_leafdata())
                if (self.bgppeerholdtime.is_set or self.bgppeerholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerholdtime.get_name_leafdata())
                if (self.bgppeerholdtimeconfigured.is_set or self.bgppeerholdtimeconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerholdtimeconfigured.get_name_leafdata())
                if (self.bgppeeridentifier.is_set or self.bgppeeridentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeeridentifier.get_name_leafdata())
                if (self.bgppeerintotalmessages.is_set or self.bgppeerintotalmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerintotalmessages.get_name_leafdata())
                if (self.bgppeerinupdateelapsedtime.is_set or self.bgppeerinupdateelapsedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerinupdateelapsedtime.get_name_leafdata())
                if (self.bgppeerinupdates.is_set or self.bgppeerinupdates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerinupdates.get_name_leafdata())
                if (self.bgppeerkeepalive.is_set or self.bgppeerkeepalive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerkeepalive.get_name_leafdata())
                if (self.bgppeerkeepaliveconfigured.is_set or self.bgppeerkeepaliveconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerkeepaliveconfigured.get_name_leafdata())
                if (self.bgppeerlasterror.is_set or self.bgppeerlasterror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerlasterror.get_name_leafdata())
                if (self.bgppeerlocaladdr.is_set or self.bgppeerlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerlocaladdr.get_name_leafdata())
                if (self.bgppeerlocalport.is_set or self.bgppeerlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerlocalport.get_name_leafdata())
                if (self.bgppeerminasoriginationinterval.is_set or self.bgppeerminasoriginationinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerminasoriginationinterval.get_name_leafdata())
                if (self.bgppeerminrouteadvertisementinterval.is_set or self.bgppeerminrouteadvertisementinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerminrouteadvertisementinterval.get_name_leafdata())
                if (self.bgppeernegotiatedversion.is_set or self.bgppeernegotiatedversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeernegotiatedversion.get_name_leafdata())
                if (self.bgppeerouttotalmessages.is_set or self.bgppeerouttotalmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerouttotalmessages.get_name_leafdata())
                if (self.bgppeeroutupdates.is_set or self.bgppeeroutupdates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeeroutupdates.get_name_leafdata())
                if (self.bgppeerremoteas.is_set or self.bgppeerremoteas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteas.get_name_leafdata())
                if (self.bgppeerremoteport.is_set or self.bgppeerremoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteport.get_name_leafdata())
                if (self.bgppeerstate.is_set or self.bgppeerstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerstate.get_name_leafdata())
                if (self.cbgppeerlasterrortxt.is_set or self.cbgppeerlasterrortxt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerlasterrortxt.get_name_leafdata())
                if (self.cbgppeerprefixaccepted.is_set or self.cbgppeerprefixaccepted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixaccepted.get_name_leafdata())
                if (self.cbgppeerprefixadvertised.is_set or self.cbgppeerprefixadvertised.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixadvertised.get_name_leafdata())
                if (self.cbgppeerprefixdenied.is_set or self.cbgppeerprefixdenied.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixdenied.get_name_leafdata())
                if (self.cbgppeerprefixlimit.is_set or self.cbgppeerprefixlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixlimit.get_name_leafdata())
                if (self.cbgppeerprefixsuppressed.is_set or self.cbgppeerprefixsuppressed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixsuppressed.get_name_leafdata())
                if (self.cbgppeerprefixwithdrawn.is_set or self.cbgppeerprefixwithdrawn.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixwithdrawn.get_name_leafdata())
                if (self.cbgppeerprevstate.is_set or self.cbgppeerprevstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprevstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgpPeerRemoteAddr" or name == "bgpPeerAdminStatus" or name == "bgpPeerConnectRetryInterval" or name == "bgpPeerFsmEstablishedTime" or name == "bgpPeerFsmEstablishedTransitions" or name == "bgpPeerHoldTime" or name == "bgpPeerHoldTimeConfigured" or name == "bgpPeerIdentifier" or name == "bgpPeerInTotalMessages" or name == "bgpPeerInUpdateElapsedTime" or name == "bgpPeerInUpdates" or name == "bgpPeerKeepAlive" or name == "bgpPeerKeepAliveConfigured" or name == "bgpPeerLastError" or name == "bgpPeerLocalAddr" or name == "bgpPeerLocalPort" or name == "bgpPeerMinASOriginationInterval" or name == "bgpPeerMinRouteAdvertisementInterval" or name == "bgpPeerNegotiatedVersion" or name == "bgpPeerOutTotalMessages" or name == "bgpPeerOutUpdates" or name == "bgpPeerRemoteAs" or name == "bgpPeerRemotePort" or name == "bgpPeerState" or name == "cbgpPeerLastErrorTxt" or name == "cbgpPeerPrefixAccepted" or name == "cbgpPeerPrefixAdvertised" or name == "cbgpPeerPrefixDenied" or name == "cbgpPeerPrefixLimit" or name == "cbgpPeerPrefixSuppressed" or name == "cbgpPeerPrefixWithdrawn" or name == "cbgpPeerPrevState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgpPeerRemoteAddr"):
                    self.bgppeerremoteaddr = value
                    self.bgppeerremoteaddr.value_namespace = name_space
                    self.bgppeerremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerAdminStatus"):
                    self.bgppeeradminstatus = value
                    self.bgppeeradminstatus.value_namespace = name_space
                    self.bgppeeradminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerConnectRetryInterval"):
                    self.bgppeerconnectretryinterval = value
                    self.bgppeerconnectretryinterval.value_namespace = name_space
                    self.bgppeerconnectretryinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerFsmEstablishedTime"):
                    self.bgppeerfsmestablishedtime = value
                    self.bgppeerfsmestablishedtime.value_namespace = name_space
                    self.bgppeerfsmestablishedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerFsmEstablishedTransitions"):
                    self.bgppeerfsmestablishedtransitions = value
                    self.bgppeerfsmestablishedtransitions.value_namespace = name_space
                    self.bgppeerfsmestablishedtransitions.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerHoldTime"):
                    self.bgppeerholdtime = value
                    self.bgppeerholdtime.value_namespace = name_space
                    self.bgppeerholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerHoldTimeConfigured"):
                    self.bgppeerholdtimeconfigured = value
                    self.bgppeerholdtimeconfigured.value_namespace = name_space
                    self.bgppeerholdtimeconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerIdentifier"):
                    self.bgppeeridentifier = value
                    self.bgppeeridentifier.value_namespace = name_space
                    self.bgppeeridentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerInTotalMessages"):
                    self.bgppeerintotalmessages = value
                    self.bgppeerintotalmessages.value_namespace = name_space
                    self.bgppeerintotalmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerInUpdateElapsedTime"):
                    self.bgppeerinupdateelapsedtime = value
                    self.bgppeerinupdateelapsedtime.value_namespace = name_space
                    self.bgppeerinupdateelapsedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerInUpdates"):
                    self.bgppeerinupdates = value
                    self.bgppeerinupdates.value_namespace = name_space
                    self.bgppeerinupdates.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerKeepAlive"):
                    self.bgppeerkeepalive = value
                    self.bgppeerkeepalive.value_namespace = name_space
                    self.bgppeerkeepalive.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerKeepAliveConfigured"):
                    self.bgppeerkeepaliveconfigured = value
                    self.bgppeerkeepaliveconfigured.value_namespace = name_space
                    self.bgppeerkeepaliveconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerLastError"):
                    self.bgppeerlasterror = value
                    self.bgppeerlasterror.value_namespace = name_space
                    self.bgppeerlasterror.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerLocalAddr"):
                    self.bgppeerlocaladdr = value
                    self.bgppeerlocaladdr.value_namespace = name_space
                    self.bgppeerlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerLocalPort"):
                    self.bgppeerlocalport = value
                    self.bgppeerlocalport.value_namespace = name_space
                    self.bgppeerlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerMinASOriginationInterval"):
                    self.bgppeerminasoriginationinterval = value
                    self.bgppeerminasoriginationinterval.value_namespace = name_space
                    self.bgppeerminasoriginationinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerMinRouteAdvertisementInterval"):
                    self.bgppeerminrouteadvertisementinterval = value
                    self.bgppeerminrouteadvertisementinterval.value_namespace = name_space
                    self.bgppeerminrouteadvertisementinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerNegotiatedVersion"):
                    self.bgppeernegotiatedversion = value
                    self.bgppeernegotiatedversion.value_namespace = name_space
                    self.bgppeernegotiatedversion.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerOutTotalMessages"):
                    self.bgppeerouttotalmessages = value
                    self.bgppeerouttotalmessages.value_namespace = name_space
                    self.bgppeerouttotalmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerOutUpdates"):
                    self.bgppeeroutupdates = value
                    self.bgppeeroutupdates.value_namespace = name_space
                    self.bgppeeroutupdates.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerRemoteAs"):
                    self.bgppeerremoteas = value
                    self.bgppeerremoteas.value_namespace = name_space
                    self.bgppeerremoteas.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerRemotePort"):
                    self.bgppeerremoteport = value
                    self.bgppeerremoteport.value_namespace = name_space
                    self.bgppeerremoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPeerState"):
                    self.bgppeerstate = value
                    self.bgppeerstate.value_namespace = name_space
                    self.bgppeerstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerLastErrorTxt"):
                    self.cbgppeerlasterrortxt = value
                    self.cbgppeerlasterrortxt.value_namespace = name_space
                    self.cbgppeerlasterrortxt.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixAccepted"):
                    self.cbgppeerprefixaccepted = value
                    self.cbgppeerprefixaccepted.value_namespace = name_space
                    self.cbgppeerprefixaccepted.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixAdvertised"):
                    self.cbgppeerprefixadvertised = value
                    self.cbgppeerprefixadvertised.value_namespace = name_space
                    self.cbgppeerprefixadvertised.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixDenied"):
                    self.cbgppeerprefixdenied = value
                    self.cbgppeerprefixdenied.value_namespace = name_space
                    self.cbgppeerprefixdenied.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixLimit"):
                    self.cbgppeerprefixlimit = value
                    self.cbgppeerprefixlimit.value_namespace = name_space
                    self.cbgppeerprefixlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixSuppressed"):
                    self.cbgppeerprefixsuppressed = value
                    self.cbgppeerprefixsuppressed.value_namespace = name_space
                    self.cbgppeerprefixsuppressed.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixWithdrawn"):
                    self.cbgppeerprefixwithdrawn = value
                    self.cbgppeerprefixwithdrawn.value_namespace = name_space
                    self.cbgppeerprefixwithdrawn.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrevState"):
                    self.cbgppeerprevstate = value
                    self.cbgppeerprevstate.value_namespace = name_space
                    self.cbgppeerprevstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bgppeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bgppeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bgpPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BGP4-MIB:BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgpPeerEntry"):
                for c in self.bgppeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Bgp4Mib.Bgppeertable.Bgppeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bgppeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgpPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Bgprcvdpathattrtable(Entity):
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
            super(Bgp4Mib.Bgprcvdpathattrtable, self).__init__()

            self.yang_name = "bgpRcvdPathAttrTable"
            self.yang_parent_name = "BGP4-MIB"

            self.bgppathattrentry = YList(self)

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
                        super(Bgp4Mib.Bgprcvdpathattrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bgp4Mib.Bgprcvdpathattrtable, self).__setattr__(name, value)


        class Bgppathattrentry(Entity):
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
            	**type**\:   :py:class:`Bgppathattrorigin <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry.Bgppathattrorigin>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry, self).__init__()

                self.yang_name = "bgpPathAttrEntry"
                self.yang_parent_name = "bgpRcvdPathAttrTable"

                self.bgppathattrdestnetwork = YLeaf(YType.str, "bgpPathAttrDestNetwork")

                self.bgppathattrpeer = YLeaf(YType.str, "bgpPathAttrPeer")

                self.bgppathattraspath = YLeaf(YType.str, "bgpPathAttrASPath")

                self.bgppathattrinterasmetric = YLeaf(YType.int32, "bgpPathAttrInterASMetric")

                self.bgppathattrnexthop = YLeaf(YType.str, "bgpPathAttrNextHop")

                self.bgppathattrorigin = YLeaf(YType.enumeration, "bgpPathAttrOrigin")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgppathattrdestnetwork",
                                "bgppathattrpeer",
                                "bgppathattraspath",
                                "bgppathattrinterasmetric",
                                "bgppathattrnexthop",
                                "bgppathattrorigin") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry, self).__setattr__(name, value)

            class Bgppathattrorigin(Enum):
                """
                Bgppathattrorigin

                The ultimate origin of the path information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")


            def has_data(self):
                return (
                    self.bgppathattrdestnetwork.is_set or
                    self.bgppathattrpeer.is_set or
                    self.bgppathattraspath.is_set or
                    self.bgppathattrinterasmetric.is_set or
                    self.bgppathattrnexthop.is_set or
                    self.bgppathattrorigin.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgppathattrdestnetwork.yfilter != YFilter.not_set or
                    self.bgppathattrpeer.yfilter != YFilter.not_set or
                    self.bgppathattraspath.yfilter != YFilter.not_set or
                    self.bgppathattrinterasmetric.yfilter != YFilter.not_set or
                    self.bgppathattrnexthop.yfilter != YFilter.not_set or
                    self.bgppathattrorigin.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgpPathAttrEntry" + "[bgpPathAttrDestNetwork='" + self.bgppathattrdestnetwork.get() + "']" + "[bgpPathAttrPeer='" + self.bgppathattrpeer.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BGP4-MIB:BGP4-MIB/bgpRcvdPathAttrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgppathattrdestnetwork.is_set or self.bgppathattrdestnetwork.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattrdestnetwork.get_name_leafdata())
                if (self.bgppathattrpeer.is_set or self.bgppathattrpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattrpeer.get_name_leafdata())
                if (self.bgppathattraspath.is_set or self.bgppathattraspath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattraspath.get_name_leafdata())
                if (self.bgppathattrinterasmetric.is_set or self.bgppathattrinterasmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattrinterasmetric.get_name_leafdata())
                if (self.bgppathattrnexthop.is_set or self.bgppathattrnexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattrnexthop.get_name_leafdata())
                if (self.bgppathattrorigin.is_set or self.bgppathattrorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppathattrorigin.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgpPathAttrDestNetwork" or name == "bgpPathAttrPeer" or name == "bgpPathAttrASPath" or name == "bgpPathAttrInterASMetric" or name == "bgpPathAttrNextHop" or name == "bgpPathAttrOrigin"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgpPathAttrDestNetwork"):
                    self.bgppathattrdestnetwork = value
                    self.bgppathattrdestnetwork.value_namespace = name_space
                    self.bgppathattrdestnetwork.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPathAttrPeer"):
                    self.bgppathattrpeer = value
                    self.bgppathattrpeer.value_namespace = name_space
                    self.bgppathattrpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPathAttrASPath"):
                    self.bgppathattraspath = value
                    self.bgppathattraspath.value_namespace = name_space
                    self.bgppathattraspath.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPathAttrInterASMetric"):
                    self.bgppathattrinterasmetric = value
                    self.bgppathattrinterasmetric.value_namespace = name_space
                    self.bgppathattrinterasmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPathAttrNextHop"):
                    self.bgppathattrnexthop = value
                    self.bgppathattrnexthop.value_namespace = name_space
                    self.bgppathattrnexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "bgpPathAttrOrigin"):
                    self.bgppathattrorigin = value
                    self.bgppathattrorigin.value_namespace = name_space
                    self.bgppathattrorigin.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bgppathattrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bgppathattrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bgpRcvdPathAttrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BGP4-MIB:BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgpPathAttrEntry"):
                for c in self.bgppathattrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bgppathattrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgpPathAttrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Bgp4Pathattrtable(Entity):
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
            super(Bgp4Mib.Bgp4Pathattrtable, self).__init__()

            self.yang_name = "bgp4PathAttrTable"
            self.yang_parent_name = "BGP4-MIB"

            self.bgp4pathattrentry = YList(self)

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
                        super(Bgp4Mib.Bgp4Pathattrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bgp4Mib.Bgp4Pathattrtable, self).__setattr__(name, value)


        class Bgp4Pathattrentry(Entity):
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
            	**type**\:   :py:class:`Bgp4Pathattratomicaggregate <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattratomicaggregate>`
            
            .. attribute:: bgp4pathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:   :py:class:`Bgp4Pathattrbest <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattrbest>`
            
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
            	**type**\:   :py:class:`Bgp4Pathattrorigin <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4Pathattrorigin>`
            
            .. attribute:: bgp4pathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'BGP4-MIB'
            _revision = '1994-05-05'

            def __init__(self):
                super(Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry, self).__init__()

                self.yang_name = "bgp4PathAttrEntry"
                self.yang_parent_name = "bgp4PathAttrTable"

                self.bgp4pathattripaddrprefix = YLeaf(YType.str, "bgp4PathAttrIpAddrPrefix")

                self.bgp4pathattripaddrprefixlen = YLeaf(YType.int32, "bgp4PathAttrIpAddrPrefixLen")

                self.bgp4pathattrpeer = YLeaf(YType.str, "bgp4PathAttrPeer")

                self.bgp4pathattraggregatoraddr = YLeaf(YType.str, "bgp4PathAttrAggregatorAddr")

                self.bgp4pathattraggregatoras = YLeaf(YType.int32, "bgp4PathAttrAggregatorAS")

                self.bgp4pathattraspathsegment = YLeaf(YType.str, "bgp4PathAttrASPathSegment")

                self.bgp4pathattratomicaggregate = YLeaf(YType.enumeration, "bgp4PathAttrAtomicAggregate")

                self.bgp4pathattrbest = YLeaf(YType.enumeration, "bgp4PathAttrBest")

                self.bgp4pathattrcalclocalpref = YLeaf(YType.int32, "bgp4PathAttrCalcLocalPref")

                self.bgp4pathattrlocalpref = YLeaf(YType.int32, "bgp4PathAttrLocalPref")

                self.bgp4pathattrmultiexitdisc = YLeaf(YType.int32, "bgp4PathAttrMultiExitDisc")

                self.bgp4pathattrnexthop = YLeaf(YType.str, "bgp4PathAttrNextHop")

                self.bgp4pathattrorigin = YLeaf(YType.enumeration, "bgp4PathAttrOrigin")

                self.bgp4pathattrunknown = YLeaf(YType.str, "bgp4PathAttrUnknown")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgp4pathattripaddrprefix",
                                "bgp4pathattripaddrprefixlen",
                                "bgp4pathattrpeer",
                                "bgp4pathattraggregatoraddr",
                                "bgp4pathattraggregatoras",
                                "bgp4pathattraspathsegment",
                                "bgp4pathattratomicaggregate",
                                "bgp4pathattrbest",
                                "bgp4pathattrcalclocalpref",
                                "bgp4pathattrlocalpref",
                                "bgp4pathattrmultiexitdisc",
                                "bgp4pathattrnexthop",
                                "bgp4pathattrorigin",
                                "bgp4pathattrunknown") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry, self).__setattr__(name, value)

            class Bgp4Pathattratomicaggregate(Enum):
                """
                Bgp4Pathattratomicaggregate

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
                Bgp4Pathattrbest

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = Enum.YLeaf(1, "false")

                true = Enum.YLeaf(2, "true")


            class Bgp4Pathattrorigin(Enum):
                """
                Bgp4Pathattrorigin

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")


            def has_data(self):
                return (
                    self.bgp4pathattripaddrprefix.is_set or
                    self.bgp4pathattripaddrprefixlen.is_set or
                    self.bgp4pathattrpeer.is_set or
                    self.bgp4pathattraggregatoraddr.is_set or
                    self.bgp4pathattraggregatoras.is_set or
                    self.bgp4pathattraspathsegment.is_set or
                    self.bgp4pathattratomicaggregate.is_set or
                    self.bgp4pathattrbest.is_set or
                    self.bgp4pathattrcalclocalpref.is_set or
                    self.bgp4pathattrlocalpref.is_set or
                    self.bgp4pathattrmultiexitdisc.is_set or
                    self.bgp4pathattrnexthop.is_set or
                    self.bgp4pathattrorigin.is_set or
                    self.bgp4pathattrunknown.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgp4pathattripaddrprefix.yfilter != YFilter.not_set or
                    self.bgp4pathattripaddrprefixlen.yfilter != YFilter.not_set or
                    self.bgp4pathattrpeer.yfilter != YFilter.not_set or
                    self.bgp4pathattraggregatoraddr.yfilter != YFilter.not_set or
                    self.bgp4pathattraggregatoras.yfilter != YFilter.not_set or
                    self.bgp4pathattraspathsegment.yfilter != YFilter.not_set or
                    self.bgp4pathattratomicaggregate.yfilter != YFilter.not_set or
                    self.bgp4pathattrbest.yfilter != YFilter.not_set or
                    self.bgp4pathattrcalclocalpref.yfilter != YFilter.not_set or
                    self.bgp4pathattrlocalpref.yfilter != YFilter.not_set or
                    self.bgp4pathattrmultiexitdisc.yfilter != YFilter.not_set or
                    self.bgp4pathattrnexthop.yfilter != YFilter.not_set or
                    self.bgp4pathattrorigin.yfilter != YFilter.not_set or
                    self.bgp4pathattrunknown.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgp4PathAttrEntry" + "[bgp4PathAttrIpAddrPrefix='" + self.bgp4pathattripaddrprefix.get() + "']" + "[bgp4PathAttrIpAddrPrefixLen='" + self.bgp4pathattripaddrprefixlen.get() + "']" + "[bgp4PathAttrPeer='" + self.bgp4pathattrpeer.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BGP4-MIB:BGP4-MIB/bgp4PathAttrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgp4pathattripaddrprefix.is_set or self.bgp4pathattripaddrprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattripaddrprefix.get_name_leafdata())
                if (self.bgp4pathattripaddrprefixlen.is_set or self.bgp4pathattripaddrprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattripaddrprefixlen.get_name_leafdata())
                if (self.bgp4pathattrpeer.is_set or self.bgp4pathattrpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrpeer.get_name_leafdata())
                if (self.bgp4pathattraggregatoraddr.is_set or self.bgp4pathattraggregatoraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattraggregatoraddr.get_name_leafdata())
                if (self.bgp4pathattraggregatoras.is_set or self.bgp4pathattraggregatoras.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattraggregatoras.get_name_leafdata())
                if (self.bgp4pathattraspathsegment.is_set or self.bgp4pathattraspathsegment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattraspathsegment.get_name_leafdata())
                if (self.bgp4pathattratomicaggregate.is_set or self.bgp4pathattratomicaggregate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattratomicaggregate.get_name_leafdata())
                if (self.bgp4pathattrbest.is_set or self.bgp4pathattrbest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrbest.get_name_leafdata())
                if (self.bgp4pathattrcalclocalpref.is_set or self.bgp4pathattrcalclocalpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrcalclocalpref.get_name_leafdata())
                if (self.bgp4pathattrlocalpref.is_set or self.bgp4pathattrlocalpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrlocalpref.get_name_leafdata())
                if (self.bgp4pathattrmultiexitdisc.is_set or self.bgp4pathattrmultiexitdisc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrmultiexitdisc.get_name_leafdata())
                if (self.bgp4pathattrnexthop.is_set or self.bgp4pathattrnexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrnexthop.get_name_leafdata())
                if (self.bgp4pathattrorigin.is_set or self.bgp4pathattrorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrorigin.get_name_leafdata())
                if (self.bgp4pathattrunknown.is_set or self.bgp4pathattrunknown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp4pathattrunknown.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgp4PathAttrIpAddrPrefix" or name == "bgp4PathAttrIpAddrPrefixLen" or name == "bgp4PathAttrPeer" or name == "bgp4PathAttrAggregatorAddr" or name == "bgp4PathAttrAggregatorAS" or name == "bgp4PathAttrASPathSegment" or name == "bgp4PathAttrAtomicAggregate" or name == "bgp4PathAttrBest" or name == "bgp4PathAttrCalcLocalPref" or name == "bgp4PathAttrLocalPref" or name == "bgp4PathAttrMultiExitDisc" or name == "bgp4PathAttrNextHop" or name == "bgp4PathAttrOrigin" or name == "bgp4PathAttrUnknown"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgp4PathAttrIpAddrPrefix"):
                    self.bgp4pathattripaddrprefix = value
                    self.bgp4pathattripaddrprefix.value_namespace = name_space
                    self.bgp4pathattripaddrprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrIpAddrPrefixLen"):
                    self.bgp4pathattripaddrprefixlen = value
                    self.bgp4pathattripaddrprefixlen.value_namespace = name_space
                    self.bgp4pathattripaddrprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrPeer"):
                    self.bgp4pathattrpeer = value
                    self.bgp4pathattrpeer.value_namespace = name_space
                    self.bgp4pathattrpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrAggregatorAddr"):
                    self.bgp4pathattraggregatoraddr = value
                    self.bgp4pathattraggregatoraddr.value_namespace = name_space
                    self.bgp4pathattraggregatoraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrAggregatorAS"):
                    self.bgp4pathattraggregatoras = value
                    self.bgp4pathattraggregatoras.value_namespace = name_space
                    self.bgp4pathattraggregatoras.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrASPathSegment"):
                    self.bgp4pathattraspathsegment = value
                    self.bgp4pathattraspathsegment.value_namespace = name_space
                    self.bgp4pathattraspathsegment.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrAtomicAggregate"):
                    self.bgp4pathattratomicaggregate = value
                    self.bgp4pathattratomicaggregate.value_namespace = name_space
                    self.bgp4pathattratomicaggregate.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrBest"):
                    self.bgp4pathattrbest = value
                    self.bgp4pathattrbest.value_namespace = name_space
                    self.bgp4pathattrbest.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrCalcLocalPref"):
                    self.bgp4pathattrcalclocalpref = value
                    self.bgp4pathattrcalclocalpref.value_namespace = name_space
                    self.bgp4pathattrcalclocalpref.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrLocalPref"):
                    self.bgp4pathattrlocalpref = value
                    self.bgp4pathattrlocalpref.value_namespace = name_space
                    self.bgp4pathattrlocalpref.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrMultiExitDisc"):
                    self.bgp4pathattrmultiexitdisc = value
                    self.bgp4pathattrmultiexitdisc.value_namespace = name_space
                    self.bgp4pathattrmultiexitdisc.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrNextHop"):
                    self.bgp4pathattrnexthop = value
                    self.bgp4pathattrnexthop.value_namespace = name_space
                    self.bgp4pathattrnexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrOrigin"):
                    self.bgp4pathattrorigin = value
                    self.bgp4pathattrorigin.value_namespace = name_space
                    self.bgp4pathattrorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp4PathAttrUnknown"):
                    self.bgp4pathattrunknown = value
                    self.bgp4pathattrunknown.value_namespace = name_space
                    self.bgp4pathattrunknown.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bgp4pathattrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bgp4pathattrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bgp4PathAttrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BGP4-MIB:BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgp4PathAttrEntry"):
                for c in self.bgp4pathattrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bgp4pathattrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgp4PathAttrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.bgp is not None and self.bgp.has_data()) or
            (self.bgp4pathattrtable is not None and self.bgp4pathattrtable.has_data()) or
            (self.bgppeertable is not None and self.bgppeertable.has_data()) or
            (self.bgprcvdpathattrtable is not None and self.bgprcvdpathattrtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.bgp is not None and self.bgp.has_operation()) or
            (self.bgp4pathattrtable is not None and self.bgp4pathattrtable.has_operation()) or
            (self.bgppeertable is not None and self.bgppeertable.has_operation()) or
            (self.bgprcvdpathattrtable is not None and self.bgprcvdpathattrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "BGP4-MIB:BGP4-MIB" + path_buffer

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

        if (child_yang_name == "bgp"):
            if (self.bgp is None):
                self.bgp = Bgp4Mib.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "bgp"
            return self.bgp

        if (child_yang_name == "bgp4PathAttrTable"):
            if (self.bgp4pathattrtable is None):
                self.bgp4pathattrtable = Bgp4Mib.Bgp4Pathattrtable()
                self.bgp4pathattrtable.parent = self
                self._children_name_map["bgp4pathattrtable"] = "bgp4PathAttrTable"
            return self.bgp4pathattrtable

        if (child_yang_name == "bgpPeerTable"):
            if (self.bgppeertable is None):
                self.bgppeertable = Bgp4Mib.Bgppeertable()
                self.bgppeertable.parent = self
                self._children_name_map["bgppeertable"] = "bgpPeerTable"
            return self.bgppeertable

        if (child_yang_name == "bgpRcvdPathAttrTable"):
            if (self.bgprcvdpathattrtable is None):
                self.bgprcvdpathattrtable = Bgp4Mib.Bgprcvdpathattrtable()
                self.bgprcvdpathattrtable.parent = self
                self._children_name_map["bgprcvdpathattrtable"] = "bgpRcvdPathAttrTable"
            return self.bgprcvdpathattrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bgp" or name == "bgp4PathAttrTable" or name == "bgpPeerTable" or name == "bgpRcvdPathAttrTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Bgp4Mib()
        return self._top_entity

