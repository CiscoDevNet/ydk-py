""" DIAL_CONTROL_MIB 

The MIB module to describe peer information for
demand access and possibly other kinds of interfaces.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DialControlMib(Entity):
    """
    
    
    .. attribute:: callactivetable
    
    	A table containing information about active calls to a specific destination
    	**type**\:   :py:class:`Callactivetable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable>`
    
    .. attribute:: callhistory
    
    	
    	**type**\:   :py:class:`Callhistory <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistory>`
    
    .. attribute:: callhistorytable
    
    	A table containing information about specific calls to a specific destination
    	**type**\:   :py:class:`Callhistorytable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable>`
    
    .. attribute:: dialctlconfiguration
    
    	
    	**type**\:   :py:class:`Dialctlconfiguration <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlconfiguration>`
    
    .. attribute:: dialctlpeercfgtable
    
    	The list of peers from which the managed device will accept calls or to which it will place them
    	**type**\:   :py:class:`Dialctlpeercfgtable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable>`
    
    

    """

    _prefix = 'DIAL-CONTROL-MIB'
    _revision = '1996-09-23'

    def __init__(self):
        super(DialControlMib, self).__init__()
        self._top_entity = None

        self.yang_name = "DIAL-CONTROL-MIB"
        self.yang_parent_name = "DIAL-CONTROL-MIB"

        self.callactivetable = DialControlMib.Callactivetable()
        self.callactivetable.parent = self
        self._children_name_map["callactivetable"] = "callActiveTable"
        self._children_yang_names.add("callActiveTable")

        self.callhistory = DialControlMib.Callhistory()
        self.callhistory.parent = self
        self._children_name_map["callhistory"] = "callHistory"
        self._children_yang_names.add("callHistory")

        self.callhistorytable = DialControlMib.Callhistorytable()
        self.callhistorytable.parent = self
        self._children_name_map["callhistorytable"] = "callHistoryTable"
        self._children_yang_names.add("callHistoryTable")

        self.dialctlconfiguration = DialControlMib.Dialctlconfiguration()
        self.dialctlconfiguration.parent = self
        self._children_name_map["dialctlconfiguration"] = "dialCtlConfiguration"
        self._children_yang_names.add("dialCtlConfiguration")

        self.dialctlpeercfgtable = DialControlMib.Dialctlpeercfgtable()
        self.dialctlpeercfgtable.parent = self
        self._children_name_map["dialctlpeercfgtable"] = "dialCtlPeerCfgTable"
        self._children_yang_names.add("dialCtlPeerCfgTable")


    class Dialctlconfiguration(Entity):
        """
        
        
        .. attribute:: dialctlacceptmode
        
        	The security level for acceptance of incoming calls. acceptNone(1)  \- incoming calls will not be accepted acceptAll(2)   \- incoming calls will be accepted,                  even if there is no matching entry                  in the dialCtlPeerCfgTable acceptKnown(3) \- incoming calls will be accepted only                  if there is a matching entry in the                  dialCtlPeerCfgTable
        	**type**\:   :py:class:`Dialctlacceptmode <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlconfiguration.Dialctlacceptmode>`
        
        .. attribute:: dialctltrapenable
        
        	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for all peers. If the value of this object is enabled(1), traps will be generated for all peers. If the value of this object is disabled(2), traps will be generated only for peers having dialCtlPeerCfgTrapEnable set to enabled(1)
        	**type**\:   :py:class:`Dialctltrapenable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlconfiguration.Dialctltrapenable>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DialControlMib.Dialctlconfiguration, self).__init__()

            self.yang_name = "dialCtlConfiguration"
            self.yang_parent_name = "DIAL-CONTROL-MIB"

            self.dialctlacceptmode = YLeaf(YType.enumeration, "dialCtlAcceptMode")

            self.dialctltrapenable = YLeaf(YType.enumeration, "dialCtlTrapEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dialctlacceptmode",
                            "dialctltrapenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DialControlMib.Dialctlconfiguration, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DialControlMib.Dialctlconfiguration, self).__setattr__(name, value)

        class Dialctlacceptmode(Enum):
            """
            Dialctlacceptmode

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
            Dialctltrapenable

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


        def has_data(self):
            return (
                self.dialctlacceptmode.is_set or
                self.dialctltrapenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dialctlacceptmode.yfilter != YFilter.not_set or
                self.dialctltrapenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dialCtlConfiguration" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dialctlacceptmode.is_set or self.dialctlacceptmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dialctlacceptmode.get_name_leafdata())
            if (self.dialctltrapenable.is_set or self.dialctltrapenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dialctltrapenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dialCtlAcceptMode" or name == "dialCtlTrapEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dialCtlAcceptMode"):
                self.dialctlacceptmode = value
                self.dialctlacceptmode.value_namespace = name_space
                self.dialctlacceptmode.value_namespace_prefix = name_space_prefix
            if(value_path == "dialCtlTrapEnable"):
                self.dialctltrapenable = value
                self.dialctltrapenable.value_namespace = name_space
                self.dialctltrapenable.value_namespace_prefix = name_space_prefix


    class Callhistory(Entity):
        """
        
        
        .. attribute:: callhistoryretaintimer
        
        	The minimum amount of time that an callHistoryEntry will be maintained before being deleted. A value of 0 will prevent any history from being retained in the callHistoryTable, but will neither prevent callCompletion traps being generated nor affect other tables
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: minutes
        
        .. attribute:: callhistorytablemaxlength
        
        	The upper limit on the number of entries that the callHistoryTable may contain.  A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and the new one will be created
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DialControlMib.Callhistory, self).__init__()

            self.yang_name = "callHistory"
            self.yang_parent_name = "DIAL-CONTROL-MIB"

            self.callhistoryretaintimer = YLeaf(YType.int32, "callHistoryRetainTimer")

            self.callhistorytablemaxlength = YLeaf(YType.int32, "callHistoryTableMaxLength")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("callhistoryretaintimer",
                            "callhistorytablemaxlength") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DialControlMib.Callhistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DialControlMib.Callhistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.callhistoryretaintimer.is_set or
                self.callhistorytablemaxlength.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.callhistoryretaintimer.yfilter != YFilter.not_set or
                self.callhistorytablemaxlength.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "callHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.callhistoryretaintimer.is_set or self.callhistoryretaintimer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.callhistoryretaintimer.get_name_leafdata())
            if (self.callhistorytablemaxlength.is_set or self.callhistorytablemaxlength.yfilter != YFilter.not_set):
                leaf_name_data.append(self.callhistorytablemaxlength.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "callHistoryRetainTimer" or name == "callHistoryTableMaxLength"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "callHistoryRetainTimer"):
                self.callhistoryretaintimer = value
                self.callhistoryretaintimer.value_namespace = name_space
                self.callhistoryretaintimer.value_namespace_prefix = name_space_prefix
            if(value_path == "callHistoryTableMaxLength"):
                self.callhistorytablemaxlength = value
                self.callhistorytablemaxlength.value_namespace = name_space
                self.callhistorytablemaxlength.value_namespace_prefix = name_space_prefix


    class Dialctlpeercfgtable(Entity):
        """
        The list of peers from which the managed device
        will accept calls or to which it will place them.
        
        .. attribute:: dialctlpeercfgentry
        
        	Configuration data for a single Peer. This entry is effectively permanent, and contains information to identify the peer, how to connect to the peer, how to identify the peer and its permissions. The value of dialCtlPeerCfgOriginateAddress must be specified before a new row in this table can become active(1). Any writeable parameters in an existing entry can be modified while the entry is active. The modification will take effect when the peer in question will be called the next time. An entry in this table can only be created if the associated ifEntry already exists
        	**type**\: list of    :py:class:`Dialctlpeercfgentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DialControlMib.Dialctlpeercfgtable, self).__init__()

            self.yang_name = "dialCtlPeerCfgTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"

            self.dialctlpeercfgentry = YList(self)

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
                        super(DialControlMib.Dialctlpeercfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DialControlMib.Dialctlpeercfgtable, self).__setattr__(name, value)


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
            
            .. attribute:: dialctlpeercfgid  <key>
            
            	This object identifies a single peer. There may be several entries in this table for one peer, defining different ways of reaching this peer. Thus, there may be several entries in this table with the same value of dialCtlPeerCfgId. Multiple entries for one peer may be used to support multilink as well as backup lines. A single peer will be identified by a unique value of this object. Several entries for one peer MUST have the same value of dialCtlPeerCfgId, but different ifEntries and thus different values of ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: dialctlpeercfgansweraddress
            
            	Calling Party Number information element, as for example passed in an ISDN SETUP message by a PBX or switch, for incoming calls. This address can be used to identify the peer. If this address is either unknown or identical to dialCtlPeerCfgOriginateAddress, this object will be a zero length string
            	**type**\:  str
            
            .. attribute:: dialctlpeercfgcallretries
            
            	The number of calls to a non\-responding address that may be made. A retry count of zero means there is no bound. The intent is to bound the number of successive calls to an address which is inaccessible, or which refuses those calls.  Some countries regulate the number of call retries to a given peer that can be made
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgcarrierdelay
            
            	The call timeout time in seconds. The default value of zero means that the call timeout as specified for the media in question will apply
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgclosedusergroup
            
            	Closed User Group at which the peer will be called. If the Closed User Group is undefined for the given media or unused, this is a zero length string
            	**type**\:  str
            
            .. attribute:: dialctlpeercfgfailuredelay
            
            	The time in seconds after which call attempts are to be placed again after a peer has been noticed to be unreachable, i.e. after dialCtlPeerCfgCallRetries unsuccessful call attempts. A value of zero means that a peer will not be called again after dialCtlPeerCfgCallRetries unsuccessful call attempts
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgiftype
            
            	The interface type to be used for calling this peer. In case of ISDN, the value of isdn(63) is to be used
            	**type**\:   :py:class:`Ianaiftype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianaiftype>`
            
            .. attribute:: dialctlpeercfginactivitytimer
            
            	The connection will be automatically disconnected if no longer carrying useful data for a time period, in seconds, specified in this object. Useful data in this context refers to forwarding packets, including routing information; it excludes the encapsulator maintenance frames. A value of zero means the connection will not be automatically taken down due to inactivity, which implies that it is a dedicated circuit
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfginfotype
            
            	The Information Transfer Capability to be used when calling this peer.  speech(2) refers to a non\-data connection, whereas audio31(6) and audio7(7) refer to data mode connections
            	**type**\:   :py:class:`Dialctlpeercfginfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfginfotype>`
            
            .. attribute:: dialctlpeercfglowerif
            
            	ifIndex value of an interface the peer will have to be called on. For example, on an ISDN interface, this can be the ifIndex value of a D channel or the ifIndex value of a B channel, whatever is appropriate for a given peer. As an example, for Basic Rate leased lines it will be necessary to specify a B channel ifIndex, while for     semi\-permanent connections the D channel ifIndex has to be specified. If the interface can be dynamically assigned, this object has a value of zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgmaxduration
            
            	Maximum call duration in seconds. Zero means 'unlimited'
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgminduration
            
            	Minimum duration of a call in seconds, starting from the time the call is connected until the call is disconnected. This is to accomplish the fact that in most countries charging applies to units of time, which should be matched as closely as possible
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgoriginateaddress
            
            	Call Address at which the peer will be called. Think of this as the set of characters following 'ATDT ' or the 'phone number' included in a D channel call request.  The structure of this information will be switch type specific. If there is no address information required for reaching the peer, i.e., for leased lines, this object will be a zero length string
            	**type**\:  str
            
            .. attribute:: dialctlpeercfgpermission
            
            	Applicable permissions. callback(4) either rejects the call and then calls back, or uses the 'Reverse charging' information element if it is available. Note that callback(4) is supposed to control charging, not security, and applies to callback prior to accepting a call. Callback for security reasons can be handled using PPP callback
            	**type**\:   :py:class:`Dialctlpeercfgpermission <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfgpermission>`
            
            .. attribute:: dialctlpeercfgretrydelay
            
            	The time in seconds between call retries if a peer cannot be reached. A value of zero means that call retries may be done without any delay
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfgspeed
            
            	The desired information transfer speed in bits/second when calling this peer. The detailed media specific information, e.g. information type and information transfer rate for ISDN circuits, has to be extracted from this object. If the transfer speed to be used is unknown or the default speed for this type of interfaces, the value of this object may be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgstatus
            
            	Status of one row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: dialctlpeercfgsubaddress
            
            	Subaddress at which the peer will be called. If the subaddress is undefined for the given media or unused, this is a zero length string
            	**type**\:  str
            
            .. attribute:: dialctlpeercfgtrapenable
            
            	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for this peer
            	**type**\:   :py:class:`Dialctlpeercfgtrapenable <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.Dialctlpeercfgtrapenable>`
            
            .. attribute:: dialctlpeerstatsacceptcalls
            
            	Number of calls from this peer accepted since system startup
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatschargedunits
            
            	The total number of charging units applying to this peer since system startup. Only the charging units applying to the local interface, i.e. for originated calls or for calls with 'Reverse charging' being active, will be counted here
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsconnecttime
            
            	Accumulated connect time to the peer since system startup. This is the total connect time, i.e. the connect time for outgoing calls plus the time for incoming calls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeerstatsfailcalls
            
            	Number of failed call attempts to this peer since system startup
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatslastdisconnectcause
            
            	The encoded network cause value associated with the last call. This object will be updated whenever a call is started or cleared. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\:  str
            
            	**length:** 0..4
            
            .. attribute:: dialctlpeerstatslastdisconnecttext
            
            	ASCII text describing the reason for the last call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause.  This object will be updated whenever a call is started or cleared
            	**type**\:  str
            
            .. attribute:: dialctlpeerstatslastsetuptime
            
            	The value of sysUpTime when the last call to this peer was started. For ISDN media, this will be the time when the setup message was received from or sent to the network. This object will be updated whenever a call is started or cleared
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsrefusecalls
            
            	Number of calls from this peer refused since system startup
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatssuccesscalls
            
            	Number of completed calls to this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry, self).__init__()

                self.yang_name = "dialCtlPeerCfgEntry"
                self.yang_parent_name = "dialCtlPeerCfgTable"

                self.dialctlpeercfgid = YLeaf(YType.int32, "dialCtlPeerCfgId")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.dialctlpeercfgansweraddress = YLeaf(YType.str, "dialCtlPeerCfgAnswerAddress")

                self.dialctlpeercfgcallretries = YLeaf(YType.int32, "dialCtlPeerCfgCallRetries")

                self.dialctlpeercfgcarrierdelay = YLeaf(YType.int32, "dialCtlPeerCfgCarrierDelay")

                self.dialctlpeercfgclosedusergroup = YLeaf(YType.str, "dialCtlPeerCfgClosedUserGroup")

                self.dialctlpeercfgfailuredelay = YLeaf(YType.int32, "dialCtlPeerCfgFailureDelay")

                self.dialctlpeercfgiftype = YLeaf(YType.enumeration, "dialCtlPeerCfgIfType")

                self.dialctlpeercfginactivitytimer = YLeaf(YType.int32, "dialCtlPeerCfgInactivityTimer")

                self.dialctlpeercfginfotype = YLeaf(YType.enumeration, "dialCtlPeerCfgInfoType")

                self.dialctlpeercfglowerif = YLeaf(YType.int32, "dialCtlPeerCfgLowerIf")

                self.dialctlpeercfgmaxduration = YLeaf(YType.int32, "dialCtlPeerCfgMaxDuration")

                self.dialctlpeercfgminduration = YLeaf(YType.int32, "dialCtlPeerCfgMinDuration")

                self.dialctlpeercfgoriginateaddress = YLeaf(YType.str, "dialCtlPeerCfgOriginateAddress")

                self.dialctlpeercfgpermission = YLeaf(YType.enumeration, "dialCtlPeerCfgPermission")

                self.dialctlpeercfgretrydelay = YLeaf(YType.int32, "dialCtlPeerCfgRetryDelay")

                self.dialctlpeercfgspeed = YLeaf(YType.int32, "dialCtlPeerCfgSpeed")

                self.dialctlpeercfgstatus = YLeaf(YType.enumeration, "dialCtlPeerCfgStatus")

                self.dialctlpeercfgsubaddress = YLeaf(YType.str, "dialCtlPeerCfgSubAddress")

                self.dialctlpeercfgtrapenable = YLeaf(YType.enumeration, "dialCtlPeerCfgTrapEnable")

                self.dialctlpeerstatsacceptcalls = YLeaf(YType.uint32, "dialCtlPeerStatsAcceptCalls")

                self.dialctlpeerstatschargedunits = YLeaf(YType.uint32, "dialCtlPeerStatsChargedUnits")

                self.dialctlpeerstatsconnecttime = YLeaf(YType.uint32, "dialCtlPeerStatsConnectTime")

                self.dialctlpeerstatsfailcalls = YLeaf(YType.uint32, "dialCtlPeerStatsFailCalls")

                self.dialctlpeerstatslastdisconnectcause = YLeaf(YType.str, "dialCtlPeerStatsLastDisconnectCause")

                self.dialctlpeerstatslastdisconnecttext = YLeaf(YType.str, "dialCtlPeerStatsLastDisconnectText")

                self.dialctlpeerstatslastsetuptime = YLeaf(YType.uint32, "dialCtlPeerStatsLastSetupTime")

                self.dialctlpeerstatsrefusecalls = YLeaf(YType.uint32, "dialCtlPeerStatsRefuseCalls")

                self.dialctlpeerstatssuccesscalls = YLeaf(YType.uint32, "dialCtlPeerStatsSuccessCalls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dialctlpeercfgid",
                                "ifindex",
                                "dialctlpeercfgansweraddress",
                                "dialctlpeercfgcallretries",
                                "dialctlpeercfgcarrierdelay",
                                "dialctlpeercfgclosedusergroup",
                                "dialctlpeercfgfailuredelay",
                                "dialctlpeercfgiftype",
                                "dialctlpeercfginactivitytimer",
                                "dialctlpeercfginfotype",
                                "dialctlpeercfglowerif",
                                "dialctlpeercfgmaxduration",
                                "dialctlpeercfgminduration",
                                "dialctlpeercfgoriginateaddress",
                                "dialctlpeercfgpermission",
                                "dialctlpeercfgretrydelay",
                                "dialctlpeercfgspeed",
                                "dialctlpeercfgstatus",
                                "dialctlpeercfgsubaddress",
                                "dialctlpeercfgtrapenable",
                                "dialctlpeerstatsacceptcalls",
                                "dialctlpeerstatschargedunits",
                                "dialctlpeerstatsconnecttime",
                                "dialctlpeerstatsfailcalls",
                                "dialctlpeerstatslastdisconnectcause",
                                "dialctlpeerstatslastdisconnecttext",
                                "dialctlpeerstatslastsetuptime",
                                "dialctlpeerstatsrefusecalls",
                                "dialctlpeerstatssuccesscalls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry, self).__setattr__(name, value)

            class Dialctlpeercfginfotype(Enum):
                """
                Dialctlpeercfginfotype

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
                Dialctlpeercfgpermission

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
                Dialctlpeercfgtrapenable

                This object indicates whether dialCtlPeerCallInformation

                and dialCtlPeerCallSetup traps should be generated for

                this peer.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            def has_data(self):
                return (
                    self.dialctlpeercfgid.is_set or
                    self.ifindex.is_set or
                    self.dialctlpeercfgansweraddress.is_set or
                    self.dialctlpeercfgcallretries.is_set or
                    self.dialctlpeercfgcarrierdelay.is_set or
                    self.dialctlpeercfgclosedusergroup.is_set or
                    self.dialctlpeercfgfailuredelay.is_set or
                    self.dialctlpeercfgiftype.is_set or
                    self.dialctlpeercfginactivitytimer.is_set or
                    self.dialctlpeercfginfotype.is_set or
                    self.dialctlpeercfglowerif.is_set or
                    self.dialctlpeercfgmaxduration.is_set or
                    self.dialctlpeercfgminduration.is_set or
                    self.dialctlpeercfgoriginateaddress.is_set or
                    self.dialctlpeercfgpermission.is_set or
                    self.dialctlpeercfgretrydelay.is_set or
                    self.dialctlpeercfgspeed.is_set or
                    self.dialctlpeercfgstatus.is_set or
                    self.dialctlpeercfgsubaddress.is_set or
                    self.dialctlpeercfgtrapenable.is_set or
                    self.dialctlpeerstatsacceptcalls.is_set or
                    self.dialctlpeerstatschargedunits.is_set or
                    self.dialctlpeerstatsconnecttime.is_set or
                    self.dialctlpeerstatsfailcalls.is_set or
                    self.dialctlpeerstatslastdisconnectcause.is_set or
                    self.dialctlpeerstatslastdisconnecttext.is_set or
                    self.dialctlpeerstatslastsetuptime.is_set or
                    self.dialctlpeerstatsrefusecalls.is_set or
                    self.dialctlpeerstatssuccesscalls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dialctlpeercfgid.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.dialctlpeercfgansweraddress.yfilter != YFilter.not_set or
                    self.dialctlpeercfgcallretries.yfilter != YFilter.not_set or
                    self.dialctlpeercfgcarrierdelay.yfilter != YFilter.not_set or
                    self.dialctlpeercfgclosedusergroup.yfilter != YFilter.not_set or
                    self.dialctlpeercfgfailuredelay.yfilter != YFilter.not_set or
                    self.dialctlpeercfgiftype.yfilter != YFilter.not_set or
                    self.dialctlpeercfginactivitytimer.yfilter != YFilter.not_set or
                    self.dialctlpeercfginfotype.yfilter != YFilter.not_set or
                    self.dialctlpeercfglowerif.yfilter != YFilter.not_set or
                    self.dialctlpeercfgmaxduration.yfilter != YFilter.not_set or
                    self.dialctlpeercfgminduration.yfilter != YFilter.not_set or
                    self.dialctlpeercfgoriginateaddress.yfilter != YFilter.not_set or
                    self.dialctlpeercfgpermission.yfilter != YFilter.not_set or
                    self.dialctlpeercfgretrydelay.yfilter != YFilter.not_set or
                    self.dialctlpeercfgspeed.yfilter != YFilter.not_set or
                    self.dialctlpeercfgstatus.yfilter != YFilter.not_set or
                    self.dialctlpeercfgsubaddress.yfilter != YFilter.not_set or
                    self.dialctlpeercfgtrapenable.yfilter != YFilter.not_set or
                    self.dialctlpeerstatsacceptcalls.yfilter != YFilter.not_set or
                    self.dialctlpeerstatschargedunits.yfilter != YFilter.not_set or
                    self.dialctlpeerstatsconnecttime.yfilter != YFilter.not_set or
                    self.dialctlpeerstatsfailcalls.yfilter != YFilter.not_set or
                    self.dialctlpeerstatslastdisconnectcause.yfilter != YFilter.not_set or
                    self.dialctlpeerstatslastdisconnecttext.yfilter != YFilter.not_set or
                    self.dialctlpeerstatslastsetuptime.yfilter != YFilter.not_set or
                    self.dialctlpeerstatsrefusecalls.yfilter != YFilter.not_set or
                    self.dialctlpeerstatssuccesscalls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dialCtlPeerCfgEntry" + "[dialCtlPeerCfgId='" + self.dialctlpeercfgid.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/dialCtlPeerCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dialctlpeercfgid.is_set or self.dialctlpeercfgid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgid.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.dialctlpeercfgansweraddress.is_set or self.dialctlpeercfgansweraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgansweraddress.get_name_leafdata())
                if (self.dialctlpeercfgcallretries.is_set or self.dialctlpeercfgcallretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgcallretries.get_name_leafdata())
                if (self.dialctlpeercfgcarrierdelay.is_set or self.dialctlpeercfgcarrierdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgcarrierdelay.get_name_leafdata())
                if (self.dialctlpeercfgclosedusergroup.is_set or self.dialctlpeercfgclosedusergroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgclosedusergroup.get_name_leafdata())
                if (self.dialctlpeercfgfailuredelay.is_set or self.dialctlpeercfgfailuredelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgfailuredelay.get_name_leafdata())
                if (self.dialctlpeercfgiftype.is_set or self.dialctlpeercfgiftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgiftype.get_name_leafdata())
                if (self.dialctlpeercfginactivitytimer.is_set or self.dialctlpeercfginactivitytimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfginactivitytimer.get_name_leafdata())
                if (self.dialctlpeercfginfotype.is_set or self.dialctlpeercfginfotype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfginfotype.get_name_leafdata())
                if (self.dialctlpeercfglowerif.is_set or self.dialctlpeercfglowerif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfglowerif.get_name_leafdata())
                if (self.dialctlpeercfgmaxduration.is_set or self.dialctlpeercfgmaxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgmaxduration.get_name_leafdata())
                if (self.dialctlpeercfgminduration.is_set or self.dialctlpeercfgminduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgminduration.get_name_leafdata())
                if (self.dialctlpeercfgoriginateaddress.is_set or self.dialctlpeercfgoriginateaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgoriginateaddress.get_name_leafdata())
                if (self.dialctlpeercfgpermission.is_set or self.dialctlpeercfgpermission.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgpermission.get_name_leafdata())
                if (self.dialctlpeercfgretrydelay.is_set or self.dialctlpeercfgretrydelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgretrydelay.get_name_leafdata())
                if (self.dialctlpeercfgspeed.is_set or self.dialctlpeercfgspeed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgspeed.get_name_leafdata())
                if (self.dialctlpeercfgstatus.is_set or self.dialctlpeercfgstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgstatus.get_name_leafdata())
                if (self.dialctlpeercfgsubaddress.is_set or self.dialctlpeercfgsubaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgsubaddress.get_name_leafdata())
                if (self.dialctlpeercfgtrapenable.is_set or self.dialctlpeercfgtrapenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeercfgtrapenable.get_name_leafdata())
                if (self.dialctlpeerstatsacceptcalls.is_set or self.dialctlpeerstatsacceptcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatsacceptcalls.get_name_leafdata())
                if (self.dialctlpeerstatschargedunits.is_set or self.dialctlpeerstatschargedunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatschargedunits.get_name_leafdata())
                if (self.dialctlpeerstatsconnecttime.is_set or self.dialctlpeerstatsconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatsconnecttime.get_name_leafdata())
                if (self.dialctlpeerstatsfailcalls.is_set or self.dialctlpeerstatsfailcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatsfailcalls.get_name_leafdata())
                if (self.dialctlpeerstatslastdisconnectcause.is_set or self.dialctlpeerstatslastdisconnectcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatslastdisconnectcause.get_name_leafdata())
                if (self.dialctlpeerstatslastdisconnecttext.is_set or self.dialctlpeerstatslastdisconnecttext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatslastdisconnecttext.get_name_leafdata())
                if (self.dialctlpeerstatslastsetuptime.is_set or self.dialctlpeerstatslastsetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatslastsetuptime.get_name_leafdata())
                if (self.dialctlpeerstatsrefusecalls.is_set or self.dialctlpeerstatsrefusecalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatsrefusecalls.get_name_leafdata())
                if (self.dialctlpeerstatssuccesscalls.is_set or self.dialctlpeerstatssuccesscalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dialctlpeerstatssuccesscalls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dialCtlPeerCfgId" or name == "ifIndex" or name == "dialCtlPeerCfgAnswerAddress" or name == "dialCtlPeerCfgCallRetries" or name == "dialCtlPeerCfgCarrierDelay" or name == "dialCtlPeerCfgClosedUserGroup" or name == "dialCtlPeerCfgFailureDelay" or name == "dialCtlPeerCfgIfType" or name == "dialCtlPeerCfgInactivityTimer" or name == "dialCtlPeerCfgInfoType" or name == "dialCtlPeerCfgLowerIf" or name == "dialCtlPeerCfgMaxDuration" or name == "dialCtlPeerCfgMinDuration" or name == "dialCtlPeerCfgOriginateAddress" or name == "dialCtlPeerCfgPermission" or name == "dialCtlPeerCfgRetryDelay" or name == "dialCtlPeerCfgSpeed" or name == "dialCtlPeerCfgStatus" or name == "dialCtlPeerCfgSubAddress" or name == "dialCtlPeerCfgTrapEnable" or name == "dialCtlPeerStatsAcceptCalls" or name == "dialCtlPeerStatsChargedUnits" or name == "dialCtlPeerStatsConnectTime" or name == "dialCtlPeerStatsFailCalls" or name == "dialCtlPeerStatsLastDisconnectCause" or name == "dialCtlPeerStatsLastDisconnectText" or name == "dialCtlPeerStatsLastSetupTime" or name == "dialCtlPeerStatsRefuseCalls" or name == "dialCtlPeerStatsSuccessCalls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dialCtlPeerCfgId"):
                    self.dialctlpeercfgid = value
                    self.dialctlpeercfgid.value_namespace = name_space
                    self.dialctlpeercfgid.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgAnswerAddress"):
                    self.dialctlpeercfgansweraddress = value
                    self.dialctlpeercfgansweraddress.value_namespace = name_space
                    self.dialctlpeercfgansweraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgCallRetries"):
                    self.dialctlpeercfgcallretries = value
                    self.dialctlpeercfgcallretries.value_namespace = name_space
                    self.dialctlpeercfgcallretries.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgCarrierDelay"):
                    self.dialctlpeercfgcarrierdelay = value
                    self.dialctlpeercfgcarrierdelay.value_namespace = name_space
                    self.dialctlpeercfgcarrierdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgClosedUserGroup"):
                    self.dialctlpeercfgclosedusergroup = value
                    self.dialctlpeercfgclosedusergroup.value_namespace = name_space
                    self.dialctlpeercfgclosedusergroup.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgFailureDelay"):
                    self.dialctlpeercfgfailuredelay = value
                    self.dialctlpeercfgfailuredelay.value_namespace = name_space
                    self.dialctlpeercfgfailuredelay.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgIfType"):
                    self.dialctlpeercfgiftype = value
                    self.dialctlpeercfgiftype.value_namespace = name_space
                    self.dialctlpeercfgiftype.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgInactivityTimer"):
                    self.dialctlpeercfginactivitytimer = value
                    self.dialctlpeercfginactivitytimer.value_namespace = name_space
                    self.dialctlpeercfginactivitytimer.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgInfoType"):
                    self.dialctlpeercfginfotype = value
                    self.dialctlpeercfginfotype.value_namespace = name_space
                    self.dialctlpeercfginfotype.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgLowerIf"):
                    self.dialctlpeercfglowerif = value
                    self.dialctlpeercfglowerif.value_namespace = name_space
                    self.dialctlpeercfglowerif.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgMaxDuration"):
                    self.dialctlpeercfgmaxduration = value
                    self.dialctlpeercfgmaxduration.value_namespace = name_space
                    self.dialctlpeercfgmaxduration.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgMinDuration"):
                    self.dialctlpeercfgminduration = value
                    self.dialctlpeercfgminduration.value_namespace = name_space
                    self.dialctlpeercfgminduration.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgOriginateAddress"):
                    self.dialctlpeercfgoriginateaddress = value
                    self.dialctlpeercfgoriginateaddress.value_namespace = name_space
                    self.dialctlpeercfgoriginateaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgPermission"):
                    self.dialctlpeercfgpermission = value
                    self.dialctlpeercfgpermission.value_namespace = name_space
                    self.dialctlpeercfgpermission.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgRetryDelay"):
                    self.dialctlpeercfgretrydelay = value
                    self.dialctlpeercfgretrydelay.value_namespace = name_space
                    self.dialctlpeercfgretrydelay.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgSpeed"):
                    self.dialctlpeercfgspeed = value
                    self.dialctlpeercfgspeed.value_namespace = name_space
                    self.dialctlpeercfgspeed.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgStatus"):
                    self.dialctlpeercfgstatus = value
                    self.dialctlpeercfgstatus.value_namespace = name_space
                    self.dialctlpeercfgstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgSubAddress"):
                    self.dialctlpeercfgsubaddress = value
                    self.dialctlpeercfgsubaddress.value_namespace = name_space
                    self.dialctlpeercfgsubaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerCfgTrapEnable"):
                    self.dialctlpeercfgtrapenable = value
                    self.dialctlpeercfgtrapenable.value_namespace = name_space
                    self.dialctlpeercfgtrapenable.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsAcceptCalls"):
                    self.dialctlpeerstatsacceptcalls = value
                    self.dialctlpeerstatsacceptcalls.value_namespace = name_space
                    self.dialctlpeerstatsacceptcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsChargedUnits"):
                    self.dialctlpeerstatschargedunits = value
                    self.dialctlpeerstatschargedunits.value_namespace = name_space
                    self.dialctlpeerstatschargedunits.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsConnectTime"):
                    self.dialctlpeerstatsconnecttime = value
                    self.dialctlpeerstatsconnecttime.value_namespace = name_space
                    self.dialctlpeerstatsconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsFailCalls"):
                    self.dialctlpeerstatsfailcalls = value
                    self.dialctlpeerstatsfailcalls.value_namespace = name_space
                    self.dialctlpeerstatsfailcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsLastDisconnectCause"):
                    self.dialctlpeerstatslastdisconnectcause = value
                    self.dialctlpeerstatslastdisconnectcause.value_namespace = name_space
                    self.dialctlpeerstatslastdisconnectcause.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsLastDisconnectText"):
                    self.dialctlpeerstatslastdisconnecttext = value
                    self.dialctlpeerstatslastdisconnecttext.value_namespace = name_space
                    self.dialctlpeerstatslastdisconnecttext.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsLastSetupTime"):
                    self.dialctlpeerstatslastsetuptime = value
                    self.dialctlpeerstatslastsetuptime.value_namespace = name_space
                    self.dialctlpeerstatslastsetuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsRefuseCalls"):
                    self.dialctlpeerstatsrefusecalls = value
                    self.dialctlpeerstatsrefusecalls.value_namespace = name_space
                    self.dialctlpeerstatsrefusecalls.value_namespace_prefix = name_space_prefix
                if(value_path == "dialCtlPeerStatsSuccessCalls"):
                    self.dialctlpeerstatssuccesscalls = value
                    self.dialctlpeerstatssuccesscalls.value_namespace = name_space
                    self.dialctlpeerstatssuccesscalls.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dialctlpeercfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dialctlpeercfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dialCtlPeerCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dialCtlPeerCfgEntry"):
                for c in self.dialctlpeercfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dialctlpeercfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dialCtlPeerCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Callactivetable(Entity):
        """
        A table containing information about active
        calls to a specific destination.
        
        .. attribute:: callactiveentry
        
        	The information regarding a single active Connection. An entry in this table will be created when a call is started. An entry in this table will be deleted when an active call clears
        	**type**\: list of    :py:class:`Callactiveentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DialControlMib.Callactivetable, self).__init__()

            self.yang_name = "callActiveTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"

            self.callactiveentry = YList(self)

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
                        super(DialControlMib.Callactivetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DialControlMib.Callactivetable, self).__setattr__(name, value)


        class Callactiveentry(Entity):
            """
            The information regarding a single active Connection.
            An entry in this table will be created when a call is
            started. An entry in this table will be deleted when
            an active call clears.
            
            .. attribute:: callactivesetuptime  <key>
            
            	The value of sysUpTime when the call associated to this entry was started. This will be useful for an NMS to retrieve all calls after a specific time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveindex  <key>
            
            	Small index variable to distinguish calls that start in the same hundredth of a second
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivecallorigin
            
            	The call origin
            	**type**\:   :py:class:`Callactivecallorigin <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.Callactivecallorigin>`
            
            .. attribute:: callactivecallstate
            
            	The current call state. unknown(1)     \- The call state is unknown. connecting(2)  \- A connection attempt (outgoing call)                  is being made. connected(3)   \- An incoming call is in the process                  of validation. active(4)      \- The call is active
            	**type**\:   :py:class:`Callactivecallstate <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.Callactivecallstate>`
            
            .. attribute:: callactivechargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveconnecttime
            
            	The value of sysUpTime when the call was connected. If the call is not connected, this object will have a value of zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveinfotype
            
            	The information type for this call
            	**type**\:   :py:class:`Callactiveinfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.Callactiveinfotype>`
            
            .. attribute:: callactivelogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call. If the ifIndex value is unknown, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeeraddress
            
            	The number this call is connected to. If the number is not available, then it will have a length of zero
            	**type**\:  str
            
            .. attribute:: callactivepeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeersubaddress
            
            	The subaddress this call is connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\:  str
            
            .. attribute:: callactivereceivebytes
            
            	The number of bytes which were received for this call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivereceivepackets
            
            	The number of packets which were received for this call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivetransmitbytes
            
            	The number of bytes which were transmitted for this call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivetransmitpackets
            
            	The number of packets which were transmitted for this call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DialControlMib.Callactivetable.Callactiveentry, self).__init__()

                self.yang_name = "callActiveEntry"
                self.yang_parent_name = "callActiveTable"

                self.callactivesetuptime = YLeaf(YType.uint32, "callActiveSetupTime")

                self.callactiveindex = YLeaf(YType.int32, "callActiveIndex")

                self.callactivecallorigin = YLeaf(YType.enumeration, "callActiveCallOrigin")

                self.callactivecallstate = YLeaf(YType.enumeration, "callActiveCallState")

                self.callactivechargedunits = YLeaf(YType.uint32, "callActiveChargedUnits")

                self.callactiveconnecttime = YLeaf(YType.uint32, "callActiveConnectTime")

                self.callactiveinfotype = YLeaf(YType.enumeration, "callActiveInfoType")

                self.callactivelogicalifindex = YLeaf(YType.int32, "callActiveLogicalIfIndex")

                self.callactivepeeraddress = YLeaf(YType.str, "callActivePeerAddress")

                self.callactivepeerid = YLeaf(YType.int32, "callActivePeerId")

                self.callactivepeerifindex = YLeaf(YType.int32, "callActivePeerIfIndex")

                self.callactivepeersubaddress = YLeaf(YType.str, "callActivePeerSubAddress")

                self.callactivereceivebytes = YLeaf(YType.uint32, "callActiveReceiveBytes")

                self.callactivereceivepackets = YLeaf(YType.uint32, "callActiveReceivePackets")

                self.callactivetransmitbytes = YLeaf(YType.uint32, "callActiveTransmitBytes")

                self.callactivetransmitpackets = YLeaf(YType.uint32, "callActiveTransmitPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("callactivesetuptime",
                                "callactiveindex",
                                "callactivecallorigin",
                                "callactivecallstate",
                                "callactivechargedunits",
                                "callactiveconnecttime",
                                "callactiveinfotype",
                                "callactivelogicalifindex",
                                "callactivepeeraddress",
                                "callactivepeerid",
                                "callactivepeerifindex",
                                "callactivepeersubaddress",
                                "callactivereceivebytes",
                                "callactivereceivepackets",
                                "callactivetransmitbytes",
                                "callactivetransmitpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DialControlMib.Callactivetable.Callactiveentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DialControlMib.Callactivetable.Callactiveentry, self).__setattr__(name, value)

            class Callactivecallorigin(Enum):
                """
                Callactivecallorigin

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
                Callactivecallstate

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
                Callactiveinfotype

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


            def has_data(self):
                return (
                    self.callactivesetuptime.is_set or
                    self.callactiveindex.is_set or
                    self.callactivecallorigin.is_set or
                    self.callactivecallstate.is_set or
                    self.callactivechargedunits.is_set or
                    self.callactiveconnecttime.is_set or
                    self.callactiveinfotype.is_set or
                    self.callactivelogicalifindex.is_set or
                    self.callactivepeeraddress.is_set or
                    self.callactivepeerid.is_set or
                    self.callactivepeerifindex.is_set or
                    self.callactivepeersubaddress.is_set or
                    self.callactivereceivebytes.is_set or
                    self.callactivereceivepackets.is_set or
                    self.callactivetransmitbytes.is_set or
                    self.callactivetransmitpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.callactivesetuptime.yfilter != YFilter.not_set or
                    self.callactiveindex.yfilter != YFilter.not_set or
                    self.callactivecallorigin.yfilter != YFilter.not_set or
                    self.callactivecallstate.yfilter != YFilter.not_set or
                    self.callactivechargedunits.yfilter != YFilter.not_set or
                    self.callactiveconnecttime.yfilter != YFilter.not_set or
                    self.callactiveinfotype.yfilter != YFilter.not_set or
                    self.callactivelogicalifindex.yfilter != YFilter.not_set or
                    self.callactivepeeraddress.yfilter != YFilter.not_set or
                    self.callactivepeerid.yfilter != YFilter.not_set or
                    self.callactivepeerifindex.yfilter != YFilter.not_set or
                    self.callactivepeersubaddress.yfilter != YFilter.not_set or
                    self.callactivereceivebytes.yfilter != YFilter.not_set or
                    self.callactivereceivepackets.yfilter != YFilter.not_set or
                    self.callactivetransmitbytes.yfilter != YFilter.not_set or
                    self.callactivetransmitpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "callActiveEntry" + "[callActiveSetupTime='" + self.callactivesetuptime.get() + "']" + "[callActiveIndex='" + self.callactiveindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/callActiveTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.callactivesetuptime.is_set or self.callactivesetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivesetuptime.get_name_leafdata())
                if (self.callactiveindex.is_set or self.callactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveindex.get_name_leafdata())
                if (self.callactivecallorigin.is_set or self.callactivecallorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivecallorigin.get_name_leafdata())
                if (self.callactivecallstate.is_set or self.callactivecallstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivecallstate.get_name_leafdata())
                if (self.callactivechargedunits.is_set or self.callactivechargedunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivechargedunits.get_name_leafdata())
                if (self.callactiveconnecttime.is_set or self.callactiveconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveconnecttime.get_name_leafdata())
                if (self.callactiveinfotype.is_set or self.callactiveinfotype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveinfotype.get_name_leafdata())
                if (self.callactivelogicalifindex.is_set or self.callactivelogicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivelogicalifindex.get_name_leafdata())
                if (self.callactivepeeraddress.is_set or self.callactivepeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivepeeraddress.get_name_leafdata())
                if (self.callactivepeerid.is_set or self.callactivepeerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivepeerid.get_name_leafdata())
                if (self.callactivepeerifindex.is_set or self.callactivepeerifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivepeerifindex.get_name_leafdata())
                if (self.callactivepeersubaddress.is_set or self.callactivepeersubaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivepeersubaddress.get_name_leafdata())
                if (self.callactivereceivebytes.is_set or self.callactivereceivebytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivereceivebytes.get_name_leafdata())
                if (self.callactivereceivepackets.is_set or self.callactivereceivepackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivereceivepackets.get_name_leafdata())
                if (self.callactivetransmitbytes.is_set or self.callactivetransmitbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivetransmitbytes.get_name_leafdata())
                if (self.callactivetransmitpackets.is_set or self.callactivetransmitpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivetransmitpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callActiveSetupTime" or name == "callActiveIndex" or name == "callActiveCallOrigin" or name == "callActiveCallState" or name == "callActiveChargedUnits" or name == "callActiveConnectTime" or name == "callActiveInfoType" or name == "callActiveLogicalIfIndex" or name == "callActivePeerAddress" or name == "callActivePeerId" or name == "callActivePeerIfIndex" or name == "callActivePeerSubAddress" or name == "callActiveReceiveBytes" or name == "callActiveReceivePackets" or name == "callActiveTransmitBytes" or name == "callActiveTransmitPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "callActiveSetupTime"):
                    self.callactivesetuptime = value
                    self.callactivesetuptime.value_namespace = name_space
                    self.callactivesetuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveIndex"):
                    self.callactiveindex = value
                    self.callactiveindex.value_namespace = name_space
                    self.callactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveCallOrigin"):
                    self.callactivecallorigin = value
                    self.callactivecallorigin.value_namespace = name_space
                    self.callactivecallorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveCallState"):
                    self.callactivecallstate = value
                    self.callactivecallstate.value_namespace = name_space
                    self.callactivecallstate.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveChargedUnits"):
                    self.callactivechargedunits = value
                    self.callactivechargedunits.value_namespace = name_space
                    self.callactivechargedunits.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveConnectTime"):
                    self.callactiveconnecttime = value
                    self.callactiveconnecttime.value_namespace = name_space
                    self.callactiveconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveInfoType"):
                    self.callactiveinfotype = value
                    self.callactiveinfotype.value_namespace = name_space
                    self.callactiveinfotype.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveLogicalIfIndex"):
                    self.callactivelogicalifindex = value
                    self.callactivelogicalifindex.value_namespace = name_space
                    self.callactivelogicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callActivePeerAddress"):
                    self.callactivepeeraddress = value
                    self.callactivepeeraddress.value_namespace = name_space
                    self.callactivepeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "callActivePeerId"):
                    self.callactivepeerid = value
                    self.callactivepeerid.value_namespace = name_space
                    self.callactivepeerid.value_namespace_prefix = name_space_prefix
                if(value_path == "callActivePeerIfIndex"):
                    self.callactivepeerifindex = value
                    self.callactivepeerifindex.value_namespace = name_space
                    self.callactivepeerifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callActivePeerSubAddress"):
                    self.callactivepeersubaddress = value
                    self.callactivepeersubaddress.value_namespace = name_space
                    self.callactivepeersubaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveReceiveBytes"):
                    self.callactivereceivebytes = value
                    self.callactivereceivebytes.value_namespace = name_space
                    self.callactivereceivebytes.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveReceivePackets"):
                    self.callactivereceivepackets = value
                    self.callactivereceivepackets.value_namespace = name_space
                    self.callactivereceivepackets.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveTransmitBytes"):
                    self.callactivetransmitbytes = value
                    self.callactivetransmitbytes.value_namespace = name_space
                    self.callactivetransmitbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveTransmitPackets"):
                    self.callactivetransmitpackets = value
                    self.callactivetransmitpackets.value_namespace = name_space
                    self.callactivetransmitpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.callactiveentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.callactiveentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "callActiveTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "callActiveEntry"):
                for c in self.callactiveentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DialControlMib.Callactivetable.Callactiveentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.callactiveentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "callActiveEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Callhistorytable(Entity):
        """
        A table containing information about specific
        calls to a specific destination.
        
        .. attribute:: callhistoryentry
        
        	The information regarding a single Connection
        	**type**\: list of    :py:class:`Callhistoryentry <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable.Callhistoryentry>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            super(DialControlMib.Callhistorytable, self).__init__()

            self.yang_name = "callHistoryTable"
            self.yang_parent_name = "DIAL-CONTROL-MIB"

            self.callhistoryentry = YList(self)

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
                        super(DialControlMib.Callhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DialControlMib.Callhistorytable, self).__setattr__(name, value)


        class Callhistoryentry(Entity):
            """
            The information regarding a single Connection.
            
            .. attribute:: callactivesetuptime  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: callhistorycallorigin
            
            	The call origin
            	**type**\:   :py:class:`Callhistorycallorigin <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable.Callhistoryentry.Callhistorycallorigin>`
            
            .. attribute:: callhistorychargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryconnecttime
            
            	The value of sysUpTime when the call was connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorydisconnectcause
            
            	The encoded network cause value associated with this call.  The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\:  str
            
            	**length:** 0..4
            
            .. attribute:: callhistorydisconnecttext
            
            	ASCII text describing the reason for call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause
            	**type**\:  str
            
            .. attribute:: callhistorydisconnecttime
            
            	The value of sysUpTime when the call was disconnected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryinfotype
            
            	The information type for this call
            	**type**\:   :py:class:`Callhistoryinfotype <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable.Callhistoryentry.Callhistoryinfotype>`
            
            .. attribute:: callhistorylogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: callhistorypeeraddress
            
            	The number this call was connected to. If the number is not available, then it will have a length of zero
            	**type**\:  str
            
            .. attribute:: callhistorypeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorypeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorypeersubaddress
            
            	The subaddress this call was connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\:  str
            
            .. attribute:: callhistoryreceivebytes
            
            	The number of bytes which were received while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryreceivepackets
            
            	The number of packets which were received while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorytransmitbytes
            
            	The number of bytes which were transmitted while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorytransmitpackets
            
            	The number of packets which were transmitted while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DIAL-CONTROL-MIB'
            _revision = '1996-09-23'

            def __init__(self):
                super(DialControlMib.Callhistorytable.Callhistoryentry, self).__init__()

                self.yang_name = "callHistoryEntry"
                self.yang_parent_name = "callHistoryTable"

                self.callactivesetuptime = YLeaf(YType.str, "callActiveSetupTime")

                self.callactiveindex = YLeaf(YType.str, "callActiveIndex")

                self.callhistorycallorigin = YLeaf(YType.enumeration, "callHistoryCallOrigin")

                self.callhistorychargedunits = YLeaf(YType.uint32, "callHistoryChargedUnits")

                self.callhistoryconnecttime = YLeaf(YType.uint32, "callHistoryConnectTime")

                self.callhistorydisconnectcause = YLeaf(YType.str, "callHistoryDisconnectCause")

                self.callhistorydisconnecttext = YLeaf(YType.str, "callHistoryDisconnectText")

                self.callhistorydisconnecttime = YLeaf(YType.uint32, "callHistoryDisconnectTime")

                self.callhistoryinfotype = YLeaf(YType.enumeration, "callHistoryInfoType")

                self.callhistorylogicalifindex = YLeaf(YType.int32, "callHistoryLogicalIfIndex")

                self.callhistorypeeraddress = YLeaf(YType.str, "callHistoryPeerAddress")

                self.callhistorypeerid = YLeaf(YType.int32, "callHistoryPeerId")

                self.callhistorypeerifindex = YLeaf(YType.int32, "callHistoryPeerIfIndex")

                self.callhistorypeersubaddress = YLeaf(YType.str, "callHistoryPeerSubAddress")

                self.callhistoryreceivebytes = YLeaf(YType.uint32, "callHistoryReceiveBytes")

                self.callhistoryreceivepackets = YLeaf(YType.uint32, "callHistoryReceivePackets")

                self.callhistorytransmitbytes = YLeaf(YType.uint32, "callHistoryTransmitBytes")

                self.callhistorytransmitpackets = YLeaf(YType.uint32, "callHistoryTransmitPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("callactivesetuptime",
                                "callactiveindex",
                                "callhistorycallorigin",
                                "callhistorychargedunits",
                                "callhistoryconnecttime",
                                "callhistorydisconnectcause",
                                "callhistorydisconnecttext",
                                "callhistorydisconnecttime",
                                "callhistoryinfotype",
                                "callhistorylogicalifindex",
                                "callhistorypeeraddress",
                                "callhistorypeerid",
                                "callhistorypeerifindex",
                                "callhistorypeersubaddress",
                                "callhistoryreceivebytes",
                                "callhistoryreceivepackets",
                                "callhistorytransmitbytes",
                                "callhistorytransmitpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DialControlMib.Callhistorytable.Callhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DialControlMib.Callhistorytable.Callhistoryentry, self).__setattr__(name, value)

            class Callhistorycallorigin(Enum):
                """
                Callhistorycallorigin

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
                Callhistoryinfotype

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


            def has_data(self):
                return (
                    self.callactivesetuptime.is_set or
                    self.callactiveindex.is_set or
                    self.callhistorycallorigin.is_set or
                    self.callhistorychargedunits.is_set or
                    self.callhistoryconnecttime.is_set or
                    self.callhistorydisconnectcause.is_set or
                    self.callhistorydisconnecttext.is_set or
                    self.callhistorydisconnecttime.is_set or
                    self.callhistoryinfotype.is_set or
                    self.callhistorylogicalifindex.is_set or
                    self.callhistorypeeraddress.is_set or
                    self.callhistorypeerid.is_set or
                    self.callhistorypeerifindex.is_set or
                    self.callhistorypeersubaddress.is_set or
                    self.callhistoryreceivebytes.is_set or
                    self.callhistoryreceivepackets.is_set or
                    self.callhistorytransmitbytes.is_set or
                    self.callhistorytransmitpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.callactivesetuptime.yfilter != YFilter.not_set or
                    self.callactiveindex.yfilter != YFilter.not_set or
                    self.callhistorycallorigin.yfilter != YFilter.not_set or
                    self.callhistorychargedunits.yfilter != YFilter.not_set or
                    self.callhistoryconnecttime.yfilter != YFilter.not_set or
                    self.callhistorydisconnectcause.yfilter != YFilter.not_set or
                    self.callhistorydisconnecttext.yfilter != YFilter.not_set or
                    self.callhistorydisconnecttime.yfilter != YFilter.not_set or
                    self.callhistoryinfotype.yfilter != YFilter.not_set or
                    self.callhistorylogicalifindex.yfilter != YFilter.not_set or
                    self.callhistorypeeraddress.yfilter != YFilter.not_set or
                    self.callhistorypeerid.yfilter != YFilter.not_set or
                    self.callhistorypeerifindex.yfilter != YFilter.not_set or
                    self.callhistorypeersubaddress.yfilter != YFilter.not_set or
                    self.callhistoryreceivebytes.yfilter != YFilter.not_set or
                    self.callhistoryreceivepackets.yfilter != YFilter.not_set or
                    self.callhistorytransmitbytes.yfilter != YFilter.not_set or
                    self.callhistorytransmitpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "callHistoryEntry" + "[callActiveSetupTime='" + self.callactivesetuptime.get() + "']" + "[callActiveIndex='" + self.callactiveindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/callHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.callactivesetuptime.is_set or self.callactivesetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivesetuptime.get_name_leafdata())
                if (self.callactiveindex.is_set or self.callactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveindex.get_name_leafdata())
                if (self.callhistorycallorigin.is_set or self.callhistorycallorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorycallorigin.get_name_leafdata())
                if (self.callhistorychargedunits.is_set or self.callhistorychargedunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorychargedunits.get_name_leafdata())
                if (self.callhistoryconnecttime.is_set or self.callhistoryconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistoryconnecttime.get_name_leafdata())
                if (self.callhistorydisconnectcause.is_set or self.callhistorydisconnectcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorydisconnectcause.get_name_leafdata())
                if (self.callhistorydisconnecttext.is_set or self.callhistorydisconnecttext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorydisconnecttext.get_name_leafdata())
                if (self.callhistorydisconnecttime.is_set or self.callhistorydisconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorydisconnecttime.get_name_leafdata())
                if (self.callhistoryinfotype.is_set or self.callhistoryinfotype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistoryinfotype.get_name_leafdata())
                if (self.callhistorylogicalifindex.is_set or self.callhistorylogicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorylogicalifindex.get_name_leafdata())
                if (self.callhistorypeeraddress.is_set or self.callhistorypeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorypeeraddress.get_name_leafdata())
                if (self.callhistorypeerid.is_set or self.callhistorypeerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorypeerid.get_name_leafdata())
                if (self.callhistorypeerifindex.is_set or self.callhistorypeerifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorypeerifindex.get_name_leafdata())
                if (self.callhistorypeersubaddress.is_set or self.callhistorypeersubaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorypeersubaddress.get_name_leafdata())
                if (self.callhistoryreceivebytes.is_set or self.callhistoryreceivebytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistoryreceivebytes.get_name_leafdata())
                if (self.callhistoryreceivepackets.is_set or self.callhistoryreceivepackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistoryreceivepackets.get_name_leafdata())
                if (self.callhistorytransmitbytes.is_set or self.callhistorytransmitbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorytransmitbytes.get_name_leafdata())
                if (self.callhistorytransmitpackets.is_set or self.callhistorytransmitpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callhistorytransmitpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callActiveSetupTime" or name == "callActiveIndex" or name == "callHistoryCallOrigin" or name == "callHistoryChargedUnits" or name == "callHistoryConnectTime" or name == "callHistoryDisconnectCause" or name == "callHistoryDisconnectText" or name == "callHistoryDisconnectTime" or name == "callHistoryInfoType" or name == "callHistoryLogicalIfIndex" or name == "callHistoryPeerAddress" or name == "callHistoryPeerId" or name == "callHistoryPeerIfIndex" or name == "callHistoryPeerSubAddress" or name == "callHistoryReceiveBytes" or name == "callHistoryReceivePackets" or name == "callHistoryTransmitBytes" or name == "callHistoryTransmitPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "callActiveSetupTime"):
                    self.callactivesetuptime = value
                    self.callactivesetuptime.value_namespace = name_space
                    self.callactivesetuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveIndex"):
                    self.callactiveindex = value
                    self.callactiveindex.value_namespace = name_space
                    self.callactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryCallOrigin"):
                    self.callhistorycallorigin = value
                    self.callhistorycallorigin.value_namespace = name_space
                    self.callhistorycallorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryChargedUnits"):
                    self.callhistorychargedunits = value
                    self.callhistorychargedunits.value_namespace = name_space
                    self.callhistorychargedunits.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryConnectTime"):
                    self.callhistoryconnecttime = value
                    self.callhistoryconnecttime.value_namespace = name_space
                    self.callhistoryconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryDisconnectCause"):
                    self.callhistorydisconnectcause = value
                    self.callhistorydisconnectcause.value_namespace = name_space
                    self.callhistorydisconnectcause.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryDisconnectText"):
                    self.callhistorydisconnecttext = value
                    self.callhistorydisconnecttext.value_namespace = name_space
                    self.callhistorydisconnecttext.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryDisconnectTime"):
                    self.callhistorydisconnecttime = value
                    self.callhistorydisconnecttime.value_namespace = name_space
                    self.callhistorydisconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryInfoType"):
                    self.callhistoryinfotype = value
                    self.callhistoryinfotype.value_namespace = name_space
                    self.callhistoryinfotype.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryLogicalIfIndex"):
                    self.callhistorylogicalifindex = value
                    self.callhistorylogicalifindex.value_namespace = name_space
                    self.callhistorylogicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryPeerAddress"):
                    self.callhistorypeeraddress = value
                    self.callhistorypeeraddress.value_namespace = name_space
                    self.callhistorypeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryPeerId"):
                    self.callhistorypeerid = value
                    self.callhistorypeerid.value_namespace = name_space
                    self.callhistorypeerid.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryPeerIfIndex"):
                    self.callhistorypeerifindex = value
                    self.callhistorypeerifindex.value_namespace = name_space
                    self.callhistorypeerifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryPeerSubAddress"):
                    self.callhistorypeersubaddress = value
                    self.callhistorypeersubaddress.value_namespace = name_space
                    self.callhistorypeersubaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryReceiveBytes"):
                    self.callhistoryreceivebytes = value
                    self.callhistoryreceivebytes.value_namespace = name_space
                    self.callhistoryreceivebytes.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryReceivePackets"):
                    self.callhistoryreceivepackets = value
                    self.callhistoryreceivepackets.value_namespace = name_space
                    self.callhistoryreceivepackets.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryTransmitBytes"):
                    self.callhistorytransmitbytes = value
                    self.callhistorytransmitbytes.value_namespace = name_space
                    self.callhistorytransmitbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "callHistoryTransmitPackets"):
                    self.callhistorytransmitpackets = value
                    self.callhistorytransmitpackets.value_namespace = name_space
                    self.callhistorytransmitpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.callhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.callhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "callHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "callHistoryEntry"):
                for c in self.callhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DialControlMib.Callhistorytable.Callhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.callhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "callHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.callactivetable is not None and self.callactivetable.has_data()) or
            (self.callhistory is not None and self.callhistory.has_data()) or
            (self.callhistorytable is not None and self.callhistorytable.has_data()) or
            (self.dialctlconfiguration is not None and self.dialctlconfiguration.has_data()) or
            (self.dialctlpeercfgtable is not None and self.dialctlpeercfgtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.callactivetable is not None and self.callactivetable.has_operation()) or
            (self.callhistory is not None and self.callhistory.has_operation()) or
            (self.callhistorytable is not None and self.callhistorytable.has_operation()) or
            (self.dialctlconfiguration is not None and self.dialctlconfiguration.has_operation()) or
            (self.dialctlpeercfgtable is not None and self.dialctlpeercfgtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DIAL-CONTROL-MIB:DIAL-CONTROL-MIB" + path_buffer

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

        if (child_yang_name == "callActiveTable"):
            if (self.callactivetable is None):
                self.callactivetable = DialControlMib.Callactivetable()
                self.callactivetable.parent = self
                self._children_name_map["callactivetable"] = "callActiveTable"
            return self.callactivetable

        if (child_yang_name == "callHistory"):
            if (self.callhistory is None):
                self.callhistory = DialControlMib.Callhistory()
                self.callhistory.parent = self
                self._children_name_map["callhistory"] = "callHistory"
            return self.callhistory

        if (child_yang_name == "callHistoryTable"):
            if (self.callhistorytable is None):
                self.callhistorytable = DialControlMib.Callhistorytable()
                self.callhistorytable.parent = self
                self._children_name_map["callhistorytable"] = "callHistoryTable"
            return self.callhistorytable

        if (child_yang_name == "dialCtlConfiguration"):
            if (self.dialctlconfiguration is None):
                self.dialctlconfiguration = DialControlMib.Dialctlconfiguration()
                self.dialctlconfiguration.parent = self
                self._children_name_map["dialctlconfiguration"] = "dialCtlConfiguration"
            return self.dialctlconfiguration

        if (child_yang_name == "dialCtlPeerCfgTable"):
            if (self.dialctlpeercfgtable is None):
                self.dialctlpeercfgtable = DialControlMib.Dialctlpeercfgtable()
                self.dialctlpeercfgtable.parent = self
                self._children_name_map["dialctlpeercfgtable"] = "dialCtlPeerCfgTable"
            return self.dialctlpeercfgtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "callActiveTable" or name == "callHistory" or name == "callHistoryTable" or name == "dialCtlConfiguration" or name == "dialCtlPeerCfgTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DialControlMib()
        return self._top_entity

