""" DIAL_CONTROL_MIB 

The MIB module to describe peer information for
demand access and possibly other kinds of interfaces.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class DialControlMib(object):
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
        self.callactivetable = DialControlMib.Callactivetable()
        self.callactivetable.parent = self
        self.callhistory = DialControlMib.Callhistory()
        self.callhistory.parent = self
        self.callhistorytable = DialControlMib.Callhistorytable()
        self.callhistorytable.parent = self
        self.dialctlconfiguration = DialControlMib.Dialctlconfiguration()
        self.dialctlconfiguration.parent = self
        self.dialctlpeercfgtable = DialControlMib.Dialctlpeercfgtable()
        self.dialctlpeercfgtable.parent = self


    class Dialctlconfiguration(object):
        """
        
        
        .. attribute:: dialctlacceptmode
        
        	The security level for acceptance of incoming calls. acceptNone(1)  \- incoming calls will not be accepted acceptAll(2)   \- incoming calls will be accepted,                  even if there is no matching entry                  in the dialCtlPeerCfgTable acceptKnown(3) \- incoming calls will be accepted only                  if there is a matching entry in the                  dialCtlPeerCfgTable
        	**type**\:   :py:class:`DialctlacceptmodeEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlconfiguration.DialctlacceptmodeEnum>`
        
        .. attribute:: dialctltrapenable
        
        	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for all peers. If the value of this object is enabled(1), traps will be generated for all peers. If the value of this object is disabled(2), traps will be generated only for peers having dialCtlPeerCfgTrapEnable set to enabled(1)
        	**type**\:   :py:class:`DialctltrapenableEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlconfiguration.DialctltrapenableEnum>`
        
        

        """

        _prefix = 'DIAL-CONTROL-MIB'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.dialctlacceptmode = None
            self.dialctltrapenable = None

        class DialctlacceptmodeEnum(Enum):
            """
            DialctlacceptmodeEnum

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

            acceptNone = 1

            acceptAll = 2

            acceptKnown = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DialControlMib.Dialctlconfiguration.DialctlacceptmodeEnum']


        class DialctltrapenableEnum(Enum):
            """
            DialctltrapenableEnum

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

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DialControlMib.Dialctlconfiguration.DialctltrapenableEnum']


        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlConfiguration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dialctlacceptmode is not None:
                return True

            if self.dialctltrapenable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DialControlMib.Dialctlconfiguration']['meta_info']


    class Callhistory(object):
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
            self.parent = None
            self.callhistoryretaintimer = None
            self.callhistorytablemaxlength = None

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.callhistoryretaintimer is not None:
                return True

            if self.callhistorytablemaxlength is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DialControlMib.Callhistory']['meta_info']


    class Dialctlpeercfgtable(object):
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
            self.parent = None
            self.dialctlpeercfgentry = YList()
            self.dialctlpeercfgentry.parent = self
            self.dialctlpeercfgentry.name = 'dialctlpeercfgentry'


        class Dialctlpeercfgentry(object):
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
            	**type**\:   :py:class:`IanaiftypeEnum <ydk.models.cisco_ios_xe.IANAifType_MIB.IanaiftypeEnum>`
            
            .. attribute:: dialctlpeercfginactivitytimer
            
            	The connection will be automatically disconnected if no longer carrying useful data for a time period, in seconds, specified in this object. Useful data in this context refers to forwarding packets, including routing information; it excludes the encapsulator maintenance frames. A value of zero means the connection will not be automatically taken down due to inactivity, which implies that it is a dedicated circuit
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: dialctlpeercfginfotype
            
            	The Information Transfer Capability to be used when calling this peer.  speech(2) refers to a non\-data connection, whereas audio31(6) and audio7(7) refer to data mode connections
            	**type**\:   :py:class:`DialctlpeercfginfotypeEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfginfotypeEnum>`
            
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
            	**type**\:   :py:class:`DialctlpeercfgpermissionEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgpermissionEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: dialctlpeercfgsubaddress
            
            	Subaddress at which the peer will be called. If the subaddress is undefined for the given media or unused, this is a zero length string
            	**type**\:  str
            
            .. attribute:: dialctlpeercfgtrapenable
            
            	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for this peer
            	**type**\:   :py:class:`DialctlpeercfgtrapenableEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgtrapenableEnum>`
            
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
                self.parent = None
                self.dialctlpeercfgid = None
                self.ifindex = None
                self.dialctlpeercfgansweraddress = None
                self.dialctlpeercfgcallretries = None
                self.dialctlpeercfgcarrierdelay = None
                self.dialctlpeercfgclosedusergroup = None
                self.dialctlpeercfgfailuredelay = None
                self.dialctlpeercfgiftype = None
                self.dialctlpeercfginactivitytimer = None
                self.dialctlpeercfginfotype = None
                self.dialctlpeercfglowerif = None
                self.dialctlpeercfgmaxduration = None
                self.dialctlpeercfgminduration = None
                self.dialctlpeercfgoriginateaddress = None
                self.dialctlpeercfgpermission = None
                self.dialctlpeercfgretrydelay = None
                self.dialctlpeercfgspeed = None
                self.dialctlpeercfgstatus = None
                self.dialctlpeercfgsubaddress = None
                self.dialctlpeercfgtrapenable = None
                self.dialctlpeerstatsacceptcalls = None
                self.dialctlpeerstatschargedunits = None
                self.dialctlpeerstatsconnecttime = None
                self.dialctlpeerstatsfailcalls = None
                self.dialctlpeerstatslastdisconnectcause = None
                self.dialctlpeerstatslastdisconnecttext = None
                self.dialctlpeerstatslastsetuptime = None
                self.dialctlpeerstatsrefusecalls = None
                self.dialctlpeerstatssuccesscalls = None

            class DialctlpeercfginfotypeEnum(Enum):
                """
                DialctlpeercfginfotypeEnum

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

                other = 1

                speech = 2

                unrestrictedDigital = 3

                unrestrictedDigital56 = 4

                restrictedDigital = 5

                audio31 = 6

                audio7 = 7

                video = 8

                packetSwitched = 9

                fax = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfginfotypeEnum']


            class DialctlpeercfgpermissionEnum(Enum):
                """
                DialctlpeercfgpermissionEnum

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

                originate = 1

                answer = 2

                both = 3

                callback = 4

                none = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgpermissionEnum']


            class DialctlpeercfgtrapenableEnum(Enum):
                """
                DialctlpeercfgtrapenableEnum

                This object indicates whether dialCtlPeerCallInformation

                and dialCtlPeerCallSetup traps should be generated for

                this peer.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgtrapenableEnum']


            @property
            def _common_path(self):
                if self.dialctlpeercfgid is None:
                    raise YPYModelError('Key property dialctlpeercfgid is None')
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlPeerCfgTable/DIAL-CONTROL-MIB:dialCtlPeerCfgEntry[DIAL-CONTROL-MIB:dialCtlPeerCfgId = ' + str(self.dialctlpeercfgid) + '][DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dialctlpeercfgid is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.dialctlpeercfgansweraddress is not None:
                    return True

                if self.dialctlpeercfgcallretries is not None:
                    return True

                if self.dialctlpeercfgcarrierdelay is not None:
                    return True

                if self.dialctlpeercfgclosedusergroup is not None:
                    return True

                if self.dialctlpeercfgfailuredelay is not None:
                    return True

                if self.dialctlpeercfgiftype is not None:
                    return True

                if self.dialctlpeercfginactivitytimer is not None:
                    return True

                if self.dialctlpeercfginfotype is not None:
                    return True

                if self.dialctlpeercfglowerif is not None:
                    return True

                if self.dialctlpeercfgmaxduration is not None:
                    return True

                if self.dialctlpeercfgminduration is not None:
                    return True

                if self.dialctlpeercfgoriginateaddress is not None:
                    return True

                if self.dialctlpeercfgpermission is not None:
                    return True

                if self.dialctlpeercfgretrydelay is not None:
                    return True

                if self.dialctlpeercfgspeed is not None:
                    return True

                if self.dialctlpeercfgstatus is not None:
                    return True

                if self.dialctlpeercfgsubaddress is not None:
                    return True

                if self.dialctlpeercfgtrapenable is not None:
                    return True

                if self.dialctlpeerstatsacceptcalls is not None:
                    return True

                if self.dialctlpeerstatschargedunits is not None:
                    return True

                if self.dialctlpeerstatsconnecttime is not None:
                    return True

                if self.dialctlpeerstatsfailcalls is not None:
                    return True

                if self.dialctlpeerstatslastdisconnectcause is not None:
                    return True

                if self.dialctlpeerstatslastdisconnecttext is not None:
                    return True

                if self.dialctlpeerstatslastsetuptime is not None:
                    return True

                if self.dialctlpeerstatsrefusecalls is not None:
                    return True

                if self.dialctlpeerstatssuccesscalls is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlPeerCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dialctlpeercfgentry is not None:
                for child_ref in self.dialctlpeercfgentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DialControlMib.Dialctlpeercfgtable']['meta_info']


    class Callactivetable(object):
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
            self.parent = None
            self.callactiveentry = YList()
            self.callactiveentry.parent = self
            self.callactiveentry.name = 'callactiveentry'


        class Callactiveentry(object):
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
            	**type**\:   :py:class:`CallactivecalloriginEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.CallactivecalloriginEnum>`
            
            .. attribute:: callactivecallstate
            
            	The current call state. unknown(1)     \- The call state is unknown. connecting(2)  \- A connection attempt (outgoing call)                  is being made. connected(3)   \- An incoming call is in the process                  of validation. active(4)      \- The call is active
            	**type**\:   :py:class:`CallactivecallstateEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.CallactivecallstateEnum>`
            
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
            	**type**\:   :py:class:`CallactiveinfotypeEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry.CallactiveinfotypeEnum>`
            
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
                self.parent = None
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.callactivecallorigin = None
                self.callactivecallstate = None
                self.callactivechargedunits = None
                self.callactiveconnecttime = None
                self.callactiveinfotype = None
                self.callactivelogicalifindex = None
                self.callactivepeeraddress = None
                self.callactivepeerid = None
                self.callactivepeerifindex = None
                self.callactivepeersubaddress = None
                self.callactivereceivebytes = None
                self.callactivereceivepackets = None
                self.callactivetransmitbytes = None
                self.callactivetransmitpackets = None

            class CallactivecalloriginEnum(Enum):
                """
                CallactivecalloriginEnum

                The call origin.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: callback = 3

                """

                originate = 1

                answer = 2

                callback = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Callactivetable.Callactiveentry.CallactivecalloriginEnum']


            class CallactivecallstateEnum(Enum):
                """
                CallactivecallstateEnum

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

                unknown = 1

                connecting = 2

                connected = 3

                active = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Callactivetable.Callactiveentry.CallactivecallstateEnum']


            class CallactiveinfotypeEnum(Enum):
                """
                CallactiveinfotypeEnum

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

                other = 1

                speech = 2

                unrestrictedDigital = 3

                unrestrictedDigital56 = 4

                restrictedDigital = 5

                audio31 = 6

                audio7 = 7

                video = 8

                packetSwitched = 9

                fax = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Callactivetable.Callactiveentry.CallactiveinfotypeEnum']


            @property
            def _common_path(self):
                if self.callactivesetuptime is None:
                    raise YPYModelError('Key property callactivesetuptime is None')
                if self.callactiveindex is None:
                    raise YPYModelError('Key property callactiveindex is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callActiveTable/DIAL-CONTROL-MIB:callActiveEntry[DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + '][DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.callactivesetuptime is not None:
                    return True

                if self.callactiveindex is not None:
                    return True

                if self.callactivecallorigin is not None:
                    return True

                if self.callactivecallstate is not None:
                    return True

                if self.callactivechargedunits is not None:
                    return True

                if self.callactiveconnecttime is not None:
                    return True

                if self.callactiveinfotype is not None:
                    return True

                if self.callactivelogicalifindex is not None:
                    return True

                if self.callactivepeeraddress is not None:
                    return True

                if self.callactivepeerid is not None:
                    return True

                if self.callactivepeerifindex is not None:
                    return True

                if self.callactivepeersubaddress is not None:
                    return True

                if self.callactivereceivebytes is not None:
                    return True

                if self.callactivereceivepackets is not None:
                    return True

                if self.callactivetransmitbytes is not None:
                    return True

                if self.callactivetransmitpackets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DialControlMib.Callactivetable.Callactiveentry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.callactiveentry is not None:
                for child_ref in self.callactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DialControlMib.Callactivetable']['meta_info']


    class Callhistorytable(object):
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
            self.parent = None
            self.callhistoryentry = YList()
            self.callhistoryentry.parent = self
            self.callhistoryentry.name = 'callhistoryentry'


        class Callhistoryentry(object):
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
            	**type**\:   :py:class:`CallhistorycalloriginEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable.Callhistoryentry.CallhistorycalloriginEnum>`
            
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
            	**type**\:   :py:class:`CallhistoryinfotypeEnum <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callhistorytable.Callhistoryentry.CallhistoryinfotypeEnum>`
            
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
                self.parent = None
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.callhistorycallorigin = None
                self.callhistorychargedunits = None
                self.callhistoryconnecttime = None
                self.callhistorydisconnectcause = None
                self.callhistorydisconnecttext = None
                self.callhistorydisconnecttime = None
                self.callhistoryinfotype = None
                self.callhistorylogicalifindex = None
                self.callhistorypeeraddress = None
                self.callhistorypeerid = None
                self.callhistorypeerifindex = None
                self.callhistorypeersubaddress = None
                self.callhistoryreceivebytes = None
                self.callhistoryreceivepackets = None
                self.callhistorytransmitbytes = None
                self.callhistorytransmitpackets = None

            class CallhistorycalloriginEnum(Enum):
                """
                CallhistorycalloriginEnum

                The call origin.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: callback = 3

                """

                originate = 1

                answer = 2

                callback = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Callhistorytable.Callhistoryentry.CallhistorycalloriginEnum']


            class CallhistoryinfotypeEnum(Enum):
                """
                CallhistoryinfotypeEnum

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

                other = 1

                speech = 2

                unrestrictedDigital = 3

                unrestrictedDigital56 = 4

                restrictedDigital = 5

                audio31 = 6

                audio7 = 7

                video = 8

                packetSwitched = 9

                fax = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DialControlMib.Callhistorytable.Callhistoryentry.CallhistoryinfotypeEnum']


            @property
            def _common_path(self):
                if self.callactivesetuptime is None:
                    raise YPYModelError('Key property callactivesetuptime is None')
                if self.callactiveindex is None:
                    raise YPYModelError('Key property callactiveindex is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistoryTable/DIAL-CONTROL-MIB:callHistoryEntry[DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + '][DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.callactivesetuptime is not None:
                    return True

                if self.callactiveindex is not None:
                    return True

                if self.callhistorycallorigin is not None:
                    return True

                if self.callhistorychargedunits is not None:
                    return True

                if self.callhistoryconnecttime is not None:
                    return True

                if self.callhistorydisconnectcause is not None:
                    return True

                if self.callhistorydisconnecttext is not None:
                    return True

                if self.callhistorydisconnecttime is not None:
                    return True

                if self.callhistoryinfotype is not None:
                    return True

                if self.callhistorylogicalifindex is not None:
                    return True

                if self.callhistorypeeraddress is not None:
                    return True

                if self.callhistorypeerid is not None:
                    return True

                if self.callhistorypeerifindex is not None:
                    return True

                if self.callhistorypeersubaddress is not None:
                    return True

                if self.callhistoryreceivebytes is not None:
                    return True

                if self.callhistoryreceivepackets is not None:
                    return True

                if self.callhistorytransmitbytes is not None:
                    return True

                if self.callhistorytransmitpackets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DialControlMib.Callhistorytable.Callhistoryentry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.callhistoryentry is not None:
                for child_ref in self.callhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DialControlMib.Callhistorytable']['meta_info']

    @property
    def _common_path(self):

        return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.callactivetable is not None and self.callactivetable._has_data():
            return True

        if self.callhistory is not None and self.callhistory._has_data():
            return True

        if self.callhistorytable is not None and self.callhistorytable._has_data():
            return True

        if self.dialctlconfiguration is not None and self.dialctlconfiguration._has_data():
            return True

        if self.dialctlpeercfgtable is not None and self.dialctlpeercfgtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DIAL_CONTROL_MIB as meta
        return meta._meta_table['DialControlMib']['meta_info']


