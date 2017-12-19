""" DRAFT_MSDP_MIB 

An experimental MIB module for MSDP Management.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DRAFTMSDPMIB(Entity):
    """
    
    
    .. attribute:: msdp
    
    	
    	**type**\:  :py:class:`Msdp <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdp>`
    
    .. attribute:: msdprequeststable
    
    	The (conceptual) table listing group ranges and MSDP peers used when deciding where to send an SA Request message when required.  If SA Caching is enabled, this table may be empty
    	**type**\:  :py:class:`Msdprequeststable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdprequeststable>`
    
    .. attribute:: msdppeertable
    
    	The (conceptual) table listing the MSDP speaker's peers
    	**type**\:  :py:class:`Msdppeertable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdppeertable>`
    
    .. attribute:: msdpsacachetable
    
    	The (conceptual) table listing the MSDP SA advertisements currently in the MSDP speaker's cache
    	**type**\:  :py:class:`Msdpsacachetable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdpsacachetable>`
    
    

    """

    _prefix = 'DRAFT-MSDP-MIB'
    _revision = '1999-12-16'

    def __init__(self):
        super(DRAFTMSDPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DRAFT-MSDP-MIB"
        self.yang_parent_name = "DRAFT-MSDP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"msdp" : ("msdp", DRAFTMSDPMIB.Msdp), "msdpRequestsTable" : ("msdprequeststable", DRAFTMSDPMIB.Msdprequeststable), "msdpPeerTable" : ("msdppeertable", DRAFTMSDPMIB.Msdppeertable), "msdpSACacheTable" : ("msdpsacachetable", DRAFTMSDPMIB.Msdpsacachetable)}
        self._child_list_classes = {}

        self.msdp = DRAFTMSDPMIB.Msdp()
        self.msdp.parent = self
        self._children_name_map["msdp"] = "msdp"
        self._children_yang_names.add("msdp")

        self.msdprequeststable = DRAFTMSDPMIB.Msdprequeststable()
        self.msdprequeststable.parent = self
        self._children_name_map["msdprequeststable"] = "msdpRequestsTable"
        self._children_yang_names.add("msdpRequestsTable")

        self.msdppeertable = DRAFTMSDPMIB.Msdppeertable()
        self.msdppeertable.parent = self
        self._children_name_map["msdppeertable"] = "msdpPeerTable"
        self._children_yang_names.add("msdpPeerTable")

        self.msdpsacachetable = DRAFTMSDPMIB.Msdpsacachetable()
        self.msdpsacachetable.parent = self
        self._children_name_map["msdpsacachetable"] = "msdpSACacheTable"
        self._children_yang_names.add("msdpSACacheTable")
        self._segment_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB"


    class Msdp(Entity):
        """
        
        
        .. attribute:: msdpenabled
        
        	The state of MSDP on this MSDP speaker \- globally enabled or disabled
        	**type**\: bool
        
        .. attribute:: msdpcachelifetime
        
        	The lifetime given to SA cache entries when created or refreshed.  A value of 0 means no SA caching is done by this MSDP speaker
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpnumsacacheentries
        
        	The total number of entries in the SA Cache table
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpsaholddownperiod
        
        	The number of seconds in the MSDP SA Hold\-down period
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DRAFTMSDPMIB.Msdp, self).__init__()

            self.yang_name = "msdp"
            self.yang_parent_name = "DRAFT-MSDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.msdpenabled = YLeaf(YType.boolean, "msdpEnabled")

            self.msdpcachelifetime = YLeaf(YType.uint32, "msdpCacheLifetime")

            self.msdpnumsacacheentries = YLeaf(YType.uint32, "msdpNumSACacheEntries")

            self.msdpsaholddownperiod = YLeaf(YType.int32, "msdpSAHoldDownPeriod")
            self._segment_path = lambda: "msdp"
            self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DRAFTMSDPMIB.Msdp, ['msdpenabled', 'msdpcachelifetime', 'msdpnumsacacheentries', 'msdpsaholddownperiod'], name, value)


    class Msdprequeststable(Entity):
        """
        The (conceptual) table listing group ranges and MSDP
        peers used when deciding where to send an SA Request
        message when required.  If SA Caching is enabled, this
        table may be empty.
        
        .. attribute:: msdprequestsentry
        
        	An entry (conceptual row) representing a group range used when deciding where to send an SA Request message
        	**type**\: list of  		 :py:class:`Msdprequestsentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdprequeststable.Msdprequestsentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DRAFTMSDPMIB.Msdprequeststable, self).__init__()

            self.yang_name = "msdpRequestsTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"msdpRequestsEntry" : ("msdprequestsentry", DRAFTMSDPMIB.Msdprequeststable.Msdprequestsentry)}

            self.msdprequestsentry = YList(self)
            self._segment_path = lambda: "msdpRequestsTable"
            self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DRAFTMSDPMIB.Msdprequeststable, [], name, value)


        class Msdprequestsentry(Entity):
            """
            An entry (conceptual row) representing a group range
            used when deciding where to send an SA Request
            message.
            
            .. attribute:: msdprequestsgroupaddress  <key>
            
            	The group address that, when combined with the mask in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsgroupmask  <key>
            
            	The mask that, when combined with the group address in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestspeer
            
            	The peer to which MSDP SA Requests for groups matching this entry's group range will be sent.  Must match the INDEX of a row in the msdpPeerTable
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsstatus
            
            	The status of this row, by which new rows may be added to the table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DRAFTMSDPMIB.Msdprequeststable.Msdprequestsentry, self).__init__()

                self.yang_name = "msdpRequestsEntry"
                self.yang_parent_name = "msdpRequestsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.msdprequestsgroupaddress = YLeaf(YType.str, "msdpRequestsGroupAddress")

                self.msdprequestsgroupmask = YLeaf(YType.str, "msdpRequestsGroupMask")

                self.msdprequestspeer = YLeaf(YType.str, "msdpRequestsPeer")

                self.msdprequestsstatus = YLeaf(YType.enumeration, "msdpRequestsStatus")
                self._segment_path = lambda: "msdpRequestsEntry" + "[msdpRequestsGroupAddress='" + self.msdprequestsgroupaddress.get() + "']" + "[msdpRequestsGroupMask='" + self.msdprequestsgroupmask.get() + "']"
                self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpRequestsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DRAFTMSDPMIB.Msdprequeststable.Msdprequestsentry, ['msdprequestsgroupaddress', 'msdprequestsgroupmask', 'msdprequestspeer', 'msdprequestsstatus'], name, value)


    class Msdppeertable(Entity):
        """
        The (conceptual) table listing the MSDP speaker's
        peers.
        
        .. attribute:: msdppeerentry
        
        	An entry (conceptual row) representing an MSDP peer
        	**type**\: list of  		 :py:class:`Msdppeerentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdppeertable.Msdppeerentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DRAFTMSDPMIB.Msdppeertable, self).__init__()

            self.yang_name = "msdpPeerTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"msdpPeerEntry" : ("msdppeerentry", DRAFTMSDPMIB.Msdppeertable.Msdppeerentry)}

            self.msdppeerentry = YList(self)
            self._segment_path = lambda: "msdpPeerTable"
            self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DRAFTMSDPMIB.Msdppeertable, [], name, value)


        class Msdppeerentry(Entity):
            """
            An entry (conceptual row) representing an MSDP peer.
            
            .. attribute:: msdppeerremoteaddress  <key>
            
            	The address of the remote MSDP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeerstate
            
            	The state of the MSDP TCP connection with this peer
            	**type**\:  :py:class:`Msdppeerstate <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdppeertable.Msdppeerentry.Msdppeerstate>`
            
            .. attribute:: msdppeerrpffailures
            
            	The number of RPF failures on SA messages received from this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsas
            
            	The number of MSDP SA messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsas
            
            	The number of MSDP SA messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsarequests
            
            	The number of MSDP SA\-Request messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsarequests
            
            	The number of MSDP SA\-Request messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsaresponses
            
            	The number of MSDP SA\-Response messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsaresponses
            
            	The number of MSDP SA Response messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerincontrolmessages
            
            	The total number of MSDP messages received on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutcontrolmessages
            
            	The total number of MSDP messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerindatapackets
            
            	The total number of encapsulated data packets received from this peer.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutdatapackets
            
            	The total number of encapsulated data packets sent to this peer.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerfsmestablishedtransitions
            
            	The total number of times the MSDP FSM transitioned into the established state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerfsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state.  It is set to zero when a new peer is configured or the MSDP speaker is booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerinmessageelapsedtime
            
            	Elapsed time in seconds since the last MSDP message was received from the peer.  Each time msdpPeerInControlMessages is incremented, the value of this object is set to zero (0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerlocaladdress
            
            	The local IP address of this entry's MSDP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeersaadvperiod
            
            	Time interval in seconds for the MinSAAdvertisementInterval MSDP timer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: msdppeerconnectretryinterval
            
            	Time interval in seconds for the ConnectRetry timer
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerholdtimeconfigured
            
            	Time interval in seconds for the Hold Timer configured for this MSDP speaker with this peer
            	**type**\: int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerkeepaliveconfigured
            
            	Time interval in seconds for the KeepAlive timer configured for this MSDP speaker with this peer.  A reasonable maximum value for this timer would be configured to be one third of that of msdpPeerHoldTimeConfigured.  If the value of this object is zero (0), no periodic KEEPALIVE messages are sent to the peer after the MSDP connection has been established
            	**type**\: int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: msdppeerdatattl
            
            	The minimum TTL a packet is required to have before it may be forwarded using SA encapsulation to this peer
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: msdppeerprocessrequestsfrom
            
            	This object indicates whether or not to process MSDP SA Request messages from this peer.  If True(1), MSDP SA Request messages from this peer are processed and replied to (if appropriate) with SA Response messages. If False(2), MSDP SA Request messages from this peer are silently ignored.  It defaults to False when msdpCacheLifetime is 0 and True when msdpCacheLifetime is non\-0
            	**type**\: bool
            
            .. attribute:: msdppeerstatus
            
            	The RowStatus object by which peers can be added and deleted.  A transition to 'active' will cause the MSDP Start Event to be generated.  A transition out of the 'active' state will cause the MSDP Stop Event to be generated.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: msdppeerremoteport
            
            	The remote port for the TCP connection between the MSDP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeerlocalport
            
            	The local port for the TCP connection between the MSDP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeerencapsulationstate
            
            	The status of the encapsulation negotiation state machine
            	**type**\:  :py:class:`Msdppeerencapsulationstate <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdppeertable.Msdppeerentry.Msdppeerencapsulationstate>`
            
            .. attribute:: msdppeerencapsulationtype
            
            	The encapsulation in use when encapsulating data in SA messages to this peer
            	**type**\:  :py:class:`Msdppeerencapsulationtype <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdppeertable.Msdppeerentry.Msdppeerencapsulationtype>`
            
            .. attribute:: msdppeerconnectionattempts
            
            	The number of times the state machine has transitioned from inactive to connecting
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinnotifications
            
            	The number of MSDP Notification messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutnotifications
            
            	The number of MSDP Notification messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerlasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\: str
            
            	**length:** 2
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DRAFTMSDPMIB.Msdppeertable.Msdppeerentry, self).__init__()

                self.yang_name = "msdpPeerEntry"
                self.yang_parent_name = "msdpPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.msdppeerremoteaddress = YLeaf(YType.str, "msdpPeerRemoteAddress")

                self.msdppeerstate = YLeaf(YType.enumeration, "msdpPeerState")

                self.msdppeerrpffailures = YLeaf(YType.uint32, "msdpPeerRPFFailures")

                self.msdppeerinsas = YLeaf(YType.uint32, "msdpPeerInSAs")

                self.msdppeeroutsas = YLeaf(YType.uint32, "msdpPeerOutSAs")

                self.msdppeerinsarequests = YLeaf(YType.uint32, "msdpPeerInSARequests")

                self.msdppeeroutsarequests = YLeaf(YType.uint32, "msdpPeerOutSARequests")

                self.msdppeerinsaresponses = YLeaf(YType.uint32, "msdpPeerInSAResponses")

                self.msdppeeroutsaresponses = YLeaf(YType.uint32, "msdpPeerOutSAResponses")

                self.msdppeerincontrolmessages = YLeaf(YType.uint32, "msdpPeerInControlMessages")

                self.msdppeeroutcontrolmessages = YLeaf(YType.uint32, "msdpPeerOutControlMessages")

                self.msdppeerindatapackets = YLeaf(YType.uint32, "msdpPeerInDataPackets")

                self.msdppeeroutdatapackets = YLeaf(YType.uint32, "msdpPeerOutDataPackets")

                self.msdppeerfsmestablishedtransitions = YLeaf(YType.uint32, "msdpPeerFsmEstablishedTransitions")

                self.msdppeerfsmestablishedtime = YLeaf(YType.uint32, "msdpPeerFsmEstablishedTime")

                self.msdppeerinmessageelapsedtime = YLeaf(YType.uint32, "msdpPeerInMessageElapsedTime")

                self.msdppeerlocaladdress = YLeaf(YType.str, "msdpPeerLocalAddress")

                self.msdppeersaadvperiod = YLeaf(YType.int32, "msdpPeerSAAdvPeriod")

                self.msdppeerconnectretryinterval = YLeaf(YType.int32, "msdpPeerConnectRetryInterval")

                self.msdppeerholdtimeconfigured = YLeaf(YType.int32, "msdpPeerHoldTimeConfigured")

                self.msdppeerkeepaliveconfigured = YLeaf(YType.int32, "msdpPeerKeepAliveConfigured")

                self.msdppeerdatattl = YLeaf(YType.int32, "msdpPeerDataTtl")

                self.msdppeerprocessrequestsfrom = YLeaf(YType.boolean, "msdpPeerProcessRequestsFrom")

                self.msdppeerstatus = YLeaf(YType.enumeration, "msdpPeerStatus")

                self.msdppeerremoteport = YLeaf(YType.int32, "msdpPeerRemotePort")

                self.msdppeerlocalport = YLeaf(YType.int32, "msdpPeerLocalPort")

                self.msdppeerencapsulationstate = YLeaf(YType.enumeration, "msdpPeerEncapsulationState")

                self.msdppeerencapsulationtype = YLeaf(YType.enumeration, "msdpPeerEncapsulationType")

                self.msdppeerconnectionattempts = YLeaf(YType.uint32, "msdpPeerConnectionAttempts")

                self.msdppeerinnotifications = YLeaf(YType.uint32, "msdpPeerInNotifications")

                self.msdppeeroutnotifications = YLeaf(YType.uint32, "msdpPeerOutNotifications")

                self.msdppeerlasterror = YLeaf(YType.str, "msdpPeerLastError")
                self._segment_path = lambda: "msdpPeerEntry" + "[msdpPeerRemoteAddress='" + self.msdppeerremoteaddress.get() + "']"
                self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpPeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DRAFTMSDPMIB.Msdppeertable.Msdppeerentry, ['msdppeerremoteaddress', 'msdppeerstate', 'msdppeerrpffailures', 'msdppeerinsas', 'msdppeeroutsas', 'msdppeerinsarequests', 'msdppeeroutsarequests', 'msdppeerinsaresponses', 'msdppeeroutsaresponses', 'msdppeerincontrolmessages', 'msdppeeroutcontrolmessages', 'msdppeerindatapackets', 'msdppeeroutdatapackets', 'msdppeerfsmestablishedtransitions', 'msdppeerfsmestablishedtime', 'msdppeerinmessageelapsedtime', 'msdppeerlocaladdress', 'msdppeersaadvperiod', 'msdppeerconnectretryinterval', 'msdppeerholdtimeconfigured', 'msdppeerkeepaliveconfigured', 'msdppeerdatattl', 'msdppeerprocessrequestsfrom', 'msdppeerstatus', 'msdppeerremoteport', 'msdppeerlocalport', 'msdppeerencapsulationstate', 'msdppeerencapsulationtype', 'msdppeerconnectionattempts', 'msdppeerinnotifications', 'msdppeeroutnotifications', 'msdppeerlasterror'], name, value)

            class Msdppeerencapsulationstate(Enum):
                """
                Msdppeerencapsulationstate

                The status of the encapsulation negotiation state

                machine.

                .. data:: default = 1

                .. data:: received = 2

                .. data:: advertising = 3

                .. data:: sent = 4

                .. data:: agreed = 5

                .. data:: failed = 6

                """

                default = Enum.YLeaf(1, "default")

                received = Enum.YLeaf(2, "received")

                advertising = Enum.YLeaf(3, "advertising")

                sent = Enum.YLeaf(4, "sent")

                agreed = Enum.YLeaf(5, "agreed")

                failed = Enum.YLeaf(6, "failed")


            class Msdppeerencapsulationtype(Enum):
                """
                Msdppeerencapsulationtype

                The encapsulation in use when encapsulating data in

                SA messages to this peer.

                .. data:: tcp = 1

                .. data:: udp = 2

                .. data:: gre = 3

                """

                tcp = Enum.YLeaf(1, "tcp")

                udp = Enum.YLeaf(2, "udp")

                gre = Enum.YLeaf(3, "gre")


            class Msdppeerstate(Enum):
                """
                Msdppeerstate

                The state of the MSDP TCP connection with this peer.

                .. data:: inactive = 1

                .. data:: listen = 2

                .. data:: connecting = 3

                .. data:: established = 4

                .. data:: disabled = 5

                """

                inactive = Enum.YLeaf(1, "inactive")

                listen = Enum.YLeaf(2, "listen")

                connecting = Enum.YLeaf(3, "connecting")

                established = Enum.YLeaf(4, "established")

                disabled = Enum.YLeaf(5, "disabled")



    class Msdpsacachetable(Entity):
        """
        The (conceptual) table listing the MSDP SA
        advertisements currently in the MSDP speaker's cache.
        
        .. attribute:: msdpsacacheentry
        
        	An entry (conceptual row) representing an MSDP SA advert
        	**type**\: list of  		 :py:class:`Msdpsacacheentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DRAFTMSDPMIB.Msdpsacachetable.Msdpsacacheentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DRAFTMSDPMIB.Msdpsacachetable, self).__init__()

            self.yang_name = "msdpSACacheTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"msdpSACacheEntry" : ("msdpsacacheentry", DRAFTMSDPMIB.Msdpsacachetable.Msdpsacacheentry)}

            self.msdpsacacheentry = YList(self)
            self._segment_path = lambda: "msdpSACacheTable"
            self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DRAFTMSDPMIB.Msdpsacachetable, [], name, value)


        class Msdpsacacheentry(Entity):
            """
            An entry (conceptual row) representing an MSDP SA
            advert.
            
            .. attribute:: msdpsacachegroupaddr  <key>
            
            	The group address of the SA Cache entry
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachesourceaddr  <key>
            
            	The source address of the SA Cache entry
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheoriginrp  <key>
            
            	The address of the RP which originated the last SA message accepted for this entry
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachepeerlearnedfrom
            
            	The peer from which this SA Cache entry was last accepted.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacherpfpeer
            
            	The peer from which an SA message corresponding to this cache entry would be accepted (i.e. the RPF peer for msdpSACacheOriginRP).  This may be different than msdpSACachePeerLearnedFrom if this entry was created by an MSDP SA\-Response.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheinsas
            
            	The number of MSDP SA messages received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheindatapackets
            
            	The number of MSDP encapsulated data packets received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheuptime
            
            	The time since this entry was placed in the SA cache
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheexpirytime
            
            	The time remaining before this entry will expire from the SA cache
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacachestatus
            
            	The status of this row in the table.  The only allowable actions are to retreive the status, which will be `active', or to set the status to `destroy' in order to remove this entry from the cache
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DRAFTMSDPMIB.Msdpsacachetable.Msdpsacacheentry, self).__init__()

                self.yang_name = "msdpSACacheEntry"
                self.yang_parent_name = "msdpSACacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.msdpsacachegroupaddr = YLeaf(YType.str, "msdpSACacheGroupAddr")

                self.msdpsacachesourceaddr = YLeaf(YType.str, "msdpSACacheSourceAddr")

                self.msdpsacacheoriginrp = YLeaf(YType.str, "msdpSACacheOriginRP")

                self.msdpsacachepeerlearnedfrom = YLeaf(YType.str, "msdpSACachePeerLearnedFrom")

                self.msdpsacacherpfpeer = YLeaf(YType.str, "msdpSACacheRPFPeer")

                self.msdpsacacheinsas = YLeaf(YType.uint32, "msdpSACacheInSAs")

                self.msdpsacacheindatapackets = YLeaf(YType.uint32, "msdpSACacheInDataPackets")

                self.msdpsacacheuptime = YLeaf(YType.uint32, "msdpSACacheUpTime")

                self.msdpsacacheexpirytime = YLeaf(YType.uint32, "msdpSACacheExpiryTime")

                self.msdpsacachestatus = YLeaf(YType.enumeration, "msdpSACacheStatus")
                self._segment_path = lambda: "msdpSACacheEntry" + "[msdpSACacheGroupAddr='" + self.msdpsacachegroupaddr.get() + "']" + "[msdpSACacheSourceAddr='" + self.msdpsacachesourceaddr.get() + "']" + "[msdpSACacheOriginRP='" + self.msdpsacacheoriginrp.get() + "']"
                self._absolute_path = lambda: "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpSACacheTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DRAFTMSDPMIB.Msdpsacachetable.Msdpsacacheentry, ['msdpsacachegroupaddr', 'msdpsacachesourceaddr', 'msdpsacacheoriginrp', 'msdpsacachepeerlearnedfrom', 'msdpsacacherpfpeer', 'msdpsacacheinsas', 'msdpsacacheindatapackets', 'msdpsacacheuptime', 'msdpsacacheexpirytime', 'msdpsacachestatus'], name, value)

    def clone_ptr(self):
        self._top_entity = DRAFTMSDPMIB()
        return self._top_entity

