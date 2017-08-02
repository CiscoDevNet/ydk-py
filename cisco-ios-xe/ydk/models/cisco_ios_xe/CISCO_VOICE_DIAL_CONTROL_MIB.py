""" CISCO_VOICE_DIAL_CONTROL_MIB 

This MIB module enhances the IETF Dial Control MIB
(RFC2128) by providing management of voice telephony
peers on both a circuit\-switched telephony network,
and an IP data network.

\*\*\* ABBREVIATIONS, ACRONYMS AND SYMBOLS \*\*\*

GSM    \- Global System for Mobile Communication

AMR\-NB \- Adaptive Multi Rate \- Narrow Band 

iLBC   \- internet Low Bitrate Codec 

KPML   \- Key Press Markup Language

MGCP   \- Media Gateway Control Protocol.

SIP    \- Session Initiation Protocol.

H323   \- One of the voip signalling protocol.

SCCP   \- Skinny Client Control Protocol.

dialpeer \- This represents a configured interface that 
           carries the dial map.  A dialpeer maps the 
           called and calling numbers with the port or 
           IP interface to be used.

License call capacity \- This represents the licensed 
                        maximum call capacity of 
                        the gateway.

iSAC    \-  Internet Speech Audio Codec

RPH    \- Resource Priority Header

DSCP   \- Diffserv Code Points

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cvamrnbrtpencap(Enum):
    """
    Cvamrnbrtpencap

    Represents GSM AMR\-NB codec RTP encapsulation type.

    .. data:: rfc3267 = 1

    """

    rfc3267 = Enum.YLeaf(1, "rfc3267")


class Cvcallconnectiontype(Enum):
    """
    Cvcallconnectiontype

    Call connection represents the connection/association/session

    between two media call end points. Following are the different

    connection types.

    h323       \- h323 protocol.

    sip        \- Session Initiation Protocol.

    mgcp       \- Media Gateway Control Protocol.

    sccp       \- Cisco proprietary Skinny Call Control Protocol.

    multicast  \- multicast call connections.

    cacontrol  \- Call Agent Control.

    telephony  \- telephony signal call connections.

    .. data:: h323 = 1

    .. data:: sip = 2

    .. data:: mgcp = 3

    .. data:: sccp = 4

    .. data:: multicast = 5

    .. data:: cacontrol = 6

    .. data:: telephony = 7

    """

    h323 = Enum.YLeaf(1, "h323")

    sip = Enum.YLeaf(2, "sip")

    mgcp = Enum.YLeaf(3, "mgcp")

    sccp = Enum.YLeaf(4, "sccp")

    multicast = Enum.YLeaf(5, "multicast")

    cacontrol = Enum.YLeaf(6, "cacontrol")

    telephony = Enum.YLeaf(7, "telephony")


class Cvcallvolumestatsintvltype(Enum):
    """
    Cvcallvolumestatsintvltype

    Represents the ids of the stats vlolume table

    Here is what each entry corresponds.

    1 \: Seconds Table\: Here each entry corresponds to a second

    2 \: Minutes Table\: Here each entry corresponds to a minute

    3 \: Hours Table\: Here each entry corresponds to an hour

    .. data:: secondStats = 1

    .. data:: minuteStats = 2

    .. data:: hourStats = 3

    """

    secondStats = Enum.YLeaf(1, "secondStats")

    minuteStats = Enum.YLeaf(2, "minuteStats")

    hourStats = Enum.YLeaf(3, "hourStats")


class Cvcallvolumewmintvltype(Enum):
    """
    Cvcallvolumewmintvltype

    Represents the Id of the watermark table.

    Here is what different values represent

    1 \: Seconds Table\: Here the entries are among last 60 second

    2 \: Minutes Table\: Here the entries are among last 60 minutes

    3 \: Hours Table\: Here the entries are among last 72 Hours

    4 \: Uptime Table\: Here the entries are from last reload/reboot

    .. data:: secondStats = 1

    .. data:: minuteStats = 2

    .. data:: hourStats = 3

    .. data:: fromReloadStats = 4

    """

    secondStats = Enum.YLeaf(1, "secondStats")

    minuteStats = Enum.YLeaf(2, "minuteStats")

    hourStats = Enum.YLeaf(3, "hourStats")

    fromReloadStats = Enum.YLeaf(4, "fromReloadStats")


class Cvilbcframemode(Enum):
    """
    Cvilbcframemode

    This Texatual Convention represents the iLBC codec

    frame modes.  

    The possible values are \:

    frameMode20\: This mode operates at 15.2 kbps and each 

                 frame is packetized in 38 bytes. 

    frameMode30\: This mode operates at 13.33 kbps and each 

                 frame is packetized in 50 bytes.

    .. data:: frameMode20 = 20

    .. data:: frameMode30 = 30

    """

    frameMode20 = Enum.YLeaf(20, "frameMode20")

    frameMode30 = Enum.YLeaf(30, "frameMode30")


class Cvsessionprotocol(Enum):
    """
    Cvsessionprotocol

    Represents a Session Protocol used by Voice calls between a

    local and remote router via the IP backbone.

    other \- none of the following.

    cisco \- cisco proprietary H.323 Lite session protocol.

    sdp   \- Session Description Protocol.

    sip   \- Session Initiation Protocol.

    sccp  \- Skinny Call Control Protocol.

    .. data:: other = 1

    .. data:: cisco = 2

    .. data:: sdp = 3

    .. data:: sip = 4

    .. data:: multicast = 5

    .. data:: sccp = 6

    """

    other = Enum.YLeaf(1, "other")

    cisco = Enum.YLeaf(2, "cisco")

    sdp = Enum.YLeaf(3, "sdp")

    sip = Enum.YLeaf(4, "sip")

    multicast = Enum.YLeaf(5, "multicast")

    sccp = Enum.YLeaf(6, "sccp")


class Cvamrnbbitratemode(Bits):
    """
    Cvamrnbbitratemode

    Represents GSM AMR\-NB bit rate modes.
    
    CodecMode             Bit\-rate (kbps)
    0                     4.75
    1                     5.15
    2                     5.90
    3                     6.70
    4                     7.40
    5                     7.95
    6                     10.2
    7                     12.2
    Keys are:- amrBitRateMode4 , amrBitRateMode5 , amrBitRateMode7 , amrBitRateMode1 , amrBitRateMode6 , amrBitRateMode0 , amrBitRateMode3 , amrBitRateMode2

    """

    def __init__(self):
        super(Cvamrnbbitratemode, self).__init__()


class CiscoVoiceDialControlMib(Entity):
    """
    
    
    .. attribute:: cvactivecallstatstable
    
    	This table represents the active voice calls in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:   :py:class:`Cvactivecallstatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvactivecallstatstable>`
    
    .. attribute:: cvactivecallwmtable
    
    	This table represents high watermarks achieved by active calls in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow  for detailed measurement to be collected
    	**type**\:   :py:class:`Cvactivecallwmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvactivecallwmtable>`
    
    .. attribute:: cvcallactivetable
    
    	This table is the voice extension to the call active table of IETF Dial Control MIB. It contains voice encapsulation call leg information that is derived from the statistics of lower layer telephony interface
    	**type**\:   :py:class:`Cvcallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallactivetable>`
    
    .. attribute:: cvcalldurationstatstable
    
    	This table represents the number of calls below a specific duration in various interval length defined by  the CvCallVolumeStatsIntvlType object.    The specific duration is configurable value of   cvCallDurationStatsThreshold object.  Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:   :py:class:`Cvcalldurationstatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalldurationstatstable>`
    
    .. attribute:: cvcallhistorytable
    
    	This table is the voice extension to the call history table of IETF Dial Control MIB. It contains voice encapsulation call leg information such as voice packet statistics, coder usage and end to end bandwidth of the call leg
    	**type**\:   :py:class:`Cvcallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallhistorytable>`
    
    .. attribute:: cvcalllegratestatstable
    
    	cvCallLegRateStatsTable table represents voice call leg rate measurement in various interval lengths defined by  the CvCallVolumeStatsIntvlType object. Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:   :py:class:`Cvcalllegratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalllegratestatstable>`
    
    .. attribute:: cvcalllegratewmtable
    
    	cvCallLegRateWMTable table represents high watermarks achieved by call\-leg rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:   :py:class:`Cvcalllegratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalllegratewmtable>`
    
    .. attribute:: cvcallratemonitor
    
    	
    	**type**\:   :py:class:`Cvcallratemonitor <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallratemonitor>`
    
    .. attribute:: cvcallratestatstable
    
    	This table represents voice call rate measurement in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:   :py:class:`Cvcallratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallratestatstable>`
    
    .. attribute:: cvcallratewmtable
    
    	This table represents high watermarks achieved by call rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:   :py:class:`Cvcallratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallratewmtable>`
    
    .. attribute:: cvcallvolconntable
    
    	This table represents the number of active call connections for each call connection type in the voice gateway
    	**type**\:   :py:class:`Cvcallvolconntable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvolconntable>`
    
    .. attribute:: cvcallvoliftable
    
    	This table represents the information about the usage of an IP interface in a voice gateway for voice media calls. This table has a sparse\-dependent relationship with   ifTable. There exists an entry in this table,  for each of the  entries in ifTable where ifType  is one of 'ethernetCsmacd' and 'softwareLoopback'
    	**type**\:   :py:class:`Cvcallvoliftable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvoliftable>`
    
    .. attribute:: cvcallvolume
    
    	
    	**type**\:   :py:class:`Cvcallvolume <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvolume>`
    
    .. attribute:: cvcallvolumestatshistory
    
    	
    	**type**\:   :py:class:`Cvcallvolumestatshistory <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvolumestatshistory>`
    
    .. attribute:: cvgatewaycallactive
    
    	
    	**type**\:   :py:class:`Cvgatewaycallactive <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvgatewaycallactive>`
    
    .. attribute:: cvgeneralconfiguration
    
    	
    	**type**\:   :py:class:`Cvgeneralconfiguration <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvgeneralconfiguration>`
    
    .. attribute:: cvpeercfgtable
    
    	The table contains the Voice Generic Peer information that is used to create an ifIndexed row with an appropriate ifType that is associated with the cvPeerCfgType and cvPeerCfgPeerType objects
    	**type**\:   :py:class:`Cvpeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercfgtable>`
    
    .. attribute:: cvpeercommoncfgtable
    
    	The table contains the Voice specific peer common configuration information that is required to accept voice calls or to which it will place them or process the incoming calls
    	**type**\:   :py:class:`Cvpeercommoncfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercommoncfgtable>`
    
    .. attribute:: cvsipmsgratestatstable
    
    	This table represents the SIP message rate measurement in various interval length defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:   :py:class:`Cvsipmsgratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvsipmsgratestatstable>`
    
    .. attribute:: cvsipmsgratewmtable
    
    	This table represents of high watermarks achieved by SIP message rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:   :py:class:`Cvsipmsgratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvsipmsgratewmtable>`
    
    .. attribute:: cvvoicepeercfgtable
    
    	The table contains the Voice over Telephony peer specific information that is required to accept voice calls or to which it will place them or perform various loopback tests via interface
    	**type**\:   :py:class:`Cvvoicepeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoicepeercfgtable>`
    
    .. attribute:: cvvoipcallactivetable
    
    	This table is the VoIP extension to the call active table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\:   :py:class:`Cvvoipcallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoipcallactivetable>`
    
    .. attribute:: cvvoipcallhistorytable
    
    	This table is the VoIP extension to the call history table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\:   :py:class:`Cvvoipcallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoipcallhistorytable>`
    
    .. attribute:: cvvoippeercfgtable
    
    	The table contains the Voice over IP (VoIP) peer specific information that is required to accept voice calls or to which it will place them via IP backbone with the specified session protocol in cvVoIPPeerCfgSessionProtocol
    	**type**\:   :py:class:`Cvvoippeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable>`
    
    

    """

    _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
    _revision = '2012-05-15'

    def __init__(self):
        super(CiscoVoiceDialControlMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

        self.cvactivecallstatstable = CiscoVoiceDialControlMib.Cvactivecallstatstable()
        self.cvactivecallstatstable.parent = self
        self._children_name_map["cvactivecallstatstable"] = "cvActiveCallStatsTable"
        self._children_yang_names.add("cvActiveCallStatsTable")

        self.cvactivecallwmtable = CiscoVoiceDialControlMib.Cvactivecallwmtable()
        self.cvactivecallwmtable.parent = self
        self._children_name_map["cvactivecallwmtable"] = "cvActiveCallWMTable"
        self._children_yang_names.add("cvActiveCallWMTable")

        self.cvcallactivetable = CiscoVoiceDialControlMib.Cvcallactivetable()
        self.cvcallactivetable.parent = self
        self._children_name_map["cvcallactivetable"] = "cvCallActiveTable"
        self._children_yang_names.add("cvCallActiveTable")

        self.cvcalldurationstatstable = CiscoVoiceDialControlMib.Cvcalldurationstatstable()
        self.cvcalldurationstatstable.parent = self
        self._children_name_map["cvcalldurationstatstable"] = "cvCallDurationStatsTable"
        self._children_yang_names.add("cvCallDurationStatsTable")

        self.cvcallhistorytable = CiscoVoiceDialControlMib.Cvcallhistorytable()
        self.cvcallhistorytable.parent = self
        self._children_name_map["cvcallhistorytable"] = "cvCallHistoryTable"
        self._children_yang_names.add("cvCallHistoryTable")

        self.cvcalllegratestatstable = CiscoVoiceDialControlMib.Cvcalllegratestatstable()
        self.cvcalllegratestatstable.parent = self
        self._children_name_map["cvcalllegratestatstable"] = "cvCallLegRateStatsTable"
        self._children_yang_names.add("cvCallLegRateStatsTable")

        self.cvcalllegratewmtable = CiscoVoiceDialControlMib.Cvcalllegratewmtable()
        self.cvcalllegratewmtable.parent = self
        self._children_name_map["cvcalllegratewmtable"] = "cvCallLegRateWMTable"
        self._children_yang_names.add("cvCallLegRateWMTable")

        self.cvcallratemonitor = CiscoVoiceDialControlMib.Cvcallratemonitor()
        self.cvcallratemonitor.parent = self
        self._children_name_map["cvcallratemonitor"] = "cvCallRateMonitor"
        self._children_yang_names.add("cvCallRateMonitor")

        self.cvcallratestatstable = CiscoVoiceDialControlMib.Cvcallratestatstable()
        self.cvcallratestatstable.parent = self
        self._children_name_map["cvcallratestatstable"] = "cvCallRateStatsTable"
        self._children_yang_names.add("cvCallRateStatsTable")

        self.cvcallratewmtable = CiscoVoiceDialControlMib.Cvcallratewmtable()
        self.cvcallratewmtable.parent = self
        self._children_name_map["cvcallratewmtable"] = "cvCallRateWMTable"
        self._children_yang_names.add("cvCallRateWMTable")

        self.cvcallvolconntable = CiscoVoiceDialControlMib.Cvcallvolconntable()
        self.cvcallvolconntable.parent = self
        self._children_name_map["cvcallvolconntable"] = "cvCallVolConnTable"
        self._children_yang_names.add("cvCallVolConnTable")

        self.cvcallvoliftable = CiscoVoiceDialControlMib.Cvcallvoliftable()
        self.cvcallvoliftable.parent = self
        self._children_name_map["cvcallvoliftable"] = "cvCallVolIfTable"
        self._children_yang_names.add("cvCallVolIfTable")

        self.cvcallvolume = CiscoVoiceDialControlMib.Cvcallvolume()
        self.cvcallvolume.parent = self
        self._children_name_map["cvcallvolume"] = "cvCallVolume"
        self._children_yang_names.add("cvCallVolume")

        self.cvcallvolumestatshistory = CiscoVoiceDialControlMib.Cvcallvolumestatshistory()
        self.cvcallvolumestatshistory.parent = self
        self._children_name_map["cvcallvolumestatshistory"] = "cvCallVolumeStatsHistory"
        self._children_yang_names.add("cvCallVolumeStatsHistory")

        self.cvgatewaycallactive = CiscoVoiceDialControlMib.Cvgatewaycallactive()
        self.cvgatewaycallactive.parent = self
        self._children_name_map["cvgatewaycallactive"] = "cvGatewayCallActive"
        self._children_yang_names.add("cvGatewayCallActive")

        self.cvgeneralconfiguration = CiscoVoiceDialControlMib.Cvgeneralconfiguration()
        self.cvgeneralconfiguration.parent = self
        self._children_name_map["cvgeneralconfiguration"] = "cvGeneralConfiguration"
        self._children_yang_names.add("cvGeneralConfiguration")

        self.cvpeercfgtable = CiscoVoiceDialControlMib.Cvpeercfgtable()
        self.cvpeercfgtable.parent = self
        self._children_name_map["cvpeercfgtable"] = "cvPeerCfgTable"
        self._children_yang_names.add("cvPeerCfgTable")

        self.cvpeercommoncfgtable = CiscoVoiceDialControlMib.Cvpeercommoncfgtable()
        self.cvpeercommoncfgtable.parent = self
        self._children_name_map["cvpeercommoncfgtable"] = "cvPeerCommonCfgTable"
        self._children_yang_names.add("cvPeerCommonCfgTable")

        self.cvsipmsgratestatstable = CiscoVoiceDialControlMib.Cvsipmsgratestatstable()
        self.cvsipmsgratestatstable.parent = self
        self._children_name_map["cvsipmsgratestatstable"] = "cvSipMsgRateStatsTable"
        self._children_yang_names.add("cvSipMsgRateStatsTable")

        self.cvsipmsgratewmtable = CiscoVoiceDialControlMib.Cvsipmsgratewmtable()
        self.cvsipmsgratewmtable.parent = self
        self._children_name_map["cvsipmsgratewmtable"] = "cvSipMsgRateWMTable"
        self._children_yang_names.add("cvSipMsgRateWMTable")

        self.cvvoicepeercfgtable = CiscoVoiceDialControlMib.Cvvoicepeercfgtable()
        self.cvvoicepeercfgtable.parent = self
        self._children_name_map["cvvoicepeercfgtable"] = "cvVoicePeerCfgTable"
        self._children_yang_names.add("cvVoicePeerCfgTable")

        self.cvvoipcallactivetable = CiscoVoiceDialControlMib.Cvvoipcallactivetable()
        self.cvvoipcallactivetable.parent = self
        self._children_name_map["cvvoipcallactivetable"] = "cvVoIPCallActiveTable"
        self._children_yang_names.add("cvVoIPCallActiveTable")

        self.cvvoipcallhistorytable = CiscoVoiceDialControlMib.Cvvoipcallhistorytable()
        self.cvvoipcallhistorytable.parent = self
        self._children_name_map["cvvoipcallhistorytable"] = "cvVoIPCallHistoryTable"
        self._children_yang_names.add("cvVoIPCallHistoryTable")

        self.cvvoippeercfgtable = CiscoVoiceDialControlMib.Cvvoippeercfgtable()
        self.cvvoippeercfgtable.parent = self
        self._children_name_map["cvvoippeercfgtable"] = "cvVoIPPeerCfgTable"
        self._children_yang_names.add("cvVoIPPeerCfgTable")


    class Cvgeneralconfiguration(Entity):
        """
        
        
        .. attribute:: cvgeneraldscppolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for a RPH to DSCP mapping violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when a RPH to DSCP violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgDSCPPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\:  bool
        
        .. attribute:: cvgeneralfallbacknotificationenable
        
        	This object indicates whether cvdcFallbackNotification traps should be generated for fallback. If the value of this object is 'true', cvdcFallbackNotification traps will be generated for all voice over IP peers
        	**type**\:  bool
        
        .. attribute:: cvgeneralmediapolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for Media violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when media violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgMediaPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\:  bool
        
        .. attribute:: cvgeneralpoorqovnotificationenable
        
        	This object indicates whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for a poor quality of voice calls.  If the value of this object is 'true', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated for all voice over IP peers when a poor quality of voice call condition is detected after the voice gateway call disconnection.  If the value of this object is 'false', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated only for calls for which the cvVoIPPeerCfgPoorQoVNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvgeneralconfiguration, self).__init__()

            self.yang_name = "cvGeneralConfiguration"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvgeneraldscppolicynotificationenable = YLeaf(YType.boolean, "cvGeneralDSCPPolicyNotificationEnable")

            self.cvgeneralfallbacknotificationenable = YLeaf(YType.boolean, "cvGeneralFallbackNotificationEnable")

            self.cvgeneralmediapolicynotificationenable = YLeaf(YType.boolean, "cvGeneralMediaPolicyNotificationEnable")

            self.cvgeneralpoorqovnotificationenable = YLeaf(YType.boolean, "cvGeneralPoorQoVNotificationEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvgeneraldscppolicynotificationenable",
                            "cvgeneralfallbacknotificationenable",
                            "cvgeneralmediapolicynotificationenable",
                            "cvgeneralpoorqovnotificationenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceDialControlMib.Cvgeneralconfiguration, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvgeneralconfiguration, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvgeneraldscppolicynotificationenable.is_set or
                self.cvgeneralfallbacknotificationenable.is_set or
                self.cvgeneralmediapolicynotificationenable.is_set or
                self.cvgeneralpoorqovnotificationenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvgeneraldscppolicynotificationenable.yfilter != YFilter.not_set or
                self.cvgeneralfallbacknotificationenable.yfilter != YFilter.not_set or
                self.cvgeneralmediapolicynotificationenable.yfilter != YFilter.not_set or
                self.cvgeneralpoorqovnotificationenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvGeneralConfiguration" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvgeneraldscppolicynotificationenable.is_set or self.cvgeneraldscppolicynotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvgeneraldscppolicynotificationenable.get_name_leafdata())
            if (self.cvgeneralfallbacknotificationenable.is_set or self.cvgeneralfallbacknotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvgeneralfallbacknotificationenable.get_name_leafdata())
            if (self.cvgeneralmediapolicynotificationenable.is_set or self.cvgeneralmediapolicynotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvgeneralmediapolicynotificationenable.get_name_leafdata())
            if (self.cvgeneralpoorqovnotificationenable.is_set or self.cvgeneralpoorqovnotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvgeneralpoorqovnotificationenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvGeneralDSCPPolicyNotificationEnable" or name == "cvGeneralFallbackNotificationEnable" or name == "cvGeneralMediaPolicyNotificationEnable" or name == "cvGeneralPoorQoVNotificationEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvGeneralDSCPPolicyNotificationEnable"):
                self.cvgeneraldscppolicynotificationenable = value
                self.cvgeneraldscppolicynotificationenable.value_namespace = name_space
                self.cvgeneraldscppolicynotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvGeneralFallbackNotificationEnable"):
                self.cvgeneralfallbacknotificationenable = value
                self.cvgeneralfallbacknotificationenable.value_namespace = name_space
                self.cvgeneralfallbacknotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvGeneralMediaPolicyNotificationEnable"):
                self.cvgeneralmediapolicynotificationenable = value
                self.cvgeneralmediapolicynotificationenable.value_namespace = name_space
                self.cvgeneralmediapolicynotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvGeneralPoorQoVNotificationEnable"):
                self.cvgeneralpoorqovnotificationenable = value
                self.cvgeneralpoorqovnotificationenable.value_namespace = name_space
                self.cvgeneralpoorqovnotificationenable.value_namespace_prefix = name_space_prefix


    class Cvgatewaycallactive(Entity):
        """
        
        
        .. attribute:: cvcallactiveds0s
        
        	The current number of DS0 interfaces used for the active calls
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: interfaces
        
        .. attribute:: cvcallactiveds0shighnotifyenable
        
        	Specifies whether or not cvdcActiveDS0sHighNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sHighNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sHighNotification          generation is disabled
        	**type**\:  bool
        
        .. attribute:: cvcallactiveds0shighthreshold
        
        	A high threshold used to determine when to generate the cvdcActiveDS0sHighNotification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\:  int
        
        	**range:** 0..100
        
        	**units**\: percent
        
        .. attribute:: cvcallactiveds0slownotifyenable
        
        	Specifies whether or not cvdcActiveDS0sLowNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sLowNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sLowNotification          generation is disabled
        	**type**\:  bool
        
        .. attribute:: cvcallactiveds0slowthreshold
        
        	A low threshold used to determine when to generate the cvdcActiveDS0sLowNotification notification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\:  int
        
        	**range:** 0..100
        
        	**units**\: percent
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvgatewaycallactive, self).__init__()

            self.yang_name = "cvGatewayCallActive"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallactiveds0s = YLeaf(YType.uint32, "cvCallActiveDS0s")

            self.cvcallactiveds0shighnotifyenable = YLeaf(YType.boolean, "cvCallActiveDS0sHighNotifyEnable")

            self.cvcallactiveds0shighthreshold = YLeaf(YType.uint32, "cvCallActiveDS0sHighThreshold")

            self.cvcallactiveds0slownotifyenable = YLeaf(YType.boolean, "cvCallActiveDS0sLowNotifyEnable")

            self.cvcallactiveds0slowthreshold = YLeaf(YType.uint32, "cvCallActiveDS0sLowThreshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvcallactiveds0s",
                            "cvcallactiveds0shighnotifyenable",
                            "cvcallactiveds0shighthreshold",
                            "cvcallactiveds0slownotifyenable",
                            "cvcallactiveds0slowthreshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceDialControlMib.Cvgatewaycallactive, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvgatewaycallactive, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvcallactiveds0s.is_set or
                self.cvcallactiveds0shighnotifyenable.is_set or
                self.cvcallactiveds0shighthreshold.is_set or
                self.cvcallactiveds0slownotifyenable.is_set or
                self.cvcallactiveds0slowthreshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvcallactiveds0s.yfilter != YFilter.not_set or
                self.cvcallactiveds0shighnotifyenable.yfilter != YFilter.not_set or
                self.cvcallactiveds0shighthreshold.yfilter != YFilter.not_set or
                self.cvcallactiveds0slownotifyenable.yfilter != YFilter.not_set or
                self.cvcallactiveds0slowthreshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvGatewayCallActive" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvcallactiveds0s.is_set or self.cvcallactiveds0s.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallactiveds0s.get_name_leafdata())
            if (self.cvcallactiveds0shighnotifyenable.is_set or self.cvcallactiveds0shighnotifyenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallactiveds0shighnotifyenable.get_name_leafdata())
            if (self.cvcallactiveds0shighthreshold.is_set or self.cvcallactiveds0shighthreshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallactiveds0shighthreshold.get_name_leafdata())
            if (self.cvcallactiveds0slownotifyenable.is_set or self.cvcallactiveds0slownotifyenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallactiveds0slownotifyenable.get_name_leafdata())
            if (self.cvcallactiveds0slowthreshold.is_set or self.cvcallactiveds0slowthreshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallactiveds0slowthreshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallActiveDS0s" or name == "cvCallActiveDS0sHighNotifyEnable" or name == "cvCallActiveDS0sHighThreshold" or name == "cvCallActiveDS0sLowNotifyEnable" or name == "cvCallActiveDS0sLowThreshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvCallActiveDS0s"):
                self.cvcallactiveds0s = value
                self.cvcallactiveds0s.value_namespace = name_space
                self.cvcallactiveds0s.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallActiveDS0sHighNotifyEnable"):
                self.cvcallactiveds0shighnotifyenable = value
                self.cvcallactiveds0shighnotifyenable.value_namespace = name_space
                self.cvcallactiveds0shighnotifyenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallActiveDS0sHighThreshold"):
                self.cvcallactiveds0shighthreshold = value
                self.cvcallactiveds0shighthreshold.value_namespace = name_space
                self.cvcallactiveds0shighthreshold.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallActiveDS0sLowNotifyEnable"):
                self.cvcallactiveds0slownotifyenable = value
                self.cvcallactiveds0slownotifyenable.value_namespace = name_space
                self.cvcallactiveds0slownotifyenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallActiveDS0sLowThreshold"):
                self.cvcallactiveds0slowthreshold = value
                self.cvcallactiveds0slowthreshold.value_namespace = name_space
                self.cvcallactiveds0slowthreshold.value_namespace_prefix = name_space_prefix


    class Cvcallvolume(Entity):
        """
        
        
        .. attribute:: cvcallvolconnmaxcallconnectionlicenese
        
        	This object represents the licensed call capacity for a voice gateway.  If the value is 0, no  licensing is done and the gateway can be  accomodate as many calls depending on its capability
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallvolconntotalactiveconnections
        
        	This object represents the total number of active call legs in the voice gateway
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallvolume, self).__init__()

            self.yang_name = "cvCallVolume"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallvolconnmaxcallconnectionlicenese = YLeaf(YType.uint32, "cvCallVolConnMaxCallConnectionLicenese")

            self.cvcallvolconntotalactiveconnections = YLeaf(YType.uint32, "cvCallVolConnTotalActiveConnections")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvcallvolconnmaxcallconnectionlicenese",
                            "cvcallvolconntotalactiveconnections") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceDialControlMib.Cvcallvolume, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallvolume, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvcallvolconnmaxcallconnectionlicenese.is_set or
                self.cvcallvolconntotalactiveconnections.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvcallvolconnmaxcallconnectionlicenese.yfilter != YFilter.not_set or
                self.cvcallvolconntotalactiveconnections.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallVolume" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvcallvolconnmaxcallconnectionlicenese.is_set or self.cvcallvolconnmaxcallconnectionlicenese.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallvolconnmaxcallconnectionlicenese.get_name_leafdata())
            if (self.cvcallvolconntotalactiveconnections.is_set or self.cvcallvolconntotalactiveconnections.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallvolconntotalactiveconnections.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallVolConnMaxCallConnectionLicenese" or name == "cvCallVolConnTotalActiveConnections"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvCallVolConnMaxCallConnectionLicenese"):
                self.cvcallvolconnmaxcallconnectionlicenese = value
                self.cvcallvolconnmaxcallconnectionlicenese.value_namespace = name_space
                self.cvcallvolconnmaxcallconnectionlicenese.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallVolConnTotalActiveConnections"):
                self.cvcallvolconntotalactiveconnections = value
                self.cvcallvolconntotalactiveconnections.value_namespace = name_space
                self.cvcallvolconntotalactiveconnections.value_namespace_prefix = name_space_prefix


    class Cvcallratemonitor(Entity):
        """
        
        
        .. attribute:: cvcallrate
        
        	This object represents the total number of calls handled by the gateway during the  monitored time
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallratehiwatermark
        
        	This object represents the high water mark for the number of calls handled by the  gateway in an unit interval of  cvCallRateMonitorTime, from the time  the call\-monitoring is enabled
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallratemonitorenable
        
        	This object represents the state of call\-monitoring. A value of 'true' indicates that call\-monitoring  is enabled.  A value of 'false' indicates that  call\-monitoring is disabled
        	**type**\:  bool
        
        .. attribute:: cvcallratemonitortime
        
        	This object represents the interval for which the gateway monitors the call\-rate
        	**type**\:  int
        
        	**range:** 1..12
        
        	**units**\: five seconds
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallratemonitor, self).__init__()

            self.yang_name = "cvCallRateMonitor"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallrate = YLeaf(YType.uint32, "cvCallRate")

            self.cvcallratehiwatermark = YLeaf(YType.uint32, "cvCallRateHiWaterMark")

            self.cvcallratemonitorenable = YLeaf(YType.boolean, "cvCallRateMonitorEnable")

            self.cvcallratemonitortime = YLeaf(YType.uint32, "cvCallRateMonitorTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvcallrate",
                            "cvcallratehiwatermark",
                            "cvcallratemonitorenable",
                            "cvcallratemonitortime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceDialControlMib.Cvcallratemonitor, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallratemonitor, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvcallrate.is_set or
                self.cvcallratehiwatermark.is_set or
                self.cvcallratemonitorenable.is_set or
                self.cvcallratemonitortime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvcallrate.yfilter != YFilter.not_set or
                self.cvcallratehiwatermark.yfilter != YFilter.not_set or
                self.cvcallratemonitorenable.yfilter != YFilter.not_set or
                self.cvcallratemonitortime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallRateMonitor" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvcallrate.is_set or self.cvcallrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallrate.get_name_leafdata())
            if (self.cvcallratehiwatermark.is_set or self.cvcallratehiwatermark.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallratehiwatermark.get_name_leafdata())
            if (self.cvcallratemonitorenable.is_set or self.cvcallratemonitorenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallratemonitorenable.get_name_leafdata())
            if (self.cvcallratemonitortime.is_set or self.cvcallratemonitortime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallratemonitortime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallRate" or name == "cvCallRateHiWaterMark" or name == "cvCallRateMonitorEnable" or name == "cvCallRateMonitorTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvCallRate"):
                self.cvcallrate = value
                self.cvcallrate.value_namespace = name_space
                self.cvcallrate.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallRateHiWaterMark"):
                self.cvcallratehiwatermark = value
                self.cvcallratehiwatermark.value_namespace = name_space
                self.cvcallratehiwatermark.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallRateMonitorEnable"):
                self.cvcallratemonitorenable = value
                self.cvcallratemonitorenable.value_namespace = name_space
                self.cvcallratemonitorenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallRateMonitorTime"):
                self.cvcallratemonitortime = value
                self.cvcallratemonitortime.value_namespace = name_space
                self.cvcallratemonitortime.value_namespace_prefix = name_space_prefix


    class Cvcallvolumestatshistory(Entity):
        """
        
        
        .. attribute:: cvcalldurationstatsthreshold
        
        	This Object specifies the thresold duration in seconds. cvCallDurationStatsTable will monitor all the calls below this  threshold.  Decresing the value of the threshold will reset this table
        	**type**\:  int
        
        	**range:** 1..3600
        
        	**units**\: seconds
        
        .. attribute:: cvcallvolumewmtablesize
        
        	This Object specifies the number of entries the watermark table will maintain.  This value will decide the number of elements in cvCallRateWMTable, cvCallLegRateWMTable, cvActiveCallWMTable and cvSipMsgRateWMTable
        	**type**\:  int
        
        	**range:** 3..10
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallvolumestatshistory, self).__init__()

            self.yang_name = "cvCallVolumeStatsHistory"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcalldurationstatsthreshold = YLeaf(YType.uint32, "cvCallDurationStatsThreshold")

            self.cvcallvolumewmtablesize = YLeaf(YType.uint32, "cvCallVolumeWMTableSize")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvcalldurationstatsthreshold",
                            "cvcallvolumewmtablesize") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceDialControlMib.Cvcallvolumestatshistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallvolumestatshistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvcalldurationstatsthreshold.is_set or
                self.cvcallvolumewmtablesize.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvcalldurationstatsthreshold.yfilter != YFilter.not_set or
                self.cvcallvolumewmtablesize.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallVolumeStatsHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvcalldurationstatsthreshold.is_set or self.cvcalldurationstatsthreshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcalldurationstatsthreshold.get_name_leafdata())
            if (self.cvcallvolumewmtablesize.is_set or self.cvcallvolumewmtablesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvcallvolumewmtablesize.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallDurationStatsThreshold" or name == "cvCallVolumeWMTableSize"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvCallDurationStatsThreshold"):
                self.cvcalldurationstatsthreshold = value
                self.cvcalldurationstatsthreshold.value_namespace = name_space
                self.cvcalldurationstatsthreshold.value_namespace_prefix = name_space_prefix
            if(value_path == "cvCallVolumeWMTableSize"):
                self.cvcallvolumewmtablesize = value
                self.cvcallvolumewmtablesize.value_namespace = name_space
                self.cvcallvolumewmtablesize.value_namespace_prefix = name_space_prefix


    class Cvpeercfgtable(Entity):
        """
        The table contains the Voice Generic Peer information that
        is used to create an ifIndexed row with an appropriate
        ifType that is associated with the cvPeerCfgType and
        cvPeerCfgPeerType objects.
        
        .. attribute:: cvpeercfgentry
        
        	A single voice generic Peer. The creation of this entry will create an associated ifEntry with an ifType that is associated with cvPeerCfgType, i.e., for 'voiceEncap' encapsulation, an ifEntry will contain an ifType voiceEncap(103); for 'voiceOverIp' encapsulation, an ifEntry will contain an ifType voiceOverIp(104). The ifAdminStatus of the newly created ifEntry is set to 'up' and ifOperStatus is set to 'down'. In addition, an associated voiceEncap/voiceOverIp Peer configuration entry is created after the successful ifEntry creation. Then ifIndex of the newly created ifEntry must be used by the network manager to create a peer configuration entry of IETF Dial Control MIB (Refer to RFC 2128 section 2.2.3.1 and the description of dialCtlPeerCfgEntry for the detailed information). In summary, the voice dial peer creation steps are as follows\: [1] create this entry (voice/data generic peer entry). [2] read the cvPeerCfgIfIndex of this entry for the     ifIndex of newly created voice/data generic peer. [3] create the dialCtlPeerCfgEntry of RFC 2128 with the     indices of dialCtlPeerCfgId and the ifIndex of newly     created voice generic peer.  For each VoIP peer, it uses IP address and UDP port with RTP protocol to transfer voice packet. Therefore, it does not have its lower layer interface. The dialCtlPeerCfgIfType object of IETF Dial Control MIB must set to 'other' and the dialCtlPeerCfgLowerIf must set to '0'.  After the successful creation of peer configuration entry of IETF Dial Control MIB, the dial plan software in managed device will set the ifOperStatus of the newly created voiceEncap/voiceOverIp ifEntry to 'up' for enabling the peer function if the peer configuration is completed. When this entry is deleted, its associated ifEntry, voiceEncap/voiceOverIp specific peer entry and the peer entry of IETF Dial Control MIB are deleted
        	**type**\: list of    :py:class:`Cvpeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvpeercfgtable, self).__init__()

            self.yang_name = "cvPeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvpeercfgentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvpeercfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvpeercfgtable, self).__setattr__(name, value)


        class Cvpeercfgentry(Entity):
            """
            A single voice generic Peer. The creation of this
            entry will create an associated ifEntry with an ifType
            that is associated with cvPeerCfgType, i.e., for
            'voiceEncap' encapsulation, an ifEntry will contain an
            ifType voiceEncap(103); for 'voiceOverIp' encapsulation,
            an ifEntry will contain an ifType voiceOverIp(104). The
            ifAdminStatus of the newly created ifEntry is set to 'up'
            and ifOperStatus is set to 'down'. In addition, an
            associated voiceEncap/voiceOverIp Peer configuration
            entry is created after the successful ifEntry creation.
            Then ifIndex of the newly created ifEntry must be used by
            the network manager to create a peer configuration entry
            of IETF Dial Control MIB (Refer to RFC 2128 section
            2.2.3.1 and the description of dialCtlPeerCfgEntry for the
            detailed information).
            In summary, the voice dial peer creation steps are as
            follows\:
            [1] create this entry (voice/data generic peer entry).
            [2] read the cvPeerCfgIfIndex of this entry for the
                ifIndex of newly created voice/data generic peer.
            [3] create the dialCtlPeerCfgEntry of RFC 2128 with the
                indices of dialCtlPeerCfgId and the ifIndex of newly
                created voice generic peer.
            
            For each VoIP peer, it uses IP address and UDP port with
            RTP protocol to transfer voice packet. Therefore, it does
            not have its lower layer interface. The
            dialCtlPeerCfgIfType object of IETF Dial Control MIB must
            set to 'other' and the dialCtlPeerCfgLowerIf must set to
            '0'.
            
            After the successful creation of peer configuration entry
            of IETF Dial Control MIB, the dial plan software in
            managed device will set the ifOperStatus of the newly
            created voiceEncap/voiceOverIp ifEntry to 'up' for
            enabling the peer function if the peer configuration is
            completed.
            When this entry is deleted, its associated ifEntry,
            voiceEncap/voiceOverIp specific peer entry and the peer
            entry of IETF Dial Control MIB are deleted.
            
            .. attribute:: cvpeercfgindex  <key>
            
            	An arbitrary index that uniquely identifies a generic voice peer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvcallvolpeerincomingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an incoming dialpeer
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolpeeroutgoingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an outgoing dialpeer
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvpeercfgifindex
            
            	The ifIndex of the peer associated ifEntry. The ifIndex appears after the associated ifEntry is created successfully. This ifIndex will be used to access the objects in the Voice over Telephony or Voice over IP peer specific table. In addition, the ifIndex is also used to access the associated peer configuration entry of the IETF Dial Control MIB. If the peer associated ifEntry had not been created, then this object has a value of zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpeercfgpeertype
            
            	Specifies the type of a peer. voice \- peer in voice type to be defined in a voice         gateway for voice calls.  data  \- peer in data type to be defined in gateway         that supports universal ports for modem/data         calls and integrated ports for data calls
            	**type**\:   :py:class:`Cvpeercfgpeertype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.Cvpeercfgpeertype>`
            
            .. attribute:: cvpeercfgrowstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cvpeercfgtype
            
            	Specifies the type of voice related encapsulation. voice \- voice encapsulation (voiceEncap ifType) on the         telephony network. voip  \- VoIP encapsulation (voiceOverIp ifType) on the IP         network. mmail \- Media Mail over IP encapsulation (mediaMailOverIp         ifType) on the IP network. voatm \- VoATM encapsulation (voiceOverATM ifType) on the         ATM network. vofr  \- VoFR encapsulation (voiceOverFR ifType) on the         Frame Relay network
            	**type**\:   :py:class:`Cvpeercfgtype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.Cvpeercfgtype>`
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry, self).__init__()

                self.yang_name = "cvPeerCfgEntry"
                self.yang_parent_name = "cvPeerCfgTable"

                self.cvpeercfgindex = YLeaf(YType.int32, "cvPeerCfgIndex")

                self.cvcallvolpeerincomingcalls = YLeaf(YType.uint32, "cvCallVolPeerIncomingCalls")

                self.cvcallvolpeeroutgoingcalls = YLeaf(YType.uint32, "cvCallVolPeerOutgoingCalls")

                self.cvpeercfgifindex = YLeaf(YType.int32, "cvPeerCfgIfIndex")

                self.cvpeercfgpeertype = YLeaf(YType.enumeration, "cvPeerCfgPeerType")

                self.cvpeercfgrowstatus = YLeaf(YType.enumeration, "cvPeerCfgRowStatus")

                self.cvpeercfgtype = YLeaf(YType.enumeration, "cvPeerCfgType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpeercfgindex",
                                "cvcallvolpeerincomingcalls",
                                "cvcallvolpeeroutgoingcalls",
                                "cvpeercfgifindex",
                                "cvpeercfgpeertype",
                                "cvpeercfgrowstatus",
                                "cvpeercfgtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry, self).__setattr__(name, value)

            class Cvpeercfgpeertype(Enum):
                """
                Cvpeercfgpeertype

                Specifies the type of a peer.

                voice \- peer in voice type to be defined in a voice

                        gateway for voice calls. 

                data  \- peer in data type to be defined in gateway

                        that supports universal ports for modem/data

                        calls and integrated ports for data calls.

                .. data:: voice = 1

                .. data:: data = 2

                """

                voice = Enum.YLeaf(1, "voice")

                data = Enum.YLeaf(2, "data")


            class Cvpeercfgtype(Enum):
                """
                Cvpeercfgtype

                Specifies the type of voice related encapsulation.

                voice \- voice encapsulation (voiceEncap ifType) on the

                        telephony network.

                voip  \- VoIP encapsulation (voiceOverIp ifType) on the IP

                        network.

                mmail \- Media Mail over IP encapsulation (mediaMailOverIp

                        ifType) on the IP network.

                voatm \- VoATM encapsulation (voiceOverATM ifType) on the

                        ATM network.

                vofr  \- VoFR encapsulation (voiceOverFR ifType) on the

                        Frame Relay network.

                .. data:: voice = 1

                .. data:: voip = 2

                .. data:: mmail = 3

                .. data:: voatm = 4

                .. data:: vofr = 5

                """

                voice = Enum.YLeaf(1, "voice")

                voip = Enum.YLeaf(2, "voip")

                mmail = Enum.YLeaf(3, "mmail")

                voatm = Enum.YLeaf(4, "voatm")

                vofr = Enum.YLeaf(5, "vofr")


            def has_data(self):
                return (
                    self.cvpeercfgindex.is_set or
                    self.cvcallvolpeerincomingcalls.is_set or
                    self.cvcallvolpeeroutgoingcalls.is_set or
                    self.cvpeercfgifindex.is_set or
                    self.cvpeercfgpeertype.is_set or
                    self.cvpeercfgrowstatus.is_set or
                    self.cvpeercfgtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpeercfgindex.yfilter != YFilter.not_set or
                    self.cvcallvolpeerincomingcalls.yfilter != YFilter.not_set or
                    self.cvcallvolpeeroutgoingcalls.yfilter != YFilter.not_set or
                    self.cvpeercfgifindex.yfilter != YFilter.not_set or
                    self.cvpeercfgpeertype.yfilter != YFilter.not_set or
                    self.cvpeercfgrowstatus.yfilter != YFilter.not_set or
                    self.cvpeercfgtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvPeerCfgEntry" + "[cvPeerCfgIndex='" + self.cvpeercfgindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvPeerCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpeercfgindex.is_set or self.cvpeercfgindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercfgindex.get_name_leafdata())
                if (self.cvcallvolpeerincomingcalls.is_set or self.cvcallvolpeerincomingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolpeerincomingcalls.get_name_leafdata())
                if (self.cvcallvolpeeroutgoingcalls.is_set or self.cvcallvolpeeroutgoingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolpeeroutgoingcalls.get_name_leafdata())
                if (self.cvpeercfgifindex.is_set or self.cvpeercfgifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercfgifindex.get_name_leafdata())
                if (self.cvpeercfgpeertype.is_set or self.cvpeercfgpeertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercfgpeertype.get_name_leafdata())
                if (self.cvpeercfgrowstatus.is_set or self.cvpeercfgrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercfgrowstatus.get_name_leafdata())
                if (self.cvpeercfgtype.is_set or self.cvpeercfgtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercfgtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvPeerCfgIndex" or name == "cvCallVolPeerIncomingCalls" or name == "cvCallVolPeerOutgoingCalls" or name == "cvPeerCfgIfIndex" or name == "cvPeerCfgPeerType" or name == "cvPeerCfgRowStatus" or name == "cvPeerCfgType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvPeerCfgIndex"):
                    self.cvpeercfgindex = value
                    self.cvpeercfgindex.value_namespace = name_space
                    self.cvpeercfgindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallVolPeerIncomingCalls"):
                    self.cvcallvolpeerincomingcalls = value
                    self.cvcallvolpeerincomingcalls.value_namespace = name_space
                    self.cvcallvolpeerincomingcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallVolPeerOutgoingCalls"):
                    self.cvcallvolpeeroutgoingcalls = value
                    self.cvcallvolpeeroutgoingcalls.value_namespace = name_space
                    self.cvcallvolpeeroutgoingcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCfgIfIndex"):
                    self.cvpeercfgifindex = value
                    self.cvpeercfgifindex.value_namespace = name_space
                    self.cvpeercfgifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCfgPeerType"):
                    self.cvpeercfgpeertype = value
                    self.cvpeercfgpeertype.value_namespace = name_space
                    self.cvpeercfgpeertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCfgRowStatus"):
                    self.cvpeercfgrowstatus = value
                    self.cvpeercfgrowstatus.value_namespace = name_space
                    self.cvpeercfgrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCfgType"):
                    self.cvpeercfgtype = value
                    self.cvpeercfgtype.value_namespace = name_space
                    self.cvpeercfgtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpeercfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpeercfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvPeerCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvPeerCfgEntry"):
                for c in self.cvpeercfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpeercfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvPeerCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvvoicepeercfgtable(Entity):
        """
        The table contains the Voice over Telephony peer specific
        information that is required to accept voice calls or to
        which it will place them or perform various loopback tests
        via interface.
        
        .. attribute:: cvvoicepeercfgentry
        
        	A single Voice specific Peer. One entry per voice encapsulation. The entry is created when its associated 'voiceEncap(103)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of    :py:class:`Cvvoicepeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable, self).__init__()

            self.yang_name = "cvVoicePeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvvoicepeercfgentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable, self).__setattr__(name, value)


        class Cvvoicepeercfgentry(Entity):
            """
            A single Voice specific Peer. One entry per voice
            encapsulation.
            The entry is created when its associated 'voiceEncap(103)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cvvoicepeercfgcasgroup
            
            	The object specifies the CAS group number of a CAS capable T1/E1  that is in the dialCtlPeerCfgLowerIf object of RFC2128. This object can be set to a valid CAS group number only if the dialCtlPeerCfgLowerIf contains a valid ifIndex for a CAS capable T1/E1. The object must set to \-1 before the value of the  dialCtlPeerCfgLowerIf object of RFC2128 can be changed
            	**type**\:  int
            
            	**range:** \-1..30
            
            .. attribute:: cvvoicepeercfgdialdigitsprefix
            
            	The object specifies the prefix of the dial digits for the peer. The dial digits prefix is sent to telephony interface before the real phone number when the system places the outgoing call to the voice encapsulation peer over telephony interface
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: cvvoicepeercfgdidcallenable
            
            	The object enables/disables the DID call treatment for incoming DNIS digits. true  \- treat the incoming DNIS digits as if the digits         are received from DID trunk. false \- Disable DID call treatment for incoming DNIS         digits
            	**type**\:  bool
            
            .. attribute:: cvvoicepeercfgechocancellertest
            
            	This object specifies which, if any, test to run in the echo canceller when a call from the network is connected. echoCancellerTestNone    \- do not run a test. echoCancellerG168Test2A  \- run ITU\-T G.168 Test 2A. echoCancellerG168Test2B  \- run ITU\-T G.168 Test 2B. echoCancellerG168Test2Ca \- run ITU\-T G.168 Test 2C(a). echoCancellerG168Test2Cb \- run ITU\-T G.168 Test 2C(b). echoCancellerG168Test3A  \- run ITU\-T G.168 Test 3A. echoCancellerG168Test3B  \- run ITU\-T G.168 Test 3B. echoCancellerG168Test3C  \- run ITU\-T G.168 Test 3C. echoCancellerG168Test4   \- run ITU\-T G.168 Test 4. echoCancellerG168Test5   \- run ITU\-T G.168 Test 5. echoCancellerG168Test6   \- run ITU\-T G.168 Test 6. echoCancellerG168Test7   \- run ITU\-T G.168 Test 7. echoCancellerG168Test9   \- run ITU\-T G.168 Test 9
            	**type**\:   :py:class:`Cvvoicepeercfgechocancellertest <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry.Cvvoicepeercfgechocancellertest>`
            
            .. attribute:: cvvoicepeercfgforwarddigits
            
            	This object specifies the number of dialed digits to forward to the remote destination in the setup message. The object can take the value\:     0\-32 number of right justified digits to forward     \-1 default     \-2 forward extra digits i.e those over and above        those needed to match to the destination pattern     \-3 forward all digits
            	**type**\:  int
            
            	**range:** \-3..32
            
            .. attribute:: cvvoicepeercfgregistere164
            
            	This object specifies that the E.164 number specified in the dialCtlPeerCfgOriginateAddress field of the associated dialCtlPeerCfgTable entry be registered as an extension  phone number of this gateway for H323 gatekeeper and/or  SIP registrar
            	**type**\:  bool
            
            .. attribute:: cvvoicepeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target.  The valid Mapping type definitions for the peer are as follows\: loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    compressed \- loopback is performed on compressed voice                 as close to the CODEC which processes the                 data as possible.    uncompressed \- loopback is performed on the PCM or                 analog voice as close to the telephony                 endpoint as possible.  Local loopback case\: uncompressed \- the PCM voice coming into the DSP is simply     turned around and sent back out, allowing testing of     the transmit\-\-> receive paths in the telephony     endpoint. compressed \- the compressed voice coming out of the CODEC is     turned around on the DSP module and fed back into the     decompressor through the jitter buffer. In addition to     the telephony endpoint, this tests both the encode and     decode paths without involving data paths or packet     handling on the host router.  Remote loopback case\: compressed \- RTP packets received from the network are     decapsulated and passed to the DSP board. Instead of     feeding these into the CODEC for decompression, they     are immediately sent back to the session application     as if they had originated locally and been compressed. uncompressed \- In addition to the above, the voice samples     are sent all the way through the CODEC and then turned     around instead of being sent to the telephony     endpoint
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry, self).__init__()

                self.yang_name = "cvVoicePeerCfgEntry"
                self.yang_parent_name = "cvVoicePeerCfgTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cvvoicepeercfgcasgroup = YLeaf(YType.int32, "cvVoicePeerCfgCasGroup")

                self.cvvoicepeercfgdialdigitsprefix = YLeaf(YType.str, "cvVoicePeerCfgDialDigitsPrefix")

                self.cvvoicepeercfgdidcallenable = YLeaf(YType.boolean, "cvVoicePeerCfgDIDCallEnable")

                self.cvvoicepeercfgechocancellertest = YLeaf(YType.enumeration, "cvVoicePeerCfgEchoCancellerTest")

                self.cvvoicepeercfgforwarddigits = YLeaf(YType.int32, "cvVoicePeerCfgForwardDigits")

                self.cvvoicepeercfgregistere164 = YLeaf(YType.boolean, "cvVoicePeerCfgRegisterE164")

                self.cvvoicepeercfgsessiontarget = YLeaf(YType.str, "cvVoicePeerCfgSessionTarget")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cvvoicepeercfgcasgroup",
                                "cvvoicepeercfgdialdigitsprefix",
                                "cvvoicepeercfgdidcallenable",
                                "cvvoicepeercfgechocancellertest",
                                "cvvoicepeercfgforwarddigits",
                                "cvvoicepeercfgregistere164",
                                "cvvoicepeercfgsessiontarget") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry, self).__setattr__(name, value)

            class Cvvoicepeercfgechocancellertest(Enum):
                """
                Cvvoicepeercfgechocancellertest

                This object specifies which, if any, test to run in the

                echo canceller when a call from the network is connected.

                echoCancellerTestNone    \- do not run a test.

                echoCancellerG168Test2A  \- run ITU\-T G.168 Test 2A.

                echoCancellerG168Test2B  \- run ITU\-T G.168 Test 2B.

                echoCancellerG168Test2Ca \- run ITU\-T G.168 Test 2C(a).

                echoCancellerG168Test2Cb \- run ITU\-T G.168 Test 2C(b).

                echoCancellerG168Test3A  \- run ITU\-T G.168 Test 3A.

                echoCancellerG168Test3B  \- run ITU\-T G.168 Test 3B.

                echoCancellerG168Test3C  \- run ITU\-T G.168 Test 3C.

                echoCancellerG168Test4   \- run ITU\-T G.168 Test 4.

                echoCancellerG168Test5   \- run ITU\-T G.168 Test 5.

                echoCancellerG168Test6   \- run ITU\-T G.168 Test 6.

                echoCancellerG168Test7   \- run ITU\-T G.168 Test 7.

                echoCancellerG168Test9   \- run ITU\-T G.168 Test 9.

                .. data:: echoCancellerTestNone = 1

                .. data:: echoCancellerG168Test2A = 2

                .. data:: echoCancellerG168Test2B = 3

                .. data:: echoCancellerG168Test2Ca = 4

                .. data:: echoCancellerG168Test2Cb = 5

                .. data:: echoCancellerG168Test3A = 6

                .. data:: echoCancellerG168Test3B = 7

                .. data:: echoCancellerG168Test3C = 8

                .. data:: echoCancellerG168Test4 = 9

                .. data:: echoCancellerG168Test6 = 10

                .. data:: echoCancellerG168Test9 = 11

                .. data:: echoCancellerG168Test5 = 12

                .. data:: echoCancellerG168Test7 = 13

                """

                echoCancellerTestNone = Enum.YLeaf(1, "echoCancellerTestNone")

                echoCancellerG168Test2A = Enum.YLeaf(2, "echoCancellerG168Test2A")

                echoCancellerG168Test2B = Enum.YLeaf(3, "echoCancellerG168Test2B")

                echoCancellerG168Test2Ca = Enum.YLeaf(4, "echoCancellerG168Test2Ca")

                echoCancellerG168Test2Cb = Enum.YLeaf(5, "echoCancellerG168Test2Cb")

                echoCancellerG168Test3A = Enum.YLeaf(6, "echoCancellerG168Test3A")

                echoCancellerG168Test3B = Enum.YLeaf(7, "echoCancellerG168Test3B")

                echoCancellerG168Test3C = Enum.YLeaf(8, "echoCancellerG168Test3C")

                echoCancellerG168Test4 = Enum.YLeaf(9, "echoCancellerG168Test4")

                echoCancellerG168Test6 = Enum.YLeaf(10, "echoCancellerG168Test6")

                echoCancellerG168Test9 = Enum.YLeaf(11, "echoCancellerG168Test9")

                echoCancellerG168Test5 = Enum.YLeaf(12, "echoCancellerG168Test5")

                echoCancellerG168Test7 = Enum.YLeaf(13, "echoCancellerG168Test7")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cvvoicepeercfgcasgroup.is_set or
                    self.cvvoicepeercfgdialdigitsprefix.is_set or
                    self.cvvoicepeercfgdidcallenable.is_set or
                    self.cvvoicepeercfgechocancellertest.is_set or
                    self.cvvoicepeercfgforwarddigits.is_set or
                    self.cvvoicepeercfgregistere164.is_set or
                    self.cvvoicepeercfgsessiontarget.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgcasgroup.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgdialdigitsprefix.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgdidcallenable.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgechocancellertest.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgforwarddigits.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgregistere164.yfilter != YFilter.not_set or
                    self.cvvoicepeercfgsessiontarget.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvVoicePeerCfgEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoicePeerCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cvvoicepeercfgcasgroup.is_set or self.cvvoicepeercfgcasgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgcasgroup.get_name_leafdata())
                if (self.cvvoicepeercfgdialdigitsprefix.is_set or self.cvvoicepeercfgdialdigitsprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgdialdigitsprefix.get_name_leafdata())
                if (self.cvvoicepeercfgdidcallenable.is_set or self.cvvoicepeercfgdidcallenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgdidcallenable.get_name_leafdata())
                if (self.cvvoicepeercfgechocancellertest.is_set or self.cvvoicepeercfgechocancellertest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgechocancellertest.get_name_leafdata())
                if (self.cvvoicepeercfgforwarddigits.is_set or self.cvvoicepeercfgforwarddigits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgforwarddigits.get_name_leafdata())
                if (self.cvvoicepeercfgregistere164.is_set or self.cvvoicepeercfgregistere164.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgregistere164.get_name_leafdata())
                if (self.cvvoicepeercfgsessiontarget.is_set or self.cvvoicepeercfgsessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoicepeercfgsessiontarget.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cvVoicePeerCfgCasGroup" or name == "cvVoicePeerCfgDialDigitsPrefix" or name == "cvVoicePeerCfgDIDCallEnable" or name == "cvVoicePeerCfgEchoCancellerTest" or name == "cvVoicePeerCfgForwardDigits" or name == "cvVoicePeerCfgRegisterE164" or name == "cvVoicePeerCfgSessionTarget"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgCasGroup"):
                    self.cvvoicepeercfgcasgroup = value
                    self.cvvoicepeercfgcasgroup.value_namespace = name_space
                    self.cvvoicepeercfgcasgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgDialDigitsPrefix"):
                    self.cvvoicepeercfgdialdigitsprefix = value
                    self.cvvoicepeercfgdialdigitsprefix.value_namespace = name_space
                    self.cvvoicepeercfgdialdigitsprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgDIDCallEnable"):
                    self.cvvoicepeercfgdidcallenable = value
                    self.cvvoicepeercfgdidcallenable.value_namespace = name_space
                    self.cvvoicepeercfgdidcallenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgEchoCancellerTest"):
                    self.cvvoicepeercfgechocancellertest = value
                    self.cvvoicepeercfgechocancellertest.value_namespace = name_space
                    self.cvvoicepeercfgechocancellertest.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgForwardDigits"):
                    self.cvvoicepeercfgforwarddigits = value
                    self.cvvoicepeercfgforwarddigits.value_namespace = name_space
                    self.cvvoicepeercfgforwarddigits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgRegisterE164"):
                    self.cvvoicepeercfgregistere164 = value
                    self.cvvoicepeercfgregistere164.value_namespace = name_space
                    self.cvvoicepeercfgregistere164.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoicePeerCfgSessionTarget"):
                    self.cvvoicepeercfgsessiontarget = value
                    self.cvvoicepeercfgsessiontarget.value_namespace = name_space
                    self.cvvoicepeercfgsessiontarget.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvvoicepeercfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvvoicepeercfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvVoicePeerCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvVoicePeerCfgEntry"):
                for c in self.cvvoicepeercfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvvoicepeercfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvVoicePeerCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvvoippeercfgtable(Entity):
        """
        The table contains the Voice over IP (VoIP) peer specific
        information that is required to accept voice calls or to
        which it will place them via IP backbone with the
        specified session protocol in cvVoIPPeerCfgSessionProtocol.
        
        .. attribute:: cvvoippeercfgentry
        
        	A single VoIP specific Peer. One entry per VoIP encapsulation. The entry is created when its associated 'voiceOverIp(104)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of    :py:class:`Cvvoippeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvvoippeercfgtable, self).__init__()

            self.yang_name = "cvVoIPPeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvvoippeercfgentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvvoippeercfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvvoippeercfgtable, self).__setattr__(name, value)


        class Cvvoippeercfgentry(Entity):
            """
            A single VoIP specific Peer. One entry per VoIP
            encapsulation.
            The entry is created when its associated 'voiceOverIp(104)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cvvoippeercfgbitrate
            
            	This object specifies the target bit rate. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'
            	**type**\:  int
            
            	**range:** 10000..32000
            
            .. attribute:: cvvoippeercfgbitrates
            
            	This object indicates modes of Bit rates. One or more upto four modes can be configured at the same time as bit rates can be changed dynamically for AMR\-NB codec. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\:   :py:class:`Cvamrnbbitratemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvamrnbbitratemode>`
            
            .. attribute:: cvvoippeercfgcoderbytes
            
            	This object specifies the size of the voice payload sample to be produced by the coder specified in cvVoIPPeerCfgCoderRate. Each coder sample produces 10 bytes of voice payload. The specified value will be rounded down to the nearest valid size.  A value of 0, specifies that the coder defined by cvVoIPPeerCfgCoderRate should produce its default payload size
            	**type**\:  int
            
            	**range:** 0..None \| 10..240
            
            	**units**\: bytes
            
            .. attribute:: cvvoippeercfgcodermode
            
            	This object indicates the iLBC codec mode to be used. The value of this object is valid only if  cvVoIPPeerCfgCoderRate is equal to 'iLBC'
            	**type**\:   :py:class:`Cvilbcframemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvilbcframemode>`
            
            .. attribute:: cvvoippeercfgcoderrate
            
            	This object specifies the most desirable codec of speech for the VoIP peer
            	**type**\:   :py:class:`Cvcspeechcoderrate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvcspeechcoderrate>`
            
            .. attribute:: cvvoippeercfgcodingmode
            
            	This object specifies the coding mode to be used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following coding modes are supported\: adaptive    (1) \- adaptive mode where iSAC performs bandwidth                     estimation and adapts to the available channel                    bandwidth. independent (2) \- independent mode in which no bandwidth estimation                    is performed
            	**type**\:   :py:class:`Cvvoippeercfgcodingmode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgcodingmode>`
            
            .. attribute:: cvvoippeercfgcrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgdesiredqos
            
            	The object specifies the user requested Quality of Service for the call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoippeercfgdesiredqosvideo
            
            	The object specifies the user requested Quality of Service for the video portion of the call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoippeercfgdigitrelay
            
            	This object specifies the methods to transmit dial digits (DTMF or MF digits) via IP network. rtpCisco       \- Enable capability to transmit dial digits                  with Cisco proprietary RTP payload type. h245Signal     \- Enable capability to transmit dtmf digits                  across the H.245 channel, via the signal                  field of the UserInputIndication message h245Alphanumeric \- Enable capability to transmit dtmf                  digit across the H.245 channel, via the                  string or alphanumeric fields of the                  UserInputIndication message rtpNte         \- Enable capability to transmit dial digits                  using Named Telephony Event per RFC 2833                  section 3. sipNotify      \- Enable capability to transmit dtmf                  digits using unsolicited SIP NOTIFY                  messages. This mechanism is only available                  for SIP dialpeers. sipKpml        \- Enable capability to transmit dtmf                  digits using KPML over SIP SUBSCRIBE                  and NOTIFY messages. This mechanism is                  only available for SIP dialpeers.   Modifying the value of cvVoIPPeerCfgSessionProtocol can reset the digit\-relay method associated bits value in this object if the modified session protocol does not support  these digit\-relay methods
            	**type**\:   :py:class:`Cvvoippeercfgdigitrelay <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgdigitrelay>`
            
            .. attribute:: cvvoippeercfgdscppolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for RPH to DSCP mapping and policing feature
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgexpectfactor
            
            	This object specifies the user requested Expectation Factor of voice quality for the call via this peer
            	**type**\:  int
            
            	**range:** 0..20
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoippeercfgfaxbytes
            
            	This object specifies the payload size to be produced by the coder when it is generating fax data. A value of 0, specifies that the coder specified in cvVoIPCfgPeerCoderRate should produce its default fax payload size
            	**type**\:  int
            
            	**range:** 0..None \| 10..255
            
            	**units**\: bytes
            
            .. attribute:: cvvoippeercfgfaxrate
            
            	This object specifies the default transmit rate of FAX the VoIP peer. If the value of this object is 'none', then the Fax relay feature is disabled; otherwise the Fax relay feature is enabled
            	**type**\:   :py:class:`Cvcfaxtransmitrate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvcfaxtransmitrate>`
            
            .. attribute:: cvvoippeercfgframesize
            
            	This object specifies the frame size used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. The frame size can be 30 ms or 60 ms, and it can be fixed for all packets or vary depending on the configuration and bandwidth estimation. Thus it can have the following values\: frameSize30      \- initial frame size of 30 ms frameSize60      \- initial frame size of 60 ms frameSize30fixed \- fixed frame size 30 ms frameSize60fixed \- fixed frame size 60 ms
            	**type**\:   :py:class:`Cvvoippeercfgframesize <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgframesize>`
            
            .. attribute:: cvvoippeercfgicpif
            
            	This object specifies the user requested Calculated Planning Impairment Factor (Icpif) for the call via this peer
            	**type**\:  int
            
            	**range:** 0..55
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoippeercfginbandsignaling
            
            	This object specifies the type of in\-band signaling that will be used between the end points of the call. It is used by the router to determine how to interpret ABCD signaling bits sent as part of voice payload data
            	**type**\:   :py:class:`Cvcinbandsignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvcinbandsignaling>`
            
            .. attribute:: cvvoippeercfgipprecedence
            
            	This object specifies the value to be stored in the IP Precedence field of voice packets, with values ranging from 0 (normal precedence) through 7 (network control), allowing the managed system to set the importance of each voice packet for delivering them to the destination peer
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cvvoippeercfgmediapolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for Media policing feature.
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgmediasetting
            
            	This object specifies how the media is to be setup on an IP\-IP Gateway. Two choices are valid\: flow\-through and flow\-around. When in flow\-through mode, which is the default setting, the IP\-IP Gateway will terminate and  then re\-originate the media stream. When flow\-around is configured the Gateway will not be involved with the media, since it will flow\-around the Gateway and will be established directly between the endpoints
            	**type**\:   :py:class:`Cvvoippeercfgmediasetting <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgmediasetting>`
            
            .. attribute:: cvvoippeercfgminacceptableqos
            
            	The object specifies the minimally acceptable Quality of Service for the call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoippeercfgminacceptableqosvideo
            
            	The object specifies the minimally acceptable Quality of Service for the video portion of the call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoippeercfgoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgpoorqovnotificationenable
            
            	This object specifies whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for the call that is associated with this peer
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgredirectip2ip
            
            	This object specifies the Inbound VoIP calls that match an outbound VoIP dialpeer will be responded with a SIP  redirect(for inbound SIP) or H.450.3 call\-forward(for  inbound H.323)
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgsessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:   :py:class:`Cvsessionprotocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvsessionprotocol>`
            
            .. attribute:: cvvoippeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target. The type\-specific\-syntax is exactly that, something that the particular mapping scheme can understand. For example, Session target           Meaning ipv4\:171.68.13.55\:1006   The session target is the IP                          version 4 address of 171.68.13.55                          and port 1006. dns\:pots.cisco.com\:1661  The session target is the IP host                          with dns name pots.cisco.com, and                          port 1661. ras                      The session target is the                          gatekeeper with RAS (Registration                          , Admission,  Status protocol). settlement               The session target is the                          settlement server. enum\:1                   The session target is the enum                           profile match table 1.  The valid Mapping type definitions for the peer are as follows\: ipv4       \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z dns        \- Syntax\: dns\:host.domain\:port or                      dns\:host.domain ras        \- Syntax\: ras settlement \- Syntax\: settlement enum       \- Syntax\: enum\:  loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    rtp \- loopback is performed at the transport protocol          level.  Local loopback case\: rtp \- the session application sets up an RTP stream to     itself (i.e. actually allocates a port pair and opens     the appropriate UDP sockets). It then does the full     RTP encapsulation, sends the packets to the loopback     IP address, receives the RTP packets, and hands the     compressed voice back to the CODEC. This tests the     entire local processing path, both transmit and     receive, in the router, as well as all of the above     paths.  Remote loopback case\: rtp\: RTP packets received from the network are decapsulated and      immediately re\-encapsulated in the outbound RTP      stream, using the same media clock (i.e. timestamp)      as the received packet. They are then sent back to      the remote source router as if the voice had      originated on a telephony port on the local router
            	**type**\:  str
            
            .. attribute:: cvvoippeercfgtechprefix
            
            	This object specifies the technology prefix of the peer, The technology prefix and the called party address are passed in Admission Request (ARQ) to gatekeeper for the called party address resolution during call setup
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cvvoippeercfgudpchecksumenable
            
            	This object specifies whether the outgoing voice related UDP packet contains a valid checksum value. true  \- enable the checksum of outgoing voice UDP packets false \- disable the checksum of outgoing voice UDP packets
            	**type**\:  bool
            
            .. attribute:: cvvoippeercfgvadenable
            
            	This object specifies whether or not the VAD (Voice Activity Detection) voice data is continuously transmitted to IP backbone
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry, self).__init__()

                self.yang_name = "cvVoIPPeerCfgEntry"
                self.yang_parent_name = "cvVoIPPeerCfgTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cvvoippeercfgbitrate = YLeaf(YType.uint32, "cvVoIPPeerCfgBitRate")

                self.cvvoippeercfgbitrates = YLeaf(YType.bits, "cvVoIPPeerCfgBitRates")

                self.cvvoippeercfgcoderbytes = YLeaf(YType.int32, "cvVoIPPeerCfgCoderBytes")

                self.cvvoippeercfgcodermode = YLeaf(YType.enumeration, "cvVoIPPeerCfgCoderMode")

                self.cvvoippeercfgcoderrate = YLeaf(YType.enumeration, "cvVoIPPeerCfgCoderRate")

                self.cvvoippeercfgcodingmode = YLeaf(YType.enumeration, "cvVoIPPeerCfgCodingMode")

                self.cvvoippeercfgcrc = YLeaf(YType.boolean, "cvVoIPPeerCfgCRC")

                self.cvvoippeercfgdesiredqos = YLeaf(YType.enumeration, "cvVoIPPeerCfgDesiredQoS")

                self.cvvoippeercfgdesiredqosvideo = YLeaf(YType.enumeration, "cvVoIPPeerCfgDesiredQoSVideo")

                self.cvvoippeercfgdigitrelay = YLeaf(YType.bits, "cvVoIPPeerCfgDigitRelay")

                self.cvvoippeercfgdscppolicynotificationenable = YLeaf(YType.boolean, "cvVoIPPeerCfgDSCPPolicyNotificationEnable")

                self.cvvoippeercfgexpectfactor = YLeaf(YType.int32, "cvVoIPPeerCfgExpectFactor")

                self.cvvoippeercfgfaxbytes = YLeaf(YType.int32, "cvVoIPPeerCfgFaxBytes")

                self.cvvoippeercfgfaxrate = YLeaf(YType.enumeration, "cvVoIPPeerCfgFaxRate")

                self.cvvoippeercfgframesize = YLeaf(YType.enumeration, "cvVoIPPeerCfgFrameSize")

                self.cvvoippeercfgicpif = YLeaf(YType.int32, "cvVoIPPeerCfgIcpif")

                self.cvvoippeercfginbandsignaling = YLeaf(YType.enumeration, "cvVoIPPeerCfgInBandSignaling")

                self.cvvoippeercfgipprecedence = YLeaf(YType.int32, "cvVoIPPeerCfgIPPrecedence")

                self.cvvoippeercfgmediapolicynotificationenable = YLeaf(YType.boolean, "cvVoIPPeerCfgMediaPolicyNotificationEnable")

                self.cvvoippeercfgmediasetting = YLeaf(YType.enumeration, "cvVoIPPeerCfgMediaSetting")

                self.cvvoippeercfgminacceptableqos = YLeaf(YType.enumeration, "cvVoIPPeerCfgMinAcceptableQoS")

                self.cvvoippeercfgminacceptableqosvideo = YLeaf(YType.enumeration, "cvVoIPPeerCfgMinAcceptableQoSVideo")

                self.cvvoippeercfgoctetaligned = YLeaf(YType.boolean, "cvVoIPPeerCfgOctetAligned")

                self.cvvoippeercfgpoorqovnotificationenable = YLeaf(YType.boolean, "cvVoIPPeerCfgPoorQoVNotificationEnable")

                self.cvvoippeercfgredirectip2ip = YLeaf(YType.boolean, "cvVoIPPeerCfgRedirectip2ip")

                self.cvvoippeercfgsessionprotocol = YLeaf(YType.enumeration, "cvVoIPPeerCfgSessionProtocol")

                self.cvvoippeercfgsessiontarget = YLeaf(YType.str, "cvVoIPPeerCfgSessionTarget")

                self.cvvoippeercfgtechprefix = YLeaf(YType.str, "cvVoIPPeerCfgTechPrefix")

                self.cvvoippeercfgudpchecksumenable = YLeaf(YType.boolean, "cvVoIPPeerCfgUDPChecksumEnable")

                self.cvvoippeercfgvadenable = YLeaf(YType.boolean, "cvVoIPPeerCfgVADEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cvvoippeercfgbitrate",
                                "cvvoippeercfgbitrates",
                                "cvvoippeercfgcoderbytes",
                                "cvvoippeercfgcodermode",
                                "cvvoippeercfgcoderrate",
                                "cvvoippeercfgcodingmode",
                                "cvvoippeercfgcrc",
                                "cvvoippeercfgdesiredqos",
                                "cvvoippeercfgdesiredqosvideo",
                                "cvvoippeercfgdigitrelay",
                                "cvvoippeercfgdscppolicynotificationenable",
                                "cvvoippeercfgexpectfactor",
                                "cvvoippeercfgfaxbytes",
                                "cvvoippeercfgfaxrate",
                                "cvvoippeercfgframesize",
                                "cvvoippeercfgicpif",
                                "cvvoippeercfginbandsignaling",
                                "cvvoippeercfgipprecedence",
                                "cvvoippeercfgmediapolicynotificationenable",
                                "cvvoippeercfgmediasetting",
                                "cvvoippeercfgminacceptableqos",
                                "cvvoippeercfgminacceptableqosvideo",
                                "cvvoippeercfgoctetaligned",
                                "cvvoippeercfgpoorqovnotificationenable",
                                "cvvoippeercfgredirectip2ip",
                                "cvvoippeercfgsessionprotocol",
                                "cvvoippeercfgsessiontarget",
                                "cvvoippeercfgtechprefix",
                                "cvvoippeercfgudpchecksumenable",
                                "cvvoippeercfgvadenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry, self).__setattr__(name, value)

            class Cvvoippeercfgcodingmode(Enum):
                """
                Cvvoippeercfgcodingmode

                This object specifies the coding mode to be used. The object is

                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following

                coding modes are supported\:

                adaptive    (1) \- adaptive mode where iSAC performs bandwidth  

                                  estimation and adapts to the available channel

                                  bandwidth.

                independent (2) \- independent mode in which no bandwidth

                estimation 

                                  is performed.

                .. data:: adaptive = 1

                .. data:: independent = 2

                """

                adaptive = Enum.YLeaf(1, "adaptive")

                independent = Enum.YLeaf(2, "independent")


            class Cvvoippeercfgframesize(Enum):
                """
                Cvvoippeercfgframesize

                This object specifies the frame size used. The object is

                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'.

                The frame size can be 30 ms or 60 ms, and it can be fixed for

                all packets or vary depending on the configuration and bandwidth

                estimation. Thus it can have the following values\:

                frameSize30      \- initial frame size of 30 ms

                frameSize60      \- initial frame size of 60 ms

                frameSize30fixed \- fixed frame size 30 ms

                frameSize60fixed \- fixed frame size 60 ms

                .. data:: frameSize30 = 1

                .. data:: frameSize60 = 2

                .. data:: frameSize30fixed = 3

                .. data:: frameSize60fixed = 4

                """

                frameSize30 = Enum.YLeaf(1, "frameSize30")

                frameSize60 = Enum.YLeaf(2, "frameSize60")

                frameSize30fixed = Enum.YLeaf(3, "frameSize30fixed")

                frameSize60fixed = Enum.YLeaf(4, "frameSize60fixed")


            class Cvvoippeercfgmediasetting(Enum):
                """
                Cvvoippeercfgmediasetting

                This object specifies how the media is to be setup on

                an IP\-IP Gateway. Two choices are valid\: flow\-through

                and flow\-around. When in flow\-through mode, which is the

                default setting, the IP\-IP Gateway will terminate and 

                then re\-originate the media stream. When flow\-around

                is configured the Gateway will not be involved with the

                media, since it will flow\-around the Gateway and will

                be established directly between the endpoints.

                .. data:: flowThrough = 1

                .. data:: flowAround = 2

                """

                flowThrough = Enum.YLeaf(1, "flowThrough")

                flowAround = Enum.YLeaf(2, "flowAround")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cvvoippeercfgbitrate.is_set or
                    self.cvvoippeercfgbitrates.is_set or
                    self.cvvoippeercfgcoderbytes.is_set or
                    self.cvvoippeercfgcodermode.is_set or
                    self.cvvoippeercfgcoderrate.is_set or
                    self.cvvoippeercfgcodingmode.is_set or
                    self.cvvoippeercfgcrc.is_set or
                    self.cvvoippeercfgdesiredqos.is_set or
                    self.cvvoippeercfgdesiredqosvideo.is_set or
                    self.cvvoippeercfgdigitrelay.is_set or
                    self.cvvoippeercfgdscppolicynotificationenable.is_set or
                    self.cvvoippeercfgexpectfactor.is_set or
                    self.cvvoippeercfgfaxbytes.is_set or
                    self.cvvoippeercfgfaxrate.is_set or
                    self.cvvoippeercfgframesize.is_set or
                    self.cvvoippeercfgicpif.is_set or
                    self.cvvoippeercfginbandsignaling.is_set or
                    self.cvvoippeercfgipprecedence.is_set or
                    self.cvvoippeercfgmediapolicynotificationenable.is_set or
                    self.cvvoippeercfgmediasetting.is_set or
                    self.cvvoippeercfgminacceptableqos.is_set or
                    self.cvvoippeercfgminacceptableqosvideo.is_set or
                    self.cvvoippeercfgoctetaligned.is_set or
                    self.cvvoippeercfgpoorqovnotificationenable.is_set or
                    self.cvvoippeercfgredirectip2ip.is_set or
                    self.cvvoippeercfgsessionprotocol.is_set or
                    self.cvvoippeercfgsessiontarget.is_set or
                    self.cvvoippeercfgtechprefix.is_set or
                    self.cvvoippeercfgudpchecksumenable.is_set or
                    self.cvvoippeercfgvadenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cvvoippeercfgbitrate.yfilter != YFilter.not_set or
                    self.cvvoippeercfgbitrates.yfilter != YFilter.not_set or
                    self.cvvoippeercfgcoderbytes.yfilter != YFilter.not_set or
                    self.cvvoippeercfgcodermode.yfilter != YFilter.not_set or
                    self.cvvoippeercfgcoderrate.yfilter != YFilter.not_set or
                    self.cvvoippeercfgcodingmode.yfilter != YFilter.not_set or
                    self.cvvoippeercfgcrc.yfilter != YFilter.not_set or
                    self.cvvoippeercfgdesiredqos.yfilter != YFilter.not_set or
                    self.cvvoippeercfgdesiredqosvideo.yfilter != YFilter.not_set or
                    self.cvvoippeercfgdigitrelay.yfilter != YFilter.not_set or
                    self.cvvoippeercfgdscppolicynotificationenable.yfilter != YFilter.not_set or
                    self.cvvoippeercfgexpectfactor.yfilter != YFilter.not_set or
                    self.cvvoippeercfgfaxbytes.yfilter != YFilter.not_set or
                    self.cvvoippeercfgfaxrate.yfilter != YFilter.not_set or
                    self.cvvoippeercfgframesize.yfilter != YFilter.not_set or
                    self.cvvoippeercfgicpif.yfilter != YFilter.not_set or
                    self.cvvoippeercfginbandsignaling.yfilter != YFilter.not_set or
                    self.cvvoippeercfgipprecedence.yfilter != YFilter.not_set or
                    self.cvvoippeercfgmediapolicynotificationenable.yfilter != YFilter.not_set or
                    self.cvvoippeercfgmediasetting.yfilter != YFilter.not_set or
                    self.cvvoippeercfgminacceptableqos.yfilter != YFilter.not_set or
                    self.cvvoippeercfgminacceptableqosvideo.yfilter != YFilter.not_set or
                    self.cvvoippeercfgoctetaligned.yfilter != YFilter.not_set or
                    self.cvvoippeercfgpoorqovnotificationenable.yfilter != YFilter.not_set or
                    self.cvvoippeercfgredirectip2ip.yfilter != YFilter.not_set or
                    self.cvvoippeercfgsessionprotocol.yfilter != YFilter.not_set or
                    self.cvvoippeercfgsessiontarget.yfilter != YFilter.not_set or
                    self.cvvoippeercfgtechprefix.yfilter != YFilter.not_set or
                    self.cvvoippeercfgudpchecksumenable.yfilter != YFilter.not_set or
                    self.cvvoippeercfgvadenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvVoIPPeerCfgEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPPeerCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cvvoippeercfgbitrate.is_set or self.cvvoippeercfgbitrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgbitrate.get_name_leafdata())
                if (self.cvvoippeercfgbitrates.is_set or self.cvvoippeercfgbitrates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgbitrates.get_name_leafdata())
                if (self.cvvoippeercfgcoderbytes.is_set or self.cvvoippeercfgcoderbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgcoderbytes.get_name_leafdata())
                if (self.cvvoippeercfgcodermode.is_set or self.cvvoippeercfgcodermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgcodermode.get_name_leafdata())
                if (self.cvvoippeercfgcoderrate.is_set or self.cvvoippeercfgcoderrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgcoderrate.get_name_leafdata())
                if (self.cvvoippeercfgcodingmode.is_set or self.cvvoippeercfgcodingmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgcodingmode.get_name_leafdata())
                if (self.cvvoippeercfgcrc.is_set or self.cvvoippeercfgcrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgcrc.get_name_leafdata())
                if (self.cvvoippeercfgdesiredqos.is_set or self.cvvoippeercfgdesiredqos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgdesiredqos.get_name_leafdata())
                if (self.cvvoippeercfgdesiredqosvideo.is_set or self.cvvoippeercfgdesiredqosvideo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgdesiredqosvideo.get_name_leafdata())
                if (self.cvvoippeercfgdigitrelay.is_set or self.cvvoippeercfgdigitrelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgdigitrelay.get_name_leafdata())
                if (self.cvvoippeercfgdscppolicynotificationenable.is_set or self.cvvoippeercfgdscppolicynotificationenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgdscppolicynotificationenable.get_name_leafdata())
                if (self.cvvoippeercfgexpectfactor.is_set or self.cvvoippeercfgexpectfactor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgexpectfactor.get_name_leafdata())
                if (self.cvvoippeercfgfaxbytes.is_set or self.cvvoippeercfgfaxbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgfaxbytes.get_name_leafdata())
                if (self.cvvoippeercfgfaxrate.is_set or self.cvvoippeercfgfaxrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgfaxrate.get_name_leafdata())
                if (self.cvvoippeercfgframesize.is_set or self.cvvoippeercfgframesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgframesize.get_name_leafdata())
                if (self.cvvoippeercfgicpif.is_set or self.cvvoippeercfgicpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgicpif.get_name_leafdata())
                if (self.cvvoippeercfginbandsignaling.is_set or self.cvvoippeercfginbandsignaling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfginbandsignaling.get_name_leafdata())
                if (self.cvvoippeercfgipprecedence.is_set or self.cvvoippeercfgipprecedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgipprecedence.get_name_leafdata())
                if (self.cvvoippeercfgmediapolicynotificationenable.is_set or self.cvvoippeercfgmediapolicynotificationenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgmediapolicynotificationenable.get_name_leafdata())
                if (self.cvvoippeercfgmediasetting.is_set or self.cvvoippeercfgmediasetting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgmediasetting.get_name_leafdata())
                if (self.cvvoippeercfgminacceptableqos.is_set or self.cvvoippeercfgminacceptableqos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgminacceptableqos.get_name_leafdata())
                if (self.cvvoippeercfgminacceptableqosvideo.is_set or self.cvvoippeercfgminacceptableqosvideo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgminacceptableqosvideo.get_name_leafdata())
                if (self.cvvoippeercfgoctetaligned.is_set or self.cvvoippeercfgoctetaligned.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgoctetaligned.get_name_leafdata())
                if (self.cvvoippeercfgpoorqovnotificationenable.is_set or self.cvvoippeercfgpoorqovnotificationenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgpoorqovnotificationenable.get_name_leafdata())
                if (self.cvvoippeercfgredirectip2ip.is_set or self.cvvoippeercfgredirectip2ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgredirectip2ip.get_name_leafdata())
                if (self.cvvoippeercfgsessionprotocol.is_set or self.cvvoippeercfgsessionprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgsessionprotocol.get_name_leafdata())
                if (self.cvvoippeercfgsessiontarget.is_set or self.cvvoippeercfgsessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgsessiontarget.get_name_leafdata())
                if (self.cvvoippeercfgtechprefix.is_set or self.cvvoippeercfgtechprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgtechprefix.get_name_leafdata())
                if (self.cvvoippeercfgudpchecksumenable.is_set or self.cvvoippeercfgudpchecksumenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgudpchecksumenable.get_name_leafdata())
                if (self.cvvoippeercfgvadenable.is_set or self.cvvoippeercfgvadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoippeercfgvadenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cvVoIPPeerCfgBitRate" or name == "cvVoIPPeerCfgBitRates" or name == "cvVoIPPeerCfgCoderBytes" or name == "cvVoIPPeerCfgCoderMode" or name == "cvVoIPPeerCfgCoderRate" or name == "cvVoIPPeerCfgCodingMode" or name == "cvVoIPPeerCfgCRC" or name == "cvVoIPPeerCfgDesiredQoS" or name == "cvVoIPPeerCfgDesiredQoSVideo" or name == "cvVoIPPeerCfgDigitRelay" or name == "cvVoIPPeerCfgDSCPPolicyNotificationEnable" or name == "cvVoIPPeerCfgExpectFactor" or name == "cvVoIPPeerCfgFaxBytes" or name == "cvVoIPPeerCfgFaxRate" or name == "cvVoIPPeerCfgFrameSize" or name == "cvVoIPPeerCfgIcpif" or name == "cvVoIPPeerCfgInBandSignaling" or name == "cvVoIPPeerCfgIPPrecedence" or name == "cvVoIPPeerCfgMediaPolicyNotificationEnable" or name == "cvVoIPPeerCfgMediaSetting" or name == "cvVoIPPeerCfgMinAcceptableQoS" or name == "cvVoIPPeerCfgMinAcceptableQoSVideo" or name == "cvVoIPPeerCfgOctetAligned" or name == "cvVoIPPeerCfgPoorQoVNotificationEnable" or name == "cvVoIPPeerCfgRedirectip2ip" or name == "cvVoIPPeerCfgSessionProtocol" or name == "cvVoIPPeerCfgSessionTarget" or name == "cvVoIPPeerCfgTechPrefix" or name == "cvVoIPPeerCfgUDPChecksumEnable" or name == "cvVoIPPeerCfgVADEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgBitRate"):
                    self.cvvoippeercfgbitrate = value
                    self.cvvoippeercfgbitrate.value_namespace = name_space
                    self.cvvoippeercfgbitrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgBitRates"):
                    self.cvvoippeercfgbitrates[value] = True
                if(value_path == "cvVoIPPeerCfgCoderBytes"):
                    self.cvvoippeercfgcoderbytes = value
                    self.cvvoippeercfgcoderbytes.value_namespace = name_space
                    self.cvvoippeercfgcoderbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgCoderMode"):
                    self.cvvoippeercfgcodermode = value
                    self.cvvoippeercfgcodermode.value_namespace = name_space
                    self.cvvoippeercfgcodermode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgCoderRate"):
                    self.cvvoippeercfgcoderrate = value
                    self.cvvoippeercfgcoderrate.value_namespace = name_space
                    self.cvvoippeercfgcoderrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgCodingMode"):
                    self.cvvoippeercfgcodingmode = value
                    self.cvvoippeercfgcodingmode.value_namespace = name_space
                    self.cvvoippeercfgcodingmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgCRC"):
                    self.cvvoippeercfgcrc = value
                    self.cvvoippeercfgcrc.value_namespace = name_space
                    self.cvvoippeercfgcrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgDesiredQoS"):
                    self.cvvoippeercfgdesiredqos = value
                    self.cvvoippeercfgdesiredqos.value_namespace = name_space
                    self.cvvoippeercfgdesiredqos.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgDesiredQoSVideo"):
                    self.cvvoippeercfgdesiredqosvideo = value
                    self.cvvoippeercfgdesiredqosvideo.value_namespace = name_space
                    self.cvvoippeercfgdesiredqosvideo.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgDigitRelay"):
                    self.cvvoippeercfgdigitrelay[value] = True
                if(value_path == "cvVoIPPeerCfgDSCPPolicyNotificationEnable"):
                    self.cvvoippeercfgdscppolicynotificationenable = value
                    self.cvvoippeercfgdscppolicynotificationenable.value_namespace = name_space
                    self.cvvoippeercfgdscppolicynotificationenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgExpectFactor"):
                    self.cvvoippeercfgexpectfactor = value
                    self.cvvoippeercfgexpectfactor.value_namespace = name_space
                    self.cvvoippeercfgexpectfactor.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgFaxBytes"):
                    self.cvvoippeercfgfaxbytes = value
                    self.cvvoippeercfgfaxbytes.value_namespace = name_space
                    self.cvvoippeercfgfaxbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgFaxRate"):
                    self.cvvoippeercfgfaxrate = value
                    self.cvvoippeercfgfaxrate.value_namespace = name_space
                    self.cvvoippeercfgfaxrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgFrameSize"):
                    self.cvvoippeercfgframesize = value
                    self.cvvoippeercfgframesize.value_namespace = name_space
                    self.cvvoippeercfgframesize.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgIcpif"):
                    self.cvvoippeercfgicpif = value
                    self.cvvoippeercfgicpif.value_namespace = name_space
                    self.cvvoippeercfgicpif.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgInBandSignaling"):
                    self.cvvoippeercfginbandsignaling = value
                    self.cvvoippeercfginbandsignaling.value_namespace = name_space
                    self.cvvoippeercfginbandsignaling.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgIPPrecedence"):
                    self.cvvoippeercfgipprecedence = value
                    self.cvvoippeercfgipprecedence.value_namespace = name_space
                    self.cvvoippeercfgipprecedence.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgMediaPolicyNotificationEnable"):
                    self.cvvoippeercfgmediapolicynotificationenable = value
                    self.cvvoippeercfgmediapolicynotificationenable.value_namespace = name_space
                    self.cvvoippeercfgmediapolicynotificationenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgMediaSetting"):
                    self.cvvoippeercfgmediasetting = value
                    self.cvvoippeercfgmediasetting.value_namespace = name_space
                    self.cvvoippeercfgmediasetting.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgMinAcceptableQoS"):
                    self.cvvoippeercfgminacceptableqos = value
                    self.cvvoippeercfgminacceptableqos.value_namespace = name_space
                    self.cvvoippeercfgminacceptableqos.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgMinAcceptableQoSVideo"):
                    self.cvvoippeercfgminacceptableqosvideo = value
                    self.cvvoippeercfgminacceptableqosvideo.value_namespace = name_space
                    self.cvvoippeercfgminacceptableqosvideo.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgOctetAligned"):
                    self.cvvoippeercfgoctetaligned = value
                    self.cvvoippeercfgoctetaligned.value_namespace = name_space
                    self.cvvoippeercfgoctetaligned.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgPoorQoVNotificationEnable"):
                    self.cvvoippeercfgpoorqovnotificationenable = value
                    self.cvvoippeercfgpoorqovnotificationenable.value_namespace = name_space
                    self.cvvoippeercfgpoorqovnotificationenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgRedirectip2ip"):
                    self.cvvoippeercfgredirectip2ip = value
                    self.cvvoippeercfgredirectip2ip.value_namespace = name_space
                    self.cvvoippeercfgredirectip2ip.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgSessionProtocol"):
                    self.cvvoippeercfgsessionprotocol = value
                    self.cvvoippeercfgsessionprotocol.value_namespace = name_space
                    self.cvvoippeercfgsessionprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgSessionTarget"):
                    self.cvvoippeercfgsessiontarget = value
                    self.cvvoippeercfgsessiontarget.value_namespace = name_space
                    self.cvvoippeercfgsessiontarget.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgTechPrefix"):
                    self.cvvoippeercfgtechprefix = value
                    self.cvvoippeercfgtechprefix.value_namespace = name_space
                    self.cvvoippeercfgtechprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgUDPChecksumEnable"):
                    self.cvvoippeercfgudpchecksumenable = value
                    self.cvvoippeercfgudpchecksumenable.value_namespace = name_space
                    self.cvvoippeercfgudpchecksumenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPPeerCfgVADEnable"):
                    self.cvvoippeercfgvadenable = value
                    self.cvvoippeercfgvadenable.value_namespace = name_space
                    self.cvvoippeercfgvadenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvvoippeercfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvvoippeercfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvVoIPPeerCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvVoIPPeerCfgEntry"):
                for c in self.cvvoippeercfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvvoippeercfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvVoIPPeerCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpeercommoncfgtable(Entity):
        """
        The table contains the Voice specific peer common
        configuration information that is required to accept voice
        calls or to which it will place them or process the
        incoming calls.
        
        .. attribute:: cvpeercommoncfgentry
        
        	A single Voice specific Peer. One entry per voice related encapsulation. The entry is created when a voice related encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of    :py:class:`Cvpeercommoncfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable, self).__init__()

            self.yang_name = "cvPeerCommonCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvpeercommoncfgentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable, self).__setattr__(name, value)


        class Cvpeercommoncfgentry(Entity):
            """
            A single Voice specific Peer. One entry per voice related
            encapsulation.
            The entry is created when a voice related encapsulation
            ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cvpeercommoncfgapplicationname
            
            	The object specifies the application to handle the incoming call after the peer is selected. If no application name is specified, then the default session application will take care of the incoming call
            	**type**\:  str
            
            .. attribute:: cvpeercommoncfgdnismappingname
            
            	The object specifies a Dialer Number Identification Service (DNIS) map name for the Voice specific peer entry specified in this row. A DNIS is a called party number and they can be grouped and identified by DNIS map
            	**type**\:  str
            
            .. attribute:: cvpeercommoncfghuntstop
            
            	This object specifies whether dialpeer hunting should stop when this peer is reached
            	**type**\:  bool
            
            .. attribute:: cvpeercommoncfgincomingdnisdigits
            
            	The object specifies the prefix of the incoming Dialed Number Identification Service (DNIS) digits for the peer. The DNIS digits prefix is used to match with the incoming DNIS number for incoming call discrimination. If the digits in this object are matched with incoming DNIS number, the  associated dialCtlPeerCfgInfoType in RFC 2128 will be used as a call discriminator for differentiating speech, data, fax, video or modem calls
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: cvpeercommoncfgmaxconnections
            
            	The object specifies the maximum allowed connection to/from the peer. A value of \-1 disables the limit of maximum connections
            	**type**\:  int
            
            	**range:** \-1..None \| 1..2147483647
            
            	**units**\: connections
            
            .. attribute:: cvpeercommoncfgpreference
            
            	This object specifies the selection preference of a peer when multiple peers are matched to the selection criteria. The value of 0 has the lowest preference for peer selection
            	**type**\:  int
            
            	**range:** 0..10
            
            .. attribute:: cvpeercommoncfgsourcecarrierid
            
            	The object specifies the Source Carrier Id for the peer. The Source Carrier Id is used to match with the Source Carrier Id of a call. If the Source Carrier Id in this object is matched with the Source Carrier Id of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\:  str
            
            .. attribute:: cvpeercommoncfgsourcetrunkgrplabel
            
            	The object specifies the Source Trunk Group Label for the peer. The Source Trunk Group Label is used to match with the Source Trunk Group Label of a call. If the Source Trunk Group Label in this object is matched with the Source Trunk Group Label of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\:  str
            
            .. attribute:: cvpeercommoncfgtargetcarrierid
            
            	The object specifies the Target Carrier Id for the peer. The Target Carrier Id is used to match with the Target Carrier Id of a call. If the Target Carrier Id in this object is matched with the Target Carrier Id of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\:  str
            
            .. attribute:: cvpeercommoncfgtargettrunkgrplabel
            
            	The object specifies the Target Trunk Group Label for the peer. The Target Trunk Group Label is used to match with the Target Trunk Group Label of a call. If the Target Trunk Group Label in this object is matched with the Target Trunk Group Label of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry, self).__init__()

                self.yang_name = "cvPeerCommonCfgEntry"
                self.yang_parent_name = "cvPeerCommonCfgTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cvpeercommoncfgapplicationname = YLeaf(YType.str, "cvPeerCommonCfgApplicationName")

                self.cvpeercommoncfgdnismappingname = YLeaf(YType.str, "cvPeerCommonCfgDnisMappingName")

                self.cvpeercommoncfghuntstop = YLeaf(YType.boolean, "cvPeerCommonCfgHuntStop")

                self.cvpeercommoncfgincomingdnisdigits = YLeaf(YType.str, "cvPeerCommonCfgIncomingDnisDigits")

                self.cvpeercommoncfgmaxconnections = YLeaf(YType.int32, "cvPeerCommonCfgMaxConnections")

                self.cvpeercommoncfgpreference = YLeaf(YType.int32, "cvPeerCommonCfgPreference")

                self.cvpeercommoncfgsourcecarrierid = YLeaf(YType.str, "cvPeerCommonCfgSourceCarrierId")

                self.cvpeercommoncfgsourcetrunkgrplabel = YLeaf(YType.str, "cvPeerCommonCfgSourceTrunkGrpLabel")

                self.cvpeercommoncfgtargetcarrierid = YLeaf(YType.str, "cvPeerCommonCfgTargetCarrierId")

                self.cvpeercommoncfgtargettrunkgrplabel = YLeaf(YType.str, "cvPeerCommonCfgTargetTrunkGrpLabel")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cvpeercommoncfgapplicationname",
                                "cvpeercommoncfgdnismappingname",
                                "cvpeercommoncfghuntstop",
                                "cvpeercommoncfgincomingdnisdigits",
                                "cvpeercommoncfgmaxconnections",
                                "cvpeercommoncfgpreference",
                                "cvpeercommoncfgsourcecarrierid",
                                "cvpeercommoncfgsourcetrunkgrplabel",
                                "cvpeercommoncfgtargetcarrierid",
                                "cvpeercommoncfgtargettrunkgrplabel") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cvpeercommoncfgapplicationname.is_set or
                    self.cvpeercommoncfgdnismappingname.is_set or
                    self.cvpeercommoncfghuntstop.is_set or
                    self.cvpeercommoncfgincomingdnisdigits.is_set or
                    self.cvpeercommoncfgmaxconnections.is_set or
                    self.cvpeercommoncfgpreference.is_set or
                    self.cvpeercommoncfgsourcecarrierid.is_set or
                    self.cvpeercommoncfgsourcetrunkgrplabel.is_set or
                    self.cvpeercommoncfgtargetcarrierid.is_set or
                    self.cvpeercommoncfgtargettrunkgrplabel.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgapplicationname.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgdnismappingname.yfilter != YFilter.not_set or
                    self.cvpeercommoncfghuntstop.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgincomingdnisdigits.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgmaxconnections.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgpreference.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgsourcecarrierid.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgsourcetrunkgrplabel.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgtargetcarrierid.yfilter != YFilter.not_set or
                    self.cvpeercommoncfgtargettrunkgrplabel.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvPeerCommonCfgEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvPeerCommonCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cvpeercommoncfgapplicationname.is_set or self.cvpeercommoncfgapplicationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgapplicationname.get_name_leafdata())
                if (self.cvpeercommoncfgdnismappingname.is_set or self.cvpeercommoncfgdnismappingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgdnismappingname.get_name_leafdata())
                if (self.cvpeercommoncfghuntstop.is_set or self.cvpeercommoncfghuntstop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfghuntstop.get_name_leafdata())
                if (self.cvpeercommoncfgincomingdnisdigits.is_set or self.cvpeercommoncfgincomingdnisdigits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgincomingdnisdigits.get_name_leafdata())
                if (self.cvpeercommoncfgmaxconnections.is_set or self.cvpeercommoncfgmaxconnections.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgmaxconnections.get_name_leafdata())
                if (self.cvpeercommoncfgpreference.is_set or self.cvpeercommoncfgpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgpreference.get_name_leafdata())
                if (self.cvpeercommoncfgsourcecarrierid.is_set or self.cvpeercommoncfgsourcecarrierid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgsourcecarrierid.get_name_leafdata())
                if (self.cvpeercommoncfgsourcetrunkgrplabel.is_set or self.cvpeercommoncfgsourcetrunkgrplabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgsourcetrunkgrplabel.get_name_leafdata())
                if (self.cvpeercommoncfgtargetcarrierid.is_set or self.cvpeercommoncfgtargetcarrierid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgtargetcarrierid.get_name_leafdata())
                if (self.cvpeercommoncfgtargettrunkgrplabel.is_set or self.cvpeercommoncfgtargettrunkgrplabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpeercommoncfgtargettrunkgrplabel.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cvPeerCommonCfgApplicationName" or name == "cvPeerCommonCfgDnisMappingName" or name == "cvPeerCommonCfgHuntStop" or name == "cvPeerCommonCfgIncomingDnisDigits" or name == "cvPeerCommonCfgMaxConnections" or name == "cvPeerCommonCfgPreference" or name == "cvPeerCommonCfgSourceCarrierId" or name == "cvPeerCommonCfgSourceTrunkGrpLabel" or name == "cvPeerCommonCfgTargetCarrierId" or name == "cvPeerCommonCfgTargetTrunkGrpLabel"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgApplicationName"):
                    self.cvpeercommoncfgapplicationname = value
                    self.cvpeercommoncfgapplicationname.value_namespace = name_space
                    self.cvpeercommoncfgapplicationname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgDnisMappingName"):
                    self.cvpeercommoncfgdnismappingname = value
                    self.cvpeercommoncfgdnismappingname.value_namespace = name_space
                    self.cvpeercommoncfgdnismappingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgHuntStop"):
                    self.cvpeercommoncfghuntstop = value
                    self.cvpeercommoncfghuntstop.value_namespace = name_space
                    self.cvpeercommoncfghuntstop.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgIncomingDnisDigits"):
                    self.cvpeercommoncfgincomingdnisdigits = value
                    self.cvpeercommoncfgincomingdnisdigits.value_namespace = name_space
                    self.cvpeercommoncfgincomingdnisdigits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgMaxConnections"):
                    self.cvpeercommoncfgmaxconnections = value
                    self.cvpeercommoncfgmaxconnections.value_namespace = name_space
                    self.cvpeercommoncfgmaxconnections.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgPreference"):
                    self.cvpeercommoncfgpreference = value
                    self.cvpeercommoncfgpreference.value_namespace = name_space
                    self.cvpeercommoncfgpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgSourceCarrierId"):
                    self.cvpeercommoncfgsourcecarrierid = value
                    self.cvpeercommoncfgsourcecarrierid.value_namespace = name_space
                    self.cvpeercommoncfgsourcecarrierid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgSourceTrunkGrpLabel"):
                    self.cvpeercommoncfgsourcetrunkgrplabel = value
                    self.cvpeercommoncfgsourcetrunkgrplabel.value_namespace = name_space
                    self.cvpeercommoncfgsourcetrunkgrplabel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgTargetCarrierId"):
                    self.cvpeercommoncfgtargetcarrierid = value
                    self.cvpeercommoncfgtargetcarrierid.value_namespace = name_space
                    self.cvpeercommoncfgtargetcarrierid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvPeerCommonCfgTargetTrunkGrpLabel"):
                    self.cvpeercommoncfgtargettrunkgrplabel = value
                    self.cvpeercommoncfgtargettrunkgrplabel.value_namespace = name_space
                    self.cvpeercommoncfgtargettrunkgrplabel.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpeercommoncfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpeercommoncfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvPeerCommonCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvPeerCommonCfgEntry"):
                for c in self.cvpeercommoncfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpeercommoncfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvPeerCommonCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallactivetable(Entity):
        """
        This table is the voice extension to the call active table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information that is derived from the statistics
        of lower layer telephony interface.
        
        .. attribute:: cvcallactiveentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and call active entry contains the call establishment to a voice over telephony network peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvcallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallactivetable, self).__init__()

            self.yang_name = "cvCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallactiveentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallactivetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallactivetable, self).__setattr__(name, value)


        class Cvcallactiveentry(Entity):
            """
            The information regarding a single voice encapsulation
            call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            active entry in the IETF Dial Control MIB is created and
            call active entry contains the call establishment to a
            voice over telephony network peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: callactivesetuptime  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: cvcallactiveaccountcode
            
            	The object indicates the account code input to the call. It could be used for call screen or by down stream server for billing purpose. The value of empty string indicates no account code input
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: cvcallactiveacomlevel
            
            	The object contains the sum of Echo Return Loss (ERL), cancellation loss (Echo Return Loss Enhancement) and nonlinear processing loss for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\:  int
            
            	**range:** \-1..127
            
            	**units**\: dB
            
            .. attribute:: cvcallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\:  bool
            
            .. attribute:: cvcallactivecallid
            
            	This object represents the call identifier for the active telephony leg of the call
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcallactivecallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\:  str
            
            .. attribute:: cvcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            .. attribute:: cvcallactiveconnectionid
            
            	The global connection identifier for the active telephony leg of the call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcallactiveecanreflectorlocation
            
            	The location in milliseconds of the largest amplitude reflector detected by the echo canceller for this call.  The value 0 indicates there is no reflector or the  information is not available
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: cvcallactiveerllevel
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\:  int
            
            	**range:** \-1..45
            
            	**units**\: dB
            
            	**status**\: deprecated
            
            .. attribute:: cvcallactiveerllevelrev1
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\:  int
            
            	**range:** \-1..200
            
            	**units**\: dB
            
            .. attribute:: cvcallactivefaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallactiveimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: pages
            
            .. attribute:: cvcallactiveinsignallevel
            
            	The object contains the active input signal level from telephony interface that is used by the call leg
            	**type**\:  int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactivenoiselevel
            
            	The object contains the active noise level for the call leg
            	**type**\:  int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactiveoutsignallevel
            
            	The object contains the active output signal level to telephony interface that is used by the call leg
            	**type**\:  int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg. This object is set with the information in the call associated cvVoicePeerCfgSessionTarget object when the call is connected
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cvcallactivetxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallactivevoicetxduration
            
            	Duration of voice transmitted from this peer to voice gateway for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry, self).__init__()

                self.yang_name = "cvCallActiveEntry"
                self.yang_parent_name = "cvCallActiveTable"

                self.callactivesetuptime = YLeaf(YType.str, "callActiveSetupTime")

                self.callactiveindex = YLeaf(YType.str, "callActiveIndex")

                self.cvcallactiveaccountcode = YLeaf(YType.str, "cvCallActiveAccountCode")

                self.cvcallactiveacomlevel = YLeaf(YType.int32, "cvCallActiveACOMLevel")

                self.cvcallactivecalleridblock = YLeaf(YType.boolean, "cvCallActiveCallerIDBlock")

                self.cvcallactivecallid = YLeaf(YType.uint32, "cvCallActiveCallId")

                self.cvcallactivecallingname = YLeaf(YType.str, "cvCallActiveCallingName")

                self.cvcallactivecodertyperate = YLeaf(YType.enumeration, "cvCallActiveCoderTypeRate")

                self.cvcallactiveconnectionid = YLeaf(YType.str, "cvCallActiveConnectionId")

                self.cvcallactiveecanreflectorlocation = YLeaf(YType.int32, "cvCallActiveEcanReflectorLocation")

                self.cvcallactiveerllevel = YLeaf(YType.int32, "cvCallActiveERLLevel")

                self.cvcallactiveerllevelrev1 = YLeaf(YType.int32, "cvCallActiveERLLevelRev1")

                self.cvcallactivefaxtxduration = YLeaf(YType.uint32, "cvCallActiveFaxTxDuration")

                self.cvcallactiveimgpagecount = YLeaf(YType.uint32, "cvCallActiveImgPageCount")

                self.cvcallactiveinsignallevel = YLeaf(YType.int32, "cvCallActiveInSignalLevel")

                self.cvcallactivenoiselevel = YLeaf(YType.int32, "cvCallActiveNoiseLevel")

                self.cvcallactiveoutsignallevel = YLeaf(YType.int32, "cvCallActiveOutSignalLevel")

                self.cvcallactivesessiontarget = YLeaf(YType.str, "cvCallActiveSessionTarget")

                self.cvcallactivetxduration = YLeaf(YType.uint32, "cvCallActiveTxDuration")

                self.cvcallactivevoicetxduration = YLeaf(YType.uint32, "cvCallActiveVoiceTxDuration")

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
                                "cvcallactiveaccountcode",
                                "cvcallactiveacomlevel",
                                "cvcallactivecalleridblock",
                                "cvcallactivecallid",
                                "cvcallactivecallingname",
                                "cvcallactivecodertyperate",
                                "cvcallactiveconnectionid",
                                "cvcallactiveecanreflectorlocation",
                                "cvcallactiveerllevel",
                                "cvcallactiveerllevelrev1",
                                "cvcallactivefaxtxduration",
                                "cvcallactiveimgpagecount",
                                "cvcallactiveinsignallevel",
                                "cvcallactivenoiselevel",
                                "cvcallactiveoutsignallevel",
                                "cvcallactivesessiontarget",
                                "cvcallactivetxduration",
                                "cvcallactivevoicetxduration") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.callactivesetuptime.is_set or
                    self.callactiveindex.is_set or
                    self.cvcallactiveaccountcode.is_set or
                    self.cvcallactiveacomlevel.is_set or
                    self.cvcallactivecalleridblock.is_set or
                    self.cvcallactivecallid.is_set or
                    self.cvcallactivecallingname.is_set or
                    self.cvcallactivecodertyperate.is_set or
                    self.cvcallactiveconnectionid.is_set or
                    self.cvcallactiveecanreflectorlocation.is_set or
                    self.cvcallactiveerllevel.is_set or
                    self.cvcallactiveerllevelrev1.is_set or
                    self.cvcallactivefaxtxduration.is_set or
                    self.cvcallactiveimgpagecount.is_set or
                    self.cvcallactiveinsignallevel.is_set or
                    self.cvcallactivenoiselevel.is_set or
                    self.cvcallactiveoutsignallevel.is_set or
                    self.cvcallactivesessiontarget.is_set or
                    self.cvcallactivetxduration.is_set or
                    self.cvcallactivevoicetxduration.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.callactivesetuptime.yfilter != YFilter.not_set or
                    self.callactiveindex.yfilter != YFilter.not_set or
                    self.cvcallactiveaccountcode.yfilter != YFilter.not_set or
                    self.cvcallactiveacomlevel.yfilter != YFilter.not_set or
                    self.cvcallactivecalleridblock.yfilter != YFilter.not_set or
                    self.cvcallactivecallid.yfilter != YFilter.not_set or
                    self.cvcallactivecallingname.yfilter != YFilter.not_set or
                    self.cvcallactivecodertyperate.yfilter != YFilter.not_set or
                    self.cvcallactiveconnectionid.yfilter != YFilter.not_set or
                    self.cvcallactiveecanreflectorlocation.yfilter != YFilter.not_set or
                    self.cvcallactiveerllevel.yfilter != YFilter.not_set or
                    self.cvcallactiveerllevelrev1.yfilter != YFilter.not_set or
                    self.cvcallactivefaxtxduration.yfilter != YFilter.not_set or
                    self.cvcallactiveimgpagecount.yfilter != YFilter.not_set or
                    self.cvcallactiveinsignallevel.yfilter != YFilter.not_set or
                    self.cvcallactivenoiselevel.yfilter != YFilter.not_set or
                    self.cvcallactiveoutsignallevel.yfilter != YFilter.not_set or
                    self.cvcallactivesessiontarget.yfilter != YFilter.not_set or
                    self.cvcallactivetxduration.yfilter != YFilter.not_set or
                    self.cvcallactivevoicetxduration.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallActiveEntry" + "[callActiveSetupTime='" + self.callactivesetuptime.get() + "']" + "[callActiveIndex='" + self.callactiveindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallActiveTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.callactivesetuptime.is_set or self.callactivesetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivesetuptime.get_name_leafdata())
                if (self.callactiveindex.is_set or self.callactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveindex.get_name_leafdata())
                if (self.cvcallactiveaccountcode.is_set or self.cvcallactiveaccountcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveaccountcode.get_name_leafdata())
                if (self.cvcallactiveacomlevel.is_set or self.cvcallactiveacomlevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveacomlevel.get_name_leafdata())
                if (self.cvcallactivecalleridblock.is_set or self.cvcallactivecalleridblock.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivecalleridblock.get_name_leafdata())
                if (self.cvcallactivecallid.is_set or self.cvcallactivecallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivecallid.get_name_leafdata())
                if (self.cvcallactivecallingname.is_set or self.cvcallactivecallingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivecallingname.get_name_leafdata())
                if (self.cvcallactivecodertyperate.is_set or self.cvcallactivecodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivecodertyperate.get_name_leafdata())
                if (self.cvcallactiveconnectionid.is_set or self.cvcallactiveconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveconnectionid.get_name_leafdata())
                if (self.cvcallactiveecanreflectorlocation.is_set or self.cvcallactiveecanreflectorlocation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveecanreflectorlocation.get_name_leafdata())
                if (self.cvcallactiveerllevel.is_set or self.cvcallactiveerllevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveerllevel.get_name_leafdata())
                if (self.cvcallactiveerllevelrev1.is_set or self.cvcallactiveerllevelrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveerllevelrev1.get_name_leafdata())
                if (self.cvcallactivefaxtxduration.is_set or self.cvcallactivefaxtxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivefaxtxduration.get_name_leafdata())
                if (self.cvcallactiveimgpagecount.is_set or self.cvcallactiveimgpagecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveimgpagecount.get_name_leafdata())
                if (self.cvcallactiveinsignallevel.is_set or self.cvcallactiveinsignallevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveinsignallevel.get_name_leafdata())
                if (self.cvcallactivenoiselevel.is_set or self.cvcallactivenoiselevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivenoiselevel.get_name_leafdata())
                if (self.cvcallactiveoutsignallevel.is_set or self.cvcallactiveoutsignallevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactiveoutsignallevel.get_name_leafdata())
                if (self.cvcallactivesessiontarget.is_set or self.cvcallactivesessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivesessiontarget.get_name_leafdata())
                if (self.cvcallactivetxduration.is_set or self.cvcallactivetxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivetxduration.get_name_leafdata())
                if (self.cvcallactivevoicetxduration.is_set or self.cvcallactivevoicetxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallactivevoicetxduration.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callActiveSetupTime" or name == "callActiveIndex" or name == "cvCallActiveAccountCode" or name == "cvCallActiveACOMLevel" or name == "cvCallActiveCallerIDBlock" or name == "cvCallActiveCallId" or name == "cvCallActiveCallingName" or name == "cvCallActiveCoderTypeRate" or name == "cvCallActiveConnectionId" or name == "cvCallActiveEcanReflectorLocation" or name == "cvCallActiveERLLevel" or name == "cvCallActiveERLLevelRev1" or name == "cvCallActiveFaxTxDuration" or name == "cvCallActiveImgPageCount" or name == "cvCallActiveInSignalLevel" or name == "cvCallActiveNoiseLevel" or name == "cvCallActiveOutSignalLevel" or name == "cvCallActiveSessionTarget" or name == "cvCallActiveTxDuration" or name == "cvCallActiveVoiceTxDuration"):
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
                if(value_path == "cvCallActiveAccountCode"):
                    self.cvcallactiveaccountcode = value
                    self.cvcallactiveaccountcode.value_namespace = name_space
                    self.cvcallactiveaccountcode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveACOMLevel"):
                    self.cvcallactiveacomlevel = value
                    self.cvcallactiveacomlevel.value_namespace = name_space
                    self.cvcallactiveacomlevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveCallerIDBlock"):
                    self.cvcallactivecalleridblock = value
                    self.cvcallactivecalleridblock.value_namespace = name_space
                    self.cvcallactivecalleridblock.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveCallId"):
                    self.cvcallactivecallid = value
                    self.cvcallactivecallid.value_namespace = name_space
                    self.cvcallactivecallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveCallingName"):
                    self.cvcallactivecallingname = value
                    self.cvcallactivecallingname.value_namespace = name_space
                    self.cvcallactivecallingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveCoderTypeRate"):
                    self.cvcallactivecodertyperate = value
                    self.cvcallactivecodertyperate.value_namespace = name_space
                    self.cvcallactivecodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveConnectionId"):
                    self.cvcallactiveconnectionid = value
                    self.cvcallactiveconnectionid.value_namespace = name_space
                    self.cvcallactiveconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveEcanReflectorLocation"):
                    self.cvcallactiveecanreflectorlocation = value
                    self.cvcallactiveecanreflectorlocation.value_namespace = name_space
                    self.cvcallactiveecanreflectorlocation.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveERLLevel"):
                    self.cvcallactiveerllevel = value
                    self.cvcallactiveerllevel.value_namespace = name_space
                    self.cvcallactiveerllevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveERLLevelRev1"):
                    self.cvcallactiveerllevelrev1 = value
                    self.cvcallactiveerllevelrev1.value_namespace = name_space
                    self.cvcallactiveerllevelrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveFaxTxDuration"):
                    self.cvcallactivefaxtxduration = value
                    self.cvcallactivefaxtxduration.value_namespace = name_space
                    self.cvcallactivefaxtxduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveImgPageCount"):
                    self.cvcallactiveimgpagecount = value
                    self.cvcallactiveimgpagecount.value_namespace = name_space
                    self.cvcallactiveimgpagecount.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveInSignalLevel"):
                    self.cvcallactiveinsignallevel = value
                    self.cvcallactiveinsignallevel.value_namespace = name_space
                    self.cvcallactiveinsignallevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveNoiseLevel"):
                    self.cvcallactivenoiselevel = value
                    self.cvcallactivenoiselevel.value_namespace = name_space
                    self.cvcallactivenoiselevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveOutSignalLevel"):
                    self.cvcallactiveoutsignallevel = value
                    self.cvcallactiveoutsignallevel.value_namespace = name_space
                    self.cvcallactiveoutsignallevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveSessionTarget"):
                    self.cvcallactivesessiontarget = value
                    self.cvcallactivesessiontarget.value_namespace = name_space
                    self.cvcallactivesessiontarget.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveTxDuration"):
                    self.cvcallactivetxduration = value
                    self.cvcallactivetxduration.value_namespace = name_space
                    self.cvcallactivetxduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallActiveVoiceTxDuration"):
                    self.cvcallactivevoicetxduration = value
                    self.cvcallactivevoicetxduration.value_namespace = name_space
                    self.cvcallactivevoicetxduration.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallactiveentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallactiveentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallActiveTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallActiveEntry"):
                for c in self.cvcallactiveentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallactiveentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallActiveEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvvoipcallactivetable(Entity):
        """
        This table is the VoIP extension to the call active table of
        IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallactiveentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the call establishment to the peer on the IP backbone via a voice over  IP peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvvoipcallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvvoipcallactivetable, self).__init__()

            self.yang_name = "cvVoIPCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvvoipcallactiveentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvvoipcallactivetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvvoipcallactivetable, self).__setattr__(name, value)


        class Cvvoipcallactiveentry(Entity):
            """
            The information regarding a single VoIP call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            active entry in the IETF Dial Control MIB is created and
            the call active entry contains information for the call
            establishment to the peer on the IP backbone via a voice
            over  IP peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: callactivesetuptime  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: ccvoipcallactivepolicyname
            
            	This object holds the policy name. It could be media policy, DSCP policy etc
            	**type**\:  str
            
            .. attribute:: cvvoipcallactivebitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:   :py:class:`Cvamrnbbitratemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvamrnbbitratemode>`
            
            .. attribute:: cvvoipcallactivecallid
            
            	This object represents the call identifier for the active VoIP leg of the call
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallactivecallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.    For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivechannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..6
            
            	**units**\: channels
            
            .. attribute:: cvvoipcallactivecodermode
            
            	The object indicates the iLBC codec mode. The value of this object is valid only if  cvVoIPCallActiveCoderTypeRate is equal to  'iLBC'
            	**type**\:   :py:class:`Cvilbcframemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvilbcframemode>`
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactiveconnectionid
            
            	The global connection identifier for the active VoIP leg of the call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallactivecrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallactiveearlypackets
            
            	The number of received voice packets that arrived too early to store in jitter buffer during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactiveencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:   :py:class:`Cvamrnbrtpencap <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvamrnbrtpencap>`
            
            .. attribute:: cvvoipcallactivegapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivehiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactiveinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..50
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallactivelatepackets
            
            	The number of received voice packets that arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactivelostpackets
            
            	The number of lost voice packets during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactivelowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivemaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivemodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallActiveBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallActiveBitRates object. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallactivemodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallactiveoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallactiveontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactiveprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivereceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemMediaIPAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvvoipcallactiveremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactiveremoteipaddress
            
            	Remote system IP address for the VoIP call
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactiveremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactiveremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemSigIPAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvvoipcallactiveremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactivereverseddirectionpeeraddress
            
            	This object store the reversed direction peer address  If the address is not available, then it will have a length of zero.  If the call is ingress then it contains called number and if the call is egress then it contains calling number
            	**type**\:  str
            
            .. attribute:: cvvoipcallactiverobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallactiveroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactiveselectedqos
            
            	The selected RSVP QoS for the voice call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoipcallactivesessionid
            
            	This object indicates the active session ID assigned by the call manager to identify call legs that belong to the same call session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivesessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:   :py:class:`Cvsessionprotocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvsessionprotocol>`
            
            .. attribute:: cvvoipcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call. This object is set with the information in the call associated cvVoIPPeerCfgSessionTarget object when the voice over IP call is connected
            	**type**\:  str
            
            .. attribute:: cvvoipcallactivesrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\:  bool
            
            .. attribute:: cvvoipcallactiveusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\:  bool
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry, self).__init__()

                self.yang_name = "cvVoIPCallActiveEntry"
                self.yang_parent_name = "cvVoIPCallActiveTable"

                self.callactivesetuptime = YLeaf(YType.str, "callActiveSetupTime")

                self.callactiveindex = YLeaf(YType.str, "callActiveIndex")

                self.ccvoipcallactivepolicyname = YLeaf(YType.str, "ccVoIPCallActivePolicyName")

                self.cvvoipcallactivebitrates = YLeaf(YType.bits, "cvVoIPCallActiveBitRates")

                self.cvvoipcallactivecallid = YLeaf(YType.uint32, "cvVoIPCallActiveCallId")

                self.cvvoipcallactivecallreferenceid = YLeaf(YType.uint32, "cvVoIPCallActiveCallReferenceId")

                self.cvvoipcallactivechannels = YLeaf(YType.int32, "cvVoIPCallActiveChannels")

                self.cvvoipcallactivecodermode = YLeaf(YType.enumeration, "cvVoIPCallActiveCoderMode")

                self.cvvoipcallactivecodertyperate = YLeaf(YType.enumeration, "cvVoIPCallActiveCoderTypeRate")

                self.cvvoipcallactiveconnectionid = YLeaf(YType.str, "cvVoIPCallActiveConnectionId")

                self.cvvoipcallactivecrc = YLeaf(YType.boolean, "cvVoIPCallActiveCRC")

                self.cvvoipcallactiveearlypackets = YLeaf(YType.uint32, "cvVoIPCallActiveEarlyPackets")

                self.cvvoipcallactiveencap = YLeaf(YType.enumeration, "cvVoIPCallActiveEncap")

                self.cvvoipcallactivegapfillwithinterpolation = YLeaf(YType.uint32, "cvVoIPCallActiveGapFillWithInterpolation")

                self.cvvoipcallactivegapfillwithprediction = YLeaf(YType.uint32, "cvVoIPCallActiveGapFillWithPrediction")

                self.cvvoipcallactivegapfillwithredundancy = YLeaf(YType.uint32, "cvVoIPCallActiveGapFillWithRedundancy")

                self.cvvoipcallactivegapfillwithsilence = YLeaf(YType.uint32, "cvVoIPCallActiveGapFillWithSilence")

                self.cvvoipcallactivehiwaterplayoutdelay = YLeaf(YType.uint32, "cvVoIPCallActiveHiWaterPlayoutDelay")

                self.cvvoipcallactiveinterleaving = YLeaf(YType.int32, "cvVoIPCallActiveInterleaving")

                self.cvvoipcallactivelatepackets = YLeaf(YType.uint32, "cvVoIPCallActiveLatePackets")

                self.cvvoipcallactivelostpackets = YLeaf(YType.uint32, "cvVoIPCallActiveLostPackets")

                self.cvvoipcallactivelowaterplayoutdelay = YLeaf(YType.uint32, "cvVoIPCallActiveLoWaterPlayoutDelay")

                self.cvvoipcallactivemaxptime = YLeaf(YType.int32, "cvVoIPCallActiveMaxPtime")

                self.cvvoipcallactivemodechgneighbor = YLeaf(YType.boolean, "cvVoIPCallActiveModeChgNeighbor")

                self.cvvoipcallactivemodechgperiod = YLeaf(YType.int32, "cvVoIPCallActiveModeChgPeriod")

                self.cvvoipcallactiveoctetaligned = YLeaf(YType.boolean, "cvVoIPCallActiveOctetAligned")

                self.cvvoipcallactiveontimervplayout = YLeaf(YType.uint32, "cvVoIPCallActiveOnTimeRvPlayout")

                self.cvvoipcallactiveprotocolcallid = YLeaf(YType.str, "cvVoIPCallActiveProtocolCallId")

                self.cvvoipcallactiveptime = YLeaf(YType.int32, "cvVoIPCallActivePtime")

                self.cvvoipcallactivereceivedelay = YLeaf(YType.uint32, "cvVoIPCallActiveReceiveDelay")

                self.cvvoipcallactiveremmediaipaddr = YLeaf(YType.str, "cvVoIPCallActiveRemMediaIPAddr")

                self.cvvoipcallactiveremmediaipaddrt = YLeaf(YType.enumeration, "cvVoIPCallActiveRemMediaIPAddrT")

                self.cvvoipcallactiveremmediaport = YLeaf(YType.int32, "cvVoIPCallActiveRemMediaPort")

                self.cvvoipcallactiveremoteipaddress = YLeaf(YType.str, "cvVoIPCallActiveRemoteIPAddress")

                self.cvvoipcallactiveremoteudpport = YLeaf(YType.int32, "cvVoIPCallActiveRemoteUDPPort")

                self.cvvoipcallactiveremsigipaddr = YLeaf(YType.str, "cvVoIPCallActiveRemSigIPAddr")

                self.cvvoipcallactiveremsigipaddrt = YLeaf(YType.enumeration, "cvVoIPCallActiveRemSigIPAddrT")

                self.cvvoipcallactiveremsigport = YLeaf(YType.int32, "cvVoIPCallActiveRemSigPort")

                self.cvvoipcallactivereverseddirectionpeeraddress = YLeaf(YType.str, "cvVoIPCallActiveReversedDirectionPeerAddress")

                self.cvvoipcallactiverobustsorting = YLeaf(YType.boolean, "cvVoIPCallActiveRobustSorting")

                self.cvvoipcallactiveroundtripdelay = YLeaf(YType.uint32, "cvVoIPCallActiveRoundTripDelay")

                self.cvvoipcallactiveselectedqos = YLeaf(YType.enumeration, "cvVoIPCallActiveSelectedQoS")

                self.cvvoipcallactivesessionid = YLeaf(YType.uint32, "cvVoIPCallActiveSessionId")

                self.cvvoipcallactivesessionprotocol = YLeaf(YType.enumeration, "cvVoIPCallActiveSessionProtocol")

                self.cvvoipcallactivesessiontarget = YLeaf(YType.str, "cvVoIPCallActiveSessionTarget")

                self.cvvoipcallactivesrtpenable = YLeaf(YType.boolean, "cvVoIPCallActiveSRTPEnable")

                self.cvvoipcallactiveusername = YLeaf(YType.str, "cvVoIPCallActiveUsername")

                self.cvvoipcallactivevadenable = YLeaf(YType.boolean, "cvVoIPCallActiveVADEnable")

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
                                "ccvoipcallactivepolicyname",
                                "cvvoipcallactivebitrates",
                                "cvvoipcallactivecallid",
                                "cvvoipcallactivecallreferenceid",
                                "cvvoipcallactivechannels",
                                "cvvoipcallactivecodermode",
                                "cvvoipcallactivecodertyperate",
                                "cvvoipcallactiveconnectionid",
                                "cvvoipcallactivecrc",
                                "cvvoipcallactiveearlypackets",
                                "cvvoipcallactiveencap",
                                "cvvoipcallactivegapfillwithinterpolation",
                                "cvvoipcallactivegapfillwithprediction",
                                "cvvoipcallactivegapfillwithredundancy",
                                "cvvoipcallactivegapfillwithsilence",
                                "cvvoipcallactivehiwaterplayoutdelay",
                                "cvvoipcallactiveinterleaving",
                                "cvvoipcallactivelatepackets",
                                "cvvoipcallactivelostpackets",
                                "cvvoipcallactivelowaterplayoutdelay",
                                "cvvoipcallactivemaxptime",
                                "cvvoipcallactivemodechgneighbor",
                                "cvvoipcallactivemodechgperiod",
                                "cvvoipcallactiveoctetaligned",
                                "cvvoipcallactiveontimervplayout",
                                "cvvoipcallactiveprotocolcallid",
                                "cvvoipcallactiveptime",
                                "cvvoipcallactivereceivedelay",
                                "cvvoipcallactiveremmediaipaddr",
                                "cvvoipcallactiveremmediaipaddrt",
                                "cvvoipcallactiveremmediaport",
                                "cvvoipcallactiveremoteipaddress",
                                "cvvoipcallactiveremoteudpport",
                                "cvvoipcallactiveremsigipaddr",
                                "cvvoipcallactiveremsigipaddrt",
                                "cvvoipcallactiveremsigport",
                                "cvvoipcallactivereverseddirectionpeeraddress",
                                "cvvoipcallactiverobustsorting",
                                "cvvoipcallactiveroundtripdelay",
                                "cvvoipcallactiveselectedqos",
                                "cvvoipcallactivesessionid",
                                "cvvoipcallactivesessionprotocol",
                                "cvvoipcallactivesessiontarget",
                                "cvvoipcallactivesrtpenable",
                                "cvvoipcallactiveusername",
                                "cvvoipcallactivevadenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.callactivesetuptime.is_set or
                    self.callactiveindex.is_set or
                    self.ccvoipcallactivepolicyname.is_set or
                    self.cvvoipcallactivebitrates.is_set or
                    self.cvvoipcallactivecallid.is_set or
                    self.cvvoipcallactivecallreferenceid.is_set or
                    self.cvvoipcallactivechannels.is_set or
                    self.cvvoipcallactivecodermode.is_set or
                    self.cvvoipcallactivecodertyperate.is_set or
                    self.cvvoipcallactiveconnectionid.is_set or
                    self.cvvoipcallactivecrc.is_set or
                    self.cvvoipcallactiveearlypackets.is_set or
                    self.cvvoipcallactiveencap.is_set or
                    self.cvvoipcallactivegapfillwithinterpolation.is_set or
                    self.cvvoipcallactivegapfillwithprediction.is_set or
                    self.cvvoipcallactivegapfillwithredundancy.is_set or
                    self.cvvoipcallactivegapfillwithsilence.is_set or
                    self.cvvoipcallactivehiwaterplayoutdelay.is_set or
                    self.cvvoipcallactiveinterleaving.is_set or
                    self.cvvoipcallactivelatepackets.is_set or
                    self.cvvoipcallactivelostpackets.is_set or
                    self.cvvoipcallactivelowaterplayoutdelay.is_set or
                    self.cvvoipcallactivemaxptime.is_set or
                    self.cvvoipcallactivemodechgneighbor.is_set or
                    self.cvvoipcallactivemodechgperiod.is_set or
                    self.cvvoipcallactiveoctetaligned.is_set or
                    self.cvvoipcallactiveontimervplayout.is_set or
                    self.cvvoipcallactiveprotocolcallid.is_set or
                    self.cvvoipcallactiveptime.is_set or
                    self.cvvoipcallactivereceivedelay.is_set or
                    self.cvvoipcallactiveremmediaipaddr.is_set or
                    self.cvvoipcallactiveremmediaipaddrt.is_set or
                    self.cvvoipcallactiveremmediaport.is_set or
                    self.cvvoipcallactiveremoteipaddress.is_set or
                    self.cvvoipcallactiveremoteudpport.is_set or
                    self.cvvoipcallactiveremsigipaddr.is_set or
                    self.cvvoipcallactiveremsigipaddrt.is_set or
                    self.cvvoipcallactiveremsigport.is_set or
                    self.cvvoipcallactivereverseddirectionpeeraddress.is_set or
                    self.cvvoipcallactiverobustsorting.is_set or
                    self.cvvoipcallactiveroundtripdelay.is_set or
                    self.cvvoipcallactiveselectedqos.is_set or
                    self.cvvoipcallactivesessionid.is_set or
                    self.cvvoipcallactivesessionprotocol.is_set or
                    self.cvvoipcallactivesessiontarget.is_set or
                    self.cvvoipcallactivesrtpenable.is_set or
                    self.cvvoipcallactiveusername.is_set or
                    self.cvvoipcallactivevadenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.callactivesetuptime.yfilter != YFilter.not_set or
                    self.callactiveindex.yfilter != YFilter.not_set or
                    self.ccvoipcallactivepolicyname.yfilter != YFilter.not_set or
                    self.cvvoipcallactivebitrates.yfilter != YFilter.not_set or
                    self.cvvoipcallactivecallid.yfilter != YFilter.not_set or
                    self.cvvoipcallactivecallreferenceid.yfilter != YFilter.not_set or
                    self.cvvoipcallactivechannels.yfilter != YFilter.not_set or
                    self.cvvoipcallactivecodermode.yfilter != YFilter.not_set or
                    self.cvvoipcallactivecodertyperate.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveconnectionid.yfilter != YFilter.not_set or
                    self.cvvoipcallactivecrc.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveearlypackets.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveencap.yfilter != YFilter.not_set or
                    self.cvvoipcallactivegapfillwithinterpolation.yfilter != YFilter.not_set or
                    self.cvvoipcallactivegapfillwithprediction.yfilter != YFilter.not_set or
                    self.cvvoipcallactivegapfillwithredundancy.yfilter != YFilter.not_set or
                    self.cvvoipcallactivegapfillwithsilence.yfilter != YFilter.not_set or
                    self.cvvoipcallactivehiwaterplayoutdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveinterleaving.yfilter != YFilter.not_set or
                    self.cvvoipcallactivelatepackets.yfilter != YFilter.not_set or
                    self.cvvoipcallactivelostpackets.yfilter != YFilter.not_set or
                    self.cvvoipcallactivelowaterplayoutdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallactivemaxptime.yfilter != YFilter.not_set or
                    self.cvvoipcallactivemodechgneighbor.yfilter != YFilter.not_set or
                    self.cvvoipcallactivemodechgperiod.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveoctetaligned.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveontimervplayout.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveprotocolcallid.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveptime.yfilter != YFilter.not_set or
                    self.cvvoipcallactivereceivedelay.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremmediaipaddr.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremmediaipaddrt.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremmediaport.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremoteipaddress.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremoteudpport.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremsigipaddr.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremsigipaddrt.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveremsigport.yfilter != YFilter.not_set or
                    self.cvvoipcallactivereverseddirectionpeeraddress.yfilter != YFilter.not_set or
                    self.cvvoipcallactiverobustsorting.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveroundtripdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveselectedqos.yfilter != YFilter.not_set or
                    self.cvvoipcallactivesessionid.yfilter != YFilter.not_set or
                    self.cvvoipcallactivesessionprotocol.yfilter != YFilter.not_set or
                    self.cvvoipcallactivesessiontarget.yfilter != YFilter.not_set or
                    self.cvvoipcallactivesrtpenable.yfilter != YFilter.not_set or
                    self.cvvoipcallactiveusername.yfilter != YFilter.not_set or
                    self.cvvoipcallactivevadenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvVoIPCallActiveEntry" + "[callActiveSetupTime='" + self.callactivesetuptime.get() + "']" + "[callActiveIndex='" + self.callactiveindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPCallActiveTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.callactivesetuptime.is_set or self.callactivesetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivesetuptime.get_name_leafdata())
                if (self.callactiveindex.is_set or self.callactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveindex.get_name_leafdata())
                if (self.ccvoipcallactivepolicyname.is_set or self.ccvoipcallactivepolicyname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccvoipcallactivepolicyname.get_name_leafdata())
                if (self.cvvoipcallactivebitrates.is_set or self.cvvoipcallactivebitrates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivebitrates.get_name_leafdata())
                if (self.cvvoipcallactivecallid.is_set or self.cvvoipcallactivecallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivecallid.get_name_leafdata())
                if (self.cvvoipcallactivecallreferenceid.is_set or self.cvvoipcallactivecallreferenceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivecallreferenceid.get_name_leafdata())
                if (self.cvvoipcallactivechannels.is_set or self.cvvoipcallactivechannels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivechannels.get_name_leafdata())
                if (self.cvvoipcallactivecodermode.is_set or self.cvvoipcallactivecodermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivecodermode.get_name_leafdata())
                if (self.cvvoipcallactivecodertyperate.is_set or self.cvvoipcallactivecodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivecodertyperate.get_name_leafdata())
                if (self.cvvoipcallactiveconnectionid.is_set or self.cvvoipcallactiveconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveconnectionid.get_name_leafdata())
                if (self.cvvoipcallactivecrc.is_set or self.cvvoipcallactivecrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivecrc.get_name_leafdata())
                if (self.cvvoipcallactiveearlypackets.is_set or self.cvvoipcallactiveearlypackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveearlypackets.get_name_leafdata())
                if (self.cvvoipcallactiveencap.is_set or self.cvvoipcallactiveencap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveencap.get_name_leafdata())
                if (self.cvvoipcallactivegapfillwithinterpolation.is_set or self.cvvoipcallactivegapfillwithinterpolation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivegapfillwithinterpolation.get_name_leafdata())
                if (self.cvvoipcallactivegapfillwithprediction.is_set or self.cvvoipcallactivegapfillwithprediction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivegapfillwithprediction.get_name_leafdata())
                if (self.cvvoipcallactivegapfillwithredundancy.is_set or self.cvvoipcallactivegapfillwithredundancy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivegapfillwithredundancy.get_name_leafdata())
                if (self.cvvoipcallactivegapfillwithsilence.is_set or self.cvvoipcallactivegapfillwithsilence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivegapfillwithsilence.get_name_leafdata())
                if (self.cvvoipcallactivehiwaterplayoutdelay.is_set or self.cvvoipcallactivehiwaterplayoutdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivehiwaterplayoutdelay.get_name_leafdata())
                if (self.cvvoipcallactiveinterleaving.is_set or self.cvvoipcallactiveinterleaving.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveinterleaving.get_name_leafdata())
                if (self.cvvoipcallactivelatepackets.is_set or self.cvvoipcallactivelatepackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivelatepackets.get_name_leafdata())
                if (self.cvvoipcallactivelostpackets.is_set or self.cvvoipcallactivelostpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivelostpackets.get_name_leafdata())
                if (self.cvvoipcallactivelowaterplayoutdelay.is_set or self.cvvoipcallactivelowaterplayoutdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivelowaterplayoutdelay.get_name_leafdata())
                if (self.cvvoipcallactivemaxptime.is_set or self.cvvoipcallactivemaxptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivemaxptime.get_name_leafdata())
                if (self.cvvoipcallactivemodechgneighbor.is_set or self.cvvoipcallactivemodechgneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivemodechgneighbor.get_name_leafdata())
                if (self.cvvoipcallactivemodechgperiod.is_set or self.cvvoipcallactivemodechgperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivemodechgperiod.get_name_leafdata())
                if (self.cvvoipcallactiveoctetaligned.is_set or self.cvvoipcallactiveoctetaligned.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveoctetaligned.get_name_leafdata())
                if (self.cvvoipcallactiveontimervplayout.is_set or self.cvvoipcallactiveontimervplayout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveontimervplayout.get_name_leafdata())
                if (self.cvvoipcallactiveprotocolcallid.is_set or self.cvvoipcallactiveprotocolcallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveprotocolcallid.get_name_leafdata())
                if (self.cvvoipcallactiveptime.is_set or self.cvvoipcallactiveptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveptime.get_name_leafdata())
                if (self.cvvoipcallactivereceivedelay.is_set or self.cvvoipcallactivereceivedelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivereceivedelay.get_name_leafdata())
                if (self.cvvoipcallactiveremmediaipaddr.is_set or self.cvvoipcallactiveremmediaipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremmediaipaddr.get_name_leafdata())
                if (self.cvvoipcallactiveremmediaipaddrt.is_set or self.cvvoipcallactiveremmediaipaddrt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremmediaipaddrt.get_name_leafdata())
                if (self.cvvoipcallactiveremmediaport.is_set or self.cvvoipcallactiveremmediaport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremmediaport.get_name_leafdata())
                if (self.cvvoipcallactiveremoteipaddress.is_set or self.cvvoipcallactiveremoteipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremoteipaddress.get_name_leafdata())
                if (self.cvvoipcallactiveremoteudpport.is_set or self.cvvoipcallactiveremoteudpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremoteudpport.get_name_leafdata())
                if (self.cvvoipcallactiveremsigipaddr.is_set or self.cvvoipcallactiveremsigipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremsigipaddr.get_name_leafdata())
                if (self.cvvoipcallactiveremsigipaddrt.is_set or self.cvvoipcallactiveremsigipaddrt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremsigipaddrt.get_name_leafdata())
                if (self.cvvoipcallactiveremsigport.is_set or self.cvvoipcallactiveremsigport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveremsigport.get_name_leafdata())
                if (self.cvvoipcallactivereverseddirectionpeeraddress.is_set or self.cvvoipcallactivereverseddirectionpeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivereverseddirectionpeeraddress.get_name_leafdata())
                if (self.cvvoipcallactiverobustsorting.is_set or self.cvvoipcallactiverobustsorting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiverobustsorting.get_name_leafdata())
                if (self.cvvoipcallactiveroundtripdelay.is_set or self.cvvoipcallactiveroundtripdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveroundtripdelay.get_name_leafdata())
                if (self.cvvoipcallactiveselectedqos.is_set or self.cvvoipcallactiveselectedqos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveselectedqos.get_name_leafdata())
                if (self.cvvoipcallactivesessionid.is_set or self.cvvoipcallactivesessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivesessionid.get_name_leafdata())
                if (self.cvvoipcallactivesessionprotocol.is_set or self.cvvoipcallactivesessionprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivesessionprotocol.get_name_leafdata())
                if (self.cvvoipcallactivesessiontarget.is_set or self.cvvoipcallactivesessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivesessiontarget.get_name_leafdata())
                if (self.cvvoipcallactivesrtpenable.is_set or self.cvvoipcallactivesrtpenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivesrtpenable.get_name_leafdata())
                if (self.cvvoipcallactiveusername.is_set or self.cvvoipcallactiveusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactiveusername.get_name_leafdata())
                if (self.cvvoipcallactivevadenable.is_set or self.cvvoipcallactivevadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallactivevadenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callActiveSetupTime" or name == "callActiveIndex" or name == "ccVoIPCallActivePolicyName" or name == "cvVoIPCallActiveBitRates" or name == "cvVoIPCallActiveCallId" or name == "cvVoIPCallActiveCallReferenceId" or name == "cvVoIPCallActiveChannels" or name == "cvVoIPCallActiveCoderMode" or name == "cvVoIPCallActiveCoderTypeRate" or name == "cvVoIPCallActiveConnectionId" or name == "cvVoIPCallActiveCRC" or name == "cvVoIPCallActiveEarlyPackets" or name == "cvVoIPCallActiveEncap" or name == "cvVoIPCallActiveGapFillWithInterpolation" or name == "cvVoIPCallActiveGapFillWithPrediction" or name == "cvVoIPCallActiveGapFillWithRedundancy" or name == "cvVoIPCallActiveGapFillWithSilence" or name == "cvVoIPCallActiveHiWaterPlayoutDelay" or name == "cvVoIPCallActiveInterleaving" or name == "cvVoIPCallActiveLatePackets" or name == "cvVoIPCallActiveLostPackets" or name == "cvVoIPCallActiveLoWaterPlayoutDelay" or name == "cvVoIPCallActiveMaxPtime" or name == "cvVoIPCallActiveModeChgNeighbor" or name == "cvVoIPCallActiveModeChgPeriod" or name == "cvVoIPCallActiveOctetAligned" or name == "cvVoIPCallActiveOnTimeRvPlayout" or name == "cvVoIPCallActiveProtocolCallId" or name == "cvVoIPCallActivePtime" or name == "cvVoIPCallActiveReceiveDelay" or name == "cvVoIPCallActiveRemMediaIPAddr" or name == "cvVoIPCallActiveRemMediaIPAddrT" or name == "cvVoIPCallActiveRemMediaPort" or name == "cvVoIPCallActiveRemoteIPAddress" or name == "cvVoIPCallActiveRemoteUDPPort" or name == "cvVoIPCallActiveRemSigIPAddr" or name == "cvVoIPCallActiveRemSigIPAddrT" or name == "cvVoIPCallActiveRemSigPort" or name == "cvVoIPCallActiveReversedDirectionPeerAddress" or name == "cvVoIPCallActiveRobustSorting" or name == "cvVoIPCallActiveRoundTripDelay" or name == "cvVoIPCallActiveSelectedQoS" or name == "cvVoIPCallActiveSessionId" or name == "cvVoIPCallActiveSessionProtocol" or name == "cvVoIPCallActiveSessionTarget" or name == "cvVoIPCallActiveSRTPEnable" or name == "cvVoIPCallActiveUsername" or name == "cvVoIPCallActiveVADEnable"):
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
                if(value_path == "ccVoIPCallActivePolicyName"):
                    self.ccvoipcallactivepolicyname = value
                    self.ccvoipcallactivepolicyname.value_namespace = name_space
                    self.ccvoipcallactivepolicyname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveBitRates"):
                    self.cvvoipcallactivebitrates[value] = True
                if(value_path == "cvVoIPCallActiveCallId"):
                    self.cvvoipcallactivecallid = value
                    self.cvvoipcallactivecallid.value_namespace = name_space
                    self.cvvoipcallactivecallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveCallReferenceId"):
                    self.cvvoipcallactivecallreferenceid = value
                    self.cvvoipcallactivecallreferenceid.value_namespace = name_space
                    self.cvvoipcallactivecallreferenceid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveChannels"):
                    self.cvvoipcallactivechannels = value
                    self.cvvoipcallactivechannels.value_namespace = name_space
                    self.cvvoipcallactivechannels.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveCoderMode"):
                    self.cvvoipcallactivecodermode = value
                    self.cvvoipcallactivecodermode.value_namespace = name_space
                    self.cvvoipcallactivecodermode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveCoderTypeRate"):
                    self.cvvoipcallactivecodertyperate = value
                    self.cvvoipcallactivecodertyperate.value_namespace = name_space
                    self.cvvoipcallactivecodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveConnectionId"):
                    self.cvvoipcallactiveconnectionid = value
                    self.cvvoipcallactiveconnectionid.value_namespace = name_space
                    self.cvvoipcallactiveconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveCRC"):
                    self.cvvoipcallactivecrc = value
                    self.cvvoipcallactivecrc.value_namespace = name_space
                    self.cvvoipcallactivecrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveEarlyPackets"):
                    self.cvvoipcallactiveearlypackets = value
                    self.cvvoipcallactiveearlypackets.value_namespace = name_space
                    self.cvvoipcallactiveearlypackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveEncap"):
                    self.cvvoipcallactiveencap = value
                    self.cvvoipcallactiveencap.value_namespace = name_space
                    self.cvvoipcallactiveencap.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveGapFillWithInterpolation"):
                    self.cvvoipcallactivegapfillwithinterpolation = value
                    self.cvvoipcallactivegapfillwithinterpolation.value_namespace = name_space
                    self.cvvoipcallactivegapfillwithinterpolation.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveGapFillWithPrediction"):
                    self.cvvoipcallactivegapfillwithprediction = value
                    self.cvvoipcallactivegapfillwithprediction.value_namespace = name_space
                    self.cvvoipcallactivegapfillwithprediction.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveGapFillWithRedundancy"):
                    self.cvvoipcallactivegapfillwithredundancy = value
                    self.cvvoipcallactivegapfillwithredundancy.value_namespace = name_space
                    self.cvvoipcallactivegapfillwithredundancy.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveGapFillWithSilence"):
                    self.cvvoipcallactivegapfillwithsilence = value
                    self.cvvoipcallactivegapfillwithsilence.value_namespace = name_space
                    self.cvvoipcallactivegapfillwithsilence.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveHiWaterPlayoutDelay"):
                    self.cvvoipcallactivehiwaterplayoutdelay = value
                    self.cvvoipcallactivehiwaterplayoutdelay.value_namespace = name_space
                    self.cvvoipcallactivehiwaterplayoutdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveInterleaving"):
                    self.cvvoipcallactiveinterleaving = value
                    self.cvvoipcallactiveinterleaving.value_namespace = name_space
                    self.cvvoipcallactiveinterleaving.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveLatePackets"):
                    self.cvvoipcallactivelatepackets = value
                    self.cvvoipcallactivelatepackets.value_namespace = name_space
                    self.cvvoipcallactivelatepackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveLostPackets"):
                    self.cvvoipcallactivelostpackets = value
                    self.cvvoipcallactivelostpackets.value_namespace = name_space
                    self.cvvoipcallactivelostpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveLoWaterPlayoutDelay"):
                    self.cvvoipcallactivelowaterplayoutdelay = value
                    self.cvvoipcallactivelowaterplayoutdelay.value_namespace = name_space
                    self.cvvoipcallactivelowaterplayoutdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveMaxPtime"):
                    self.cvvoipcallactivemaxptime = value
                    self.cvvoipcallactivemaxptime.value_namespace = name_space
                    self.cvvoipcallactivemaxptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveModeChgNeighbor"):
                    self.cvvoipcallactivemodechgneighbor = value
                    self.cvvoipcallactivemodechgneighbor.value_namespace = name_space
                    self.cvvoipcallactivemodechgneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveModeChgPeriod"):
                    self.cvvoipcallactivemodechgperiod = value
                    self.cvvoipcallactivemodechgperiod.value_namespace = name_space
                    self.cvvoipcallactivemodechgperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveOctetAligned"):
                    self.cvvoipcallactiveoctetaligned = value
                    self.cvvoipcallactiveoctetaligned.value_namespace = name_space
                    self.cvvoipcallactiveoctetaligned.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveOnTimeRvPlayout"):
                    self.cvvoipcallactiveontimervplayout = value
                    self.cvvoipcallactiveontimervplayout.value_namespace = name_space
                    self.cvvoipcallactiveontimervplayout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveProtocolCallId"):
                    self.cvvoipcallactiveprotocolcallid = value
                    self.cvvoipcallactiveprotocolcallid.value_namespace = name_space
                    self.cvvoipcallactiveprotocolcallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActivePtime"):
                    self.cvvoipcallactiveptime = value
                    self.cvvoipcallactiveptime.value_namespace = name_space
                    self.cvvoipcallactiveptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveReceiveDelay"):
                    self.cvvoipcallactivereceivedelay = value
                    self.cvvoipcallactivereceivedelay.value_namespace = name_space
                    self.cvvoipcallactivereceivedelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemMediaIPAddr"):
                    self.cvvoipcallactiveremmediaipaddr = value
                    self.cvvoipcallactiveremmediaipaddr.value_namespace = name_space
                    self.cvvoipcallactiveremmediaipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemMediaIPAddrT"):
                    self.cvvoipcallactiveremmediaipaddrt = value
                    self.cvvoipcallactiveremmediaipaddrt.value_namespace = name_space
                    self.cvvoipcallactiveremmediaipaddrt.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemMediaPort"):
                    self.cvvoipcallactiveremmediaport = value
                    self.cvvoipcallactiveremmediaport.value_namespace = name_space
                    self.cvvoipcallactiveremmediaport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemoteIPAddress"):
                    self.cvvoipcallactiveremoteipaddress = value
                    self.cvvoipcallactiveremoteipaddress.value_namespace = name_space
                    self.cvvoipcallactiveremoteipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemoteUDPPort"):
                    self.cvvoipcallactiveremoteudpport = value
                    self.cvvoipcallactiveremoteudpport.value_namespace = name_space
                    self.cvvoipcallactiveremoteudpport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemSigIPAddr"):
                    self.cvvoipcallactiveremsigipaddr = value
                    self.cvvoipcallactiveremsigipaddr.value_namespace = name_space
                    self.cvvoipcallactiveremsigipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemSigIPAddrT"):
                    self.cvvoipcallactiveremsigipaddrt = value
                    self.cvvoipcallactiveremsigipaddrt.value_namespace = name_space
                    self.cvvoipcallactiveremsigipaddrt.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRemSigPort"):
                    self.cvvoipcallactiveremsigport = value
                    self.cvvoipcallactiveremsigport.value_namespace = name_space
                    self.cvvoipcallactiveremsigport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveReversedDirectionPeerAddress"):
                    self.cvvoipcallactivereverseddirectionpeeraddress = value
                    self.cvvoipcallactivereverseddirectionpeeraddress.value_namespace = name_space
                    self.cvvoipcallactivereverseddirectionpeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRobustSorting"):
                    self.cvvoipcallactiverobustsorting = value
                    self.cvvoipcallactiverobustsorting.value_namespace = name_space
                    self.cvvoipcallactiverobustsorting.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveRoundTripDelay"):
                    self.cvvoipcallactiveroundtripdelay = value
                    self.cvvoipcallactiveroundtripdelay.value_namespace = name_space
                    self.cvvoipcallactiveroundtripdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveSelectedQoS"):
                    self.cvvoipcallactiveselectedqos = value
                    self.cvvoipcallactiveselectedqos.value_namespace = name_space
                    self.cvvoipcallactiveselectedqos.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveSessionId"):
                    self.cvvoipcallactivesessionid = value
                    self.cvvoipcallactivesessionid.value_namespace = name_space
                    self.cvvoipcallactivesessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveSessionProtocol"):
                    self.cvvoipcallactivesessionprotocol = value
                    self.cvvoipcallactivesessionprotocol.value_namespace = name_space
                    self.cvvoipcallactivesessionprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveSessionTarget"):
                    self.cvvoipcallactivesessiontarget = value
                    self.cvvoipcallactivesessiontarget.value_namespace = name_space
                    self.cvvoipcallactivesessiontarget.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveSRTPEnable"):
                    self.cvvoipcallactivesrtpenable = value
                    self.cvvoipcallactivesrtpenable.value_namespace = name_space
                    self.cvvoipcallactivesrtpenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveUsername"):
                    self.cvvoipcallactiveusername = value
                    self.cvvoipcallactiveusername.value_namespace = name_space
                    self.cvvoipcallactiveusername.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallActiveVADEnable"):
                    self.cvvoipcallactivevadenable = value
                    self.cvvoipcallactivevadenable.value_namespace = name_space
                    self.cvvoipcallactivevadenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvvoipcallactiveentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvvoipcallactiveentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvVoIPCallActiveTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvVoIPCallActiveEntry"):
                for c in self.cvvoipcallactiveentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvvoipcallactiveentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvVoIPCallActiveEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallvolconntable(Entity):
        """
        This table represents the number of active
        call connections for each call connection type
        in the voice gateway.
        
        .. attribute:: cvcallvolconnentry
        
        	An entry in the cvCallVolConnTable indicates number of active calls for a call connection type in the voice gateway
        	**type**\: list of    :py:class:`Cvcallvolconnentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallvolconntable, self).__init__()

            self.yang_name = "cvCallVolConnTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallvolconnentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallvolconntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallvolconntable, self).__setattr__(name, value)


        class Cvcallvolconnentry(Entity):
            """
            An entry in the cvCallVolConnTable indicates
            number of active calls for a call connection type
            in the voice gateway.
            
            .. attribute:: cvcallvolconnindex  <key>
            
            	This object represents index to the cvCallVolConnTable
            	**type**\:   :py:class:`Cvcallconnectiontype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallconnectiontype>`
            
            .. attribute:: cvcallvolconnactiveconnection
            
            	This object represents the total number of active calls for a connection type  in the voice gateway
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry, self).__init__()

                self.yang_name = "cvCallVolConnEntry"
                self.yang_parent_name = "cvCallVolConnTable"

                self.cvcallvolconnindex = YLeaf(YType.enumeration, "cvCallVolConnIndex")

                self.cvcallvolconnactiveconnection = YLeaf(YType.uint32, "cvCallVolConnActiveConnection")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcallvolconnindex",
                                "cvcallvolconnactiveconnection") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcallvolconnindex.is_set or
                    self.cvcallvolconnactiveconnection.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcallvolconnindex.yfilter != YFilter.not_set or
                    self.cvcallvolconnactiveconnection.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallVolConnEntry" + "[cvCallVolConnIndex='" + self.cvcallvolconnindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallVolConnTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcallvolconnindex.is_set or self.cvcallvolconnindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolconnindex.get_name_leafdata())
                if (self.cvcallvolconnactiveconnection.is_set or self.cvcallvolconnactiveconnection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolconnactiveconnection.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallVolConnIndex" or name == "cvCallVolConnActiveConnection"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallVolConnIndex"):
                    self.cvcallvolconnindex = value
                    self.cvcallvolconnindex.value_namespace = name_space
                    self.cvcallvolconnindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallVolConnActiveConnection"):
                    self.cvcallvolconnactiveconnection = value
                    self.cvcallvolconnactiveconnection.value_namespace = name_space
                    self.cvcallvolconnactiveconnection.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallvolconnentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallvolconnentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallVolConnTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallVolConnEntry"):
                for c in self.cvcallvolconnentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallvolconnentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallVolConnEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallvoliftable(Entity):
        """
        This table represents the information about
        the usage of an IP interface in a voice
        gateway for voice media calls. This table
        has a sparse\-dependent relationship with  
        ifTable. There exists an entry in this table, 
        for each of the  entries in ifTable where ifType 
        is one of 'ethernetCsmacd' and 'softwareLoopback'.
        
        .. attribute:: cvcallvolifentry
        
        	Each entry represents a row in cvCallVolIfTable and corresponds to the information about an IP  interface in the voice gateway
        	**type**\: list of    :py:class:`Cvcallvolifentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallvoliftable, self).__init__()

            self.yang_name = "cvCallVolIfTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallvolifentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallvoliftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallvoliftable, self).__setattr__(name, value)


        class Cvcallvolifentry(Entity):
            """
            Each entry represents a row in cvCallVolIfTable
            and corresponds to the information about an IP 
            interface in the voice gateway.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cvcallvolmediaincomingcalls
            
            	This object represents the total number of inbound active media calls through this IP  interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolmediaoutgoingcalls
            
            	This object represents the total number of outbound active media calls through the IP  interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry, self).__init__()

                self.yang_name = "cvCallVolIfEntry"
                self.yang_parent_name = "cvCallVolIfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cvcallvolmediaincomingcalls = YLeaf(YType.uint32, "cvCallVolMediaIncomingCalls")

                self.cvcallvolmediaoutgoingcalls = YLeaf(YType.uint32, "cvCallVolMediaOutgoingCalls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cvcallvolmediaincomingcalls",
                                "cvcallvolmediaoutgoingcalls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cvcallvolmediaincomingcalls.is_set or
                    self.cvcallvolmediaoutgoingcalls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cvcallvolmediaincomingcalls.yfilter != YFilter.not_set or
                    self.cvcallvolmediaoutgoingcalls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallVolIfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallVolIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cvcallvolmediaincomingcalls.is_set or self.cvcallvolmediaincomingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolmediaincomingcalls.get_name_leafdata())
                if (self.cvcallvolmediaoutgoingcalls.is_set or self.cvcallvolmediaoutgoingcalls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallvolmediaoutgoingcalls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cvCallVolMediaIncomingCalls" or name == "cvCallVolMediaOutgoingCalls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallVolMediaIncomingCalls"):
                    self.cvcallvolmediaincomingcalls = value
                    self.cvcallvolmediaincomingcalls.value_namespace = name_space
                    self.cvcallvolmediaincomingcalls.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallVolMediaOutgoingCalls"):
                    self.cvcallvolmediaoutgoingcalls = value
                    self.cvcallvolmediaoutgoingcalls.value_namespace = name_space
                    self.cvcallvolmediaoutgoingcalls.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallvolifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallvolifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallVolIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallVolIfEntry"):
                for c in self.cvcallvolifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallvolifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallVolIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallhistorytable(Entity):
        """
        This table is the voice extension to the call history table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information such as voice packet statistics,
        coder usage and end to end bandwidth of the call leg.
        
        .. attribute:: cvcallhistoryentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains the call establishment to a voice encapsulation peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvcallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallhistorytable, self).__init__()

            self.yang_name = "cvCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallhistoryentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallhistorytable, self).__setattr__(name, value)


        class Cvcallhistoryentry(Entity):
            """
            The information regarding a single voice encapsulation
            call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            history entry in the IETF Dial Control MIB is created and
            the call history entry contains the call establishment to
            a voice encapsulation peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: ccallhistoryindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvcallhistoryaccountcode
            
            	The object indicates the account code input to the call. It could be used by down stream billing server. The value of empty string indicates no account code input
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: cvcallhistoryacomlevel
            
            	The object contains the average ACOM level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\:  int
            
            	**range:** \-1..127
            
            	**units**\: dB
            
            .. attribute:: cvcallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\:  bool
            
            .. attribute:: cvcallhistorycallid
            
            	This object represents the call identifier for the telephony leg, which was assigned to the call
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcallhistorycallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\:  str
            
            .. attribute:: cvcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            .. attribute:: cvcallhistoryconnectionid
            
            	The global connection identifier for the telephony leg, which was assigned to the call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcallhistoryfaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallhistoryimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: pages
            
            .. attribute:: cvcallhistorynoiselevel
            
            	The object contains the average noise level for the call leg
            	**type**\:  int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg via telephony interface
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cvcallhistorytxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallhistoryvoicetxduration
            
            	Duration for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry, self).__init__()

                self.yang_name = "cvCallHistoryEntry"
                self.yang_parent_name = "cvCallHistoryTable"

                self.ccallhistoryindex = YLeaf(YType.str, "cCallHistoryIndex")

                self.cvcallhistoryaccountcode = YLeaf(YType.str, "cvCallHistoryAccountCode")

                self.cvcallhistoryacomlevel = YLeaf(YType.int32, "cvCallHistoryACOMLevel")

                self.cvcallhistorycalleridblock = YLeaf(YType.boolean, "cvCallHistoryCallerIDBlock")

                self.cvcallhistorycallid = YLeaf(YType.uint32, "cvCallHistoryCallId")

                self.cvcallhistorycallingname = YLeaf(YType.str, "cvCallHistoryCallingName")

                self.cvcallhistorycodertyperate = YLeaf(YType.enumeration, "cvCallHistoryCoderTypeRate")

                self.cvcallhistoryconnectionid = YLeaf(YType.str, "cvCallHistoryConnectionId")

                self.cvcallhistoryfaxtxduration = YLeaf(YType.uint32, "cvCallHistoryFaxTxDuration")

                self.cvcallhistoryimgpagecount = YLeaf(YType.uint32, "cvCallHistoryImgPageCount")

                self.cvcallhistorynoiselevel = YLeaf(YType.int32, "cvCallHistoryNoiseLevel")

                self.cvcallhistorysessiontarget = YLeaf(YType.str, "cvCallHistorySessionTarget")

                self.cvcallhistorytxduration = YLeaf(YType.uint32, "cvCallHistoryTxDuration")

                self.cvcallhistoryvoicetxduration = YLeaf(YType.uint32, "cvCallHistoryVoiceTxDuration")

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
                                "cvcallhistoryaccountcode",
                                "cvcallhistoryacomlevel",
                                "cvcallhistorycalleridblock",
                                "cvcallhistorycallid",
                                "cvcallhistorycallingname",
                                "cvcallhistorycodertyperate",
                                "cvcallhistoryconnectionid",
                                "cvcallhistoryfaxtxduration",
                                "cvcallhistoryimgpagecount",
                                "cvcallhistorynoiselevel",
                                "cvcallhistorysessiontarget",
                                "cvcallhistorytxduration",
                                "cvcallhistoryvoicetxduration") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccallhistoryindex.is_set or
                    self.cvcallhistoryaccountcode.is_set or
                    self.cvcallhistoryacomlevel.is_set or
                    self.cvcallhistorycalleridblock.is_set or
                    self.cvcallhistorycallid.is_set or
                    self.cvcallhistorycallingname.is_set or
                    self.cvcallhistorycodertyperate.is_set or
                    self.cvcallhistoryconnectionid.is_set or
                    self.cvcallhistoryfaxtxduration.is_set or
                    self.cvcallhistoryimgpagecount.is_set or
                    self.cvcallhistorynoiselevel.is_set or
                    self.cvcallhistorysessiontarget.is_set or
                    self.cvcallhistorytxduration.is_set or
                    self.cvcallhistoryvoicetxduration.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccallhistoryindex.yfilter != YFilter.not_set or
                    self.cvcallhistoryaccountcode.yfilter != YFilter.not_set or
                    self.cvcallhistoryacomlevel.yfilter != YFilter.not_set or
                    self.cvcallhistorycalleridblock.yfilter != YFilter.not_set or
                    self.cvcallhistorycallid.yfilter != YFilter.not_set or
                    self.cvcallhistorycallingname.yfilter != YFilter.not_set or
                    self.cvcallhistorycodertyperate.yfilter != YFilter.not_set or
                    self.cvcallhistoryconnectionid.yfilter != YFilter.not_set or
                    self.cvcallhistoryfaxtxduration.yfilter != YFilter.not_set or
                    self.cvcallhistoryimgpagecount.yfilter != YFilter.not_set or
                    self.cvcallhistorynoiselevel.yfilter != YFilter.not_set or
                    self.cvcallhistorysessiontarget.yfilter != YFilter.not_set or
                    self.cvcallhistorytxduration.yfilter != YFilter.not_set or
                    self.cvcallhistoryvoicetxduration.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallHistoryEntry" + "[cCallHistoryIndex='" + self.ccallhistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccallhistoryindex.is_set or self.ccallhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryindex.get_name_leafdata())
                if (self.cvcallhistoryaccountcode.is_set or self.cvcallhistoryaccountcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryaccountcode.get_name_leafdata())
                if (self.cvcallhistoryacomlevel.is_set or self.cvcallhistoryacomlevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryacomlevel.get_name_leafdata())
                if (self.cvcallhistorycalleridblock.is_set or self.cvcallhistorycalleridblock.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorycalleridblock.get_name_leafdata())
                if (self.cvcallhistorycallid.is_set or self.cvcallhistorycallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorycallid.get_name_leafdata())
                if (self.cvcallhistorycallingname.is_set or self.cvcallhistorycallingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorycallingname.get_name_leafdata())
                if (self.cvcallhistorycodertyperate.is_set or self.cvcallhistorycodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorycodertyperate.get_name_leafdata())
                if (self.cvcallhistoryconnectionid.is_set or self.cvcallhistoryconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryconnectionid.get_name_leafdata())
                if (self.cvcallhistoryfaxtxduration.is_set or self.cvcallhistoryfaxtxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryfaxtxduration.get_name_leafdata())
                if (self.cvcallhistoryimgpagecount.is_set or self.cvcallhistoryimgpagecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryimgpagecount.get_name_leafdata())
                if (self.cvcallhistorynoiselevel.is_set or self.cvcallhistorynoiselevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorynoiselevel.get_name_leafdata())
                if (self.cvcallhistorysessiontarget.is_set or self.cvcallhistorysessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorysessiontarget.get_name_leafdata())
                if (self.cvcallhistorytxduration.is_set or self.cvcallhistorytxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistorytxduration.get_name_leafdata())
                if (self.cvcallhistoryvoicetxduration.is_set or self.cvcallhistoryvoicetxduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallhistoryvoicetxduration.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cCallHistoryIndex" or name == "cvCallHistoryAccountCode" or name == "cvCallHistoryACOMLevel" or name == "cvCallHistoryCallerIDBlock" or name == "cvCallHistoryCallId" or name == "cvCallHistoryCallingName" or name == "cvCallHistoryCoderTypeRate" or name == "cvCallHistoryConnectionId" or name == "cvCallHistoryFaxTxDuration" or name == "cvCallHistoryImgPageCount" or name == "cvCallHistoryNoiseLevel" or name == "cvCallHistorySessionTarget" or name == "cvCallHistoryTxDuration" or name == "cvCallHistoryVoiceTxDuration"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cCallHistoryIndex"):
                    self.ccallhistoryindex = value
                    self.ccallhistoryindex.value_namespace = name_space
                    self.ccallhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryAccountCode"):
                    self.cvcallhistoryaccountcode = value
                    self.cvcallhistoryaccountcode.value_namespace = name_space
                    self.cvcallhistoryaccountcode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryACOMLevel"):
                    self.cvcallhistoryacomlevel = value
                    self.cvcallhistoryacomlevel.value_namespace = name_space
                    self.cvcallhistoryacomlevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryCallerIDBlock"):
                    self.cvcallhistorycalleridblock = value
                    self.cvcallhistorycalleridblock.value_namespace = name_space
                    self.cvcallhistorycalleridblock.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryCallId"):
                    self.cvcallhistorycallid = value
                    self.cvcallhistorycallid.value_namespace = name_space
                    self.cvcallhistorycallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryCallingName"):
                    self.cvcallhistorycallingname = value
                    self.cvcallhistorycallingname.value_namespace = name_space
                    self.cvcallhistorycallingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryCoderTypeRate"):
                    self.cvcallhistorycodertyperate = value
                    self.cvcallhistorycodertyperate.value_namespace = name_space
                    self.cvcallhistorycodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryConnectionId"):
                    self.cvcallhistoryconnectionid = value
                    self.cvcallhistoryconnectionid.value_namespace = name_space
                    self.cvcallhistoryconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryFaxTxDuration"):
                    self.cvcallhistoryfaxtxduration = value
                    self.cvcallhistoryfaxtxduration.value_namespace = name_space
                    self.cvcallhistoryfaxtxduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryImgPageCount"):
                    self.cvcallhistoryimgpagecount = value
                    self.cvcallhistoryimgpagecount.value_namespace = name_space
                    self.cvcallhistoryimgpagecount.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryNoiseLevel"):
                    self.cvcallhistorynoiselevel = value
                    self.cvcallhistorynoiselevel.value_namespace = name_space
                    self.cvcallhistorynoiselevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistorySessionTarget"):
                    self.cvcallhistorysessiontarget = value
                    self.cvcallhistorysessiontarget.value_namespace = name_space
                    self.cvcallhistorysessiontarget.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryTxDuration"):
                    self.cvcallhistorytxduration = value
                    self.cvcallhistorytxduration.value_namespace = name_space
                    self.cvcallhistorytxduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallHistoryVoiceTxDuration"):
                    self.cvcallhistoryvoicetxduration = value
                    self.cvcallhistoryvoicetxduration.value_namespace = name_space
                    self.cvcallhistoryvoicetxduration.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallHistoryEntry"):
                for c in self.cvcallhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvvoipcallhistorytable(Entity):
        """
        This table is the VoIP extension to the call history table
        of IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallhistoryentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains information for the call establishment to the peer on the IP backbone via a voice over IP peer. The entry is deleted when its associated call history entry in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvvoipcallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable, self).__init__()

            self.yang_name = "cvVoIPCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvvoipcallhistoryentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable, self).__setattr__(name, value)


        class Cvvoipcallhistoryentry(Entity):
            """
            The information regarding a single VoIP call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            history entry in the IETF Dial Control MIB is created and
            the call history entry contains information for the call
            establishment to the peer on the IP backbone via a voice
            over IP peer.
            The entry is deleted when its associated call history
            entry in the IETF Dial Control MIB is deleted.
            
            .. attribute:: ccallhistoryindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvvoipcallhistorybitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:   :py:class:`Cvamrnbbitratemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvamrnbbitratemode>`
            
            .. attribute:: cvvoipcallhistorycallid
            
            	This object represents the call identifier for the VoIP leg, which was assigned to the call
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallhistorycallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.   For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorychannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..6
            
            	**units**\: channels
            
            .. attribute:: cvvoipcallhistorycodermode
            
            	The object indicates the iLBC mode. The value of this object is valid only if  cvVoIPCallHistoryCoderTypeRate is equal to  'iLBC'
            	**type**\:   :py:class:`Cvilbcframemode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvilbcframemode>`
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryconnectionid
            
            	The global connection identifier for the VoIP leg, which was assigned to the call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallhistorycrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallhistoryearlypackets
            
            	The number of received voice packets that are arrived too early to store in jitter buffer during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistoryencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:   :py:class:`Cvamrnbrtpencap <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvamrnbrtpencap>`
            
            .. attribute:: cvvoipcallhistoryfallbackdelay
            
            	The FallbackDelay is calculated as follows \- Take the sum of the round trips for all the probes,  divide by the number of probes,  and divide by two to get the one\-way delay.   Then add in jitter\_in or jiter\_out, which ever is higher
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryfallbackicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the fallback probe = Itotal (total impairment value)  \- configured fallback (Expectation Factor). A value of 0 implies that Icpif was not calculated and is meaningless for this attempt
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cvvoipcallhistoryfallbackloss
            
            	FallbackLoss is the percentage of loss packets based on the total packets sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorygapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or  frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryhiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the call = Itotal (total impairment value) of the call \- A (Expectation Factor) in the cvVoIPPeerCfgExpectFactor of the call leg associated peer. A value of \-1 implies that Icpif was not calculated and is meaningless for this call
            	**type**\:  int
            
            	**range:** \-1..55
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoipcallhistoryinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..50
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallhistorylatepackets
            
            	The number of received voice packets that are arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistorylostpackets
            
            	The number of lost voice packets during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistorylowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorymaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorymodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallHistoryBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallHistoryBitRates object. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallhistorymodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallhistoryoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallhistoryontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryreceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemMediaIPAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvvoipcallhistoryremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryremoteipaddress
            
            	Remote system IP address for the call
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets for the call
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemSigIPAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvvoipcallhistoryremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryrobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  bool
            
            .. attribute:: cvvoipcallhistoryroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryselectedqos
            
            	The selected RSVP QoS for the call
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INT_SERV_MIB.Qosservice>`
            
            .. attribute:: cvvoipcallhistorysessionid
            
            	This object indicates the session ID assigned by the call manager to identify call legs that belong to the same call session.  This session ID (history) represents a completed call session, whereas the active session ID (cvVoIPCallActiveSessionId) represents an ongoing session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorysessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:   :py:class:`Cvsessionprotocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvsessionprotocol>`
            
            .. attribute:: cvvoipcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the Voice over IP call
            	**type**\:  str
            
            .. attribute:: cvvoipcallhistorysrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\:  bool
            
            .. attribute:: cvvoipcallhistoryusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\:  bool
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry, self).__init__()

                self.yang_name = "cvVoIPCallHistoryEntry"
                self.yang_parent_name = "cvVoIPCallHistoryTable"

                self.ccallhistoryindex = YLeaf(YType.str, "cCallHistoryIndex")

                self.cvvoipcallhistorybitrates = YLeaf(YType.bits, "cvVoIPCallHistoryBitRates")

                self.cvvoipcallhistorycallid = YLeaf(YType.uint32, "cvVoIPCallHistoryCallId")

                self.cvvoipcallhistorycallreferenceid = YLeaf(YType.uint32, "cvVoIPCallHistoryCallReferenceId")

                self.cvvoipcallhistorychannels = YLeaf(YType.int32, "cvVoIPCallHistoryChannels")

                self.cvvoipcallhistorycodermode = YLeaf(YType.enumeration, "cvVoIPCallHistoryCoderMode")

                self.cvvoipcallhistorycodertyperate = YLeaf(YType.enumeration, "cvVoIPCallHistoryCoderTypeRate")

                self.cvvoipcallhistoryconnectionid = YLeaf(YType.str, "cvVoIPCallHistoryConnectionId")

                self.cvvoipcallhistorycrc = YLeaf(YType.boolean, "cvVoIPCallHistoryCRC")

                self.cvvoipcallhistoryearlypackets = YLeaf(YType.uint32, "cvVoIPCallHistoryEarlyPackets")

                self.cvvoipcallhistoryencap = YLeaf(YType.enumeration, "cvVoIPCallHistoryEncap")

                self.cvvoipcallhistoryfallbackdelay = YLeaf(YType.uint32, "cvVoIPCallHistoryFallbackDelay")

                self.cvvoipcallhistoryfallbackicpif = YLeaf(YType.int32, "cvVoIPCallHistoryFallbackIcpif")

                self.cvvoipcallhistoryfallbackloss = YLeaf(YType.uint32, "cvVoIPCallHistoryFallbackLoss")

                self.cvvoipcallhistorygapfillwithinterpolation = YLeaf(YType.uint32, "cvVoIPCallHistoryGapFillWithInterpolation")

                self.cvvoipcallhistorygapfillwithprediction = YLeaf(YType.uint32, "cvVoIPCallHistoryGapFillWithPrediction")

                self.cvvoipcallhistorygapfillwithredundancy = YLeaf(YType.uint32, "cvVoIPCallHistoryGapFillWithRedundancy")

                self.cvvoipcallhistorygapfillwithsilence = YLeaf(YType.uint32, "cvVoIPCallHistoryGapFillWithSilence")

                self.cvvoipcallhistoryhiwaterplayoutdelay = YLeaf(YType.uint32, "cvVoIPCallHistoryHiWaterPlayoutDelay")

                self.cvvoipcallhistoryicpif = YLeaf(YType.int32, "cvVoIPCallHistoryIcpif")

                self.cvvoipcallhistoryinterleaving = YLeaf(YType.int32, "cvVoIPCallHistoryInterleaving")

                self.cvvoipcallhistorylatepackets = YLeaf(YType.uint32, "cvVoIPCallHistoryLatePackets")

                self.cvvoipcallhistorylostpackets = YLeaf(YType.uint32, "cvVoIPCallHistoryLostPackets")

                self.cvvoipcallhistorylowaterplayoutdelay = YLeaf(YType.uint32, "cvVoIPCallHistoryLoWaterPlayoutDelay")

                self.cvvoipcallhistorymaxptime = YLeaf(YType.int32, "cvVoIPCallHistoryMaxPtime")

                self.cvvoipcallhistorymodechgneighbor = YLeaf(YType.boolean, "cvVoIPCallHistoryModeChgNeighbor")

                self.cvvoipcallhistorymodechgperiod = YLeaf(YType.int32, "cvVoIPCallHistoryModeChgPeriod")

                self.cvvoipcallhistoryoctetaligned = YLeaf(YType.boolean, "cvVoIPCallHistoryOctetAligned")

                self.cvvoipcallhistoryontimervplayout = YLeaf(YType.uint32, "cvVoIPCallHistoryOnTimeRvPlayout")

                self.cvvoipcallhistoryprotocolcallid = YLeaf(YType.str, "cvVoIPCallHistoryProtocolCallId")

                self.cvvoipcallhistoryptime = YLeaf(YType.int32, "cvVoIPCallHistoryPtime")

                self.cvvoipcallhistoryreceivedelay = YLeaf(YType.uint32, "cvVoIPCallHistoryReceiveDelay")

                self.cvvoipcallhistoryremmediaipaddr = YLeaf(YType.str, "cvVoIPCallHistoryRemMediaIPAddr")

                self.cvvoipcallhistoryremmediaipaddrt = YLeaf(YType.enumeration, "cvVoIPCallHistoryRemMediaIPAddrT")

                self.cvvoipcallhistoryremmediaport = YLeaf(YType.int32, "cvVoIPCallHistoryRemMediaPort")

                self.cvvoipcallhistoryremoteipaddress = YLeaf(YType.str, "cvVoIPCallHistoryRemoteIPAddress")

                self.cvvoipcallhistoryremoteudpport = YLeaf(YType.int32, "cvVoIPCallHistoryRemoteUDPPort")

                self.cvvoipcallhistoryremsigipaddr = YLeaf(YType.str, "cvVoIPCallHistoryRemSigIPAddr")

                self.cvvoipcallhistoryremsigipaddrt = YLeaf(YType.enumeration, "cvVoIPCallHistoryRemSigIPAddrT")

                self.cvvoipcallhistoryremsigport = YLeaf(YType.int32, "cvVoIPCallHistoryRemSigPort")

                self.cvvoipcallhistoryrobustsorting = YLeaf(YType.boolean, "cvVoIPCallHistoryRobustSorting")

                self.cvvoipcallhistoryroundtripdelay = YLeaf(YType.uint32, "cvVoIPCallHistoryRoundTripDelay")

                self.cvvoipcallhistoryselectedqos = YLeaf(YType.enumeration, "cvVoIPCallHistorySelectedQoS")

                self.cvvoipcallhistorysessionid = YLeaf(YType.uint32, "cvVoIPCallHistorySessionId")

                self.cvvoipcallhistorysessionprotocol = YLeaf(YType.enumeration, "cvVoIPCallHistorySessionProtocol")

                self.cvvoipcallhistorysessiontarget = YLeaf(YType.str, "cvVoIPCallHistorySessionTarget")

                self.cvvoipcallhistorysrtpenable = YLeaf(YType.boolean, "cvVoIPCallHistorySRTPEnable")

                self.cvvoipcallhistoryusername = YLeaf(YType.str, "cvVoIPCallHistoryUsername")

                self.cvvoipcallhistoryvadenable = YLeaf(YType.boolean, "cvVoIPCallHistoryVADEnable")

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
                                "cvvoipcallhistorybitrates",
                                "cvvoipcallhistorycallid",
                                "cvvoipcallhistorycallreferenceid",
                                "cvvoipcallhistorychannels",
                                "cvvoipcallhistorycodermode",
                                "cvvoipcallhistorycodertyperate",
                                "cvvoipcallhistoryconnectionid",
                                "cvvoipcallhistorycrc",
                                "cvvoipcallhistoryearlypackets",
                                "cvvoipcallhistoryencap",
                                "cvvoipcallhistoryfallbackdelay",
                                "cvvoipcallhistoryfallbackicpif",
                                "cvvoipcallhistoryfallbackloss",
                                "cvvoipcallhistorygapfillwithinterpolation",
                                "cvvoipcallhistorygapfillwithprediction",
                                "cvvoipcallhistorygapfillwithredundancy",
                                "cvvoipcallhistorygapfillwithsilence",
                                "cvvoipcallhistoryhiwaterplayoutdelay",
                                "cvvoipcallhistoryicpif",
                                "cvvoipcallhistoryinterleaving",
                                "cvvoipcallhistorylatepackets",
                                "cvvoipcallhistorylostpackets",
                                "cvvoipcallhistorylowaterplayoutdelay",
                                "cvvoipcallhistorymaxptime",
                                "cvvoipcallhistorymodechgneighbor",
                                "cvvoipcallhistorymodechgperiod",
                                "cvvoipcallhistoryoctetaligned",
                                "cvvoipcallhistoryontimervplayout",
                                "cvvoipcallhistoryprotocolcallid",
                                "cvvoipcallhistoryptime",
                                "cvvoipcallhistoryreceivedelay",
                                "cvvoipcallhistoryremmediaipaddr",
                                "cvvoipcallhistoryremmediaipaddrt",
                                "cvvoipcallhistoryremmediaport",
                                "cvvoipcallhistoryremoteipaddress",
                                "cvvoipcallhistoryremoteudpport",
                                "cvvoipcallhistoryremsigipaddr",
                                "cvvoipcallhistoryremsigipaddrt",
                                "cvvoipcallhistoryremsigport",
                                "cvvoipcallhistoryrobustsorting",
                                "cvvoipcallhistoryroundtripdelay",
                                "cvvoipcallhistoryselectedqos",
                                "cvvoipcallhistorysessionid",
                                "cvvoipcallhistorysessionprotocol",
                                "cvvoipcallhistorysessiontarget",
                                "cvvoipcallhistorysrtpenable",
                                "cvvoipcallhistoryusername",
                                "cvvoipcallhistoryvadenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccallhistoryindex.is_set or
                    self.cvvoipcallhistorybitrates.is_set or
                    self.cvvoipcallhistorycallid.is_set or
                    self.cvvoipcallhistorycallreferenceid.is_set or
                    self.cvvoipcallhistorychannels.is_set or
                    self.cvvoipcallhistorycodermode.is_set or
                    self.cvvoipcallhistorycodertyperate.is_set or
                    self.cvvoipcallhistoryconnectionid.is_set or
                    self.cvvoipcallhistorycrc.is_set or
                    self.cvvoipcallhistoryearlypackets.is_set or
                    self.cvvoipcallhistoryencap.is_set or
                    self.cvvoipcallhistoryfallbackdelay.is_set or
                    self.cvvoipcallhistoryfallbackicpif.is_set or
                    self.cvvoipcallhistoryfallbackloss.is_set or
                    self.cvvoipcallhistorygapfillwithinterpolation.is_set or
                    self.cvvoipcallhistorygapfillwithprediction.is_set or
                    self.cvvoipcallhistorygapfillwithredundancy.is_set or
                    self.cvvoipcallhistorygapfillwithsilence.is_set or
                    self.cvvoipcallhistoryhiwaterplayoutdelay.is_set or
                    self.cvvoipcallhistoryicpif.is_set or
                    self.cvvoipcallhistoryinterleaving.is_set or
                    self.cvvoipcallhistorylatepackets.is_set or
                    self.cvvoipcallhistorylostpackets.is_set or
                    self.cvvoipcallhistorylowaterplayoutdelay.is_set or
                    self.cvvoipcallhistorymaxptime.is_set or
                    self.cvvoipcallhistorymodechgneighbor.is_set or
                    self.cvvoipcallhistorymodechgperiod.is_set or
                    self.cvvoipcallhistoryoctetaligned.is_set or
                    self.cvvoipcallhistoryontimervplayout.is_set or
                    self.cvvoipcallhistoryprotocolcallid.is_set or
                    self.cvvoipcallhistoryptime.is_set or
                    self.cvvoipcallhistoryreceivedelay.is_set or
                    self.cvvoipcallhistoryremmediaipaddr.is_set or
                    self.cvvoipcallhistoryremmediaipaddrt.is_set or
                    self.cvvoipcallhistoryremmediaport.is_set or
                    self.cvvoipcallhistoryremoteipaddress.is_set or
                    self.cvvoipcallhistoryremoteudpport.is_set or
                    self.cvvoipcallhistoryremsigipaddr.is_set or
                    self.cvvoipcallhistoryremsigipaddrt.is_set or
                    self.cvvoipcallhistoryremsigport.is_set or
                    self.cvvoipcallhistoryrobustsorting.is_set or
                    self.cvvoipcallhistoryroundtripdelay.is_set or
                    self.cvvoipcallhistoryselectedqos.is_set or
                    self.cvvoipcallhistorysessionid.is_set or
                    self.cvvoipcallhistorysessionprotocol.is_set or
                    self.cvvoipcallhistorysessiontarget.is_set or
                    self.cvvoipcallhistorysrtpenable.is_set or
                    self.cvvoipcallhistoryusername.is_set or
                    self.cvvoipcallhistoryvadenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccallhistoryindex.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorybitrates.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorycallid.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorycallreferenceid.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorychannels.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorycodermode.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorycodertyperate.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryconnectionid.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorycrc.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryearlypackets.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryencap.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryfallbackdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryfallbackicpif.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryfallbackloss.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorygapfillwithinterpolation.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorygapfillwithprediction.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorygapfillwithredundancy.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorygapfillwithsilence.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryhiwaterplayoutdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryicpif.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryinterleaving.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorylatepackets.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorylostpackets.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorylowaterplayoutdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorymaxptime.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorymodechgneighbor.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorymodechgperiod.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryoctetaligned.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryontimervplayout.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryprotocolcallid.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryptime.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryreceivedelay.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremmediaipaddr.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremmediaipaddrt.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremmediaport.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremoteipaddress.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremoteudpport.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremsigipaddr.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremsigipaddrt.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryremsigport.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryrobustsorting.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryroundtripdelay.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryselectedqos.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorysessionid.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorysessionprotocol.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorysessiontarget.yfilter != YFilter.not_set or
                    self.cvvoipcallhistorysrtpenable.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryusername.yfilter != YFilter.not_set or
                    self.cvvoipcallhistoryvadenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvVoIPCallHistoryEntry" + "[cCallHistoryIndex='" + self.ccallhistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPCallHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccallhistoryindex.is_set or self.ccallhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryindex.get_name_leafdata())
                if (self.cvvoipcallhistorybitrates.is_set or self.cvvoipcallhistorybitrates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorybitrates.get_name_leafdata())
                if (self.cvvoipcallhistorycallid.is_set or self.cvvoipcallhistorycallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorycallid.get_name_leafdata())
                if (self.cvvoipcallhistorycallreferenceid.is_set or self.cvvoipcallhistorycallreferenceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorycallreferenceid.get_name_leafdata())
                if (self.cvvoipcallhistorychannels.is_set or self.cvvoipcallhistorychannels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorychannels.get_name_leafdata())
                if (self.cvvoipcallhistorycodermode.is_set or self.cvvoipcallhistorycodermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorycodermode.get_name_leafdata())
                if (self.cvvoipcallhistorycodertyperate.is_set or self.cvvoipcallhistorycodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorycodertyperate.get_name_leafdata())
                if (self.cvvoipcallhistoryconnectionid.is_set or self.cvvoipcallhistoryconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryconnectionid.get_name_leafdata())
                if (self.cvvoipcallhistorycrc.is_set or self.cvvoipcallhistorycrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorycrc.get_name_leafdata())
                if (self.cvvoipcallhistoryearlypackets.is_set or self.cvvoipcallhistoryearlypackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryearlypackets.get_name_leafdata())
                if (self.cvvoipcallhistoryencap.is_set or self.cvvoipcallhistoryencap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryencap.get_name_leafdata())
                if (self.cvvoipcallhistoryfallbackdelay.is_set or self.cvvoipcallhistoryfallbackdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryfallbackdelay.get_name_leafdata())
                if (self.cvvoipcallhistoryfallbackicpif.is_set or self.cvvoipcallhistoryfallbackicpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryfallbackicpif.get_name_leafdata())
                if (self.cvvoipcallhistoryfallbackloss.is_set or self.cvvoipcallhistoryfallbackloss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryfallbackloss.get_name_leafdata())
                if (self.cvvoipcallhistorygapfillwithinterpolation.is_set or self.cvvoipcallhistorygapfillwithinterpolation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorygapfillwithinterpolation.get_name_leafdata())
                if (self.cvvoipcallhistorygapfillwithprediction.is_set or self.cvvoipcallhistorygapfillwithprediction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorygapfillwithprediction.get_name_leafdata())
                if (self.cvvoipcallhistorygapfillwithredundancy.is_set or self.cvvoipcallhistorygapfillwithredundancy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorygapfillwithredundancy.get_name_leafdata())
                if (self.cvvoipcallhistorygapfillwithsilence.is_set or self.cvvoipcallhistorygapfillwithsilence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorygapfillwithsilence.get_name_leafdata())
                if (self.cvvoipcallhistoryhiwaterplayoutdelay.is_set or self.cvvoipcallhistoryhiwaterplayoutdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryhiwaterplayoutdelay.get_name_leafdata())
                if (self.cvvoipcallhistoryicpif.is_set or self.cvvoipcallhistoryicpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryicpif.get_name_leafdata())
                if (self.cvvoipcallhistoryinterleaving.is_set or self.cvvoipcallhistoryinterleaving.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryinterleaving.get_name_leafdata())
                if (self.cvvoipcallhistorylatepackets.is_set or self.cvvoipcallhistorylatepackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorylatepackets.get_name_leafdata())
                if (self.cvvoipcallhistorylostpackets.is_set or self.cvvoipcallhistorylostpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorylostpackets.get_name_leafdata())
                if (self.cvvoipcallhistorylowaterplayoutdelay.is_set or self.cvvoipcallhistorylowaterplayoutdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorylowaterplayoutdelay.get_name_leafdata())
                if (self.cvvoipcallhistorymaxptime.is_set or self.cvvoipcallhistorymaxptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorymaxptime.get_name_leafdata())
                if (self.cvvoipcallhistorymodechgneighbor.is_set or self.cvvoipcallhistorymodechgneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorymodechgneighbor.get_name_leafdata())
                if (self.cvvoipcallhistorymodechgperiod.is_set or self.cvvoipcallhistorymodechgperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorymodechgperiod.get_name_leafdata())
                if (self.cvvoipcallhistoryoctetaligned.is_set or self.cvvoipcallhistoryoctetaligned.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryoctetaligned.get_name_leafdata())
                if (self.cvvoipcallhistoryontimervplayout.is_set or self.cvvoipcallhistoryontimervplayout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryontimervplayout.get_name_leafdata())
                if (self.cvvoipcallhistoryprotocolcallid.is_set or self.cvvoipcallhistoryprotocolcallid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryprotocolcallid.get_name_leafdata())
                if (self.cvvoipcallhistoryptime.is_set or self.cvvoipcallhistoryptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryptime.get_name_leafdata())
                if (self.cvvoipcallhistoryreceivedelay.is_set or self.cvvoipcallhistoryreceivedelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryreceivedelay.get_name_leafdata())
                if (self.cvvoipcallhistoryremmediaipaddr.is_set or self.cvvoipcallhistoryremmediaipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremmediaipaddr.get_name_leafdata())
                if (self.cvvoipcallhistoryremmediaipaddrt.is_set or self.cvvoipcallhistoryremmediaipaddrt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremmediaipaddrt.get_name_leafdata())
                if (self.cvvoipcallhistoryremmediaport.is_set or self.cvvoipcallhistoryremmediaport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremmediaport.get_name_leafdata())
                if (self.cvvoipcallhistoryremoteipaddress.is_set or self.cvvoipcallhistoryremoteipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremoteipaddress.get_name_leafdata())
                if (self.cvvoipcallhistoryremoteudpport.is_set or self.cvvoipcallhistoryremoteudpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremoteudpport.get_name_leafdata())
                if (self.cvvoipcallhistoryremsigipaddr.is_set or self.cvvoipcallhistoryremsigipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremsigipaddr.get_name_leafdata())
                if (self.cvvoipcallhistoryremsigipaddrt.is_set or self.cvvoipcallhistoryremsigipaddrt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremsigipaddrt.get_name_leafdata())
                if (self.cvvoipcallhistoryremsigport.is_set or self.cvvoipcallhistoryremsigport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryremsigport.get_name_leafdata())
                if (self.cvvoipcallhistoryrobustsorting.is_set or self.cvvoipcallhistoryrobustsorting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryrobustsorting.get_name_leafdata())
                if (self.cvvoipcallhistoryroundtripdelay.is_set or self.cvvoipcallhistoryroundtripdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryroundtripdelay.get_name_leafdata())
                if (self.cvvoipcallhistoryselectedqos.is_set or self.cvvoipcallhistoryselectedqos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryselectedqos.get_name_leafdata())
                if (self.cvvoipcallhistorysessionid.is_set or self.cvvoipcallhistorysessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorysessionid.get_name_leafdata())
                if (self.cvvoipcallhistorysessionprotocol.is_set or self.cvvoipcallhistorysessionprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorysessionprotocol.get_name_leafdata())
                if (self.cvvoipcallhistorysessiontarget.is_set or self.cvvoipcallhistorysessiontarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorysessiontarget.get_name_leafdata())
                if (self.cvvoipcallhistorysrtpenable.is_set or self.cvvoipcallhistorysrtpenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistorysrtpenable.get_name_leafdata())
                if (self.cvvoipcallhistoryusername.is_set or self.cvvoipcallhistoryusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryusername.get_name_leafdata())
                if (self.cvvoipcallhistoryvadenable.is_set or self.cvvoipcallhistoryvadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvvoipcallhistoryvadenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cCallHistoryIndex" or name == "cvVoIPCallHistoryBitRates" or name == "cvVoIPCallHistoryCallId" or name == "cvVoIPCallHistoryCallReferenceId" or name == "cvVoIPCallHistoryChannels" or name == "cvVoIPCallHistoryCoderMode" or name == "cvVoIPCallHistoryCoderTypeRate" or name == "cvVoIPCallHistoryConnectionId" or name == "cvVoIPCallHistoryCRC" or name == "cvVoIPCallHistoryEarlyPackets" or name == "cvVoIPCallHistoryEncap" or name == "cvVoIPCallHistoryFallbackDelay" or name == "cvVoIPCallHistoryFallbackIcpif" or name == "cvVoIPCallHistoryFallbackLoss" or name == "cvVoIPCallHistoryGapFillWithInterpolation" or name == "cvVoIPCallHistoryGapFillWithPrediction" or name == "cvVoIPCallHistoryGapFillWithRedundancy" or name == "cvVoIPCallHistoryGapFillWithSilence" or name == "cvVoIPCallHistoryHiWaterPlayoutDelay" or name == "cvVoIPCallHistoryIcpif" or name == "cvVoIPCallHistoryInterleaving" or name == "cvVoIPCallHistoryLatePackets" or name == "cvVoIPCallHistoryLostPackets" or name == "cvVoIPCallHistoryLoWaterPlayoutDelay" or name == "cvVoIPCallHistoryMaxPtime" or name == "cvVoIPCallHistoryModeChgNeighbor" or name == "cvVoIPCallHistoryModeChgPeriod" or name == "cvVoIPCallHistoryOctetAligned" or name == "cvVoIPCallHistoryOnTimeRvPlayout" or name == "cvVoIPCallHistoryProtocolCallId" or name == "cvVoIPCallHistoryPtime" or name == "cvVoIPCallHistoryReceiveDelay" or name == "cvVoIPCallHistoryRemMediaIPAddr" or name == "cvVoIPCallHistoryRemMediaIPAddrT" or name == "cvVoIPCallHistoryRemMediaPort" or name == "cvVoIPCallHistoryRemoteIPAddress" or name == "cvVoIPCallHistoryRemoteUDPPort" or name == "cvVoIPCallHistoryRemSigIPAddr" or name == "cvVoIPCallHistoryRemSigIPAddrT" or name == "cvVoIPCallHistoryRemSigPort" or name == "cvVoIPCallHistoryRobustSorting" or name == "cvVoIPCallHistoryRoundTripDelay" or name == "cvVoIPCallHistorySelectedQoS" or name == "cvVoIPCallHistorySessionId" or name == "cvVoIPCallHistorySessionProtocol" or name == "cvVoIPCallHistorySessionTarget" or name == "cvVoIPCallHistorySRTPEnable" or name == "cvVoIPCallHistoryUsername" or name == "cvVoIPCallHistoryVADEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cCallHistoryIndex"):
                    self.ccallhistoryindex = value
                    self.ccallhistoryindex.value_namespace = name_space
                    self.ccallhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryBitRates"):
                    self.cvvoipcallhistorybitrates[value] = True
                if(value_path == "cvVoIPCallHistoryCallId"):
                    self.cvvoipcallhistorycallid = value
                    self.cvvoipcallhistorycallid.value_namespace = name_space
                    self.cvvoipcallhistorycallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryCallReferenceId"):
                    self.cvvoipcallhistorycallreferenceid = value
                    self.cvvoipcallhistorycallreferenceid.value_namespace = name_space
                    self.cvvoipcallhistorycallreferenceid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryChannels"):
                    self.cvvoipcallhistorychannels = value
                    self.cvvoipcallhistorychannels.value_namespace = name_space
                    self.cvvoipcallhistorychannels.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryCoderMode"):
                    self.cvvoipcallhistorycodermode = value
                    self.cvvoipcallhistorycodermode.value_namespace = name_space
                    self.cvvoipcallhistorycodermode.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryCoderTypeRate"):
                    self.cvvoipcallhistorycodertyperate = value
                    self.cvvoipcallhistorycodertyperate.value_namespace = name_space
                    self.cvvoipcallhistorycodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryConnectionId"):
                    self.cvvoipcallhistoryconnectionid = value
                    self.cvvoipcallhistoryconnectionid.value_namespace = name_space
                    self.cvvoipcallhistoryconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryCRC"):
                    self.cvvoipcallhistorycrc = value
                    self.cvvoipcallhistorycrc.value_namespace = name_space
                    self.cvvoipcallhistorycrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryEarlyPackets"):
                    self.cvvoipcallhistoryearlypackets = value
                    self.cvvoipcallhistoryearlypackets.value_namespace = name_space
                    self.cvvoipcallhistoryearlypackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryEncap"):
                    self.cvvoipcallhistoryencap = value
                    self.cvvoipcallhistoryencap.value_namespace = name_space
                    self.cvvoipcallhistoryencap.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryFallbackDelay"):
                    self.cvvoipcallhistoryfallbackdelay = value
                    self.cvvoipcallhistoryfallbackdelay.value_namespace = name_space
                    self.cvvoipcallhistoryfallbackdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryFallbackIcpif"):
                    self.cvvoipcallhistoryfallbackicpif = value
                    self.cvvoipcallhistoryfallbackicpif.value_namespace = name_space
                    self.cvvoipcallhistoryfallbackicpif.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryFallbackLoss"):
                    self.cvvoipcallhistoryfallbackloss = value
                    self.cvvoipcallhistoryfallbackloss.value_namespace = name_space
                    self.cvvoipcallhistoryfallbackloss.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryGapFillWithInterpolation"):
                    self.cvvoipcallhistorygapfillwithinterpolation = value
                    self.cvvoipcallhistorygapfillwithinterpolation.value_namespace = name_space
                    self.cvvoipcallhistorygapfillwithinterpolation.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryGapFillWithPrediction"):
                    self.cvvoipcallhistorygapfillwithprediction = value
                    self.cvvoipcallhistorygapfillwithprediction.value_namespace = name_space
                    self.cvvoipcallhistorygapfillwithprediction.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryGapFillWithRedundancy"):
                    self.cvvoipcallhistorygapfillwithredundancy = value
                    self.cvvoipcallhistorygapfillwithredundancy.value_namespace = name_space
                    self.cvvoipcallhistorygapfillwithredundancy.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryGapFillWithSilence"):
                    self.cvvoipcallhistorygapfillwithsilence = value
                    self.cvvoipcallhistorygapfillwithsilence.value_namespace = name_space
                    self.cvvoipcallhistorygapfillwithsilence.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryHiWaterPlayoutDelay"):
                    self.cvvoipcallhistoryhiwaterplayoutdelay = value
                    self.cvvoipcallhistoryhiwaterplayoutdelay.value_namespace = name_space
                    self.cvvoipcallhistoryhiwaterplayoutdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryIcpif"):
                    self.cvvoipcallhistoryicpif = value
                    self.cvvoipcallhistoryicpif.value_namespace = name_space
                    self.cvvoipcallhistoryicpif.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryInterleaving"):
                    self.cvvoipcallhistoryinterleaving = value
                    self.cvvoipcallhistoryinterleaving.value_namespace = name_space
                    self.cvvoipcallhistoryinterleaving.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryLatePackets"):
                    self.cvvoipcallhistorylatepackets = value
                    self.cvvoipcallhistorylatepackets.value_namespace = name_space
                    self.cvvoipcallhistorylatepackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryLostPackets"):
                    self.cvvoipcallhistorylostpackets = value
                    self.cvvoipcallhistorylostpackets.value_namespace = name_space
                    self.cvvoipcallhistorylostpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryLoWaterPlayoutDelay"):
                    self.cvvoipcallhistorylowaterplayoutdelay = value
                    self.cvvoipcallhistorylowaterplayoutdelay.value_namespace = name_space
                    self.cvvoipcallhistorylowaterplayoutdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryMaxPtime"):
                    self.cvvoipcallhistorymaxptime = value
                    self.cvvoipcallhistorymaxptime.value_namespace = name_space
                    self.cvvoipcallhistorymaxptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryModeChgNeighbor"):
                    self.cvvoipcallhistorymodechgneighbor = value
                    self.cvvoipcallhistorymodechgneighbor.value_namespace = name_space
                    self.cvvoipcallhistorymodechgneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryModeChgPeriod"):
                    self.cvvoipcallhistorymodechgperiod = value
                    self.cvvoipcallhistorymodechgperiod.value_namespace = name_space
                    self.cvvoipcallhistorymodechgperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryOctetAligned"):
                    self.cvvoipcallhistoryoctetaligned = value
                    self.cvvoipcallhistoryoctetaligned.value_namespace = name_space
                    self.cvvoipcallhistoryoctetaligned.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryOnTimeRvPlayout"):
                    self.cvvoipcallhistoryontimervplayout = value
                    self.cvvoipcallhistoryontimervplayout.value_namespace = name_space
                    self.cvvoipcallhistoryontimervplayout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryProtocolCallId"):
                    self.cvvoipcallhistoryprotocolcallid = value
                    self.cvvoipcallhistoryprotocolcallid.value_namespace = name_space
                    self.cvvoipcallhistoryprotocolcallid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryPtime"):
                    self.cvvoipcallhistoryptime = value
                    self.cvvoipcallhistoryptime.value_namespace = name_space
                    self.cvvoipcallhistoryptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryReceiveDelay"):
                    self.cvvoipcallhistoryreceivedelay = value
                    self.cvvoipcallhistoryreceivedelay.value_namespace = name_space
                    self.cvvoipcallhistoryreceivedelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemMediaIPAddr"):
                    self.cvvoipcallhistoryremmediaipaddr = value
                    self.cvvoipcallhistoryremmediaipaddr.value_namespace = name_space
                    self.cvvoipcallhistoryremmediaipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemMediaIPAddrT"):
                    self.cvvoipcallhistoryremmediaipaddrt = value
                    self.cvvoipcallhistoryremmediaipaddrt.value_namespace = name_space
                    self.cvvoipcallhistoryremmediaipaddrt.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemMediaPort"):
                    self.cvvoipcallhistoryremmediaport = value
                    self.cvvoipcallhistoryremmediaport.value_namespace = name_space
                    self.cvvoipcallhistoryremmediaport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemoteIPAddress"):
                    self.cvvoipcallhistoryremoteipaddress = value
                    self.cvvoipcallhistoryremoteipaddress.value_namespace = name_space
                    self.cvvoipcallhistoryremoteipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemoteUDPPort"):
                    self.cvvoipcallhistoryremoteudpport = value
                    self.cvvoipcallhistoryremoteudpport.value_namespace = name_space
                    self.cvvoipcallhistoryremoteudpport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemSigIPAddr"):
                    self.cvvoipcallhistoryremsigipaddr = value
                    self.cvvoipcallhistoryremsigipaddr.value_namespace = name_space
                    self.cvvoipcallhistoryremsigipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemSigIPAddrT"):
                    self.cvvoipcallhistoryremsigipaddrt = value
                    self.cvvoipcallhistoryremsigipaddrt.value_namespace = name_space
                    self.cvvoipcallhistoryremsigipaddrt.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRemSigPort"):
                    self.cvvoipcallhistoryremsigport = value
                    self.cvvoipcallhistoryremsigport.value_namespace = name_space
                    self.cvvoipcallhistoryremsigport.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRobustSorting"):
                    self.cvvoipcallhistoryrobustsorting = value
                    self.cvvoipcallhistoryrobustsorting.value_namespace = name_space
                    self.cvvoipcallhistoryrobustsorting.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryRoundTripDelay"):
                    self.cvvoipcallhistoryroundtripdelay = value
                    self.cvvoipcallhistoryroundtripdelay.value_namespace = name_space
                    self.cvvoipcallhistoryroundtripdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistorySelectedQoS"):
                    self.cvvoipcallhistoryselectedqos = value
                    self.cvvoipcallhistoryselectedqos.value_namespace = name_space
                    self.cvvoipcallhistoryselectedqos.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistorySessionId"):
                    self.cvvoipcallhistorysessionid = value
                    self.cvvoipcallhistorysessionid.value_namespace = name_space
                    self.cvvoipcallhistorysessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistorySessionProtocol"):
                    self.cvvoipcallhistorysessionprotocol = value
                    self.cvvoipcallhistorysessionprotocol.value_namespace = name_space
                    self.cvvoipcallhistorysessionprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistorySessionTarget"):
                    self.cvvoipcallhistorysessiontarget = value
                    self.cvvoipcallhistorysessiontarget.value_namespace = name_space
                    self.cvvoipcallhistorysessiontarget.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistorySRTPEnable"):
                    self.cvvoipcallhistorysrtpenable = value
                    self.cvvoipcallhistorysrtpenable.value_namespace = name_space
                    self.cvvoipcallhistorysrtpenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryUsername"):
                    self.cvvoipcallhistoryusername = value
                    self.cvvoipcallhistoryusername.value_namespace = name_space
                    self.cvvoipcallhistoryusername.value_namespace_prefix = name_space_prefix
                if(value_path == "cvVoIPCallHistoryVADEnable"):
                    self.cvvoipcallhistoryvadenable = value
                    self.cvvoipcallhistoryvadenable.value_namespace = name_space
                    self.cvvoipcallhistoryvadenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvvoipcallhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvvoipcallhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvVoIPCallHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvVoIPCallHistoryEntry"):
                for c in self.cvvoipcallhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvvoipcallhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvVoIPCallHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallratestatstable(Entity):
        """
        This table represents voice call rate measurement in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcallratestatsentry
        
        	This is a conceptual\-row in cvCallRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of    :py:class:`Cvcallratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallratestatstable, self).__init__()

            self.yang_name = "cvCallRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallratestatsentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallratestatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallratestatstable, self).__setattr__(name, value)


        class Cvcallratestatsentry(Entity):
            """
            This is a conceptual\-row in cvCallRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcallratestatsintvldurunits  <key>
            
            	The Object indexes in Call Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:   :py:class:`Cvcallvolumestatsintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumestatsintvltype>`
            
            .. attribute:: cvcallratestatsintvldur  <key>
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\:  int
            
            	**range:** 1..72
            
            .. attribute:: cvcallratestatsavgval
            
            	This object indicates the average calls per second that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls-per-second
            
            .. attribute:: cvcallratestatsmaxval
            
            	This object indicates the maximum calls per second that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls-per-second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry, self).__init__()

                self.yang_name = "cvCallRateStatsEntry"
                self.yang_parent_name = "cvCallRateStatsTable"

                self.cvcallratestatsintvldurunits = YLeaf(YType.enumeration, "cvCallRateStatsIntvlDurUnits")

                self.cvcallratestatsintvldur = YLeaf(YType.uint32, "cvCallRateStatsIntvlDur")

                self.cvcallratestatsavgval = YLeaf(YType.uint32, "cvCallRateStatsAvgVal")

                self.cvcallratestatsmaxval = YLeaf(YType.uint32, "cvCallRateStatsMaxVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcallratestatsintvldurunits",
                                "cvcallratestatsintvldur",
                                "cvcallratestatsavgval",
                                "cvcallratestatsmaxval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcallratestatsintvldurunits.is_set or
                    self.cvcallratestatsintvldur.is_set or
                    self.cvcallratestatsavgval.is_set or
                    self.cvcallratestatsmaxval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcallratestatsintvldurunits.yfilter != YFilter.not_set or
                    self.cvcallratestatsintvldur.yfilter != YFilter.not_set or
                    self.cvcallratestatsavgval.yfilter != YFilter.not_set or
                    self.cvcallratestatsmaxval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallRateStatsEntry" + "[cvCallRateStatsIntvlDurUnits='" + self.cvcallratestatsintvldurunits.get() + "']" + "[cvCallRateStatsIntvlDur='" + self.cvcallratestatsintvldur.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallRateStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcallratestatsintvldurunits.is_set or self.cvcallratestatsintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratestatsintvldurunits.get_name_leafdata())
                if (self.cvcallratestatsintvldur.is_set or self.cvcallratestatsintvldur.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratestatsintvldur.get_name_leafdata())
                if (self.cvcallratestatsavgval.is_set or self.cvcallratestatsavgval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratestatsavgval.get_name_leafdata())
                if (self.cvcallratestatsmaxval.is_set or self.cvcallratestatsmaxval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratestatsmaxval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallRateStatsIntvlDurUnits" or name == "cvCallRateStatsIntvlDur" or name == "cvCallRateStatsAvgVal" or name == "cvCallRateStatsMaxVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallRateStatsIntvlDurUnits"):
                    self.cvcallratestatsintvldurunits = value
                    self.cvcallratestatsintvldurunits.value_namespace = name_space
                    self.cvcallratestatsintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateStatsIntvlDur"):
                    self.cvcallratestatsintvldur = value
                    self.cvcallratestatsintvldur.value_namespace = name_space
                    self.cvcallratestatsintvldur.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateStatsAvgVal"):
                    self.cvcallratestatsavgval = value
                    self.cvcallratestatsavgval.value_namespace = name_space
                    self.cvcallratestatsavgval.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateStatsMaxVal"):
                    self.cvcallratestatsmaxval = value
                    self.cvcallratestatsmaxval.value_namespace = name_space
                    self.cvcallratestatsmaxval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallratestatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallratestatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallRateStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallRateStatsEntry"):
                for c in self.cvcallratestatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallratestatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallRateStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcalllegratestatstable(Entity):
        """
        cvCallLegRateStatsTable table represents voice call leg rate
        measurement in various interval lengths defined by 
        the CvCallVolumeStatsIntvlType object.
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcalllegratestatsentry
        
        	This is a conceptual\-row in cvCallLegRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of    :py:class:`Cvcalllegratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcalllegratestatstable, self).__init__()

            self.yang_name = "cvCallLegRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcalllegratestatsentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcalllegratestatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcalllegratestatstable, self).__setattr__(name, value)


        class Cvcalllegratestatsentry(Entity):
            """
            This is a conceptual\-row in cvCallLegRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalllegratestatsintvldurunits  <key>
            
            	The Object indexes in Call Leg Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:   :py:class:`Cvcallvolumestatsintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumestatsintvltype>`
            
            .. attribute:: cvcalllegratestatsintvldur  <key>
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\:  int
            
            	**range:** 1..72
            
            .. attribute:: cvcalllegratestatsavgval
            
            	This object indicates the average call\-legs per second that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: call-legs per second
            
            .. attribute:: cvcalllegratestatsmaxval
            
            	This object indicates the maximum call\-legs per second that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: call-legs per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry, self).__init__()

                self.yang_name = "cvCallLegRateStatsEntry"
                self.yang_parent_name = "cvCallLegRateStatsTable"

                self.cvcalllegratestatsintvldurunits = YLeaf(YType.enumeration, "cvCallLegRateStatsIntvlDurUnits")

                self.cvcalllegratestatsintvldur = YLeaf(YType.uint32, "cvCallLegRateStatsIntvlDur")

                self.cvcalllegratestatsavgval = YLeaf(YType.uint32, "cvCallLegRateStatsAvgVal")

                self.cvcalllegratestatsmaxval = YLeaf(YType.uint32, "cvCallLegRateStatsMaxVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcalllegratestatsintvldurunits",
                                "cvcalllegratestatsintvldur",
                                "cvcalllegratestatsavgval",
                                "cvcalllegratestatsmaxval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcalllegratestatsintvldurunits.is_set or
                    self.cvcalllegratestatsintvldur.is_set or
                    self.cvcalllegratestatsavgval.is_set or
                    self.cvcalllegratestatsmaxval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcalllegratestatsintvldurunits.yfilter != YFilter.not_set or
                    self.cvcalllegratestatsintvldur.yfilter != YFilter.not_set or
                    self.cvcalllegratestatsavgval.yfilter != YFilter.not_set or
                    self.cvcalllegratestatsmaxval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallLegRateStatsEntry" + "[cvCallLegRateStatsIntvlDurUnits='" + self.cvcalllegratestatsintvldurunits.get() + "']" + "[cvCallLegRateStatsIntvlDur='" + self.cvcalllegratestatsintvldur.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallLegRateStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcalllegratestatsintvldurunits.is_set or self.cvcalllegratestatsintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratestatsintvldurunits.get_name_leafdata())
                if (self.cvcalllegratestatsintvldur.is_set or self.cvcalllegratestatsintvldur.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratestatsintvldur.get_name_leafdata())
                if (self.cvcalllegratestatsavgval.is_set or self.cvcalllegratestatsavgval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratestatsavgval.get_name_leafdata())
                if (self.cvcalllegratestatsmaxval.is_set or self.cvcalllegratestatsmaxval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratestatsmaxval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallLegRateStatsIntvlDurUnits" or name == "cvCallLegRateStatsIntvlDur" or name == "cvCallLegRateStatsAvgVal" or name == "cvCallLegRateStatsMaxVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallLegRateStatsIntvlDurUnits"):
                    self.cvcalllegratestatsintvldurunits = value
                    self.cvcalllegratestatsintvldurunits.value_namespace = name_space
                    self.cvcalllegratestatsintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateStatsIntvlDur"):
                    self.cvcalllegratestatsintvldur = value
                    self.cvcalllegratestatsintvldur.value_namespace = name_space
                    self.cvcalllegratestatsintvldur.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateStatsAvgVal"):
                    self.cvcalllegratestatsavgval = value
                    self.cvcalllegratestatsavgval.value_namespace = name_space
                    self.cvcalllegratestatsavgval.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateStatsMaxVal"):
                    self.cvcalllegratestatsmaxval = value
                    self.cvcalllegratestatsmaxval.value_namespace = name_space
                    self.cvcalllegratestatsmaxval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcalllegratestatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcalllegratestatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallLegRateStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallLegRateStatsEntry"):
                for c in self.cvcalllegratestatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcalllegratestatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallLegRateStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvactivecallstatstable(Entity):
        """
        This table represents the active voice calls in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvactivecallstatsentry
        
        	This is a conceptual\-row in cvActiveCallStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of    :py:class:`Cvactivecallstatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvactivecallstatstable, self).__init__()

            self.yang_name = "cvActiveCallStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvactivecallstatsentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvactivecallstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvactivecallstatstable, self).__setattr__(name, value)


        class Cvactivecallstatsentry(Entity):
            """
            This is a conceptual\-row in cvActiveCallStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvactivecallstatsintvldurunits  <key>
            
            	The Object indexes in Active Call Rate Table (con\-current calls table) to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:   :py:class:`Cvcallvolumestatsintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumestatsintvltype>`
            
            .. attribute:: cvactivecallstatsintvldur  <key>
            
            	This is an index that references to the different past periods in given in interval of active call table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\:  int
            
            	**range:** 1..72
            
            .. attribute:: cvactivecallstatsavgval
            
            	This object indicates the average number of active calls that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvactivecallstatsmaxval
            
            	This object indicates the maximum number of active call that occured for the given period for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry, self).__init__()

                self.yang_name = "cvActiveCallStatsEntry"
                self.yang_parent_name = "cvActiveCallStatsTable"

                self.cvactivecallstatsintvldurunits = YLeaf(YType.enumeration, "cvActiveCallStatsIntvlDurUnits")

                self.cvactivecallstatsintvldur = YLeaf(YType.uint32, "cvActiveCallStatsIntvlDur")

                self.cvactivecallstatsavgval = YLeaf(YType.uint32, "cvActiveCallStatsAvgVal")

                self.cvactivecallstatsmaxval = YLeaf(YType.uint32, "cvActiveCallStatsMaxVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvactivecallstatsintvldurunits",
                                "cvactivecallstatsintvldur",
                                "cvactivecallstatsavgval",
                                "cvactivecallstatsmaxval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvactivecallstatsintvldurunits.is_set or
                    self.cvactivecallstatsintvldur.is_set or
                    self.cvactivecallstatsavgval.is_set or
                    self.cvactivecallstatsmaxval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvactivecallstatsintvldurunits.yfilter != YFilter.not_set or
                    self.cvactivecallstatsintvldur.yfilter != YFilter.not_set or
                    self.cvactivecallstatsavgval.yfilter != YFilter.not_set or
                    self.cvactivecallstatsmaxval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvActiveCallStatsEntry" + "[cvActiveCallStatsIntvlDurUnits='" + self.cvactivecallstatsintvldurunits.get() + "']" + "[cvActiveCallStatsIntvlDur='" + self.cvactivecallstatsintvldur.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvActiveCallStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvactivecallstatsintvldurunits.is_set or self.cvactivecallstatsintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallstatsintvldurunits.get_name_leafdata())
                if (self.cvactivecallstatsintvldur.is_set or self.cvactivecallstatsintvldur.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallstatsintvldur.get_name_leafdata())
                if (self.cvactivecallstatsavgval.is_set or self.cvactivecallstatsavgval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallstatsavgval.get_name_leafdata())
                if (self.cvactivecallstatsmaxval.is_set or self.cvactivecallstatsmaxval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallstatsmaxval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvActiveCallStatsIntvlDurUnits" or name == "cvActiveCallStatsIntvlDur" or name == "cvActiveCallStatsAvgVal" or name == "cvActiveCallStatsMaxVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvActiveCallStatsIntvlDurUnits"):
                    self.cvactivecallstatsintvldurunits = value
                    self.cvactivecallstatsintvldurunits.value_namespace = name_space
                    self.cvactivecallstatsintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallStatsIntvlDur"):
                    self.cvactivecallstatsintvldur = value
                    self.cvactivecallstatsintvldur.value_namespace = name_space
                    self.cvactivecallstatsintvldur.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallStatsAvgVal"):
                    self.cvactivecallstatsavgval = value
                    self.cvactivecallstatsavgval.value_namespace = name_space
                    self.cvactivecallstatsavgval.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallStatsMaxVal"):
                    self.cvactivecallstatsmaxval = value
                    self.cvactivecallstatsmaxval.value_namespace = name_space
                    self.cvactivecallstatsmaxval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvactivecallstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvactivecallstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvActiveCallStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvActiveCallStatsEntry"):
                for c in self.cvactivecallstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvactivecallstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvActiveCallStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcalldurationstatstable(Entity):
        """
        This table represents the number of calls below a specific
        duration in various interval length defined by 
        the CvCallVolumeStatsIntvlType object.  
        
        The specific duration is configurable value of 
         cvCallDurationStatsThreshold object.
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected.
        
        .. attribute:: cvcalldurationstatsentry
        
        	This is a conceptual\-row in cvCallDurationStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of    :py:class:`Cvcalldurationstatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcalldurationstatstable, self).__init__()

            self.yang_name = "cvCallDurationStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcalldurationstatsentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcalldurationstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcalldurationstatstable, self).__setattr__(name, value)


        class Cvcalldurationstatsentry(Entity):
            """
            This is a conceptual\-row in cvCallDurationStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalldurationstatsintvldurunits  <key>
            
            	The Object indexes in Call Duration Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:   :py:class:`Cvcallvolumestatsintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumestatsintvltype>`
            
            .. attribute:: cvcalldurationstatsintvldur  <key>
            
            	This is an index that references to the different past periods in given in interval of call Duration table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\:  int
            
            	**range:** 1..72
            
            .. attribute:: cvcalldurationstatsavgval
            
            	This object indicates the average number of calls having a duration which is below the threshold for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvcalldurationstatsmaxval
            
            	This object indicates the maximum number of calls having a duration which is below the threshold for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry, self).__init__()

                self.yang_name = "cvCallDurationStatsEntry"
                self.yang_parent_name = "cvCallDurationStatsTable"

                self.cvcalldurationstatsintvldurunits = YLeaf(YType.enumeration, "cvCallDurationStatsIntvlDurUnits")

                self.cvcalldurationstatsintvldur = YLeaf(YType.uint32, "cvCallDurationStatsIntvlDur")

                self.cvcalldurationstatsavgval = YLeaf(YType.uint32, "cvCallDurationStatsAvgVal")

                self.cvcalldurationstatsmaxval = YLeaf(YType.uint32, "cvCallDurationStatsMaxVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcalldurationstatsintvldurunits",
                                "cvcalldurationstatsintvldur",
                                "cvcalldurationstatsavgval",
                                "cvcalldurationstatsmaxval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcalldurationstatsintvldurunits.is_set or
                    self.cvcalldurationstatsintvldur.is_set or
                    self.cvcalldurationstatsavgval.is_set or
                    self.cvcalldurationstatsmaxval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcalldurationstatsintvldurunits.yfilter != YFilter.not_set or
                    self.cvcalldurationstatsintvldur.yfilter != YFilter.not_set or
                    self.cvcalldurationstatsavgval.yfilter != YFilter.not_set or
                    self.cvcalldurationstatsmaxval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallDurationStatsEntry" + "[cvCallDurationStatsIntvlDurUnits='" + self.cvcalldurationstatsintvldurunits.get() + "']" + "[cvCallDurationStatsIntvlDur='" + self.cvcalldurationstatsintvldur.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallDurationStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcalldurationstatsintvldurunits.is_set or self.cvcalldurationstatsintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalldurationstatsintvldurunits.get_name_leafdata())
                if (self.cvcalldurationstatsintvldur.is_set or self.cvcalldurationstatsintvldur.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalldurationstatsintvldur.get_name_leafdata())
                if (self.cvcalldurationstatsavgval.is_set or self.cvcalldurationstatsavgval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalldurationstatsavgval.get_name_leafdata())
                if (self.cvcalldurationstatsmaxval.is_set or self.cvcalldurationstatsmaxval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalldurationstatsmaxval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallDurationStatsIntvlDurUnits" or name == "cvCallDurationStatsIntvlDur" or name == "cvCallDurationStatsAvgVal" or name == "cvCallDurationStatsMaxVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallDurationStatsIntvlDurUnits"):
                    self.cvcalldurationstatsintvldurunits = value
                    self.cvcalldurationstatsintvldurunits.value_namespace = name_space
                    self.cvcalldurationstatsintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallDurationStatsIntvlDur"):
                    self.cvcalldurationstatsintvldur = value
                    self.cvcalldurationstatsintvldur.value_namespace = name_space
                    self.cvcalldurationstatsintvldur.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallDurationStatsAvgVal"):
                    self.cvcalldurationstatsavgval = value
                    self.cvcalldurationstatsavgval.value_namespace = name_space
                    self.cvcalldurationstatsavgval.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallDurationStatsMaxVal"):
                    self.cvcalldurationstatsmaxval = value
                    self.cvcalldurationstatsmaxval.value_namespace = name_space
                    self.cvcalldurationstatsmaxval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcalldurationstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcalldurationstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallDurationStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallDurationStatsEntry"):
                for c in self.cvcalldurationstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcalldurationstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallDurationStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvsipmsgratestatstable(Entity):
        """
        This table represents the SIP message rate measurement in
        various interval length defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratestatsentry
        
        	This is a conceptual\-row in cvSipMsgRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of    :py:class:`Cvsipmsgratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable, self).__init__()

            self.yang_name = "cvSipMsgRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvsipmsgratestatsentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable, self).__setattr__(name, value)


        class Cvsipmsgratestatsentry(Entity):
            """
            This is a conceptual\-row in cvSipMsgRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvsipmsgratestatsintvldurunits  <key>
            
            	The Object indexes in SIP Message Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:   :py:class:`Cvcallvolumestatsintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumestatsintvltype>`
            
            .. attribute:: cvsipmsgratestatsintvldur  <key>
            
            	This is an index that references to the different past periods in given in interval of SIP message rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\:  int
            
            	**range:** 1..72
            
            .. attribute:: cvsipmsgratestatsavgval
            
            	This object indicates the average SIP messages per second that is received for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            .. attribute:: cvsipmsgratestatsmaxval
            
            	This object indicates the maximum SIP messages  per second that is received for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry, self).__init__()

                self.yang_name = "cvSipMsgRateStatsEntry"
                self.yang_parent_name = "cvSipMsgRateStatsTable"

                self.cvsipmsgratestatsintvldurunits = YLeaf(YType.enumeration, "cvSipMsgRateStatsIntvlDurUnits")

                self.cvsipmsgratestatsintvldur = YLeaf(YType.uint32, "cvSipMsgRateStatsIntvlDur")

                self.cvsipmsgratestatsavgval = YLeaf(YType.uint32, "cvSipMsgRateStatsAvgVal")

                self.cvsipmsgratestatsmaxval = YLeaf(YType.uint32, "cvSipMsgRateStatsMaxVal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvsipmsgratestatsintvldurunits",
                                "cvsipmsgratestatsintvldur",
                                "cvsipmsgratestatsavgval",
                                "cvsipmsgratestatsmaxval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvsipmsgratestatsintvldurunits.is_set or
                    self.cvsipmsgratestatsintvldur.is_set or
                    self.cvsipmsgratestatsavgval.is_set or
                    self.cvsipmsgratestatsmaxval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvsipmsgratestatsintvldurunits.yfilter != YFilter.not_set or
                    self.cvsipmsgratestatsintvldur.yfilter != YFilter.not_set or
                    self.cvsipmsgratestatsavgval.yfilter != YFilter.not_set or
                    self.cvsipmsgratestatsmaxval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvSipMsgRateStatsEntry" + "[cvSipMsgRateStatsIntvlDurUnits='" + self.cvsipmsgratestatsintvldurunits.get() + "']" + "[cvSipMsgRateStatsIntvlDur='" + self.cvsipmsgratestatsintvldur.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvSipMsgRateStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvsipmsgratestatsintvldurunits.is_set or self.cvsipmsgratestatsintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratestatsintvldurunits.get_name_leafdata())
                if (self.cvsipmsgratestatsintvldur.is_set or self.cvsipmsgratestatsintvldur.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratestatsintvldur.get_name_leafdata())
                if (self.cvsipmsgratestatsavgval.is_set or self.cvsipmsgratestatsavgval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratestatsavgval.get_name_leafdata())
                if (self.cvsipmsgratestatsmaxval.is_set or self.cvsipmsgratestatsmaxval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratestatsmaxval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvSipMsgRateStatsIntvlDurUnits" or name == "cvSipMsgRateStatsIntvlDur" or name == "cvSipMsgRateStatsAvgVal" or name == "cvSipMsgRateStatsMaxVal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvSipMsgRateStatsIntvlDurUnits"):
                    self.cvsipmsgratestatsintvldurunits = value
                    self.cvsipmsgratestatsintvldurunits.value_namespace = name_space
                    self.cvsipmsgratestatsintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateStatsIntvlDur"):
                    self.cvsipmsgratestatsintvldur = value
                    self.cvsipmsgratestatsintvldur.value_namespace = name_space
                    self.cvsipmsgratestatsintvldur.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateStatsAvgVal"):
                    self.cvsipmsgratestatsavgval = value
                    self.cvsipmsgratestatsavgval.value_namespace = name_space
                    self.cvsipmsgratestatsavgval.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateStatsMaxVal"):
                    self.cvsipmsgratestatsmaxval = value
                    self.cvsipmsgratestatsmaxval.value_namespace = name_space
                    self.cvsipmsgratestatsmaxval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvsipmsgratestatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvsipmsgratestatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvSipMsgRateStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvSipMsgRateStatsEntry"):
                for c in self.cvsipmsgratestatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvsipmsgratestatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvSipMsgRateStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcallratewmtable(Entity):
        """
        This table represents high watermarks achieved
        by call rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcallratewmentry
        
        	This is a conceptual\-row in cvCallRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of    :py:class:`Cvcallratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcallratewmtable, self).__init__()

            self.yang_name = "cvCallRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcallratewmentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcallratewmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcallratewmtable, self).__setattr__(name, value)


        class Cvcallratewmentry(Entity):
            """
            This is a conceptual\-row in cvCallRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcallratewmintvldurunits  <key>
            
            	The Object indexes in call rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:   :py:class:`Cvcallvolumewmintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumewmintvltype>`
            
            .. attribute:: cvcallratewmindex  <key>
            
            	This is an index that references to different peaks in past period in call rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: cvcallratewmts
            
            	This object indicates date and Time when the high watermark is achieved for calls per second for the given interval
            	**type**\:  str
            
            .. attribute:: cvcallratewmvalue
            
            	This object indicates high watermark value achieved by the calls per second for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry, self).__init__()

                self.yang_name = "cvCallRateWMEntry"
                self.yang_parent_name = "cvCallRateWMTable"

                self.cvcallratewmintvldurunits = YLeaf(YType.enumeration, "cvCallRateWMIntvlDurUnits")

                self.cvcallratewmindex = YLeaf(YType.uint32, "cvCallRateWMIndex")

                self.cvcallratewmts = YLeaf(YType.str, "cvCallRateWMts")

                self.cvcallratewmvalue = YLeaf(YType.uint32, "cvCallRateWMValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcallratewmintvldurunits",
                                "cvcallratewmindex",
                                "cvcallratewmts",
                                "cvcallratewmvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcallratewmintvldurunits.is_set or
                    self.cvcallratewmindex.is_set or
                    self.cvcallratewmts.is_set or
                    self.cvcallratewmvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcallratewmintvldurunits.yfilter != YFilter.not_set or
                    self.cvcallratewmindex.yfilter != YFilter.not_set or
                    self.cvcallratewmts.yfilter != YFilter.not_set or
                    self.cvcallratewmvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallRateWMEntry" + "[cvCallRateWMIntvlDurUnits='" + self.cvcallratewmintvldurunits.get() + "']" + "[cvCallRateWMIndex='" + self.cvcallratewmindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallRateWMTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcallratewmintvldurunits.is_set or self.cvcallratewmintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratewmintvldurunits.get_name_leafdata())
                if (self.cvcallratewmindex.is_set or self.cvcallratewmindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratewmindex.get_name_leafdata())
                if (self.cvcallratewmts.is_set or self.cvcallratewmts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratewmts.get_name_leafdata())
                if (self.cvcallratewmvalue.is_set or self.cvcallratewmvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcallratewmvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallRateWMIntvlDurUnits" or name == "cvCallRateWMIndex" or name == "cvCallRateWMts" or name == "cvCallRateWMValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallRateWMIntvlDurUnits"):
                    self.cvcallratewmintvldurunits = value
                    self.cvcallratewmintvldurunits.value_namespace = name_space
                    self.cvcallratewmintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateWMIndex"):
                    self.cvcallratewmindex = value
                    self.cvcallratewmindex.value_namespace = name_space
                    self.cvcallratewmindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateWMts"):
                    self.cvcallratewmts = value
                    self.cvcallratewmts.value_namespace = name_space
                    self.cvcallratewmts.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallRateWMValue"):
                    self.cvcallratewmvalue = value
                    self.cvcallratewmvalue.value_namespace = name_space
                    self.cvcallratewmvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcallratewmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcallratewmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallRateWMTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallRateWMEntry"):
                for c in self.cvcallratewmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcallratewmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallRateWMEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcalllegratewmtable(Entity):
        """
        cvCallLegRateWMTable table represents high watermarks achieved
        by call\-leg rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcalllegratewmentry
        
        	This is a conceptual\-row in cvCallLegRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of    :py:class:`Cvcalllegratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvcalllegratewmtable, self).__init__()

            self.yang_name = "cvCallLegRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvcalllegratewmentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvcalllegratewmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvcalllegratewmtable, self).__setattr__(name, value)


        class Cvcalllegratewmentry(Entity):
            """
            This is a conceptual\-row in cvCallLegRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcalllegratewmintvldurunits  <key>
            
            	The Object indexes in call leg rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:   :py:class:`Cvcallvolumewmintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumewmintvltype>`
            
            .. attribute:: cvcalllegratewmindex  <key>
            
            	This is an index that references to different peaks in past period in call leg rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: cvcalllegratewmts
            
            	This object indicates date and time when the high watermark is achieved for call\-legs per second for the given interval
            	**type**\:  str
            
            .. attribute:: cvcalllegratewmvalue
            
            	This object indicates high watermark value achieved by the call legs per second for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: call legs per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry, self).__init__()

                self.yang_name = "cvCallLegRateWMEntry"
                self.yang_parent_name = "cvCallLegRateWMTable"

                self.cvcalllegratewmintvldurunits = YLeaf(YType.enumeration, "cvCallLegRateWMIntvlDurUnits")

                self.cvcalllegratewmindex = YLeaf(YType.uint32, "cvCallLegRateWMIndex")

                self.cvcalllegratewmts = YLeaf(YType.str, "cvCallLegRateWMts")

                self.cvcalllegratewmvalue = YLeaf(YType.uint32, "cvCallLegRateWMValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvcalllegratewmintvldurunits",
                                "cvcalllegratewmindex",
                                "cvcalllegratewmts",
                                "cvcalllegratewmvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvcalllegratewmintvldurunits.is_set or
                    self.cvcalllegratewmindex.is_set or
                    self.cvcalllegratewmts.is_set or
                    self.cvcalllegratewmvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvcalllegratewmintvldurunits.yfilter != YFilter.not_set or
                    self.cvcalllegratewmindex.yfilter != YFilter.not_set or
                    self.cvcalllegratewmts.yfilter != YFilter.not_set or
                    self.cvcalllegratewmvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCallLegRateWMEntry" + "[cvCallLegRateWMIntvlDurUnits='" + self.cvcalllegratewmintvldurunits.get() + "']" + "[cvCallLegRateWMIndex='" + self.cvcalllegratewmindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallLegRateWMTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvcalllegratewmintvldurunits.is_set or self.cvcalllegratewmintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratewmintvldurunits.get_name_leafdata())
                if (self.cvcalllegratewmindex.is_set or self.cvcalllegratewmindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratewmindex.get_name_leafdata())
                if (self.cvcalllegratewmts.is_set or self.cvcalllegratewmts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratewmts.get_name_leafdata())
                if (self.cvcalllegratewmvalue.is_set or self.cvcalllegratewmvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcalllegratewmvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvCallLegRateWMIntvlDurUnits" or name == "cvCallLegRateWMIndex" or name == "cvCallLegRateWMts" or name == "cvCallLegRateWMValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvCallLegRateWMIntvlDurUnits"):
                    self.cvcalllegratewmintvldurunits = value
                    self.cvcalllegratewmintvldurunits.value_namespace = name_space
                    self.cvcalllegratewmintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateWMIndex"):
                    self.cvcalllegratewmindex = value
                    self.cvcalllegratewmindex.value_namespace = name_space
                    self.cvcalllegratewmindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateWMts"):
                    self.cvcalllegratewmts = value
                    self.cvcalllegratewmts.value_namespace = name_space
                    self.cvcalllegratewmts.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCallLegRateWMValue"):
                    self.cvcalllegratewmvalue = value
                    self.cvcalllegratewmvalue.value_namespace = name_space
                    self.cvcalllegratewmvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcalllegratewmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcalllegratewmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCallLegRateWMTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCallLegRateWMEntry"):
                for c in self.cvcalllegratewmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcalllegratewmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCallLegRateWMEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvactivecallwmtable(Entity):
        """
        This table represents high watermarks achieved
        by active calls in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow 
        for detailed measurement to be collected.
        
        .. attribute:: cvactivecallwmentry
        
        	This is a conceptual\-row in cvActiveCallWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of    :py:class:`Cvactivecallwmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvactivecallwmtable, self).__init__()

            self.yang_name = "cvActiveCallWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvactivecallwmentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvactivecallwmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvactivecallwmtable, self).__setattr__(name, value)


        class Cvactivecallwmentry(Entity):
            """
            This is a conceptual\-row in cvActiveCallWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvactivecallwmintvldurunits  <key>
            
            	The Object indexes in active call Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:   :py:class:`Cvcallvolumewmintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumewmintvltype>`
            
            .. attribute:: cvactivecallwmindex  <key>
            
            	This is an index that references to different peaks in past period in acive call watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: cvactivecallwmts
            
            	This object indicates date and time when the high watermark is achieved for active calls for the given interval
            	**type**\:  str
            
            .. attribute:: cvactivecallwmvalue
            
            	This object indicates high watermark value achieved by the active calls for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry, self).__init__()

                self.yang_name = "cvActiveCallWMEntry"
                self.yang_parent_name = "cvActiveCallWMTable"

                self.cvactivecallwmintvldurunits = YLeaf(YType.enumeration, "cvActiveCallWMIntvlDurUnits")

                self.cvactivecallwmindex = YLeaf(YType.uint32, "cvActiveCallWMIndex")

                self.cvactivecallwmts = YLeaf(YType.str, "cvActiveCallWMts")

                self.cvactivecallwmvalue = YLeaf(YType.uint32, "cvActiveCallWMValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvactivecallwmintvldurunits",
                                "cvactivecallwmindex",
                                "cvactivecallwmts",
                                "cvactivecallwmvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvactivecallwmintvldurunits.is_set or
                    self.cvactivecallwmindex.is_set or
                    self.cvactivecallwmts.is_set or
                    self.cvactivecallwmvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvactivecallwmintvldurunits.yfilter != YFilter.not_set or
                    self.cvactivecallwmindex.yfilter != YFilter.not_set or
                    self.cvactivecallwmts.yfilter != YFilter.not_set or
                    self.cvactivecallwmvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvActiveCallWMEntry" + "[cvActiveCallWMIntvlDurUnits='" + self.cvactivecallwmintvldurunits.get() + "']" + "[cvActiveCallWMIndex='" + self.cvactivecallwmindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvActiveCallWMTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvactivecallwmintvldurunits.is_set or self.cvactivecallwmintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallwmintvldurunits.get_name_leafdata())
                if (self.cvactivecallwmindex.is_set or self.cvactivecallwmindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallwmindex.get_name_leafdata())
                if (self.cvactivecallwmts.is_set or self.cvactivecallwmts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallwmts.get_name_leafdata())
                if (self.cvactivecallwmvalue.is_set or self.cvactivecallwmvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvactivecallwmvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvActiveCallWMIntvlDurUnits" or name == "cvActiveCallWMIndex" or name == "cvActiveCallWMts" or name == "cvActiveCallWMValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvActiveCallWMIntvlDurUnits"):
                    self.cvactivecallwmintvldurunits = value
                    self.cvactivecallwmintvldurunits.value_namespace = name_space
                    self.cvactivecallwmintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallWMIndex"):
                    self.cvactivecallwmindex = value
                    self.cvactivecallwmindex.value_namespace = name_space
                    self.cvactivecallwmindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallWMts"):
                    self.cvactivecallwmts = value
                    self.cvactivecallwmts.value_namespace = name_space
                    self.cvactivecallwmts.value_namespace_prefix = name_space_prefix
                if(value_path == "cvActiveCallWMValue"):
                    self.cvactivecallwmvalue = value
                    self.cvactivecallwmvalue.value_namespace = name_space
                    self.cvactivecallwmvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvactivecallwmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvactivecallwmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvActiveCallWMTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvActiveCallWMEntry"):
                for c in self.cvactivecallwmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvactivecallwmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvActiveCallWMEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvsipmsgratewmtable(Entity):
        """
        This table represents of high watermarks achieved
        by SIP message rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratewmentry
        
        	This is a conceptual\-row in cvSipMsgRateWMTable. This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted if cvCallVolumeWMTableSize is changed
        	**type**\: list of    :py:class:`Cvsipmsgratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable, self).__init__()

            self.yang_name = "cvSipMsgRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"

            self.cvsipmsgratewmentry = YList(self)

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
                        super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable, self).__setattr__(name, value)


        class Cvsipmsgratewmentry(Entity):
            """
            This is a conceptual\-row in cvSipMsgRateWMTable.
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvsipmsgratewmintvldurunits  <key>
            
            	The Object indexes in SIP Message rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:   :py:class:`Cvcallvolumewmintvltype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.Cvcallvolumewmintvltype>`
            
            .. attribute:: cvsipmsgratewmindex  <key>
            
            	This is an index that references to different peaks in past period in sip message rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: cvsipmsgratewmts
            
            	This object indicates date and time when the high watermark is achieved for SIP messages per second for the given interval
            	**type**\:  str
            
            .. attribute:: cvsipmsgratewmvalue
            
            	This object indicates high watermark value achieved by the SIP messages per second for the given interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry, self).__init__()

                self.yang_name = "cvSipMsgRateWMEntry"
                self.yang_parent_name = "cvSipMsgRateWMTable"

                self.cvsipmsgratewmintvldurunits = YLeaf(YType.enumeration, "cvSipMsgRateWMIntvlDurUnits")

                self.cvsipmsgratewmindex = YLeaf(YType.uint32, "cvSipMsgRateWMIndex")

                self.cvsipmsgratewmts = YLeaf(YType.str, "cvSipMsgRateWMts")

                self.cvsipmsgratewmvalue = YLeaf(YType.uint32, "cvSipMsgRateWMValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvsipmsgratewmintvldurunits",
                                "cvsipmsgratewmindex",
                                "cvsipmsgratewmts",
                                "cvsipmsgratewmvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvsipmsgratewmintvldurunits.is_set or
                    self.cvsipmsgratewmindex.is_set or
                    self.cvsipmsgratewmts.is_set or
                    self.cvsipmsgratewmvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvsipmsgratewmintvldurunits.yfilter != YFilter.not_set or
                    self.cvsipmsgratewmindex.yfilter != YFilter.not_set or
                    self.cvsipmsgratewmts.yfilter != YFilter.not_set or
                    self.cvsipmsgratewmvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvSipMsgRateWMEntry" + "[cvSipMsgRateWMIntvlDurUnits='" + self.cvsipmsgratewmintvldurunits.get() + "']" + "[cvSipMsgRateWMIndex='" + self.cvsipmsgratewmindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvSipMsgRateWMTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvsipmsgratewmintvldurunits.is_set or self.cvsipmsgratewmintvldurunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratewmintvldurunits.get_name_leafdata())
                if (self.cvsipmsgratewmindex.is_set or self.cvsipmsgratewmindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratewmindex.get_name_leafdata())
                if (self.cvsipmsgratewmts.is_set or self.cvsipmsgratewmts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratewmts.get_name_leafdata())
                if (self.cvsipmsgratewmvalue.is_set or self.cvsipmsgratewmvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvsipmsgratewmvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvSipMsgRateWMIntvlDurUnits" or name == "cvSipMsgRateWMIndex" or name == "cvSipMsgRateWMts" or name == "cvSipMsgRateWMValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvSipMsgRateWMIntvlDurUnits"):
                    self.cvsipmsgratewmintvldurunits = value
                    self.cvsipmsgratewmintvldurunits.value_namespace = name_space
                    self.cvsipmsgratewmintvldurunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateWMIndex"):
                    self.cvsipmsgratewmindex = value
                    self.cvsipmsgratewmindex.value_namespace = name_space
                    self.cvsipmsgratewmindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateWMts"):
                    self.cvsipmsgratewmts = value
                    self.cvsipmsgratewmts.value_namespace = name_space
                    self.cvsipmsgratewmts.value_namespace_prefix = name_space_prefix
                if(value_path == "cvSipMsgRateWMValue"):
                    self.cvsipmsgratewmvalue = value
                    self.cvsipmsgratewmvalue.value_namespace = name_space
                    self.cvsipmsgratewmvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvsipmsgratewmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvsipmsgratewmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvSipMsgRateWMTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvSipMsgRateWMEntry"):
                for c in self.cvsipmsgratewmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvsipmsgratewmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvSipMsgRateWMEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cvactivecallstatstable is not None and self.cvactivecallstatstable.has_data()) or
            (self.cvactivecallwmtable is not None and self.cvactivecallwmtable.has_data()) or
            (self.cvcallactivetable is not None and self.cvcallactivetable.has_data()) or
            (self.cvcalldurationstatstable is not None and self.cvcalldurationstatstable.has_data()) or
            (self.cvcallhistorytable is not None and self.cvcallhistorytable.has_data()) or
            (self.cvcalllegratestatstable is not None and self.cvcalllegratestatstable.has_data()) or
            (self.cvcalllegratewmtable is not None and self.cvcalllegratewmtable.has_data()) or
            (self.cvcallratemonitor is not None and self.cvcallratemonitor.has_data()) or
            (self.cvcallratestatstable is not None and self.cvcallratestatstable.has_data()) or
            (self.cvcallratewmtable is not None and self.cvcallratewmtable.has_data()) or
            (self.cvcallvolconntable is not None and self.cvcallvolconntable.has_data()) or
            (self.cvcallvoliftable is not None and self.cvcallvoliftable.has_data()) or
            (self.cvcallvolume is not None and self.cvcallvolume.has_data()) or
            (self.cvcallvolumestatshistory is not None and self.cvcallvolumestatshistory.has_data()) or
            (self.cvgatewaycallactive is not None and self.cvgatewaycallactive.has_data()) or
            (self.cvgeneralconfiguration is not None and self.cvgeneralconfiguration.has_data()) or
            (self.cvpeercfgtable is not None and self.cvpeercfgtable.has_data()) or
            (self.cvpeercommoncfgtable is not None and self.cvpeercommoncfgtable.has_data()) or
            (self.cvsipmsgratestatstable is not None and self.cvsipmsgratestatstable.has_data()) or
            (self.cvsipmsgratewmtable is not None and self.cvsipmsgratewmtable.has_data()) or
            (self.cvvoicepeercfgtable is not None and self.cvvoicepeercfgtable.has_data()) or
            (self.cvvoipcallactivetable is not None and self.cvvoipcallactivetable.has_data()) or
            (self.cvvoipcallhistorytable is not None and self.cvvoipcallhistorytable.has_data()) or
            (self.cvvoippeercfgtable is not None and self.cvvoippeercfgtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cvactivecallstatstable is not None and self.cvactivecallstatstable.has_operation()) or
            (self.cvactivecallwmtable is not None and self.cvactivecallwmtable.has_operation()) or
            (self.cvcallactivetable is not None and self.cvcallactivetable.has_operation()) or
            (self.cvcalldurationstatstable is not None and self.cvcalldurationstatstable.has_operation()) or
            (self.cvcallhistorytable is not None and self.cvcallhistorytable.has_operation()) or
            (self.cvcalllegratestatstable is not None and self.cvcalllegratestatstable.has_operation()) or
            (self.cvcalllegratewmtable is not None and self.cvcalllegratewmtable.has_operation()) or
            (self.cvcallratemonitor is not None and self.cvcallratemonitor.has_operation()) or
            (self.cvcallratestatstable is not None and self.cvcallratestatstable.has_operation()) or
            (self.cvcallratewmtable is not None and self.cvcallratewmtable.has_operation()) or
            (self.cvcallvolconntable is not None and self.cvcallvolconntable.has_operation()) or
            (self.cvcallvoliftable is not None and self.cvcallvoliftable.has_operation()) or
            (self.cvcallvolume is not None and self.cvcallvolume.has_operation()) or
            (self.cvcallvolumestatshistory is not None and self.cvcallvolumestatshistory.has_operation()) or
            (self.cvgatewaycallactive is not None and self.cvgatewaycallactive.has_operation()) or
            (self.cvgeneralconfiguration is not None and self.cvgeneralconfiguration.has_operation()) or
            (self.cvpeercfgtable is not None and self.cvpeercfgtable.has_operation()) or
            (self.cvpeercommoncfgtable is not None and self.cvpeercommoncfgtable.has_operation()) or
            (self.cvsipmsgratestatstable is not None and self.cvsipmsgratestatstable.has_operation()) or
            (self.cvsipmsgratewmtable is not None and self.cvsipmsgratewmtable.has_operation()) or
            (self.cvvoicepeercfgtable is not None and self.cvvoicepeercfgtable.has_operation()) or
            (self.cvvoipcallactivetable is not None and self.cvvoipcallactivetable.has_operation()) or
            (self.cvvoipcallhistorytable is not None and self.cvvoipcallhistorytable.has_operation()) or
            (self.cvvoippeercfgtable is not None and self.cvvoippeercfgtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB" + path_buffer

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

        if (child_yang_name == "cvActiveCallStatsTable"):
            if (self.cvactivecallstatstable is None):
                self.cvactivecallstatstable = CiscoVoiceDialControlMib.Cvactivecallstatstable()
                self.cvactivecallstatstable.parent = self
                self._children_name_map["cvactivecallstatstable"] = "cvActiveCallStatsTable"
            return self.cvactivecallstatstable

        if (child_yang_name == "cvActiveCallWMTable"):
            if (self.cvactivecallwmtable is None):
                self.cvactivecallwmtable = CiscoVoiceDialControlMib.Cvactivecallwmtable()
                self.cvactivecallwmtable.parent = self
                self._children_name_map["cvactivecallwmtable"] = "cvActiveCallWMTable"
            return self.cvactivecallwmtable

        if (child_yang_name == "cvCallActiveTable"):
            if (self.cvcallactivetable is None):
                self.cvcallactivetable = CiscoVoiceDialControlMib.Cvcallactivetable()
                self.cvcallactivetable.parent = self
                self._children_name_map["cvcallactivetable"] = "cvCallActiveTable"
            return self.cvcallactivetable

        if (child_yang_name == "cvCallDurationStatsTable"):
            if (self.cvcalldurationstatstable is None):
                self.cvcalldurationstatstable = CiscoVoiceDialControlMib.Cvcalldurationstatstable()
                self.cvcalldurationstatstable.parent = self
                self._children_name_map["cvcalldurationstatstable"] = "cvCallDurationStatsTable"
            return self.cvcalldurationstatstable

        if (child_yang_name == "cvCallHistoryTable"):
            if (self.cvcallhistorytable is None):
                self.cvcallhistorytable = CiscoVoiceDialControlMib.Cvcallhistorytable()
                self.cvcallhistorytable.parent = self
                self._children_name_map["cvcallhistorytable"] = "cvCallHistoryTable"
            return self.cvcallhistorytable

        if (child_yang_name == "cvCallLegRateStatsTable"):
            if (self.cvcalllegratestatstable is None):
                self.cvcalllegratestatstable = CiscoVoiceDialControlMib.Cvcalllegratestatstable()
                self.cvcalllegratestatstable.parent = self
                self._children_name_map["cvcalllegratestatstable"] = "cvCallLegRateStatsTable"
            return self.cvcalllegratestatstable

        if (child_yang_name == "cvCallLegRateWMTable"):
            if (self.cvcalllegratewmtable is None):
                self.cvcalllegratewmtable = CiscoVoiceDialControlMib.Cvcalllegratewmtable()
                self.cvcalllegratewmtable.parent = self
                self._children_name_map["cvcalllegratewmtable"] = "cvCallLegRateWMTable"
            return self.cvcalllegratewmtable

        if (child_yang_name == "cvCallRateMonitor"):
            if (self.cvcallratemonitor is None):
                self.cvcallratemonitor = CiscoVoiceDialControlMib.Cvcallratemonitor()
                self.cvcallratemonitor.parent = self
                self._children_name_map["cvcallratemonitor"] = "cvCallRateMonitor"
            return self.cvcallratemonitor

        if (child_yang_name == "cvCallRateStatsTable"):
            if (self.cvcallratestatstable is None):
                self.cvcallratestatstable = CiscoVoiceDialControlMib.Cvcallratestatstable()
                self.cvcallratestatstable.parent = self
                self._children_name_map["cvcallratestatstable"] = "cvCallRateStatsTable"
            return self.cvcallratestatstable

        if (child_yang_name == "cvCallRateWMTable"):
            if (self.cvcallratewmtable is None):
                self.cvcallratewmtable = CiscoVoiceDialControlMib.Cvcallratewmtable()
                self.cvcallratewmtable.parent = self
                self._children_name_map["cvcallratewmtable"] = "cvCallRateWMTable"
            return self.cvcallratewmtable

        if (child_yang_name == "cvCallVolConnTable"):
            if (self.cvcallvolconntable is None):
                self.cvcallvolconntable = CiscoVoiceDialControlMib.Cvcallvolconntable()
                self.cvcallvolconntable.parent = self
                self._children_name_map["cvcallvolconntable"] = "cvCallVolConnTable"
            return self.cvcallvolconntable

        if (child_yang_name == "cvCallVolIfTable"):
            if (self.cvcallvoliftable is None):
                self.cvcallvoliftable = CiscoVoiceDialControlMib.Cvcallvoliftable()
                self.cvcallvoliftable.parent = self
                self._children_name_map["cvcallvoliftable"] = "cvCallVolIfTable"
            return self.cvcallvoliftable

        if (child_yang_name == "cvCallVolume"):
            if (self.cvcallvolume is None):
                self.cvcallvolume = CiscoVoiceDialControlMib.Cvcallvolume()
                self.cvcallvolume.parent = self
                self._children_name_map["cvcallvolume"] = "cvCallVolume"
            return self.cvcallvolume

        if (child_yang_name == "cvCallVolumeStatsHistory"):
            if (self.cvcallvolumestatshistory is None):
                self.cvcallvolumestatshistory = CiscoVoiceDialControlMib.Cvcallvolumestatshistory()
                self.cvcallvolumestatshistory.parent = self
                self._children_name_map["cvcallvolumestatshistory"] = "cvCallVolumeStatsHistory"
            return self.cvcallvolumestatshistory

        if (child_yang_name == "cvGatewayCallActive"):
            if (self.cvgatewaycallactive is None):
                self.cvgatewaycallactive = CiscoVoiceDialControlMib.Cvgatewaycallactive()
                self.cvgatewaycallactive.parent = self
                self._children_name_map["cvgatewaycallactive"] = "cvGatewayCallActive"
            return self.cvgatewaycallactive

        if (child_yang_name == "cvGeneralConfiguration"):
            if (self.cvgeneralconfiguration is None):
                self.cvgeneralconfiguration = CiscoVoiceDialControlMib.Cvgeneralconfiguration()
                self.cvgeneralconfiguration.parent = self
                self._children_name_map["cvgeneralconfiguration"] = "cvGeneralConfiguration"
            return self.cvgeneralconfiguration

        if (child_yang_name == "cvPeerCfgTable"):
            if (self.cvpeercfgtable is None):
                self.cvpeercfgtable = CiscoVoiceDialControlMib.Cvpeercfgtable()
                self.cvpeercfgtable.parent = self
                self._children_name_map["cvpeercfgtable"] = "cvPeerCfgTable"
            return self.cvpeercfgtable

        if (child_yang_name == "cvPeerCommonCfgTable"):
            if (self.cvpeercommoncfgtable is None):
                self.cvpeercommoncfgtable = CiscoVoiceDialControlMib.Cvpeercommoncfgtable()
                self.cvpeercommoncfgtable.parent = self
                self._children_name_map["cvpeercommoncfgtable"] = "cvPeerCommonCfgTable"
            return self.cvpeercommoncfgtable

        if (child_yang_name == "cvSipMsgRateStatsTable"):
            if (self.cvsipmsgratestatstable is None):
                self.cvsipmsgratestatstable = CiscoVoiceDialControlMib.Cvsipmsgratestatstable()
                self.cvsipmsgratestatstable.parent = self
                self._children_name_map["cvsipmsgratestatstable"] = "cvSipMsgRateStatsTable"
            return self.cvsipmsgratestatstable

        if (child_yang_name == "cvSipMsgRateWMTable"):
            if (self.cvsipmsgratewmtable is None):
                self.cvsipmsgratewmtable = CiscoVoiceDialControlMib.Cvsipmsgratewmtable()
                self.cvsipmsgratewmtable.parent = self
                self._children_name_map["cvsipmsgratewmtable"] = "cvSipMsgRateWMTable"
            return self.cvsipmsgratewmtable

        if (child_yang_name == "cvVoicePeerCfgTable"):
            if (self.cvvoicepeercfgtable is None):
                self.cvvoicepeercfgtable = CiscoVoiceDialControlMib.Cvvoicepeercfgtable()
                self.cvvoicepeercfgtable.parent = self
                self._children_name_map["cvvoicepeercfgtable"] = "cvVoicePeerCfgTable"
            return self.cvvoicepeercfgtable

        if (child_yang_name == "cvVoIPCallActiveTable"):
            if (self.cvvoipcallactivetable is None):
                self.cvvoipcallactivetable = CiscoVoiceDialControlMib.Cvvoipcallactivetable()
                self.cvvoipcallactivetable.parent = self
                self._children_name_map["cvvoipcallactivetable"] = "cvVoIPCallActiveTable"
            return self.cvvoipcallactivetable

        if (child_yang_name == "cvVoIPCallHistoryTable"):
            if (self.cvvoipcallhistorytable is None):
                self.cvvoipcallhistorytable = CiscoVoiceDialControlMib.Cvvoipcallhistorytable()
                self.cvvoipcallhistorytable.parent = self
                self._children_name_map["cvvoipcallhistorytable"] = "cvVoIPCallHistoryTable"
            return self.cvvoipcallhistorytable

        if (child_yang_name == "cvVoIPPeerCfgTable"):
            if (self.cvvoippeercfgtable is None):
                self.cvvoippeercfgtable = CiscoVoiceDialControlMib.Cvvoippeercfgtable()
                self.cvvoippeercfgtable.parent = self
                self._children_name_map["cvvoippeercfgtable"] = "cvVoIPPeerCfgTable"
            return self.cvvoippeercfgtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cvActiveCallStatsTable" or name == "cvActiveCallWMTable" or name == "cvCallActiveTable" or name == "cvCallDurationStatsTable" or name == "cvCallHistoryTable" or name == "cvCallLegRateStatsTable" or name == "cvCallLegRateWMTable" or name == "cvCallRateMonitor" or name == "cvCallRateStatsTable" or name == "cvCallRateWMTable" or name == "cvCallVolConnTable" or name == "cvCallVolIfTable" or name == "cvCallVolume" or name == "cvCallVolumeStatsHistory" or name == "cvGatewayCallActive" or name == "cvGeneralConfiguration" or name == "cvPeerCfgTable" or name == "cvPeerCommonCfgTable" or name == "cvSipMsgRateStatsTable" or name == "cvSipMsgRateWMTable" or name == "cvVoicePeerCfgTable" or name == "cvVoIPCallActiveTable" or name == "cvVoIPCallHistoryTable" or name == "cvVoIPPeerCfgTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVoiceDialControlMib()
        return self._top_entity

