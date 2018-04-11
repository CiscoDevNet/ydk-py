""" CISCO_DIAL_CONTROL_MIB 

The MIB module to describe call history information for
demand access and possibly other kinds of interfaces.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCODIALCONTROLMIB(Entity):
    """
    
    
    .. attribute:: cpeerglobalconfiguration
    
    	
    	**type**\:  :py:class:`Cpeerglobalconfiguration <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Cpeerglobalconfiguration>`
    
    .. attribute:: ccallhistorytable
    
    	A table containing information about specific calls to a specific destination
    	**type**\:  :py:class:`Ccallhistorytable <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable>`
    
    .. attribute:: ccallhistoryiectable
    
    	This table contains information about Internal Error Code(s) (IEC) which caused the call to fail
    	**type**\:  :py:class:`Ccallhistoryiectable <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistoryiectable>`
    
    

    """

    _prefix = 'CISCO-DIAL-CONTROL-MIB'
    _revision = '2005-05-26'

    def __init__(self):
        super(CISCODIALCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cPeerGlobalConfiguration", ("cpeerglobalconfiguration", CISCODIALCONTROLMIB.Cpeerglobalconfiguration)), ("cCallHistoryTable", ("ccallhistorytable", CISCODIALCONTROLMIB.Ccallhistorytable)), ("cCallHistoryIecTable", ("ccallhistoryiectable", CISCODIALCONTROLMIB.Ccallhistoryiectable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpeerglobalconfiguration = CISCODIALCONTROLMIB.Cpeerglobalconfiguration()
        self.cpeerglobalconfiguration.parent = self
        self._children_name_map["cpeerglobalconfiguration"] = "cPeerGlobalConfiguration"
        self._children_yang_names.add("cPeerGlobalConfiguration")

        self.ccallhistorytable = CISCODIALCONTROLMIB.Ccallhistorytable()
        self.ccallhistorytable.parent = self
        self._children_name_map["ccallhistorytable"] = "cCallHistoryTable"
        self._children_yang_names.add("cCallHistoryTable")

        self.ccallhistoryiectable = CISCODIALCONTROLMIB.Ccallhistoryiectable()
        self.ccallhistoryiectable.parent = self
        self._children_name_map["ccallhistoryiectable"] = "cCallHistoryIecTable"
        self._children_yang_names.add("cCallHistoryIecTable")
        self._segment_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB"


    class Cpeerglobalconfiguration(Entity):
        """
        
        
        .. attribute:: cpeersearchtype
        
        	Specifies the peer search preference based on the type of peers in an universal/integrated port platform.  none      \- both voice and data peers are searched            in same preference. datavoice \- search data peers first. If no data peers            are found, the voice peers are searched. voicedata \- search voice peers first. If no voice peers            are found, the data peers are searched
        	**type**\:  :py:class:`Cpeersearchtype <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Cpeerglobalconfiguration.Cpeersearchtype>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            super(CISCODIALCONTROLMIB.Cpeerglobalconfiguration, self).__init__()

            self.yang_name = "cPeerGlobalConfiguration"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpeersearchtype', YLeaf(YType.enumeration, 'cPeerSearchType')),
            ])
            self.cpeersearchtype = None
            self._segment_path = lambda: "cPeerGlobalConfiguration"
            self._absolute_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODIALCONTROLMIB.Cpeerglobalconfiguration, ['cpeersearchtype'], name, value)

        class Cpeersearchtype(Enum):
            """
            Cpeersearchtype (Enum Class)

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

            none = Enum.YLeaf(1, "none")

            datavoice = Enum.YLeaf(2, "datavoice")

            voicedata = Enum.YLeaf(3, "voicedata")



    class Ccallhistorytable(Entity):
        """
        A table containing information about specific
        calls to a specific destination.
        
        .. attribute:: ccallhistoryentry
        
        	The information regarding a single Connection
        	**type**\: list of  		 :py:class:`Ccallhistoryentry <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            super(CISCODIALCONTROLMIB.Ccallhistorytable, self).__init__()

            self.yang_name = "cCallHistoryTable"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cCallHistoryEntry", ("ccallhistoryentry", CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry))])
            self._leafs = OrderedDict()

            self.ccallhistoryentry = YList(self)
            self._segment_path = lambda: "cCallHistoryTable"
            self._absolute_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODIALCONTROLMIB.Ccallhistorytable, [], name, value)


        class Ccallhistoryentry(Entity):
            """
            The information regarding a single Connection.
            
            .. attribute:: ccallhistoryindex  (key)
            
            	A monotonically increasing integer for the sole purpose of indexing call disconnection events.  When it reaches the  maximum value, an extremely unlikely event, the agent wraps  the value back to 1 and may flush existing entries
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccallhistorysetuptime
            
            	The value of sysUpTime when the call setup was started. This will be useful for an NMS to sort the call history entry with call setup time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network. The value of this object is the same as callActiveSetupTime in the callActiveTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorypeeraddress
            
            	The number this call was connected to. If the number is not available, then it will have a length of zero
            	**type**\: str
            
            .. attribute:: ccallhistorypeersubaddress
            
            	The subaddress this call was connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\: str
            
            .. attribute:: ccallhistorypeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorypeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorylogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call. If the ifIndex value is unknown, the value of this object  will be zero. For an IP call, the value will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccallhistorydisconnectcause
            
            	The encoded network cause value associated with this call.  The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\: str
            
            	**length:** 0..4
            
            .. attribute:: ccallhistorydisconnecttext
            
            	ASCII text describing the reason for call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause
            	**type**\: str
            
            .. attribute:: ccallhistoryconnecttime
            
            	The value of sysUpTime when the call was connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorydisconnecttime
            
            	The value of sysUpTime when the call was disconnected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorycallorigin
            
            	The call origin
            	**type**\:  :py:class:`Ccallhistorycallorigin <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry.Ccallhistorycallorigin>`
            
            .. attribute:: ccallhistorychargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryinfotype
            
            	The information type for this call
            	**type**\:  :py:class:`Ccallhistoryinfotype <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryinfotype>`
            
            .. attribute:: ccallhistorytransmitpackets
            
            	The number of packets which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistorytransmitbytes
            
            	The number of bytes which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryreceivepackets
            
            	The number of packets which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryreceivebytes
            
            	The number of bytes which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccallhistoryreleasesource
            
            	Originator of the call release
            	**type**\:  :py:class:`Ccallhistoryreleasesource <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryreleasesource>`
            
            	**status**\: deprecated
            
            .. attribute:: ccallhistoryreleasesrc
            
            	Originator of the call release. Indicates the source of  the call release as follows \:  1) callingPartyInPstn \: Calling party in PSTN. 2) callingPartyInVoip \: Calling party in VoIP. 3) calledPartyInPstn \: Called party in PSTN. 4) calledPartyInVoip \: Called party in VoIP. 5) internalReleaseInPotsLeg \: Due to an internal error     in Telephony call leg. 6) internalReleaseInVoipLeg \: Due to an internal error    in VoIP call leg. 7) internalCallControlApp \: Due to an internal error    in Session Application or Tcl or VXML script originated    release.  8) internalReleaseInVoipAAA \: Due to an internal error    in VoIP AAA module. 9) consoleCommand \: Due to CLI or MML. 10) externalRadiusServer \: Call failed during authorization     , authentication or due to receipt of POD from the      RADIUS server. 11) externalNmsApp \: Due to SNMP request to clear      the call. 12) externalCallControlAgent \: External Call Control Agent     initiated clear. 13) gatekeeper \: Gatekeeper initiated clear due to receipt     of Admission Reject, Disengage Request message. 14) externalGKTMPServer \: External GKTMP server initiated     clear due to receipt of Admission Reject message from     the gatekeeper, triggered by RESPONSE.ARJ message from     the GKTMP server
            	**type**\:  :py:class:`Ccallhistoryreleasesrc <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryreleasesrc>`
            
            

            """

            _prefix = 'CISCO-DIAL-CONTROL-MIB'
            _revision = '2005-05-26'

            def __init__(self):
                super(CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry, self).__init__()

                self.yang_name = "cCallHistoryEntry"
                self.yang_parent_name = "cCallHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccallhistoryindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccallhistoryindex', YLeaf(YType.uint32, 'cCallHistoryIndex')),
                    ('ccallhistorysetuptime', YLeaf(YType.uint32, 'cCallHistorySetupTime')),
                    ('ccallhistorypeeraddress', YLeaf(YType.str, 'cCallHistoryPeerAddress')),
                    ('ccallhistorypeersubaddress', YLeaf(YType.str, 'cCallHistoryPeerSubAddress')),
                    ('ccallhistorypeerid', YLeaf(YType.int32, 'cCallHistoryPeerId')),
                    ('ccallhistorypeerifindex', YLeaf(YType.int32, 'cCallHistoryPeerIfIndex')),
                    ('ccallhistorylogicalifindex', YLeaf(YType.int32, 'cCallHistoryLogicalIfIndex')),
                    ('ccallhistorydisconnectcause', YLeaf(YType.str, 'cCallHistoryDisconnectCause')),
                    ('ccallhistorydisconnecttext', YLeaf(YType.str, 'cCallHistoryDisconnectText')),
                    ('ccallhistoryconnecttime', YLeaf(YType.uint32, 'cCallHistoryConnectTime')),
                    ('ccallhistorydisconnecttime', YLeaf(YType.uint32, 'cCallHistoryDisconnectTime')),
                    ('ccallhistorycallorigin', YLeaf(YType.enumeration, 'cCallHistoryCallOrigin')),
                    ('ccallhistorychargedunits', YLeaf(YType.uint32, 'cCallHistoryChargedUnits')),
                    ('ccallhistoryinfotype', YLeaf(YType.enumeration, 'cCallHistoryInfoType')),
                    ('ccallhistorytransmitpackets', YLeaf(YType.uint32, 'cCallHistoryTransmitPackets')),
                    ('ccallhistorytransmitbytes', YLeaf(YType.uint32, 'cCallHistoryTransmitBytes')),
                    ('ccallhistoryreceivepackets', YLeaf(YType.uint32, 'cCallHistoryReceivePackets')),
                    ('ccallhistoryreceivebytes', YLeaf(YType.uint32, 'cCallHistoryReceiveBytes')),
                    ('ccallhistoryreleasesource', YLeaf(YType.enumeration, 'cCallHistoryReleaseSource')),
                    ('ccallhistoryreleasesrc', YLeaf(YType.enumeration, 'cCallHistoryReleaseSrc')),
                ])
                self.ccallhistoryindex = None
                self.ccallhistorysetuptime = None
                self.ccallhistorypeeraddress = None
                self.ccallhistorypeersubaddress = None
                self.ccallhistorypeerid = None
                self.ccallhistorypeerifindex = None
                self.ccallhistorylogicalifindex = None
                self.ccallhistorydisconnectcause = None
                self.ccallhistorydisconnecttext = None
                self.ccallhistoryconnecttime = None
                self.ccallhistorydisconnecttime = None
                self.ccallhistorycallorigin = None
                self.ccallhistorychargedunits = None
                self.ccallhistoryinfotype = None
                self.ccallhistorytransmitpackets = None
                self.ccallhistorytransmitbytes = None
                self.ccallhistoryreceivepackets = None
                self.ccallhistoryreceivebytes = None
                self.ccallhistoryreleasesource = None
                self.ccallhistoryreleasesrc = None
                self._segment_path = lambda: "cCallHistoryEntry" + "[cCallHistoryIndex='" + str(self.ccallhistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/cCallHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry, ['ccallhistoryindex', 'ccallhistorysetuptime', 'ccallhistorypeeraddress', 'ccallhistorypeersubaddress', 'ccallhistorypeerid', 'ccallhistorypeerifindex', 'ccallhistorylogicalifindex', 'ccallhistorydisconnectcause', 'ccallhistorydisconnecttext', 'ccallhistoryconnecttime', 'ccallhistorydisconnecttime', 'ccallhistorycallorigin', 'ccallhistorychargedunits', 'ccallhistoryinfotype', 'ccallhistorytransmitpackets', 'ccallhistorytransmitbytes', 'ccallhistoryreceivepackets', 'ccallhistoryreceivebytes', 'ccallhistoryreleasesource', 'ccallhistoryreleasesrc'], name, value)

            class Ccallhistorycallorigin(Enum):
                """
                Ccallhistorycallorigin (Enum Class)

                The call origin.

                .. data:: originate = 1

                .. data:: answer = 2

                .. data:: callback = 3

                """

                originate = Enum.YLeaf(1, "originate")

                answer = Enum.YLeaf(2, "answer")

                callback = Enum.YLeaf(3, "callback")


            class Ccallhistoryinfotype(Enum):
                """
                Ccallhistoryinfotype (Enum Class)

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


            class Ccallhistoryreleasesource(Enum):
                """
                Ccallhistoryreleasesource (Enum Class)

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

                callingPartyInPstn = Enum.YLeaf(1, "callingPartyInPstn")

                callingPartyInVoip = Enum.YLeaf(2, "callingPartyInVoip")

                calledPartyInPstn = Enum.YLeaf(3, "calledPartyInPstn")

                calledPartyInVoip = Enum.YLeaf(4, "calledPartyInVoip")

                internalRelease = Enum.YLeaf(5, "internalRelease")

                internalCallControlApp = Enum.YLeaf(6, "internalCallControlApp")

                consoleCommand = Enum.YLeaf(7, "consoleCommand")

                externalRadiusServer = Enum.YLeaf(8, "externalRadiusServer")

                externalNmsApp = Enum.YLeaf(9, "externalNmsApp")

                externalCallControlAgent = Enum.YLeaf(10, "externalCallControlAgent")


            class Ccallhistoryreleasesrc(Enum):
                """
                Ccallhistoryreleasesrc (Enum Class)

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

                callingPartyInPstn = Enum.YLeaf(1, "callingPartyInPstn")

                callingPartyInVoip = Enum.YLeaf(2, "callingPartyInVoip")

                calledPartyInPstn = Enum.YLeaf(3, "calledPartyInPstn")

                calledPartyInVoip = Enum.YLeaf(4, "calledPartyInVoip")

                internalReleaseInPotsLeg = Enum.YLeaf(5, "internalReleaseInPotsLeg")

                internalReleaseInVoipLeg = Enum.YLeaf(6, "internalReleaseInVoipLeg")

                internalCallControlApp = Enum.YLeaf(7, "internalCallControlApp")

                internalReleaseInVoipAAA = Enum.YLeaf(8, "internalReleaseInVoipAAA")

                consoleCommand = Enum.YLeaf(9, "consoleCommand")

                externalRadiusServer = Enum.YLeaf(10, "externalRadiusServer")

                externalNmsApp = Enum.YLeaf(11, "externalNmsApp")

                externalCallControlAgent = Enum.YLeaf(12, "externalCallControlAgent")

                gatekeeper = Enum.YLeaf(13, "gatekeeper")

                externalGKTMPServer = Enum.YLeaf(14, "externalGKTMPServer")



    class Ccallhistoryiectable(Entity):
        """
        This table contains information about Internal Error
        Code(s) (IEC) which caused the call to fail.
        
        .. attribute:: ccallhistoryiecentry
        
        	The IEC information regarding a single call
        	**type**\: list of  		 :py:class:`Ccallhistoryiecentry <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistoryiectable.Ccallhistoryiecentry>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            super(CISCODIALCONTROLMIB.Ccallhistoryiectable, self).__init__()

            self.yang_name = "cCallHistoryIecTable"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cCallHistoryIecEntry", ("ccallhistoryiecentry", CISCODIALCONTROLMIB.Ccallhistoryiectable.Ccallhistoryiecentry))])
            self._leafs = OrderedDict()

            self.ccallhistoryiecentry = YList(self)
            self._segment_path = lambda: "cCallHistoryIecTable"
            self._absolute_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODIALCONTROLMIB.Ccallhistoryiectable, [], name, value)


        class Ccallhistoryiecentry(Entity):
            """
            The IEC information regarding a single call.
            
            .. attribute:: ccallhistoryindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: ccallhistoryiecindex  (key)
            
            	This object is used to index one or more IECs in the context of a single call.  In most cases there will only be one IEC when a call fails.  However, it is possible for the software processing the call to  generate multiple IECs before the call ultimately fails. In that scenario, there will be multiple entries in this table related to a single call (cCallHistoryIndex) and this object will serve to uniquely identify each IEC
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: ccallhistoryiec
            
            	This object reflects the Internal Error Code. The format is a string of dotted decimal numbers composed of the following components\:  Version.Entity.Category.Subsystem.Errorcode.Diagnostic  Each component is defined as follows\: Version     \: The version of IEC software. Entity      \: The network entity that originated               the error. Category    \: The category of the error (eg, software               error, hardware resource unavailable, ...) Subsystem   \: The subsystem in which the error occurred. Errorcode   \: A subsytem\-specific error code. Diagnostic  \: An implementation\-specific diagnostic code
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-DIAL-CONTROL-MIB'
            _revision = '2005-05-26'

            def __init__(self):
                super(CISCODIALCONTROLMIB.Ccallhistoryiectable.Ccallhistoryiecentry, self).__init__()

                self.yang_name = "cCallHistoryIecEntry"
                self.yang_parent_name = "cCallHistoryIecTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccallhistoryindex','ccallhistoryiecindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccallhistoryindex', YLeaf(YType.str, 'cCallHistoryIndex')),
                    ('ccallhistoryiecindex', YLeaf(YType.uint32, 'cCallHistoryIecIndex')),
                    ('ccallhistoryiec', YLeaf(YType.str, 'cCallHistoryIec')),
                ])
                self.ccallhistoryindex = None
                self.ccallhistoryiecindex = None
                self.ccallhistoryiec = None
                self._segment_path = lambda: "cCallHistoryIecEntry" + "[cCallHistoryIndex='" + str(self.ccallhistoryindex) + "']" + "[cCallHistoryIecIndex='" + str(self.ccallhistoryiecindex) + "']"
                self._absolute_path = lambda: "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/cCallHistoryIecTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODIALCONTROLMIB.Ccallhistoryiectable.Ccallhistoryiecentry, ['ccallhistoryindex', 'ccallhistoryiecindex', 'ccallhistoryiec'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCODIALCONTROLMIB()
        return self._top_entity

