""" CISCO_DIAL_CONTROL_MIB 

The MIB module to describe call history information for
demand access and possibly other kinds of interfaces.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoDialControlMib(Entity):
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
        super(CiscoDialControlMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"

        self.ccallhistoryiectable = CiscoDialControlMib.Ccallhistoryiectable()
        self.ccallhistoryiectable.parent = self
        self._children_name_map["ccallhistoryiectable"] = "cCallHistoryIecTable"
        self._children_yang_names.add("cCallHistoryIecTable")

        self.ccallhistorytable = CiscoDialControlMib.Ccallhistorytable()
        self.ccallhistorytable.parent = self
        self._children_name_map["ccallhistorytable"] = "cCallHistoryTable"
        self._children_yang_names.add("cCallHistoryTable")

        self.cpeerglobalconfiguration = CiscoDialControlMib.Cpeerglobalconfiguration()
        self.cpeerglobalconfiguration.parent = self
        self._children_name_map["cpeerglobalconfiguration"] = "cPeerGlobalConfiguration"
        self._children_yang_names.add("cPeerGlobalConfiguration")


    class Cpeerglobalconfiguration(Entity):
        """
        
        
        .. attribute:: cpeersearchtype
        
        	Specifies the peer search preference based on the type of peers in an universal/integrated port platform.  none      \- both voice and data peers are searched            in same preference. datavoice \- search data peers first. If no data peers            are found, the voice peers are searched. voicedata \- search voice peers first. If no voice peers            are found, the data peers are searched
        	**type**\:   :py:class:`Cpeersearchtype <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Cpeerglobalconfiguration.Cpeersearchtype>`
        
        

        """

        _prefix = 'CISCO-DIAL-CONTROL-MIB'
        _revision = '2005-05-26'

        def __init__(self):
            super(CiscoDialControlMib.Cpeerglobalconfiguration, self).__init__()

            self.yang_name = "cPeerGlobalConfiguration"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"

            self.cpeersearchtype = YLeaf(YType.enumeration, "cPeerSearchType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpeersearchtype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDialControlMib.Cpeerglobalconfiguration, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDialControlMib.Cpeerglobalconfiguration, self).__setattr__(name, value)

        class Cpeersearchtype(Enum):
            """
            Cpeersearchtype

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


        def has_data(self):
            return self.cpeersearchtype.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpeersearchtype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPeerGlobalConfiguration" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpeersearchtype.is_set or self.cpeersearchtype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpeersearchtype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPeerSearchType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cPeerSearchType"):
                self.cpeersearchtype = value
                self.cpeersearchtype.value_namespace = name_space
                self.cpeersearchtype.value_namespace_prefix = name_space_prefix


    class Ccallhistorytable(Entity):
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
            super(CiscoDialControlMib.Ccallhistorytable, self).__init__()

            self.yang_name = "cCallHistoryTable"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"

            self.ccallhistoryentry = YList(self)

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
                        super(CiscoDialControlMib.Ccallhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDialControlMib.Ccallhistorytable, self).__setattr__(name, value)


        class Ccallhistoryentry(Entity):
            """
            The information regarding a single Connection.
            
            .. attribute:: ccallhistoryindex  <key>
            
            	A monotonically increasing integer for the sole purpose of indexing call disconnection events.  When it reaches the  maximum value, an extremely unlikely event, the agent wraps  the value back to 1 and may flush existing entries
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccallhistorycallorigin
            
            	The call origin
            	**type**\:   :py:class:`Ccallhistorycallorigin <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.Ccallhistorycallorigin>`
            
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
            	**type**\:   :py:class:`Ccallhistoryinfotype <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryinfotype>`
            
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
            	**type**\:   :py:class:`Ccallhistoryreleasesource <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryreleasesource>`
            
            	**status**\: deprecated
            
            .. attribute:: ccallhistoryreleasesrc
            
            	Originator of the call release. Indicates the source of  the call release as follows \:  1) callingPartyInPstn \: Calling party in PSTN. 2) callingPartyInVoip \: Calling party in VoIP. 3) calledPartyInPstn \: Called party in PSTN. 4) calledPartyInVoip \: Called party in VoIP. 5) internalReleaseInPotsLeg \: Due to an internal error     in Telephony call leg. 6) internalReleaseInVoipLeg \: Due to an internal error    in VoIP call leg. 7) internalCallControlApp \: Due to an internal error    in Session Application or Tcl or VXML script originated    release.  8) internalReleaseInVoipAAA \: Due to an internal error    in VoIP AAA module. 9) consoleCommand \: Due to CLI or MML. 10) externalRadiusServer \: Call failed during authorization     , authentication or due to receipt of POD from the      RADIUS server. 11) externalNmsApp \: Due to SNMP request to clear      the call. 12) externalCallControlAgent \: External Call Control Agent     initiated clear. 13) gatekeeper \: Gatekeeper initiated clear due to receipt     of Admission Reject, Disengage Request message. 14) externalGKTMPServer \: External GKTMP server initiated     clear due to receipt of Admission Reject message from     the gatekeeper, triggered by RESPONSE.ARJ message from     the GKTMP server
            	**type**\:   :py:class:`Ccallhistoryreleasesrc <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.Ccallhistoryreleasesrc>`
            
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
                super(CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry, self).__init__()

                self.yang_name = "cCallHistoryEntry"
                self.yang_parent_name = "cCallHistoryTable"

                self.ccallhistoryindex = YLeaf(YType.uint32, "cCallHistoryIndex")

                self.ccallhistorycallorigin = YLeaf(YType.enumeration, "cCallHistoryCallOrigin")

                self.ccallhistorychargedunits = YLeaf(YType.uint32, "cCallHistoryChargedUnits")

                self.ccallhistoryconnecttime = YLeaf(YType.uint32, "cCallHistoryConnectTime")

                self.ccallhistorydisconnectcause = YLeaf(YType.str, "cCallHistoryDisconnectCause")

                self.ccallhistorydisconnecttext = YLeaf(YType.str, "cCallHistoryDisconnectText")

                self.ccallhistorydisconnecttime = YLeaf(YType.uint32, "cCallHistoryDisconnectTime")

                self.ccallhistoryinfotype = YLeaf(YType.enumeration, "cCallHistoryInfoType")

                self.ccallhistorylogicalifindex = YLeaf(YType.int32, "cCallHistoryLogicalIfIndex")

                self.ccallhistorypeeraddress = YLeaf(YType.str, "cCallHistoryPeerAddress")

                self.ccallhistorypeerid = YLeaf(YType.int32, "cCallHistoryPeerId")

                self.ccallhistorypeerifindex = YLeaf(YType.int32, "cCallHistoryPeerIfIndex")

                self.ccallhistorypeersubaddress = YLeaf(YType.str, "cCallHistoryPeerSubAddress")

                self.ccallhistoryreceivebytes = YLeaf(YType.uint32, "cCallHistoryReceiveBytes")

                self.ccallhistoryreceivepackets = YLeaf(YType.uint32, "cCallHistoryReceivePackets")

                self.ccallhistoryreleasesource = YLeaf(YType.enumeration, "cCallHistoryReleaseSource")

                self.ccallhistoryreleasesrc = YLeaf(YType.enumeration, "cCallHistoryReleaseSrc")

                self.ccallhistorysetuptime = YLeaf(YType.uint32, "cCallHistorySetupTime")

                self.ccallhistorytransmitbytes = YLeaf(YType.uint32, "cCallHistoryTransmitBytes")

                self.ccallhistorytransmitpackets = YLeaf(YType.uint32, "cCallHistoryTransmitPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccallhistoryindex",
                                "ccallhistorycallorigin",
                                "ccallhistorychargedunits",
                                "ccallhistoryconnecttime",
                                "ccallhistorydisconnectcause",
                                "ccallhistorydisconnecttext",
                                "ccallhistorydisconnecttime",
                                "ccallhistoryinfotype",
                                "ccallhistorylogicalifindex",
                                "ccallhistorypeeraddress",
                                "ccallhistorypeerid",
                                "ccallhistorypeerifindex",
                                "ccallhistorypeersubaddress",
                                "ccallhistoryreceivebytes",
                                "ccallhistoryreceivepackets",
                                "ccallhistoryreleasesource",
                                "ccallhistoryreleasesrc",
                                "ccallhistorysetuptime",
                                "ccallhistorytransmitbytes",
                                "ccallhistorytransmitpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry, self).__setattr__(name, value)

            class Ccallhistorycallorigin(Enum):
                """
                Ccallhistorycallorigin

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
                Ccallhistoryinfotype

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
                Ccallhistoryreleasesource

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
                Ccallhistoryreleasesrc

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


            def has_data(self):
                return (
                    self.ccallhistoryindex.is_set or
                    self.ccallhistorycallorigin.is_set or
                    self.ccallhistorychargedunits.is_set or
                    self.ccallhistoryconnecttime.is_set or
                    self.ccallhistorydisconnectcause.is_set or
                    self.ccallhistorydisconnecttext.is_set or
                    self.ccallhistorydisconnecttime.is_set or
                    self.ccallhistoryinfotype.is_set or
                    self.ccallhistorylogicalifindex.is_set or
                    self.ccallhistorypeeraddress.is_set or
                    self.ccallhistorypeerid.is_set or
                    self.ccallhistorypeerifindex.is_set or
                    self.ccallhistorypeersubaddress.is_set or
                    self.ccallhistoryreceivebytes.is_set or
                    self.ccallhistoryreceivepackets.is_set or
                    self.ccallhistoryreleasesource.is_set or
                    self.ccallhistoryreleasesrc.is_set or
                    self.ccallhistorysetuptime.is_set or
                    self.ccallhistorytransmitbytes.is_set or
                    self.ccallhistorytransmitpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccallhistoryindex.yfilter != YFilter.not_set or
                    self.ccallhistorycallorigin.yfilter != YFilter.not_set or
                    self.ccallhistorychargedunits.yfilter != YFilter.not_set or
                    self.ccallhistoryconnecttime.yfilter != YFilter.not_set or
                    self.ccallhistorydisconnectcause.yfilter != YFilter.not_set or
                    self.ccallhistorydisconnecttext.yfilter != YFilter.not_set or
                    self.ccallhistorydisconnecttime.yfilter != YFilter.not_set or
                    self.ccallhistoryinfotype.yfilter != YFilter.not_set or
                    self.ccallhistorylogicalifindex.yfilter != YFilter.not_set or
                    self.ccallhistorypeeraddress.yfilter != YFilter.not_set or
                    self.ccallhistorypeerid.yfilter != YFilter.not_set or
                    self.ccallhistorypeerifindex.yfilter != YFilter.not_set or
                    self.ccallhistorypeersubaddress.yfilter != YFilter.not_set or
                    self.ccallhistoryreceivebytes.yfilter != YFilter.not_set or
                    self.ccallhistoryreceivepackets.yfilter != YFilter.not_set or
                    self.ccallhistoryreleasesource.yfilter != YFilter.not_set or
                    self.ccallhistoryreleasesrc.yfilter != YFilter.not_set or
                    self.ccallhistorysetuptime.yfilter != YFilter.not_set or
                    self.ccallhistorytransmitbytes.yfilter != YFilter.not_set or
                    self.ccallhistorytransmitpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cCallHistoryEntry" + "[cCallHistoryIndex='" + self.ccallhistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/cCallHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccallhistoryindex.is_set or self.ccallhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryindex.get_name_leafdata())
                if (self.ccallhistorycallorigin.is_set or self.ccallhistorycallorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorycallorigin.get_name_leafdata())
                if (self.ccallhistorychargedunits.is_set or self.ccallhistorychargedunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorychargedunits.get_name_leafdata())
                if (self.ccallhistoryconnecttime.is_set or self.ccallhistoryconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryconnecttime.get_name_leafdata())
                if (self.ccallhistorydisconnectcause.is_set or self.ccallhistorydisconnectcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorydisconnectcause.get_name_leafdata())
                if (self.ccallhistorydisconnecttext.is_set or self.ccallhistorydisconnecttext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorydisconnecttext.get_name_leafdata())
                if (self.ccallhistorydisconnecttime.is_set or self.ccallhistorydisconnecttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorydisconnecttime.get_name_leafdata())
                if (self.ccallhistoryinfotype.is_set or self.ccallhistoryinfotype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryinfotype.get_name_leafdata())
                if (self.ccallhistorylogicalifindex.is_set or self.ccallhistorylogicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorylogicalifindex.get_name_leafdata())
                if (self.ccallhistorypeeraddress.is_set or self.ccallhistorypeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorypeeraddress.get_name_leafdata())
                if (self.ccallhistorypeerid.is_set or self.ccallhistorypeerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorypeerid.get_name_leafdata())
                if (self.ccallhistorypeerifindex.is_set or self.ccallhistorypeerifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorypeerifindex.get_name_leafdata())
                if (self.ccallhistorypeersubaddress.is_set or self.ccallhistorypeersubaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorypeersubaddress.get_name_leafdata())
                if (self.ccallhistoryreceivebytes.is_set or self.ccallhistoryreceivebytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryreceivebytes.get_name_leafdata())
                if (self.ccallhistoryreceivepackets.is_set or self.ccallhistoryreceivepackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryreceivepackets.get_name_leafdata())
                if (self.ccallhistoryreleasesource.is_set or self.ccallhistoryreleasesource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryreleasesource.get_name_leafdata())
                if (self.ccallhistoryreleasesrc.is_set or self.ccallhistoryreleasesrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryreleasesrc.get_name_leafdata())
                if (self.ccallhistorysetuptime.is_set or self.ccallhistorysetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorysetuptime.get_name_leafdata())
                if (self.ccallhistorytransmitbytes.is_set or self.ccallhistorytransmitbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorytransmitbytes.get_name_leafdata())
                if (self.ccallhistorytransmitpackets.is_set or self.ccallhistorytransmitpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistorytransmitpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cCallHistoryIndex" or name == "cCallHistoryCallOrigin" or name == "cCallHistoryChargedUnits" or name == "cCallHistoryConnectTime" or name == "cCallHistoryDisconnectCause" or name == "cCallHistoryDisconnectText" or name == "cCallHistoryDisconnectTime" or name == "cCallHistoryInfoType" or name == "cCallHistoryLogicalIfIndex" or name == "cCallHistoryPeerAddress" or name == "cCallHistoryPeerId" or name == "cCallHistoryPeerIfIndex" or name == "cCallHistoryPeerSubAddress" or name == "cCallHistoryReceiveBytes" or name == "cCallHistoryReceivePackets" or name == "cCallHistoryReleaseSource" or name == "cCallHistoryReleaseSrc" or name == "cCallHistorySetupTime" or name == "cCallHistoryTransmitBytes" or name == "cCallHistoryTransmitPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cCallHistoryIndex"):
                    self.ccallhistoryindex = value
                    self.ccallhistoryindex.value_namespace = name_space
                    self.ccallhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryCallOrigin"):
                    self.ccallhistorycallorigin = value
                    self.ccallhistorycallorigin.value_namespace = name_space
                    self.ccallhistorycallorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryChargedUnits"):
                    self.ccallhistorychargedunits = value
                    self.ccallhistorychargedunits.value_namespace = name_space
                    self.ccallhistorychargedunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryConnectTime"):
                    self.ccallhistoryconnecttime = value
                    self.ccallhistoryconnecttime.value_namespace = name_space
                    self.ccallhistoryconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryDisconnectCause"):
                    self.ccallhistorydisconnectcause = value
                    self.ccallhistorydisconnectcause.value_namespace = name_space
                    self.ccallhistorydisconnectcause.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryDisconnectText"):
                    self.ccallhistorydisconnecttext = value
                    self.ccallhistorydisconnecttext.value_namespace = name_space
                    self.ccallhistorydisconnecttext.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryDisconnectTime"):
                    self.ccallhistorydisconnecttime = value
                    self.ccallhistorydisconnecttime.value_namespace = name_space
                    self.ccallhistorydisconnecttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryInfoType"):
                    self.ccallhistoryinfotype = value
                    self.ccallhistoryinfotype.value_namespace = name_space
                    self.ccallhistoryinfotype.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryLogicalIfIndex"):
                    self.ccallhistorylogicalifindex = value
                    self.ccallhistorylogicalifindex.value_namespace = name_space
                    self.ccallhistorylogicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryPeerAddress"):
                    self.ccallhistorypeeraddress = value
                    self.ccallhistorypeeraddress.value_namespace = name_space
                    self.ccallhistorypeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryPeerId"):
                    self.ccallhistorypeerid = value
                    self.ccallhistorypeerid.value_namespace = name_space
                    self.ccallhistorypeerid.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryPeerIfIndex"):
                    self.ccallhistorypeerifindex = value
                    self.ccallhistorypeerifindex.value_namespace = name_space
                    self.ccallhistorypeerifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryPeerSubAddress"):
                    self.ccallhistorypeersubaddress = value
                    self.ccallhistorypeersubaddress.value_namespace = name_space
                    self.ccallhistorypeersubaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryReceiveBytes"):
                    self.ccallhistoryreceivebytes = value
                    self.ccallhistoryreceivebytes.value_namespace = name_space
                    self.ccallhistoryreceivebytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryReceivePackets"):
                    self.ccallhistoryreceivepackets = value
                    self.ccallhistoryreceivepackets.value_namespace = name_space
                    self.ccallhistoryreceivepackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryReleaseSource"):
                    self.ccallhistoryreleasesource = value
                    self.ccallhistoryreleasesource.value_namespace = name_space
                    self.ccallhistoryreleasesource.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryReleaseSrc"):
                    self.ccallhistoryreleasesrc = value
                    self.ccallhistoryreleasesrc.value_namespace = name_space
                    self.ccallhistoryreleasesrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistorySetupTime"):
                    self.ccallhistorysetuptime = value
                    self.ccallhistorysetuptime.value_namespace = name_space
                    self.ccallhistorysetuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryTransmitBytes"):
                    self.ccallhistorytransmitbytes = value
                    self.ccallhistorytransmitbytes.value_namespace = name_space
                    self.ccallhistorytransmitbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryTransmitPackets"):
                    self.ccallhistorytransmitpackets = value
                    self.ccallhistorytransmitpackets.value_namespace = name_space
                    self.ccallhistorytransmitpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccallhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccallhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cCallHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cCallHistoryEntry"):
                for c in self.ccallhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccallhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cCallHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ccallhistoryiectable(Entity):
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
            super(CiscoDialControlMib.Ccallhistoryiectable, self).__init__()

            self.yang_name = "cCallHistoryIecTable"
            self.yang_parent_name = "CISCO-DIAL-CONTROL-MIB"

            self.ccallhistoryiecentry = YList(self)

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
                        super(CiscoDialControlMib.Ccallhistoryiectable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDialControlMib.Ccallhistoryiectable, self).__setattr__(name, value)


        class Ccallhistoryiecentry(Entity):
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
                super(CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry, self).__init__()

                self.yang_name = "cCallHistoryIecEntry"
                self.yang_parent_name = "cCallHistoryIecTable"

                self.ccallhistoryindex = YLeaf(YType.str, "cCallHistoryIndex")

                self.ccallhistoryiecindex = YLeaf(YType.uint32, "cCallHistoryIecIndex")

                self.ccallhistoryiec = YLeaf(YType.str, "cCallHistoryIec")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccallhistoryindex",
                                "ccallhistoryiecindex",
                                "ccallhistoryiec") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccallhistoryindex.is_set or
                    self.ccallhistoryiecindex.is_set or
                    self.ccallhistoryiec.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccallhistoryindex.yfilter != YFilter.not_set or
                    self.ccallhistoryiecindex.yfilter != YFilter.not_set or
                    self.ccallhistoryiec.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cCallHistoryIecEntry" + "[cCallHistoryIndex='" + self.ccallhistoryindex.get() + "']" + "[cCallHistoryIecIndex='" + self.ccallhistoryiecindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/cCallHistoryIecTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccallhistoryindex.is_set or self.ccallhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryindex.get_name_leafdata())
                if (self.ccallhistoryiecindex.is_set or self.ccallhistoryiecindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryiecindex.get_name_leafdata())
                if (self.ccallhistoryiec.is_set or self.ccallhistoryiec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryiec.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cCallHistoryIndex" or name == "cCallHistoryIecIndex" or name == "cCallHistoryIec"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cCallHistoryIndex"):
                    self.ccallhistoryindex = value
                    self.ccallhistoryindex.value_namespace = name_space
                    self.ccallhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryIecIndex"):
                    self.ccallhistoryiecindex = value
                    self.ccallhistoryiecindex.value_namespace = name_space
                    self.ccallhistoryiecindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cCallHistoryIec"):
                    self.ccallhistoryiec = value
                    self.ccallhistoryiec.value_namespace = name_space
                    self.ccallhistoryiec.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccallhistoryiecentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccallhistoryiecentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cCallHistoryIecTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cCallHistoryIecEntry"):
                for c in self.ccallhistoryiecentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccallhistoryiecentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cCallHistoryIecEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ccallhistoryiectable is not None and self.ccallhistoryiectable.has_data()) or
            (self.ccallhistorytable is not None and self.ccallhistorytable.has_data()) or
            (self.cpeerglobalconfiguration is not None and self.cpeerglobalconfiguration.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ccallhistoryiectable is not None and self.ccallhistoryiectable.has_operation()) or
            (self.ccallhistorytable is not None and self.ccallhistorytable.has_operation()) or
            (self.cpeerglobalconfiguration is not None and self.cpeerglobalconfiguration.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-DIAL-CONTROL-MIB:CISCO-DIAL-CONTROL-MIB" + path_buffer

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

        if (child_yang_name == "cCallHistoryIecTable"):
            if (self.ccallhistoryiectable is None):
                self.ccallhistoryiectable = CiscoDialControlMib.Ccallhistoryiectable()
                self.ccallhistoryiectable.parent = self
                self._children_name_map["ccallhistoryiectable"] = "cCallHistoryIecTable"
            return self.ccallhistoryiectable

        if (child_yang_name == "cCallHistoryTable"):
            if (self.ccallhistorytable is None):
                self.ccallhistorytable = CiscoDialControlMib.Ccallhistorytable()
                self.ccallhistorytable.parent = self
                self._children_name_map["ccallhistorytable"] = "cCallHistoryTable"
            return self.ccallhistorytable

        if (child_yang_name == "cPeerGlobalConfiguration"):
            if (self.cpeerglobalconfiguration is None):
                self.cpeerglobalconfiguration = CiscoDialControlMib.Cpeerglobalconfiguration()
                self.cpeerglobalconfiguration.parent = self
                self._children_name_map["cpeerglobalconfiguration"] = "cPeerGlobalConfiguration"
            return self.cpeerglobalconfiguration

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cCallHistoryIecTable" or name == "cCallHistoryTable" or name == "cPeerGlobalConfiguration"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoDialControlMib()
        return self._top_entity

