""" CISCO_DIAL_CONTROL_MIB 

The MIB module to describe call history information for
demand access and possibly other kinds of interfaces.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoDialControlMib(object):
    """
    
    
    .. attribute:: ccallhistoryiectable
    
    	This table contains information about Internal Error Code(s) (IEC) which caused the call to fail
    	**type**\:   :py:class:`Ccallhistoryiectable <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistoryiectable>`
    
    .. attribute:: ccallhistorytable
    
    	A table containing information about specific calls to a specific destination
    	**type**\:   :py:class:`Ccallhistorytable <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable>`
    
    .. attribute:: cpeerglobalconfiguration
    
    	
    	**type**\:   :py:class:`Cpeerglobalconfiguration <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Cpeerglobalconfiguration>`
    
    

    """

    _prefix = 'CISCO-DIAL-CONTROL-MIB'
    _revision = '2005-05-26'

    def __init__(self):
        self.ccallhistoryiectable = CiscoDialControlMib.Ccallhistoryiectable()
        self.ccallhistoryiectable.parent = self
        self.ccallhistorytable = CiscoDialControlMib.Ccallhistorytable()
        self.ccallhistorytable.parent = self
        self.cpeerglobalconfiguration = CiscoDialControlMib.Cpeerglobalconfiguration()
        self.cpeerglobalconfiguration.parent = self


    class Cpeerglobalconfiguration(object):
        """
        
        
        .. attribute:: cpeersearchtype
        
        	Specifies the peer search preference based on the type of peers in an universal/integrated port platform.  none      \- both voice and data peers are searched            in same preference. datavoice \- search data peers first. If no data peers            are found, the voice peers are searched. voicedata \- search voice peers first. If no voice peers            are found, the data peers are searched
        	**type**\:   :py:class:`CpeersearchtypeEnum <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Cpeerglobalconfiguration.CpeersearchtypeEnum>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            self.parent = None
            self.cpeersearchtype = None

        class CpeersearchtypeEnum(Enum):
            """
            CpeersearchtypeEnum

            Specifies the peer search preference based on the

            type of peers in an universal/integrated port

            platform.

            none      \- both voice and data peers are searched

                       in same preference.

            datavoice \- search data peers first. If no data peers

                       are found, the voice peers are searched.

            voicedata \- search voice peers first. If no voice peers

                       are found, the data peers are searched.

            .. data:: none = 1

            .. data:: datavoice = 2

            .. data:: voicedata = 3

            """

            none = 1

            datavoice = 2

            voicedata = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CiscoDialControlMib.Cpeerglobalconfiguration.CpeersearchtypeEnum']


        @property
        def _common_path(self):

            return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/CISCO-DIAL-CONTROL-MIB:cPeerGlobalConfiguration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpeersearchtype is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CiscoDialControlMib.Cpeerglobalconfiguration']['meta_info']


    class Ccallhistorytable(object):
        """
        A table containing information about specific
        calls to a specific destination.
        
        .. attribute:: ccallhistoryentry
        
        	The information regarding a single Connection
        	**type**\: list of    :py:class:`Ccallhistoryentry <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            self.parent = None
            self.ccallhistoryentry = YList()
            self.ccallhistoryentry.parent = self
            self.ccallhistoryentry.name = 'ccallhistoryentry'


        class Ccallhistoryentry(object):
            """
            The information regarding a single Connection.
            
            .. attribute:: ccallhistoryindex  <key>
            
            	A monotonically increasing integer for the sole purpose of indexing call disconnection events.  When it reaches the  maximum value, an extremely unlikely event, the agent wraps  the value back to 1 and may flush existing entries
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccallhistorycallorigin
            
            	The call origin
            	**type**\:   :py:class:`CcallhistorycalloriginEnum <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistorycalloriginEnum>`
            
            .. attribute:: ccallhistorychargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryconnecttime
            
            	The value of sysUpTime when the call was connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorydisconnectcause
            
            	The encoded network cause value associated with this call.  The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\:  str
            
            	**length:** 0..4
            
            .. attribute:: ccallhistorydisconnecttext
            
            	ASCII text describing the reason for call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause
            	**type**\:  str
            
            .. attribute:: ccallhistorydisconnecttime
            
            	The value of sysUpTime when the call was disconnected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryinfotype
            
            	The information type for this call
            	**type**\:   :py:class:`CcallhistoryinfotypeEnum <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryinfotypeEnum>`
            
            .. attribute:: ccallhistorylogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call. If the ifIndex value is unknown, the value of this object  will be zero. For an IP call, the value will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorypeeraddress
            
            	The number this call was connected to. If the number is not available, then it will have a length of zero
            	**type**\:  str
            
            .. attribute:: ccallhistorypeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorypeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorypeersubaddress
            
            	The subaddress this call was connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\:  str
            
            .. attribute:: ccallhistoryreceivebytes
            
            	The number of bytes which were received while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryreceivepackets
            
            	The number of packets which were received while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryreleasesource
            
            	Originator of the call release
            	**type**\:   :py:class:`CcallhistoryreleasesourceEnum <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesourceEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: ccallhistoryreleasesrc
            
            	Originator of the call release. Indicates the source of  the call release as follows \:  1) callingPartyInPstn \: Calling party in PSTN. 2) callingPartyInVoip \: Calling party in VoIP. 3) calledPartyInPstn \: Called party in PSTN. 4) calledPartyInVoip \: Called party in VoIP. 5) internalReleaseInPotsLeg \: Due to an internal error     in Telephony call leg. 6) internalReleaseInVoipLeg \: Due to an internal error    in VoIP call leg. 7) internalCallControlApp \: Due to an internal error    in Session Application or Tcl or VXML script originated    release.  8) internalReleaseInVoipAAA \: Due to an internal error    in VoIP AAA module. 9) consoleCommand \: Due to CLI or MML. 10) externalRadiusServer \: Call failed during authorization     , authentication or due to receipt of POD from the      RADIUS server. 11) externalNmsApp \: Due to SNMP request to clear      the call. 12) externalCallControlAgent \: External Call Control Agent     initiated clear. 13) gatekeeper \: Gatekeeper initiated clear due to receipt     of Admission Reject, Disengage Request message. 14) externalGKTMPServer \: External GKTMP server initiated     clear due to receipt of Admission Reject message from     the gatekeeper, triggered by RESPONSE.ARJ message from     the GKTMP server
            	**type**\:   :py:class:`CcallhistoryreleasesrcEnum <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesrcEnum>`
            
            .. attribute:: ccallhistorysetuptime
            
            	The value of sysUpTime when the call setup was started. This will be useful for an NMS to sort the call history entry with call setup time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network. The value of this object is the same as callActiveSetupTime in the callActiveTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorytransmitbytes
            
            	The number of bytes which were transmitted while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorytransmitpackets
            
            	The number of packets which were transmitted while this call was active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-DIAL-CONTROL-MIB'
            _revision = '2005-05-26'

            def __init__(self):
                self.parent = None
                self.ccallhistoryindex = None
                self.ccallhistorycallorigin = None
                self.ccallhistorychargedunits = None
                self.ccallhistoryconnecttime = None
                self.ccallhistorydisconnectcause = None
                self.ccallhistorydisconnecttext = None
                self.ccallhistorydisconnecttime = None
                self.ccallhistoryinfotype = None
                self.ccallhistorylogicalifindex = None
                self.ccallhistorypeeraddress = None
                self.ccallhistorypeerid = None
                self.ccallhistorypeerifindex = None
                self.ccallhistorypeersubaddress = None
                self.ccallhistoryreceivebytes = None
                self.ccallhistoryreceivepackets = None
                self.ccallhistoryreleasesource = None
                self.ccallhistoryreleasesrc = None
                self.ccallhistorysetuptime = None
                self.ccallhistorytransmitbytes = None
                self.ccallhistorytransmitpackets = None

            class CcallhistorycalloriginEnum(Enum):
                """
                CcallhistorycalloriginEnum

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
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistorycalloriginEnum']


            class CcallhistoryinfotypeEnum(Enum):
                """
                CcallhistoryinfotypeEnum

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
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryinfotypeEnum']


            class CcallhistoryreleasesourceEnum(Enum):
                """
                CcallhistoryreleasesourceEnum

                Originator of the call release.

                .. data:: callingPartyInPstn = 1

                .. data:: callingPartyInVoip = 2

                .. data:: calledPartyInPstn = 3

                .. data:: calledPartyInVoip = 4

                .. data:: internalRelease = 5

                .. data:: internalCallControlApp = 6

                .. data:: consoleCommand = 7

                .. data:: externalRadiusServer = 8

                .. data:: externalNmsApp = 9

                .. data:: externalCallControlAgent = 10

                """

                callingPartyInPstn = 1

                callingPartyInVoip = 2

                calledPartyInPstn = 3

                calledPartyInVoip = 4

                internalRelease = 5

                internalCallControlApp = 6

                consoleCommand = 7

                externalRadiusServer = 8

                externalNmsApp = 9

                externalCallControlAgent = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesourceEnum']


            class CcallhistoryreleasesrcEnum(Enum):
                """
                CcallhistoryreleasesrcEnum

                Originator of the call release. Indicates the source of 

                the call release as follows \: 

                1) callingPartyInPstn \: Calling party in PSTN.

                2) callingPartyInVoip \: Calling party in VoIP.

                3) calledPartyInPstn \: Called party in PSTN.

                4) calledPartyInVoip \: Called party in VoIP.

                5) internalReleaseInPotsLeg \: Due to an internal error 

                   in Telephony call leg.

                6) internalReleaseInVoipLeg \: Due to an internal error

                   in VoIP call leg.

                7) internalCallControlApp \: Due to an internal error

                   in Session Application or Tcl or VXML script originated

                   release. 

                8) internalReleaseInVoipAAA \: Due to an internal error

                   in VoIP AAA module.

                9) consoleCommand \: Due to CLI or MML.

                10) externalRadiusServer \: Call failed during authorization

                    , authentication or due to receipt of POD from the 

                    RADIUS server.

                11) externalNmsApp \: Due to SNMP request to clear 

                    the call.

                12) externalCallControlAgent \: External Call Control Agent

                    initiated clear.

                13) gatekeeper \: Gatekeeper initiated clear due to receipt

                    of Admission Reject, Disengage Request message.

                14) externalGKTMPServer \: External GKTMP server initiated

                    clear due to receipt of Admission Reject message from

                    the gatekeeper, triggered by RESPONSE.ARJ message from

                    the GKTMP server.

                .. data:: callingPartyInPstn = 1

                .. data:: callingPartyInVoip = 2

                .. data:: calledPartyInPstn = 3

                .. data:: calledPartyInVoip = 4

                .. data:: internalReleaseInPotsLeg = 5

                .. data:: internalReleaseInVoipLeg = 6

                .. data:: internalCallControlApp = 7

                .. data:: internalReleaseInVoipAAA = 8

                .. data:: consoleCommand = 9

                .. data:: externalRadiusServer = 10

                .. data:: externalNmsApp = 11

                .. data:: externalCallControlAgent = 12

                .. data:: gatekeeper = 13

                .. data:: externalGKTMPServer = 14

                """

                callingPartyInPstn = 1

                callingPartyInVoip = 2

                calledPartyInPstn = 3

                calledPartyInVoip = 4

                internalReleaseInPotsLeg = 5

                internalReleaseInVoipLeg = 6

                internalCallControlApp = 7

                internalReleaseInVoipAAA = 8

                consoleCommand = 9

                externalRadiusServer = 10

                externalNmsApp = 11

                externalCallControlAgent = 12

                gatekeeper = 13

                externalGKTMPServer = 14


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesrcEnum']


            @property
            def _common_path(self):
                if self.ccallhistoryindex is None:
                    raise YPYModelError('Key property ccallhistoryindex is None')

                return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/CISCO-DIAL-CONTROL-MIB:cCallHistoryTable/CISCO-DIAL-CONTROL-MIB:cCallHistoryEntry[CISCO-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ccallhistoryindex is not None:
                    return True

                if self.ccallhistorycallorigin is not None:
                    return True

                if self.ccallhistorychargedunits is not None:
                    return True

                if self.ccallhistoryconnecttime is not None:
                    return True

                if self.ccallhistorydisconnectcause is not None:
                    return True

                if self.ccallhistorydisconnecttext is not None:
                    return True

                if self.ccallhistorydisconnecttime is not None:
                    return True

                if self.ccallhistoryinfotype is not None:
                    return True

                if self.ccallhistorylogicalifindex is not None:
                    return True

                if self.ccallhistorypeeraddress is not None:
                    return True

                if self.ccallhistorypeerid is not None:
                    return True

                if self.ccallhistorypeerifindex is not None:
                    return True

                if self.ccallhistorypeersubaddress is not None:
                    return True

                if self.ccallhistoryreceivebytes is not None:
                    return True

                if self.ccallhistoryreceivepackets is not None:
                    return True

                if self.ccallhistoryreleasesource is not None:
                    return True

                if self.ccallhistoryreleasesrc is not None:
                    return True

                if self.ccallhistorysetuptime is not None:
                    return True

                if self.ccallhistorytransmitbytes is not None:
                    return True

                if self.ccallhistorytransmitpackets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/CISCO-DIAL-CONTROL-MIB:cCallHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccallhistoryentry is not None:
                for child_ref in self.ccallhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CiscoDialControlMib.Ccallhistorytable']['meta_info']


    class Ccallhistoryiectable(object):
        """
        This table contains information about Internal Error
        Code(s) (IEC) which caused the call to fail.
        
        .. attribute:: ccallhistoryiecentry
        
        	The IEC information regarding a single call
        	**type**\: list of    :py:class:`Ccallhistoryiecentry <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            self.parent = None
            self.ccallhistoryiecentry = YList()
            self.ccallhistoryiecentry.parent = self
            self.ccallhistoryiecentry.name = 'ccallhistoryiecentry'


        class Ccallhistoryiecentry(object):
            """
            The IEC information regarding a single call.
            
            .. attribute:: ccallhistoryindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: ccallhistoryiecindex  <key>
            
            	This object is used to index one or more IECs in the context of a single call.  In most cases there will only be one IEC when a call fails.  However, it is possible for the software processing the call to  generate multiple IECs before the call ultimately fails. In that scenario, there will be multiple entries in this table related to a single call (cCallHistoryIndex) and this object will serve to uniquely identify each IEC
            	**type**\:  int
            
            	**range:** 1..1024
            
            .. attribute:: ccallhistoryiec
            
            	This object reflects the Internal Error Code. The format is a string of dotted decimal numbers composed of the following components\:  Version.Entity.Category.Subsystem.Errorcode.Diagnostic  Each component is defined as follows\: Version     \: The version of IEC software. Entity      \: The network entity that originated               the error. Category    \: The category of the error (eg, software               error, hardware resource unavailable, ...) Subsystem   \: The subsystem in which the error occurred. Errorcode   \: A subsytem\-specific error code. Diagnostic  \: An implementation\-specific diagnostic code
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-DIAL-CONTROL-MIB'
            _revision = '2005-05-26'

            def __init__(self):
                self.parent = None
                self.ccallhistoryindex = None
                self.ccallhistoryiecindex = None
                self.ccallhistoryiec = None

            @property
            def _common_path(self):
                if self.ccallhistoryindex is None:
                    raise YPYModelError('Key property ccallhistoryindex is None')
                if self.ccallhistoryiecindex is None:
                    raise YPYModelError('Key property ccallhistoryiecindex is None')

                return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/CISCO-DIAL-CONTROL-MIB:cCallHistoryIecTable/CISCO-DIAL-CONTROL-MIB:cCallHistoryIecEntry[CISCO-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + '][CISCO-DIAL-CONTROL-MIB:cCallHistoryIecIndex = ' + str(self.ccallhistoryiecindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ccallhistoryindex is not None:
                    return True

                if self.ccallhistoryiecindex is not None:
                    return True

                if self.ccallhistoryiec is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/CISCO-DIAL-CONTROL-MIB:cCallHistoryIecTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ccallhistoryiecentry is not None:
                for child_ref in self.ccallhistoryiecentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CiscoDialControlMib.Ccallhistoryiectable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ccallhistoryiectable is not None and self.ccallhistoryiectable._has_data():
            return True

        if self.ccallhistorytable is not None and self.ccallhistorytable._has_data():
            return True

        if self.cpeerglobalconfiguration is not None and self.cpeerglobalconfiguration._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CiscoDialControlMib']['meta_info']


