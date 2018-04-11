""" DIAL_CONTROL_MIB 

The MIB module to describe peer information for
demand access and possibly other kinds of interfaces.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DIALCONTROLMIB(Entity):
    """
    
    
    .. attribute:: dialctlconfiguration
    
    	
    	**type**\:  :py:class:`Dialctlconfiguration <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlconfiguration>`
    
    .. attribute:: callhistory
    
    	
    	**type**\:  :py:class:`Callhistory <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callhistory>`
    
    .. attribute:: dialctlpeercfgtable
    
    	The list of peers from which the managed device will accept calls or to which it will place them
    	**type**\:  :py:class:`Dialctlpeercfgtable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlpeercfgtable>`
    
    .. attribute:: callactivetable
    
    	A table containing information about active calls to a specific destination
    	**type**\:  :py:class:`Callactivetable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable>`
    
    .. attribute:: callhistorytable
    
    	A table containing information about specific calls to a specific destination
    	**type**\:  :py:class:`Callhistorytable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callhistorytable>`
    
    

    """

    _prefix = 'DIAL-CONTROL-MIB'
    _revision = '1996-09-23'

    def __init__(self):
        super(DIALCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DIAL-CONTROL-MIB"
        self.yang_parent_name = "DIAL-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("dialCtlConfiguration", ("dialctlconfiguration", DIALCONTROLMIB.Dialctlconfiguration)), ("callHistory", ("callhistory", DIALCONTROLMIB.Callhistory)), ("dialCtlPeerCfgTable", ("dialctlpeercfgtable", DIALCONTROLMIB.Dialctlpeercfgtable)), ("callActiveTable", ("callactivetable", DIALCONTROLMIB.Callactivetable)), ("callHistoryTable", ("callhistorytable", DIALCONTROLMIB.Callhistorytable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.dialctlconfiguration = DIALCONTROLMIB.Dialctlconfiguration()
        self.dialctlconfiguration.parent = self
        self._children_name_map["dialctlconfiguration"] = "dialCtlConfiguration"
        self._children_yang_names.add("dialCtlConfiguration")

        self.callhistory = DIALCONTROLMIB.Callhistory()
        self.callhistory.parent = self
        self._children_name_map["callhistory"] = "callHistory"
        self._children_yang_names.add("callHistory")

        self.dialctlpeercfgtable = DIALCONTROLMIB.Dialctlpeercfgtable()
        self.dialctlpeercfgtable.parent = self
        self._children_name_map["dialctlpeercfgtable"] = "dialCtlPeerCfgTable"
        self._children_yang_names.add("dialCtlPeerCfgTable")

        self.callactivetable = DIALCONTROLMIB.Callactivetable()
        self.callactivetable.parent = self
        self._children_name_map["callactivetable"] = "callActiveTable"
        self._children_yang_names.add("callActiveTable")

        self.callhistorytable = DIALCONTROLMIB.Callhistorytable()
        self.callhistorytable.parent = self
        self._children_name_map["callhistorytable"] = "callHistoryTable"
        self._children_yang_names.add("callHistoryTable")
        self._segment_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB"


    class Dialctlconfiguration(Entity):
        """
        
        
        .. attribute:: dialctlacceptmode
        
        	The security level for acceptance of incoming calls. acceptNone(1)  \- incoming calls will not be accepted acceptAll(2)   \- incoming calls will be accepted,                  even if there is no matching entry                  in the dialCtlPeerCfgTable acceptKnown(3) \- incoming calls will be accepted only                  if there is a matching entry in the                  dialCtlPeerCfgTable
        	**type**\:  :py:class:`Dialctlacceptmode <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlconfiguration.Dialctlacceptmode>`
        
        .. attribute:: dialctltrapenable
        
        	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for all peers. If the value of this object is enabled(1), traps will be generated for all peers. If the value of this object is disabled(2), traps will be generated only for peers having dialCtlPeerCfgTrapEnable set to enabled(1)
        	**type**\:  :py:class:`Dialctltrapenable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlconfiguration.Dialctltrapenable>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DIALCONTROLMIB.Dialctlconfiguration, self).__init__()

            self.yang_name = "dialCtlConfiguration"
            self.yang_parent_name = "DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dialctlacceptmode', YLeaf(YType.enumeration, 'dialCtlAcceptMode')),
                ('dialctltrapenable', YLeaf(YType.enumeration, 'dialCtlTrapEnable')),
            ])
            self.dialctlacceptmode = None
            self.dialctltrapenable = None
            self._segment_path = lambda: "dialCtlConfiguration"
            self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DIALCONTROLMIB.Dialctlconfiguration, ['dialctlacceptmode', 'dialctltrapenable'], name, value)

        class Dialctlacceptmode(Enum):
            """
            Dialctlacceptmode (Enum Class)

            The security level for acceptance of incoming calls.

            acceptNone(1)  \- incoming calls will not be accepted

            acceptAll(2)   \- incoming calls will be accepted,

                             even if there is no matching entry

                             in the dialCtlPeerCfgTable

            acceptKnown(3) \- incoming calls will be accepted only

                             if there is a matching entry in the

                             dialCtlPeerCfgTable

            .. data:: acceptNone = 1

            .. data:: acceptAll = 2

            .. data:: acceptKnown = 3

            """

            acceptNone = Enum.YLeaf(1, "acceptNone")

            acceptAll = Enum.YLeaf(2, "acceptAll")

            acceptKnown = Enum.YLeaf(3, "acceptKnown")


        class Dialctltrapenable(Enum):
            """
            Dialctltrapenable (Enum Class)

            This object indicates whether dialCtlPeerCallInformation

            and dialCtlPeerCallSetup traps should be generated for

            all peers. If the value of this object is enabled(1),

            traps will be generated for all peers. If the value

            of this object is disabled(2), traps will be generated

            only for peers having dialCtlPeerCfgTrapEnable set

            to enabled(1).

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")



    class Callhistory(Entity):
        """
        
        
        .. attribute:: callhistorytablemaxlength
        
        	The upper limit on the number of entries that the callHistoryTable may contain.  A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and the new one will be created
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: callhistoryretaintimer
        
        	The minimum amount of time that an callHistoryEntry will be maintained before being deleted. A value of 0 will prevent any history from being retained in the callHistoryTable, but will neither prevent callCompletion traps being generated nor affect other tables
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: minutes
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DIALCONTROLMIB.Callhistory, self).__init__()

            self.yang_name = "callHistory"
            self.yang_parent_name = "DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('callhistorytablemaxlength', YLeaf(YType.int32, 'callHistoryTableMaxLength')),
                ('callhistoryretaintimer', YLeaf(YType.int32, 'callHistoryRetainTimer')),
            ])
            self.callhistorytablemaxlength = None
            self.callhistoryretaintimer = None
            self._segment_path = lambda: "callHistory"
            self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DIALCONTROLMIB.Callhistory, ['callhistorytablemaxlength', 'callhistoryretaintimer'], name, value)


    class Dialctlpeercfgtable(Entity):
        """
        The list of peers from which the managed device
        will accept calls or to which it will place them.
        
        .. attribute:: dialctlpeercfgentry
        
        	Configuration data for a single Peer. This entry is effectively permanent, and contains information to identify the peer, how to connect to the peer, how to identify the peer and its permissions. The value of dialCtlPeerCfgOriginateAddress must be specified before a new row in this table can become active(1). Any writeable parameters in an existing entry can be modified while the entry is active. The modification will take effect when the peer in question will be called the next time. An entry in this table can only be created if the associated ifEntry already exists
        	**type**\: list of  		 :py:class:`Dialctlpeercfgentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DIALCONTROLMIB.Dialctlpeercfgtable, self).__init__()

            self.yang_name = "dialCtlPeerCfgTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dialCtlPeerCfgEntry", ("dialctlpeercfgentry", DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry))])
            self._leafs = OrderedDict()

            self.dialctlpeercfgentry = YList(self)
            self._segment_path = lambda: "dialCtlPeerCfgTable"
            self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DIALCONTROLMIB.Dialctlpeercfgtable, [], name, value)


        class Dialctlpeercfgentry(Entity):
            """
            Configuration data for a single Peer. This entry is
            effectively permanent, and contains information
            to identify the peer, how to connect to the peer,
            how to identify the peer and its permissions.
            The value of dialCtlPeerCfgOriginateAddress must be
            specified before a new row in this table can become
            active(1). Any writeable parameters in an existing entry
            can be modified while the entry is active. The modification
            will take effect when the peer in question will be
            called the next time.
            An entry in this table can only be created if the
            associated ifEntry already exists.
            
            .. attribute:: dialctlpeercfgid  (key)
            
            	This object identifies a single peer. There may be several entries in this table for one peer, defining different ways of reaching this peer. Thus, there may be several entries in this table with the same value of dialCtlPeerCfgId. Multiple entries for one peer may be used to support multilink as well as backup lines. A single peer will be identified by a unique value of this object. Several entries for one peer MUST have the same value of dialCtlPeerCfgId, but different ifEntries and thus different values of ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: dialctlpeercfgiftype
            
            	The interface type to be used for calling this peer. In case of ISDN, the value of isdn(63) is to be used
            	**type**\:  :py:class:`IANAifType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAifType>`
            
            .. attribute:: dialctlpeercfglowerif
            
            	ifIndex value of an interface the peer will have to be called on. For example, on an ISDN interface, this can be the ifIndex value of a D channel or the ifIndex value of a B channel, whatever is appropriate for a given peer. As an example, for Basic Rate leased lines it will be necessary to specify a B channel ifIndex, while for     semi\-permanent connections the D channel ifIndex has to be specified. If the interface can be dynamically assigned, this object has a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgoriginateaddress
            
            	Call Address at which the peer will be called. Think of this as the set of characters following 'ATDT ' or the 'phone number' included in a D channel call request.  The structure of this information will be switch type specific. If there is no address information required for reaching the peer, i.e., for leased lines, this object will be a zero length string
            	**type**\: str
            
            .. attribute:: dialctlpeercfgansweraddress
            
            	Calling Party Number information element, as for example passed in an ISDN SETUP message by a PBX or switch, for incoming calls. This address can be used to identify the peer. If this address is either unknown or identical to dialCtlPeerCfgOriginateAddress, this object will be a zero length string
            	**type**\: str
            
            .. attribute:: dialctlpeercfgsubaddress
            
            	Subaddress at which the peer will be called. If the subaddress is undefined for the given media or unused, this is a zero length string
            	**type**\: str
            
            .. attribute:: dialctlpeercfgclosedusergroup
            
            	Closed User Group at which the peer will be called. If the Closed User Group is undefined for the given media or unused, this is a zero length string
            	**type**\: str
            
            .. attribute:: dialctlpeercfgspeed
            
            	The desired information transfer speed in bits/second when calling this peer. The detailed media specific information, e.g. information type and information transfer rate for ISDN circuits, has to be extracted from this object. If the transfer speed to be used is unknown or the default speed for this type of interfaces, the value of this object may be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfginfotype
            
            	The Information Transfer Capability to be used when calling this peer.  speech(2) refers to a non\-data connection, whereas audio31(6) and audio7(7) refer to data mode connections
            	**type**\:  :py:class:`Dialctlpeercfginfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfginfotype>`
            
            .. attribute:: dialctlpeercfgpermission
            
            	Applicable permissions. callback(4) either rejects the call and then calls back, or uses the 'Reverse charging' information element if it is available. Note that callback(4) is supposed to control charging, not security, and applies to callback prior to accepting a call. Callback for security reasons can be handled using PPP callback
            	**type**\:  :py:class:`Dialctlpeercfgpermission <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfgpermission>`
            
            .. attribute:: dialctlpeercfginactivitytimer
            
            	The connection will be automatically disconnected if no longer carrying useful data for a time period, in seconds, specified in this object. Useful data in this context refers to forwarding packets, including routing information; it excludes the encapsulator maintenance frames. A value of zero means the connection will not be automatically taken down due to inactivity, which implies that it is a dedicated circuit
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgminduration
            
            	Minimum duration of a call in seconds, starting from the time the call is connected until the call is disconnected. This is to accomplish the fact that in most countries charging applies to units of time, which should be matched as closely as possible
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgmaxduration
            
            	Maximum call duration in seconds. Zero means 'unlimited'
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgcarrierdelay
            
            	The call timeout time in seconds. The default value of zero means that the call timeout as specified for the media in question will apply
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgcallretries
            
            	The number of calls to a non\-responding address that may be made. A retry count of zero means there is no bound. The intent is to bound the number of successive calls to an address which is inaccessible, or which refuses those calls.  Some countries regulate the number of call retries to a given peer that can be made
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgretrydelay
            
            	The time in seconds between call retries if a peer cannot be reached. A value of zero means that call retries may be done without any delay
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgfailuredelay
            
            	The time in seconds after which call attempts are to be placed again after a peer has been noticed to be unreachable, i.e. after dialCtlPeerCfgCallRetries unsuccessful call attempts. A value of zero means that a peer will not be called again after dialCtlPeerCfgCallRetries unsuccessful call attempts
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgtrapenable
            
            	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for this peer
            	**type**\:  :py:class:`Dialctlpeercfgtrapenable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfgtrapenable>`
            
            .. attribute:: dialctlpeercfgstatus
            
            	Status of one row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: dialctlpeerstatsconnecttime
            
            	Accumulated connect time to the peer since system startup. This is the total connect time, i.e. the connect time for outgoing calls plus the time for incoming calls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeerstatschargedunits
            
            	The total number of charging units applying to this peer since system startup. Only the charging units applying to the local interface, i.e. for originated calls or for calls with 'Reverse charging' being active, will be counted here
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatssuccesscalls
            
            	Number of completed calls to this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsfailcalls
            
            	Number of failed call attempts to this peer since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsacceptcalls
            
            	Number of calls from this peer accepted since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsrefusecalls
            
            	Number of calls from this peer refused since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatslastdisconnectcause
            
            	The encoded network cause value associated with the last call. This object will be updated whenever a call is started or cleared. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\: str
            
            	**length:** 0..4
            
            .. attribute:: dialctlpeerstatslastdisconnecttext
            
            	ASCII text describing the reason for the last call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause.  This object will be updated whenever a call is started or cleared
            	**type**\: str
            
            .. attribute:: dialctlpeerstatslastsetuptime
            
            	The value of sysUpTime when the last call to this peer was started. For ISDN media, this will be the time when the setup message was received from or sent to the network. This object will be updated whenever a call is started or cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry, self).__init__()

                self.yang_name = "dialCtlPeerCfgEntry"
                self.yang_parent_name = "dialCtlPeerCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dialctlpeercfgid','ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dialctlpeercfgid', YLeaf(YType.int32, 'dialCtlPeerCfgId')),
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('dialctlpeercfgiftype', YLeaf(YType.enumeration, 'dialCtlPeerCfgIfType')),
                    ('dialctlpeercfglowerif', YLeaf(YType.int32, 'dialCtlPeerCfgLowerIf')),
                    ('dialctlpeercfgoriginateaddress', YLeaf(YType.str, 'dialCtlPeerCfgOriginateAddress')),
                    ('dialctlpeercfgansweraddress', YLeaf(YType.str, 'dialCtlPeerCfgAnswerAddress')),
                    ('dialctlpeercfgsubaddress', YLeaf(YType.str, 'dialCtlPeerCfgSubAddress')),
                    ('dialctlpeercfgclosedusergroup', YLeaf(YType.str, 'dialCtlPeerCfgClosedUserGroup')),
                    ('dialctlpeercfgspeed', YLeaf(YType.int32, 'dialCtlPeerCfgSpeed')),
                    ('dialctlpeercfginfotype', YLeaf(YType.enumeration, 'dialCtlPeerCfgInfoType')),
                    ('dialctlpeercfgpermission', YLeaf(YType.enumeration, 'dialCtlPeerCfgPermission')),
                    ('dialctlpeercfginactivitytimer', YLeaf(YType.int32, 'dialCtlPeerCfgInactivityTimer')),
                    ('dialctlpeercfgminduration', YLeaf(YType.int32, 'dialCtlPeerCfgMinDuration')),
                    ('dialctlpeercfgmaxduration', YLeaf(YType.int32, 'dialCtlPeerCfgMaxDuration')),
                    ('dialctlpeercfgcarrierdelay', YLeaf(YType.int32, 'dialCtlPeerCfgCarrierDelay')),
                    ('dialctlpeercfgcallretries', YLeaf(YType.int32, 'dialCtlPeerCfgCallRetries')),
                    ('dialctlpeercfgretrydelay', YLeaf(YType.int32, 'dialCtlPeerCfgRetryDelay')),
                    ('dialctlpeercfgfailuredelay', YLeaf(YType.int32, 'dialCtlPeerCfgFailureDelay')),
                    ('dialctlpeercfgtrapenable', YLeaf(YType.enumeration, 'dialCtlPeerCfgTrapEnable')),
                    ('dialctlpeercfgstatus', YLeaf(YType.enumeration, 'dialCtlPeerCfgStatus')),
                    ('dialctlpeerstatsconnecttime', YLeaf(YType.uint32, 'dialCtlPeerStatsConnectTime')),
                    ('dialctlpeerstatschargedunits', YLeaf(YType.uint32, 'dialCtlPeerStatsChargedUnits')),
                    ('dialctlpeerstatssuccesscalls', YLeaf(YType.uint32, 'dialCtlPeerStatsSuccessCalls')),
                    ('dialctlpeerstatsfailcalls', YLeaf(YType.uint32, 'dialCtlPeerStatsFailCalls')),
                    ('dialctlpeerstatsacceptcalls', YLeaf(YType.uint32, 'dialCtlPeerStatsAcceptCalls')),
                    ('dialctlpeerstatsrefusecalls', YLeaf(YType.uint32, 'dialCtlPeerStatsRefuseCalls')),
                    ('dialctlpeerstatslastdisconnectcause', YLeaf(YType.str, 'dialCtlPeerStatsLastDisconnectCause')),
                    ('dialctlpeerstatslastdisconnecttext', YLeaf(YType.str, 'dialCtlPeerStatsLastDisconnectText')),
                    ('dialctlpeerstatslastsetuptime', YLeaf(YType.uint32, 'dialCtlPeerStatsLastSetupTime')),
                ])
                self.dialctlpeercfgid = None
                self.ifindex = None
                self.dialctlpeercfgiftype = None
                self.dialctlpeercfglowerif = None
                self.dialctlpeercfgoriginateaddress = None
                self.dialctlpeercfgansweraddress = None
                self.dialctlpeercfgsubaddress = None
                self.dialctlpeercfgclosedusergroup = None
                self.dialctlpeercfgspeed = None
                self.dialctlpeercfginfotype = None
                self.dialctlpeercfgpermission = None
                self.dialctlpeercfginactivitytimer = None
                self.dialctlpeercfgminduration = None
                self.dialctlpeercfgmaxduration = None
                self.dialctlpeercfgcarrierdelay = None
                self.dialctlpeercfgcallretries = None
                self.dialctlpeercfgretrydelay = None
                self.dialctlpeercfgfailuredelay = None
                self.dialctlpeercfgtrapenable = None
                self.dialctlpeercfgstatus = None
                self.dialctlpeerstatsconnecttime = None
                self.dialctlpeerstatschargedunits = None
                self.dialctlpeerstatssuccesscalls = None
                self.dialctlpeerstatsfailcalls = None
                self.dialctlpeerstatsacceptcalls = None
                self.dialctlpeerstatsrefusecalls = None
                self.dialctlpeerstatslastdisconnectcause = None
                self.dialctlpeerstatslastdisconnecttext = None
                self.dialctlpeerstatslastsetuptime = None
                self._segment_path = lambda: "dialCtlPeerCfgEntry" + "[dialCtlPeerCfgId='" + str(self.dialctlpeercfgid) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/dialCtlPeerCfgTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DIALCONTROLMIB.Dialctlpeercfgtable.Dialctlpeercfgentry, ['dialctlpeercfgid', 'ifindex', 'dialctlpeercfgiftype', 'dialctlpeercfglowerif', 'dialctlpeercfgoriginateaddress', 'dialctlpeercfgansweraddress', 'dialctlpeercfgsubaddress', 'dialctlpeercfgclosedusergroup', 'dialctlpeercfgspeed', 'dialctlpeercfginfotype', 'dialctlpeercfgpermission', 'dialctlpeercfginactivitytimer', 'dialctlpeercfgminduration', 'dialctlpeercfgmaxduration', 'dialctlpeercfgcarrierdelay', 'dialctlpeercfgcallretries', 'dialctlpeercfgretrydelay', 'dialctlpeercfgfailuredelay', 'dialctlpeercfgtrapenable', 'dialctlpeercfgstatus', 'dialctlpeerstatsconnecttime', 'dialctlpeerstatschargedunits', 'dialctlpeerstatssuccesscalls', 'dialctlpeerstatsfailcalls', 'dialctlpeerstatsacceptcalls', 'dialctlpeerstatsrefusecalls', 'dialctlpeerstatslastdisconnectcause', 'dialctlpeerstatslastdisconnecttext', 'dialctlpeerstatslastsetuptime'], name, value)

            class Dialctlpeercfginfotype(Enum):
                """
                Dialctlpeercfginfotype (Enum Class)

                The Information Transfer Capability to be used when

                calling this peer.

                speech(2) refers to a non\-data connection, whereas

                audio31(6) and audio7(7) refer to data mode

                connections.

                .. data:: other = 1

                .. data:: speech = 2

                .. data:: unrestrictedDigital = 3

                .. data:: unrestrictedDigital56 = 4

                .. data:: restrictedDigital = 5

                .. data:: audio31 = 6

                .. data:: audio7 = 7

                .. data:: video = 8

                .. data:: packetSwitched = 9

                .. data:: fax = 10

                """

                other = Enum.YLeaf(1, "other")

                speech = Enum.YLeaf(2, "speech")

                unrestrictedDigital = Enum.YLeaf(3, "unrestrictedDigital")

                unrestrictedDigital56 = Enum.YLeaf(4, "unrestrictedDigital56")

                restrictedDigital = Enum.YLeaf(5, "restrictedDigital")

                audio31 = Enum.YLeaf(6, "audio31")

                audio7 = Enum.YLeaf(7, "audio7")

                video = Enum.YLeaf(8, "video")

                packetSwitched = Enum.YLeaf(9, "packetSwitched")

                fax = Enum.YLeaf(10, "fax")


            class Dialctlpeercfgpermission(Enum):
                """
                Dialctlpeercfgpermission (Enum Class)

                Applicable permissions. callback(4) either rejects the

                call and then calls back, or uses the 'Reverse charging'

                information element if it is available.

                Note that callback(4) is supposed to control charging, not

                security, and applies to callback prior to accepting a

                call. Callback for security reasons can be handled using

                PPP callback.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: both = 3

                .. data:: callback = 4

                .. data:: none = 5

                """

                originate = Enum.YLeaf(1, "originate")

                answer = Enum.YLeaf(2, "answer")

                both = Enum.YLeaf(3, "both")

                callback = Enum.YLeaf(4, "callback")

                none = Enum.YLeaf(5, "none")


            class Dialctlpeercfgtrapenable(Enum):
                """
                Dialctlpeercfgtrapenable (Enum Class)

                This object indicates whether dialCtlPeerCallInformation

                and dialCtlPeerCallSetup traps should be generated for

                this peer.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")



    class Callactivetable(Entity):
        """
        A table containing information about active
        calls to a specific destination.
        
        .. attribute:: callactiveentry
        
        	The information regarding a single active Connection. An entry in this table will be created when a call is started. An entry in this table will be deleted when an active call clears
        	**type**\: list of  		 :py:class:`Callactiveentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DIALCONTROLMIB.Callactivetable, self).__init__()

            self.yang_name = "callActiveTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("callActiveEntry", ("callactiveentry", DIALCONTROLMIB.Callactivetable.Callactiveentry))])
            self._leafs = OrderedDict()

            self.callactiveentry = YList(self)
            self._segment_path = lambda: "callActiveTable"
            self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DIALCONTROLMIB.Callactivetable, [], name, value)


        class Callactiveentry(Entity):
            """
            The information regarding a single active Connection.
            An entry in this table will be created when a call is
            started. An entry in this table will be deleted when
            an active call clears.
            
            .. attribute:: callactivesetuptime  (key)
            
            	The value of sysUpTime when the call associated to this entry was started. This will be useful for an NMS to retrieve all calls after a specific time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveindex  (key)
            
            	Small index variable to distinguish calls that start in the same hundredth of a second
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivepeeraddress
            
            	The number this call is connected to. If the number is not available, then it will have a length of zero
            	**type**\: str
            
            .. attribute:: callactivepeersubaddress
            
            	The subaddress this call is connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\: str
            
            .. attribute:: callactivepeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivelogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call. If the ifIndex value is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactiveconnecttime
            
            	The value of sysUpTime when the call was connected. If the call is not connected, this object will have a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivecallstate
            
            	The current call state. unknown(1)     \- The call state is unknown. connecting(2)  \- A connection attempt (outgoing call)                  is being made. connected(3)   \- An incoming call is in the process                  of validation. active(4)      \- The call is active
            	**type**\:  :py:class:`Callactivecallstate <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry.Callactivecallstate>`
            
            .. attribute:: callactivecallorigin
            
            	The call origin
            	**type**\:  :py:class:`Callactivecallorigin <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry.Callactivecallorigin>`
            
            .. attribute:: callactivechargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveinfotype
            
            	The information type for this call
            	**type**\:  :py:class:`Callactiveinfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry.Callactiveinfotype>`
            
            .. attribute:: callactivetransmitpackets
            
            	The number of packets which were transmitted for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivetransmitbytes
            
            	The number of bytes which were transmitted for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivereceivepackets
            
            	The number of packets which were received for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivereceivebytes
            
            	The number of bytes which were received for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DIALCONTROLMIB.Callactivetable.Callactiveentry, self).__init__()

                self.yang_name = "callActiveEntry"
                self.yang_parent_name = "callActiveTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['callactivesetuptime','callactiveindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('callactivesetuptime', YLeaf(YType.uint32, 'callActiveSetupTime')),
                    ('callactiveindex', YLeaf(YType.int32, 'callActiveIndex')),
                    ('callactivepeeraddress', YLeaf(YType.str, 'callActivePeerAddress')),
                    ('callactivepeersubaddress', YLeaf(YType.str, 'callActivePeerSubAddress')),
                    ('callactivepeerid', YLeaf(YType.int32, 'callActivePeerId')),
                    ('callactivepeerifindex', YLeaf(YType.int32, 'callActivePeerIfIndex')),
                    ('callactivelogicalifindex', YLeaf(YType.int32, 'callActiveLogicalIfIndex')),
                    ('callactiveconnecttime', YLeaf(YType.uint32, 'callActiveConnectTime')),
                    ('callactivecallstate', YLeaf(YType.enumeration, 'callActiveCallState')),
                    ('callactivecallorigin', YLeaf(YType.enumeration, 'callActiveCallOrigin')),
                    ('callactivechargedunits', YLeaf(YType.uint32, 'callActiveChargedUnits')),
                    ('callactiveinfotype', YLeaf(YType.enumeration, 'callActiveInfoType')),
                    ('callactivetransmitpackets', YLeaf(YType.uint32, 'callActiveTransmitPackets')),
                    ('callactivetransmitbytes', YLeaf(YType.uint32, 'callActiveTransmitBytes')),
                    ('callactivereceivepackets', YLeaf(YType.uint32, 'callActiveReceivePackets')),
                    ('callactivereceivebytes', YLeaf(YType.uint32, 'callActiveReceiveBytes')),
                ])
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.callactivepeeraddress = None
                self.callactivepeersubaddress = None
                self.callactivepeerid = None
                self.callactivepeerifindex = None
                self.callactivelogicalifindex = None
                self.callactiveconnecttime = None
                self.callactivecallstate = None
                self.callactivecallorigin = None
                self.callactivechargedunits = None
                self.callactiveinfotype = None
                self.callactivetransmitpackets = None
                self.callactivetransmitbytes = None
                self.callactivereceivepackets = None
                self.callactivereceivebytes = None
                self._segment_path = lambda: "callActiveEntry" + "[callActiveSetupTime='" + str(self.callactivesetuptime) + "']" + "[callActiveIndex='" + str(self.callactiveindex) + "']"
                self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/callActiveTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DIALCONTROLMIB.Callactivetable.Callactiveentry, ['callactivesetuptime', 'callactiveindex', 'callactivepeeraddress', 'callactivepeersubaddress', 'callactivepeerid', 'callactivepeerifindex', 'callactivelogicalifindex', 'callactiveconnecttime', 'callactivecallstate', 'callactivecallorigin', 'callactivechargedunits', 'callactiveinfotype', 'callactivetransmitpackets', 'callactivetransmitbytes', 'callactivereceivepackets', 'callactivereceivebytes'], name, value)

            class Callactivecallorigin(Enum):
                """
                Callactivecallorigin (Enum Class)

                The call origin.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: callback = 3

                """

                originate = Enum.YLeaf(1, "originate")

                answer = Enum.YLeaf(2, "answer")

                callback = Enum.YLeaf(3, "callback")


            class Callactivecallstate(Enum):
                """
                Callactivecallstate (Enum Class)

                The current call state.

                unknown(1)     \- The call state is unknown.

                connecting(2)  \- A connection attempt (outgoing call)

                                 is being made.

                connected(3)   \- An incoming call is in the process

                                 of validation.

                active(4)      \- The call is active.

                .. data:: unknown = 1

                .. data:: connecting = 2

                .. data:: connected = 3

                .. data:: active = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                connecting = Enum.YLeaf(2, "connecting")

                connected = Enum.YLeaf(3, "connected")

                active = Enum.YLeaf(4, "active")


            class Callactiveinfotype(Enum):
                """
                Callactiveinfotype (Enum Class)

                The information type for this call.

                .. data:: other = 1

                .. data:: speech = 2

                .. data:: unrestrictedDigital = 3

                .. data:: unrestrictedDigital56 = 4

                .. data:: restrictedDigital = 5

                .. data:: audio31 = 6

                .. data:: audio7 = 7

                .. data:: video = 8

                .. data:: packetSwitched = 9

                .. data:: fax = 10

                """

                other = Enum.YLeaf(1, "other")

                speech = Enum.YLeaf(2, "speech")

                unrestrictedDigital = Enum.YLeaf(3, "unrestrictedDigital")

                unrestrictedDigital56 = Enum.YLeaf(4, "unrestrictedDigital56")

                restrictedDigital = Enum.YLeaf(5, "restrictedDigital")

                audio31 = Enum.YLeaf(6, "audio31")

                audio7 = Enum.YLeaf(7, "audio7")

                video = Enum.YLeaf(8, "video")

                packetSwitched = Enum.YLeaf(9, "packetSwitched")

                fax = Enum.YLeaf(10, "fax")



    class Callhistorytable(Entity):
        """
        A table containing information about specific
        calls to a specific destination.
        
        .. attribute:: callhistoryentry
        
        	The information regarding a single Connection
        	**type**\: list of  		 :py:class:`Callhistoryentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callhistorytable.Callhistoryentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DIALCONTROLMIB.Callhistorytable, self).__init__()

            self.yang_name = "callHistoryTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("callHistoryEntry", ("callhistoryentry", DIALCONTROLMIB.Callhistorytable.Callhistoryentry))])
            self._leafs = OrderedDict()

            self.callhistoryentry = YList(self)
            self._segment_path = lambda: "callHistoryTable"
            self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DIALCONTROLMIB.Callhistorytable, [], name, value)


        class Callhistoryentry(Entity):
            """
            The information regarding a single Connection.
            
            .. attribute:: callactivesetuptime  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: callhistorypeeraddress
            
            	The number this call was connected to. If the number is not available, then it will have a length of zero
            	**type**\: str
            
            .. attribute:: callhistorypeersubaddress
            
            	The subaddress this call was connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\: str
            
            .. attribute:: callhistorypeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorypeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorylogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callhistorydisconnectcause
            
            	The encoded network cause value associated with this call.  The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\: str
            
            	**length:** 0..4
            
            .. attribute:: callhistorydisconnecttext
            
            	ASCII text describing the reason for call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause
            	**type**\: str
            
            .. attribute:: callhistoryconnecttime
            
            	The value of sysUpTime when the call was connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorydisconnecttime
            
            	The value of sysUpTime when the call was disconnected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorycallorigin
            
            	The call origin
            	**type**\:  :py:class:`Callhistorycallorigin <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callhistorytable.Callhistoryentry.Callhistorycallorigin>`
            
            .. attribute:: callhistorychargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryinfotype
            
            	The information type for this call
            	**type**\:  :py:class:`Callhistoryinfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callhistorytable.Callhistoryentry.Callhistoryinfotype>`
            
            .. attribute:: callhistorytransmitpackets
            
            	The number of packets which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorytransmitbytes
            
            	The number of bytes which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryreceivepackets
            
            	The number of packets which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryreceivebytes
            
            	The number of bytes which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DIALCONTROLMIB.Callhistorytable.Callhistoryentry, self).__init__()

                self.yang_name = "callHistoryEntry"
                self.yang_parent_name = "callHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['callactivesetuptime','callactiveindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('callactivesetuptime', YLeaf(YType.str, 'callActiveSetupTime')),
                    ('callactiveindex', YLeaf(YType.str, 'callActiveIndex')),
                    ('callhistorypeeraddress', YLeaf(YType.str, 'callHistoryPeerAddress')),
                    ('callhistorypeersubaddress', YLeaf(YType.str, 'callHistoryPeerSubAddress')),
                    ('callhistorypeerid', YLeaf(YType.int32, 'callHistoryPeerId')),
                    ('callhistorypeerifindex', YLeaf(YType.int32, 'callHistoryPeerIfIndex')),
                    ('callhistorylogicalifindex', YLeaf(YType.int32, 'callHistoryLogicalIfIndex')),
                    ('callhistorydisconnectcause', YLeaf(YType.str, 'callHistoryDisconnectCause')),
                    ('callhistorydisconnecttext', YLeaf(YType.str, 'callHistoryDisconnectText')),
                    ('callhistoryconnecttime', YLeaf(YType.uint32, 'callHistoryConnectTime')),
                    ('callhistorydisconnecttime', YLeaf(YType.uint32, 'callHistoryDisconnectTime')),
                    ('callhistorycallorigin', YLeaf(YType.enumeration, 'callHistoryCallOrigin')),
                    ('callhistorychargedunits', YLeaf(YType.uint32, 'callHistoryChargedUnits')),
                    ('callhistoryinfotype', YLeaf(YType.enumeration, 'callHistoryInfoType')),
                    ('callhistorytransmitpackets', YLeaf(YType.uint32, 'callHistoryTransmitPackets')),
                    ('callhistorytransmitbytes', YLeaf(YType.uint32, 'callHistoryTransmitBytes')),
                    ('callhistoryreceivepackets', YLeaf(YType.uint32, 'callHistoryReceivePackets')),
                    ('callhistoryreceivebytes', YLeaf(YType.uint32, 'callHistoryReceiveBytes')),
                ])
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.callhistorypeeraddress = None
                self.callhistorypeersubaddress = None
                self.callhistorypeerid = None
                self.callhistorypeerifindex = None
                self.callhistorylogicalifindex = None
                self.callhistorydisconnectcause = None
                self.callhistorydisconnecttext = None
                self.callhistoryconnecttime = None
                self.callhistorydisconnecttime = None
                self.callhistorycallorigin = None
                self.callhistorychargedunits = None
                self.callhistoryinfotype = None
                self.callhistorytransmitpackets = None
                self.callhistorytransmitbytes = None
                self.callhistoryreceivepackets = None
                self.callhistoryreceivebytes = None
                self._segment_path = lambda: "callHistoryEntry" + "[callActiveSetupTime='" + str(self.callactivesetuptime) + "']" + "[callActiveIndex='" + str(self.callactiveindex) + "']"
                self._absolute_path = lambda: "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/callHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DIALCONTROLMIB.Callhistorytable.Callhistoryentry, ['callactivesetuptime', 'callactiveindex', 'callhistorypeeraddress', 'callhistorypeersubaddress', 'callhistorypeerid', 'callhistorypeerifindex', 'callhistorylogicalifindex', 'callhistorydisconnectcause', 'callhistorydisconnecttext', 'callhistoryconnecttime', 'callhistorydisconnecttime', 'callhistorycallorigin', 'callhistorychargedunits', 'callhistoryinfotype', 'callhistorytransmitpackets', 'callhistorytransmitbytes', 'callhistoryreceivepackets', 'callhistoryreceivebytes'], name, value)

            class Callhistorycallorigin(Enum):
                """
                Callhistorycallorigin (Enum Class)

                The call origin.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: callback = 3

                """

                originate = Enum.YLeaf(1, "originate")

                answer = Enum.YLeaf(2, "answer")

                callback = Enum.YLeaf(3, "callback")


            class Callhistoryinfotype(Enum):
                """
                Callhistoryinfotype (Enum Class)

                The information type for this call.

                .. data:: other = 1

                .. data:: speech = 2

                .. data:: unrestrictedDigital = 3

                .. data:: unrestrictedDigital56 = 4

                .. data:: restrictedDigital = 5

                .. data:: audio31 = 6

                .. data:: audio7 = 7

                .. data:: video = 8

                .. data:: packetSwitched = 9

                .. data:: fax = 10

                """

                other = Enum.YLeaf(1, "other")

                speech = Enum.YLeaf(2, "speech")

                unrestrictedDigital = Enum.YLeaf(3, "unrestrictedDigital")

                unrestrictedDigital56 = Enum.YLeaf(4, "unrestrictedDigital56")

                restrictedDigital = Enum.YLeaf(5, "restrictedDigital")

                audio31 = Enum.YLeaf(6, "audio31")

                audio7 = Enum.YLeaf(7, "audio7")

                video = Enum.YLeaf(8, "video")

                packetSwitched = Enum.YLeaf(9, "packetSwitched")

                fax = Enum.YLeaf(10, "fax")


    def clone_ptr(self):
        self._top_entity = DIALCONTROLMIB()
        return self._top_entity

